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
Sugestão: usar o mesmo termo do resto do vault e linkar `[[Visão Geral dos Paths]]` na
primeira ocorrência. Se forem coisas diferentes, dizer a diferença em uma frase.

**06-I — Jargão pesado não definido nem linkado** · `Economia Imortal.md`, `Como um Mestre Gu Ganha a Vida.md`, `Eventos e Instituições Jogáveis.md`
Tipo: jargão não explicado.
Lista do que usei sem entender:
- **"veias de dao"** (`Economia Imortal`) — "dao" nunca aparece definido nesta pasta. Há
  uma nota `[[Dao Marks]]` em `01 - Cultivo`, não linkada aqui.
- **"provações"** / **"calamidade"** (`Economia Imortal`, `Eventos e Instituições
  Jogáveis`) — usadas como se eu soubesse o que são. Existe `[[Tribulações e
  Calamidades]]`, nunca linkada.
- **"fazenda de provações"** (na seção "Relações" de `Economia Imortal`) — um termo que
  não aparece em lugar nenhum do corpo de nenhuma nota desta pasta. Fui procurar e não
  achei.
- **"gruta-céu"** (`Eventos e Instituições Jogáveis`) e **"Domínio recluso de céu e
  terra"** (`Economia Imortal`) — dois nomes, aparentemente para a mesma coisa, nenhum
  explicado, nenhum linkado a `[[Blessed Lands e Grotto-Heavens]]`, que existe.
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
não-precificável — ver [[Blessed Lands e Grotto-Heavens]]").

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
