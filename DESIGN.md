---
name: Atelier JW
description: One-page company site for a two-person family company in Celina, Texas, drawn as a warm artisan bakery in window light.
colors:
  olive: "#394718"
  on-olive: "#f7f5ec"
  espresso: "#3b1c09"
  ink: "#1d1612"
  ink-soft: "#5c5047"
  flour: "#f8f6f3"
  paper: "#efe8df"
  rule: "#ddd5cd"
  olive-dark: "#b9c67c"
  on-olive-dark: "#1b2106"
  espresso-dark: "#f6ecdf"
  ink-dark: "#f1e8dc"
  ink-soft-dark: "#c5b8a9"
  flour-dark: "#191410"
  paper-dark: "#221b15"
  rule-dark: "#3d3229"
typography:
  display:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "clamp(2.75rem, 1rem + 5vw, 5.25rem)"
    fontWeight: 400
    lineHeight: 1.03
    letterSpacing: "-0.022em"
  mail:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "clamp(1.75rem, 1rem + 2.6vw, 3.25rem)"
    fontWeight: 400
    lineHeight: 1.15
  headline:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "clamp(2rem, 1.5rem + 1.3vw, 2.625rem)"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  wordmark:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "1.625rem"
    fontWeight: 400
    lineHeight: 1
  intro:
    fontFamily: "Castoro, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: "clamp(1.25rem, 0.5rem + 1.3vw, 1.625rem)"
    fontWeight: 400
    lineHeight: 1.35
  body:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "clamp(1rem, 0.94rem + 0.25vw, 1.125rem)"
    fontWeight: 400
    lineHeight: 1.55
  caption:
    fontFamily: "'Red Hat Text', 'Segoe UI Variable Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.55
rounded:
  none: "0"
  circle: "50%"
spacing:
  pad: "clamp(20px, 4vw, 56px)"
  gap: "clamp(14px, 1.5vw, 24px)"
  space: "clamp(80px, 10vw, 144px)"
components:
  wordmark:
    textColor: "{colors.espresso}"
    typography: "{typography.wordmark}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "10px 0"
  theme-switch:
    textColor: "{colors.espresso}"
    rounded: "{rounded.circle}"
    width: "44px"
    height: "44px"
  text-link:
    textColor: "{colors.olive}"
    typography: "{typography.intro}"
  mail-link:
    textColor: "{colors.olive}"
    typography: "{typography.mail}"
  print:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.none}"
  caption-note:
    textColor: "{colors.ink-soft}"
    typography: "{typography.caption}"
  entry-heading:
    textColor: "{colors.espresso}"
    typography: "{typography.headline}"
  entry-statement:
    textColor: "{colors.espresso}"
    typography: "{typography.intro}"
  skip-link:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-olive}"
    padding: "10px 16px"
---

# Design System: Atelier JW

## Overview

**Creative North Star: "The Window-Lit Counter"**

The site is a bakery counter seen in soft window light: a flour-white ground, espresso-brown lettering, and photographs of cast iron, cakes, linen and marble hung like prints with square corners. It is a familiar, clean, premium-homeware arrangement, chosen over louder graphic directions; the craft sits in proportion, type and light, not in ornament.

The page carries one idea, the company's plan in order, and the layout repeats it. The headline says kitchen goods first, then a bakery and café; under it the cast-iron pot fills the left half and the cakes and the café table sit on the right half, and the chapters row sets Forge Kitchen and the bakery and café in the same two halves. Everything hangs from one grid of four equal columns whose middle line is the page's single axis. Density is generous and calm: sections are separated by space, and the only rules on the page are the two hairlines above Company and Contact.

The system is authored twice. Light is flour and espresso; dark is a roasted brown ground with cream lettering, and olive turns from deep to pale so links keep their contrast. Photographs are AI-generated illustrations of mood and material and are labelled as illustrative.

