---
tags:
  - pipeline/dados
  - gu/evolucao
  - gu/fusao
  - gu/compatibilidade
status: verificado-no-texto
fontes: ["cap. 17", "cap. 47", "cap. 62", "cap. 64", "cap. 76", "cap. 98", "cap. 104", "cap. 105", "cap. 106", "cap. 107", "cap. 109", "cap. 111", "cap. 121", "cap. 123", "cap. 126", "cap. 129", "cap. 152", "cap. 155", "cap. 156", "cap. 157", "cap. 163", "cap. 166", "cap. 183", "cap. 185", "cap. 187", "cap. 192", "cap. 194", "cap. 222", "cap. 230", "cap. 266", "cap. 275", "cap. 280", "cap. 289", "cap. 290", "cap. 291", "cap. 292", "cap. 298", "cap. 301", "cap. 307", "cap. 308", "cap. 316", "cap. 320", "cap. 326", "cap. 343", "cap. 345", "cap. 353", "cap. 354", "cap. 355", "cap. 374", "cap. 412", "cap. 428", "cap. 442", "cap. 443", "cap. 452", "cap. 454", "cap. 457", "cap. 463", "cap. 504", "cap. 507", "cap. 522", "cap. 526", "cap. 544", "cap. 548", "cap. 558", "cap. 560", "cap. 569", "cap. 570", "cap. 573", "cap. 574", "cap. 579", "cap. 678", "cap. 734", "cap. 746", "cap. 758", "cap. 831", "cap. 853", "cap. 854", "cap. 855", "cap. 1065", "cap. 1069", "cap. 1288", "cap. 1444", "cap. 1540", "cap. 1562", "cap. 1578", "cap. 1680", "cap. 1852", "cap. 2072", "cap. 2108", "cap. 2140", "cap. 2235", "cap. 2247", "cap. 2252", "cap. 2298"]
---

# Árvores de evolução, séries de rank e interações entre Gu

**Este arquivo não é uma nota para a designer.** É o **conjunto de dados** de que os
agentes que reescrevem os catálogos por rank vão se alimentar. Cada aresta aqui foi
conferida no texto-fonte e traz o capítulo. Uma aresta errada se propaga para seis
catálogos — então, onde a obra não confirma, este arquivo **diz que não confirma** em
vez de completar a figura.

## Como este arquivo foi feito

### Fontes e método

1. Ponto de partida: `11 - Apendices/06 - Catálogo de Receitas.md`,
   `11 - Apendices/04 - Catálogo de Gu - Mortais.md` e
   `11 - Apendices/05 - Catálogo de Gu - Imortais.md`.
2. Verificação no texto-fonte (`Reverend-Insanity-fonte/texto/Volume_*.txt`), sempre com
   busca **insensível a maiúsculas** — a obra grafa nomes de Gu em minúsculas
   ("brave fight Gu", "moonglow Gu"), e busca sensível perde a maior parte das ocorrências.
3. Construções que se mostraram produtivas: `fuse … to form`, `refined from`,
   `advancement of the rank`, `advancement route`, `advancement path`, `series Gu`,
   `rank … version`, `main material`, `reverse refine`, `interfere`.
4. Cada afirmação do catálogo que **não** encontrou respaldo no texto está registrada
   abaixo, na seção de correções, em vez de ser silenciosamente reproduzida.

### Convenção de confiabilidade (a mesma do vault)

| Marca | Significa |
|---|---|
| texto simples | a obra afirma, e o capítulo está na aresta |
| `(ded.)` | dedução segura a partir de algo que a obra afirma |
| `*` | invenção ou indução nossa, **sem base textual** |
| `—` | a obra não informa e nada foi preenchido |

Apagar tudo marcado com `*` devolve este arquivo a cem por cento canônico. Neste
documento o `*` aparece **duas vezes**, ambas sinalizadas no ponto em que ocorrem.

### As três coisas distintas que este arquivo separa

Confundi-las é o erro mais fácil de cometer ao ler os catálogos, e a fonte de metade
das imprecisões que corrigi:

1. **Evolução (árvore).** Um Gu de rank N é **consumido** para produzir um Gu de rank
   N+1 com **nome diferente**. É a árvore propriamente dita. Ex.: Moonlight → Moonglow.
2. **Série (linha de produto).** Vários Gu de ranks diferentes com **nomes diferentes**
   que *não* se transformam uns nos outros — cada um tem receita própria e se compra
   separado. Ex.: jin strength Gu / strength of ten jin Gu / jun strength Gu; a série
   dos Relic Gu. **Não é árvore**, e tratá-la como árvore é erro.
3. **Mesmo Gu em ranks diferentes.** O **mesmo nome** cobre dois ou mais ranks, às vezes
   com efeitos diferentes. Ex.: bronze skin Gu (ranks 1–3), Spring Autumn Cicada
   (já foi rank 9, hoje é rank 6). Está na seção *Pares de rank sem nome próprio*.

Há ainda um caso híbrido, e a obra o descreve com todas as letras: uma **série cujos
degraus são material um do outro** — cada rank tem nome e receita próprios, e a receita
do rank N+1 exige o rank N como material principal. É o caso da linhagem do fogo
(charcoal → stove → hut → tower → pagoda). Tratei essas como árvore, porque
funcionalmente são.

### Regra geral do mundo que rege as árvores

- **A fusão herda uma só habilidade.** O Gu novo pega **uma** das habilidades dos
  componentes e perde as demais — é por isso que White Boar + Jade Skin dá um Gu de
  defesa pura, e a força se perde (cap. 105).
- **A fusão consome os componentes.** Escolher um galho queima os outros.
- **A fusão pode falhar**, e a falha fere ou mata os componentes; um Gu ferido perde
  brilho e tem chance de sucesso muito menor até se recuperar (cap. 106).
- **O Gu vital nunca morre numa falha de fusão** — no pior caso fica quase morto e se
  recupera (cap. 106).
- **Um Gu pode regredir de rank por fome.** Um Liquor worm de rank 5 caiu a rank 1 por
  décadas de subalimentação (cap. 17); um Mist Perspiring Butterfly reverteu a Liquor
  worm pelo mesmo motivo, depois que o dono morreu (cap. 105). A árvore corre nos dois
  sentidos, e o sentido descendente é gratuito e involuntário.
- **Para subir um Gu Imortal de rank, a versão inferior é consumida como material
  principal** (cap. 1444, sobre o Cleanse Soul rank 6 → rank 7).
- **Acima do rank 6 o nome do Gu Imortal não muda ao subir de rank** (cap. 463) — a
  razão pela qual tantos Gu Imortais aparecem em dois ou três ranks com o mesmo nome.
