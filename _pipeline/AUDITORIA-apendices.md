# Auditoria dos apêndices de referência (`10 - Apendices/`)

Agente: auditor dos apêndices. Escopo exclusivo: `01 - Glossário EN-PT.md`,
`02 - Tabelas de Referência Rápida.md`, `09 - Linha do Tempo e Eras.md`.
Os catálogos `03`–`08` pertencem a outro agente e **não foram tocados**.

Convenção de origem usada nas três notas (a mesma do vault): texto simples =
canônico; `(ded.)` / `inferido` = dedução segura; `*` = invenção nossa; `—` = a
obra não informa.

Status: **em andamento** — este arquivo é escrito incrementalmente.

---

## Glossário

### Bug crítico encontrado e corrigido: o termo em inglês está errado no vault inteiro

A obra **nunca** escreve "primordial essence", "primordial sea" ou "primordial
stones". A grafia canônica em inglês é **`primeval essence` / `primeval sea` /
`primeval stones`**. Contagem no texto-fonte (`grep -io`, seis volumes):

| Forma | Ocorrências na obra |
|---|---|
| `primeval essence` (só no Volume 1) | 672 |
| `primeval sea` | 175 |
| `primeval stone(s)` | 1.194 |
| `primordial essence` | **0** |

"Primordial" existe na obra, mas designa **outra coisa**: o nome próprio
`Primordial Origin Immortal Venerable` (o primeiro rank 9) e o `Primordial
Domain`. Ou seja, escrever "primordial essence" como termo inglês colide com o
nome de um Venerável.

Além do erro de raiz, a grafia estava **corrompida com um L a mais**
("primordiall essence"), sinal de uma substituição automática mal feita em algum
momento da construção do vault.

Nada disso afeta o **português**: a tradução brasileira publicada de fato escreve
"essência primordial" / "mar primordial" / "pedra primordial", e é a forma que o
vault deve continuar usando. O erro estava só na coluna do termo em inglês.

