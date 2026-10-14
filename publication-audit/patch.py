from pathlib import Path
import subprocess
pairs=[(r'\mathbb{Z}','ℤ'),(r'\mathbb{Q}','ℚ'),(r'\mathbb{R}','ℝ'),(r'\mathcal{O}','𝒪')]
for file in ['README.md','dujella-problem-1.7/README.md']:
 p=Path(file);s=p.read_text()
 for old,new in pairs:s=s.replace(old,new)
 p.write_text(s)
p=Path('publication-audit/check_source.py');s=p.read_text();s=s.replace('def canonical(s):','def canonical(s):\n    for old,new in '+repr(pairs)+':\n        s=s.replace(old,new)');p.write_text(s)
p=Path('publication-audit/render.mjs');s=p.read_text()
s=s.replace('for(const width of [1440,430])','for(const width of [430,1440])')
s=s.replace("const response=await page.goto(url", """const diagnostics=[];
   page.on('console',msg=>{if(msg.type()==='error')diagnostics.push({type:'console',text:msg.text()});});
   page.on('pageerror',e=>diagnostics.push({type:'pageerror',text:String(e.stack||e)}));
   page.on('requestfailed',r=>diagnostics.push({type:'requestfailed',url:r.url(),text:r.failure()?.errorText}));
   page.on('response',r=>{if(r.status()>=400)diagnostics.push({type:'response',url:r.url(),status:r.status()});});
   const response=await page.goto(url""")
s=s.replace("fs.writeFileSync(`${out}/report-${width}.json`,JSON.stringify(result,null,2));", """fs.writeFileSync(`${out}/report-${width}.json`,JSON.stringify(result,null,2));
   fs.writeFileSync(`${out}/diagnostics-${width}.json`,JSON.stringify(diagnostics,null,2));
   fs.writeFileSync(`${out}/renderer-class-${width}.txt`,await page.evaluate(()=>String(customElements.get('math-renderer'))));""")
s=s.replace('The following macros are not allowed|Missing close brace','Unable to render expression|The following macros are not allowed|Missing close brace')
p.write_text(s)
subprocess.run(['git','add','README.md'],check=True)
