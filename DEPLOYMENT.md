# Deployment and custom-domain guide

## Production status

- Production: https://atelier-jw.com
- Alternate host: https://www.atelier-jw.com
- Cloudflare Pages: https://atelier-jw.pages.dev
- GitHub: https://github.com/ox8884/atelier-jw-website
- Cloudflare project: `atelier-jw`
- Nameservers: `arya.ns.cloudflare.com`, `jay.ns.cloudflare.com`
- DNS zone: active
- HTTPS: active on root and www
- Email DNS preserved: MX, SPF, DMARC

## DNS architecture

Bizee remains the domain registrar. Cloudflare is the authoritative DNS provider and Pages host. Do not request a transfer code unless intentionally moving the domain registration away from Bizee.

Website records:

- CNAME `@` -> `atelier-jw.pages.dev` (proxied)
- CNAME `www` -> `atelier-jw.pages.dev` (proxied)

Email records retained:

- MX `atelier-jw.com` -> `mx.atelier-jw.com.cust.hostedemail.com` priority 10
- TXT SPF -> `v=spf1 include:_spf.hostedemail.com ~all`
- TXT DMARC `_dmarc` -> `v=DMARC1; p=none; rua=mailto:jayheo8884@gmail.com`

## Safe deployment

Never run `wrangler pages deploy .` from the repository root. That can upload `.git`, test reports, and unrelated files.

Use the allowlist deployment script:

```bash
python scripts/deploy_cloudflare.py
```

The script creates a temporary directory containing only these public files:

- index.html
- styles.css
- script.js
- robots.txt
- sitemap.xml
- _headers
- five optimized WebP images
- concepts/index.html
- concepts/clear/index.html
- concepts/warm/index.html
- concepts/bold/index.html
- concepts/museum/index.html

It reads the existing Wrangler OAuth credential without printing it, deploys the allowlist, and removes only its own temporary directory when finished.

## Verification

After every deployment:

```bash
curl -fsSI https://atelier-jw.com/
curl -fsSI https://www.atelier-jw.com/
```

Expected: HTTP 200, Cloudflare server header, CSP and security headers present.

Sensitive-path checks must return the homepage fallback, not repository contents:

```bash
curl -fsS https://atelier-jw.com/.git/config
curl -fsS https://atelier-jw.com/.lighthouse-tmp/production.json
```

The response should start with `<!doctype html>`, never Git configuration or JSON.

## Quality baseline

Production Lighthouse after deployment:

- Performance: 98
- Accessibility: 100
- Best Practices: 100
- SEO: 100
- LCP: 1.8 s
- TBT: 0 ms
- CLS: 0
