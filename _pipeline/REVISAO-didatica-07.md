# Revisão didática — `07 - Veneraveis e Legados/`

**Revisora:** designer de RPG contratada, sem nenhuma leitura prévia de *Reverend Insanity*.
**Material:** as 4 notas da pasta 07 (695 linhas), lidas como única fonte.
**Data:** 2026-09-01.

**Por que esta revisão existe:** as pastas `01`–`06` e `08`/`09` já passaram por leitura
leiga. A `07` foi escrita e depois corrigida pelo mesmo agente, sem olhar externo.

**Método:** li as quatro notas na ordem em que uma designer as encontraria (nota-porta
primeiro), anotando cada termo que não entendi e cada nome que não consegui situar.
Depois cruzei todo número e toda afirmação estrutural contra `09 - Apendices/Tabelas de
Referência Rápida.md` (fonte soberana), `09 - Apendices/Linha do Tempo e Eras.md`,
`09 - Apendices/Glossário EN-PT.md`, `01 - Cultivo/Tornar-se Venerável.md`,
`04 - Mundo/Cosmologia.md` e `04 - Mundo/Fate Gu.md`. Por fim auditei as 36 âncoras de
wikilink da pasta contra os cabeçalhos reais das notas de destino.

---

## Bloqueadores

Cinco. Impedem o trabalho de design ou fazem com que ele seja feito em cima de premissa
errada.

### B1. O caminho principal de Primordial Origin é uma invenção não marcada — e as duas notas se contradizem

A tabela dos dez (`Visão Geral dos Veneráveis`, linha 111) dá o caminho principal de
Primordial Origin como **`origin path` (caminho da origem)**, em texto simples, ou seja,
apresentado como canônico.

`Os Arquitetos da Ordem` diz o oposto, na ficha (linha 39) e na nota de rodapé:

> não nomeado explicitamente nas fontes […] o nome "Primordial Origin" sugere associação
> com o *origin path*, mas isso **não é afirmado no texto**.

Não existe `03 - Paths/Origin Path.md`, e "origin path" não aparece em nenhum outro lugar
do vault fora dessas duas linhas. É uma inferência a partir do nome próprio, exatamente a
que a footnote diz ter recusado.

**Por que é bloqueador e não sério:** está na tabela da nota-porta, que é a superfície mais
lida da pasta e a única que muita gente vai ler. Anotei "caminho da origem" no meu caderno
de cenário na primeira passada e só descobri que era chute quando abri a segunda nota e li
a footnote. Uma designer com menos tempo não teria descoberto.

### B2. A definição de Dao Lord contradiz a nota que o próprio vault designa como fonte única — e omite a metade jogável do mecanismo

`01 - Cultivo/Tornar-se Venerável.md` afirma, sobre a seção "O Dao Lord":

> Esta seção é a **fonte única** do assunto no vault; as outras notas remetem para cá.

**Nenhuma das quatro notas da pasta 07 linka `[[Tornar-se Venerável]]`.** Zero ocorrências
(auditei todos os 36 wikilinks da pasta). Em vez de remeter, a `Visão Geral dos Veneráveis`
mantém uma seção `## Dao Lord` própria, paralela — e as duas divergem no conteúdo:

| | O que a 07 diz | O que a fonte única diz |
|---|---|---|
| Alcance | "sentir e refinar **automaticamente** todas as marcas de dao daquele caminho existentes **no mundo inteiro**" | a **capacidade** nasce global; a **realização é territorial e leva séculos**: "um Venerável recém-alçado a Dao Lord **ainda não é invencível**" — precisa sair e refinar as marcas região por região |
| Permanência | não menciona | **perde-se**, de duas formas documentadas (saturação do caminho; perda da própria mente), e recupera-se num lugar específico |

O `Glossário EN-PT` (linha 250) confirma o lado territorial: "Venerável que reivindicou
todas as marcas naturais do próprio caminho **num território**".

