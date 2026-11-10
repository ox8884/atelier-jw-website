---
name: Atelier JW
description: One-page company site for a two-person family company in Celina, Texas, drawn as a warm artisan bakery in window light.
colors:
  olive: "#394718"
  olive-deep: "#2b3611"
  on-olive: "#f7f5ec"
  on-olive-soft: "#d9dcc4"
  espresso: "#3b1c09"
  ink: "#1d1612"
  ink-soft: "#5c5047"
  flour: "#f8f6f3"
  band: "#f5ece5"
  switch: "#efeee6"
  rule: "#ddd5cd"
  rule-strong: "#8f8279"
  olive-dark: "#b9c67c"
  olive-deep-dark: "#cad692"
  on-olive-dark: "#1b2106"
  on-olive-soft-dark: "#3a431c"
  espresso-dark: "#f6ecdf"
  ink-dark: "#f1e8dc"
  ink-soft-dark: "#c5b8a9"
  flour-dark: "#191410"
  band-dark: "#221b15"
  switch-dark: "#2b241d"
  rule-dark: "#3d3229"
  rule-strong-dark: "#7d6e60"
  contact-band-dark: "#2b3611"
  on-contact-dark: "#f1eedc"
  on-contact-soft-dark: "#c4c9a4"
typography:
  display:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "95px"
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: "-0.022em"
  contact-title:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "96px"
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: "-0.025em"
  band-title:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "71px"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "60px"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "-0.02em"
  mail:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "46px"
    fontWeight: 400
    lineHeight: 1.15
  brand:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "40.5px"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "40px"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  cta:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "37px"
    fontWeight: 400
    lineHeight: 1
  line:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "34px"
    fontWeight: 400
    lineHeight: 1.22
  value:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "clamp(1.25rem, 28px, 1.75rem)"
    fontWeight: 400
    lineHeight: 1.25
  caption:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "27px"
    fontWeight: 400
    lineHeight: 1.4
  lede:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "26px"
    fontWeight: 400
    lineHeight: 1.285
  facts:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "25.3px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0.012em"
  band-text:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "23px"
    fontWeight: 400
    lineHeight: 1.26
    letterSpacing: "0.01em"
  nav:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "22.5px"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "clamp(1rem, 21px, 1.3125rem)"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "clamp(0.875rem, 16px, 1rem)"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0.02em"
rounded:
  none: "0"
  focus: "2px"
  button: "7px"
  pill: "999px"
spacing:
  gap: "17px"
  pad: "44px"
  section: "112px"
components:
  button-primary:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-olive}"
    typography: "{typography.cta}"
    rounded: "{rounded.button}"
    width: "374px"
    height: "78px"
  button-primary-hover:
    backgroundColor: "{colors.olive-deep}"
    textColor: "{colors.on-olive}"
  theme-switch:
    backgroundColor: "{colors.switch}"
    textColor: "{colors.olive}"
    rounded: "{rounded.pill}"
    width: "96px"
    height: "40px"
  theme-switch-knob:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-olive}"
    rounded: "{rounded.pill}"
    width: "50px"
    height: "32px"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav}"
  chapter-caption:
    textColor: "{colors.espresso}"
    typography: "{typography.caption}"
  brand-band:
    backgroundColor: "{colors.band}"
    textColor: "{colors.espresso}"
    typography: "{typography.band-title}"
    padding: "20px 44px 36px"
  ledger-label:
    textColor: "{colors.ink-soft}"
    typography: "{typography.label}"
  ledger-value:
    textColor: "{colors.espresso}"
    typography: "{typography.value}"
    padding: "16px 0"
  contact-band:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-olive}"
    typography: "{typography.contact-title}"
    padding: "104px 44px 112px"
  contact-mail:
    textColor: "{colors.on-olive}"
    typography: "{typography.mail}"
---

# Design System: Atelier JW

## Overview

**Creative North Star: "The Window-Lit Counter"**

The site is a bakery counter seen in soft window light: a flour-white ground, espresso-brown lettering, warm hairlines, and photographs of cakes, cast iron, linen and marble hung like prints with square corners. It is a familiar, clean, premium-homeware arrangement, chosen over louder graphic directions; the craft sits in proportion, type and light, not in ornament.

Density is generous and calm. One sentence spans the full width, three equal photographs follow it, and every later section is a ruled, two-voice composition: a Castoro headline or italic line against Red Hat Text reading copy. Facts are set as ledgers on hairlines because the company has facts, not products, to show.

