# Plano de processamento da obra

Fonte: `/home/azuatz/Documentos/Reverend-Insanity-fonte/Volumes/` (capítulos .xhtml,
numeração global contínua entre volumes).

Estratégia: blocos de ~40 capítulos (~500 KB) por agente `leitor-ri`, em levas de até
5 leitores paralelos por volume. Após cada leva completa, consolidação via
`sintetizador-ri` + commit. Blocos dos volumes 2–6 são definidos ao iniciar cada
volume (conferir numeração e tamanho com `ls` + `stat`).

## Volume 1 — A Demon's Nature Doesn't Change (caps 0–199)

| Bloco | Capítulos | Nota bruta |
|---|---|---|
| 1.1 | 0–39 | `notas/notas-caps-0000-0039.md` |
| 1.2 | 40–79 | `notas/notas-caps-0040-0079.md` |
| 1.3 | 80–119 | `notas/notas-caps-0080-0119.md` |
| 1.4 | 120–159 | `notas/notas-caps-0120-0159.md` |
| 1.5 | 160–199 | `notas/notas-caps-0160-0199.md` |

## Volumes 2–6 (numeração contínua, sem buracos)

| Volume | Capítulos | Blocos (~41 caps) |
|---|---|---|
| 2 — The Demon Leaves the Mountain | 200–405 (206) | 5 |
| 3 — The Demon Wreaks Chaos in the World | 406–649 (244) | 6 |
| 4 — The Demon Lord Rampages Unhindered | 650–1021 (372) | 9 |
| 5 — Demon King's Domination | 1022–1966 (945) | 23 |
| 6 — Demon Venerable's Eternal Life | 1967–2334 (368) | 9 |

Execução: levas de até 6 leitores paralelos; commit a cada bloco; sintetizador por
volume, sempre em série (editam os mesmos rascunhos); leitura do volume seguinte
pode começar enquanto a consolidação do anterior roda.

## Fases do projeto

1. Leitura integral (volumes 1–6, leva a leva), consolidando sempre em rascunhos
   internos (`_pipeline/rascunho/`, organização por `TAXONOMIA.md`).
2. Pesquisa externa (wiki reverendinsanity.fandom.com, Reddit) para lacunas e debates
   — também para os rascunhos.
3. Escrita final: só com a obra inteira lida, escrever as notas didáticas das pastas
   `01`–`09` a partir dos rascunhos, no formato de `_pipeline/MODELOS/`.
4. Passe de verificação (grep no texto para as afirmações centrais) + LEIA-ME final.
