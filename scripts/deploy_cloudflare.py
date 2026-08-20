from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = "atelier-jw"
ACCOUNT_ID = "6c9a027f1f7b30461dc3f80864fb61f2"
PUBLIC_FILES = ["index.html", "styles.css", "script.js", "robots.txt", "sitemap.xml", "_headers"]
PUBLIC_ASSETS = [
    "hero-desktop.webp",
    "hero-mobile.webp",
    "forge-kitchen.webp",
    "bakery-hands.webp",
    "cafe-interior.webp",
]


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
    missing = [name for name in PUBLIC_FILES if not (ROOT / name).is_file()]
    missing += [f"assets/{name}" for name in PUBLIC_ASSETS if not (ROOT / "assets" / name).is_file()]
    if missing:
        raise SystemExit(f"Missing public files: {', '.join(missing)}")

    token = oauth_token()
    if not token:
        raise SystemExit("Cloudflare credentials not found. Run: npx wrangler login --device --browser=false")

    with tempfile.TemporaryDirectory(prefix="atelier-jw-deploy-") as temp:
        out = Path(temp)
        for name in PUBLIC_FILES:
            shutil.copy2(ROOT / name, out / name)
        assets = out / "assets"
        assets.mkdir()
        for name in PUBLIC_ASSETS:
            shutil.copy2(ROOT / "assets" / name, assets / name)

        files = [path for path in out.rglob("*") if path.is_file()]
        print(f"Deploying {len(files)} allowlisted public files.")
        env = os.environ.copy()
        env["CLOUDFLARE_API_TOKEN"] = token
        env["CLOUDFLARE_ACCOUNT_ID"] = ACCOUNT_ID
        npx = shutil.which("npx") or shutil.which("npx.cmd")
        if not npx:
            raise SystemExit("npx not found")
        subprocess.run(
            [npx, "--yes", "wrangler", "pages", "deploy", str(out), "--project-name", PROJECT, "--branch", "main"],
            check=True,
            env=env,
        )


if __name__ == "__main__":
    main()
