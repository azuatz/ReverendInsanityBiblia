---
tags:
  - pipeline/revisao
  - path
aliases:
  - Revisão leiga da pasta 03 - Paths
status: concluido
---

# Revisão de leitora leiga — `03 - Paths`

**O papel assumido:** uma designer de RPG competente que **nunca leu Reverend Insanity** e não
vai ler. Tudo que ela sabe do mundo vem destas 29 notas. Foram lidas do começo ao fim, na ordem
da pasta.

**Classificação usada:**

- **Bloqueador** — torna a nota inutilizável ou enganosa: número que contradiz a
  [[02 - Tabelas de Referência Rápida|tabela soberana]], afirmação que contradiz outra nota do
  vault, contagem que não fecha, promessa não cumprida, invenção nossa apresentada como cânone.
- **Sério** — faz entender errado ou perder tempo.
- **Menor** — repetição, frase confusa, link apontando para o lugar menos útil.

**Auditoria de links ao fim do trabalho:** `python3 _pipeline/auditar-links.py` →
216 notas, 4.813 links por nome exato, **zero quebrados**, zero dependentes de alias.

---

## Veredito de conjunto

**Sim: a pasta ensina os caminhos a quem nunca leu a obra.** É o material mais maduro que já
passou por esta revisão. Três coisas sustentam isso e valem ser ditas com nome e sobrenome:

1. **O gabarito da pasta está cumprido em 27 de 27 notas de caminho.** Todas terminam com
   `> [!note] Para o design` abrindo em **"Arquétipo entregue: …"**, e todas têm
   `## A camada escondida`. As duas notas estruturais (`01` e `02`) não têm arquétipo, e não
   deviam mesmo ter.
2. **A camada escondida é explicada, não anunciada.** Fui atrás de seções que só prometessem
   mistério e não achei nenhuma. As doze notas escritas hoje entregam mecanismo com custo e
   consequência de mesa: a parede das cem almas e a alma que muda de espécie
   (`12 - Soul Path`), a estrela que precisa ser refinada uma a uma e pode ser destruída pelo
   inimigo (`19 - Star Path`), o corte que vira propriedade permanente do terreno
   (`11 - Sword Path`), a marca de pintura que **reveste** em vez de disputar
   (`28 - Painting Path`), a coleira institucional embutida no caminho da liberdade
   (`24 - Human Path`), o "empobrecer é um método" de `25 - Heaven Path`.
3. **A honestidade sobre lacunas é o traço mais forte do conjunto.** `09 - Formation Path`
   registra que a camada escondida dele é **uma ausência** — "não existem marcas do Dao de
   formação", verificado por busca direta — e transforma isso na melhor definição do caminho na
   pasta ("uma gramática, não um vocabulário"). `28 - Painting Path` publica uma tabela de Gu
   **vazia** e explica que a tabela vazia é a consequência do segredo, não falha de pesquisa.
   `22 - Phantom Path` registra uma divergência de datação que a obra não resolve, em vez de
   escolher.

**As notas coletivas não viraram depósito.** `27 - Os Caminhos Elementais` dá verbete próprio a
cada caminho e **declara o tamanho da evidência de cada um** — o verbete da nuvem chega a abrir
um callout dizendo "este é o verbete mais pobre dos onze, e vale dizer com todas as letras".
`29 - Os Demais Caminhos` faz o mesmo e enuncia a regra na abertura: "um verbete curto não é uma
nota malfeita: é a medida exata do que existe". O caminho do selo tem três linhas, e as três
linhas estão certas.

**A regra do não-ciclo estava bem fechada em `27`** — com a verificação no texto-fonte, com o
mecanismo substituto (densidade recíproca) e com as duas exceções que a obra realmente autoriza.
O que faltava era a porta da frente: quem abre a pasta pela nota `01` não encontrava o aviso.
Corrigido (ver abaixo).

---

## Achados por nota

