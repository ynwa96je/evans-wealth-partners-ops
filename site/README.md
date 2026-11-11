# Evans Wealth Partners: website build kit

Everything used to rebuild https://evanswealthpartners.com from the design exports as
Elementor 4 (atomic) pages on WordPress + Astra, built in a Claude Code session on 8–9 Nov 2026
(session title: "Evans Wealth Partners: Elementor v4 site build", tag `project:evans-wealth-partners`).

## What is on the site

| Page      | ID  | URL                                  | Notes |
|-----------|-----|--------------------------------------|-------|
| Home      | 84  | https://evanswealthpartners.com/     | Set as the static front page |
| About     | 129 | /about/                              | |
| Services  | 154 | /services/                           | Anchors: `#planning #retirement #investments #protection #income #estate #business-planning` |
| Resources | 176 | /resources/                          | Topic pills are visual only; guide/worksheet links point to /resources/ until guides/PDFs exist |
| Contact   | 194 | /contact/                            | Empty form slot: left column of the first section, flexbox ID `contact-form`, Navigator title "Contact form (empty: add your form here)" |

All pages: template **Elementor Full Width**; Astra per-page settings full-width container, no sidebar,
title hidden. Built only from Elementor v4 atomic elements (e-flexbox, e-heading, e-paragraph,
e-button, e-image, e-svg). No HTML widgets, shortcodes, stylesheets, Additional CSS or child theme.

### Design system in Elementor (Site Settings kit ID 6)
- **24 global variables**: 22 colours (`color-paper`, `color-navy`, `color-pitch`, `color-brass`, scrims, …)
  and 2 fonts (`font-serif` = `"Source Serif 4", Georgia, "Times New Roman", serif`,
  `font-sans` = `"Source Sans 3", "Helvetica Neue", Arial, sans-serif`).
  Font values are quoted stacks on purpose: Elementor writes an unquoted `Source Serif 4`, which is invalid CSS.
- **129 global classes**, all prefixed `ewp-` (defined in `build/ewp_lib.py`). Order matters:
  classes earlier in the list win, so modifiers (`ewp-*-on-navy`, `ewp-card-feature`, …) come first.
- Kit Global Fonts set to Source Serif 4 / Source Sans 3 (these make Elementor load the Google Fonts).
- Size/spacing values are literal values inside the classes: **size variables need Elementor Pro**.

### Header & footer (Astra Header/Footer Builder)
- Logo = `assets/logo/ewp-logo-dark.png` (header) and `ewp-logo-light.png` (footer); site title
  "Evans Wealth Partners", tagline "Family wealth management".
- Menu "Primary" (ID 2) → locations `primary` and `mobile_menu`.
- Header: logo | menu | "Book an intro call" button; ≤921px: outlined "Menu" dropdown with the button inside.
- Footer: above row = Footer Widgets 1–4 (blocks: logo + intro + button / Pages / Services / Get in touch),
  primary row = HTML 1 (disclosure), below row = Copyright (`© [current_year] Evans Wealth Partners`) + HTML 2 ("Avon, Connecticut").
- Astra palette: 0 pitch · 1 pitch hover · 2 navy · 3 slate · 4 white · 5 paper · 6 navy · 7 line · 8 brass.
- Full configuration: `server/astra-header-footer.php`.

### Media
- Photos: WebP, ≤1600px longest edge, <400 KB, converted on the server (`server/convert-photos.php`).
  Originals in `assets/photos-original/` (Home) and `assets/user-sent/` (About; see `MAP.txt`).