The system is authored twice. Light is flour and espresso; dark is a roasted brown ground with cream lettering, and olive flips from a deep field to a pale one so the action keeps its contrast. Photographs are AI-generated illustrations of mood and material and are labelled as illustrative wherever they could be read as product or place.

**Key Characteristics:**
- Flour ground, espresso headlines, one olive that belongs to the action and the closing band.
- Castoro for everything that is said aloud (headlines, italic captions, values); Red Hat Text for everything that is read.
- Square-cornered photographs; the only curves are the button (7px) and the pill switch.
- Flat: no shadows anywhere. Depth is tone and hairline.
- One proportional unit above 960px: the whole 1536px composition scales down together.
- Light and dark themes are both first-class.

## Colors

A warm neutral palette lifted from flour, crust and coffee, with a single deep olive as the only chromatic voice.

### Primary
- **Counter Olive** (`olive`, dark theme `olive-dark`): the action colour. Fills the Email button and the theme-switch knob, draws the leaf mark, the short bar under each brand title, the focus ring and text selection, and floods the closing contact band.
- **Pressed Olive** (`olive-deep`, dark `olive-deep-dark`): hover state of the olive button only.
- **Cream on Olive** (`on-olive`, `on-olive-soft`): text and icons on olive; the soft step is for supporting copy and the address inside the contact band.

### Neutral
- **Flour** (`flour`, dark `flour-dark`): the page ground and the sticky header.
- **Linen Band** (`band`, dark `band-dark`): the tinted strip behind each brand title.
- **Espresso** (`espresso`, dark `espresso-dark`): all headings, italic captions, ledger values, founder names and the wordmark.
- **Ink** (`ink`, dark `ink-dark`): reading text.
- **Soft Ink** (`ink-soft`, dark `ink-soft-dark`): labels, figcaptions, the company aside and the footer.
- **Hairline** (`rule`, dark `rule-dark`): horizontal rules: header, facts row, ledger rows, section top.
- **Strong Hairline** (`rule-strong`, dark `rule-strong-dark`): vertical dividers, the rule over each founder, the scrollbar thumb.
- **Switch Track** (`switch`, dark `switch-dark`): the theme-switch track only.

### Named Rules
**The Olive Is Spoken For Rule.** Olive fills only the action (the Email button, the switch knob) and the closing contact band; elsewhere it appears as a line or mark (leaf mark, title bar, focus ring), never as body text or a second coloured field.

**The Band Stays Dark Rule.** In the dark theme olive becomes pale so the button reads on a roasted ground, but the contact band does not follow it: it stays deep olive (`contact-band-dark`) with cream text (`on-contact-dark`, `on-contact-soft-dark`). The closing band is a dark olive field in both themes.

**The Dimmed Print Rule.** Photographs are never swapped per theme. In dark they are dimmed to 90% brightness, and the linen strip drops to 50% opacity.

## Typography

**Display Font:** Castoro, regular and italic (with Iowan Old Style, Palatino Linotype, Georgia)
**Body Font:** Red Hat Text, variable 400 to 600, only 400 in use (with Segoe UI Variable Text, Segoe UI, system-ui)

**Character:** An old-style serif with a warm, slightly inked italic, set large and tight, against a quiet humanist sans. Both are self-hosted woff2; the content security policy forbids third-party font hosts. Every style is weight 400: hierarchy comes from size, family and italic, never from bold.

Sizes in the frontmatter are the 1536px design values. Above 960px each is multiplied by the unit `--u = min(100vw / 1536, 1px)`, so type shrinks with a narrower desktop and never grows past the design. Body, value and label carry rem floors and ceilings so reading text stays between 16px and 21px, values between 20px and 28px, labels between 14px and 16px. At 960px and below the tokens switch to the fixed or fluid values noted here.

