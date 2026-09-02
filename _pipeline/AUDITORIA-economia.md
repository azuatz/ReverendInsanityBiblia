---
tags:
  - pipeline/auditoria
  - economia
status: em-andamento
---

# Auditoria de completude — `06 - Economia e Vida`

> Auditoria de **completude** da pasta de economia, com correção aplicada. Método: leitura
> das 12 notas finais + `_pipeline/rascunho/economia-e-vida.md` + topo de `LACUNAS.md` +
> seção de economia da tabela soberana, seguida de varredura dirigida ao **texto-fonte**
> (`grep -i` em `/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/`) atrás dos
> assuntos que não haviam chegado às notas finais.
>
> Escopo escrito: todas as notas de `06 - Economia e Vida/` e este relatório.

## Lacunas encontradas

Severidade: **bloqueador** (a designer não consegue fazer o que a pasta promete),
**sério** (falta um assunto inteiro que a obra documenta bem), **menor** (número errado,
imprecisão, oportunidade perdida).

### Bloqueadores

1. **Não havia como montar a planilha de preços que a pasta promete.**
   A nota `02 - Pedras Primordiais` se declara "fonte única de preços do vault" e traz
   **20 linhas de preço**. Uma varredura por `<número> primeval stones` no texto-fonte
   devolve **448 ocorrências**, das quais mais de uma centena são preços de cena
   utilizáveis. A obra dá muito mais do que a pasta registrava: séries completas de preço
   por rank dentro de uma mesma família de Gu, tabela de acesso por anel de cidade,
   spread entre preço de compra e de venda, curva de inflação de um insumo ao longo de uma
   crise, capacidade de Gu de armazenamento, taxas de aluguel por padrão de imóvel.
   Evidência do tamanho do buraco: só o cap. 442 traz a escada
   `jin strength Gu (r1) 220 → strength of ten jin (r2) 690 → jun strength (r3) 4.550 →
   strength of ten jun (r4) 36.000` — a mesma linha de produto em quatro ranks, que é
   exatamente o dado que calibra uma economia de jogo, e ele não estava em lugar nenhum.