**Key Characteristics:**
- Flour ground, espresso headings, and one olive that belongs to links and focus.
- Castoro for what the company says; Red Hat Text for what is read.
- One four-column grid: headings and text start at the left margin or at the middle line.
- Space separates sections; two hairlines are the only rules.
- Square-cornered photographs over a paper tone; the one curve is the round theme switch.
- Flat and still: no shadows, no tinted bands, no gradients, no entrance motion.
- Light and dark themes are both first-class.

## Colors

A warm neutral palette lifted from flour, crust and coffee, with a single deep olive as the only chromatic voice.

### Primary
- **Counter Olive** (`olive`, dark theme `olive-dark`): the colour of inline text links (the email address in the intro and in the contact row), the focus ring, text selection and the skip link. Deep on flour in light, pale on the roasted ground in dark.
- **Cream on Olive** (`on-olive`, dark `on-olive-dark`): text on olive, which means selected text and the skip link only.

### Neutral
- **Flour** (`flour`, dark `flour-dark`): the page ground, edge to edge. It is also the browser theme colour and the scrollbar track.
- **Espresso** (`espresso`, dark `espresso-dark`): everything set in Castoro except the links: the headline, section headings, the intro, the company statement and the wordmark. Also the theme-switch icon.
- **Ink** (`ink`, dark `ink-dark`): reading text and navigation links.
- **Soft Ink** (`ink-soft`, dark `ink-soft-dark`): the caption note, the footer, the theme-switch outline on hover and the scrollbar thumb.
- **Hairline** (`rule`, dark `rule-dark`): the 1px rule above the Company and Contact rows and the theme-switch outline at rest.
- **Print Paper** (`paper`, dark `paper-dark`): the tone behind every photograph while it loads. It is never used as a visible surface.

### Named Rules
**The Olive Is a Link Rule.** Olive colours text that can be followed and the marks of focus: inline links, the focus ring, selection, the skip link. It is never a section field, a band, a bar or a heading colour. Navigation links and the wordmark stay ink and espresso.

**The One Ground Rule.** The whole page sits on flour. There is no second surface colour; paper appears only behind a photograph that has not loaded yet.

**The Dimmed Print Rule.** Photographs are never swapped per theme. In dark they are dimmed to 90% brightness.

## Typography

**Display Font:** Castoro, regular (with Iowan Old Style, Palatino Linotype, Georgia)
**Body Font:** Red Hat Text, variable 400 to 600, only 400 in use (with Segoe UI Variable Text, Segoe UI, system-ui)

**Character:** An old-style serif with a warm, slightly inked drawing, set large and tight, against a quiet humanist sans. Both are self-hosted woff2; the content security policy forbids third-party font hosts. Every style is weight 400 and upright: hierarchy comes from size and family, never from bold.

There are seven steps. Five are a single `clamp()` between a rem floor and a rem ceiling, so type moves with the window; the wordmark and the caption are fixed. No breakpoint changes a font size.

### Hierarchy
- **Display** (400, `clamp(2.75rem, 1rem + 5vw, 5.25rem)`, line-height 1.03, -0.022em): the single opening sentence, balanced over two lines on desktop and three on a phone.
- **Mail** (400, `clamp(1.75rem, 1rem + 2.6vw, 3.25rem)`, line-height 1.15): the email address in the contact row, in olive, allowed to break anywhere so it never overflows.
- **Headline** (400, `clamp(2rem, 1.5rem + 1.3vw, 2.625rem)`, line-height 1.08, -0.015em): the four section headings.
- **Wordmark** (400, 1.625rem, line-height 1): "Atelier JW" in the header.
- **Intro** (400, `clamp(1.25rem, 0.5rem + 1.3vw, 1.625rem)`, line-height 1.35): the serif paragraph in the hero, capped at 24em, and the company statement.
- **Body** (400, `clamp(1rem, 0.94rem + 0.25vw, 1.125rem)`, line-height 1.55): reading copy, capped at 31em, and the navigation links.
- **Caption** (400, 0.875rem, sentence case): the note under photographs and the footer, in soft ink.