### `01 - Visão Geral dos Paths`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 1 | **Bloqueador** | A escala de *attainment* estava em **oito degraus**, com um callout afirmando que "não existe um degrau de quase-mestre" e chamando a versão de nove degraus de "erro nosso". Isso contradizia a tabela soberana (seção 10, nove degraus), a nota `08 - Attainment` (nove degraus) e o próprio texto-fonte, onde a lista aparece completa e o termo *quasi-master* ocorre 17 vezes. Contradizia ainda `08 - Refinement Path` e `09 - Formation Path`, que já usavam "Quase-mestre" nas próprias tabelas. Pior: o parágrafo seguinte falava em "os quatro 'quase'" e a lista trazia só três — a nota se contradizia sozinha. | **Corrigido.** Escala refeita em nove degraus, callout reescrito para explicar o erro na direção certa, e a linha de *Relações* ("os oito degraus") acertada. |
| 2 | **Bloqueador** | Penalidade territorial de caminho menor dada como **20–39%** em dois lugares. A tabela soberana e a citação literal em `13 - Sound Path` dizem **20–30%**. | **Corrigido** nos dois lugares. |
| 3 | Sério | "vinte e cinco caminhos com nota própria, mais duas notas coletivas que cobrem outros **vinte e cinco**" — a conta real das coletivas é 11 + 13 = 24, e nenhuma das duas contagens era verificável pela leitora. | **Corrigido** para "mais de vinte", que é verdadeiro e não convida à conferência. |
| 4 | Sério | O mapa da pasta anunciava "**doze** caminhos naturais" em `27`. São **onze** (ver o achado de `27`). | **Corrigido.** |
| 5 | Sério | A **regra do não-ciclo** — o erro que um designer comete por hábito de gênero — só aparecia numa nota de rodapé no fim da nota-porta. Quem lê as "Regras do mundo" e vai direto praticar não era avisado. | **Corrigido.** Acrescentada como **regra 14**, com o mecanismo substituto (densidade recíproca), os dois pares que a obra realmente autoriza (fogo × madeira, água × fogo) e o link para `27`. As regras 1–13 não foram renumeradas, porque outras notas referenciam "a regra 9" e "a regra 11" por número. |

**O que está bom:** a seção *Como nasce um caminho* é a melhor página conceitual da pasta — a
distinção entre "existir de fato" e "existir de direito" é o que faz `26 - Dream Path` e o
caminho da matança fazerem sentido. O quadro **criador × Dao Lord** e o aviso de que
"pseudo-Venerável não é um degrau, é um rótulo de fracasso" evitam dois erros que a leitora
cometeria sozinha. A legenda **"Como ler as tabelas de Gu representativos"**, centralizada aqui e
citada por todas as outras notas, é uma decisão de arquitetura acertada: a diferença entre `—`
("você decide") e `X (máximo)` ("está decidido") é exatamente o que uma designer precisa saber.

### `02 - Como se Escolhe um Caminho`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 6 | Menor | Lista de "quatro alavancas de rendimento" quebrada ao meio por uma linha em branco — em Obsidian, isso parte a lista em duas e o terceiro item perde a numeração visual. | **Corrigido.** |

**O que está bom:** esta é a melhor nota da pasta e uma das melhores do vault. Ela resolve o
problema pedagógico mais difícil do material — a leitora chega perguntando "quando escolho minha
classe?" e a nota responde invertendo a pergunta, com a frase que fecha tudo: *"Você não escolhe
seu caminho. Você o rega."* A seção **"De onde vêm as marcas de cada caminho"** é a única do
vault que explica o vetor de marcas como **autobiografia auditável** do personagem, e o
"você monta o menu, o adversário faz o pedido" é a formulação mais jogável do material inteiro.
O bloco `> [!important] Como esta nota está marcada` declara explicitamente que **não há nenhum
`*` na nota** — e a varredura confirma. Nada a mexer no corpo.

### `03 - Blood Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 7 | **Bloqueador** | A nota dizia que o Venerável do sangue cultivava "**sangue como principal, sorte como especialidade**". `01 - Visão Geral dos Paths` e `23 - Luck Path` dizem o inverso (sorte principal, sangue especialidade). Conferido no texto-fonte: a obra registra as duas coisas — ele **planejou** sangue como principal, mas o caminho do sangue foi barrado pelo mundo, e a lista canônica dos pares dos dez o registra com sorte na frente. | **Corrigido em três lugares** (camada escondida, sinergias, praticantes notáveis), preservando a nuance em vez de escolher um lado: é o único dos dez cujo par saiu diferente do planejado, e a razão é política. |

