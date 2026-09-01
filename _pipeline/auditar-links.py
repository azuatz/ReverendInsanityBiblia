#!/usr/bin/env python3
"""Auditoria de wikilinks do vault.

Rode a partir da raiz do vault:  python3 _pipeline/auditar-links.py

Classifica cada wikilink em três categorias:
  - exato    : aponta para o nome de arquivo real. Sempre funciona.
  - alias    : só resolve pelo campo `aliases` do frontmatter do destino.
               FRÁGIL — o Obsidian pode falhar e criar arquivo novo ao clicar.
               Devem ser convertidos para [[Arquivo Real|texto mostrado]].
  - quebrado : não existe destino nenhum.

Ignora links dentro de crase (código inline) e de blocos de código, que são
documentação de convenção e não links de verdade.
"""
import re, io, os, glob, sys

def limpar_codigo(t):
    t = re.sub(r"```.*?```", "", t, flags=re.S)   # blocos de código
    t = re.sub(r"`[^`\n]*`", "", t)               # código inline
    return t

def main():
    files = sorted(glob.glob("0*/*.md") + glob.glob("*.md"))
    fname, alias = {}, {}
    for p in files:
        b = os.path.basename(p)[:-3]
        fname[b] = p
        m = re.match(r"^---\n(.*?\n)---\n", io.open(p, encoding="utf-8").read(), re.S)
        if m:
            a = re.search(r"^aliases:\s*\n((?:  - .*\n)+)", m.group(1), re.M)
            if a:
                for l in a.group(1).strip().split("\n"):
                    alias.setdefault(l.strip()[2:].strip(), p)

    exato = 0
    so_alias, quebrado = {}, {}
    for p in files:
        t = limpar_codigo(io.open(p, encoding="utf-8").read())
        for lk in re.findall(r"\[\[([^\]|#\n]+)", t):
            lk = lk.strip()
            if lk in fname:
                exato += 1
            elif lk in alias:
                so_alias.setdefault(lk, set()).add(os.path.basename(p))
            else:
                quebrado.setdefault(lk, set()).add(os.path.basename(p))

    print("notas no vault: %d" % len(files))
    print("links por nome exato de arquivo: %d  (ok)" % exato)
    print("links que dependem só de alias: %d destinos  (frágil)" % len(so_alias))
    for k, v in sorted(so_alias.items()):
        print("   ~ %s  <- %s" % (k, ", ".join(sorted(v))[:70]))
    print("links quebrados: %d" % len(quebrado))
    for k, v in sorted(quebrado.items()):
        print("   X %s  <- %s" % (k, ", ".join(sorted(v))[:70]))
    return 1 if quebrado or so_alias else 0

if __name__ == "__main__":
    sys.exit(main())