### Named Rules
**The Spoken and Read Rule.** Castoro carries what the company says in its own voice: the headline, section headings, the intro, the company statement, the wordmark and the email address. Red Hat Text carries what is read: paragraphs, navigation, captions, the footer.

**The One Weight Rule.** Everything is weight 400. Emphasis is a change of family or size.

**The Fluid Ramp Rule.** A new size is one of the seven steps. A size is written once and is not restated inside a breakpoint.

## Layout

The page is one column of sections inside a wrap capped at 1520px with `pad` side padding. Inside the wrap there is one grid of four equal columns with `gap` between them. Its middle line is the page's single axis: headings and text start at the left margin or at that line, and photographs take a quarter, a half or the full width. The header and footer are not on the grid; they pin their items to the two outer margins.

The headline spans the full width above the grid. In the hero, the cast-iron pot print fills the left two columns and both rows, the serif intro hangs from the top of the right half, and two small prints sit on the bottom edge of the right half, one column each. The chapters row repeats those proportions as two halves: one landscape print for Forge Kitchen on the left, two portrait prints for the bakery and café on the right inside a box of the same landscape proportion, and under each its caption note, heading and paragraph. A wide table photograph follows at the full wrap width. Company and Contact are two ruled rows, heading on the left half and content on the right half, aligned on their first baselines.

Photograph proportions are fixed: 3:2 for every print and for the box that holds the portrait pair, 2:1 for the table photograph (3:2 at 900px and below).

Rhythm is three fluid values. `space` opens every section: above the chapters, the table photograph, the first ruled row and the footer. The second ruled row sits closer (`clamp(48px, 5vw, 72px)`). 14px separates a heading from its paragraph and a photograph from its caption note. The header is not sticky; it scrolls away with the page.

There are two breakpoints. At 900px and below the hero becomes two columns (the intro first at full width, then the pot print, then the two small prints side by side), and the chapters and the ruled rows collapse to one column; the portrait pair stays side by side. At 640px and below the navigation moves to its own row under the wordmark, spread across the width, and the theme switch stays on the first row. There is no menu button at any width.

### Named Rules
**The One Axis Rule.** In the main content, a heading or a block of text starts at the left margin or at the middle line of the four-column grid, and a photograph takes a quarter, a half or the full width. No block is centred or set on a third.

**The Space, Not Lines Rule.** Sections are separated by `space`. The hairlines above Company and Contact are the only dividing rules on the page; there are no vertical dividers, bands or bars.

## Elevation & Depth

The system is flat. There are no box shadows, text shadows, blurs, gradients, masks or tinted surfaces in the build, and nothing overlaps. Depth comes from the photographs themselves and from the two hairlines. Only the skip link is lifted above the page, and only while it has focus.

### Named Rules
**The No Shadow Rule.** A shadow would be the first one in the system.

## Shapes

Photographs and sections have square corners (0). The single curve is the theme switch, a 44px circle (50%) with a 1px hairline outline. The focus outline is square.

Lines are 1px: the two hairlines, the switch outline, and link underlines, which sit 0.22em below the baseline. The only icon is the theme-switch mark, a 20px outline circle with a 1.5 stroke and one half filled.

**The Print Rule.** A photograph is a print: square corners, no border, no radius, no overlay text. Its caption note sits beneath it.

## Components

### Header
A single row at the top of the wrap: wordmark at the left, navigation and theme switch at the right, 18px above and below. It is not sticky and carries no rule beneath it.
- **Wordmark:** "Atelier JW" in Castoro at the wordmark size, espresso, no underline, linking home. There is no mark or logo beside it.
- **Navigation:** four Red Hat Text links at the body size in ink (Forge Kitchen, Bakery, Company, Contact), always visible, with 10px of vertical padding for a comfortable target. The underline is transparent at rest and fades to the text colour on hover over 0.2s.
- **Theme switch:** a round icon-only button (44px, 1px `rule` outline, no fill) with `role="switch"` and the label "Dark theme". The outline moves to soft ink on hover. The half-filled circle turns 180 degrees when the theme changes.

