const { chromium } = require('playwright');
(async () => {
  const [design, exUrl, th, tok, nh, nonce, url, width, ...sels] = process.argv.slice(2);
  const b = await chromium.launch();
  const d = await (await b.newContext({ viewport: { width: +width, height: 900 } })).newPage();
  const s = await (await b.newContext({ viewport: { width: +width, height: 900 } })).newPage();
  await d.goto('file://' + design); await d.waitForTimeout(1200);
  const j = await (await fetch(exUrl, { method: 'POST', headers: { [th]: tok, [nh]: nonce } })).json();
  await s.goto(j.login_url); await s.goto(url, { waitUntil: 'networkidle' });
  await s.evaluate(() => { document.documentElement.classList.remove('kodee-sidebar-active'); document.body.classList.remove('kodee-sidebar-active'); });
  await s.addStyleTag({ content: '#wpadminbar,#vue-app{display:none!important} html{margin-top:0!important}' }); await s.waitForTimeout(800);
  const f = (pre) => (sels) => Object.fromEntries(sels.map(x => [x, [...document.querySelectorAll('.' + pre + x)].slice(0, 2).map(e => { const r = e.getBoundingClientRect(); const c = getComputedStyle(e); return Math.round(r.width) + 'x' + Math.round(r.height) + ' lh' + c.lineHeight + ' fs' + c.fontSize; }).join(' | ')]));
  const dr = await d.evaluate(new Function('sels', 'return (' + f('').toString() + ')("")(sels)'), sels).catch(() => null);
  const dd = await d.evaluate((sels) => Object.fromEntries(sels.map(x => [x, [...document.querySelectorAll('.' + x)].slice(0, 2).map(e => { const r = e.getBoundingClientRect(); const c = getComputedStyle(e); return Math.round(r.width) + 'x' + Math.round(r.height) + ' lh' + c.lineHeight + ' fs' + c.fontSize; }).join(' | ')])), sels);
  const ss = await s.evaluate((sels) => Object.fromEntries(sels.map(x => [x, [...document.querySelectorAll((x==='container'?'.ewp-wrap':'.ewp-' + x))].slice(0, 2).map(e => { const r = e.getBoundingClientRect(); const c = getComputedStyle(e); return Math.round(r.width) + 'x' + Math.round(r.height) + ' lh' + c.lineHeight + ' fs' + c.fontSize; }).join(' | ')])), sels);
  for (const x of sels) console.log(x.padEnd(20), 'D', dd[x], '\n' + ' '.repeat(21) + 'S', ss[x]);
  await b.close();
})();