**Consequência de design, que é o que me interessa.** Na versão da 07, Dao Lord é um
interruptor binário: ligado, onipresente, nada a jogar. Na versão correta é uma conquista
de mapa **em curso**, com regiões já tomadas e regiões ainda não — o que é imediatamente
utilizável (onde estamos? já é dele aqui?).

Pior é a omissão da perda do senhorio, que custa caro em dois lugares distintos:

1. **É a explicação estrutural de por que Giant Sun escondeu o caminho da sorte.** A fonte
   única diz: se muitos rank 8 do mesmo caminho acumulam avanços coletivos, o caminho
   ultrapassa um limiar e o Venerável é **expulso** do supremo grão-mestre, perdendo o
   senhorio. Logo, um Dao Lord tem motivo mecânico para manter o próprio caminho secreto e
   subdesenvolvido. `Os Criadores de Caminhos` apresenta o segredo de Giant Sun como
   decisão sem causa — o dado que a torna óbvia está a uma nota de distância e não é
   citado.
2. **É a única alavanca real que personagens não-rank-9 têm contra um Venerável** —
   pesquisar o caminho dele, em grupo, por gerações. Sem isso, a pasta me entrega dez
   figuras invencíveis e nenhum vetor de ataque.

Escrevi minhas primeiras notas de regra a partir desta pasta e desenhei um Dao Lord
binário e onipresente. Teria descoberto o erro depois de já ter construído em cima.

### B3. Número de amplificação diverge da fonte soberana — e a fórmula inferida está apresentada como fato

`Visão Geral dos Veneráveis`, linha 62:

> a regra prática é que **cada mil marcas somam uma vez o efeito base** — mil marcas dobram
> o efeito, dois mil triplicam, **dez mil o multiplicam por onze**. A curva é linear, e não
> uma duplicação a cada mil.

`Tabelas de Referência Rápida` §7 traz quatro pontos, todos rotulados "ponto citado na
obra": 100 → 1,1× · 1.000 → 2× · **10.000 → 10×** · 50.000 → 50×. A fórmula
`× (1 + marcas ÷ 1.000)` é marcada **`inferido`**, com esta observação literal:

> 10.000 marcas dariam 11× e o texto diz "dez vezes"; 50.000 dariam 51× e o texto diz
> "cinquenta vezes".

Ou seja: o "onze" da 07 é precisamente o artefato de arredondamento que a fonte soberana
identifica como efeito colateral da **nossa** reconstrução. A pasta publica como canônico o
número que a fonte soberana marca como não-canônico, sem nenhuma marcação de confiabilidade,
e ainda apaga dois dos quatro pontos que a obra fornece.

Regra do vault: divergiu da soberana, é aqui que está errado.

### B4. A pasta sobre quem inventou as disciplinas não linka nenhuma disciplina

A pasta credita a fundação de nove caminhos: força, transformação, madeira, alma, regra,
sabedoria, roubo, sorte, e o espaço como especialidade. O vault tem nota própria para
**sete** deles: `Strength Path`, `Transformation Path`, `Soul Path`, `Rule Path`,
`Wisdom Path`, `Space Path`, `Luck Path` (madeira e roubo não têm nota — isso está certo,
não são lacunas da 07).

A pasta linka **dois**: `[[Luck Path]]` e `[[Soul Path]]`. `[[Rule Path]]` e
`[[Heaven Path]]` linkam para dentro da 07 e não recebem retorno.

Para uma designer, esse é o clique mais previsível do material inteiro: leio "ele criou o
caminho da regra", quero saber na mesma hora **o que o caminho da regra faz numa mesa**. A
pasta me conta quem foi o autor e não me diz onde está o produto. Cada vez que isso
acontece eu paro, saio da pasta e procuro pelo nome — nove vezes.

### B5. A nota-porta exige que eu já saiba o que é um Gu

`Visão Geral dos Veneráveis` é o primeiro arquivo que uma pessoa abre nesta pasta. Ela usa,
sem definir e sem linkar:

