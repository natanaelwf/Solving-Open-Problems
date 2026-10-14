#!/usr/bin/env python3
"""Transport the audited publication files with an exact integrity check."""
from pathlib import Path
import base64,hashlib,json,lzma
parts=[Path(f'publication-audit/transfer-{i}.txt') for i in range(1,6)]
b=base64.b64decode(''.join(p.read_text() for p in parts),validate=True)
assert hashlib.sha256(b).hexdigest()=='4c82a93b8222d2f2d2a236f2c0ce578955d23d4d25553658ca8b10ddd7220a0b'
files=json.loads(lzma.decompress(b))
for name,text in files.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    assert p.parts[0] in ('dujella-problem-1.7','publication-audit')
    assert isinstance(text,str)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(text,encoding='utf-8')
print(f'Restored {len(files)} checked UTF-8 publication files.')
