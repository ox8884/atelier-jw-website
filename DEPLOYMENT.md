# Deployment and custom-domain guide

## Current status

- Production domain: `atelier-jw.com`
- Registration date: 2026-08-20
- Current nameservers:
  - `ns1.systemdns.com`
  - `ns2.systemdns.com`
  - `ns3.systemdns.com`
- GitHub repository: https://github.com/ox8884/atelier-jw-website
- Live preview: https://ox8884.github.io/atelier-jw-website/
- Cloudflare authentication: not configured yet

## Recommended production setup

Use Cloudflare Pages Free. Keep the domain registration with Bizee and change only the nameservers after the Cloudflare zone is ready.

### 1. Create the Cloudflare zone

1. Sign in or create an account at https://dash.cloudflare.com.
2. Choose **Add a domain** and enter `atelier-jw.com`.
3. Select the Free plan.
4. Let Cloudflare scan existing DNS records.
5. Before changing nameservers, confirm that any email-related `MX`, `TXT`, SPF, DKIM, or verification records were imported.
6. Copy the two Cloudflare nameservers assigned to the domain.

### 2. Update nameservers at Bizee

1. Open the Bizee domain dashboard for `atelier-jw.com`.
2. Find Domain settings, DNS, or Nameservers.
3. Choose custom nameservers.
4. Replace the three `systemdns.com` nameservers with the two assigned by Cloudflare.
5. Save and wait for DNS propagation. It can be quick but may take up to 24-48 hours.

Do not change nameservers before Cloudflare has added the zone and imported any email records.

### 3. Create the Cloudflare Pages project

1. Open **Workers & Pages** in Cloudflare.
2. Create a Pages project and connect GitHub.
3. Select `ox8884/atelier-jw-website`.
4. Framework preset: None.
5. Build command: leave blank.
6. Build output directory: repository root (`/` or `.` as accepted by the UI).
7. Deploy.

### 4. Attach the custom domain

1. In the Pages project, open **Custom domains**.
2. Add `atelier-jw.com`.
3. Add `www.atelier-jw.com`.
4. Set the preferred canonical host to `atelier-jw.com` and redirect `www` to the apex domain if Cloudflare does not do so automatically.
5. Wait for the Cloudflare SSL certificate to become active.

### 5. Verify

- `https://atelier-jw.com` loads without a certificate warning.
- `https://www.atelier-jw.com` redirects or serves the same site.
- Mobile and desktop render correctly.
- Contact links open the email client.
- Existing email, if configured later, has valid MX and SPF/DKIM records.

## Future updates

Push changes to the `main` branch. Cloudflare Pages will redeploy automatically when connected to GitHub.