**O que está bom:** o enquadramento social é exemplar para uma leitora leiga — a nota não se
contenta com "é o caminho mais odiado", ela **explica o termo de comparação** ("pior que queimar
almas") e, num callout, marca honestamente que o enquadramento é reconstrução nossa. A camada
escondida entrega três mecanismos completos (marcas que blindam e se gastam; a separação do
corpo com custo em marcas; o feto de sangue que cultiva sozinho por trezentos anos) e a inversão
de tom no fim — o caminho mais imundo do mundo é, no topo, o melhor curandeiro — é o tipo de
achado que justifica a seção existir.

### `04 - Strength Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 8 | Menor | O título do item dizia "força fundida com **escravização**" e o texto abaixo explicava um núcleo do **caminho da alma**. A leitora fica sem saber qual é. | **Corrigido:** o golpe funde os três, e o título agora diz isso. |

**O que está bom:** a **mecânica das duas camadas** (quanta força você tem × quanto dela
consegue sair) é o melhor achado de design da pasta, e a nota o entrega com o dado que o torna
jogável — "às vezes nem dez por cento". O bestiário de fantasmas como **biografia do personagem
em forma de estatística** é ouro, e a escalada dentro da própria cena (um fantasma → oito
conforme o lutador apanha) é uma curva de tensão embutida na ficha. O callout do **Puxar Água**
ensina duas regras gerais do sistema de uma vez, e a segunda — "o domínio que destranca a receita
é o do caminho *secundário*" — é contraintuitiva e valiosa.

### `05 - Qi Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 9 | Sério | A camada escondida anunciava "**quatro** coisas" e entregava seis subseções. | **Corrigido** para seis, com a lista completa. |
| 10 | Sério | Duas seções repetidas quase palavra por palavra entre *A camada escondida* e *Mecânicas típicas*: a regra do material-no-lugar-de-Gu e o efeito do milhão de marcas sobre a abertura. A leitora lê a mesma coisa duas vezes e desconfia de que perdeu alguma diferença. | **Corrigido:** as versões de *Mecânicas típicas* viraram ponteiros curtos, preservando o que só elas tinham (a inversão econômica "arsenal por consumível" e os três números de amplificação). |
| 11 | Sério | A tabela de Gu estava **inteiramente em inglês** (*Heaven Qi*, *Big Family Qi*, *Atmosphere Gu*…) enquanto todas as outras 26 notas usam nomes em português. Para quem não lê a obra, isso quebra a leitura no meio. | **Corrigido:** tabela traduzida, com "Qi de Força" batendo com o nome já usado em `04 - Strength Path`. |
| 12 | Menor | O nome do Venerável aparecia em inglês sem explicação. `25 - Heaven Path` tem um callout explicando a política; esta nota não tinha. | **Corrigido** com nota de rodapé remetendo à mesma política. |

**O que está bom:** este é o melhor **estudo de caso de ciclo de vida de escola de magia** que a
obra oferece, e a nota o monta inteiro: nasce como arma política de um grupo oprimido, domina
80% do mundo, morre por falta de insumo (não por derrota), vira nota de rodapé e ressuscita por
um evento geológico. A seção *A economia de um caminho morto* — os Gu baratos e invendáveis, as
receitas caríssimas, "o estoque global cabe numa compra" — é material de campanha direto.

### `06 - Transformation Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 13 | Menor | A tabela trazia "Mudar Forma ⭐ \| **6 (já foi 9)**" sem explicação. A legenda de níveis não cobre esse formato, e a leitora não tem como saber o que aconteceu. | **Corrigido** com a história completa (foi destruído e refeito dezenas de vezes; houve um exemplar de nível 9, destruído com o dono; desde então o mundo recomeça do 6), conferida contra `05 - Catálogo de Gu - Imortais`. |

**O que está bom:** "um caminho que projeta incontáveis caminhos" é enunciado e depois
**demonstrado** — as marcas de transformação como moeda conversível, com o caso das dez mil
marcas de espada. E o contrapeso é igualmente concreto: a limpeza obrigatória entre formas, com
a janela de vulnerabilidade. O domínio traduzido em "quantas marcas simultâneas cabem em você",
amarrado literalmente a "quantos pares de asas você consegue enxertar", é a melhor progressão de
metamorfo do material.

### `07 - Enslavement Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 14 | **Bloqueador** | A linha de rank 9 afirmava: "Ele **nunca teve um progenitor de rank 9 próprio**". Isso contradiz frontalmente `01 - Visão Geral dos Paths` e `05 - Qi Path`, que creditam a criação do caminho a um Venerável nomeado. Conferido no texto-fonte: a obra afirma **as duas coisas** em passagens diferentes e nunca as concilia. | **Corrigido.** A linha de rank 9 foi reescrita para dizer o que é verificável (a obra não mostra Venerável usando escravização como caminho principal, nem repertório de rank 9), e a divergência ganhou um callout próprio na abertura, com a leitura conciliadora marcada `(ded.)` e o convite explícito a decidir na mesa. |
| 15 | Menor | O Gu "Coragem" aparecia com nível `—` aqui e `efêmero` em `12 - Soul Path`. | **Corrigido** para `efêmero` nos dois. |

**O que está bom:** a honestidade sobre o arquétipo — "o praticante em si é fraco", dito na
primeira linha — é rara e útil. A regra **"decapitar o líder"** transforma uma batalha de massa
numa missão de infiltração dentro de uma batalha de massa, que é a melhor solução de mesa da
pasta para invocadores. E a **fundação de alma** como segunda barra que *desce se você parar de
treinar* é a mecânica que faz o personagem parecer outra classe em três cenas diferentes.

### `08 - Refinement Path`

Nenhum achado. É a nota mais bem construída do bloco antigo: o **fracasso como matéria-prima**
(um torneio aberto a todos cuja função real é colher os fracassos alheios, operado por quem já
leva cinco sextos do prêmio) é o achado mais original da pasta inteira, e a verdade escondida —
o caminho não é humano, e o melhor jeito de refinar do mundo pertence a uma espécie massacrada —
dá um arco de campanha pronto. A **progressão por erudição em vez de rank** é a escolha certa
para o único caminho da obra em que o rank importa pouco.

### `09 - Formation Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 16 | Sério | "As quatro ferramentas do caminho" e "Gu e golpes de assinatura, com o mecanismo" descreviam as mesmas quatro ferramentas com o mesmo detalhamento, a 200 linhas de distância. | **Corrigido:** a primeira virou um ponteiro nomeando as quatro e remetendo à segunda, que é mais completa (tem a porta dos fundos e a formação-prova). |

**O que está bom:** a tabela dos **três construtos que todo mundo confunde** (formação Gu ×
formação de batalha antiga × golpe de campo de batalha) é a peça didática mais valiosa da pasta:
sete linhas de comparação, cada célula com custo e consequência. A camada escondida como
**ausência** é uma decisão editorial corajosa e correta. E a economia que **inverte no meio da
escada** — grão-mestre gasta materiais caros, grande grão-mestre usa o chão de graça — é o tipo
de progressão que muda a moeda em vez de aumentar números.

### `10 - Poison Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 17 | Sério | A camada escondida anunciava "**quatro** fenômenos" e entregava cinco subseções numeradas. | **Corrigido.** |
| 18 | Sério | A nota não tinha o callout de convenção no cabeçalho — ele estava enterrado no meio da camada escondida, depois de a leitora já ter passado por `—` e `(ded.)` em várias tabelas. | **Corrigido** (ver o achado 19, tratado em bloco). |

**O que está bom:** o callout de abertura é modelo de honestidade — declara que a obra dá **um
único Gu Imortal** deste caminho e nenhum fundador, e diz onde está o material que compensa isso.
"O território do envenenador vira veneno" é a melhor peça de worldbuilding da pasta: um único
cultivador, ao longo de séculos, **vaza** uma zona proibida, com fauna e economia de guias
próprias. E a inversão "veneno é também remédio, e este é o caminho da doença" — confirmada por
ausência, já que não existe caminho da praga separado — resolve sozinha o problema de o
envenenador ser injogável num grupo.

### `11 - Sword Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 19 | **Bloqueador** | A camada escondida abria dizendo "Este é o único **dos cinco caminhos desta nota** cuja filosofia a obra enuncia em voz alta". A nota trata de **um** caminho. É resíduo de um modelo de nota coletiva, e faz a leitora procurar quatro caminhos que não existem ali. | **Corrigido.** |
| 20 | Sério | Sem callout de convenção no cabeçalho. | **Corrigido.** |

**O que está bom:** a tese filosófica é a mais bem entregue da pasta, porque vem com **gesto**:
a postura de acionamento (baixar a cabeça, fechar os olhos, erguer o punho) e a frase
*"eu decido meu próprio destino, não o céu"* dão à leitora uma frase de identidade de classe
pronta para um livro de regras. O contraste com o golpe que *toma emprestada a força do céu e da
terra* é canônico e faz o ponto sozinho. E a seção **"Técnica sem fundação, e fundação sem
técnica"** responde, com os dois lados canônicos, a pergunta que todo sistema enfrenta.

### `12 - Soul Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 21 | Sério | Sem callout de convenção no cabeçalho. | **Corrigido.** |

**O que está bom:** **a parede das cem almas** é a melhor mecânica de progressão da pasta — uma
barra que trava num teto absoluto, cuja única saída não é mais volume e sim **mudar de tipo**,
com a alma virando meio-lobo e podendo então crescer de novo. Progressão que também é
caracterização, e visível para quem souber olhar. A brecha na regra da erudição intransferível
("ler não ensina; fundir ensina, e te estraga") cobre a mesa inteira em duas regras que convivem.

### `13 - Sound Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 22 | **Bloqueador** | A nota citava a passagem canônica corretamente ("vinte a trinta por cento") e, três parágrafos depois, repetia o número como **20–39%**, ecoando o erro de `01`. A leitora vê dois números para a mesma regra na mesma página. | **Corrigido.** |

**O que está bom:** esta é a melhor nota escrita hoje. A **vantagem estrutural quantificada**
(metade da penalidade territorial) dá um motivo mecânico limpo para escolher o caminho
impopular, e a rota de "acumulação em vez de aquisição" — nível 7 lutando como nível 8 porque a
ficha dele não explica a força dele — é uma segunda trilha de progressão completa. A tabela de
**contramedidas** é única na pasta: nove antídotos nomeados, o que é um presente para um mestre
que precise conter um poder assustador sem inventar nada. E as nove canções entregam a
organização interna que ninguém esperaria (duas para estudar, quatro guardadas, uma extrema),
com a oitava marcada honestamente como sem nome.

### `14 - Space Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 23 | Sério | A linha de *Relações* chamava o caminho fantasma de "o **terceiro** melhor recipiente sem forma". `22 - Phantom Path` cita a fila canônica: fantasma, força, espaço, regra — o fantasma é o **primeiro**, e o espaço é o terceiro. A própria nota já dizia isso corretamente em *Sinergias*, e se contradizia. | **Corrigido.** |
| 24 | Sério | Sem callout de convenção no cabeçalho. | **Corrigido.** |

**O que está bom:** "Espaço é o que faz a abertura imortal ser grande" é o achado que afeta
**todo cultivador do mundo**, cultive espaço ou não, e a nota o transforma numa economia de
campanha inteira (o inventário do grupo é um lugar, o lugar tem tamanho, o tamanho é uma
estatística). A sequência da travessia da parede regional — uma barreira que **se fecha enquanto
você a atravessa** e cobra um recurso caro de cada membro por vez — é uma cena de aventura
completa, com relógio e custo distribuído.

### `15 - Theft Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 25 | Menor | "que já está registrada **acima** nesta nota" — a coisa referida está 100 linhas **abaixo**. | **Corrigido** para "adiante", com a seção nomeada. |

**O que está bom:** o único caminho da obra com **manifesto escrito pelo fundador**, e a nota
tem o bom senso de citá-lo quase inteiro em vez de resumir — "criar uma organização e fazer
regras, inventar honra ou usar emoções e cultura, tudo isso são métodos do caminho do roubo" é a
fala de vilão mais reaproveitável do cenário, e a nota explica por que ela **não é falsa**. A
virada final — a profundidade suprema do caminho do tomar é um ato de **doação**, selado atrás
de um patamar de domínio que ninguém vivo alcança, e a obra nunca explica por quê — é a melhor
lacuna deliberada do material.

### `16 - Wisdom Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 26 | **Bloqueador** | "cem marcas do Dao rendiam uma amplificação de cerca de **vinte por cento**". A tabela soberana (seção 7) e `19 - Star Path` dizem **dez por cento** para cem marcas; vinte por cento são **duzentas**. Conferido no texto-fonte. | **Corrigido**, e a régua foi ampliada para os três pontos que a leitora precisa (100 → 10%, 200 → 20%, 1.000 → dobro). |
| 27 | Sério | Sem callout de convenção no cabeçalho. | **Corrigido.** |

**O que está bom:** o custo **nas três dimensões ao mesmo tempo** — quanto você viverá, quão
rápido você pensa, quão forte você é — é o perfil de custo mais rico do sistema, e a lesão mental
com anatomia, sintoma e sequela permanente é muito melhor que "teste falhado". A condição de
segurança é elegante e contraintuitiva: **a ferramenta que dispensa competência exige competência
para ser usada em segurança**. E o callout que separa os dois Gu de adivinhação, corrigindo uma
confusão que o próprio vault tinha cometido, é exatamente o tipo de trabalho que a leitora nunca
vai ver e sem o qual ela erraria.

### `17 - Information Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 28 | Sério | Seção intitulada "As **onze** maneiras de romper um juramento" com **doze** itens numerados — e a camada escondida, mais acima, já se referia corretamente à "**décima segunda** maneira". | **Corrigido** para doze. |

**O que está bom:** o **sistema de juramentos** é o subsistema mais bem documentado da pasta e o
mais diretamente importável. A frase que funda tudo — *"não havia consequência para mentir"* — é
a justificativa de por que uma escola aparentemente burocrática é das mais valiosas do cenário, e
a nota a coloca cedo, onde uma leitora cética ainda está decidindo se vale a pena continuar. A
**corrida armamentista** (cadeado → gazua → cadeado novo → gazua nova, com datas) é um gerador de
campanha pronto, e o **modelo de aluguel** é o melhor argumento do material contra tesouros que
só dão números maiores.

### `18 - Time Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 29 | Menor | "Trezentas mil marcas num caminho é o patamar descrito como **nível de pseudo-Venerável**" — `01` define pseudo-Venerável como **rótulo de fracasso** (quem tentou a última prova do rank 9 e não sobreviveu), não como patamar de progressão. | **Corrigido:** a linha agora aponta para as quatro condições formais na tabela soberana, que é onde o número mora. |

**O que está bom:** a ideia de que a velocidade com que o refúgio do grupo **produz recursos** é
a mesma estatística que decide **com que frequência a catástrofe bate na porta** é a melhor coisa
da nota, e resolve sozinha o problema do tempo livre em campanha. A tabela do relógio, com seis
valores de fluxo, é o tipo de dado que uma designer usa sem precisar entender o mundo. E o
"teto duro" — a lista honesta do que este caminho declaradamente **não** faz, incluindo o
desmentido de que ele seria o mais forte do mundo — evita a expectativa que a leitora traria de
fora.

### `19 - Star Path`

Nenhum achado. **O céu é o depósito, e ele tem de ser conquistado peça por peça** é o melhor
achado de camada escondida entre as notas novas: um poder cuja **munição são posições no mapa do
céu**, cada uma comprada com semanas de trabalho e destrutível pelo inimigo — "o poder não sobe
de nível: ele se instala, e pode ser desinstalado por outra pessoa". O preço escondido (o
caminho que produz o melhor apoio do mundo produz também o pior paciente do mundo) é a
contrapartida mais elegante da pasta. E os números batem com a tabela soberana.

