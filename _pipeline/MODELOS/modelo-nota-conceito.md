# Modelo — Nota de conceito

> **Regra de estilo (usuário, 2026-09-01):** nas notas FINAIS da designer, NÃO usar
> citações "(cap. NN)"/URLs inline no corpo, tabelas ou callouts — a prosa deve ser
> limpa; os capítulos vão somente no campo `fontes` do frontmatter. Ignorar as
> citações inline dos exemplos abaixo ao aplicar o modelo. (Rascunhos internos de
> `_pipeline/rascunho/` podem e devem citar capítulos inline.)

Uso: qualquer conceito do mundo/sistema (ex.: `Abertura.md`, `Essência Primeva.md`,
`Refino de Gu.md`, `Blessed Land.md`). Copiar a estrutura, não o texto.

```markdown
---
tags:
  - dominio/subtopico
aliases:
  - Termo em inglês
status: rascunho
fontes: ["cap. NN", "cap. MM"]
---

# Nome do Conceito

**Em uma frase:** o que é, dito para quem nunca ouviu falar. Defina o ==termo== aqui.

## Como funciona

Explicação completa, do zero, em prosa didática. Todo termo do mundo que aparecer
vira wikilink (ex.: [[Essência Primeva]]). Números exatos quando a obra der
(percentuais, custos, durações). Sem citações de capítulo no texto — os capítulos
ficam só no `fontes` do frontmatter.

## Regras e limites

- O que pode e o que não pode; exceções conhecidas.
- Evolução da regra ao longo da obra, se houver (versão antiga → versão madura).

## Na vida de um Mestre Gu

Como isso aparece no dia a dia / na prática, com exemplos concretos.

> [!example] Caso mecânico
> Um exemplo real da obra, descrito mecanicamente, sem enredo.

> [!note] Para o design
> O que isso sugere de jogável: progressão, risco/recompensa, economia, crafting…

## Relações

- [[Conceito vizinho]] — como se conectam.

Notas de rodapé para ressalvas de tradução ou divergência wiki × texto.[^1]

[^1]: ...
```

Estilo: escrever para uma pessoa inteligente que NUNCA leu a obra. Nada de "como
sabemos", nada de referência a personagens sem contexto. Didática de professor, não
resumo de leitor.
