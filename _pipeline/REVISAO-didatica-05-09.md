---
tags:
  - pipeline
  - revisao
status: em-andamento
escopo: "pastas 05 a 09"
revisor: "designer externa de TTRPG, leiga na obra"
---

# Revisão didática — pastas 05 a 09

**Quem escreve:** uma designer profissional de RPG de mesa que nunca leu *Reverend
Insanity*, contratada para projetar o jogo, tendo este vault como fonte única.

**O que este documento é:** uma leitura crítica de 24 notas (pastas 05–09), procurando
o que me impediria ou atrasaria o trabalho de design. Organizado por severidade.
Não editei nenhuma nota.

**Como ler as entradas:** cada problema traz `[arquivo]`, o trecho ou a localização, o
tipo do problema e uma sugestão concreta.

> Documento gravado incrementalmente. Seções são acrescentadas conforme a leitura avança.

---

## Índice

- [Bloqueadores](#bloqueadores)
- [Sérios](#sérios)
- [Menores](#menores)
- [O que está bom e não precisa mexer](#o-que-está-bom-e-não-precisa-mexer)
- [Veredito](#veredito)

---

*(seções preenchidas ao final da leitura de todas as pastas; anotações brutas por pasta
abaixo)*

---

# Anotações brutas por pasta

## 05 - Sociedade — lido

### Impressão geral

A melhor pasta que li até agora em termos de utilidade de design. Cinco das seis notas
abrem com "Em uma frase", têm resumo, e terminam com "Relações". Os blocos
`> [!note] Para o design` são reais — dizem o que fazer com a informação, não só que ela
é interessante. `Visão Geral da Sociedade` faz o serviço que uma porta de entrada deve
fazer: define "Mestre Gu", "mortal" e "rank" **antes** de usá-los.

### Problemas

**05-A — Três nomes para a mesma instituição, sem aviso** · `Tribunal Celestial e Grandes Forças.md`
Tipo: jargão/inconsistência de nomenclatura.
O título da nota diz "Tribunal Celestial". O corpo escreve sempre "Heavenly Court",
"Corte Celestial" ou "a Corte". O `aliases` traz "Heavenly Court" e "Corte Celestial".
E há um wikilink para uma nota **diferente** chamada `[[Tribunal Celestial]]`.
Como leiga, passei um bom tempo tentando decidir se "Tribunal Celestial" e "Corte
Celestial" são duas instituições (um judiciário e um governo?) ou uma só.
`Visão Geral da Sociedade` piora: usa exclusivamente "Heavenly Court (Corte Celestial)"
e nunca escreve "Tribunal".
Sugestão: escolher **um** nome em português e usá-lo em todo o corpo, com o inglês entre
parênteses só na primeira ocorrência de cada nota. Se "Tribunal" foi a escolha do
glossário, renomear as ocorrências de "Corte" no corpo — ou renomear a nota.

**05-B — Tabela da hierarquia de seitas mistura dois eixos na mesma coluna** · `Seitas e Academias.md`
Tipo: tabela sem chave de leitura.
A tabela "Hierarquia de discipulado" tem a coluna "Como se sobe", mas as quatro
primeiras linhas respondem *com que frequência há exame* e as três últimas respondem
*a que rank de cultivo corresponde*. São perguntas diferentes. Um discípulo de legado é
de que rank? Um rank 4 é automaticamente ancião de seita, ou precisa ter passado pelos
degraus? Não dá para saber, e isso é exatamente o tipo de coisa que vira regra de ficha.
Sugestão: três colunas — `Degrau | Rank típico | Como se sobe` — e uma frase dizendo se
os dois eixos são independentes (dá para ser rank 4 e ainda discípulo externo?).

**05-C — "Abertura" e "essência" usados sem definição nem link** · `Clãs.md`
Tipo: jargão não explicado.
- "dopar herdeiros com **transfusões de essência** antes de testes públicos"
- "O patrimônio de um morto é verificado inspecionando sua **abertura interna**"
Nenhum dos dois termos é definido nesta nota nem linkado. Eu não sei o que é uma
abertura (um órgão? um espaço mágico? uma mochila?) nem o que é essência. E os dois são
centrais — "inspecionar a abertura de um morto" é uma cena de jogo que eu escreveria
errado.
Sugestão: `[[Abertura|abertura interna]]` e `[[Essência Primeva|essência]]` na primeira
ocorrência, mais uma aposição de meia linha ("a cavidade interna onde os Gu são
guardados").

**05-D — O mesmo subsídio aparece com dois valores de precisão** · `Clãs.md` × `Seitas e Academias.md`
Tipo: número que não bate entre notas.
`Clãs`: "subsídio semanal de **três pedras**". `Seitas e Academias`, descrevendo a mesma
academia de clã: "subsídio semanal de **algumas pedras primevas**".
Não é contradição, é perda de informação numa nota que se apresenta como a detalhada
sobre academias. Quem lê só `Seitas` não fica com número nenhum.
Sugestão: repetir "três pedras primevas por semana" em `Seitas`, ou remeter à tabela do
apêndice.

**05-E — Notas marcadas `conhecimento: comum` contêm seção "O que só o mestre sabe"** · `Visão Geral da Sociedade.md`
Tipo: confusão estrutural / contrato de metadados.
O LEIA-ME diz que `conhecimento` classifica a nota inteira e que material `comum` é
"material de manual do jogador". Mas esta nota, marcada `comum`, tem uma seção inteira de
segredos pesados (a instituição construída para ser colhida, os espiões de mil anos).
Se eu imprimir as notas `comum` como base do livro do jogador, vazo o cenário inteiro.
Sugestão: ou o campo passa a significar "nível da *maior parte* da nota, ver seções", e
isso fica dito no LEIA-ME, ou as seções "O que só o mestre sabe" saem para notas próprias.
Como leiga vinda de fora, eu esperava poder confiar no campo do frontmatter para
recortar o material.

**05-F — Benchmark de poder ausente onde a nota depende dele** · `Tribunal Celestial e Grandes Forças.md`
Tipo: falta de utilidade para design.
"uma força-tarefa oficial com três cultivadores de **rank 8** e três fortalezas móveis já
é suficiente para liquidar uma super força inteira". Eu não tenho nenhuma noção do que um
rank 8 faz. Quantos rank 6 ele vale? Uma super força tem quantos imortais? A frase é
retórica para mim, quando deveria ser calibração.
Sugestão: uma linha de referência ("um rank 8 supera N rank 7 simultâneos; uma super
força típica tem X imortais, majoritariamente rank 6") ou um link explícito para a tabela
de escala do apêndice.

**05-G — "anciãos" e "anciães" alternam** · `Clãs.md` × `Seitas e Academias.md` × `Cultura das Cinco Regiões.md`
Tipo: menor, consistência de termo.
`Clãs` usa "anciãos". `Seitas` e `Cultura` usam "anciães supremos". São o mesmo cargo?
"Ancião supremo" parece ser um cargo distinto (ranks 6+), mas a variação ortográfica do
plural faz parecer distinção onde talvez não haja.
Sugestão: padronizar o plural e reservar "supremo" como o qualificador que marca a
diferença de cargo.

**05-H — Densidade de instituições sem nome próprio** · `Cultura das Cinco Regiões.md`
Tipo: densidade / abstração excessiva.
Curiosamente o problema aqui é o **inverso** do esperado: quase nada tem nome. "um clã
número um absoluto", "outro se apresenta como a nêmesis do caminho demoníaco", "uma
cidade governada por uma raça alada", "uma família descendente de uma figura fundadora".
Entendo a decisão de evitar spoiler, mas para desenhar um cenário eu preciso de rótulos
para pendurar as coisas — mesmo que sejam rótulos meus. Doze entidades sem nome em uma
nota viram uma névoa.
Sugestão: um apêndice "quem é quem, com nomes" (mesmo que marcado `segredo`), ou nomes
de trabalho entre colchetes para eu poder referenciar. Ver também 07 e 09, onde o mesmo
padrão aparece.

**05-I — "Aptidão de A a D" aparece sem escala** · `Clãs.md`, `Seitas e Academias.md`
Tipo: jargão parcialmente explicado / pendência de cross-check.
"grau de aptidão (de A a D, ou nenhuma)" e "o comum é o grau B, e há muitos de grau A".
Nenhuma das duas notas diz o que a aptidão *faz* mecanicamente nem linka para onde isso
está. A distribuição populacional (quantos % são A?) é decisiva para eu calibrar criação
de personagem.
Sugestão: link para `[[Aptidão]]` na primeira ocorrência em cada nota. (Verificado
contra o apêndice mais adiante nesta revisão.)

### O que está bom nesta pasta

- `Visão Geral da Sociedade` define Mestre Gu / mortal / rank antes de usá-los. É o
  modelo que as outras visões gerais deveriam seguir.
- As "Regras do mundo" numeradas são diretamente conversíveis em regras de mesa. A #12
  ("força individual supera número") sozinha define o tipo de jogo que isto é.
- A matriz talento × virtude em `Caminho Correto e Caminho Demoníaco` é um artefato de
  design pronto: dois eixos, quatro quadrantes, duas leituras opostas. Eu usaria isso na
  ficha.
- O "acordo de não-intervenção com preço tabelado" (`Tribunal Celestial e Grandes
  Forças`) resolve o problema clássico de "por que os NPCs poderosos não resolvem tudo"
  de forma diegética. Melhor solução que a maioria dos cenários publicados.
- Os pontos de contribuição de seita são uma economia de facção pronta, com preços e
  com o detalhe do **aluguel por prazo**, que é ouro em mesa.
- A tabela comparativa das cinco regiões é autoexplicativa e caberia num encarte.