### `20 - Food Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 30 | Sério | Duas seções inteiras repetidas entre *Mecânicas típicas* e *A camada escondida* — a comida como fonte de marcas (incluindo a "rota exótica" quase palavra por palavra) e o ataque por alimentação. | **Corrigido:** as versões de *Mecânicas típicas* viraram resumos de duas frases com ponteiro para a seção completa. |
| 31 | Sério | "uma das **três** vias de adquirir marcas do caminho do céu" em três lugares — mas `25 - Heaven Path` lista **cinco** fontes, das quais **duas** passam pela comida. | **Corrigido** aqui e nas duas linhas correspondentes de `25`. |
| 32 | Menor | A palavra inglesa **"beastman"** solta no meio do texto em português, sem tradução nem glosa. | **Corrigido** para "raça variante", com link para `12 - Povos e Variantes Humanas`. |

**O que está bom:** a inversão que faz o caminho valer a nota está enunciada com todas as letras
— *"o caminho da comida não é o caminho de comer: é o caminho de sobreviver ao que se comeu"* —
e vem com o caso que a prova (a água imortal que mataria até um Gu Imortal que a bebesse sem
métodos de comida). A **fabricação de espécies** (a criatura mais vendida do mercado imortal não
é natural: foi projetada, e melhorada geração a geração) tem uma consequência de mundo perfeita:
quando a variedade nova aparece no mercado, o mundo inteiro deduz que existe uma herança
verdadeira por trás — e vai atrás dela.

