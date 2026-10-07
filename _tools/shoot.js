// Take JPG screenshots of running sites with Playwright.
// Usage: node _tools/shoot.js <jobs.json>
// jobs.json: [{ "out": "folder/screenshots/01-home.jpg", "url": "http://...", "width": 1440, "height": 900,
//               "fullPage": false, "mobile": false, "wait": 800,
//               "css": "injected CSS, e.g. to hide cookie banners", "clicks": ["selectors to click first"],
//               "login": { "url": "...", "fields": { "#username": "admin" }, "submit": "button[type=submit]" } }]
// Jobs that share a "session" name reuse one logged-in browser context.
const path = require('path');
const fs = require('fs');
const PW = process.env.PLAYWRIGHT_PATH || 'C:/xampp/htdocs/everest-pet-shop/node_modules/playwright';
const { chromium } = require(PW);

(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch({ channel: 'chrome' });
  const contexts = {};
  for (const job of jobs) {
    const key = job.session || `_${Math.random()}`;
    try {
      if (!contexts[key]) {
        contexts[key] = await browser.newContext({
          viewport: { width: job.width || (job.mobile ? 390 : 1440), height: job.height || (job.mobile ? 844 : 900) },
          deviceScaleFactor: job.mobile ? 2 : 1,
          isMobile: !!job.mobile,
          ignoreHTTPSErrors: true,
        });
        if (job.apiLogin) {
          const r = await contexts[key].request.post(job.apiLogin.url, { data: job.apiLogin.data });
          console.log(`api login ${key} -> ${r.status()}`);
        }
        if (job.login) {
          const p = await contexts[key].newPage();
          await p.goto(job.login.url, { waitUntil: 'networkidle', timeout: 60000 });
          for (const sel of job.login.clicks || []) await p.click(sel, { timeout: 3000 }).catch(() => {});
          for (const [sel, val] of Object.entries(job.login.fields)) await p.fill(sel, val);
          await Promise.all([p.waitForLoadState('networkidle'), p.click(job.login.submit)]);
          await p.waitForTimeout(1500);
          console.log(`login ${key} -> ${p.url()}`);
          await p.close();
        }
      }
      const page = await contexts[key].newPage();
      await page.goto(job.url, { waitUntil: 'networkidle', timeout: 60000 });
      if (job.css) await page.addStyleTag({ content: job.css });
      for (const sel of job.clicks || []) {
        await page.click(sel, { timeout: 3000 }).catch(() => {});
      }
      await page.waitForTimeout(job.wait ?? 800);
      const out = path.resolve(job.out);
      fs.mkdirSync(path.dirname(out), { recursive: true });
      await page.screenshot({ path: out, type: 'jpeg', quality: 85, fullPage: !!job.fullPage });
      console.log(`ok  ${job.out}  (${page.url()})`);
      await page.close();
    } catch (e) {
      console.log(`ERR ${job.out}: ${e.message.split('\n')[0]}`);
    }
  }
  await browser.close();
})();
