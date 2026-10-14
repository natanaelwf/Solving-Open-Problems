/** Check table structure, exact editorial fields, native scrollers and published bytes. */
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { chromium } from 'playwright';

const sha = process.env.AUDIT_COMMIT;
assert.match(sha || '', /^[a-f0-9]{40}$/);
const root = 'publication-audit/evidence';
const origin = 'https://github.com/natanaelwf/Solving-Open-Problems';
const browser = await chromium.launch({ headless: true });
const records = [];
try {
  for (const [slug, file] of [['index', 'README.md'], ['article', 'dujella-problem-1.7/README.md']]) {
    for (const width of [430, 1440]) {
      const page = await browser.newPage({ viewport: { width, height: 1000 }, reducedMotion: 'reduce' });
      await page.goto(`${origin}/blob/${sha}/${file}`, { waitUntil: 'domcontentloaded', timeout: 120000 });
      await page.waitForSelector('article.markdown-body');
      await page.waitForFunction(() => [...document.querySelectorAll('article.markdown-body math-renderer')].every(e => e.querySelector('math,mjx-container')), null, {timeout: 120000});
      const tables = await page.locator('article.markdown-body table').evaluateAll(ts => ts.map(t => ({
        rows: [...t.rows].map(r => [...r.cells].map(c => c.innerText.trim())),
        width: t.clientWidth, scrollWidth: t.scrollWidth,
      })));
      if (slug === 'index') {
        assert.equal(tables.length, 1);
        assert(tables[0].rows.every(r => r.length === 5));
        const row = tables[0].rows.find(r => r[0] === "Dujella's Problem 1.7");
        assert(row, 'The new entry is missing from the index.');
        assert.equal(row[3], '14 October 2026');
        assert.equal(row[4], 'Not Yet');
        assert(row[2].includes('part (c)') && row[2].includes('part (d)') && row[2].includes('remains unresolved'));
      } else {
        assert.equal(tables.length, 2);
        assert(tables[0].rows.every(r => r.length === 6));
        assert.equal(tables[0].rows.length, 5);
        assert(tables[1].rows.every(r => r.length === 3));
        assert.deepEqual(tables[1].rows.slice(1).map(r => r[2]), ['3620','6178','6368','10652','6140','12448']);
      }
      const scrollers = await page.locator('article.markdown-body table, article.markdown-body pre').evaluateAll(es => es.map((e, index) => ({index, tag: e.tagName, client: e.clientWidth, scroll: e.scrollWidth})).filter(e => e.scroll > e.client + 2));
      const directory = `${root}/editorial/${slug}-${width}`;
      fs.mkdirSync(directory, { recursive: true });
      for (const item of scrollers) {
        const element = page.locator('article.markdown-body table, article.markdown-body pre').nth(item.index);
        await element.scrollIntoViewIfNeeded();
        await element.evaluate(e => { e.scrollLeft = e.scrollWidth; });
        assert(await element.evaluate(e => e.scrollLeft > 0), 'Overflowing content must be horizontally accessible.');
        await element.screenshot({ path: `${directory}/scroller-${item.index}-right.png` });
      }
      records.push({slug, width, tables, nativeScrollableContainers: scrollers, status: 'PASS'});
      await page.close();
    }
  }
  const tracked = execFileSync('git', ['ls-files', 'README.md', 'dujella-problem-1.7', 'publication-audit', '.github/workflows/dujella-1-7-render.yml'], {encoding:'utf8'}).trim().split('\n');
  const request = await browser.newContext();
  const hashes = [];
  for (const file of tracked) {
    const response = await request.request.get(`https://raw.githubusercontent.com/natanaelwf/Solving-Open-Problems/${sha}/${file}`);
    assert(response.ok(), `Cannot retrieve ${file}: ${response.status()}`);
    const bytes = await response.body();
    assert(bytes.equals(fs.readFileSync(file)), `Published bytes differ: ${file}`);
    hashes.push({file, bytes:bytes.length, sha256:createHash('sha256').update(bytes).digest('hex'), matchesCheckout:true});
    const target = `${root}/snapshot/${file}`;
    fs.mkdirSync(path.dirname(target), {recursive:true});
    fs.writeFileSync(target, bytes);
  }
  fs.writeFileSync(`${root}/all-published-hashes.json`, JSON.stringify(hashes,null,2)+'\n');
  const summary = JSON.parse(fs.readFileSync(`${root}/summary.json`, 'utf8'));
  assert.equal(summary.status, 'PASS');
  const manifest = {
    repository: 'natanaelwf/Solving-Open-Problems', commit: sha,
    generatedAt: new Date().toISOString(), status: 'PASS',
    browser: browser.version(), viewports: [430,1440],
    sourceCheck: fs.readFileSync(`${root}/source-check.txt`, 'utf8').trim(),
    pages: summary.reports, editorialChecks: records,
    publishedFiles: hashes,
    note: 'Page and article overflow is forbidden. Native table and code scrollers are checked for accessibility and captured at their rightmost position.'
  };
  fs.writeFileSync(`${root}/manifest.json`, JSON.stringify(manifest,null,2)+'\n');
  await request.close();
  console.log(`PASS: editorial structure, native scrollers and all ${hashes.length} published file hashes.`);
} finally {
  await browser.close();
}