### `21 - Rule Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 33 | Menor | A tabela de progressão trazia "Ranks 6–8", depois "Rank 7", depois "Rank 8" — três linhas com faixas sobrepostas, sem dizer que a primeira atravessa as outras duas. | **Corrigido:** a primeira virou "A série da desintegração (ranks 6–8)" e explica que as duas seguintes detalham o que **mais** entra em cada rank. |
| 34 | Menor | Nome de Venerável em inglês sem glosa, ao contrário de `25 - Heaven Path`, que explica a política. | **Corrigido** com a explicação em uma linha. |

**O que está bom:** o callout que **corrige um erro anterior nosso** sobre significado verdadeiro
— e que explica a regra certa com o contraexemplo nominal — é modelo de como registrar uma
correção sem apagar o rastro. A **literalidade** ("Grande aumenta o tamanho, não a força") é a
melhor caracterização do caminho e uma fonte inesgotável de bons desastres numa mesa. E o
reconhecimento honesto de que **o mecanismo interno do caminho nunca é explicado** transforma a
lacuna no "espaço mais convidativo do cenário para uma contribuição autoral".

### `22 - Phantom Path`

Nenhum achado. A curva de poder é o melhor uso de citação da pasta: uma passagem só desenha a
progressão inteira (mortal = só defesa; imortal = defesa quase perfeita **mais** emboscada), e a
nota tira dali um ponto de virada narrativo. **"O teto do caminho não é uma técnica: é uma região
da realidade"** e o registro de que o **segredo mais caro do mundo anda dentro dos cadáveres de
quem o guarda** são camada escondida de primeira linha. A tabela "ele já tem / ele ainda não tem"
resolve, com duas colunas, a confusão sobre graus de separação de um sub-caminho.

