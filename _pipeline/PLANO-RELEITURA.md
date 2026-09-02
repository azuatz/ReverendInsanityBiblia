# Plano da releitura completa e do fechamento de lacunas (sessão de 2026-09-02)

Pedido do usuário: reler a obra inteira a partir do repositório-fonte, verificar se está
tudo completo, acrescentar o que falta, escrever os **grandes eventos** do mundo como
cenários jogáveis, e completar o dossiê de **forças e organizações por região**. Tudo em
modo automático: onde houver decisão, tomar a recomendada, registrar, e seguir.

## Decisões tomadas automaticamente (com a alternativa descartada)

1. **O que significa "reler a obra inteira".** Descartado: repetir a leitura linear dos
   28 MB, que só duplicaria a primeira passada. Adotado: uma segunda varredura completa
   dos 2.334 capítulos com **lentes novas** — eventos e completude por domínio —, usando
   as notas brutas da primeira leitura como índice e voltando sempre ao texto-fonte para
   ler o trecho de verdade. Cobre a obra toda e produz material novo em vez de repetido.
2. **Onde moram os grandes eventos.** Descartado: enfiá-los em `04 - Mundo` ou na nota de
   eventos institucionais da pasta de economia, que trata de instituições recorrentes
   (leilões, convenções), não de acontecimentos. Adotado: pasta própria,
   `08 - Eventos e Cenarios/`, com Estudos de Caso passando a `09` e Apêndices a `10`,
   para que os apêndices continuem sendo a última coisa do currículo.
3. **Como um evento entra sem virar spoiler.** O evento entra como **situação**, nunca
   como história: causa mecânica, geografia, perigos, regras especiais do local, forças
   presentes como tipos e facções, prêmios, relógio, desfechos possíveis. Fica de fora
   quem venceu, quem morreu e o papel de personagens nomeados. É a política de spoiler do
   projeto aplicada a acontecimentos, e é o que o usuário pediu: os jogadores estão no
   evento pelo ambiente e pelo contexto, mas a história dentro dele é deles.
4. **Onde moram as forças e organizações.** Descartado: engordar
   `05 - Sociedade/07 - As Grandes Forças do Mundo.md`, que já é uma visão geral e não
   comporta ficha por organização. Adotado: pasta própria, uma nota por região, com ficha
   padronizada por clã, seita, tribo, templo ou cidade.
5. **Recorte temporal das fichas de força.** As fichas descrevem cada organização **como
   ela está no presente do cenário** — o estado de coisas com que uma campanha começa.
   Líder e rank entram porque são status quo do mundo, não trama; o que o enredo faz com
   elas depois fica de fora.
6. **Numeração das notas novas.** Agentes criam notas com prefixo continuando o maior
   número da pasta e informam a posição correta de leitura; o orquestrador arruma tudo no
   fim com `numerar-notas.py`, que passou a ser idempotente exatamente para isso.

## Ondas

- **Onda 1 — varredura de eventos** (6 agentes, faixas de ~400 capítulos cobrindo 1-2334)
  → `_pipeline/notas/eventos-caps-*.md`.
- **Onda 2 — auditoria de completude por domínio** (7 agentes: cultivo, Gu, paths, mundo,
  sociedade+veneráveis, economia, apêndices) → `_pipeline/AUDITORIA-*.md` + correção
  aplicada nas notas de cada pasta.
- **Onda 3 — forças e organizações por região** (5 agentes, um por região)
  → pasta de forças + `_pipeline/pesquisa/forcas-*.md`.
- **Onda 4 — escrita das notas de evento** a partir das notas brutas da onda 1.
- **Onda 5 — catálogos** (varredura extra de Gu, deduplicação, catálogos novos).
- **Onda 6 — integração**: entrada das notas novas no guia da designer, nas trilhas de
  jogador e de mestre, renumeração, auditoria de links, revisão de leitora leiga.

## Lembrete de processo

O limite é de 20 agentes simultâneos. Agentes paralelos precisam de **posse exclusiva de
arquivo**; nomes de arquivo temporário únicos por agente; nenhum agente commita.
