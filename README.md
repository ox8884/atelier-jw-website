# Atelier JW website

Premium static company site for Atelier JW LLC and its growing brand portfolio.

## Local preview

```bash
python -m http.server 4173
```

Open `http://localhost:4173`.

## Deployment

Production: https://atelier-jw.com

Cloudflare Pages fallback: https://atelier-jw.pages.dev

GitHub: https://github.com/ox8884/atelier-jw-website

Deploy only through the allowlist script. Never deploy the repository root directly.

```bash
python scripts/deploy_cloudflare.py
```

See `DEPLOYMENT.md` for DNS, security, and verification details.

## Redesign concepts

Earlier redesign drafts live in `concepts/` for reference. They are not published; open them locally (for example `python -m http.server` and visit `/concepts/`).

## Custom domain

Production domain: `atelier-jw.com`

Live preview: https://ox8884.github.io/atelier-jw-website/

GitHub repository: https://github.com/ox8884/atelier-jw-website

For Cloudflare Pages:

1. Create a Pages project from this Git repository.
2. Leave build command blank.
3. Set output directory to `/` or the repository root.
4. Add `atelier-jw.com` and `www.atelier-jw.com` under Custom domains.
5. Follow Cloudflare's DNS instructions. Preserve any MX records used for email.

## Photography

The published photographs are illustrative images generated with a GPT image model in November 2026. They set a mood; they do not show actual Forge Kitchen products or a real café location, and the footer says so. Each file carries its generation prompt (PNG metadata, or a `.json` sidecar next to a `.webp`).

Fonts (Castoro, Red Hat Text) are self-hosted from `assets/fonts/` under the SIL Open Font License.

Earlier Unsplash photographs remain in `assets/` for reference and are no longer published:

- Ceramic still life: https://unsplash.com/photos/Rzwc4pyNYP8
- Green kitchen: https://unsplash.com/photos/qkGabQMHfNA
- Bread making: https://unsplash.com/photos/6Fa9E8r5_90
- Café interior: https://unsplash.com/photos/8705DdIrKtE

## Privacy

The site uses no forms or advertising trackers. Cloudflare Web Analytics is injected by the hosting platform for privacy-focused aggregate performance and traffic measurement. Contact links open the user's email client.
