#!/usr/bin/env python3
"""One-time typography repair; checked against the immutable source inventory."""
from pathlib import Path
import base64,hashlib,json,zlib
DATA='eNrNV9tO6zgU/ZWIh8qW40PjpD30oQ9wLiMhwQjmBYRJlRtt1TZM27QDE/nfZ9txbjQpOQiNDhK52Gtf1ra9uvPwcPJ9kjrmwmUCXeMx508bL0iZmzqnthCpzfkf3mrlIXZqY9cWnAM0hRd4+h4tEw8t8LWbWmpg+Tw1rnlM/pwskB7E5ol5wrkfTedx6i3n0zgKBY+rMXufEVT+xT3O1zsvrMfnMedRHBbBTx7Nh5MIUppPlyhGHvFJgAnz/ICwzTZRExvM43HsMo1CAfWoj11GHeT5JMYa9KWRW+9951m2XSI0Zl/1jwmKZQAc0Egbgdd4rP0gL5BXX15b0n3fm063yWVLfsvoCcjuo01icL5dw+0b1Q/n+cMF55v5dKZxkHK+Da5Eim5JhkrPLwRGuQ+S+8gfLrCQGSyjim1h+E2IVsofSFBX4YNZ5hu0PdXGUrINeoFd4YU0xtTTS8VeXglboxfyiskaZtkmJLFernG/hXPVU+24dHXbthXfBALQcgmuV/OQLUwIIWPIIs+nK4g0B0BKLdPiXBSzq6KqGmcsZHHAkcTIXHcJ3W9741XF4TQI0c7cS82Sj1szwWNLwz25TmBu7LaFha+H9kkxtMmHtqQIfCgYZTmnXjKLNiXNrixlSsc5ZvaKpSIpLd6h+A5DiTnKryCjF3K7W03kjtz528QLFqklN6uxg2ti7MFhteRW5v8v9aZw925qnzIhVGkUT87BP2i1hIg0g2YqLsrDfj7RMONSpEzL+T0oeHpj5udOn1IFq41NZKGfkleBrHZx+z9p1SXi87h1PnrzOJlYrjY1fk7u0Q54mOEuS6s2/ZCghFj40U2p+mmNM1VEWfYW0/lS/W6rd5QZYS2NeELCN8poXLKCaWPuLevUnnrh/rdIv630ehOZN9DQWGavOLEmW5yqU6jGq2oGo+vdfJ/Pc/736jk0bjTGuUXn5BajC7jk0H6GSWXnpGHnhzJw0TtUuttSCRZfuipcSUllrjw18KrT6s7q10i91bZGRnVN+yH7QDxmhQiUki3uJtlrfKgQXbVBu2hTiGy2SSdUg3rXIllZ0r3fL+vDHvuu5XjoumvHl6qhD8LnxMl79n+lgDLcobGv9fLHC/YZ4dq/Izp0ukg2TdAZy9soxm/aWwmVU+RKIcjoSq0HugI9QiN5XbtOl371aJiyzTyIVc7UQzYSm+Xl9JBPWAJ74R+yL3pt1bXm7Ywn0kDuDlMi9ZwfiPzZgNhVM8BLrK1n/Qqumf2s15xLtaP+1YQObI9l1VigQB03HdKBXt4W8AFlD31iDUvG1dkRG1zBWqhpaWuxAQzYzaSD3nH/B58TTUFyTBmr468Z/BrSoTNTjmbwryXXB1UaDGeuQy12NnNt6pxpjAYE8JHYHwFiSLP7gA4sBgbEsgZwtyUWtu3Z2Yx+1TZhacP60uGAWl9Hymjo9KUNO5NhZDBqDbr1E59OoC4MH2FT99CNWrY6an1D6tNAtpHwGS6JUbDASHK0qc2UEyCKxyAB08Tom21CUndWftof8ZmDctctaaae6ZuBCR1CtiZLH0JFRjG6Ue85uAnaCFT2TT7fANUx9kKp5MtJbISnKB/z5dEOsHJwDGUA5vHxP0CBePU='
b=zlib.decompress(base64.b64decode(DATA))
assert hashlib.sha256(b).hexdigest()=='be44585e8344bbdc0f1c130f311908d08b67ea0ecf68c73984bc539b320e8abc'
p=Path('dujella-problem-1.7/README.md')
s=p.read_text()
assert hashlib.sha256(s.encode()).hexdigest()=='c1ac6947e8a4ac9d581e80f38b6670c29a7ff5826bdb51e204f07bf4a0f26f12'
for old,new in json.loads(b):
    assert old in s,old
    s=s.replace(old,new)
