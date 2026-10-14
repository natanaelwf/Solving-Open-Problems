from pathlib import Path
import re
p=Path('dujella-problem-1.7/README.md');s=p.read_text()
s,n=re.subn(r'\$([A-Za-z])\$',r'<var>\1</var>',s)
assert n==91,n
assert s.count(r'\{')==5
s=s.replace(r'\{',r'\lbrace ').replace(r'\}',r'\rbrace ');p.write_text(s)
p=Path('publication-audit/render.mjs');s=p.read_text()
s=s.replace("const expected=JSON.parse(fs.readFileSync(inventory,'utf8'));","const expected=JSON.parse(fs.readFileSync(inventory,'utf8'));\n  const expectedVars=[...fs.readFileSync(file,'utf8').matchAll(/<var>([A-Za-z])<\\/var>/g)].map(m=>m[1]);")
s=s.replace('expressions:[...a.querySelectorAll(\'math-renderer\')]','variables:[...a.querySelectorAll(\'var\')].map(v=>({text:v.textContent,style:getComputedStyle(v).fontStyle,width:v.getBoundingClientRect().width,height:v.getBoundingClientRect().height})),\n     expressions:[...a.querySelectorAll(\'math-renderer\')]')
s=s.replace('const bad=[];',"""if(JSON.stringify(result.variables.map(v=>v.text))!==JSON.stringify(expectedVars))errors.push(`${slug}/${width}: semantic variable content mismatch`);
   if(result.variables.some(v=>v.style!=='italic'||v.width<=0||v.height<=0))errors.push(`${slug}/${width}: unstyled or invisible semantic variable`);
   const bad=[];""")
s=s.replace('expressions:result.expressions.length,display:', 'expressions:result.expressions.length,semanticVariables:result.variables.length,display:')
p.write_text(s)
