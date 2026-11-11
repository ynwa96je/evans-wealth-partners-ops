const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const pages = ['/', '/about/', '/services/', '/resources/', '/contact/'];
  for (const [n, w] of [['desktop', 1440], ['tablet', 834], ['mobile', 390]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } }); const p = await ctx.newPage();
    const rows = [];
    for (const path of pages) {
      const r = await p.goto('https://evanswealthpartners.com' + path + '?v=' + Date.now(), { waitUntil: 'networkidle' });
      const info = await p.evaluate(() => ({
        docW: document.documentElement.scrollWidth,
        active: (document.querySelector('#ast-desktop-header .current-menu-item > a, #ast-hf-menu-1 .current-menu-item > a') || {}).textContent || '-',
        btnVisible: (() => { const a = [...document.querySelectorAll('#masthead a')].find(x => /Book an intro call/.test(x.textContent)); return a ? getComputedStyle(a).display !== 'none' && a.offsetParent !== null : false; })(),
        trigger: !!([...document.querySelectorAll('#masthead button')].find(x => x.offsetParent !== null)),
        footerCols: document.querySelectorAll('#colophon .footer-widget-area').length,
        logo: !!document.querySelector('#masthead img.custom-logo'),
      }));
      rows.push(path.padEnd(12) + r.status() + ' ' + JSON.stringify(info));
    }
    console.log('== ' + n + '\n' + rows.join('\n'));
    if (n === 'tablet') { await p.goto('https://evanswealthpartners.com/services/', { waitUntil: 'networkidle' }); const h = await p.$('#masthead'); await h.screenshot({ path: '/home/user/ewp/final-tablet-header.png' }); }
    await ctx.close();
  }
  await b.close();
})();
