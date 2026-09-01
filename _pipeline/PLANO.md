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

## Volumes 2–6

A definir ao chegar em cada um (mesmo esquema). Tamanho total da obra: ~28 MB.

## Fases posteriores

1. Leitura integral (volumes 1–6, leva a leva, consolidando sempre).
2. Pesquisa externa (wiki reverendinsanity.fandom.com, Reddit) para lacunas e debates.
3. Passe de verificação (grep no texto para cada afirmação central) + LEIA-ME final.