| Termo | Onde aparece primeiro | Nota que existe e não é linkada |
|---|---|---|
| **Gu** | l. 37, "Um Gu de rank 9 não é feito de…" | `[[O que é um Gu]]`, `[[Gu Imortais]]` |
| **marcas de dao** | l. 37, sem glosa; só na l. 62 dá para inferir o que são | `[[Dao Marks]]` |
| **rank** | l. 29, na frase de abertura | `[[Ranks e Avanço]]` |
| **caminho / path** | l. 52–53, os dois termos misturados | `[[Visão Geral dos Paths]]` |
| **mundo privado / dimensão privada / abertura** | l. 35, l. 61, l. 137 — três nomes para a mesma coisa | `[[Blessed Lands e Grotto-Heavens]]` |
| **golpe** | l. 53, "Golpes lendários de Veneráveis" | `[[Killer Moves]]` (nunca linkada em toda a pasta) |
| **via correta / via demoníaca** | l. 45, e é a 2ª coluna da tabela dos dez | `[[Caminho Correto e Caminho Demoníaco]]` |
| **Grande Dao** | l. 37 | — (nunca definido em lugar nenhum da pasta) |
| **human path** | l. 52, em inglês, sem glosa | — |
| **essência imortal de terceiro/quarto grau** | l. 61, l. 64 | o vault **nomeia** as quatro: uva-verde, tâmara-vermelha, lichia-branca, damasco-amarelo |

As três notas temáticas se saem melhor que a nota-porta nisso, o que é o inverso do que
deveria acontecer. Uma nota-porta que pressupõe as outras seis pastas não é uma porta.

---

## Sérios

Causam erro de leitura ou retrabalho, mas não travam o design.

### S1. "Nível de realização" é a tradução que o próprio Glossário rejeita por escrito

`Glossário EN-PT`, linhas 87 e 170:

> attainment level | ~~nível de realização~~ → **o vault escreve "attainment"** | "realização"
> não sugere que se trata de **compreensão** de um caminho.

A pasta 07 escreve "nível de realização" (`Visão Geral` l. 63; `Criadores` l. 116), "níveis
de domínio" (`Visão Geral` l. 63; `Criadores` l. 33; `Arquitetos` l. 84). A palavra
`attainment` **não aparece uma única vez na pasta**, e `[[Attainment]]` nunca é linkada.

Efeito prático em mim: li a escada de nove degraus em `Attainment`/`Tabelas`, li o gargalo
do rank 9 na 07, e **não reconheci que eram a mesma escada** até cruzar os arquivos.

### S2. A tabela dos dez está fora da ordem de era que ela mesma anuncia

Ela diz "Estão em ordem aproximada de era". Contra `Linha do Tempo e Eras`:

| Era | Quem, segundo a linha do tempo | Posição na tabela da 07 |
|---|---|---|
| Remota | Primordial Origin, Star Constellation | 1, 2 ✔ |
| Antiga | Reckless Savage, Thieving Heaven, Limitless | 3, **5**, **7** |
| Medieval | Giant Sun, Genesis Lotus | **6**, **4** |
| Tardia | Spectral Soul, Paradise Earth, Red Lotus | 8, 9, 10 ✔ |

Genesis Lotus (Medieval) aparece em #4, antes de dois da era Antiga; Limitless (Antiga)
aparece em #7, depois de Giant Sun (Medieval). As eras estão intercaladas.

Agravante: a tabela **não tem coluna de era** e a nota-porta **não linka
`[[Linha do Tempo e Eras]]`**. "Quando" é a segunda pergunta que faço depois de "quem", e a
pasta não responde nem aponta para quem responde.

### S3. Aliases duplicados — cada um dos dez nomes é alias de duas notas ao mesmo tempo

`Visão Geral` declara os dez nomes nos `aliases`. `Criadores` declara cinco deles,
`Arquitetos` três, `Romperam` dois. **Todos colidem.** O Obsidian acusa conflito e resolve
de forma arbitrária: digitar "Giant Sun" pode me levar à nota-porta ou à ficha, sem
critério.

A regra do vault ("nunca dependa de alias") existe por isso, mas aqui os aliases não são só
frágeis — estão ativamente quebrados, e são o principal caminho de busca de quem só tem um
nome próprio na mão.

