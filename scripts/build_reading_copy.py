#!/usr/bin/env python3
"""Make a reading copy without editing the archived mathematical QMD source."""

import argparse
import collections
import json
from pathlib import Path
import re
import subprocess
import tempfile


TITLE = 'Large-N Convexity of Low-Threshold Stationary Polygons'
AFFILIATION = 'School of Mathematics and Statistics, HNP-LAMA, Central South University, Changsha, Hunan 410083, P. R. China'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('repository', nargs='?', default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument('--pandoc', default='pandoc')
    parser.add_argument('--xelatex', default='xelatex')
    args = parser.parse_args()
    root = Path(args.repository).resolve()
    source = root / 'project/workspace/large-n-proof.qmd'
    manifest = json.loads((root / 'project/.qmd-prover/manifest.json').read_text())
    snapshot = json.loads((root / 'archive/snapshot.json').read_text())
    facts = {fact['id']: fact for fact in manifest['results']}
    text = source.read_text()
    labels = {}
    counters = collections.Counter()
    for match in re.finditer(r'^::: \{#([A-Za-z0-9_-]+)\s+([^\n]+)\}\s*$', text, re.M):
        identifier, attrs = match.groups()
        fact = facts[identifier]
        kind = fact['kind'].replace('_', ' ').title()
        counters[kind] += 1
        labels[identifier] = kind + ' ' + str(counters[kind])
    if set(labels) != set(facts):
        raise RuntimeError('The reading copy would omit a semantic fact')
    lines = []
    declarations = []
    proof_count = 0
    for line in text.splitlines():
        opening = re.match(r'^::: \{(.*)\}\s*$', line)
        if opening:
            attrs = opening.group(1)
            identifier = re.search(r'(?:^|\s)#([A-Za-z0-9_-]+)', attrs)
            proof = re.search(r'\.proof(?:\s|$)', attrs)
            if identifier:
                identifier = identifier.group(1)
                if identifier not in facts:
                    raise RuntimeError('Unknown semantic declaration: ' + identifier)
                fact = facts[identifier]
                lines.extend(['', '## ' + labels[identifier] + ': ' + fact['title'] + ' {#' + identifier + '}', ''])
                declarations.append(identifier)
            elif proof:
                target = re.search(r'\bof="([A-Za-z0-9_-]+)"', attrs)
                if not target or target.group(1) not in labels:
                    raise RuntimeError('Unknown proof target')
                target = target.group(1)
                lines.extend(['', '### Proof of ' + labels[target] + ' {#proof-' + target + '}', ''])
                proof_count += 1
            else:
                raise RuntimeError('Unrecognized fenced div; preserve it explicitly before building')
        elif re.match(r'^:::\s*$', line):
            lines.append('')
        else:
            lines.append(line)
    rendered = '\n'.join(lines)
    unresolved = set()

    def reference(match):
        identifier = match.group(1)
        if identifier not in labels:
            unresolved.add(identifier)
            return match.group(0)
        return '[' + labels[identifier] + '](#' + identifier + ')'

    rendered = re.sub(r'(?<![\w\\])@([A-Za-z][A-Za-z0-9_-]*)', reference, rendered)
    if unresolved:
        raise RuntimeError('Unresolved reading-copy references: ' + ', '.join(sorted(unresolved)))
    if len(declarations) != len(facts) or proof_count != len(manifest['proofs']):
        raise RuntimeError('Source/result/proof counts do not agree')
    out = root / 'manuscript'
    out.mkdir(exist_ok=True)
    md = out / 'large-n-proof.md'
    tex = out / 'large-n-proof.tex'
    pdf = out / 'large-n-proof.pdf'
    md.write_text(rendered + '\n')
    when = snapshot['snapshot_completed']['asia_shanghai']
    template = r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{unicode-math}
\usepackage{longtable,booktabs,array}
\usepackage{graphicx}
\usepackage[unicode,colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\hypersetup{pdftitle={''' + TITLE + r'''},pdfauthor={Zhuo Cheng}}
\setlength{\emergencystretch}{3em}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\setcounter{tocdepth}{2}
\allowdisplaybreaks[2]
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}
\providecommand{\pandocbounded}[1]{#1}
\begin{document}
\begin{titlepage}
\centering
\vspace*{18mm}
{\LARGE\bfseries Large-N Convexity of\par Low-Threshold Stationary Polygons\par}
\vspace{12mm}
{\large Zhuo Cheng\par}
\vspace{5mm}
School of Mathematics and Statistics, HNP-LAMA,\par
Central South University,\par
Changsha, Hunan 410083, P. R. China\par
\vspace{3mm}
\href{mailto:zhuo@outlook.cz}{zhuo@outlook.cz}\par
\vspace{14mm}
{\large Proof manuscript and research snapshot\par}
\vspace{6mm}
\texttt{''' + when.replace('+', r'\char43 ') + r'''}\par
Asia/Shanghai (UTC+08:00)\par
\vfill
\begin{minipage}{0.88\textwidth}
\small
This reading copy is derived from the archived QMD manuscript without changing
its mathematical content. The original QMD, dependency graphs and verification
records are preserved separately in the repository. The recorded qmd-prover
state has 45 facts globally marked verified, including the main theorem;
the verifier configuration is Codex, gpt-6.1-sol, high effort, standard rigor
and standard citation requirements. This document records that checker state
and does not represent an additional mathematical verification run.
\end{minipage}
\vspace{8mm}
\end{titlepage}
\tableofcontents
\clearpage
$body$
\end{document}
'''
    # Temporary build products are kept outside the research repository.
    with tempfile.TemporaryDirectory(prefix='large-n-pdf-') as temporary:
        directory = Path(temporary)
        template_file = directory / 'template.tex'
        template_file.write_text(template)
        command = [args.pandoc, str(md), '--from=markdown+fenced_divs+tex_math_dollars',
                   '--to=latex', '--standalone', '--no-highlight', '--template=' + str(template_file),
                   '--metadata=title:' + TITLE, '--output=' + str(tex)]
        subprocess.run(command, check=True, capture_output=True, text=True)
        for _ in range(3):
            process = subprocess.run([args.xelatex, '-halt-on-error', '-interaction=nonstopmode',
                                      '-output-directory=' + str(directory), str(tex)],
                                     capture_output=True, text=True, timeout=120)
            if process.returncode:
                raise RuntimeError('XeLaTeX failed:\n' + process.stdout[-5000:] + process.stderr[-1000:])
        pdf.write_bytes((directory / 'large-n-proof.pdf').read_bytes())
        log = (directory / 'large-n-proof.log').read_text(errors='replace')
    report = {'source': 'project/workspace/large-n-proof.qmd', 'semantic_facts': len(facts),
              'proof_blocks': proof_count, 'unresolved_cross_references': sorted(unresolved),
              'math_source_modified': False,
              'overfull_boxes': len(re.findall(r'Overfull \\[hv]box', log)),
              'missing_glyphs': len(re.findall(r'Missing character:', log)),
              'undefined_references': bool(re.search(r'There were undefined references', log)),
              'pdf_bytes': pdf.stat().st_size,
              'pandoc_version': subprocess.check_output([args.pandoc, '--version'], text=True).splitlines()[0],
              'xelatex_version': subprocess.check_output([args.xelatex, '--version'], text=True).splitlines()[0]}
    (root / 'archive/reading-copy-build.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
