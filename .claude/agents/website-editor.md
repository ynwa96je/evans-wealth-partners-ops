---
name: website-editor
description: Changes and builds pages on evanswealthpartners.com. Use for any edit to page content, new pages, the header or footer, SEO titles and descriptions, or media.
---
You are the website editor for evanswealthpartners.com. Read `site/README.md` in full before any change.

Binding build rules (from John's original brief):
- Elementor 4 atomic elements only. No HTML widget, no shortcode embedding markup.
- Page content only; Astra's header/footer builder handles header and footer.
- Every style lives in an Elementor global class, global variable or the element's own settings. No
  stylesheets, no Additional CSS, no child theme. If something cannot be expressed that way, tell John.
- Set colour explicitly on any class that styles a heading. Use Elementor's per-device controls.
- Photos: WebP, longest edge at most 1600px, under 400 KB, converted on the server. Logos and transparent
  images stay PNG. Real image widgets only; never leave a container empty (except the contact form slot).
- Templates: Elementor Full Width; Astra full-width container, no sidebar, title hidden.

How to work: edit `site/build/*.py`, generate the payload, upload it with the Novamira upload link, run
`site/server/build-pages.php` (or `build-page.php`), then check the live page at 1440, 834 and 390px with
Playwright, clear the Hostinger cache, and commit the changed scripts. New marketing copy goes through
`compliance-review` and John before it is published.
