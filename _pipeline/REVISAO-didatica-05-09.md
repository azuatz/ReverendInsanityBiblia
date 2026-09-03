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
E há um wikilink para uma nota **diferente** chamada `[[19 - Tribunal Celestial|Tribunal Celestial]]`.
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
Sugestão: `[[02 - Abertura|abertura interna]]` e `[[Essência Primeva|essência]]` na primeira
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
Sugestão: link para `[[03 - Aptidão|Aptidão]]` na primeira ocorrência em cada nota. (Verificado
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

---

## 06 - Economia e Vida — lido

### Impressão geral

Conceitualmente a pasta mais forte do vault: "moeda = combustível de progressão" é uma
ideia de design de primeira linha e as notas sabem disso. Mas é também onde estão os
piores problemas numéricos que encontrei. Há **duas tabelas de preços que se contradizem
com a própria escala de subsistência**, e a tabela de câmbio imortal está enunciada de
forma invertida. Como economia é literalmente a primeira coisa que eu preciso fechar num
sistema de RPG, isso vira bloqueador.

### Problemas

**06-A — A proporção das essências imortais está enunciada ao contrário da própria tabela** · `Economia Imortal.md`
Tipo: **furo lógico / número que não bate — bloqueador.**
A tabela diz, na coluna "Custo em pedras de essência imortal": uva verde (rank 6) = 1;
tâmara vermelha (rank 7) = 100; lichia branca (rank 8) = 10.000.
A frase imediatamente abaixo diz: "Ou seja: **uva verde : tâmara vermelha : lichia branca
= 10.000 : 100 : 1**."
Isso não é um "ou seja". É a razão **invertida**. Pela tabela, a proporção é 1 : 100 :
10.000. Pela frase, é 10.000 : 100 : 1.
As duas leituras podem até estar ambas corretas na obra, se uma medir *custo por conta* e
a outra *contas obtidas por pedra* — mas a nota nunca diz isso, e liga as duas com "ou
seja", como se fossem a mesma afirmação. Eu não consigo escrever uma regra de conversão
de moeda a partir daqui.
Piora: `Visão Geral da Economia` repete só a versão em prosa — "dez mil para cem para um,
entre os ranks 6, 7 e 8" — sem a tabela. Quem ler só aquela nota conclui que a essência
de rank 6 vale dez mil vezes a de rank 8, o que é o oposto do que a nota quer dizer.
Sugestão: renomear as colunas para deixar explícita a direção ("Pedras de essência
imortal necessárias para 1 conta" vs. "Contas obtidas por 1 pedra") e trocar o "ou seja"
por "visto do outro lado". Um exemplo numerado resolveria de vez: *"1 pedra de essência
imortal rende 10.000 contas de uva verde, ou 100 de tâmara vermelha, ou 1 de lichia
branca."*

**06-B — O preço dos escravos quebra a economia inteira** · `Pedras Primevas.md`, `Vida Cotidiana.md`
Tipo: **furo lógico / ordem de grandeza — bloqueador.**
- "Cinco homens mortais escravizados custam cerca de **meia pedra primeva**."
- "Um javali de caça | **meia pedra**."
- "Cinco meses de vida de uma família mortal de três pessoas | 5 pedras."
Combinando: um escravo custa 0,1 pedra; e 1 pedra sustenta uma pessoa por cerca de cinco
meses. Ou seja, **um escravo custa menos que duas semanas da própria comida dele**, e
cinco escravos valem um javali.
Mas as mesmas notas dizem que o tráfico de escravos é "o negócio mais próspero da região",
que ele opera "em escala industrial", "aos milhões", e que há uma precificação
sofisticada por controlabilidade em que raças variantes custam *mais*. Um comércio de
bilhões de unidades a 0,1 pedra cada movimentaria menos que um único Gu de rank 3.
Ou o preço está errado (falta um fator de 100 ou 1.000), ou ele se refere a algum lote
degradado específico, ou "meia pedra" era o preço numa cena excepcional.
Isso me trava: eu não consigo precificar mão de obra, resgates, indenizações nem o valor
de um NPC capturado.
Sugestão: marcar o número como caso isolado ("num leilão de saldo, cinco cativos foram
arrematados por meia pedra") e dar uma faixa típica separada; ou corrigir a ordem de
grandeza. E cruzar com a multa por matar servos (ver 06-C).

**06-C — A tabela de preços e a escala de subsistência vivem em universos diferentes** · `Pedras Primevas.md`
Tipo: **furo lógico / tabela sem chave de leitura — bloqueador.**
Da mesma nota, na mesma página:
- 1 pedra ≈ 1 mês de vida de uma família mortal de três pessoas.
- "**Chá comum | 5 pedras**" → uma xícara de chá comum custa cinco meses de subsistência
  de uma família.
- "Ingresso de arena, como espectador | 20" → vinte meses de subsistência para assistir a
  uma luta.
- "Entrada numa cidade grande | 1 a 10 pedras por pessoa" → nenhum mortal jamais entra
  numa cidade.
- "Aluguel de um imóvel modesto | 8 a 25 pedras por mês" → o aluguel "modesto" custa de 8
  a 25 vezes o sustento integral de uma família.
Suspeito que a explicação seja "todos esses preços são da economia de Mestre Gu, e o
mortal simplesmente não participa dela". Se for isso, é uma decisão de cenário
interessantíssima — e a nota precisa **dizer**, porque ela apresenta as duas escalas
misturadas na mesma tabela sem nenhuma marcação.
Sugestão: acrescentar uma coluna "público" (mortal / Mestre Gu) às duas tabelas de
preços, e um parágrafo dizendo explicitamente que o mortal comum vive fora da economia
monetária — se for esse o caso. Do jeito atual, a tabela mais importante do vault para
mim é inutilizável sem adivinhação.

**06-D — "Cada rank multiplica o preço por dez" é contradito pela tabela logo acima** · `Pedras Primevas.md`
Tipo: número que não bate.
A tabela de preço de Gu: rank 1 = ~500; rank 2 = 500 a 1.000; rank 3 = 1.000 a 10.000;
rank 4 = 10.000 a 100.000; rank 5 = 100.000 a 1.000.000.
A observação nº 1 abaixo dela: "**Cada rank multiplica o preço por dez.** É uma escala
logarítmica limpa e fácil de usar em mesa."
Do rank 1 para o 2 o multiplicador é 1 a 2, não 10. Do 2 para o 3 é 1 a 10. Só a partir
do rank 3 a regra vale. Como designer, eu adotaria a regra ×10 e depois descobriria que
minha tabela não bate com a do apêndice nos dois primeiros ranks — exatamente onde os
personagens começam.
Sugestão: ou ajustar a tabela (rank 1 ≈ 50–100), ou reescrever a observação: "a partir do
rank 3, cada rank multiplica por dez; os ranks 1 e 2 são comprimidos porque o piso do
mercado é o custo de captura, não o de refino".

**06-E — Os números da guerra de preços são maiores que a economia que os contém** · `Economia Imortal.md`
Tipo: **furo lógico / ordem de grandeza — sério.**
Na mesma nota:
- "Riqueza típica por rank": rank 8 = "dezenas de milhares; veteranos, centenas de
  milhares"; **"Uma super força inteira | Da ordem de 1.000.000 em caixa"**.
- Estudo da guerra de preços: "**lucro líquido de doze milhões** de pedras de essência
  imortal, com as dívidas quitadas e **dez milhões livres**".
Um único comerciante sai de uma única operação comercial com **dez vezes o caixa de uma
super força inteira**. Ou a tabela de riqueza está subdimensionada, ou o lucro está
superdimensionado, ou faltam anos e contexto na operação. E a própria nota chama a
manobra de "regra, não exceção", o que significa que ela seria replicável — o que
destruiria a escala econômica declarada duas seções acima.
Sugestão: uma frase de calibração ("este foi o maior lucro comercial individual
registrado na obra; opere sua mesa uma ou duas ordens de grandeza abaixo"), ou revisar um
dos dois números. Sem isso eu não sei se um milhão é muito ou pouco.

**06-F — "Unidades de renda mensal" é uma unidade que não existe** · `Economia Imortal.md`, `Como um Mestre Gu Ganha a Vida.md`
Tipo: jargão/unidade não definida + número que não bate.
- "Um monopólio documentado passou de **48 para 92 e depois para cerca de 300 unidades de
  renda mensal**." Unidades de quê? Pedras de essência imortal? Contas? Nunca é dito.
- "Um portfólio maduro rende **mais de mil unidades da moeda imortal por mês**."
E a tabela de riqueza típica diz que um rank 6 tem "algumas centenas" de pedras de
essência imortal **no total**. Se ele ganha mais de mil por mês, sua renda mensal é
várias vezes seu patrimônio típico. Não fecha.
Sugestão: nomear a unidade em todas as ocorrências ("pedras de essência imortal por mês")
e dizer de que rank é o portfólio em questão; ou separar "renda de um imortal-empresário
excepcional" de "renda típica de rank 6".

**06-G — A aposta de pedra é vendida duas vezes como "minijogo pronto" e não tem tabela de prêmios** · `Mercados e Leilões.md`, `Como um Mestre Gu Ganha a Vida.md`
Tipo: falta de utilidade para design + número que não bate.
Duas notas trazem um bloco "Para o design" dizendo que a aposta de pedra é "um minijogo
pronto com todas as peças no lugar". Ela tem custo (cinco categorias de preço), tem
perícia, tem segunda perícia. **Não tem prêmio.** Em nenhum lugar se diz o que se ganha:
qual o rank típico do Gu encontrado, qual o valor esperado, se compensa.
E os números disponíveis sugerem que não compensa: uma pedra "média" custa ~1.000, o
especialista acerta 2 em 10 (5.000 por acerto), e um Gu de rank 1 vale ~500. O minijogo,
como está, é uma máquina de perder dinheiro.
Pior, há uma incoerência de probabilidade: "cerca de **nove em cada dez** pedras são
maciças" (logo, no máximo 10% contêm algo), mas "um especialista com séculos de prática
acerta algo em torno de **duas em dez**" — 20%, o dobro do teto. Faz sentido se o
especialista *escolhe* quais comprar, mas a nota apresenta as duas taxas lado a lado como
se fossem comparáveis.
Sugestão: (a) acrescentar uma tabela de resultado por categoria de pedra — "sucata: 1% de
Gu vivo de rank 1; super: 40% de Gu vivo de rank 3–4" ou o que a obra permitir, marcado
como reconstrução; (b) dizer explicitamente que a taxa do especialista é sobre pedras
*selecionadas*, não sobre a população.

**06-H — "Campo de cultivo" é o mesmo que "Path" e nada avisa** · `Economia Imortal.md`
Tipo: **jargão / colisão de sinônimos — sério.**
`Economia Imortal` usa "campo de cultivo" repetidamente: "Prosperidade de um **campo de
cultivo** é um ciclo auto-reforçado", "cada missão exige métodos de **campos de cultivo**
específicos", "veias de dao — canais que concentram a energia de um **campo específico**".
O vault tem uma pasta inteira chamada `03 - Paths` com uma nota por caminho de
especialização. Levei um tempo até concluir que "campo de cultivo" e "Path" são a mesma
coisa — e ainda não tenho certeza.
Se forem a mesma coisa, isto é grave: o conceito mais central do sistema aparece com um
nome alternativo, sem link, na nota que define a economia de alto nível.
Sugestão: usar o mesmo termo do resto do vault e linkar `[[01 - Visão Geral dos Paths|Visão Geral dos Paths]]` na
primeira ocorrência. Se forem coisas diferentes, dizer a diferença em uma frase.

**06-I — Jargão pesado não definido nem linkado** · `Economia Imortal.md`, `Como um Mestre Gu Ganha a Vida.md`, `Eventos e Instituições Jogáveis.md`
Tipo: jargão não explicado.
Lista do que usei sem entender:
- **"veias de dao"** (`Economia Imortal`) — "dao" nunca aparece definido nesta pasta. Há
  uma nota `[[16 - Dao Marks|Dao Marks]]` em `01 - Cultivo`, não linkada aqui.
- **"provações"** / **"calamidade"** (`Economia Imortal`, `Eventos e Instituições
  Jogáveis`) — usadas como se eu soubesse o que são. Existe `[[Tribulações e
  Calamidades]]`, nunca linkada.
- **"fazenda de provações"** (na seção "Relações" de `Economia Imortal`) — um termo que
  não aparece em lugar nenhum do corpo de nenhuma nota desta pasta. Fui procurar e não
  achei.
- **"gruta-céu"** (`Eventos e Instituições Jogáveis`) e **"Domínio recluso de céu e
  terra"** (`Economia Imortal`) — dois nomes, aparentemente para a mesma coisa, nenhum
  explicado, nenhum linkado a `[[13 - Blessed Lands e Grotto-Heavens|Blessed Lands e Grotto-Heavens]]`, que existe.
- **"abertura"** (`Eventos e Instituições Jogáveis`: "ele entra na **abertura** do
  candidato").
- **"fichas de autoridade"** (`Como um Mestre Gu Ganha a Vida`) — definidas em `Visão
  Geral da Economia`, não aqui.
- **"maré de feras"** vs. **"marés de bestas"** — duas grafias do mesmo evento, em notas
  diferentes, nenhuma definida onde aparece primeiro.
Sugestão: uma passada de linkagem na primeira ocorrência de cada termo em cada nota. É
barato e resolve metade das minhas queixas do vault inteiro.

**06-J — A tabela de pontos de recurso não responde à própria pergunta** · `Economia Imortal.md`
Tipo: tabela sem chave de leitura.
| Porte | Produz |
| Minúsculo, pequeno, médio | Nível rank 1 a 5 |
| ... | ... |
| **Pináculo** | **Domínio recluso de céu e terra** |
Dois defeitos. Primeiro, a linha de cima junta **três** portes numa faixa só — não sei
diferenciar um "minúsculo" de um "médio", que é justamente a faixa em que uma campanha
mortal aconteceria. Segundo, a última linha não responde "produz o quê": ela dá o nome de
outra coisa, não um nível de produção, quebrando o contrato da coluna.
Sugestão: uma linha por porte, e converter a linha "Pináculo" em produção ("rank 9 /
não-precificável — ver [[13 - Blessed Lands e Grotto-Heavens|Blessed Lands e Grotto-Heavens]]").

**06-K — A tabela de renda não diz de que rank é quem ganha** · `Como um Mestre Gu Ganha a Vida.md`
Tipo: falta de utilidade para design.
A "Tabela de referência: ordens de grandeza de renda" é a tabela que eu mais quero usar —
é dela que sai a recompensa por sessão. Mas quase nenhuma linha diz **quem** ganha
aquilo. "Missão simples de coleta | 2 a 6" — de que rank? "Luta de arena de bom público |
milhares" — um rank 2 ganha isso? "Recompensa por afugentar um invasor de rank alto |
500" — quem afugentou, e como sobreviveu?
Sem a coluna de rank eu não consigo montar uma curva de recompensa, que é a primeira
planilha que qualquer designer abre.
Sugestão: acrescentar uma coluna "rank típico do executante" e outra "tempo gasto". Com
essas duas colunas essa tabela sozinha valeria metade do trabalho de balanceamento.

**06-L — Duas multas incompatíveis para crimes contra mortais** · `Pedras Primevas.md` × `Clãs.md` / `Vida Cotidiana.md`
Tipo: número que não bate.
"Multa por **ferir** um cidadão comum | cerca de 49 pedras" (`Pedras Primevas`) contra
"**Matar vários** servos mortais custa uma multa de algumas dezenas de pedras" (`Clãs`,
`Vida Cotidiana`).
Ferir um custa o mesmo que matar vários. Deve haver uma distinção jurídica entre "cidadão
comum" e "servo" que explica isso, mas nenhuma nota a enuncia.
Sugestão: uma linha nomeando as categorias legais de mortal (cidadão livre / servo /
escravo) com o valor de cada uma. Isso é diretamente uma tabela de consequências para a
mesa, e hoje está implícita.

**06-M — Faixas de preço de consumível divergem entre a nota e o resumo** · `Pedras Primevas.md` × `Como um Mestre Gu Ganha a Vida.md`
Tipo: menor, número que não bate.
"Folha medicinal cultivada (unidade) | **55** a 80" contra "Venda de consumível cultivado
(por unidade) | **50** a 80". Diferença pequena, mas é sintoma: as duas tabelas foram
mantidas à mão em vez de uma referenciar a outra.
Sugestão: eleger `Pedras Primevas` (ou o apêndice) como fonte única de preços e fazer as
outras notas remeterem a ela em vez de repetir.

**06-N — A escada de fichas coloridas tem nove degraus e só dois nomes** · `Mercados e Leilões.md`
Tipo: densidade invertida / falta de utilidade.
"uma escada de **fichas coloridas** — nove cores, do preto ao roxo-espinho". As sete do
meio nunca aparecem. E "a ficha de topo equivale a cerca de **metade da autoridade de um
ancião de clã**" usa "autoridade" como se fosse uma grandeza medida, mas ela não é
quantificada em lugar nenhum do vault.
A mecânica de "moeda dupla" que a própria nota (com razão) elogia depende exatamente
dessa escada, e ela não está aqui.
Sugestão: listar as nove cores com o que cada uma destrava, mesmo que parcialmente
reconstruído e marcado como tal. Um sistema de acesso de nove níveis é bom demais para
ficar em duas cores.

**06-O — `Eventos e Instituições Jogáveis` entrega, mas o "prêmio" quase sempre falta** · `Eventos e Instituições Jogáveis.md`
Tipo: falta de utilidade parcial.
A nota abre prometendo, num callout: "Cada evento abaixo vem com o que uma mesa precisa:
**quem participa, qual é a regra, qual é o prêmio, e o que dá errado**."
Ela cumpre para "regra" quase sempre, e para "prêmio" quase nunca. Contando: dos ~25
eventos listados, **cerca de seis** trazem prêmio quantificado (arena, trono decenal,
convenção de refino, subjugação de matilhas, torneio entre organizações, provas de
sucessão). Os demais dizem "prêmios crescentes", "benefícios territoriais", "vantagens
concretas", "recursos escalonando em valor". Nas caçadas, nos reinos de sonho, nas provas
de herança institucionalizadas e nas feiras, não há um único número.
Sugestão: ou cumprir a promessa do callout com uma coluna de prêmio para cada evento, ou
suavizar o callout. Como está, ele me faz confiar em algo que a nota não entrega, e eu só
descubro no meio do planejamento de sessão. (Fora isso a nota é excelente — ver a seção
"o que está bom".)

**06-P — Repetição em bloco entre três notas** · `Como um Mestre Gu Ganha a Vida.md`, `Mercados e Leilões.md`, `Economia Imortal.md`
Tipo: densidade / manutenção.
A aposta de pedra aparece quase integralmente em duas notas; as caravanas em três; os
pontos de contribuição em quatro (contando `Seitas e Academias`); "renda não é reserva" e
o parágrafo do "rio" aparecem literalmente idênticos em duas.
Para leitura isolada isso é uma virtude. Para mim, que li tudo de enfiada, é onde os
números começam a divergir (ver 06-M) — porque a mesma informação é mantida em quatro
lugares.
Sugestão: eleger uma nota dona de cada assunto e deixar nas outras um resumo de duas
linhas mais o link. Reduz a superfície de erro.

### O que está bom nesta pasta

- **"Moeda é combustível de progressão"** é a melhor ideia de design do vault inteiro, e
  as notas a defendem bem, com a consequência certa tirada em cada lugar ("gasto para
  viver ou gasto para subir?"). Eu construiria o sistema em volta disso.
- **"O gargalo é artefato, não capital"** resolve o problema da loja de itens de forma
  elegante e diegética. Dinheiro compra insumo, treino e comida; artefato só vem de
  aventura. É uma regra que eu escreveria literalmente com essas palavras.
- **A escala de câmbio que empobrece quem sobe de rank** é uma invenção rara e ótima
  (apesar do problema de enunciado em 06-A). Impede que a riqueza de um patamar
  trivialize o seguinte sem inflação artificial.
- **A tabela de crédito imortal por perfil de credor** (seis empréstimos, seis termos
  diferentes, todos políticos) é um artefato de mesa pronto. Eu usaria como tabela de
  rolagem.
- **`Eventos e Instituições Jogáveis`** entrega de verdade, apesar da queixa 06-O: o
  ciclo decenal do trono é uma campanha inteira em uma página, o obelisco de mérito é um
  quadro de missões completo com desbloqueios comprados e saldo negativo, e o
  **"calendário de campanha pronto"** no fim é a tabela mais imediatamente utilizável do
  vault. É a nota que eu levaria impressa para a primeira reunião.
- **`Vida Cotidiana`** faz algo que quase nenhum cenário faz: dá o chão. "O horror aqui é
  administrativo" é uma nota de direção de tom que vale por três páginas de descrição, e
  a tabela "Marcos de uma vida" é diretamente um gerador de personagem.
- **A cerimônia de despertar aos quinze** como ponto de partida de campanha, incluindo a
  possibilidade de um jogador **não passar**, é o melhor gancho de sessão zero do vault.
- **O lance cego por escrito** e o **álibi do fóssil** são dois minijogos sociais de custo
  zero em regras.

---

## 08 - Estudos de Caso Mecânicos — lido

### Resposta direta à pergunta feita

**Sim, cada caso diz explicitamente se é exceção ou regra replicável.** Todos os nove
trazem um callout `> [!warning] É exceção ou regra?` com veredito em negrito, e a nota
fecha com um **índice rápido exceção × regra** que resume os doze vereditos numa tabela.
Nesse quesito específico é a nota mais bem construída do vault, e eu não mexeria na
estrutura.

**Dá para extrair uma regra de jogo a partir deles?** Parcialmente. Dá para extrair o
*princípio* — a nota é ótima nisso — mas quase nunca o *número*. Ver 08-D e 08-G.

### Problemas

**08-A — Contradição direta com o apêndice sobre a trava de aptidão** · `Estudos de Caso Mecânicos.md` × `09/Tabelas de Referência Rápida.md`
Tipo: **furo lógico — bloqueador.**
Caso 2, "versão barata", enuncia como regra ilustrada: "*Uma aptidão baixa nunca alcança
esse patamar — a barreira é **intransponível** por quem tem pouco talento.*"
E o veredito do mesmo caso, oito linhas abaixo: "**Regra plenamente replicável.**
*Qualquer* cultivador com pedras suficientes, disciplina e garantia de não ser
interrompido consegue."
As duas frases não podem ser verdadeiras ao mesmo tempo. Se o método lento e sustentado é
plenamente replicável por qualquer um, então a aptidão **deixa de ser uma trava** — e
todo o edifício do apêndice desaba junto: `Tabelas de Referência Rápida` §2 diz que "quem
não alcança a porcentagem exigida simplesmente **não rompe a parede**, por mais séculos
que cultive", e §1 diz que "o 55% explica de imediato por que o grau C é uma sentença
social".
Esta é a decisão de design mais importante do jogo inteiro — **aptidão é um teto duro ou
um imposto?** — e o material me dá as duas respostas, em notas que se citam mutuamente.
Sugestão: decidir e escrever. Se o método lento funciona, ele precisa de uma trava
própria (custo em pedras proibitivo? só funciona de 1→2? risco de morte?) para que a
aptidão continue significando algo. Se não funciona para qualquer um, o veredito precisa
dizer "replicável **por quem já tem aptidão suficiente**; o que o caso mostra é que se
pode substituir potência por tempo, não talento por dinheiro".

**08-B — A nota mais densa do vault é a que tem menos links** · `Estudos de Caso Mecânicos.md`
Tipo: **jargão não explicado — sério.**
Não há **um único wikilink no corpo da nota** — só na seção "Relações", no fim. E é
justamente a nota que empilha mais jargão: *abertura interna*, *Gu Vital*, *essência*,
*refino*, *espírito guardião*, *terra abençoada*, *gruta-céu*, *território pessoal*,
*fundação*, *anexação*, *provações*, *dao marks*, *pedras primevas*, *rank*, *attainment*
(sem usar a palavra — ver 08-C).
Termos em **negrito** sem link me sinalizam "isto é importante" e ao mesmo tempo "vire-se".
Alguns nunca são definidos em lugar nenhum que eu pudesse achar sozinha, notadamente
**"fundação"** — que é o critério decisivo do caso 6 ("o teste não é entre ranks: é entre
fundações") e do caso 6 ("a fundação absurda de quem os executou"). Eu não sei se fundação
é o tamanho da terra abençoada, o total de dao marks, o acervo de artefatos, ou outra
coisa. Sem isso, o caso 6 é ilegível para mim.
Sugestão: linkar na primeira ocorrência de cada termo, e acrescentar uma definição de
"fundação" — nem que seja de uma linha, no bloco "Como usar esta nota".

**08-C — O caso 6 cai exatamente na armadilha que o apêndice avisa** · `Estudos de Caso Mecânicos.md`
Tipo: jargão ambíguo.
`Tabelas de Referência Rápida` abre com um callout dedicado avisando que **"Mestre Gu"** e
**"Mestre"** (nível de attainment) são coisas diferentes que dividem a palavra em
português. O caso 6 então escreve: "*um nível de domínio '**mestre**' basta para anexar
territórios de rank 6; um domínio **quase-superior** serve para a maioria deles; mas
'mestre' **não** basta para um território de rank 7*" — sem nunca dizer a palavra
*attainment*, sem linkar, e usando "quase-superior", que não é um degrau da escala do
apêndice (lá os degraus são Quase Grão-Mestre, Grão-Mestre, Quase Grande Grão-Mestre,
Grande Grão-Mestre, Quase Supremo, Supremo Grão-Mestre).
"Quase-superior" é qual deles? Levei três leituras para entender que o caso está falando
de attainment, e ainda não sei mapear o degrau.
Sugestão: usar os nomes exatos da escala de `[[08 - Attainment|Attainment]]` e linkar.

**08-D — Os casos replicáveis não têm preço** · `Estudos de Caso Mecânicos.md`
Tipo: **falta de utilidade para design — sério.**
A nota promete, no callout de abertura, que cada caso traz "**os recursos gastos**". Ela
cumpre em prosa e falha em número, justamente nos casos marcados como replicáveis — que
são os únicos que eu posso transformar em regra:
- Caso 2 (versão barata), o mais jogável de todos: "*absorvendo pedras primevas em
  paralelo*", "*uma quantidade grande de pedras primevas*". **Quantas?** É o item de
  orçamento mais importante que um personagem de rank 1 vai enfrentar na campanha, e o
  número não está aqui nem em `Pedras Primevas`.
- Caso 3 (versão ativa, "regra corrente e cotidiana"): "*apenas a posse do Gu superior*".
  Quanto tempo leva o refino assistido? Quanto ele economiza?
- Caso 5: "*os vinte conjuntos de materiais*" — de quê, custando quanto?
Sugestão: uma linha "custo estimado em pedras primevas" em cada caso replicável, marcada
como reconstrução onde a obra não der o número. Sem isso a nota me dá boas cenas e nenhuma
planilha.

**08-E — "2% de aptidão" é ambíguo justamente onde mais importa** · `Estudos de Caso Mecânicos.md`
Tipo: número mal especificado.
Caso 2, ritual demoníaco: "*mesmo com limpeza imediata, a perda de aptidão é de cerca de
**2%**, irrecuperável*".
Dois por cento de quê? Se são **pontos percentuais** na escala do apêndice (onde as faixas
têm 20 pontos de largura), um cultivador grau B de 61% cai para 59% e **muda de grau**,
perdendo a possibilidade de chegar ao rank 3. Se são 2% relativos, a perda é de ~1,2 ponto
e quase não importa. A diferença entre as duas leituras decide se este atalho é um preço
alto ou um detalhe.
E o mesmo caso diz que o Gu resultante permite quebrar a barreira com "*cerca de **38%**
dessa energia*", quando o limiar canônico do apêndice é 55%. Por que 38 e não 55? Nunca é
explicado, e é a única pista que eu teria de como o atalho realmente funciona.
Sugestão: escrever "2 pontos percentuais de aptidão (ex.: 61% → 59%)" e uma frase
explicando por que o ritual reduz o limiar efetivo.

**08-F — Um termo em inglês aparece do nada, e briga com a nota de sociedade** · `Estudos de Caso Mecânicos.md`
Tipo: menor, terminologia.
Caso 9: "*escravos 'dentre os **feathermen** no chão'*". É o único termo racial não
traduzido do material que li, sem glossa e sem link. `Cultura das Cinco Regiões` chama o
mesmo povo de "**uma raça alada**", e `Tribunal Celestial e Grandes Forças` fala em
"**humanos variantes**".
Sugestão: usar o termo do glossário e citar o original entre parênteses uma vez.

**08-G — Nenhum caso vira regra proposta** · `Estudos de Caso Mecânicos.md`
Tipo: falta de utilidade para design.
O callout de abertura diz que os casos servem a três usos, e o segundo é "**virar regra
opcional**". Nenhum caso chega a enunciar uma. Os blocos "Para o design" são bons, mas
falam de *ficção* ("cria um relógio no meio da aventura", "é uma inversão maravilhosa
para uma sessão de assalto") — nunca de *mecânica*.
O caso 5 é o exemplo mais gritante: ele descreve um sistema de tentativas limitadas com
contagem assimétrica, que é literalmente uma regra pronta, e mesmo assim não a escreve.
Sugestão: fechar cada caso com uma linha `**Regra proposta:**` em itálico. Duas frases
bastam. É a diferença entre uma coletânea de precedentes e um capítulo de manual.

**08-H — Cobertura concentrada no topo** · `Estudos de Caso Mecânicos.md`
Tipo: cobertura / utilidade.
Dos nove casos, **seis** se passam na camada imortal (1, 4, 6, 7, 8 e parte do 9). Só o
caso 2 e o caso 3 são utilizáveis numa campanha de ranks 1–3, que é onde qualquer mesa
começa e onde a maioria das mesas vai passar a vida inteira.
Sugestão: acrescentar dois ou três casos mortais — uma disputa de sucessão de clã resolvida
por regra, um golpe de leilão, uma missão de grupo de cinco que deu errado — com o mesmo
formato. O formato é bom demais para servir só ao endgame.

### O que está bom nesta pasta

- **O veredito "exceção ou regra" em todo caso, mais o índice-resumo no fim.** É
  exatamente o que eu precisava e quase nenhum material de cenário faz. Isso responde
  sozinho a metade das minhas dúvidas de "posso generalizar isto?".
- **Os quatro meta-padrões na abertura** dão uma chave de leitura antes dos casos, e o
  caso 5 até se refere a eles por número. Funciona.
- **O caso 4 (três vias para tomar um território) é o melhor pedaço de design do vault**:
  três rotas com preços diferentes, uma delas explicitamente marcada como "não funciona",
  e a razão pela qual não funciona é uma regra generalizável (trava de força × trava de
  reconhecimento, e a violência queima a segunda de forma irreversível). Eu escreveria uma
  subclasse de aventura inteira em cima disso.
- **O caso 9 (brechas de contrato)** é uma aula. Quatro brechas de sofisticação crescente,
  todas com a mesma explicação estrutural ("o contrato é um mecanismo, não um árbitro"), e
  um conselho de design correto: escreva o juramento e deixe os jogadores lerem.
- **O caso 8 (fazenda de provações)** é o melhor NPC-patrono do vault, e a nota entende
  por quê: a exploração funciona *porque as duas partes ganham de verdade*.
- **"Personagens aparecem apenas como 'um cultivador de rank X'"** — a decisão de despir os
  casos de nomes próprios funcionou. Aqui a ausência de nomes ajuda, ao contrário do que
  acontece em 05 e 07.

---

## 09 - Apêndices — parcial: `Tabelas de Referência Rápida.md`

> Esta é a nota que a coordenação pediu para conferir contra as notas de conteúdo.
> Conferi as três suspeitas levantadas, mais o que encontrei por conta própria.

### Veredito sobre as três suspeitas levantadas

**(1) Tabela de amplificação por dao marks — a suspeita procede, e é pior do que parecia.**
Ver 09-A.

**(2) Piso de 100.000 dao marks no rank 8 — o apêndice está certo; o erro sobreviveu em
outro lugar.** O apêndice traz rank 8 = 30.000–300.000 e ainda documenta a correção num
callout: *"Uma versão anterior desta tabela trazia '100.000' como piso do rank 8; era erro
nosso, sem base no texto, e foi corrigido."* Refiz a aritmética das três linhas e ela
fecha exatamente (9.000 / 30.000 / 300.000 — conferi as três multiplicações). `01 -
Cultivo/Dao Marks.md` também já está corrigido. **Mas a correção não propagou:** ver 09-G.

**(3) Escada 65/75/85% — está corretamente marcada como reconstrução em todos os lugares.**
Rastreei as cinco ocorrências no vault (`LEIA-ME`, `Ranks e Avanço`, `Aptidão`, `Visão
Geral do Cultivo`, e o apêndice). Todas dizem que é reconstrução, e o apêndice ainda
acrescenta um contraexemplo honesto (um caso em que 90% não bastou para 3→4). **Nada a
corrigir aqui — pelo contrário, é o padrão que o resto do vault deveria seguir.** A única
ressalva é indireta: ver 09-E, onde a escada inferida é usada silenciosamente para derivar
outra coluna.

### Problemas

**09-A — A tabela de amplificação anuncia uma fórmula fechada, tem o número de âncoras errado, e não fecha** · `Tabelas de Referência Rápida.md` §7
Tipo: **inferência disfarçada de fato + número que não bate — bloqueador.**
O texto diz: "*A obra fecha a fórmula com **três** âncoras numéricas explícitas:*" — e a
tabela logo abaixo tem **quatro** linhas (100, 1.000, 10.000, 50.000). Erro de contagem
óbvio, mas o problema de fundo é maior.
Testei se os quatro pontos fecham como fórmula única. Não fecham:
- `mult = 1 + marcas/1000` acerta em cheio as duas primeiras linhas (100 → 1,1× = "+10%";
  1.000 → 2×) e **erra as duas últimas** (daria 11× e 51×, a tabela diz 10× e 50×).
- `mult = marcas/1000` acerta as duas últimas (10× e 50×) e **erra as duas primeiras**
  (daria 0,1× e 1×).
As duas leituras diferem exatamente em 1, ou seja, na diferença entre "fator de
amplificação" e "bônus acrescentado". Provavelmente as duas últimas linhas são
arredondamentos de 11× e 51×, mas **a nota nunca escreve a fórmula**, então eu não tenho
como saber — e, o que é pior, não tenho como interpolar. **Quanto rende 5.000 dao marks?
5× ou 6×?** Essa é a pergunta que eu, como designer, faço em todo combate, e o apêndice
não responde.
Some-se a isso que a tabela viola a convenção declarada da própria nota: ela é apresentada
como texto literal da obra ("a obra fecha a fórmula"), sem marca `inferido`, quando na
melhor das hipóteses são quatro pontos avulsos.
Sugestão: (a) corrigir "três" para "quatro"; (b) escrever a fórmula explicitamente —
sugiro `efeito = base × (1 + dao marks ÷ 1.000)` — marcá-la como `inferido`, e anotar que
as duas últimas linhas da obra são arredondamentos dela; (c) dizer sobre o que incide a
amplificação (dano? duração? alcance? tudo?).

**09-B — Duas tabelas da mesma nota discordam sobre o rank 8** · `Tabelas de Referência Rápida.md` §6 × §8
Tipo: número que não bate.
A §6 calcula o rank 8 como "**24 × 750 + 3 × 7.250 + 3 miríades × 86.750 = 300.000**" —
ou seja, 24 tribulações celestiais, 3 grandes e 3 miríades.
A §8, coluna "Total ao completar o rank", registra para o rank 8 apenas: "**3 tribulações
miríades**". Somem as 24 celestiais e as 3 grandes que a §6 usa na conta.
E não é descuido de arredondamento: as linhas dos ranks 6 e 7 da §8 listam a composição
completa ("27 calamidades + 3 tribulações celestiais", "24 calamidades + 3 celestiais + 3
grandes"). Só a linha do rank 8 é incompleta — e é justamente a que sustenta o número mais
importante do sistema, os 300.000 do rank 9.
(Confirmo que a §8 está internamente coerente: com celestial /10, grande /50 e miríade
/100 em 300 anos, dá 24 + 3 + 3. Só a célula da tabela está incompleta.)
Sugestão: completar a célula para "24 celestiais + 3 grandes + 3 miríades". Também vale
preencher a linha do rank 9, hoje toda com `—`: um Venerável ainda tribula?

**09-C — O bloco "Para o design" da §5 contradiz a nota de economia inteira** · `Tabelas de Referência Rápida.md` §5 × `06/Economia Imortal.md`
Tipo: **furo lógico — sério.**
O apêndice conclui: "*riqueza imortal é **literalmente intransferível**, o que **mata pela
raiz qualquer economia de mercenariado no topo** e força alianças a serem feitas em
favores, não em pagamento.*"
`Economia Imortal` descreve exatamente o contrário: uma praça de comércio mundial, taxa de
serviço, juros de 10% ao mês, seis credores com termos diferentes, custódia remunerada,
uma guerra de preços de doze milhões, e ressurreição precificada em pontos de recurso.
A reconciliação existe — as **contas** (uva verde etc.) são pessoais e intransferíveis, as
**pedras de essência imortal** são moeda corrente — mas o bloco de design funde as duas
coisas e tira uma conclusão de sistema a partir da fusão.
Se eu tivesse lido o apêndice primeiro (como o LEIA-ME recomenda), teria projetado uma
camada de alto nível **sem economia monetária**, e depois descoberto uma nota inteira
descrevendo a economia que eu decidi que não existia.
Sugestão: reescrever o bloco distinguindo os dois instrumentos em uma frase — "as contas
de essência são pessoais e intransferíveis; a pedra de essência imortal é a moeda que
circula" — e trocar a conclusão por algo verdadeiro (por exemplo: o que não se compra no
topo são os *artefatos*, não os serviços).

**09-D — Duas medidas de produção da mesma coisa, com 100× de diferença** · `Tabelas de Referência Rápida.md` §5 × §9 × `06/Economia Imortal.md`
Tipo: **ordem de grandeza — sério.**
- §5: "*o núcleo de uma abertura imortal excepcional de rank 7 produz cerca de **16 contas
  de red date por dia**, o equivalente a 1.600 pedras de essência imortal diárias*".
- §9, grades de terra abençoada: produção de "**10+ contas/ano**" (baixa) a "**50+
  contas/ano**" (super).
Anualizando a §5: 16 × 365 ≈ **5.840 contas por ano**, contra as 50+ da melhor grade da
§9. Cento e vinte vezes de diferença, na mesma nota, sem uma linha de ponte. Entendo que a
§9 fale de uma terra recém-nascida de rank 6 (uva verde) e a §5 de um núcleo excepcional
de rank 7 — mas o leitor tem que adivinhar isso, e mesmo adivinhando a distância não fecha
com o ×100 por rank que a própria nota estabelece.
Pior: 1.600 pedras/dia = ~584.000 pedras/ano, enquanto `Economia Imortal` dá como riqueza
típica de um rank 7 "milhares a mais de 10.000 pedras" **no total**. Um único cultivador
produziria, por semana, mais do que o patrimônio inteiro de um par seu.
Sugestão: rotular cada número com rank e denominação ("terra abençoada grade baixa,
recém-ascendida, rank 6: 10+ contas de uva-verde/ano"), e checar qual dos dois está fora
de escala. Sem isso não consigo precificar renda no alto nível — que é a espinha de
qualquer campanha de endgame.

**09-E — Uma coluna canônica derivada de números inferidos** · `Tabelas de Referência Rápida.md` §1
Tipo: inferência disfarçada de fato + contradição interna.
A nota declara na abertura: "*Números marcados como `inferido` são extrapolações... **Todo
o resto é numeração literal da obra**.*"
A coluna "**Teto de rank esperado**" da tabela de aptidão não tem marca `inferido`, mas só
pode ter sido derivada da escada 65/75/85 — que é reconstrução. Um grau B (60–79%) "chega
a rank 3, eventualmente rank 4" **porque** o limiar 3→4 seria 75%. Se a escada mudar, a
coluna inteira muda.
E há uma contradição aritmética direta: **grau D = 20–30%**, teto declarado "rank 1; **no
máximo rank 2**". Mas romper para o rank 2 exige 55%, que é o único limiar **canônico** da
obra. Um D nunca chega lá. A célula deveria dizer "rank 1, e só isso".
Sugestão: marcar a coluna como `inferido` e corrigir a célula do D. Se o "no máximo rank
2" vem de casos em que a aptidão foi elevada artificialmente, dizer isso na célula — é
informação útil, mas é outra coisa.

**09-F — Referência cruzada apontando para a seção errada** · `Tabelas de Referência Rápida.md` §2
Tipo: menor.
A linha "5 → 6" diz "*a ascensão a Imortal não é percentual (**ver seção 8**)*". A seção 8
é "Cadência de calamidades e tribulações", que trata do que acontece *depois* de já ser
imortal. O que explica o critério de ascensão (qi humano acumulado, constituição extrema
ou Grão-Mestre) é a **seção 9**.
Sugestão: trocar para "ver seção 9".

**09-G — A correção do rank 8 não propagou para as notas de conteúdo** · `Tabelas de Referência Rápida.md` §6 × `01 - Cultivo/Tornar-se Venerável.md`
Tipo: **número que não bate entre notas — sério.**
O apêndice e `01 - Cultivo/Dao Marks.md` dizem: rank 7 = 9.000–30.000; rank 8 =
30.000–300.000.
`01 - Cultivo/Tornar-se Venerável.md` ainda diz: "*um rank 7 comum tem entre **dez e
trinta mil**; um rank 8, entre **cem e trezentos mil**.*"
Ou seja, o piso de 100.000 que o apêndice declara ter corrigido continua vivo na nota que
explica a condição mais importante do sistema (as 300.000 dao marks para virar Venerável).
Está fora das minhas pastas, mas afeta diretamente a confiança que posso depositar no
apêndice: se a correção não foi varrida, não sei o que mais ficou para trás.
Sugestão: corrigir a frase e, mais importante, adotar a regra de que **os números vivem só
no apêndice** e as notas de conteúdo remetem a ele em vez de repetir. Hoje os mesmos
números estão duplicados em três e quatro lugares (ver também 06-M e 06-P).

**09-H — A tabela de refino tem três taxas incompatíveis para o rank 6** · `Tabelas de Referência Rápida.md` §12
Tipo: número que não bate.
Na mesma tabela: "Gu Imortal de rank 6, refinador comum: **menos de 1%**"; "Especialista
reconhecido, rank 6: **40%**"; e "Número típico de tentativas por sucesso (referência de
mercado): **50 a 60**".
Cinquenta a sessenta tentativas por sucesso implica uma taxa de ~1,7–2%, que não é nem
"menos de 1%" nem 40%. As três linhas são apresentadas lado a lado sem dizer a que
população cada uma se refere.
Sugestão: acrescentar uma coluna "de quem é esta taxa" (refinador comum / especialista /
média de mercado ponderada), ou separar em duas tabelas.

### O que está bom nesta nota

Apesar da lista acima, esta é a **nota mais bem construída do vault do ponto de vista de
engenharia de informação**, e vários dos seus achados são exatamente o que eu queria de um
apêndice:

- **As duas convenções declaradas na abertura** — `—` significa "a obra não diz", e
  `inferido` marca extrapolação — são a prática correta, e são seguidas na maior parte da
  nota. Isso é raro e vale muito.
- **O callout que separa "Mestre Gu" de "Mestre" (attainment)** antecipa uma confusão real
  antes que ela aconteça. Boa didática.
- **Admitir o vão 31–39% na escala de aptidão** em vez de preenchê-lo é honestidade
  intelectual e me diz exatamente onde eu tenho liberdade de design.
- **O callout que mostra a aritmética das faixas de dao marks** (27 × 250 + 3 × 750 =
  9.000 etc.) é o melhor recurso didático do vault inteiro: não me pede para confiar, me
  mostra a conta. Refiz as três e fecham.
- **Documentar a própria correção** ("uma versão anterior trazia 100.000; era erro nosso")
  é uma prática que eu gostaria de ver em todo o material.
- **O aviso de que a escada 65/75/85 pode ser ignorada sem contradizer o cânone** me
  autoriza explicitamente a inventar. É o tipo de permissão que economiza semanas.
- **A §8 é uma tabela de encontros pronta** para o reino imortal: quatro classes de
  provação, recompensa fixa, cadência conhecida e um relógio manipulável pelo jogador.
- **A §10 (attainment) resolve um problema clássico** ao separar "o que você consegue
  fazer" de "com quanta força você faz", e a regra de que attainment insuficiente produz o
  **efeito errado** (não um efeito fraco) é ouro de mesa.
- **Nenhum wikilink quebrado.** Rodei uma verificação de todos os links das pastas 05 a 09
  contra os nomes de nota e os aliases: os 73 arquivos e 222 aliases cobrem tudo. Isso
  significa que os apontamentos "ver nota X" que eu segui sempre chegaram a algum lugar.

---

## 09 - Apêndices — restante das notas

### Resposta direta às perguntas feitas

**As tabelas são autoexplicativas?** As de `Tabelas de Referência Rápida` quase sempre sim
(com as exceções acima). As dos catálogos, sim — a nota-índice explica as colunas e as
convenções antes de qualquer lista, o que é o certo.

**O glossário serve para consulta rápida?** Como **dicionário da obra**, sim, e é
excelente. Como **autoridade sobre a terminologia deste projeto**, não: a coluna que ele
chama de "PT adotado" descreve escolhas que o vault não fez, e em dois pontos contradiz o
próprio glossário. Ver 09-I, que considero o achado mais caro desta pasta depois de 09-A.

### Problemas

**09-I — O glossário declara adotar termos que o vault não usa, e contradiz a si mesmo** · `Glossário EN-PT.md`
Tipo: **inconsistência de nomenclatura — bloqueador.**
A nota define a coluna do meio assim: "*PT adotado — **a tradução que este projeto usa**.*"
Contei as ocorrências no vault inteiro (fora de `_pipeline`). Ela não descreve o projeto:

| Termo (EN) | Glossário diz que adotou | O vault realmente usa | Contagem |
|---|---|---|---|
| primeval essence | essência primordial | **essência primeva** | 43 × 10 |
| primeval stones | pedra primordial | **pedras primevas** | 64 × 7 |
| primeval sea | mar primordial | mar primevo | — |
| rank (1–9) | **nível** | **rank** | 476 × 170 |
| attainment level | nível de realização | **attainment** | 71 × 7 |
| refining | refinamento | **refino** | 227 × 43 |
| killer move | movimento assassino | *Killer Moves* (título de nota) | — |
| Heavenly Court | Corte Celestial | **Tribunal** Celestial (título de nota) | — |

Três agravantes:
1. **O glossário contradiz o próprio glossário.** A tabela da §1 diz que `rank (1–9)` →
   "**nível**", e a §9.1, dez páginas abaixo, recomenda o contrário com todas as letras:
   "*neste projeto usamos **rank** para a escada de 1 a 9*".
2. **O glossário contradiz uma nota que decide explicitamente o oposto.** A §9.4 diz
   "**Adotamos 'essência primordial'**"; o rodapé de `06/Pedras Primevas.md` diz
   "**Adotamos 'pedra primeva' nesta base** por consistência com 'essência primeva'". As
   duas notas anunciam decisões contrárias, cada uma como se fosse a autoridade.
3. **A marcação `°` fica sem sentido em palavras comuns.** `°` é definido como "sem
   tradução registrada... **o termo fica em inglês**". Estão marcados assim: `clan`,
   `sect`, `Immortal Gu`, `recipe`, `inheritance`. O vault escreve clã, seita, Gu Imortal,
   receita e herança em português, centenas de vezes. Ou a convenção não vale para essas
   palavras, ou o vault a viola sistematicamente — e eu não sei qual.
Sugestão: separar em **duas colunas** — "PT da tradução brasileira" e "PT usado neste
vault" — que é o que a nota de fato precisa ter. Elas divergem por decisão consciente em
vários casos (o rodapé de `Pedras Primevas` explica bem por quê), e fingir que são uma só
é o que produz o erro. E resolver as três contradições acima antes de qualquer outra
coisa: enquanto o glossário não for confiável, nenhum termo do vault é.

**09-J — A linha do tempo nomeia oito Veneráveis e afirma que são dez** · `Linha do Tempo e Eras.md`
Tipo: **furo lógico / contagem — sério.**
A nota abre com um callout categórico: "*Os Veneráveis... foram exatamente **dez em toda
a história do mundo**... Eles aparecem aqui como **marcos históricos e estruturais**.*"
Contando os que ela efetivamente nomeia, no corpo e na tabela-resumo: Primordial Origin,
Star Constellation, Reckless Savage, Thieving Heaven, Giant Sun, Genesis Lotus, Spectral
Soul, Red Lotus. São **oito**. Um nono aparece como "*e um terceiro do mesmo período*",
sem nome. O décimo não aparece de forma alguma.
Verifiquei contra o resto do vault: os dois que faltam são o **Paradise Earth Immortal
Venerable** e o **Limitless Demon Venerable**, ambos amplamente documentados em `07 -
Veneráveis e Legados`. Não é que a obra não os nomeie — é que a linha do tempo os perdeu.
Para mim isso é grave porque a nota se apresenta como o **eixo temporal** que permite
"situar uma campanha em qualquer época e saber o que existia". Se dois dos dez marcos
estruturais não estão datados, há eras inteiras onde eu não sei o que existia.
Sugestão: alocar os dois nas eras corretas, substituir "um terceiro do mesmo período" pelo
nome, e — como salvaguarda — acrescentar à tabela-resumo uma linha de verificação
("total: 10").

**09-K — Nomes dos Veneráveis em inglês, caminhos em português, na mesma frase** · `Linha do Tempo e Eras.md`
Tipo: inconsistência de nomenclatura.
"*o **Giant Sun Immortal Venerable** (criador secreto do **caminho da sorte**...)*". A nota
traduz todos os caminhos e todos os conceitos, e mantém todos os nomes próprios em inglês,
inclusive a parte genérica do título — "Immortal Venerable" e "Demon Venerable" — que o
`Glossário` traduz como "Venerável Imortal" e "Venerável Demônio" e discute na §9.6.
Também não se explica em lugar nenhum da nota **qual é a diferença** entre um "Immortal
Venerable" e um "Demon Venerable". Deduzi que é correto × demoníaco, mas a linha do tempo
usa os dois rótulos dezenas de vezes sem nunca dizer.
Sugestão: adotar a forma do glossário ("Venerável Imortal Giant Sun") ou manter o inglês
integralmente, mas escolher — e glosar a distinção Imortal/Demônio na primeira ocorrência.

**09-L — Três taxonomias diferentes de "caminho", e nenhuma é a lista de classes** · `Catálogo de Gu - Mortais.md` × `Glossário EN-PT.md` × `03 - Paths/`
Tipo: **confusão estrutural — sério.**
A pergunta que eu preciso responder para desenhar o jogo é "**quantas classes existem e
quais são?**". O material me dá três respostas diferentes:
- `03 - Paths/` tem **17** notas de caminho (blood, dream, enslavement, food, heaven,
  luck, poison, refinement, rule, soul, space, star, strength, sword, time,
  transformation, wisdom).
- O `Glossário` §3 lista **21** caminhos — os 17 acima mais human, theft, information,
  formation e qi.
- O `Catálogo de Gu - Mortais` se organiza em **cerca de 29 seções**, e várias não são
  caminhos de forma alguma: "Defesa e reforço corporal", "Furtividade e disfarce",
  "Contratos e juramentos", "Armazenamento e logística", "Cura e vida", "Gu lendários e
  conceituais", "Linhagem lunar". E inclui como caminhos vários que não têm nota em `03`:
  luz, fogo, gelo/água, madeira, terra, som/raio, roubo, homem, formação.
A nota-índice do catálogo **avisa** parte disso ("nos primeiros volumes o vocabulário
formal de caminhos ainda não existia; nesses casos os Gu foram agrupados pela família
funcional"), o que é honesto. Mas o cabeçalho da seção "Como usar" continua afirmando
"*cada seção é um **caminho** (path)*", o que não é verdade para um terço delas.
E o problema de fundo permanece: `Linha do Tempo` atribui a Veneráveis a criação dos
caminhos "do roubo", "da madeira" e "da água" — três caminhos centrais na história do
mundo, **nenhum com nota em `03`**.
Sugestão: uma tabela única, num só lugar, com as colunas `Caminho | Tem nota? | Tem seção
de catálogo? | É jogável como especialização?`. Sem ela eu não consigo nem começar a lista
de classes, que é a primeira decisão de um TTRPG.

**09-M — A marcação `⭐` prometida não tem função onde está prometida** · `Catálogo de Gu.md`
Tipo: menor.
A nota-índice diz: "*Gu Imortais aparecem marcados com ⭐*". Mas a mesma nota acabou de
explicar que mortais e imortais foram separados em **dois arquivos distintos**. Num
catálogo só de imortais, marcar todos com ⭐ não distingue nada; num catálogo só de
mortais, não deveria haver nenhum.
Sugestão: ou remover a convenção do índice, ou dizer onde ela se aplica (imagino que seja
para Gu Imortais citados dentro do catálogo mortal, o que faria sentido — mas então
precisa estar dito).

**09-N — A nota-índice do catálogo não dá a contagem** · `Catálogo de Gu.md`
Tipo: falta de utilidade para design.
Eu queria saber, antes de abrir dois arquivos de 40 KB: **quantos Gu existem catalogados,
por rank e por caminho?** É a primeira informação de calibragem que um designer procura —
ela me diz se tenho 30 ou 300 itens para trabalhar, e onde estão os buracos.
Sugestão: acrescentar ao índice uma tabela de contagem (Gu por rank; Gu por caminho), mais
uma linha dizendo quantos têm dieta informada. O aviso honesto de que "a coluna Alimento
tem muitos traços" ficaria muito mais útil com o número ao lado.

### O que está bom nestas notas

- **`Linha do Tempo e Eras` é conceitualmente a nota mais útil da pasta**, e a frase que a
  abre resume por quê: "*Ambientar em outra era não é trocar o cenário — é trocar as
  **regras disponíveis**.*" A tabela "O que muda nas regras do mundo" (antes × depois da
  Grande Era) é um documento de design pronto: doze linhas, cada uma um par de regras
  contrastadas. Eu construiria duas campanhas com aquilo sem consultar mais nada.
- A tabela-resumo final da linha do tempo (era / marca estrutural / o que nasce /
  Veneráveis) é exatamente o formato certo para escolher uma ambientação — pena a lacuna
  do 09-J.
- **O glossário, apesar do 09-I, faz três coisas raras e valiosas.** A §9 inteira
  (avisos sobre a tradução brasileira, nove casos com recomendação) é trabalho de curadoria
  de verdade. A §9.8 (espírito da terra × espírito celestial) me salvou de tratar como erro
  o que é distinção real do mundo, e ainda me deu de brinde uma pista de rank. E a §8
  (unidades chinesas: li, mu, catty, jun, liang) é o tipo de coisa que ninguém lembra de
  incluir e todo mundo precisa.
- **A honestidade metodológica do glossário no fim** ("a cobertura é contínua nos capítulos
  iniciais e esparsa no restante... nenhum termo desta nota foi traduzido por conta
  própria") me diz exatamente quanto peso dar a cada linha.
- **A nota-índice do `Catálogo de Gu` está estruturalmente correta**: explica as colunas e
  as convenções *antes* das listas, declara que o catálogo não é exaustivo, e — o melhor
  — transforma a incompletude em regra de design ("inventar um Gu inédito é uma conquista
  de personagem, não uma quebra de cânone"). É a resposta certa para um catálogo que nunca
  poderá ser completo.
- **A convenção `—` = "a obra não informa", repetida em todas as notas da pasta**, e
  respeitada. E o conselho explícito sobre o que fazer com os traços da coluna Alimento
  ("se precisar de dietas para todos, invente-as — o padrão é que a comida seja
  tematicamente ligada ao efeito") é exatamente o tipo de permissão que eu preciso.
- **"Um Gu = exatamente um efeito, e todo poder complexo vem de combinar vários"**, com
  teto de dois a três Gu simultâneos: é uma mecânica de construção de personagem inteira
  em duas linhas, e está no lugar certo (o bloco "Para o design" do catálogo).
