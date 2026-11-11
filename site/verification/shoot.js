// usage: node shoot.js <exchange_url> <token_header> <token> <nonce_header> <nonce> <page_url> <outprefix>
const { chromium } = require('playwright');
(async () => {
  const [exUrl, th, tok, nh, nonce, pageUrl, out] = process.argv.slice(2);
  const res = await fetch(exUrl, { method: 'POST', headers: { [th]: tok, [nh]: nonce } });
  const j = await res.json();
  if (!j.login_url) { console.log('exchange failed', JSON.stringify(j)); process.exit(1); }
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  await page.goto(j.login_url, { waitUntil: 'load' });
  const consoleErrs = [];
  page.on('console', m => { if (m.type() === 'error') consoleErrs.push(m.text()); });
  for (const [name, w] of [['desktop', 1440], ['tablet', 834], ['mobile', 390]]) {
    await page.setViewportSize({ width: w, height: 900 });
    await page.goto(pageUrl, { waitUntil: 'networkidle' });
    await page.evaluate(() => { document.documentElement.classList.remove('kodee-sidebar-active'); document.body.classList.remove('kodee-sidebar-active'); });
    await page.addStyleTag({ content: '#wpadminbar,#vue-app{display:none!important} html{margin-top:0!important}' });
    for (let y = 0; y < 12000; y += 600) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(60); }
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(800);
    await page.screenshot({ path: `${out}-${name}.png`, fullPage: true });
    const info = await page.evaluate(() => {
      const q = s => document.querySelector(s);
      const cs = (el, props) => el ? Object.fromEntries(props.map(p => [p, getComputedStyle(el)[p]])) : null;
      return {
        docWidth: document.documentElement.scrollWidth,
        h1: cs(q('h1.ewp-banner-title'), ['color', 'fontFamily', 'fontSize', 'lineHeight', 'margin']),
        h2: cs(q('h2.ewp-title-section'), ['color', 'fontFamily', 'fontSize', 'margin']),
        h3navy: cs(q('.ewp-card-navy h3'), ['color', 'fontSize']),
        p: cs(q('.ewp-fact .ewp-text-body'), ['color', 'fontFamily', 'fontSize', 'lineHeight', 'margin']),
        btn: cs(q('.ewp-button-primary'), ['color', 'backgroundColor', 'padding', 'borderRadius', 'fontFamily', 'textDecoration']),
        link: cs(q('.ewp-link-arrow'), ['color', 'fontSize', 'textDecoration', 'display']),
        wrap: cs(q('.ewp-wrap'), ['maxWidth', 'width', 'padding']),
        bannerImg: q('.ewp-banner-photo') ? { tag: q('.ewp-banner-photo').tagName, ...cs(q('.ewp-banner-photo'), ['position', 'width', 'height', 'objectFit']) } : null,
        svg: q('.ewp-icon svg') ? q('.ewp-icon').outerHTML.slice(0, 300) : null,
        imgs: [...document.querySelectorAll('img.e-image-base')].map(i => [i.className.split(' ').pop(), i.naturalWidth, Math.round(i.getBoundingClientRect().width)+'x'+Math.round(i.getBoundingClientRect().height)]),
        sectionsTop: [...document.querySelectorAll('section.ewp-section, section.ewp-banner')].map(s => Math.round(s.getBoundingClientRect().height)),
        entryTitle: !!q('.entry-title'),
        sidebar: !!q('#secondary'),
      };
    });
    console.log(name, JSON.stringify(info));
  }
  console.log('console errors', consoleErrs.slice(0, 5));
  await browser.close();
})();