### S4. A porta por onde entram os demônios de outro mundo é atribuída à pessoa errada

`Os Que Romperam as Leis`, seção "O que os dois têm em comum":

> **Um abriu a porta por onde entram os seres de fora**

O "um" no contexto é Thieving Heaven. Mas `Cosmologia#A fronteira do mundo` e a ficha de
Limitless em `Os Criadores de Caminhos` (item 3) são explícitos e concordes entre si: a
construção que perfura deliberadamente a fronteira e puxa matéria de fora é de **Limitless**,
e os demônios de outro mundo "não são anomalia — são **subproduto da obra dele**".

Thieving Heaven fez outra coisa: **rompeu** a membrana no ponto fino (o quase-apocalipse) e
depois a **remendou**. Ele não abriu a porta dos demônios — ele próprio já era um, o que é
justamente o que a nota estabelece três seções antes.

Duas notas da mesma pasta dando dois autores para o mesmo fenômeno é o tipo de coisa que eu
só descubro depois de já ter escrito um arco em cima.

### S5. Red Lotus é o único dos dez sem era; Spectral Soul tem era relativa em vez de nomeada

A ficha de Red Lotus não tem linha **Era**. As outras nove têm. Como ele é o último da
tabela e o dono da consequência mais grave do cenário, é o que eu mais precisaria situar.

Spectral Soul recebe "surgiu cerca de 200.000 anos depois da morte de Giant Sun" — o que me
obriga a resolver uma conta para localizar a figura numa linha do tempo que a pasta não
linka. `Linha do Tempo e Eras` diz simplesmente: Antiguidade Tardia.

### S6. A pasta afirma que não há décimo primeiro; o vault registra a divergência

`Visão Geral`, l. 122: "A lista acima é fechada e **não há um décimo primeiro**."

`Tornar-se Venerável` traz um callout de transparência: a obra fecha em dez em praticamente
todo o texto, mas "uma passagem tardia fala em onze — provavelmente incluindo alguém
posterior ou um pseudo-Venerável revivificado".

A contagem de dez está certa e não é isso que estou contestando. O problema é de **forma**:
a nota-porta apaga uma divergência que o resto do vault escolheu declarar, e o faz com uma
ênfase ("não há") que soa a fechamento de assunto. Se eu cruzar com a outra nota, passo a
duvidar de qual das duas está desatualizada.

### S7. "Um dos três Veneráveis Demônios daquela era" aparece três vezes e nunca nomeia os três

A fórmula está nas fichas de Reckless Savage, Limitless (`Criadores`) e Thieving Heaven
(`Romperam`) — três notas, três vezes, e em nenhuma delas se diz quem são os outros dois.
Quem lê uma ficha isolada fica com um conjunto aberto.

É exatamente o vício que esta pasta tinha mais chance de ter: nomes próprios estrangeiros em
série, sem o mapa que os liga. Aqui o mapa existe (`Linha do Tempo e Eras` resolve em uma
linha) e não é oferecido.

### S8. Termos com nota própria no vault, usados cegos

| Termo | Onde | Nota existente, não linkada |
|---|---|---|
| reino de sonho (e "reino de sonho **profético**", categoria apresentada sem a base) | `Arquitetos` l. 108 | `[[Dream Path]]` |
| Gu de longevidade — que é **um dos três componentes** do bloqueio celestial | `Arquitetos` l. 147 | `[[Longevidade]]` |
| refino; unicidade dos Gu Imortais como regra ativa | `Romperam` l. 68 | `[[Refino de Gu]]`, `[[Gu Imortais]]` |
| caminho do tempo | `Romperam` l. 113 | `[[Time Path]]` |
| "segredo celeste" | `Arquitetos`, ficha e item 2 de Paradise Earth | — nunca definido na pasta |
| tribulações / desastres | `Criadores` l. 142; `Romperam` l. 62 | `[[Tribulações e Calamidades]]` (linkada só uma vez, em `Arquitetos`) |
| **pedras de essência imortal** | `Arquitetos` l. 56 | confundível com `[[Pedras Primordiais]]`, que é outra moeda, de outro público — sem link eu misturei as duas na primeira leitura |
| "construção mágica de rank 8/9" (3×) | `Criadores` l. 80; `Arquitetos` l. 88, l. 131 | o vault tem termo próprio: **Casa de Gu Imortal**, definido em `[[Killer Moves]]` e usado em toda a 05 |

