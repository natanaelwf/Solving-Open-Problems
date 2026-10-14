/** Live GitHub browser audit, supplementing the supplied reference auditor.
 * In addition to its checks, preserve evidence on failure, compare server TeX,
 * check the inner MathML boxes for clipping, validate links and download hashes.
 */
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { chromium } from 'playwright';
const sha=process.env.AUDIT_COMMIT;
if(!/^[a-f0-9]{40}$/.test(sha||'')) throw new Error('A commit SHA is required.');
const root='publication-audit/evidence';
fs.mkdirSync(root,{recursive:true});
const extra='ell int ll gg asymp lfloor rfloor lceil rceil nmid bmod pmod'.split(' ').flatMap(s=>['--allow-macro',s]);
const reports=[],errors=[];
const browser=await chromium.launch({headless:true});
const origin='https://github.com/natanaelwf/Solving-Open-Problems';
try{
 for(const [slug,file] of [['index','README.md'],['article','dujella-problem-1.7/README.md']]){
  const out=`${root}/${slug}`;fs.mkdirSync(out,{recursive:true});
  const inventory=`${out}/inventory.json`;
  const lint=execFileSync('python',['publication-audit/github_math_guard_v2.py','lint',file,'--strict','--inventory-out',inventory,...extra],{encoding:'utf8'});
  fs.writeFileSync(`${out}/lint.txt`,lint);
  const expected=JSON.parse(fs.readFileSync(inventory,'utf8'));
  const url=`${origin}/blob/${sha}/${file}`;
  for(const width of [1440,430]){
   const view={width,height:width===430?932:1200};
   const page=await browser.newPage({viewport:view,reducedMotion:'reduce',deviceScaleFactor:1});
   const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:120000});
   if(!response?.ok()) throw new Error(`HTTP ${response?.status()} at ${url}`);
   const server=`${out}/server-${width}.html`;
   fs.writeFileSync(server,await response.text());
   try{
    const check=execFileSync('python',['publication-audit/github_math_guard_v2.py','verify-html',file,server,'--strict',...extra],{encoding:'utf8'});
    fs.writeFileSync(`${out}/server-check-${width}.txt`,check);
   }catch(e){errors.push(`${slug}/${width}: server-source mismatch`);fs.writeFileSync(`${out}/server-check-${width}.txt`,`${e.stdout}\n${e.stderr}`);}
   await page.waitForFunction(n=>document.querySelectorAll('article.markdown-body math-renderer').length===n,expected.length,{timeout:120000});
   await page.waitForFunction(()=>[...document.querySelectorAll('article.markdown-body math-renderer')].every(e=>e.querySelector('math,mjx-container')),null,{timeout:120000});
   await page.waitForTimeout(1000);
   const result=await page.evaluate(()=>{
    const a=document.querySelector('article.markdown-body');
    const ar=a.getBoundingClientRect();
    const clean=r=>({left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height});
    return {url:location.href,text:a.innerText,article:clean(ar),articleClient:a.clientWidth,articleScroll:a.scrollWidth,pageHeight:document.documentElement.scrollHeight,pageClient:document.documentElement.clientWidth,pageScroll:document.documentElement.scrollWidth,
     expressions:[...a.querySelectorAll('math-renderer')].map((e,i)=>{
      const output=e.querySelector('math,mjx-container');
      const child=output?.firstElementChild;
      const rect=clean(e.getBoundingClientRect()),box=output?clean(output.getBoundingClientRect()):null;
      return {index:i+1,kind:e.classList.contains('js-display-math')?'display':'inline',text:e.innerText,html:e.innerHTML,rect,box,inner:child?clean(child.getBoundingClientRect()):null,client:e.clientWidth,scroll:e.scrollWidth,output:!!output};
     }),
     localLinks:[...a.querySelectorAll('a[href]')].filter(e=>e.getAttribute('href').startsWith('#')).map(e=>({href:e.getAttribute('href'),found:!!document.getElementById(e.getAttribute('href').slice(1))||!!document.getElementById('user-content-'+e.getAttribute('href').slice(1))})),
     files:[...a.querySelectorAll('a[href]')].filter(e=>/\.(?:pdf|tex|py|json|txt)(?:$|[?#])/.test(e.getAttribute('href'))).map(e=>e.href)};
   });
   fs.writeFileSync(`${out}/report-${width}.json`,JSON.stringify(result,null,2));
   if(result.expressions.length!==expected.length)errors.push(`${slug}/${width}: count mismatch`);
   const bad=[];
   for(const e of result.expressions){
    if(!e.output||e.rect.width<=0||e.rect.height<=0||!e.box||e.box.width<=0||e.box.height<=0)bad.push({index:e.index,reason:'missing or zero-sized math'});
    if(/The following macros are not allowed|Missing close brace|Undefined control sequence|Math input error|MathJax error|ParseError|<merror\b/i.test(e.text+'\n'+e.html))bad.push({index:e.index,reason:'math error'});
    if(e.box&&(e.box.width>result.article.width+2||e.box.right>result.article.right+2||e.box.left<result.article.left-2))bad.push({index:e.index,reason:'equation extends beyond article',width:e.box.width,article:result.article.width});
    if(e.kind==='display'&&e.inner&&e.inner.width>e.rect.width+2)bad.push({index:e.index,reason:'inner equation clipping',width:e.inner.width,available:e.rect.width});
   }
   if(result.pageScroll>result.pageClient+2||result.articleScroll>result.articleClient+2)errors.push(`${slug}/${width}: horizontal overflow`);
   if(bad.length)errors.push(`${slug}/${width}: ${bad.length} expression layout errors`);
   const broken=result.localLinks.filter(x=>!x.found);
   if(broken.length)errors.push(`${slug}/${width}: ${broken.length} broken anchors`);
   fs.writeFileSync(`${out}/issues-${width}.json`,JSON.stringify({bad,broken},null,2));
   const screens=`${out}/${width}`;fs.mkdirSync(screens,{recursive:true});
   let n=0;
   for(let y=0;y<result.pageHeight;y+=view.height-100){
    await page.evaluate(y=>window.scrollTo(0,y),y);await page.waitForTimeout(80);
    await page.screenshot({path:`${screens}/${String(++n).padStart(3,'0')}.png`});
   }
   await page.screenshot({path:`${out}/full-${width}.png`,fullPage:true});
   reports.push({slug,file,width,url,expressions:result.expressions.length,display:result.expressions.filter(e=>e.kind==='display').length,inline:result.expressions.filter(e=>e.kind==='inline').length,screenshots:n,layoutIssues:bad.length,brokenAnchors:broken.length});
   await page.close();
  }
 }
 const context=await browser.newContext();
 const hashes=[];
 for(const file of ['README.md','dujella-problem-1.7/README.md','dujella-problem-1.7/paper.pdf','dujella-problem-1.7/paper.tex','dujella-problem-1.7/verify.py','dujella-problem-1.7/requirements.txt','dujella-problem-1.7/verification_results.json']){
  const url=`https://raw.githubusercontent.com/natanaelwf/Solving-Open-Problems/${sha}/${file}`;
  const r=await context.request.get(url);if(!r.ok())throw new Error(`Raw HTTP ${r.status()} ${url}`);
  const bytes=await r.body(),local=fs.readFileSync(file);
  if(!bytes.equals(local))errors.push(`Published bytes differ: ${file}`);
  hashes.push({file,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex'),matchesCheckout:bytes.equals(local)});
  const dest=`${root}/snapshot/${file}`;fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,bytes);
 }
 fs.writeFileSync(`${root}/published-hashes.json`,JSON.stringify(hashes,null,2));
 await context.close();
} catch(e){errors.push(String(e.stack||e));}
finally{await browser.close();}
fs.writeFileSync(`${root}/summary.json`,JSON.stringify({commit:sha,reports,errors,status:errors.length?'FAIL':'PASS'},null,2));
console.log(JSON.stringify({commit:sha,reports,errors},null,2));
if(errors.length)process.exitCode=1;
