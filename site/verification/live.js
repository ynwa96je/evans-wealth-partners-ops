const { chromium } = require('playwright');
(async () => {
  const [design, url] = process.argv.slice(2);
  const b = await chromium.launch(); const d = await (await b.newContext()).newPage(); const s = await (await b.newContext()).newPage();
  for (const [n, w] of [['desktop', 1440], ['tablet', 834], ['mobile', 390]]) {
    await d.setViewportSize({ width: w, height: 900 }); await s.setViewportSize({ width: w, height: 900 });
    await d.goto('file://' + design); await d.waitForTimeout(1200);
    const resp = await s.goto(url, { waitUntil: 'networkidle' });
    for (let y = 0; y < 14000; y += 700) { await s.evaluate(v => window.scrollTo(0, v), y); await s.waitForTimeout(50); }
    await s.waitForTimeout(800);
    const dh = await d.evaluate(() => [...document.querySelectorAll('main > section')].map(x => Math.round(x.getBoundingClientRect().height)));
    const r = await s.evaluate(() => ({ h: [...document.querySelectorAll('section.ewp-section')].map(x => Math.round(x.getBoundingClientRect().height)),
      imgs: [...document.querySelectorAll('img.e-image-base')].map(i => (i.naturalWidth > 0 && !/placeholder/.test(i.src)) ? 1 : 0).join(''), w: document.documentElement.scrollWidth }));
    console.log(n.padEnd(8), resp.status(), 'match', JSON.stringify(dh) === JSON.stringify(r.h), JSON.stringify(r.h), 'imgs', r.imgs, 'docW', r.w);
    if (n === 'desktop') await s.screenshot({ path: '/home/user/ewp/about-live-desktop.png', fullPage: true });
  }
  await b.close();
})();