---

## Menores

Polimento. Nenhum causa erro.

- **`[[#Dao Lord]]`** (`Visão Geral` l. 53): wikilink de âncora nua, fora da convenção do
  vault ("pelo nome exato do arquivo").
- **Erro de digitação** (`Romperam` l. 99): "**Zumbis existem.** A almas que deveriam ser
  reivindicadas na morte e não são." → "As almas".
- **A frase de abertura de `Arquitetos`** encadeia três pessoas em três orações e é a mais
  difícil de processar da pasta.
- **"Céu da Longevidade"** aparece na tabela de cabeçalho de Giant Sun e nunca no corpo:
  nome próprio solto, sem nada atrás.
- **"o trono que se disputa periodicamente"** (`Criadores`, Giant Sun item 3):
  `[[Eventos e Instituições Jogáveis]]` fixa **decenal**. Dar o número custa uma palavra e
  me poupa uma consulta.
- **Star Constellation, "19.000 anos"**: é o único número da pasta sem retaguarda na fonte
  soberana nem em `Tornar-se Venerável` (que registra só os extremos, 25.000 e ~3.000). Não
  é divergência — é o único dado que não consegui confirmar em lugar nenhum.
- **Nenhuma nota linka `[[Glossário EN-PT]]`**, apesar de `Visão Geral` ter um callout
  inteiro (`[!warning] Sobre os nomes`) dedicado a explicar por que os nomes ficam em inglês
  — que é literalmente o assunto da seção final do Glossário.
- **"outro Gu de rank 9, associado ao amor"** (`Romperam` l. 103) nunca é nomeado nem
  linkado. Fico sem saber se é um objeto catalogado que eu poderia consultar.
- **"significado verdadeiro"** é muito bem glosado (`Criadores`, Reckless Savage item 3),
  mas a glosa chega **depois** do termo já ter sido usado no título em negrito do item.

---

## O que está bom e não precisa mexer

Registro com o mesmo cuidado, porque várias destas decisões são melhores que o padrão do
mercado e alguém pode "corrigi-las" por engano.

1. **A porta de entrada existe e funciona.** A tabela "Os dez" responde "quem são e o que
   cada um mudou no mundo" em uma tela, com caminho, legado em uma linha e coluna "Onde
   ler". Consegui responder à pergunta **sem abrir as três notas temáticas** — que era o
   teste. É a melhor decisão estrutural da pasta e a razão de os problemas acima serem
   corrigíveis em vez de fatais.
2. **Agrupar por tipo de legado em vez de uma nota por pessoa** é a escolha certa para
   design, e a nota-porta **explica por que** faz isso — o que evita que o leitor conclua
   que é desorganização.
