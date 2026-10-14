import fs from 'node:fs';
import { chromium } from 'playwright';
const sha=process.env.AUDIT_COMMIT;
if(!/^[a-f0-9]{40}$/.test(sha||'')) throw new Error('Missing commit SHA');
const url=`https://github.com/natanaelwf/Solving-Open-Problems/blob/${sha}/publication-audit/macro-fixture.md`;
const out='publication-audit/evidence';
fs.mkdirSync(out,{recursive:true});
const browser=await chromium.launch({headless:true});
const reports=[];
try {
 for(const width of [1440,430]) {
  const page=await browser.newPage({viewport:{width,height:1200},reducedMotion:'reduce'});
  const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:120000});
  if(!response?.ok()) throw new Error(`HTTP ${response?.status()}`);
  fs.writeFileSync(`${out}/server-${width}.html`,await response.text());
  await page.waitForFunction(()=>document.querySelectorAll('math-renderer').length===6,{},{timeout:120000});
  await page.waitForFunction(()=>[...document.querySelectorAll('math-renderer')].every(e=>e.querySelector('math,mjx-container')),{},{timeout:120000});
  const result=await page.evaluate(()=>{
   const article=document.querySelector('article.markdown-body');
   return {url:location.href,text:article?.innerText,html:article?.outerHTML,pageWidth:document.documentElement.clientWidth,pageScroll:document.documentElement.scrollWidth,articleWidth:article?.clientWidth,articleScroll:article?.scrollWidth,expressions:[...document.querySelectorAll('math-renderer')].map(e=>({text:e.innerText,html:e.innerHTML,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height,output:!!e.querySelector('math,mjx-container')}))};
  });
  fs.writeFileSync(`${out}/report-${width}.json`,JSON.stringify(result,null,2));
  await page.screenshot({path:`${out}/page-${width}.png`,fullPage:true});
  if(result.expressions.length!==6||result.expressions.some(e=>!e.output||e.width<=0||e.height<=0)) throw new Error('Missing mathematical output');
  if(/macros are not allowed|Undefined control sequence|Math input error|MathJax error|ParseError/i.test(result.text)) throw new Error('Math rendering error');
  if(result.pageScroll>result.pageWidth+2||result.articleScroll>result.articleWidth+2) throw new Error('Horizontal overflow');
  reports.push({width,status:'PASS',expressions:result.expressions.length});
  await page.close();
 }
}finally{await browser.close();}
fs.writeFileSync(`${out}/summary.json`,JSON.stringify({commit:sha,url,reports},null,2));
console.log(JSON.stringify(reports));
