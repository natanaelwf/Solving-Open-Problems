/** Bounded retries for transient HTTP failures, never for mathematical or layout errors. */
import fs from 'node:fs';
import path from 'node:path';
const directory = 'publication-audit/evidence/network';
const retryable = new Set([429, 502, 503, 504]);
let serial = 0;

export async function visit(page, url) {
  let last;
  for (let attempt = 0; attempt < 4; attempt++) {
    const target = new URL(url);
    if (attempt) target.searchParams.set('publication-audit-retry', `${Date.now()}-${attempt}`);
    const response = await page.goto(target.href, {waitUntil: 'domcontentloaded', timeout: 120000});
    if (response?.ok()) return response;
    last = response?.status();
    fs.mkdirSync(directory, {recursive: true});
    const id = String(++serial).padStart(3, '0');
    fs.writeFileSync(path.join(directory, `${id}.json`), JSON.stringify({url:target.href,status:last,attempt},null,2));
    if (response) fs.writeFileSync(path.join(directory, `${id}.html`), await response.text());
    if (!retryable.has(last)) throw new Error(`HTTP ${last} at ${target.href}`);
    console.warn(`Transient HTTP ${last}; navigation attempt ${attempt + 1}/4: ${url}`);
    if (attempt < 3) await page.waitForTimeout([5000,15000,30000][attempt]);
  }
  throw new Error(`HTTP ${last} persisted after four attempts at ${url}`);
}