3. **A política "legado, não biografia" está sendo cumprida de verdade.** Varri as quatro
   notas atrás de enredo vazando e achei quase nada. O mais próximo são o arco temático de
   Thieving Heaven ("um estrangeiro que passou a existência inteira tentando ir embora") e o
   fecho de Star Constellation ("a pessoa mais racional da história concluiu que a solução
   era deixar de ser uma pessoa") — ambos dentro de callouts de design, ambos enunciados
   como **tema** e não como acontecimento. Nenhum evento datado, nenhuma reviravolta, nenhum
   nome de personagem secundário.
4. **As 36 âncoras de wikilink conferem.** Testei uma a uma contra os cabeçalhos reais das
   notas de destino (`Cosmologia#A fronteira do mundo`, `Blessed Lands e Grotto-Heavens#
   Anexação…`, `Vontade dos Céus#Casos de resistência da lei`, etc.). Nenhuma quebrada.
   Isso é raro e vale dizer.
5. **As duas lacunas honestas, com footnote explicando por que são lacunas** (caminho
   principal de Primordial Origin e de Red Lotus) são exatamente o comportamento certo. O
   defeito é a tabela desobedecer à própria footnote (B1), não a footnote.
6. **Os callouts "Para o design" são o melhor conteúdo da pasta** e resolvem o critério de
   utilidade com folga. A Caverna como megadungeon com proibição diegética; o quadro de
   missões de Paradise Earth como **empregador** em vez de tesouro; as almas divididas como
   conspiração honesta em que toda pista é verdadeira; "patronos poderosos só agem por
   peças" como solução do problema clássico dos NPCs fortes; o destino **rachado** em vez de
   abolido. Nove das dez figuras me deixam com uma peça de jogo na mão.
7. **A seção "Ter ou não ter um Venerável vivo"** entrega uma escolha de cenário
   explicitamente à designer, com as consequências dos três estados e o registro de que a
   era sem Venerável é "uma era de candidatos". Isso é desenho de ferramenta, não descrição
   de mundo.
8. **`Os Que Romperam as Leis` é a nota mais bem escrita das quatro para leigo**: glosa
   marcas de dao como "o equivalente a pontos de experiência", glosa "terra abençoada"
   dentro do próprio link, e fecha com uma seção que enuncia o eixo comum dos dois em quatro
   marcadores.

---

## Veredito

**Sim, eu conseguiria usar os Veneráveis no meu jogo — mas não com a pasta no estado em que
a recebi.**

Sendo específica sobre o que consigo e o que não consigo:

**Consigo** montar uma campanha inteira só com esta pasta. Ela me dá um megadungeon de nove
camadas com uma regra diegética que mantém os mais poderosos do mundo do lado de fora
(deixando o interior para personagens de escala jogável, que é o problema mais difícil de
resolver em cenários de poder alto); um empregador morto que paga em moeda própria e não se
esgota quando encontrado; um antagonista que é literalmente dezenas de pessoas ao mesmo
tempo sem que os fragmentos saibam uns dos outros; uma ordem política que roda sozinha o
programa de um cadáver enquanto os participantes acham que estão disputando um trono; e um
destino rachado, com um partido tentando remendá-lo e outro tentando alargar a rachadura.
Isso é mais material jogável do que a maioria dos cenários publicados entrega.

**Não consigo**, sem corrigir antes, colocar um Venerável em cena como força ativa — e é o
B2 que impede. A peça que explica *como* um Venerável opera, o Dao Lord, está aqui numa
versão que a própria fonte única do vault contradiz, e sem o mecanismo de perda do senhorio,
que é a única alavanca que personagens abaixo do rank 9 têm contra ele. Eu já tinha
rascunhado um Dao Lord binário e onipresente antes de cruzar os arquivos. Teria descoberto o
erro com o cenário já construído em cima.

**E o custo maior não está em nenhum item isolado, está no acoplamento.** Cada vez que a
pasta diz "ele criou o caminho da regra" e não me dá o link, eu saio da pasta e procuro pelo
nome — nove vezes. Cada vez que diz "nível de realização", eu não reconheço a escada que já
tinha aprendido em outro lugar do vault. A pasta está escrita como se eu já tivesse lido as
outras seis pastas, e a nota-porta — que é justamente a que não pode assumir isso — é a que
mais assume.

Resumo em uma frase: **o conteúdo desta pasta está entre os melhores do vault e o
acoplamento dela com o resto do vault é o pior.** Todos os cinco bloqueadores se resolvem
com edições localizadas; nenhum exige reescrever uma nota.

---

## Fase 2 — correções aplicadas

Aplicadas na ordem: bloqueadores primeiro, uma nota por vez.

### `Visão Geral dos Veneráveis.md`
- **B1** — linha do Primordial Origin na tabela dos dez: `origin path` substituído por
  `— (a obra não informa)`, com nota abaixo da tabela explicando por que os **dois** traços
  existem e remetendo à footnote de `Os Arquitetos da Ordem`.
- **B2** — seção `## Dao Lord` reescrita: passa a remeter a `[[Tornar-se Venerável]]` como
  fonte única, corrige "automaticamente no mundo inteiro" para a distinção
  capacidade global / realização territorial em curso, e acrescenta a perda do senhorio
  (saturação e perda de mente) com a consequência de design. Nova entrada em "Relações".
- **B3** — regra de amplificação realinhada com `Tabelas de Referência Rápida` §7: os quatro
  pontos canônicos passam a ser citados como tais, e a fórmula fica marcada `(ded.)`.
- **B5** — glosa e link na primeira aparição de Gu, marcas de dao, rank, caminho, abertura
  imortal, golpe, via correta/demoníaca, Grande Dao, caminho humano; as quatro essências
  passam a ser nomeadas.
- **S1** — "nível de realização"/"níveis de domínio" → `attainment`, com link para
  `[[Attainment]]`.
- **S2** — tabela dos dez reordenada por era, com **coluna de era** nova e link para
  `[[Linha do Tempo e Eras]]`.
- **S3** — `aliases` reduzidos aos que designam a própria nota; os dez nomes próprios saem
  daqui e ficam nas fichas.
- **S6** — a afirmação de fechamento passa a registrar a divergência das onze, remetendo ao
  callout de `Tornar-se Venerável`.
- **Menores** — `[[#Dao Lord]]` → wikilink pelo nome do arquivo; link para
  `[[Glossário EN-PT]]` no callout sobre os nomes.

### `Os Criadores de Caminhos.md`
- **B4** — links para `[[Strength Path]]`, `[[Transformation Path]]`, `[[Soul Path]]`,
  `[[Rule Path]]`, `[[Luck Path]]` nas fichas correspondentes.
- **B2 (consequência)** — a ficha de Giant Sun passa a dar o motivo mecânico do segredo
  (saturação do caminho tira o senhorio), com link para `[[Tornar-se Venerável]]`.
- **S1** — vocabulário de attainment corrigido e linkado.
- **S3** — aliases desduplicados.
- **S5** — era de Spectral Soul nomeada (Antiguidade Tardia), mantendo o intervalo relativo.
- **S7** — os três Veneráveis Demônios da Antiguidade Antiga passam a ser nomeados onde a
  fórmula aparece.
- **S8** — `[[Killer Moves|Casa de Gu Imortal]]`, `[[Tribulações e Calamidades]]`,
  `[[Blessed Lands e Grotto-Heavens]]` na primeira aparição de dimensão privada.
- **Menores** — "Céu da Longevidade" explicado no corpo; ciclo do trono qualificado como
  decenal; glosa de "significado verdadeiro" antecipada.

### `Os Arquitetos da Ordem.md`
- **B1** — footnote de Primordial Origin reforçada e referenciada a partir da nota-porta.
- **B4/S8** — links para `[[Wisdom Path]]`, `[[Dream Path]]`, `[[Longevidade]]`,
  `[[Killer Moves]]`, `[[Attainment]]`; "pedras de essência imortal" desambiguada contra
  `[[Pedras Primordiais]]`; "segredo celeste" definido na primeira aparição.
- **S1** — vocabulário de attainment corrigido.
- **S3** — aliases desduplicados.
- **Menores** — frase de abertura desmembrada.

### `Os Que Romperam as Leis.md`
- **S4** — "O que os dois têm em comum" corrigida: a porta dos demônios de outro mundo é
  atribuída a Limitless (conforme `Cosmologia` e `Os Criadores de Caminhos`), e o que
  Thieving Heaven fez — romper e remendar — é enunciado com precisão.
- **S5** — ficha de Red Lotus ganha linha **Era** (Antiguidade Tardia).
- **B4/S8** — links para `[[Space Path]]`, `[[Time Path]]`, `[[Refino de Gu]]`,
  `[[Gu Imortais]]`, `[[Tribulações e Calamidades]]`.
- **S3** — aliases desduplicados.
- **Menores** — "A almas" → "As almas".