s=s.replace('| k | Delta(k) | E_k(10^9) |','| k | Density factor | Principal-family count |')
p.write_text(s)
p=Path('publication-audit/check_source.py')
s=p.read_text().replace('def canonical(s):','def canonical(s):\n    # Named delimiters preserve visible set braces through GitHub parsing.\n    s=s.replace(r"\\{",r"\\lbrace").replace(r"\\}",r"\\rbrace")')
p.write_text(s)
p=Path('publication-audit/render.mjs')
s=p.read_text()
s=s.replace("[['index','README.md'],['article','dujella-problem-1.7/README.md']]","[['index','README.md','blob'],['article','dujella-problem-1.7/README.md','blob'],['index-landing','README.md','tree'],['article-landing','dujella-problem-1.7/README.md','tree']]")
s=s.replace('[slug,file] of','[slug,file,mode] of')
s=s.replace('const url=`${origin}/blob/${sha}/${file}`;','const url=mode===\'blob\'?`${origin}/blob/${sha}/${file}`:`${origin}/tree/${sha}/${file.includes(\'/\')?file.slice(0,file.lastIndexOf(\'/\')):\'\'}`;')
old="""   await page.waitForFunction(()=>[...document.querySelectorAll('article.markdown-body math-renderer')].every(e=>e.querySelector('math,mjx-container')),null,{timeout:120000});
   await page.waitForTimeout(1000);"""
new="""   // Trigger any viewport-dependent work before judging missing output.
   for(let y=0;y<await page.evaluate(()=>document.documentElement.scrollHeight);y+=view.height-100){
    await page.evaluate(y=>window.scrollTo(0,y),y);await page.waitForTimeout(40);
   }
   await page.evaluate(()=>window.scrollTo(0,0));
   try{await page.waitForFunction(()=>[...document.querySelectorAll('article.markdown-body math-renderer')].every(e=>e.querySelector('math,mjx-container')),null,{timeout:60000});}
   catch(e){fs.writeFileSync(`${out}/output-wait-${width}.txt`,String(e));}
   await page.evaluate(()=>document.fonts.ready);
   await page.waitForTimeout(1000);"""
assert old in s
s=s.replace(old,new)
s=s.replace('const child=output?.firstElementChild;',"""const children=output?[...output.children].map(c=>c.getBoundingClientRect()).filter(r=>r.width>0&&r.height>0):[];
      const inner=children.length?{left:Math.min(...children.map(r=>r.left)),right:Math.max(...children.map(r=>r.right)),top:Math.min(...children.map(r=>r.top)),bottom:Math.max(...children.map(r=>r.bottom))}:null;
      if(inner){inner.width=inner.right-inner.left;inner.height=inner.bottom-inner.top;}""")
s=s.replace('inner:child?clean(child.getBoundingClientRect()):null','inner')
s=s.replace("if(e.kind==='display'&&e.inner&&e.inner.width>e.rect.width+2)","if(e.inner&&(e.inner.width>e.rect.width+2||e.inner.left<result.article.left-2||e.inner.right>result.article.right+2))")
p.write_text(s)
print('Repaired parser-sensitive markup and long equations; expanded live layout checks.')
