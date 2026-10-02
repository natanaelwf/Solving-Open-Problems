const fs = require('fs');
const { chromium } = require('playwright');

const target = process.env.TARGET_URL;
const viewports = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844 },
];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const report = { target, auditedAt: new Date().toISOString(), viewports: {} };

  for (const viewport of viewports) {
    const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height } });
    const page = await context.newPage();
    const response = await page.goto(target, { waitUntil: 'domcontentloaded', timeout: 120000 });
    assert(response && response.ok(), `${viewport.name}: HTTP ${response && response.status()}`);
    await page.waitForTimeout(6000);

    const initial = await page.evaluate(() => ({
      title: document.title,
      height: document.documentElement.scrollHeight,
    }));
    assert(!/Page not found/i.test(initial.title), `${viewport.name}: GitHub returned a not-found page`);

    for (let y = 0; y < initial.height; y += Math.max(500, Math.floor(viewport.height * 0.75))) {
      await page.evaluate(pos => window.scrollTo(0, pos), y);
      await page.waitForTimeout(120);
    }
    await page.waitForTimeout(3000);

    const metrics = await page.evaluate(() => {
      const article = document.querySelector('article.markdown-body, .markdown-body');
      if (!article) return { articleFound: false };

      const text = article.innerText || '';
      const allMathRenderer = [...article.querySelectorAll('math-renderer')];
      const allMjx = [...article.querySelectorAll('mjx-container')];
      const allMathML = [...article.querySelectorAll('math')];
      const allRenderTargets = [...article.querySelectorAll('.js-render-target')];
      const formulaNodes = allMathRenderer.length ? allMathRenderer : (allMjx.length ? allMjx : allMathML);

      const hasScrollableAncestor = (node) => {
        let current = node;
        while (current && current !== article.parentElement) {
          const style = getComputedStyle(current);
          if ((style.overflowX === 'auto' || style.overflowX === 'scroll') && current.scrollWidth > current.clientWidth) return true;
          current = current.parentElement;
        }
        return false;
      };

      const formulaOverflow = formulaNodes.map((node, index) => {
        const rect = node.getBoundingClientRect();
        const bad = rect.width > 0 && (rect.left < -2 || rect.right > window.innerWidth + 2) && !hasScrollableAncestor(node);
        return bad ? { index, left: rect.left, right: rect.right, width: rect.width, snippet: (node.getAttribute('aria-label') || node.textContent || '').slice(0, 160) } : null;
      }).filter(Boolean);

      const forbiddenVisible = [
        'Missing close brace',
        'Undefined control sequence',
        'MathJax Error',
        '```math',
        '\\begin{aligned}',
        '\\end{aligned}',
        '\\frac{',
        '\\lt',
        '\\gt',
        '\\tag',
        '\\boxed',
      ].filter(token => text.includes(token));

      const merrors = article.querySelectorAll('merror, .merror, mjx-merror, [data-math-error]').length;
      const isolatedVisibleLines = text.split(/\n+/).map(s => s.trim()).filter(s => /^(a|b|w|0|7w)$/.test(s));

      return {
        articleFound: true,
        title: document.title,
        heading: article.querySelector('h1')?.innerText || '',
        textLength: text.length,
        containsOpeningClaim: text.includes('A complete negative solution to Dujella'),
        containsFinalProofSentence: text.includes('This proves Theorem 1.1.'),
        mathRendererCount: allMathRenderer.length,
        mjxContainerCount: allMjx.length,
        mathMLCount: allMathML.length,
        renderTargetCount: allRenderTargets.length,
        merrors,
        forbiddenVisible,
        isolatedVisibleLines,
        formulaOverflow,
        documentWidth: document.documentElement.scrollWidth,
        viewportWidth: window.innerWidth,
        bodyHorizontalOverflow: document.documentElement.scrollWidth > window.innerWidth + 2,
        pageHeight: document.documentElement.scrollHeight,
      };
    });

    assert(metrics.articleFound, `${viewport.name}: rendered Markdown article not found`);
    assert(metrics.heading === 'Uniqueness of a Smaller Extension of a Diophantine Triple', `${viewport.name}: wrong title: ${metrics.heading}`);
    assert(metrics.containsOpeningClaim, `${viewport.name}: subtitle missing`);
    assert(metrics.containsFinalProofSentence, `${viewport.name}: end of proof missing`);
    assert(Math.max(metrics.mathRendererCount, metrics.mjxContainerCount, metrics.mathMLCount, metrics.renderTargetCount) >= 300,
      `${viewport.name}: too few rendered mathematical expressions: ${JSON.stringify(metrics)}`);
    assert(metrics.merrors === 0, `${viewport.name}: MathJax error nodes found`);
    assert(metrics.forbiddenVisible.length === 0, `${viewport.name}: raw/error text visible: ${metrics.forbiddenVisible.join(', ')}`);
    assert(metrics.formulaOverflow.length === 0, `${viewport.name}: uncontained formula overflow: ${JSON.stringify(metrics.formulaOverflow.slice(0, 5))}`);

    const positions = [
      ['top', 0],
      ['middle', Math.max(0, Math.floor(metrics.pageHeight / 2 - viewport.height / 2))],
      ['bottom', Math.max(0, metrics.pageHeight - viewport.height)],
    ];
    for (const [label, y] of positions) {
      await page.evaluate(pos => window.scrollTo(0, pos), y);
      await page.waitForTimeout(600);
      await page.screenshot({ path: `render-audit/${viewport.name}-${label}.png`, fullPage: false });
    }

    report.viewports[viewport.name] = metrics;
    await context.close();
  }

  fs.writeFileSync('render-audit/report.json', JSON.stringify(report, null, 2));
  const summary = [
    `Target: ${target}`,
    `Audited: ${report.auditedAt}`,
    ...Object.entries(report.viewports).map(([name, m]) =>
      `${name}: heading OK; math-renderer=${m.mathRendererCount}; mjx=${m.mjxContainerCount}; mathML=${m.mathMLCount}; render-target=${m.renderTargetCount}; merrors=${m.merrors}; forbidden=${m.forbiddenVisible.length}; formula-overflow=${m.formulaOverflow.length}; body-overflow=${m.bodyHorizontalOverflow}`
    ),
  ].join('\n') + '\n';
  fs.writeFileSync('render-audit/summary.txt', summary);
  console.log(summary);
  await browser.close();
})().catch(error => {
  console.error(error.stack || error);
  process.exit(1);
});