- Hartford Athletic crest: 700×700 transparent PNG (logo → kept as PNG).
- Icons/illustration: `assets/svg/` (uploaded as SVG attachments; the illustration's colours use the colour variables).
- Every photo attachment has an `_ewp_key` post meta (e.g. `banner`, `about-anfield`) used by the build scripts.

## Folder layout
```
build/            Page generators (Python). ewp_lib.py = all global classes + element helpers;
                  home.py / about.py / services.py / resources.py / contact.py = one page each.
                  unpack_bundle.py = extracts pages/images from the bundled design HTML.
server/           PHP run on the WordPress server:
                  build-page.php       save all classes + create/update one page from a payload
                  convert-photos.php   photo → WebP media import
                  astra-header-footer.php  the Astra header/footer configuration
design-source/    The design exports as received (Home bundle, About/Services/Resources/Contact, Header, Footer, site.css).
assets/           Logos, SVG icons, original photos.
verification/     Playwright scripts used to compare the live pages with the design at 1440 / 834 / 390px.
```

## How to change or add a page later
1. Edit/add classes in `build/ewp_lib.py` and the page in `build/<page>.py`.
2. `cd build && python3 <page>.py` → writes `<page>_payload.json` (or `<page>_build.json`).
3. Upload that file to `wp-content/uploads/ewp-source/payload.json` on the server
   (Novamira "create-upload-link" + `curl -X PUT ...`), then run `server/build-page.php` on the server.
   It always re-saves the **complete** class set, so keep every class in `ewp_lib.py`.
4. Check the draft, publish, clear the Hostinger cache (Hostinger Tools → Clear cache, or the REST call noted in the script).

In a new Claude Code session: attach this folder (or ask Claude to read it from the server copy) and say
"continue the Evans Wealth Partners site using the build kit".

## Known limits (accepted)
- Hover effects where hovering one element restyles another (card → icon box, timeline row → marker) are not expressible in Elementor classes.
- `prefers-reduced-motion` / `:focus-within` rules from the design are not expressible.
- Elementor loads Source Serif 4 without its optical-size axis, so some large headings wrap one line earlier than in the design.
- Elementor breakpoints are 1024/767 (design used 1000/640). Astra switches to the mobile header at 921px.
- Astra cannot draw the design's 2px brass underline on the active menu item (colour only).
- The footer hairline above the disclosure spans the full width; footer columns stack on mobile.

## Environment note
The Claude Code cloud environment "Default" had `evanswealthpartners.com` added to its network allowlist so files could be uploaded to the server.

## SEO / AEO (10 Nov 2026), set in the Visibility SEO plugin (`native_aeo_pack_settings`)
- Per-page SEO title + meta description + OG title/description (also copied to each page's excerpt, which feeds llms.txt):
  Home "Financial Advisor in Avon, CT | Evans Wealth Partners" · About "About John "Jack" Evans | Avon, CT Financial Advisor" ·
  Services "Financial Planning & Wealth Management Services | Avon, CT" · Resources "Financial Planning Guides for Connecticut Families" ·
  Contact "Contact Evans Wealth Partners | Avon, CT Financial Advisor".
- Identity schema on: LocalBusiness → FinancialService, name, URL, description, logo (att 197), email john@…, address Avon, CT, US (no street/phone yet).
- OG fallback image = banner (att 8); publisher logo = dark logo (197).
- /llms.txt and /llms-full.txt on. AI crawlers are NOT blocked in robots.txt (keep it that way for AI search).
- noindex: search results, attachment pages (redirected), author archive; user sitemap off. "Hello world!" post trashed.
- FAQ schema in this plugin only reads core Details/Accordion blocks, so it does not see Elementor content.
- 10 Nov: phone 860-857-4770 and hours (by appointment, 8am–9pm daily) added to the Contact page (build/contact.py),
  footer "Get in touch" widget (block-10) and identity schema (telephone, openingHoursSpecification). Service-area business:
  no street address published. sameAs = LinkedIn https://www.linkedin.com/in/ynwa96/.
- 10 Nov: footer email/phone set to 15px with a <wbr> after "@" (no more ".c/om" wrap); footer rows got 40px desktop side
  padding (they touched the screen edge at 922–1200px). Copy for compliance review (FAQ + 3 guides) is in the Claude doc
  "Evans Wealth Partners: website copy for compliance review" — nothing published from it yet.
- 10 Nov: approved copy published.
  Guides (children of Resources, built by build/guides.py): /resources/connecticut-estate-and-gift-tax/ (216),
  /resources/connecticut-529-plan/ (220), /resources/selling-your-business/ (224, anchor #buy-sell). SEO title/description set.
  FAQ sections: Home (4 Qs, before the booking band) and Contact (5 Qs, below the contact section); copy in ewp_lib.FAQ.
  Held back until confirmed: "How are you paid?", the registered-states line, the CHET direct vs advisor-sold note.
  Resources cards now link to the three guides. New classes: ewp-article, ewp-article-part, ewp-faq-list, ewp-faq-item (133 total).
  Multi-page build: python3 guides.py/home.py/contact.py/resources.py -> combine into build/bundle.json (see server/build-pages.php header)
  -> upload to wp-content/uploads/ewp-source/bundle.json -> run server/build-pages.php.