### `23 - Luck Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 35 | Menor | A camada escondida vem **antes** das mecânicas (escolha defensável, dado o caráter secreto do caminho), mas abria com "Tudo o que vem abaixo é material de mestre" — o que é falso: metade da nota, depois dela, é o que um praticante aprende. | **Corrigido:** a abertura agora delimita o escopo e explica por que a seção vem primeiro. |

**O que está bom:** **sorte se cozinha** é a mecânica mais original da pasta — não "role de novo"
nem "+2", mas pegar a sorte que se tem (um caixão preto, um pardal cinzento) e **convertê-la**
noutro tipo, numa oficina, com escala de força decidindo em quem se consegue mexer. A taxonomia
visual (cor, forma, tamanho) é um sistema de leitura de personagem que dispensa exposição do
mestre. E a trava **psicológica** do Gu que só aceita quem tem genuína disposição ao
autossacrifício é um teste de caráter que nenhuma perícia contorna.

### `24 - Human Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 36 | Sério | A tabela "O domínio, degrau a degrau" trazia **Pseudo-Venerável** como uma linha da escada de *attainment*. Não é um degrau de domínio: é um patamar de poder — e, por `01`, um rótulo de fracasso. A leitora conclui que existe um décimo degrau de erudição. | **Corrigido:** a linha saiu da tabela e virou um callout que preserva o requisito canônico (curar um Venerável exige pseudo-Venerável do caminho humano) explicando o que a expressão significa. |
| 37 | Menor | "dez **físicos extremos**" na primeira ocorrência, sem ligar ao termo que a pasta usa em toda parte ("as dez constituições extremas") nem à nota que os trata. | **Corrigido**, com os dois termos e o link. |