### Hierarchy
- **Display** (400, 95u; `clamp(2.75rem, 11.5vw, 5rem)` at 960px and below, line-height 1.14 then 1.02, -0.022em): the single opening sentence, one line at full width on desktop.
- **Contact title** (400, 96u; `clamp(3rem, 13vw, 5rem)`, line-height 0.98, -0.025em): the closing call on the olive band.
- **Band title** (400, 71u; `clamp(2.5rem, 9vw, 3.5rem)`, line-height 1.02, -0.02em): brand names on the linen band.
- **Headline** (400, 60u; `clamp(2rem, 7vw, 3rem)`, line-height 1.08, -0.02em): section statements.
- **Mail** (400, 46u; `clamp(1.375rem, 6vw, 2.25rem)`, line-height 1.15): the email address as a link.
- **Title** (400, 40u; 1.75rem, line-height 1.1, -0.01em): founder names. The wordmark sits beside it at 40.5u (1.625rem).
- **CTA** (400, 37u; 1.5rem, line-height 1): the button label.
- **Line** (italic 400, 34u; 1.625rem, line-height 1.22): one italic sentence per brand.
- **Value** (400, 20px to 28px, line-height 1.25): the answer in a ledger row.
- **Caption** (italic 400, 27u; 1.25rem, and `clamp(0.875rem, 1.95vw, 1.0625rem)` between 700px and 960px, line-height 1.4): centred under each chapter photograph.
- **Lede** (400, 26u; `clamp(1.0625rem, 2.6vw, 1.25rem)`, line-height 1.285 then 1.5): the opening paragraph, capped at 940u (60ch on small screens).
- **Facts / Band text / Nav** (400, 25.3u, 23u, 22.5u; 1rem, 1.0625rem, 1rem): the ruled fact row, the band description, header links.
- **Body** (400, 16px to 21px, line-height 1.5): reading copy, capped at 40 to 44ch.
- **Label** (400, 14px to 16px, 0.02em, sentence case): ledger terms, founder roles, figcaptions, footer.

### Named Rules
**The Spoken and Read Rule.** Castoro carries what the company says in its own voice: headlines, italic lines and captions, names, ledger values, the button and the email address. Red Hat Text carries what is read: paragraphs, navigation, facts, labels.

**The One Weight Rule.** Everything is weight 400. Emphasis is a change of family, size or italic.

**The Italic Is a Caption Rule.** Castoro italic appears only on photo captions and the single brand line. Headlines stay upright.

## Layout

The page is a single column of full-width sections inside a 1536px wrap with 44u side padding. Above 960px every dimension is written in `--u`, one pixel of the 1536px design, so a 1280px or 1440px window shows the same composition reduced, not reflowed. Section rhythm is 112u top and bottom; column gap is 17u.

Sections use a 12-column grid: photograph 8 and notes 4 (Forge Kitchen); notes 4, photograph 4, photograph 4 with the last dropped 96u (Bakery + Café); headline 7 with an aside in columns 9 to 12 (Company); 6 and 6 (Contact). The hero is not on the grid: a full-width headline, then paragraph, vertical hairline and button in a row, then three equal photographs, then a ruled fact row. The sticky header is 74u tall on a hairline inset to the wrap padding.

Photograph proportions are fixed: 474:325 for the three chapter prints, 3:2 for a landscape, 2:3 for a portrait, 21:9 for the full-bleed table photograph (4:3 at 960px and below).

At 960px and below the unit system is replaced: padding `clamp(18px, 5vw, 36px)`, gap 14px, section `clamp(64px, 12vw, 96px)`. The header stops being sticky and the navigation wraps onto its own row under the wordmark, with no menu button. Grids collapse to one column, except the two portrait bakery photographs, which stay side by side. Vertical hairlines disappear; the fact row becomes ruled lines. From 700px to 960px the three chapter photographs return to a row with a 12px gap and the facts spread across one line.

**The Shrink, Don't Reflow Rule.** Between 961px and 1536px nothing rearranges. New desktop dimensions are written as `calc(n * var(--u))`, with a rem clamp only on text small enough to become unreadable.

## Elevation & Depth

The system is flat. There are no box shadows, text shadows, blurs or glass layers in the build. Depth comes from three things: tone (the linen band and the olive contact band against flour), 1px hairlines, and the photographs themselves. The sticky header is an opaque flour bar with a hairline, not a floating one. The one soft edge is the linen strip at the right of the Forge Kitchen band, which fades into the band through a gradient mask.

### Named Rules
**The No Shadow Rule.** Surfaces separate by tone or a 1px rule. A shadow would be the first one in the system.

## Shapes

Photographs, bands and sections have square corners (0). Curves are reserved for controls: the Email button (7u, 6px on small screens) and the pill theme switch (999px). The focus outline carries a 2px radius.

Lines are 1px in two strengths: `rule` for horizontals, `rule-strong` for verticals between a title and its text. The only heavier mark is the olive bar under each brand title (112u by 6u; 72px by 4px on small screens). Icons are outline SVG with a 1.6 stroke, round caps and joins; the leaf mark is the one filled drawing.

**The Print Rule.** A photograph is a print: square corners, no border, no radius, no overlay text. Its caption sits beneath it.

## Components

