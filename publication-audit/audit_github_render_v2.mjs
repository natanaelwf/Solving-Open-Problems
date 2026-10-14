#!/usr/bin/env node
/**
 * audit_github_render_v2.mjs
 *
 * Browser-level validation of a commit-specific GitHub Markdown page.
 *
 * Requirements:
 *   npm install --no-save playwright
 *   npx playwright install chromium
 *
 * Usage:
 *   node audit_github_render_v2.mjs \
 *     --url "https://github.com/OWNER/REPO/blob/COMMIT/PATH/README.md" \
 *     --inventory math-inventory.json \
 *     --out browser-audit
 */

import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';

function parseArgs(argv) {
  const result = {};
  for (let i = 2; i < argv.length; i += 2) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!key?.startsWith('--') || value === undefined) {
      throw new Error(`Invalid argument sequence near ${key ?? '<end>'}`);
    }
    result[key.slice(2)] = value;
  }
  for (const required of ['url', 'inventory', 'out']) {
    if (!result[required]) {
      throw new Error(`Missing required argument --${required}`);
    }
  }
  return result;
}

const args = parseArgs(process.argv);
const inventory = JSON.parse(fs.readFileSync(args.inventory, 'utf8'));
const expectedDisplay = inventory.filter(item => item.kind === 'display');
const expectedInline = inventory.filter(item => item.kind === 'inline');
const expectedTotal = expectedDisplay.length + expectedInline.length;
const outDir = args.out;
fs.mkdirSync(outDir, { recursive: true });

const forbiddenMessages = [
  'The following macros are not allowed',
  'Missing close brace',
  'Undefined control sequence',
  'Math input error',
  'MathJax error',
  'ParseError',
];

const viewports = [
  { name: 'wide', width: 1440, height: 1200 },
  { name: 'narrow', width: 430, height: 932 },
];

const browser = await chromium.launch({ headless: true });
const reports = [];

try {
  for (const viewport of viewports) {
    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height },
      deviceScaleFactor: 1,
      reducedMotion: 'reduce',
    });
    const page = await context.newPage();

    await page.goto(args.url, {
      waitUntil: 'domcontentloaded',
      timeout: 120_000,
    });

    await page.waitForFunction(
      count => document.querySelectorAll('math-renderer').length === count,
      expectedTotal,
      { timeout: 120_000 },
    );

    await page.waitForFunction(
      () => [...document.querySelectorAll('math-renderer')].every(element =>
        element.querySelector('math, mjx-container') !== null
      ),
      { timeout: 120_000 },
    );

    await page.waitForTimeout(1500);

    const pageText = await page.locator('body').innerText();
    for (const message of forbiddenMessages) {
      if (pageText.toLowerCase().includes(message.toLowerCase())) {
        throw new Error(`${viewport.name}: GitHub displayed ${JSON.stringify(message)}`);
      }
    }

    const result = await page.evaluate(() => {
      const elements = [...document.querySelectorAll('math-renderer')];
      const article = document.querySelector('article.markdown-body');
      const articleRect = article?.getBoundingClientRect() ?? null;

      const inspect = (element, index) => {
        const rect = element.getBoundingClientRect();
        const output = element.querySelector('math, mjx-container');
        return {
          index: index + 1,
          classes: [...element.classList],
          visibleText: element.innerText ?? '',
          html: element.innerHTML,
          width: rect.width,
          height: rect.height,
          left: rect.left,
          right: rect.right,
          scrollWidth: element.scrollWidth,
          clientWidth: element.clientWidth,
          hasMathOutput: output !== null,
        };
      };

      return {
        title: document.title,
        url: location.href,
        pageHeight: document.documentElement.scrollHeight,
        documentScrollWidth: document.documentElement.scrollWidth,
        documentClientWidth: document.documentElement.clientWidth,
        bodyScrollWidth: document.body.scrollWidth,
        bodyClientWidth: document.body.clientWidth,
        articleWidth: articleRect?.width ?? null,
        articleScrollWidth: article?.scrollWidth ?? null,
        articleClientWidth: article?.clientWidth ?? null,
        display: elements
          .filter(element => element.classList.contains('js-display-math'))
          .map(inspect),
        inline: elements
          .filter(element => element.classList.contains('js-inline-math'))
          .map(inspect),
      };
    });

    if (result.display.length !== expectedDisplay.length) {
      throw new Error(
        `${viewport.name}: expected ${expectedDisplay.length} display expressions, ` +
        `found ${result.display.length}`
      );
    }
    if (result.inline.length !== expectedInline.length) {
      throw new Error(
        `${viewport.name}: expected ${expectedInline.length} inline expressions, ` +
        `found ${result.inline.length}`
      );
    }

    for (const expression of [...result.display, ...result.inline]) {
      if (!expression.hasMathOutput) {
        throw new Error(
          `${viewport.name}: rendered expression ${expression.index} lacks MathML/MathJax output`
        );
      }
      if (!(expression.width > 0) || !(expression.height > 0)) {
        throw new Error(
          `${viewport.name}: rendered expression ${expression.index} has a zero-sized box`
        );
      }
      const combined = `${expression.visibleText}\n${expression.html}`;
      for (const message of forbiddenMessages) {
        if (combined.toLowerCase().includes(message.toLowerCase())) {
          throw new Error(
            `${viewport.name}: expression ${expression.index} contains ${JSON.stringify(message)}`
          );
        }
      }
      if (/\\(?:operatorname|tag|boxed|newcommand|renewcommand|DeclareMathOperator)\b/.test(combined)) {
        throw new Error(
          `${viewport.name}: expression ${expression.index} exposes a forbidden TeX command`
        );
      }
    }

    if (result.documentScrollWidth > result.documentClientWidth + 2) {
      throw new Error(
        `${viewport.name}: page-level horizontal overflow: ` +
        `${result.documentScrollWidth} > ${result.documentClientWidth}`
      );
    }
    if (
      result.articleScrollWidth !== null &&
      result.articleClientWidth !== null &&
      result.articleScrollWidth > result.articleClientWidth + 2
    ) {
      throw new Error(
        `${viewport.name}: article-level horizontal overflow: ` +
        `${result.articleScrollWidth} > ${result.articleClientWidth}`
      );
    }

    const viewportDir = path.join(outDir, viewport.name);
    fs.mkdirSync(viewportDir, { recursive: true });
    const step = Math.max(300, viewport.height - 80);
    let screenshotCount = 0;

    for (let y = 0; y < result.pageHeight; y += step) {
      await page.evaluate(scrollY => window.scrollTo(0, scrollY), y);
      await page.waitForTimeout(100);
      screenshotCount += 1;
      await page.screenshot({
        path: path.join(
          viewportDir,
          `page-${String(screenshotCount).padStart(3, '0')}.png`
        ),
        fullPage: false,
      });
    }

    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({
      path: path.join(outDir, `${viewport.name}-full.png`),
      fullPage: true,
    });

    reports.push({
      viewport,
      ...result,
      screenshotCount,
    });
    await context.close();
  }
} finally {
  await browser.close();
}

const reportPath = path.join(outDir, 'browser-report.json');
fs.writeFileSync(reportPath, JSON.stringify(reports, null, 2));

console.log(
  `PASS: GitHub rendered ${expectedDisplay.length} display and ` +
  `${expectedInline.length} inline expressions at both viewport widths.`
);
console.log(`Report: ${reportPath}`);