**O que está bom:** a tabela céu × humano em três linhas é a melhor peça conceitual da pasta
depois da de `09`. **"O caminho que está dentro de todos os outros"** — a descoberta de que as
criações de pico de outras escolas contêm profundidade humana, e que é isso que **tranca** certas
receitas — muda a categoria do caminho de "mais uma escola" para "uma camada que atravessa o
sistema". E a ironia central (o caminho que serve para resistir ao céu vem com uma coleira
institucional embutida) é o gancho político mais forte do material.

### `25 - Heaven Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 38 | **Bloqueador** | "**Três** fontes registradas:" seguido de **cinco** itens numerados. Numa nota cujo assunto é o caminho mais difícil de entender da pasta, uma contagem errada logo na lista mais operacional é caro. | **Corrigido**, com as três referências cruzadas em `20 - Food Path` e nas *Relações* desta nota. |

**O que está bom:** o callout de abertura **"O caminho em três linhas"** é a melhor decisão
editorial da pasta: a nota reconhece que é a mais difícil e entrega o quadro inteiro (o que você
precisa, o que você paga, o que você ganha) antes de qualquer detalhe. A tabela que separa
**tribulação miríade do calendário** de **provação induzida** conserta um erro que quebraria o
subsistema de progressão imortal inteiro, e diz isso na cara. E **"empobrecer é um método"** é a
mecânica que menos se parece com qualquer sistema existente: a dificuldade da provação é
proporcional ao seu patrimônio, então destruir o próprio patrimônio é uma jogada tecnicamente
correta.

### `26 - Dream Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 39 | Menor | Dois blocos repetidos: as limitações do Gu de "desvendar sonho" (abaixo da tabela de Gu e na tabela de golpes) e o método de limpar a vontade do céu de um reino (na tabela de golpes e em *Em combate e fora dele*). | **Corrigido:** as duplicatas viraram ponteiros de uma linha. |

**O que está bom:** a propriedade única está isolada e explicada — *"existe **um único** método
para adquirir o attainment de outra pessoa: explorar com sucesso o reino de sonho dela"* — e o
mecanismo (o sonho não te ensina; ele **guarda** o que o sonhador entendeu) é elegante. As três
regras finas (o domínio que você ganha é o **do dono do sonho**; a qualidade do professor decide
o ganho; só vale o que você vence) transformam a escolha de qual sonho invadir numa decisão de
carreira. E o número que dá a dimensão da injustiça — cem anos de pesquisa contra um a dois meses
de sonho — faz o ponto sem retórica.

### `27 - Os Caminhos Elementais`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 40 | **Bloqueador** | A nota se anuncia com "**doze** caminhos da natureza física" e enumera **onze** na mesma frase (fogo, água, gelo-e-neve, terra, madeira, metal, relâmpago, vento, luz, trevas, nuvem). A seção se chamava "Os doze verbetes" e tem onze verbetes — o décimo segundo item é a comparação *Luz × Trevas*, que não é um caminho. A própria nota dedica um callout a explicar que **gelo e neve são um caminho, não dois**, o que fecha a conta em onze. O erro se propagava para `01` e `29`. Doze usos corrigidos aqui, mais um em `01` e um em `29`. | **Corrigido**, e a seção *Luz × Trevas* ganhou uma linha dizendo que não é um verbete. |
| 41 | **Bloqueador** | "O número canônico: com cerca de dezesseis mil marcas de gelo-e-neve, o poder é **dezessete vezes**". A obra diz **dezesseis vezes** — dezessete é o que a fórmula reconstruída dá, e a nota o apresentava como texto. Contradizia a tabela soberana, que registra o arredondamento que a obra faz em números altos. | **Corrigido:** a regra agora traz a régua canônica inteira (100 → 10%, 1.000 → dobro, 16.000 → 16×) e remete à tabela soberana. |

**O que está bom:** a **regra do não-ciclo** é tratada exatamente como devia — verificada no
texto-fonte, com o aviso de que é ausência **no texto**, não numa wiki; com o mecanismo
substituto explicado por uma cena de engenharia (as marcas de fogo empurradas para as raízes das
ilhas, onde a terra é mais densa, virando **magma**); e com as duas exceções que a obra realmente
autoriza, nomeadas. A lição de que **o produto da contenção não é anulação, é uma terceira coisa**
é melhor que qualquer tabela de vantagem elemental. A seção "De onde vem a capacidade de imitar
outros caminhos" — a natureza já encadeia fogo em vapor, vapor em nuvem, sem marca nenhuma do
caminho da nuvem — é a melhor justificativa de "multiclasse sem multiclassar" do material, e um
leigo a entende na primeira frase. E os verbetes declaram o tamanho da evidência de cada um, com
a seção final "O que a obra não diz" listando exatamente quais dos onze não têm criador, essência
ou fraqueza declarada.

### `28 - Painting Path`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 42 | Menor | "comprender" → "compreender". | **Corrigido.** |

