# Modelo — Catálogo de Gu

> **Regra de estilo (usuário, 2026-09-01):** nas notas FINAIS da designer, NÃO usar
> citações "(cap. NN)"/URLs inline no corpo, tabelas ou callouts — a prosa deve ser
> limpa; os capítulos vão somente no campo `fontes` do frontmatter. Ignorar as
> citações inline dos exemplos abaixo ao aplicar o modelo. (Rascunhos internos de
> `_pipeline/rascunho/` podem e devem citar capítulos inline.)

Uso: `11 - Apêndices/Catálogo de Gu.md` — tabela mestra de todos os Gu da obra,
dividida por path (uma seção `## Path` por path, Gu Imortais com ⭐ no nome). Gu
especialmente importantes ganham nota própria além da linha na tabela.

Formato da tabela:

```markdown
| Gu | Rank | Efeito | Alimento | Nota própria |
|---|---|---|---|---|
| Moonlight Gu | 1 | Lâmina de luz lunar cortante | folhas prateadas | [[Moonlight Gu]] |
| ⭐ Spring Autumn Cicada | 6 | (ver nota) | (ver nota) | [[Spring Autumn Cicada]] |
```

Regras:
- "Efeito" em até ~12 palavras, para leigos; detalhe vai na nota própria.
- Campo desconhecido = "—" (nunca inventar rank/path/alimento).
- Sem citações de capítulo na tabela; os capítulos de origem ficam no `fontes` do
  frontmatter do catálogo e nas notas brutas do `_pipeline/`.
- Nota própria de Gu segue o modelo de nota de conceito, com seções "Como funciona",
  "Alimentação", "Como se obtém/refina" e "Para o design".
```
