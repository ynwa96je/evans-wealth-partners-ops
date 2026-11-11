const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext({ deviceScaleFactor: 3, viewport: { width: 600, height: 300 } })).newPage();
  await p.goto('file:///home/user/ewp/logo/logo.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log(await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight).join(', ')));
  for (const id of ['dark', 'light']) {
    const el = await p.$('#' + id); const bb = await el.boundingBox();
    console.log(id, JSON.stringify(bb));
    await el.screenshot({ path: `/home/user/ewp/logo/ewp-logo-${id}.png`, omitBackground: true });
  }
  await b.close();
})();
