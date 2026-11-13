from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = "atelier-jw"
ACCOUNT_ID = "6c9a027f1f7b30461dc3f80864fb61f2"
PUBLIC_FILES = ["index.html", "robots.txt", "sitemap.xml", "_headers"]
# Published as assets/<name>.<hash>.<ext> alongside the photos (same immutable cache rule).
HASHED_ROOT_FILES = ["styles.css", "script.js"]
# Assets are served with an immutable 1-year cache, so they are published under
# content-hashed names (photo.1a2b3c4d.webp) and index.html is rewritten to match.
# Replacing a photo in place is therefore safe: its published name changes.
PUBLIC_ASSETS = [
    "og-image.jpg",
    "photo-desserts.webp",
    "photo-pot.webp",
    "photo-cafe.webp",
    "photo-forge.webp",
    "photo-bakery.webp",
    "photo-cafe-corner.webp",
    "photo-table.webp",
    # PNG fallbacks behind the <picture> webp sources.
    "plates/photo-desserts.png",
    "plates/photo-pot.png",
    "plates/photo-cafe.png",
    "fonts/castoro.woff2",
    "fonts/red-hat-text.woff2",
]


def hashed_name(name: str, data: bytes) -> str:
    """photo.webp -> photo.1a2b3c4d.webp; keeps a leading folder (fonts/x.woff2)."""
    digest = hashlib.sha256(data).hexdigest()[:8]
    stem, _, ext = name.rpartition(".")
    return f"{stem}.{digest}.{ext}"


def oauth_token() -> str | None:
    if os.environ.get("CLOUDFLARE_API_TOKEN"):
        return os.environ["CLOUDFLARE_API_TOKEN"]
    candidates = [
        Path.home() / ".wrangler" / "config" / "default.toml",
        Path(os.environ.get("APPDATA", "")) / "xdg.config" / ".wrangler" / "config" / "default.toml",
    ]
    for path in candidates:
        if path.is_file():
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            if data.get("oauth_token"):
                return str(data["oauth_token"])
    return None


def main() -> None:
    missing = [name for name in PUBLIC_FILES + HASHED_ROOT_FILES if not (ROOT / name).is_file()]
    missing += [f"assets/{name}" for name in PUBLIC_ASSETS if not (ROOT / "assets" / name).is_file()]
    if missing:
        raise SystemExit(f"Missing public files: {', '.join(missing)}")

    dry_run = "--dry-run" in sys.argv
    if not dry_run and not (ROOT / "node_modules" / "wrangler" / "package.json").is_file():
        raise SystemExit("wrangler is not installed. Run: npm ci")
    token = None if dry_run else oauth_token()
    if not dry_run and not token:
        raise SystemExit("Cloudflare credentials not found. Run: npx wrangler login --device --browser=false")

    with tempfile.TemporaryDirectory(prefix="atelier-jw-deploy-") as temp:
        out = Path(temp)
        for name in PUBLIC_FILES:
            shutil.copy2(ROOT / name, out / name)
        assets = out / "assets"
        assets.mkdir()
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        css = (ROOT / "styles.css").read_text(encoding="utf-8")
        for name in PUBLIC_ASSETS:
            published = hashed_name(name, (ROOT / "assets" / name).read_bytes())
            (assets / published).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / "assets" / name, assets / published)
            html = html.replace(f"assets/{name}", f"assets/{published}")
            # The stylesheet is published inside assets/, so its paths lose the folder.
            css = css.replace(f"assets/{name}", published)
        if "assets/" in css:
            raise SystemExit("styles.css references an asset that is not in PUBLIC_ASSETS")
        for name in HASHED_ROOT_FILES:
            data = css.encode("utf-8") if name == "styles.css" else (ROOT / name).read_bytes()
            published = hashed_name(name, data)
            (assets / published).write_bytes(data)
            if html.count(f'"{name}"') != 1:
                raise SystemExit(f"Expected exactly one reference to {name} in index.html")
            html = html.replace(f'"{name}"', f'"assets/{published}"')
        broken = [ref for ref in re.findall(r"assets/[\w./-]+", html) if not (out / ref).is_file()]
        if broken:
            raise SystemExit(f"index.html references unpublished assets: {', '.join(sorted(set(broken)))}")
        (out / "index.html").write_text(html, encoding="utf-8")

        files = [path for path in out.rglob("*") if path.is_file()]
        if dry_run:
            print("\n".join(sorted(path.relative_to(out).as_posix() for path in files)))
            return
        print(f"Deploying {len(files)} allowlisted public files.")
        env = os.environ.copy()
        env["CLOUDFLARE_API_TOKEN"] = token
        env["CLOUDFLARE_ACCOUNT_ID"] = ACCOUNT_ID
        npx = shutil.which("npx") or shutil.which("npx.cmd")
        if not npx:
            raise SystemExit("npx not found")
        subprocess.run(
            # --no: use the wrangler pinned in package.json, never fetch another version
            [npx, "--no", "--", "wrangler", "pages", "deploy", str(out), "--project-name", PROJECT, "--branch", "main"],
            check=True,
            cwd=ROOT,
            env=env,
        )


if __name__ == "__main__":
    main()