**O que está bom:** a nota curta é curta **por um motivo declarado no cabeçalho**, e isso é
exatamente o que a leitora precisa para não achar que faltou trabalho. A cena da marca de pintura
vista de perto — que diante de marcas de outros caminhos **não briga, não é destruída, e se
assenta por cima** — explica a propriedade central do caminho em escala microscópica, e a nota
tem a honestidade de abrir um `> [!info]` dizendo que essa cena resolve uma lacuna que a própria
nota registrava. O caso do golpe escondido dentro da Casa de Gu de investigação número um do
mundo, sobrevivendo a reformas por eras sem nunca interferir, é a mecânica de infiltração mais
forte do cenário — e ela não usa furtividade, usa **compatibilidade**. O contraste final com
`05 - Qi Path` (difundir mantém vivo e condena a envelhecer; guardar preserva intacto e
esteriliza) fecha as duas notas.

### `29 - Os Demais Caminhos`

| # | Nível | Achado | Estado |
|---|---|---|---|
| 43 | Menor | "os **doze** caminhos naturais" nas *Relações*. | **Corrigido** para onze. |

**O que está bom:** a nota enuncia a regra editorial na abertura — "um verbete curto não é uma
nota malfeita: é a medida exata do que existe" — e a cumpre. **A árvore de derivação** em bloco
de código é a peça mais didática do material para entender como o sistema se organiza, e o
**teste de duas perguntas** ("tem marcas do Dao próprias? tem significado verdadeiro próprio?")
resolve sozinho quantas escolas o mundo tem. Os dois casos especiais — o caminho que **fracassou**
(yin-yang, e o motivo é conceitual, não de poder: "um Venerável falhou em fundar um caminho não
por falta de poder, mas por a ideia não ser boa o bastante") e o que **nunca nasceu** (matança,
com o Gu-núcleo órfão solto no mundo) — são os dois melhores ganchos da pasta. E as três rotas de
construir um caminho novo mais as duas de fracassar são um sistema de "crie sua própria escola"
quase pronto.

---

## Ficou em aberto

| Item | Por quê |
|---|---|
| **`00 - Trilha do Jogador` ainda diz "os doze caminhos da natureza física"** ao apresentar `27`. É o mesmo erro corrigido em `01`, `27` e `29`. | Fora do meu escopo de arquivos. Correção de uma palavra: *doze* → *onze*. |
| **Divergência de fundação do caminho da escravização.** Registrada em `07` como divergência, não resolvida. | A obra afirma as duas versões e nunca as concilia; resolver exigiria escolher, o que a política do vault não autoriza. A leitura conciliadora está marcada `(ded.)`. |
| **Divergência de datação do caminho fantasma** (Antiguidade Tardia × herança da Era Imemorial), já registrada em `22`. | Mesma razão. |
| **`05 - Qi Path` mantém *Xi Land* e *Hu Land* em inglês** sem glosa. | São topônimos, e a política do vault é não inventar tradução. Uma glosa entre parênteses seria útil, mas depende de checar se a tradução PT publicada os nomeia. |
| **Nomes de Veneráveis em inglês** em `21` e `25`. | É política declarada do vault, agora explicada nas três notas onde os nomes aparecem sem contexto. Não é defeito; é decisão. |

---

## As três coisas que eu mudaria com mais tempo

1. **Padronizar a posição da camada escondida.** Ela aparece depois de *Mecânicas típicas* em
   quase todas as notas, antes dela em `23 - Luck Path`, e dentro de *Filosofia* em `27`. Como a
   leitora vai ler 27 notas em sequência, a inconsistência de estrutura custa mais do que
   parece — ela perde a expectativa de onde procurar. A ordem certa é a maioritária
   (filosofia → mecânicas → camada escondida → progressão → Gu → design), e as exceções deviam
   ser justificadas no lugar, como `23` agora justifica.

2. **Cortar a redundância residual entre *Mecânicas típicas* e *A camada escondida*.** Tratei os
   três casos piores (`05`, `20`, `26`) e o de `09`, mas o padrão se repete em menor escala em
   pelo menos meia dúzia de notas: a mecânica é apresentada uma vez de leve e depois de novo por
   inteiro. A regra que resolveria isso de vez, e que vale escrever no modelo de nota:
   ***Mecânicas típicas* descreve o que o praticante faz; *A camada escondida* descreve por que
   funciona e o que custa. Se as duas seções contam o mesmo fato, o fato pertence à segunda.**

3. **Dar à pasta uma página de duas colunas: "o caminho que faz X".** As 29 notas são excelentes
   verticalmente e a leitora não tem como atravessá-las horizontalmente. Ela vai chegar com
   perguntas de função — *quem cura? quem move o grupo? quem fabrica? quem investiga? quem quebra
   uma fortaleza?* — e hoje precisa abrir vinte e sete notas para responder. O mapa por função em
   `01` é o começo disso, mas ele agrupa caminhos, não capacidades. Uma tabela de trinta linhas
   (capacidade → caminho principal → caminho alternativo → o que custa) transformaria a pasta de
   enciclopédia em ferramenta de mesa, e é a única coisa que falta para ela ficar completa.
