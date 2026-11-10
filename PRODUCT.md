# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

No single primary audience (confirmed by the owner, 2026-11-09). The site is the company's face for everyone who looks it up: marketplaces, banks and suppliers checking that the company is real; future Forge Kitchen customers; partners, wholesale buyers and press. All of them arrive cold, usually from a search or a link in an email, and stay for one visit.

## Product Purpose

atelier-jw.com is the one-page company site for Atelier JW LLC. It says who the company is, what it is building, and how to reach it. Success is a first-time visitor leaving with a clear, favorable picture of a real, tasteful, current company, and knowing the email address to write to.

## Positioning

A two-person family company (Jay and Wave Heo) in Celina, Texas, with two chapters: Forge Kitchen, a kitchen and tabletop goods brand in development, shaped by Jay's restaurant experience; and a future bakery and café, shaped by Wave's baking. Korean sensibility and Texas hospitality.

## Operating Context

Static site (index.html, styles.css, script.js) deployed to Cloudflare Pages through `scripts/deploy_cloudflare.py`, which publishes only an allowlist of files and refuses to deploy if index.html references an asset outside it. Assets are content-hashed at deploy. No forms, no trackers beyond Cloudflare Web Analytics. Contact is a mailto link.

## Capabilities and Constraints

- English only.
- Light and dark themes with a switch in the header. The same photographs serve both themes, dimmed slightly in dark.
- Nothing is for sale yet. Forge Kitchen is "in development" / "launching soon"; the bakery and café is a future plan. No product names, prices, launch dates, or store links exist.
- Company facts must stay exactly as stated: Atelier JW LLC, a Texas limited liability company; founded August 2026 in Celina, Texas; founders Yoonjae (Jay) Heo and Mulgyeol (Wave) Heo, co-founders; contact jayheo@atelier-jw.com.
- The contact email must stay crawlable (the `email_off` comments around it are deliberate).
- JSON-LD Organization data, canonical URL, og tags, sitemap and robots stay accurate.
- Copy may be rewritten (owner, 2026-11-09) as long as the facts above hold.

## Brand Commitments

- Names: Atelier JW (company), Forge Kitchen (first brand), Jay and Wave (founders' short names).
- The owner wants the site to look refined and current, "for this generation", and finds the present look poor (2026-11-09). The previous look is not a commitment.
- Standing preference (owner, 2026-11-10): the site should feel like "our café". Loud graphic directions (saturated colour fields, stamp or poster graphics, flat illustration) were rejected as off-brand; the familiar, clean premium-homeware arrangement was chosen. The café's mood sits with warm artisan bakeries in the Tartine vein: warm neutrals, fresh bread, natural light, handmade feel. Craft bar: Tartine Bakery, East Fork, Heath Ceramics.

## Evidence on Hand

- Real: company facts, founder names, the email address, the registered FORGE KITCHEN trademark application.
- Absent, and not to be fabricated: products, product photos, a storefront, customers, reviews, press, prices, dates.
- Photography: the owner chose AI-generated imagery for this redesign (2026-11-09). It illustrates mood and material; it must never be presented as a photograph of an actual Forge Kitchen product or an actual café location.

## Product Principles

1. True first. A company with nothing to sell yet earns trust by being exact about what exists and what is coming.
2. One visit has to be enough. Who, what, where, and how to write, without a second page.
3. Two people, named. The company is small on purpose; the site should not pretend otherwise.
4. Taste is the proof. Until there are products, the quality of the site is the only sample of the company's standards.

## Accessibility & Inclusion

Keep the baseline: skip link, navigation links always visible (no menu button), visible focus, reduced-motion support, Lighthouse accessibility 100.
