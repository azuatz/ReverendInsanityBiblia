# Auditoria de completude — domínio Mundo (`04 - Mundo/`)

> Relatório incremental. Auditoria de **completude de conteúdo**: o objetivo declarado pelo
> usuário é que "como o mundo funciona" esteja completo o bastante para um sistema de RPG
> explicar o cenário a quem nunca leu a obra.
>
> Método: (1) leitura das 15 notas da pasta; (2) confronto com `_pipeline/rascunho/mundo-e-cosmologia.md`
> e com as pesquisas de `_pipeline/pesquisa/`; (3) leitura do topo de `_pipeline/LACUNAS.md`;
> (4) varredura dirigida do TEXTO-FONTE nos assuntos que nenhum dos dois cobria.

## Lacunas encontradas

### 🔴 BLOQUEADORES (a designer não consegue rodar uma cena sem isso)

**L1 — O relógio e o calendário do mundo não existem em nota nenhuma.** `severidade: alta`
Nenhuma das 15 notas responde "que horas são?", "que mês é?", "quanto dura um ano?".
Grep na pasta: `calendário` só aparece como metáfora ("calendário de desastre", "calendário
institucional"); `meia-noite`, `estações do ano` como sistema, `eclipse` e `hora` como unidade
não aparecem em lugar nenhum. Uma mestra que precise dizer "vocês chegam ao anoitecer do
terceiro dia do quinto mês" não tem onde consultar. Evidência de que a obra **tem** esse
material: cap. 213 mede tempo em "enough time passed for an incense stick to burn"; cap. 907
data um fenômeno anual por mês do calendário ("during May in Eastern Sea"); caps. 34, 60, 131,
205, 365 usam meia-noite como marco operacional de cultivo e de vigília.

**L2 — O mecanismo físico do dia e da noite está pela metade, e do jeito que está induz erro.**
`severidade: alta`
`01 - Visão Geral do Mundo` e `13 - Cosmologia` afirmam que os dois céus "se revezam como dia e
noite" — o que é canônico (cap. 466: "the two alternating between day and night"; cap. 740) —,
mas **nenhuma nota diz que existe um sol**, e a obra o menciona centenas de vezes ("the sun
rose from the east", cap. 21; "the blazing sun slowly descended from the highest point in the
sky", cap. 73). Uma leitora leiga conclui, das notas como estão, que este mundo **não tem sol**
— e vai desenhar um cenário errado. O texto que costura as duas coisas existe e é preciso
(cap. 389): a luz do sol da era imemorial "could pierce through the nine heavens"; hoje ela
"had weakened to the extreme, being able to pierce through **only the white heaven**". Ou seja:
o sol é real, os céus são filtros, e a noite é o céu negro barrando a luz.

**L3 — A biosfera ordinária (plantas, bichos comuns, comida, lavoura, rebanho) não tem nota.**
`severidade: alta`
`07 - Bestas Gu e Reis Fera` cobre magnificamente a fauna **que hospeda Gu**; o Atlas cobre
flora e fauna **por região**. Falta a camada transversal: o que é um animal normal neste mundo,
o que se planta, o que se come, quem cria gado, o que um mortal janta. Grep na pasta:
`agricultura`, `arroz`, `trigo`, `carroça` — zero ocorrências. `colheita` só aparece com o
sentido de colher recursos de cultivo.

**L4 — Só três das cinco paredes regionais estavam nomeadas; a obra nomeia as cinco.**
`severidade: alta` — **erro factual, já corrigido.**
`04 - As Cinco Regiões` afirmava "Três das cinco paredes são nomeadas na obra". Falso: cap. 1043
lista as cinco de uma vez (miasma / licorice / raging flame / blue water / saint), e cap. 1044
confirma a de miasma no mundo real (não só na imitação). Faltavam também **as cores** e **o
interior** de cada parede, que a obra descreve com riqueza (cap. 710).

### 🟠 SÉRIAS

**L10 — A nota de Cosmologia tratava a maré de qi como desastre periódico e antigo.**
`severidade: alta` — **erro conceitual, corrigido.**
A nota dizia, no bloco "Para o design": "como é periódico, dá ritmo de campanha: o mundo inteiro
sabe que a próxima maré vem". Duas coisas erradas nisso. Primeira: **a expressão "qi tide" não
aparece uma única vez nos Volumes 1 a 5** — ela nasce no Volume 6, no exato momento em que as
cinco regiões se fundem e as paredes caem (caps. 1968, 1970). Numa campanha ambientada **antes**
da Grande Era o fenômeno não existe e ninguém ouviu falar dele. Segunda: a obra afirma
explicitamente o contrário de periodicidade — "é impossível calcular quanto tempo este fenômeno de
maré de qi vai durar, ou se vai ficar mais forte ou mais fraco; não conseguimos nem prever uma
tendência" (cap. 1968). O erro faria a designer construir um calendário de campanha em cima de um
fenômeno que a obra descreve como imprevisível por natureza.

**L11 — Faltava o efeito mecânico da maré de qi sobre cultivadores, que é assimétrico e jogável.**
`severidade: média` — **corrigido.** A maré força **todo Gu Imortal das cinco regiões** a parar e
se recuperar, e **quanto mais forte a fundação da dimensão interna, mais tempo de recuperação** —
enquanto quem vem dos dois céus e a instituição suserana não sofrem o efeito (cap. 1968). É uma
janela em que os fortes do mundo de baixo ficam imobilizados e os de fora ficam livres.

**L12 — Navegação e viagem por água não existiam em nota nenhuma.** `severidade: média` —
**corrigido** (era L7). O achado mais valioso: o Mar Oriental tem uma **rede de estradas expressas
submarinas**. Uma corrente submarina é "como um dragão ou píton sem forma" que abre um túnel de
água no fundo do mar, e quem a pega viaja mais rápido que os golpes imortais comuns de movimento;
super forças mantêm **caravanas submarinas** que percorrem dez mil a cem mil li em pouco tempo
para comerciar; existe um tipo de **mapa precioso que registra só as correntes**, nem as ilhas nem
a superfície; e ele **perde a validade**, porque as correntes mudam de traçado o tempo todo
(cap. 894, e cap. 114976 do Vol. 5). Nada disso estava no vault.

**L13 — Este mundo não tem ponte nem balsa, e ninguém tinha registrado isso.** `severidade: média`
— **corrigido.** Varredura dedicada: não há travessia de rio por ponte de madeira ou pedra usada
por população comum, e "balsa/barqueiro" não aparece em nenhum volume. As pontes que existem são
decorativas ou mágicas (ponte de ouro, de arco-íris, de jade, criadas na hora por um cultivador).
É um silêncio consistente com o cenário, e vale mais dito do que omitido: atravessar um rio é
problema real para quem não tem poder.

**L14 — O subsolo, que é a fonte do dinheiro do mundo, não tinha nota.** `severidade: alta` —
**corrigido com nota nova.** A cadeia inteira estava dispersa: a caverna subterrânea é o motivo
pelo qual um clã se instalou naquela montanha (cap. 4), abriga a nascente, o cofre de Gu de
reserva e o ritual de despertar (caps. 1, 156, 158), e é área proibida. Faltava também **quem
minera neste mundo** — e a resposta é surpreendente: os *rockmen*, humanos variantes que comem
minério, dormem enrolados em bola por sete ou oito anos, vivem mil anos, têm metal crescendo no
corpo e pagam tributo em minério **a cada dez anos** a quem controla o território, sendo tratados
explicitamente como escravos (caps. 409, 412, 414, 423).

**L15 — A nota de Cosmologia tratava as Trincheiras Terrestres como fenômeno da Grande Era.**
`severidade: média` — **corrigido.** Cap. 931 (Volume 4, muito antes da Grande Era): "não só as
Planícies do Norte tinham uma Trincheira Terrestre — na verdade, **as cinco regiões todas
tinham**". São acidentes geográficos antigos e permanentes, com dono, e a do norte é a grande área
de recursos da região mais pobre das cinco. O que a Grande Era faz é abrir trincheiras **novas**.

**L16 — A seção "As veias do mundo" era um parágrafo de três linhas para o sistema técnico mais
reaproveitável do domínio.** `severidade: alta` — **corrigido.** Faltava praticamente tudo: que
"veia" é uma **categoria genérica** (a obra cita veia de fogo, veia de água, além das três); que as
veias de terra expelem magma a cada cem anos e remodelam o terreno (cap. 1155); que **acumulam as
emoções negativas de uma região e podem gerar feras a partir delas** (cap. 1301); que a Fronteira
Sul treme primeiro porque tem a veia mais profunda, por ter mais marcas de dao do caminho da terra,
e por isso é a mais devastada **e** a mais recompensada, com o Mar Oriental no extremo oposto
(cap. 1408); que existem **nós** de veia de céu e que um mundo privado assentado sobre um deles
produz mais recursos (cap. 2001); e que as veias humanas se formam onde a humanidade se aglomera e
**explicam por que certos lugares produzem gênios**, com a maior cidade mortal do mundo sempre
voltando a se assentar sobre o traçado da sua (caps. 1931, 1947).

**L17 — O que o sol realmente é: o segredo cosmológico melhor guardado do domínio, e ele estava
fora do vault.** `severidade: alta` — **corrigido.** Cap. 2277: "o sol é uma congregação de marcas
de dao do caminho do céu, do caminho da luz e do caminho do fogo; é tangível, mas não sólido. Pode
ser visto como **uma tribulação que vem acontecendo há incontáveis anos**, e que começou a se
acumular desde o início do mundo". E é o **maior nó de veia de céu do mundo inteiro**. E pode ser
destruído — um Venerável destruiu o sol de propósito para acelerar a fusão dos dois céus
(cap. 2333).

**L9 — O Atlas afirmava que a Fronteira Sul não tem estações do ano.** `severidade: média` —
**corrigido.** A obra descreve estação chuvosa e inverno na região e mostra os dois produzindo
materiais de refino diferentes no mesmo lugar (cap. 2098). O silêncio real é mais estreito: não há
calendário agrícola.

**L5 — Ninguém explica que as paredes regionais se tocam.** `severidade: média`
Cap. 710: saindo da parede santa entra-se direto na parede alcaçuz. Cap. 1045: da parede de
miasma direto para a de água azul. Cap. 1211 idem. Consequência que muda o mapa: **não existe
terra de ninguém entre duas regiões**, e toda travessia é a travessia de *duas* membranas
seguidas. As notas descreviam a parede como se fosse uma só.

**L6 — A parede regional tem espessura medida em passos, se regenera enquanto se cava, e tem
pontos fracos localizáveis por adivinhação.** `severidade: média` — cap. 710. As notas tinham a
regeneração, mas não a unidade de medida (76 passos abertos por um golpe imortal; +3.000 passos
até um ponto fraco) nem o fato de que **um adivinho consegue calcular onde a parede é fina** —
o que é uma profissão e um item de mercado inteiros.

**L7 — Navegação e viagem por água não existem em nota nenhuma.** `severidade: média`
`06 - Escala, Distâncias e Viagem` tem a escada de mobilidade terrestre e aérea completa, e
nenhuma linha sobre barco. A obra tem: jangada de bambu com vela descendo rio, cinco dias de
viagem, encalhe em recifes (cap. 200); navios mercantes de clã atacados por bandidos (cap. 998);
vilas de pescadores em ilhas do Mar Oriental (cap. 894); elefantes-d'água usados como
embarcação (cap. 1297). E o Mar Oriental tem "milhões, ou dezenas de milhões" de ilhas, quase
todas desabitadas (cap. 894).

**L8 — "Zona proibida" é um conceito operacional do mundo com cinco sentidos distintos, e não
está em lugar nenhum.** `severidade: média`
A obra usa `forbidden zone / area / land` 65 vezes, em cinco acepções que uma mestra precisa
distinguir: (a) a área proibida institucional de um clã, onde nem o líder pode entrar
(caps. 178, 962); (b) a zona ecologicamente letal, cujo núcleo mata (caps. 429, 433); (c) o
cordão político de mil li em volta de um achado, com ordem de matar (cap. 908); (d) a zona
proibida **fabricada** por um Gu, que se expande sozinha e enche o lugar de intenção assassina
(caps. 958-961); (e) o interdito cósmico — Rio do Tempo, Porta da Vida e da Morte, Ordinary
Abyss — "a forbidden area in the great dao" (caps. 196, 384, 401).

## O que foi corrigido

### `13 - Cosmologia.md`
- **Acrescentada a seção "Sim, existe um sol — e os céus são filtros"** (L2), que resolve a
  ambiguidade mais perigosa do domínio: o mundo tem sol, lua e estrelas comuns, e os dois céus são
  **filtros** por cima deles — a luz atravessa o céu branco (dia) e não atravessa o negro (noite),
  porque a luz de hoje é um resíduo enfraquecido da luz imemorial, que atravessava os nove.
- **Acrescentado** o corolário econômico: com sete céus caídos, os trovões dos dois restantes quase
  nunca se chocam, e a pedra de refino que nascia desse choque praticamente deixou de ser produzida
  — uma catástrofe de milhões de anos atrás que ainda se manifesta como escassez de mercado.
- `fontes` atualizado com caps. 21, 34, 73, 559, 1028.

### `13 - Cosmologia.md` (segunda rodada)
- **Corrigido L10**: acrescentado um `[!warning]` dizendo que **antes da Grande Era não existe maré
  de qi nenhuma**, e que depois que ela começa ninguém consegue prever periodicidade, duração nem
  tendência. O bloco "Para o design" foi reescrito para usar a maré como acaso permanente em vez de
  calendário, e a tabela de corte da nota agora avisa que a linha só vale para campanhas
  ambientadas depois da Grande Era.
- **Acrescentado L11**: o bloco "O que a maré faz com quem cultiva", com a assimetria completa
  (morte de vida, dano em núcleo de alma, tremor forçando recuperação, penalidade invertida por
  fundação, e a imunidade de quem não é das cinco regiões) e a leitura de design de que, pela
  primeira vez, ser pequeno é vantagem.
- `fontes` atualizado com caps. 1970, 1972, 1992.

### `01 - Visão Geral do Mundo.md`
- **Corrigido o risco de leitura de L2**: a linha "existem dois céus que se alternam como dia e
  noite" agora diz explicitamente que isso **não** substitui o sol, e aponta para a seção nova de
  Cosmologia e para `16 - O Relógio do Mundo`.
- Tabela "Mapa da pasta" e sugestão de ordem de leitura atualizadas com as três notas novas.

### `04 - As Cinco Regiões.md`
- **Corrigido erro factual** (L4): a frase "Três das cinco paredes são nomeadas na obra" foi
  substituída por uma **tabela das cinco paredes** com nome em português e inglês, cor vista de
  fora e descrição do interior — com `—` explícito nas três que a obra não descreve por dentro.
- **Acrescentado** (L5): as três consequências de mapa — a parede é uma casca que envolve a
  região inteira; as paredes se tocam, logo toda travessia é de duas paredes seguidas; e nada
  vive dentro da parede, ela é o obstáculo inteiro.
- **Acrescentado** (L6): a espessura medida em passos, a regeneração durante a escavação e os
  pontos fracos localizáveis por dedução.
- **Acrescentado um `[!example]`** com o dado mais vívido que a obra dá sobre travessia: um grupo
  que foi do Mar Oriental às Planícies do Norte atravessou **duas paredes** e perdeu **quatro
  imortais de rank 7 mortos dentro delas**, com os três de rank 8 gravemente feridos — enquanto o
  de cultivo mais baixo do grupo passou com facilidade (cap. 928). É a ilustração canônica da
  regra "o mundo é permeável para os fracos e sólido para os fortes".
- `fontes` do frontmatter atualizado com caps. 1044, 1045, 1211, 1258.

### `13 - Cosmologia.md` (terceira rodada)
- **Reescrita a seção "As veias do mundo"** (L16), que passou de três linhas a três subseções
  completas: veias de terra (as cinco funções, a caixa explicando por que a Fronteira Sul treme
  primeiro e ganha mais), veias de céu (os nós, o mundo privado que rende mais pelo endereço, o
  fruto anômalo da fusão e a solução de **mudar a propriedade de lugar**, e a destruição de nó como
  ato de guerra) e veias humanas (por que certos lugares produzem gênios, e a cidade que sempre
  volta a se assentar sobre a veia).
- **Acrescentada a subseção `conhecimento: segredo` "O que o sol realmente é"** (L17): o sol como
  acúmulo de marcas de dao, como tribulação permanente em curso desde o início do mundo, como maior
  nó de veia de céu, e como alvo destrutível.
- **Corrigido L15**: a seção das Earth Trenches agora separa as **cinco trincheiras antigas**, uma
  por região, que já existem e têm dono, das trincheiras **novas** que a Grande Era abre.
- `fontes` atualizado com caps. 1155, 1301, 1408, 1531, 2001, 2140, 2267, 2277, 2278, 2333.

### `06 - Escala, Distâncias e Viagem.md`
- **Acrescentada a seção "Pela água"** (L12 e L13), que a nota não tinha: a jangada de bambu e a
  descida de rio; o `[!warning]` sobre a **ausência de pontes e balsas** no mundo; a frase-régua do
  mar ("para os Mestres Gu o mar era muito profundo; para os Gu Imortais a água ainda era muito
  rasa"); o mergulho como trabalho de mortal e as duas regras dele (a superfície engana; luz
  atrai); a **rede de correntes submarinas** com as caravanas de fundo de mar, o mapa exclusivo de
  correntes e a validade que ele perde; as casas-fortaleza imortais em forma de navio; e o
  elefante-d'água como embarcação viva, com a escala de poder codificada no número de andares.
- Três regras do mundo novas acrescentadas à lista enumerada (15 a 17).
- `fontes` atualizado com caps. 201, 1228, 1652-1656.

### `05 - Atlas das Cinco Regiões.md`
- **Preenchida uma lacuna que o próprio atlas declarava** (L9, abaixo): o bloco de clima da
  Fronteira Sul dizia que a região não tem estações. Ela tem — a obra registra **estação chuvosa e
  inverno distintos** (cap. 2098), e registra a neblina como estado permanente, não evento. O que
  de fato falta é o **calendário agrícola** (meses de plantio e colheita), e a lista de silêncios do
  fim da nota foi corrigida para dizer isso em vez de negar as estações.
- **Acrescentado um `[!example]`** com o caso mais concreto de estação mudando recurso: uma montanha
  de lama do sul que produz um material de refino na estação chuvosa e outro no inverno.
- `fontes` atualizado com cap. 2098.

## Notas novas criadas

> As três notas nasceram com prefixo provisório continuando o maior da pasta (`16`, `17`, `18`).
> **A posição de leitura correta é outra** — indicada abaixo. O orquestrador deve rodar
> `_pipeline/numerar-notas.py` com a ordem nova para renumerar e reescrever os wikilinks.

### `16 - O Relógio do Mundo.md` — resolve L1 e L2
Posição de leitura sugerida: **logo depois do Atlas e antes de "Escala, Distâncias e Viagem"**
(posição 6 na ordem nova). O Atlas diz onde o grupo está; esta nota diz quando e com que tempo.
Cobre: o céu ordinário (sol, lua, estrelas, fases) e a costura com os dois céus; o calendário
(meses, data corrente, calendário regional, ausência de ano numerado, eras com nome de Venerável,
Ano Novo e a idade coletiva, calendário institucional de meio e fim de ano); as três escalas de
duração (hora / sopro / vareta de incenso) e o vigia noturno como relógio público; dia e noite
(perigo por falta de luz, Gu de visão noturna, "de dia se luta, de noite se conspira"); as quatro
estações, o clima regional permanente, o zoneamento vertical de montanha e a estação mudando o que
o terreno produz; quem controla o clima; e a regra de tom mais forte do achado — **quase todo
desastre deste mundo tem culpado**.

### `17 - As Plantas e os Bichos Comuns.md` — resolve L3
Posição de leitura sugerida: **imediatamente antes de "Bestas Gu e Reis Fera"** (posição 8 na
ordem nova). É a metade não-mágica da natureza, e prepara a metade mágica.
Cobre: a regra "bicho não é Gu" com a citação decisiva; o aviso de que muita "erva" da obra é um Gu;
plantas comuns nomeadas e a grama-zarabatana como planta-que-vira-dinheiro-e-gera-Gu; a escada de
grau das plantas `(ded.)` e as três plantas de topo (árvore-bruma-das-mil-serpentes, Árvore dos Mil
Desejos, girassóis-de-rosto-fantasma); agricultura real e a **regra social** de que plantar é
trabalho de mortal de fora; os Gu de rank 1 que produzem comida e por que isso explica a estrutura
social; fauna comum e comportamento animal utilizável como regra de rastreamento; a tabela de
montarias; rebanho, couro e a especialização de criação por terreno; e a regra de que **todo ser
vivo precisa comer, imortais inclusive**.

### `18 - O Selvagem, as Ruínas e as Zonas Proibidas.md` — resolve L8 e o item "seguro × selvagem"
Posição de leitura sugerida: **imediatamente depois de "Bestas Gu e Reis Fera"** (posição 10 na
ordem nova). Fecha o movimento "o que existe fora dos muros".
Cobre: o selvagem como padrão do mapa e o assentamento como exceção; a régua **rank 3 para sair,
rank 4 para andar sozinho**, com a tabela de classes de mobilidade; a estrada como lugar; a
fronteira do seguro que recua durante uma maré de bestas; a ausência de cartografia pública e os
códigos idiossincráticos dos mapas de caçador; **os cinco sentidos de zona proibida**
(institucional, ecológica, política, fabricada, cósmica) com exemplo mecânico de cada; e a seção
sobre por que uma ruína continua perigosa — o qi de rancor como substância interrogável, o acúmulo
de morte atraindo raios, a ruína que gera população própria, e batalhas imortais que apagam
acidentes geográficos deixando os nomes órfãos.

### `19 - O Subsolo.md` — resolve L14
Posição de leitura sugerida: **imediatamente depois do Atlas** (posição 6 na ordem nova). O Atlas
descreve a superfície; esta nota vira o mapa de cabeça para baixo.
Cobre: a caverna como motivo da vila, com as quatro funções sobrepostas (fundação econômica,
santuário do ritual de despertar, cofre de Gu e lavoura protegida) e o interior descrito
literalmente pela obra — estalactites coloridas, rio subterrâneo de nove metros, mar de flores; a
geologia do dinheiro (a pedra é cristalização da energia da nascente, não minério), com as três
regras que decorrem disso e o segredo de que **a moeda imortal não tem nascente equivalente**; os
homens de pedra como o povo minerador do mundo, com o retrato completo e a relação de tributo e
servidão; o que sai do chão, com nomes; o Abismo da Terra e as Trincheiras Terrestres como duas
formações distintas, incluindo a trincheira submarina; os perigos do subsolo (com o registro de que
**falta de ar não é um deles**); e o que se constrói lá embaixo, incluindo a prisão falsa montada
na frente da verdadeira como isca.

### Ordem de leitura completa proposta para a pasta

1. Visão Geral do Mundo · 2. A Filosofia do Mundo · 3. As Duas Eras de um Mestre Gu ·
4. As Cinco Regiões · 5. Atlas das Cinco Regiões · **6. O Subsolo** · **7. O Relógio do Mundo** ·
8. Escala, Distâncias e Viagem · **9. As Plantas e os Bichos Comuns** · 10. Bestas Gu e Reis Fera ·
**11. O Selvagem, as Ruínas e as Zonas Proibidas** · 12. Lendas de Ren Zu ·
13. Blessed Lands e Grotto-Heavens · 14. Viver Dentro da Abertura Imortal · 15. Vontade dos Céus ·
16. Fate Gu · 17. Cosmologia · 18. Lugares Fora das Cinco Regiões · 19. Tribunal Celestial.

Os quatro arquivos novos estão no disco como `16`, `17`, `18` e `19` (continuando o maior número
da pasta, como pedido). A renumeração para a ordem acima é trabalho do
`_pipeline/numerar-notas.py`.

`01 - Visão Geral do Mundo.md` **já foi atualizada** com as três notas novas na tabela "Mapa da
pasta" e no texto da sugestão de ordem de leitura, usando os nomes de arquivo atuais.

## Decisões tomadas

**D1 — Corrigir a nota 04 em vez de criar uma nota "Paredes Regionais".** O material novo sobre
as paredes é grande, mas é o assunto declarado da nota 04, que já tem a escada de conhecimento
em três degraus e as regras de travessia. Alternativa descartada: nota própria — separaria a
parede da região que ela envolve e obrigaria a duplicar a escada de conhecimento.

## Grandes eventos que encontrei

*(lista para os agentes de `08 - Eventos e Cenarios/`. Não escrevi nota de nenhum deles — só
registro que existem e onde está a evidência. Vários já aparecem como pano de fundo em notas de
`04 - Mundo/`, o que significa que a pasta 08 deve tratá-los como **cenário jogável**, não repetir
a descrição de mundo.)*

**Ciclos com data marcada (os melhores para virar estrutura de campanha):**

- **A maré de bestas / calamidade de bestas** — trienal no caso mais documentado, com quatro fases
  sazonais legíveis; a calamidade é a escala secular acima. Já descrita como mecânica em
  `07 - Bestas Gu e Reis Fera`.
- **A grande nevasca decenal das Planícies do Norte** — dura meses, mata em massa, seca as
  nascentes de toda a região e é seguida do melhor período de crescimento. Segredo: não é
  meteorologia. Já descrita em `04 - As Cinco Regiões` e no Atlas.
- **A maré de terra anual do Mar Oriental** — abre a única porta regular do mundo, e as rotas de
  travessia são um ativo comercial perecível. Já descrita no Atlas.
- **A erupção centenária da grande cratera do Deserto Ocidental** — redesenha o terreno em volta.
- **A dispersão anual da névoa da montanha número um** (Continente Central) — dispara uma
  peregrinação continental de reivindicação e instalação de heranças.
- **A convenção do caminho de refino** — a cada cem anos, com inscrições por todo o continente.
- **A frutificação da Árvore dos Mil Desejos** (Deserto Ocidental) — ciclo de 300/600/900 anos,
  exatamente mil frutos, exige chegar com uma receita de Gu em mãos; já causou guerras entre
  facções imortais. Descrita em `17 - As Plantas e os Bichos Comuns`. **Excelente candidata a
  cenário.**
- **A submersão sazonal de ilhas-mercado no Mar Oriental** — o mercado abre e fecha com a maré.
- **A disputa decenal pelo trono** nas Planícies do Norte (já em `06 - Economia e Vida`).

**Eventos estruturais únicos:**

- **A Grande Era** — as veias de terra se fundem, as paredes regionais caem, as cinco regiões viram
  uma só, e as diferenças de qi congeladas viram marés de qi que varrem o mundo. É o evento que
  divide o cenário em "antes" e "depois". Ver `04 - As Cinco Regiões` e `13 - Cosmologia`.
- **A queda dos sete céus imemoriais** — origem dos mundos fragmentados e da escassez permanente de
  vários materiais.
- **A ruptura da fronteira do mundo, há ~300 mil anos** — quatro Veneráveis remendaram; o remendo
  nunca ficou completo. `conhecimento: segredo` de nível máximo.
- **A "batalha dos cem dias"** — um vale desaparece do mapa e vira lugar de visitação (cap. 953).
- **O massacre de Mu Bei mountain** — um clã inteiro chacinado e convertido em zumbis, com lápide
  gigante erguida sobre as ruínas; sacudiu a Fronteira Sul inteira e deixou a montanha com nome
  novo e população hostil permanente (cap. 253). É o **modelo canônico de ruína amaldiçoada**, e
  está descrito como mecânica em `18 - O Selvagem, as Ruínas e as Zonas Proibidas`.
- **A queda de um fragmento de gruta-céu num vale** (cap. 908) — dez grandes seitas cercam mil li e
  matam quem entrar. Modelo de "corrida ao ouro com cordão militar".
- **A fome histórica da capital** (cap. 1992) — citada de passagem, sem causa nem frequência.
  `—` Espaço grande e limpo para a pasta 08 preencher.

## O que a obra realmente não diz

Levantamento de silêncios **verificados por varredura do texto-fonte**, não por ausência em fonte
secundária. Todos foram registrados dentro das notas com `—` ou em callout `[!question]`, para que
a designer saiba que pode preencher sem contradizer nada.

**Tempo e céu**
- Não há conversão numérica de "tempo de um sopro", "vareta de incenso" ou "quarto de hora" para
  segundos/minutos. Só dá para calibrar por comparação relativa.
- Não existe datação por ano numerado. Nenhum "ano 3.412", nenhum calendário imperial, nenhuma
  contagem desde uma fundação. Só eras com nome de Venerável.
- Não existe relógio de nenhum tipo — nem de água, nem de sol, nem ampulheta. E a obra também não
  usa o sistema chinês de doze duplas-horas.
- **Não existem eclipses**, em nenhum dos seis volumes.
- A fase da lua real não tem nenhum efeito mecânico conhecido sobre cultivo. A única ligação
  registrada é folclórica: lobos uivam na lua cheia.
- Não há nenhuma afirmação de que a noite favoreça o cultivo. O perigo noturno é explicado por
  falta de luz, e nada mais.
- Não há duração numérica da noite nem do dia.

**Clima e desastre**
- O Continente Central é o maior silêncio meteorológico da obra: sem estações, monções, secas ou
  desastre sazonal próprio.
- O Deserto Ocidental não tem estações agrícolas nem calendário sazonal formal.
- **Quase não existe desastre natural espontâneo.** Terremoto, tsunami, tempestade de areia,
  enchente e epidemia aparecem quase sempre ou como comparação literária, ou com causa mágica
  identificável. A obra nunca *nega* que existam desastres naturais puros; simplesmente quase nunca
  narra um.
- Não há **nenhuma epidemia natural** em nenhum volume. Toda "praga" nomeada é arma de cultivador.
- A fome histórica é citada uma vez, sem causa, frequência ou resposta social.
- Não há protocolo descrito de proteção contra desastre puro (dique, abrigo, celeiro público).

**Natureza**
- A obra nunca enuncia num parágrafo só a escada de grau das **plantas**, como faz com as feras —
  a escada é dedução por vocabulário.
- A obra **nunca usa o verbo "domesticar"**. Fala em criar, escravizar e manter fazenda.
- Não existem os termos "herbalista", "farmácia", "jardim de ervas" nem "planta carnívora".
- A fronteira entre "planta cultivada comum" e "planta que é um Gu" nem sempre é explicitada: várias
  flores listadas como material de refino não recebem classificação.

**Geografia e travessia**
- A obra não descreve o interior das paredes regionais de miasma, de chama ardente e de água azul —
  só o das de santa e de alcaçuz.
- A cadência exata e a duração da maré de terra do Mar Oriental nunca são dadas.
- Não existe sistema de marés comuns com ciclo lunar; a maré aparece só como pano de fundo.
- Não há lista de ruínas famosas do mundo, nem escala de "níveis de assombração", nem prazo de
  dissipação natural do qi de rancor. O que existe é o mecanismo.
- Não existe cartografia pública de nenhuma região, e a obra faz disso uma propriedade do cenário:
  **sempre existe mais mundo do que mapa**.
