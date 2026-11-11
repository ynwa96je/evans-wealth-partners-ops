// usage: node cmp.js <design_html> <site_url> <exUrl th tok nh nonce> <outprefix>
const { chromium } = require('playwright');
(async () => {
  const [design, siteUrl, exUrl, th, tok, nh, nonce, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const dctx = await b.newContext(); const d = await dctx.newPage();
  const sctx = await b.newContext(); const s = await sctx.newPage();
  const j = await (await fetch(exUrl, { method: 'POST', headers: { [th]: tok, [nh]: nonce } })).json();
  await s.goto(j.login_url);
  for (const [n, w] of [['desktop', 1440], ['tablet', 834], ['mobile', 390]]) {
    await d.setViewportSize({ width: w, height: 900 }); await s.setViewportSize({ width: w, height: 900 });
    await d.goto('file://' + design); await d.waitForTimeout(1500);
    await s.goto(siteUrl, { waitUntil: 'networkidle' });
    await s.evaluate(() => { document.documentElement.classList.remove('kodee-sidebar-active'); document.body.classList.remove('kodee-sidebar-active'); });
    await s.addStyleTag({ content: '#wpadminbar,#vue-app{display:none!important} html{margin-top:0!important}' });
    for (let y = 0; y < 14000; y += 700) { await s.evaluate(v => window.scrollTo(0, v), y); await s.waitForTimeout(50); }
    await s.evaluate(() => window.scrollTo(0, 0)); await s.waitForTimeout(1000);
    const dh = await d.evaluate(() => [...document.querySelectorAll('main > section')].map(x => Math.round(x.getBoundingClientRect().height)));
    const sh = await s.evaluate(() => [...document.querySelectorAll('section.ewp-section, section.ewp-banner')].map(x => Math.round(x.getBoundingClientRect().height)));
    const imgs = await s.evaluate(() => [...document.querySelectorAll('img.e-image-base')].map(i => i.naturalWidth > 0 ? 1 : 0).join(''));
    const docw = await s.evaluate(() => document.documentElement.scrollWidth);
    console.log(n.padEnd(8), 'design', JSON.stringify(dh), '\n         site  ', JSON.stringify(sh), 'imgsLoaded', imgs, 'docW', docw);
    await s.screenshot({ path: `${out}-site-${n}.png`, fullPage: true });
    await d.screenshot({ path: `${out}-design-${n}.png`, fullPage: true });
  }
  await b.close();
})();