### Buttons
One button exists: the olive Email action. It is confident and plain, a serif label beside an outline envelope.
- **Shape:** softly eased corners (7u; 6px at 960px and below).
- **Primary:** `olive` fill, `on-olive` Castoro label at the CTA size, envelope icon with a 34u gap, 374u by 78u; full width up to 420px and 60px tall on small screens.
- **Hover / Focus:** fill moves to `olive-deep` over 0.3s and the envelope lifts 3u and tilts -4deg on the house ease; pressing drops the button 1px. Focus is a 2px olive outline offset 3px.

### Theme switch
- **Style:** pill track in `switch` (96u by 40u; 76px by 44px on small screens) with an olive knob that slides across over 0.5s. Sun and moon are outline icons; the one under the knob takes `on-olive`, the other olive. It is a `button` with `role="switch"`.

### Navigation
- **Style:** three Red Hat Text links at the nav size, 48u apart, in the inherited ink colour. Hover and focus draw a 1px underline from the left over 0.45s. A strong vertical hairline separates the links from the theme switch. On small screens the links wrap to a second row with 10px vertical padding; there is no hamburger.
- **Wordmark:** olive leaf mark, a strong vertical hairline, then "Atelier JW" in Castoro.

### Chapter prints
Three equal photographs, each a link to its section, with a centred Castoro italic caption beneath. On hover or focus the photograph scales to 1.035 inside its frame over 1.1s and a 1px underline grows from the centre of the caption. On arrival each print is unveiled from the top edge, staggered 0.1s, while the image settles from 1.09 scale.

### Brand band
A full-width strip in `band`: brand title with the short olive bar beneath, a strong vertical hairline, then a short description capped at 690u. The Forge Kitchen band carries the page's one material, a linen strip with an olive stripe, masked into the right edge. On small screens title and text stack and the hairline is removed.

### Ledger
Facts as a definition list: each row opens with a 1px hairline, a label in soft ink above a Castoro value in espresso, 16u of padding; the list closes with a hairline. The wide variant puts the label in a 250u column beside the value and stacks on small screens.

### Founders
Two columns, each under a strong hairline: name at the title size, role as a label, one sentence of body copy capped at 40ch.

### Photographs and figcaptions
Photographs sit in their fixed proportions with `object-fit: cover`. Any photograph that could be mistaken for a product or a place carries a label-size figcaption in soft ink saying it is illustrative, and the footer repeats the note. Below the fold, photographs settle from 1.09 scale as they enter view where scroll-driven animation is supported.

### Contact band
The closing section is a full-width olive field: the contact title in the left six columns, and in the right six a short line of copy, the email address as a Castoro link with a 1px underline that thickens to 3px on hover and an arrow that nudges up and right, then the address. Focus rings and selection invert to cream here.

### Footer
One row of label-size soft-ink text on flour: copyright, place, underlined email, and the illustrative-photography note beneath.

### Motion
One ease, `cubic-bezier(0.16, 1, 0.3, 1)`, for everything that moves. Entrances happen once, on arrival, in reading order: headline and intro rise 16u out of a 5px blur, prints unveil, captions and facts fade. Under `prefers-reduced-motion: reduce` all transitions and animations are off.

## Do's and Don'ts

### Do:
- **Do** write desktop dimensions as `calc(n * var(--u))` so new elements scale with the rest of the 1536px composition, and give them fixed or clamp values inside the 960px breakpoint.
- **Do** author every colour in both themes, using the custom properties; check the dark theme whenever olive is involved, because it inverts from a deep field to a pale one.
- **Do** keep photographs square-cornered, in one of the existing proportions (474:325, 3:2, 2:3, 21:9), with a real `alt` and explicit width and height.
- **Do** label any image that could read as a product or a location as illustrative, in a label-size figcaption.
- **Do** set facts as ledger rows on hairlines, label above value.
- **Do** put styles in `styles.css`; the content security policy blocks inline `style` attributes and third-party fonts and stylesheets.
- **Do** write asset URLs in `styles.css` from the repository root (`assets/fonts/...`); the deploy script rewrites them.
- **Do** keep the 2px olive focus outline with its 3px offset, and the cream version on olive.

### Don't:
- **Don't** add a second accent colour or a second coloured field; olive is the only chromatic voice and it is spoken for.
- **Don't** use olive for body text or decorative fills.
- **Don't** add shadows, blurs, gradients over text, or rounded corners on photographs.
- **Don't** use bold; every style is weight 400.
- **Don't** set headlines in italic or reading text in Castoro.
- **Don't** load fonts from a third-party host or add a third family.
- **Don't** swap photographs per theme; dim them.
- **Don't** present an illustrative image as an actual Forge Kitchen product or an actual café.
- **Don't** animate on a loop or re-trigger entrances; prints are hung once.
