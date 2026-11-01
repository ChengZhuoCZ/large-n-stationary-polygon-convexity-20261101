#!/usr/bin/env python3
"""Verify the archived files without calling a model or changing the project."""
import hashlib
import json
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
checked = 0
for line in (root / 'CHECKSUMS.sha256').read_text().splitlines():
    expected, relative = line.split('  ', 1)
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise SystemExit('Missing or unsafe archive entry: ' + relative)
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit('Checksum mismatch: ' + relative)
    checked += 1
source = json.loads((root / 'archive/source-manifest.json').read_text())
for entry in source['files']:
    path = root / entry['export_path']
    if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256_export']:
        raise SystemExit('Captured source mismatch: ' + entry['export_path'])
graph = json.loads((root / 'project/.qmd-prover/graph.json').read_text())
assert len(graph['nodes']) == 45
assert not graph['cycles']
assert all(n['global_verification']['status'] == 'verified' for n in graph['nodes'])
print(json.dumps({'files_verified': checked, 'source_files_verified': len(source['files']),
                  'recorded_facts': 45, 'recorded_global_status': 'verified',
                  'model_requests_made': 0}))