2. **Não havia como montar a planilha de renda.** A nota `03` traz 11 linhas de renda,
   todas de *trabalho*. Faltava inteiramente a **renda de patrimônio**, que é a metade
   que decide se um personagem escapa da roda-viva: quanto rende uma nascente espiritual
   (cap. 421: ≥100 milhões de pedras ao longo de 50–60 anos por nascente pequena), quanto
   rende a versão portátil dela (cap. 273: **50 pedras por dia**, número que a pasta nunca
   registrou), qual o prazo de retorno de um negócio comprado (cap. 112: "os stones
   gastos seriam repostos com **dois ou três anos** de operação"), e qual o resultado de
   uma prova de multiplicação de capital (caps. 322–333: 100.000 de capital inicial →
   440.000 em pouco mais de dois meses).

3. **Custo de vida acima do rank 1 estava marcado como inexistente na obra, e não é.**
   As notas `03` e `06` afirmam corretamente que a obra nunca *tabela* o consumo por
   rank, mas deixavam a impressão de que não há nenhuma âncora acima do rank 1. Há uma,
   explícita: cap. 278, um Mestre Gu de rank 3 em cidade-mercado calcula que
   **"420.000 pedras não me durariam nem um ano"** — duas ordens e meia de grandeza acima
   das 3 a 5 pedras/dia do rank 1, na mesma frase em que a obra repete que "quanto maior o
   rank, maiores as despesas".

### Sérios

4. **Impostos, tributos, taxas e pedágios: assunto inteiro ausente.** A obra documenta
   pedágio de entrada de cidade **escalonado por anel** (cap. 259–261), pedágio de estrada
   institucionalizado e negociado (caps. 240–241, os macacos-bandidos de Fei Hou), taxa de
   corretagem de mercado que escala com o valor do item (cap. 1885), taxa de inscrição de
   evento (caps. 829, 1698), taxa de ilha recém-conquistada (cap. 1899) e **mensalidade de
   aliança paga em pontos de recurso** (caps. 2275–2276). Nada disso estava nas notas.

5. **Crédito, dívida, penhor e agiotagem no mundo mortal: ausente.** A pasta cobria com
   cuidado o crédito *imortal* (nota `11`) e mencionava "agiota" numa linha da nota `03`.
   A obra dá o sistema mortal inteiro: agiotas a que um ancião de clã recorre por
   300.000 pedras num dia, **penhor de um Gu** para levantar os 200.000 restantes
   (caps. 295–296), casa de penhores como esconderijo de bem suspeito (cap. 284),
   empréstimo entre membros de clã com recibo assinado (cap. 155), **servidão por dívida
   com prazo** — vinte anos de serviço para quitar (cap. 329) — e a hipoteca de um imóvel
   como forma de levantar dinheiro em vinte e quatro horas (cap. 112).

6. **Contratos e a tecnologia que os faz valer: ausente.** O `poison vow Gu` (voto
   venenoso) é o instrumento contratual do mundo — rank 3, consumível, 4.500 pedras,
   exige ficha de acesso para comprar, bebe o sangue dos dois contratantes e explode em
   sangue estragado se um dos lados leu a cláusula sem a intenção verdadeira. A obra
   explicita que **contrato em papel não basta** ("não confio num acordo de papel, temos
   que jurar", cap. 268) e descreve uma **corrida armamentista contratual** — voto venenoso
   → Gu de comer as próprias palavras (quebra votos) → Gu do papel preto e branco
   (imune ao anterior) → Gu de distorcer preto e branco (cap. 278). Nada disso estava
   na pasta de economia.

7. **Corretagem e intermediação: ausente.** A obra trata o intermediário como instituição
   política, não como conveniência: paga-se *através* de um terceiro para não parecer que
   se pagou ("é o jeito do caminho correto", cap. 1305); há corretora profissional de
   oportunidades em quem tanto demoníacos quanto independentes confiam (cap. 1224); e um
   Venerável exige que um rival sirva de intermediário como prova de sinceridade
   (cap. 2251).

8. **Materiais e cadeia produtiva: assunto inteiro ausente.** Não havia nota nenhuma
   sobre de onde saem as matérias-primas, quem as extrai, quem as compra e quanto valem —
   apesar de a obra publicar o catálogo do mercado imortal item a item (caps. 466, 666:
   "Gu, receitas, golpes, rebanhos, humanos variantes, vegetação, **veios de minério,
   solo, água**, vinho fino"), o deserto de minério gerido por uma super força com
   mineiros escravos (cap. 1474), a divisão étnica do trabalho entre raças variantes
   (cap. 799) e a regra de que **o Gu pertence à região onde foi refinado, não à região de
   onde veio o material** (cap. 469) — que é a regra que decide se vale a pena transportar
   insumo entre regiões.

9. **Mercado negro, contrabando e recompensas por cabeça: cobertura de uma linha.** A obra
   dá o mercado negro mortal de bens desviados (cap. 520), o mercado negro *de revenda*
   dentro do próprio mercado imortal, criado por oferta menor que a demanda (caps. 1199,
   1451), a mecânica completa do mandado de prisão (caps. 234, 259, 271, 293) e — o dado
   que organiza tudo — a **escada canônica de lucro por grau de honestidade** (cap. 243):
   comércio honesto 7 a 8 vezes (declarado como o teto do mundo), métodos ilegais mais de
   10 vezes, fraude aberta dezenas de vezes, assalto "não precisa nem de capital".

10. **A tabela soberana e a nota `02` divergiam do texto no preço de entrada de cidade.**
    Ver a seção de divergências.

### Menores

11. Nota `02` dizia "entrada numa cidade grande: 1 a 10 pedras por pessoa". A faixa real
    documentada vai de **1 a 600** por pessoa, escalonada por anel.
12. A pasta nunca registrou o **spread entre preço de compra e de venda**, embora ele
    esteja em cena: uma loja compra um Gu de rank 1 por ~250 e o mercado o revende por
    ~500 (caps. 262 e 278). Sem isso a designer lê os dois números como contradição.
13. A pasta menciona "fichas destravam compras" sem nunca dizer que elas **também dão
    desconto quantificado**: a ficha de topo cortou 1.500 de um item de 4.500, um terço do
    preço (cap. 272).
14. A capacidade dos Gu de armazenamento de dinheiro nunca aparece, embora seja o que
    define quanto um personagem consegue carregar: 30.000 pedras num Gu de rank 3 comum,
    **1.000.000** no Gu de armazenamento especializado, que custa 6.600 em leilão
    (caps. 161, 268, 422).
15. Nenhuma nota registrava que **noventa por cento das transações do mercado imortal são
    escambo puro** (cap. 2245), o que muda a leitura de toda a nota `11`.
16. A nota `03` descreve caravanas sem dizer **quem protege a estrada** e a que preço.

## O que foi corrigido

### `01 - Visão Geral da Economia.md`

- **Resumo**: acrescentado parágrafo que apresenta as três camadas que faltavam — cadeia
  produtiva, instituições de crédito/contrato/tributo e economia criminal — com wikilinks
  para as notas novas.
- **Regra 6** reescrita: a escada de lucro deixou de ser "sete ou oito vezes / dezenas /
  infinito" solto e virou os **quatro degraus canônicos** (7–8× honesto, declarado como
  teto do mundo; >10× ilegal; dezenas de vezes fraude; sem capital no assalto), com a
  observação de que a pressão é aritmética e não moral (cap. 243).
- **Regras 13 a 17 acrescentadas**: origem física de todo produto; a regra da região de
  refino (cap. 469); tributação por portão e não por renda; contrato que só vale selado por
  Gu; garantia define o instrumento de crédito.
- **"O que todo personagem sabe"**: acrescentado o custo de vida do rank 3, a existência
  da renda de patrimônio, os pedágios de entrada e o Gu de contrato.
- **"Como as peças se encaixam"**: ordem de leitura da pasta refeita de 7 para 11 itens,
  posicionando as notas novas.

### `02 - Pedras Primordiais.md`

- **Corrigido**: "Entrada numa cidade grande | 1 a 10 pedras por pessoa" → a escada real
  documentada, **1 / 10 / 100 / 200 / 600** por pessoa conforme o anel (caps. 259–261,
  293, 1973).
- **Callout "fonte única de preços" reescrito**: a nota agora se declara guardiã das
  **âncoras** e delega o catálogo completo a `13`, com regra explícita de precedência.
- **Callout novo sobre spread de compra e venda**: 250 (a loja compra) contra 500 (o
  mercado vende), com a regra prática de usar metade quando o personagem vende
  (caps. 262, 278).
- **Regras e limites**: acrescentado o item sobre **volume físico do dinheiro** e a
  capacidade dos Gu de armazenamento (30.000 / 1.000.000, este custando 6.600) — incluindo
  o detalhe do velho de nuvens cuja expressão muda com o saldo (caps. 161, 268, 422).
- Relações atualizadas.

### `03 - Como um Mestre Gu Ganha a Vida.md`

- **Seção 4 (comércio)**: substituída a frase solta sobre lucro pela **tabela dos quatro
  degraus**, mais a doutrina canônica de que "um mercador de verdade ganha ao longo do
  caminho, não no destino" (cap. 243).
- **Seção 5 (profissões vizinhas)**: corretor de informação agora traz a faixa de preços
  (10 / 2.000 / 3.000.000); agiota virou "agiota e casa de penhores" com o penhor de Gu;
  acrescentadas três profissões novas — **fornecedor de contratos**, **extrator e coletor**
  (com a informação de que é um departamento formal de clã, cap. 1072) e **lojista e
  locador**.
- **Seção 11 nova — "Viver de patrimônio"**: as quatro portas de renda passiva
  (negócio com retorno em 2–3 anos, planta produtiva a ~400/dia, nascente espiritual com
  ≥100 milhões em 50–60 anos, nascente portátil a 50/dia), com callout de design sobre a
  virada de gênero da campanha.
- **Fechamento da tabela de renda**: acrescentado o custo de vida do rank 3 e trocada a
  regra de precedência de `02` para `13`.
- Relações atualizadas.

### `04 - Vida Cotidiana.md`

- **"Trabalho, dinheiro e administração"**: o item sobre salários mortais foi ampliado com
  a periodicidade (mensal), o reajuste em porcentagem (20% garçom / 40% gerente) e a fala
  dos empregados sobre não conseguirem sustentar a família (caps. 103, 117).
- Acrescentados dois itens: **servos-lavradores** como estatuto das aldeias em volta de um
  clã (cap. 67) e a existência de **crédito na base da pirâmide** (fiado, agiota, penhor,
  servidão de vinte anos), com wikilink para `16`.
- Relações atualizadas.

### `05 - Mercados e Leilões.md`

- **Fichas de autoridade**: acrescentado que a ficha **desconta o preço**, com o número —
  um terço a menos num item de 4.500 (cap. 272). A pasta tratava a ficha só como acesso.
- **Leilões**: acrescentado o comentário canônico "o verdadeiro vencedor é a casa de
  leilões" (cap. 308) e a regra de que a taxa do mercado imortal escala com o valor do
  lote, gerando fuga para praças sem taxa (caps. 1885, 1884).
- **Seção nova "Quando o comprador é que tem monopólio"**: o caso do clã que controla todas
  as lojas da cidade e recusa comprar de forma coordenada (caps. 262–264) — monopsônio,
  assunto que a pasta não tocava.
- Relações atualizadas.

### `06 - Ritmo de Cultivo e Reclusão.md`

- **"Quanto custa deixar o relógio andando"**: acrescentada a âncora do rank 3
  (>400.000/ano, cap. 278), fechando a escala que a nota tratava como aberta em uma ponta
  só.
- Os dois callouts de lacuna foram corrigidos: a obra dá **duas** âncoras (ranks 1 e 3) e
  silencia sobre os ranks 4 e 5 — antes o texto sugeria que só havia a do rank 1.

### `08 - Eventos e Instituições Jogáveis.md`

- Callout de calibragem de prêmios repontado para `13` (que agora reúne preço e renda no
  mesmo lugar).
- **Pedágios rituais** ampliado com o mecanismo completo da rota de montanha: postos de
  cobrança sucessivos, disputa ritual, entrega de parte da carga na derrota e a origem
  histórica da rota (caps. 240–241).

### `11 - Economia Imortal.md`

- Acrescentado o dado que faltava e que reorienta a nota inteira: **nove em cada dez
  transações do mercado imortal são escambo puro**, e a décima é super força comprando
  pedras a preço alto (caps. 469, 2245). Com callout de design sobre o que isso muda numa
  campanha de alto nível.
- Relações atualizadas.

## Notas novas criadas

Quatro. O prefixo numérico segue a numeração de disco atual (a pasta tinha 12 notas); a
**posição de leitura correta** é outra e está indicada abaixo, para o passe de renumeração
com `_pipeline/numerar-notas.py`.

| Arquivo criado | Posição de leitura sugerida | O que cobre |
|---|---|---|
| `13 - Preços, Renda e Custo de Vida.md` | **3ª** — logo depois de `Pedras Primordiais` e antes de `Como um Mestre Gu Ganha a Vida` | catálogo completo de preços por categoria; o que existe abaixo da pedra primordial; escada de pedágio por anel; série de preço dentro de uma linha de produto; renda de trabalho e de patrimônio; curva de inflação; custo de vida por patamar |
| `14 - Materiais e Cadeia Produtiva.md` | **5ª** — depois de `Como um Mestre Gu Ganha a Vida` | o que conta como material; as seis fontes (caça, lavoura, mineração, território, espólio, compra); quem faz o trabalho; quem compra; nove regras de mundo; preços de lote |
| `15 - Crime, Mercado Negro e Recompensas.md` | **8ª** — depois de `Mercados e Leilões` | escada de lucro por grau de honestidade; mandados de captura; os dois mercados negros; contrabando e falsificação; extorsão e sequestro; roubo de Gu; quem protege as estradas; comércio de gente; por que a sociedade não desmorona |
| `16 - Crédito, Contratos e Tributos.md` | **7ª** — depois de `Mercados e Leilões` e antes de `Crime` | seis formas de crédito mortal; servidão por dívida; crédito imortal resumido; o Gu de voto venenoso e a corrida armamentista contratual; corretagem e intermediários; tabela de tributos, taxas e pedágios |

Ordem de leitura completa proposta para a pasta, já com as novas:

1. Visão Geral da Economia · 2. Pedras Primordiais · 3. **Preços, Renda e Custo de Vida** ·
4. Como um Mestre Gu Ganha a Vida · 5. **Materiais e Cadeia Produtiva** ·
6. Mercados e Leilões · 7. **Crédito, Contratos e Tributos** ·
8. **Crime, Mercado Negro e Recompensas** · 9. Aposta de Rochas · 10. Vida Cotidiana ·
11. Ritmo de Cultivo e Reclusão · 12. Heranças e Provações ·
13. Eventos e Instituições Jogáveis · 14. Convenção do Caminho de Refino ·
15. Economia Imortal · 16. Produzir Gu Dentro da Abertura

### Candidata a apêndice

`13 - Preços, Renda e Custo de Vida.md` é a candidata forte. Ela é longa, é quase toda
tabela, e é a nota que a designer vai abrir no meio de uma sessão em vez de ler de ponta a
ponta — exatamente o perfil de `10 - Apêndices`. **Sugestão**: mover o corpo de tabelas
para um apêndice `Tabela de Preços e Renda`, deixando na pasta `06` uma nota curta de
leitura corrida que explique as duas economias, o spread compra/venda, a curva de inflação
e o custo de vida por patamar, e aponte para o apêndice. Não fiz a mudança porque
`10 - Apêndices` não é meu arquivo; deixo a decisão e o material prontos para quem cuidar
dos apêndices.

## Decisões tomadas

1. **A nota `02` deixou de ser "fonte única de preços"; passou a ser fonte das âncoras, e
   `13` virou o catálogo.** *Alternativa descartada:* engordar a `02` com as cem linhas
   novas. Descartada porque a `02` é uma nota de **conceito** — ela existe para explicar
   por que a moeda também é combustível mágico — e enterrar essa ideia sob dez tabelas
   destruiria a nota mais didática da pasta. A precedência entre as duas ficou escrita nas
   duas.

2. **Criar quatro notas em vez das três sugeridas.** O quarto assunto (crédito, contratos e
   tributos) está explicitamente na lista de partida da tarefa em três itens separados e
   tem material canônico farto — em particular o Gu de voto venenoso, que é uma das melhores
   invenções mecânicas da obra e não aparecia em nenhuma nota do vault. *Alternativa
   descartada:* espalhar crédito na `03`, contratos na `05` e tributos na `04`. Descartada
   porque as três coisas se explicam juntas — todas respondem "como se faz um negócio valer
   quando não há Estado" — e separá-las devolveria a lacuna sob outra forma.

3. **O spread compra/venda foi generalizado como regra de mesa, marcado `(ded.)`.** A obra
   dá o par 250/500 numa categoria; usar "metade quando vender" para todas as categorias é
   dedução nossa e está marcada como tal nas duas notas onde aparece.

4. **A escala de custo de vida dos ranks 4 e 5 foi deixada em branco, com uma sugestão
   marcada `*` e isolada num callout.** *Alternativa descartada:* interpolar e publicar uma
   tabela de cinco linhas. Descartada pela mesma razão registrada na nota `09` quando a
   tabela de prêmios da aposta de rochas foi removida: números inventados no meio de uma
   tabela cujas pontas são canônicas acabam sendo lidos como cânone.

5. **A tributação de clã foi enunciada como "tributo em trabalho", marcado `(ded.)`.** A
   obra não mostra nenhuma taxa monetária periódica cobrada de membros de clã; mostra a
   obrigação de uma missão por mês e as contrapartidas. A leitura de que isso é
   funcionalmente um imposto é nossa, e está declarada como tal.

6. **Preços de patamar imortal ficaram em `11` e `14`, não em `13`.** A `13` é
   deliberadamente a planilha do **mundo mortal**, que é onde a campanha da designer vai
   acontecer. Misturar as duas unidades na mesma tabela é o erro que a própria nota `11`
   já alerta contra.

7. **Não toquei em `_pipeline/rascunho/economia-e-vida.md` nem em `10 - Apêndices/`**, por
   não serem meus arquivos. Os achados novos de texto-fonte estão registrados aqui com
   capítulo, prontos para o próximo passe de consolidação.

## Divergências com a tabela soberana

Uma real, uma aparente e uma observação.

1. **Divergência real — preço de entrada em cidade.**
   `10 - Apêndices/02 - Tabelas de Referência Rápida.md`, seção 13.8, registra
   *"Entrada em cidade-clã | **10 pedras por pessoa** | canônico"*. O número está certo mas
   é **um degrau de uma escada**, e usá-lo sozinho subestima o custo de acesso em até
   sessenta vezes. O texto documenta, no mesmo complexo urbano: **10** pedras para o anel
   externo (cap. 259), **100** para a primeira cidade interna, **200** para a segunda e
   **600** para a terceira sem ficha de autoridade (cap. 261) — e, em outra região, **1**
   pedra por pessoa numa cidade de deserto (cap. 1973).
   **Encaminhamento:** as notas `02` e `13` já registram a escada completa; recomendo que
   quem cuida dos apêndices atualize a linha 13.8. Registrei aqui em vez de editar a tabela
   soberana porque ela não é meu arquivo. Enquanto a linha não for atualizada, há uma
   divergência viva entre `06` e `10`, e a **minha leitura é que a escada vence**, porque
   os quatro valores estão no texto e o "10" é apenas o mais citado.

2. **Divergência aparente — nada a corrigir.** A tabela soberana diz que uma montaria comum
   custa "menos de 1 pedra primordial" e compara com "um Gu de rank 1: centenas de pedras".
   Isso é compatível com as faixas de `13` (rank 1 ≈ 500 no varejo, ≈ 250 na compra por
   loja) e não exige ajuste.

3. **Observação — a tabela soberana e a `13` não competem.** A soberana cobre os números do
   **sistema de cultivo** (aptidão, dao marks, tempo, distância, alcance) e alguns custos de
   transporte; a `13` cobre **preços e renda**. A única sobreposição é a seção 13.8, tratada
   no item 1. As notas novas apontam para a soberana como fonte dos números de sistema.

## O que a obra realmente não diz

Verificado por `grep -i` no texto-fonte, não por ausência em fonte secundária.

- **Não existe moeda menor que a pedra primordial.** A obra afirma duas vezes, com todas as
  letras, que a pedra primordial é *a* moeda do mundo, usada para medir o valor de todas as
  mercadorias (caps. 8 e 11). Uma varredura por `copper coin`, `gold coin`, `taels of
  silver`, `coinage`, `penny` e `smallest denomination` não devolve **nenhuma** ocorrência
  de moeda mortal alternativa. O troco é feito em **frações da própria pedra**, que é
  fisicamente divisível, e o resto é escambo e favor. Esta negativa está verificada e pode
  ser afirmada com segurança.
- **Não existe imposto sobre renda ou patrimônio.** Toda cobrança documentada é de
  passagem, acesso, participação ou transação. A varredura por `tax`, `taxation`,
  `tribute`, `levy` e `toll` devolve pedágio de cidade, pedágio de estrada, taxa de
  transação de mercado, taxa de inscrição, taxa de ilha conquistada, mensalidade de aliança
  e tributo cerimonial — nunca uma alíquota sobre o que alguém ganha ou possui.
- **Não existe taxa periódica cobrada pelo clã dos próprios membros.** O que existe é a
  obrigação de uma missão por mês. Ver decisão 5.
- **Custo de vida dos ranks 4 e 5**: silêncio total. A obra afirma que cresce e dá âncoras
  nos ranks 1 e 3.
- **Preço de passagem de caravana**: nunca precificado — e o silêncio não é lacuna, é
  modelo: entra-se numa caravana como pessoal contratado ou como mercador com carga
  própria, nunca como passageiro pagante. Já registrado na tabela soberana.
- **Percentual da comissão de uma casa de leilões mortal**: a obra afirma que a casa lucra
  com qualquer resultado, mas nunca dá a alíquota. No mercado imortal diz apenas que a taxa
  escala com o valor do lote.
- **Preço de contrato de escolta ou de mercenário por tempo**: não existe. O que existe são
  recompensas **por feito** (afugentar uma ameaça, servir de isca, executar um mandado).
- **Salário mortal em números absolutos**: só variações (+meia pedra por mês numa promoção;
  +20% e +40% num reajuste de taverna) e a afirmação de que é "muito pouco por mês". O
  valor de base nunca aparece.
- **Valor da mensalidade de aliança e da taxa da ilha conquistada**: confirmados como
  existentes, quantias nunca reveladas.
- **Tabela de prêmios da aposta de rochas**: continua não existindo, como a nota `09` já
  registra.
- **Preço de um Gu Imortal em moeda**: não existe por regra, não por omissão — artefatos
  imortais não se vendem por dinheiro, só se trocam ou se emprestam.
