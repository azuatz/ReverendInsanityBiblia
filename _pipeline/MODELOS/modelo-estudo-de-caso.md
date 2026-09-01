# Modelo — Estudo de caso mecânico

> **Regra de estilo (usuário, 2026-09-01):** nas notas FINAIS da designer, NÃO usar
> citações "(cap. NN)"/URLs inline no corpo, tabelas ou callouts — a prosa deve ser
> limpa; os capítulos vão somente no campo `fontes` do frontmatter. Ignorar as
> citações inline dos exemplos abaixo ao aplicar o modelo. (Rascunhos internos de
> `_pipeline/rascunho/` podem e devem citar capítulos inline.)

Uso: notas em `08 - Estudos de Caso Mecânicos/` (ex.: `Refino de Gu Imortal em rank
3.md`). O caso existe para provar/ilustrar regras — nunca para contar história.

```markdown
---
tags:
  - caso-mecanico
  - dominio/subtopico
status: rascunho
fontes: ["cap. NN"]
---

# Título curto do caso

**Regra que este caso ilustra:** [[Nota do conceito]] — e em que sentido (confirma,
cria exceção, mostra limite).

## Situação (mínimo necessário)

Uma ou duas frases de contexto mecânico: quem (por rank/recursos, não por biografia),
com o quê, tentando o quê.

## O método, passo a passo

1. ...
2. ...
Cada passo com o recurso gasto/risco corrido e o porquê mecânico.

## Por que funcionou (ou falhou)

A explicação de sistema: que regras se combinaram, que brecha foi usada, que preço
foi pago.

> [!warning] É exceção ou regra?
> Deixar explícito se isso é replicável por qualquer um nas mesmas condições ou se
> dependeu de circunstâncias raras — e quais.

> [!note] Para o design
> O que o caso ensina para o jogo: pode virar regra opcional? aventura? exploit a
> prever nas regras?
```
