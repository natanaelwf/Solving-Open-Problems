#!/usr/bin/env python3
"""Compare complete exact results, ignoring only runtime and Python version."""
from pathlib import Path
import json
record=json.loads(Path('dujella-problem-1.7/verification_results.json').read_text())
rerun=json.loads(Path('publication-audit/evidence/final-verification.json').read_text())
for obj in (record,rerun):
    obj.pop('python_version',None)
    obj.pop('elapsed_seconds',None)
assert record==rerun,'Exact verification results differ from the recorded data.'
print('PASS: all exact results match the recorded data.')