### Links
- **Inline link:** olive, in the type of the sentence around it, with a 1px underline that thickens to 2px on hover.
- **Mail link:** the email address at the mail size in olive, same underline behaviour, set on its own line under one sentence of body copy.
- **Focus:** every focusable element takes a 2px olive outline offset 3px.

### Prints
Photographs fill their box with `object-fit: cover`, square-cornered, with `paper` behind them while loading, explicit width and height and a real `alt`. In dark they are dimmed to 90% brightness. The hero prints load eagerly, the pot with high priority; photographs below the hero load lazily.
- **Print:** 3:2.
- **Pair:** two portrait photographs side by side with `gap` between them, inside a 3:2 box so the pair is the same height as a print.
- **Wide:** the table photograph at 2:1 across the wrap, 3:2 at 900px and below.

### Caption note
One small style, caption size in soft ink, 14px under a photograph or a group of photographs, saying that the photographs are illustrative. The footer repeats it for the whole page.

### Chapter
A print or a pair, its caption note, a headline, then one paragraph of body copy capped at 31em. Two chapters sit side by side on the halves of the grid.

### Ruled row
A 1px hairline, then a headline on the left half and content on the right half, aligned on their first baselines. The content is either a statement at the intro size (Company) or a sentence of body copy with the mail link beneath it (Contact). At 900px and below the headline stacks above the content with a 14px gap.

### Skip link
An olive block with cream text, off screen until focused, then 16px from the top left corner.

### Footer
One row of caption-size soft-ink text on flour, copyright at the left and the photography note at the right, wrapping onto two lines when narrow.

### Motion
The page does not animate on arrival or on scroll. Motion is feedback only, and all of it sits inside `prefers-reduced-motion: no-preference`: the navigation underline fades in over 0.2s, the theme-switch icon turns over 0.5s on `cubic-bezier(0.16, 1, 0.3, 1)`, and in-page links scroll smoothly. Underline thickening and the switch outline change are instant.

## Do's and Don'ts

### Do:
- **Do** start headings and text at the left margin or at the middle line of the four-column grid, and size photographs to a quarter, a half or the full width.
- **Do** separate sections with `space`, and keep hairlines to the ruled rows.
- **Do** keep photographs square-cornered at 3:2 (or as a pair inside a 3:2 box, or the 2:1 wide photograph), over `paper`, with a real `alt` and explicit width and height.
- **Do** put the caption note under any photograph that could read as a product or a location.
- **Do** author every colour in both themes, using the custom properties, and dim photographs in dark instead of replacing them.
- **Do** take type sizes from the seven-step ramp.
- **Do** keep all motion inside `prefers-reduced-motion: no-preference`.
- **Do** keep the navigation links visible at every width, and the 2px olive focus outline with its 3px offset.
- **Do** put styles in `styles.css`; the content security policy blocks inline `style` attributes and third-party fonts and stylesheets.
- **Do** write asset URLs in `styles.css` from the repository root (`assets/fonts/...`); the deploy script rewrites them.

### Don't:
- **Don't** use olive as a field, band, bar or heading colour; it belongs to links and focus.
- **Don't** add a second accent colour or a second surface colour.
- **Don't** divide with vertical lines, tinted bands or decorative bars.
- **Don't** add shadows, blurs, gradients, or rounded corners on photographs.
- **Don't** use bold; every style is weight 400.
- **Don't** load fonts from a third-party host or add a third family.
- **Don't** add entrance, scroll-driven or looping animation.
- **Don't** swap photographs per theme; dim them.
- **Don't** present an illustrative image as an actual Forge Kitchen product or an actual café.
