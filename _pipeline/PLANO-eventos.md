# PLANO — pasta `08 - Eventos e Cenarios/`

> **Estado:** plano fechado, pronto para distribuição aos redatores.
> **Data:** 2026-09-02.
> **Gabarito obrigatório:** `_pipeline/MODELOS/modelo-evento.md`. Nenhuma nota desta pasta
> foge dele.
> **Fontes brutas:** `_pipeline/notas/eventos-caps-0001-0400.md` (daqui em diante **A**),
> `-0401-0800` (**B**), `-0801-1200` (**C**), `-1201-1600` (**D**), `-1601-2000` (**E**),
> `-2001-2334` (**F**). Total varrido: ~197 entradas em 7.093 linhas.

---

## 1. A regra que governa a pasta (repetir no topo de toda nota)

O evento entra como **situação**, nunca como história. O que a designer precisa é: a causa
mecânica, a geografia, os perigos, as regras especiais que valem no local, as forças
descritas como *tipos e facções*, os prêmios, o relógio e o leque de desfechos possíveis.
O que **não** entra: o encadeamento narrativo do romance, quem venceu, quem morreu, quem
traiu quem, o papel de personagens nomeados. Um personagem histórico só aparece como
**função** ("o fundador da herança", "a força que convocou a assembleia").

Cada nota bruta traz um campo **"Cuidado de spoiler"**. Ele é vinculante: o que está lá
não migra para a nota final, em nenhuma hipótese.

---

## 2. Critério de curadoria aplicado

Das ~197 entradas das seis varreduras, aplicou-se este filtro, nesta ordem:

1. **Deduplicação entre faixas** (seção 3): eventos que aparecem em mais de um arquivo
   viraram uma entrada só, somando as informações complementares.
2. **Único e grande → nota própria.** Um acontecimento irrepetível que rende um cenário
   inteiro ganha nota (ex.: a Herança dos Três Reis, a Montanha Yi Tian, a Caverna do
   Demônio Enlouquecido).
3. **Recorrente → nota temática.** Categorias que se repetem no mundo viram uma nota que
   cobre a categoria, com os exemplares concretos dentro (marés de bestas, aberturas de
   herança, cercos de terra abençoada, calamidades, torneios, assembleias, feiras).
4. **Histórico citado → uma nota só, de pano de fundo.** Serve de contexto, não de cenário.
5. **Descartado:** o que já é coberto como *instituição* nas pastas `05` e `06` (ver
   seção 5), e o que só interessava por "o que aconteceu com fulano".

**Ordem de leitura da pasta = escala + faixa de rank.** Abre com o que uma mesa iniciante
de rank 1 joga na primeira sessão e fecha com o que muda o mundo inteiro. É esse o
critério do prefixo numérico, e é ele que a barra lateral do Obsidian vai mostrar.

**Total: 28 notas de conteúdo (`02` a `29`) + a nota-porta (`01`).**

---

## 3. Lista unificada e deduplicação entre faixas

Eventos que apareceram em mais de uma varredura, às vezes com nome diferente. Esta é a
tabela que impede dois redatores de escreverem a mesma coisa duas vezes.

| Evento unificado | Aparece em | Como cada faixa o chama | Nota de destino |
|---|---|---|---|
| **Marés de bestas** (a categoria) | A, B, C, F | "ciclo das marés de bestas" (A), "beast wave usada como arma" (B), "marés de bestas" (C), "beast tides" (F) | `03` |
| **Maré de lobos de Qing Mao** | A | "small beast tide" + "The Wolf Tide / Great Wolf Tide" + "Crane Disaster" (três entradas encadeadas) | `02` (crane disaster em `03`) |
| **Calamidade terrena de terra abençoada** | A, B, C, F | regra do cap. 374 (A), "Sixth Earthly Calamity of Hu Immortal" (B), "Calamidades terrestres e tribulações celestiais" (C), "escada de calamidades" (F) | `21` |
| **Lang Ya blessed land** | B, C, D, E, F | "Siege of Lang Ya" (B, 1ª aparição), "Defesa de Lang Ya — quarta onda" (C), "campanha de Heavenly Court contra Lang Ya" (D), "Cerco de Lang Ya" (E), "as sete ondas" como histórico (C, F) | `19` (é o caso-modelo de "cofre sem dono assediado em ondas") |
| **Hu Immortal / Dang Hun / Tian Ti** | A, B | "Hu Immortal Inheritance" (A), "Sixth Earthly Calamity" e "Assault on Hu Immortal Blessed Land" (B) | herança em `10`; calamidade em `21`; assalto em `19` |
| **Tai Qiu / herança de wisdom path** | B, C | "Scramble for the Wisdom Path Inheritance at Tai Qiu" (B), "Disputa pela herança em Tai Qiu e saque de Jade Pool" (C) | `08` (a regra da aura fraca) e `12` (Tai Qiu como área feroz) |
| **Starry Sky grotto-heaven** | B, C | "Expedition into Starry Sky Grotto-Heaven" (B, ainda inteiro), "O estilhaçamento do Starry Sky e a corrida pelos fragmentos" (C) | `11` (fragmentos) e `12` (a expedição à abertura órfã) |
| **Ciclo decenal do Norte** | B, C | "Great Blizzard", "Heroes Assembly", "Imperial Court Contest", "Great Battle of Northern Plains", "Eighty-Eight True Yang Building", "True Inheritance Secluded Domain" (todos B); ecos em C | `14` (o ciclo) + `15` (o edifício) |
| **Imperial Court contest** | B, E, F | "Imperial Court Contest" (B), "Northern Plains Imperial Court Contest" como histórico de escala mortal (E), "instituição encerrada" (F) | `14` |
| **Convenção do Caminho de Refino** | C, E | "Refinement Path Convention" (C, edição normal), "Central Continent Refinement Path Convention" (E, a edição sabotada durante a guerra) | já tem nota própria em `06 - Economia e Vida`; a **edição sob ataque** entra em `25` |
| **Yi Tian Mountain** | A, C, D, E | "Grande Batalha Justo-Demoníaca de Yi Tian" anunciada (A), "gambling contest" + "armadilha, fase imortal" (C), "cerco permanente ao giant dream realm" + "Batalha do Domínio de Sonho" (D), "doutrina das formações autônomas" (E) | `16` (a nota cobre a montanha inteira, nas duas eras) |
| **Blood Plain Martial Competition** | C, D | "Blood Plain Martial Competition" (C, montagem), "blood battle martial competition" (D, curso e fim) | `07` |
| **A Grande Era** | D, E, F | "a chegada da Grande Era" + "terremotos das veias da terra" (D), "The Great Era / fusão das cinco regiões" (E), "Dez Terras" e "qi tides" (F) | `24` |
| **Marés de qi** | E, F | "as marés de qi" (E), "qi tides" + "qi harvest fruit" (F) | `24` |
| **Guerra das grotto-heavens dos dois céus** | E, F | "Aliança dos Dois Céus e a primeira invasão vinda de fora" (E), "War of the Two Heavens" (F) | `27` |
| **Aliança de raças variantes** | C, E, F | "A Aliança das Quatro Raças" (C), "Aliança dos Dois Céus" (E), "Aliança dos Dois Céus" (F) | `27` (o bloco) e `06` (o rito de fundação) |
| **Crazed Demon Cave** | C, F | "Crazed Demon Cave" como área feroz de nove camadas (C), "Expedition to Crazed Demon Cave / Battle of the Three Great Worlds" (F) | `26` |
| **Earth Trench / subsolo** | C, D, F | "Expedição ao Earth Trench" (C), trincheiras abertas pelos terremotos (D), "Earth Treasury e as Dez Terras" (F) | `12` (exploração) e `24` (a origem) |
| **Divine Bean Palace** | D, E | "A disputa pelo Divine Bean Palace" (D), "A batalha do Divine Bean Palace" como histórico (E) | `08` |
| **Espólio de imortal morto / terras órfãs** | C, F | "O espólio de um Gu Immortal morto" (C), "extermínios de superforças" (F) | `18` |
| **Zombie Alliance** | B, C, D | "Zombie Alliance e Snowy Mountain Alliance" (B), "Yu Lu / aliança do Eastern Sea" (C), "campanha de extermínio da Zombie Alliance" (D) | `29` (histórico) |
| **Guerra caótica das cinco regiões** | B, C, D, E, F | sempre citada, **nunca mostrada** | `28` |
| **Dream realms** | B, C, D, F | "abertura da era dos Dream Realms" (B), "dream realm no Starry Sky" (C), "exploração de dream realms" (D), "heaven path dream realms" (F) | `16` (o cercado de Yi Tian) e `27` (os de heaven path) |
| **Treasure Yellow Heaven** | B, C, D, F | "mercado permanente dos imortais" (B), "Aberturas do Treasure Yellow Heaven" (C), "guerra de preços do year Gu" (D), "mercado aberto de refino" (F) | `22` |
| **Leilões e convenções de imortais** | A, B, D, E | leilão de liquidação e Shang clan city (A), "Grand Auction of Northern Plains" (B), "Eastern Sea Trading Convention" (D), "Qi Sea Banquet" (E) | `05` (mortal) e `22` (imortal) |
| **Tribulação de ascensão** | B, C, D, F | "Immortal Ascension Tribulation" + "Formless Hand" (B), "calamidades e tribulações" (C), "a ascensão a Gu Imortal" (D), "Trend of immortal ascension" (F) | `21` |
| **Caçadas coletivas** | B, D, E | mandados de captura (A), "caçada continental" (D), "caçada coletiva regional a um imortal demoníaco" (E) | `17` |
| **Paredes regionais** | C, D | "Earth tide e a travessia das paredes regionais" (C), "As paredes regionais: travessia e emboscada" (D) | `17` |
| **Chaos in Northern Plains / queda de superforça** | C, D | "Chaos in Northern Plains" (C), "destruição de uma tribo-superpotência" (D, histórico) | `18` |
| **Reverse Flow River** | D, F | "A prova do Reverse Flow River" (D), "A Reverse Flow River battle" (F, histórico) | `20` |
| **Emperor City** | E | fossa que a engole + versão do mundo-pintura | `25` (a fossa) e `28` (a cidade-pintura depois) |

**Falsos duplicados (registrar para ninguém fundir por engano):**

- A **maré de lobos de Qing Mao** (A) e as **marés de bestas** genéricas (C, F) não são o
  mesmo evento: a primeira é um caso concreto de um ciclo trienal específico; a segunda é
  a categoria.
- **Lang Ya blessed land** e **Hu Immortal blessed land** são dois lugares diferentes, os
  dois sitiados, os dois com calamidade decenal. Não confundir.
- **Yi Tian Mountain** (Fronteira Sul) e **Yi Tian Village** (a aldeia-fortaleza erguida
  sobre ela) são o mesmo lugar em fases diferentes.
- A **Convenção do Caminho de Refino** de C (caps. 828-859) e a de E (caps. 1698-1941)
  são **duas edições distintas** da mesma instituição — a segunda acontece sob guerra.
- O **Imperial Court contest** do Norte (B) e o **Imperial Court** citado em F como
  "instituição encerrada" são o mesmo torneio, séculos depois.

---

## 4. As notas planejadas

Formato de cada bloco: **nome de arquivo exato** · o que cobre · fontes brutas ·
faixa de rank dos personagens · o que a torna jogável.

### LOTE 1 — A vila e o clã mortal (rank 1-3)

Redator do lote 1: seis notas. É a porta de entrada da pasta e o material que uma mesa
iniciante usa nas primeiras sessões. Tom: concreto, doméstico, com números pequenos.

---

**`02 - A Maré de Lobos de Qing Mao Shan.md`**

- **Cobre:** o evento único mais completo da obra para uma mesa iniciante — o ciclo trienal
  de maré de lobos numa montanha da Fronteira Sul, do prelúdio ao rescaldo: a maré pequena
  anômala como aviso datado; os sinais de inverno; a negociação de aliança entre três clãs;
  a economia de guerra (quadro de méritos, dez pontos por olho de lobo, ranking por grupo
  pequeno atualizado em tempo real); os cercos às vilas; a escalada de reis-fera até o
  lycan estrategista com o Gu de fumaça de cem li de raio; a fraqueza explorável (visão de
  águia, olfato humano); a intervenção de rank 5 externo que **expulsa em vez de matar**; e
  o rescaldo (metade da população varrida, política congelada, vagas abertas).
- **Fontes:** **A**, entradas "Small beast tide / small beast horde de Qing Mao Mountain"
  (caps. 93-97), "The Wolf Tide / Great Wolf Tide" (caps. 111-112, 121-199), "Assembleia de
  Aliança dos Três Clãs" (caps. 123-127) e "Battle Merit Board" (cap. 127). Complementar
  com "Ciclo das marés de bestas" (A, caps. 31, 93, 118, 122) só para a regra de
  fortificação.
- **Faixa de rank:** 1 a 3.
- **Por que é jogável:** dura mais de um ano, tem calendário previsível, escalada clara,
  uma tabela de recompensas embutida com placar público, uma aliança forçada com regras
  escritas que rendem enredo social, e **congela a política interna** — o que dá aos
  jogadores licença para agir. Cabe uma campanha inteira, não uma sessão.

---

**`03 - Marés de Bestas.md`**

- **Cobre:** a categoria. Como uma maré se forma (instinto territorial + inverno + expulsão
  de velhos pelo rei-fera); a periodicidade ("a cada poucos anos"; três anos em Qing Mao);
  a escalada padrão (maré pequena → ondas → maré grande com reis-fera); **a regra de
  diagnóstico**: uma maré natural é de uma espécie só — espécies misturadas que não se
  atacam significam desastre humano, não natural; a defesa como engenharia (muros com
  Steel Vine e Poison Flower Gu, fossos, torres, três camadas, formação de evacuação,
  desviar um rio contra lobos-tartaruga, cavar túnel contra aves); o limite de crescimento
  urbano; a maré dirigida como arma de guerra negável; o desastre das grous em campo aberto
  (o contraponto: sem muro não há defesa); a maré como álibi social; e as marés de escala
  imortal nas áreas ferozes, onde não se luta contra a maré, anda-se junto com ela.
- **Fontes:** **A** "Ciclo das marés de bestas", "Crane Disaster"; **B** "Turtleback Wolf
  Group e Night Wolf Group"; **C** "Marés de bestas (caps. 850, 1034-1036, 1085-1093)";
  **F** "Beast tides" (caps. 2046, 2081-2082, 2220, 2287) e a maré do mundo-pintura.
- **Faixa de rank:** 1 a 5.
- **Por que é jogável:** entrega o encontro grande mais barato do cenário — cerco de aldeia
  com contramedida específica por tipo de horda, cronômetro dado pela distância do bando, e
  uma pista investigativa embutida (a maré errada denuncia um culpado).

---

**`04 - Desastres Locais e Problemas Crônicos.md`**

- **Cobre:** os acontecimentos que caem sobre uma comunidade pequena e são grandes demais
  para ela. Quatro casos-modelo: **(a)** a criatura de rank 5 no lugar errado — o sapo que
  entope o rio, que não pode ser ferido, só realocado, e cujo erro afoga uma região e
  antecipa uma maré de bestas; **(b)** o furacão anual que um dia vence a defesa e destrói
  a nascente espiritual, extinguindo um clã de séculos, com a onda de refugiados e o leilão
  de liquidação como consequência direta; **(c)** a rota comercial cronicamente infestada —
  a montanha dos zumbis, com o ciclo de infecção que se realimenta, a hierarquia legível
  por cor de pelo, o custo de cura de meia pedra primeva por arranhão e o esquadrão anual
  que todos sabem que não resolve; **(d)** o terreno proibido debaixo dos próprios pés —
  colher o recurso que sela o lugar é o que o destranca; a caverna de lago de sangue, o
  espaço semi-selado onde uma luta com fogo consome o ar, e a regra de que dois rank 5
  brigando é um mapa a atravessar, não uma batalha a vencer.
- **Fontes:** **A** "River Swallowing Toad", "A destruição do clã Ju pelo furacão de Ju Feng
  Mountain, e o leilão de liquidação", "Mu Bei Mountain, a montanha dos zumbis",
  "Blood Pond Graveyard".
- **Faixa de rank:** 1 a 3.
- **Por que é jogável:** quatro sessões fechadas, curtas e de tom diferente entre si — uma
  de engenharia sem violência, uma de evacuação e rescaldo econômico, uma de travessia com
  economia de recursos, uma de fuga e terror. Todas rodam com personagens que ainda contam
  pedras primevas uma a uma.

---

**`05 - Feiras, Caravanas e Festivais.md`**

- **Cobre:** o calendário social do mundo mortal como cenário. A **caravana mercante anual**
  (três dias e três noites, uma vez por ano, o cardápio da feira, a casa de aposta em
  fósseis, a loja de lance cego com confidencialidade garantida, os preços-âncora, e a
  regra do mundo de por que **não existe leilão dentro de uma vila-clã**); a **grande
  caravana de longa distância** como sociedade móvel com linhas de defesa politicamente
  disputadas; a **cidade-clã** como máquina de eventos (anéis com pedágio, zona de batalha
  com escada de vitórias líquidas, zona de leilão); a **Festa Auspiciosa** onde os convites
  simultâneos transformam a escolha de banquete em declaração pública; e o **Festival da
  Lua**, com as três provas (chá, poesia, abrir pedras), a ordem dos assentos como recado e
  a versão mortal da mesma noite.
- **Fontes:** **A** "A caravana mercante anual", "A grande caravana de longa distância",
  "Shang Clan City", "Auspicious Festival"; **D** "Moon Festival"; **E** "Sea God Ceremony"
  (a versão de um povo variante, com as pérolas e as três músicas).
- **Faixa de rank:** 1 a 4.
- **Por que é jogável:** sessões inteiras sem iniciativa nem dano, com consequência política
  real três sessões depois; e é onde uma mesa pobre encosta pela primeira vez no mundo
  grande.

---

**`06 - Assembleias, Alianças e Quadros de Mérito.md`**

- **Cobre:** como o mundo negocia quando é obrigado a cooperar. A **assembleia de aliança**
  (o lugar fixo consagrado por gerações, as semanas de travamento na divisão de custos, as
  contendas de Gu como exercício militar e ficha de barganha, o torneio de sparring que
  para antes da morte, a assinatura das regras); as **regras de um pacto de guerra**
  (proibição de matar entre aliados, grupo investigador dedicado, entrega obrigatória de Gu
  tirado de cadáver, pena de morte com a família respondendo); a **assembleia dos heróis**
  do Norte (desafio que não se pode recusar, reféns e casamentos como fichas, o pária que
  se vende à melhor facção); o **quadro de méritos** nas suas duas escalas (prova física por
  abate na vila; auditoria por Gu de captura de imagem em quinze tendas na guerra grande,
  com mercado onde gastar e medo real de desvio); a **fundação de uma aliança regional** e a
  rede de torres-farol que a materializa (cem torres ≈ uma casa imortal; a rede treme
  inteira quando uma cai); e o **rito de fundação de uma aliança de povos oprimidos**, com
  hierarquia definida por poder militar bruto.
- **Fontes:** **A** "Assembleia de Aliança dos Três Clãs", "Battle Merit Board", regras de
  aliança dentro de "The Wolf Tide"; **B** "Heroes Assembly", "The Great Battle of Northern
  Plains" (o Battle Merit Board detalhado); **C** "A Aliança das Quatro Raças"; **E**
  "Fundação da Southern Alliance" (torres-farol).
- **Faixa de rank:** 1 a 5.
- **Por que é jogável:** transforma diplomacia em mecânica — cada vitória dos jogadores no
  palco vale concessão na mesa lá em cima, e o placar público converte tudo o que a mesa faz
  em moeda gastável numa loja.

---

**`07 - Torneios, Arenas e Duelos.md`**

- **Cobre:** a competição formal em todas as escalas. **Escala de clã:** a competição entre
  três clãs que substitui uma negociação fracassada — cem li de arena, do anúncio ao pôr do
  sol, trinta fichas para classificar, sem limite de participantes, sem proibição de matar,
  e o texto admitindo que não é justa. **Escala urbana:** a escada de arenas de uma
  cidade-clã (oitenta arenas com terrenos diferentes, promoção por vitórias líquidas, o
  vencedor leva um Gu do perdedor, um desafio irrecusável por mês, e o viés que suprime
  força bruta no nível alto). **Escala não violenta:** a prova de sucessão por comércio (cem
  mil pedras, três meses, régua histórica de resultados, atalho ilegal que já derrubou
  gente melhor) e as competições de poesia (dezoito rodadas, três chances, e gente que
  vomita sangue por compor no limite). **Escala imortal:** o duelo formal que substitui a
  guerra entre clãs justos (condição de término negociada antes, local descartável, recusar
  é covardia pública) e o torneio de campeões que é um compromisso encenado entre dois rank
  8 que nunca vão pisar no palco. **Escala de povo:** a sucessão por combate com endosso
  popular prévio por reputação.
- **Fontes:** **A** "Three Clans Competition", "Shang Clan City / Battle Zone", "A Competição
  de Jovem Mestre do clã Shang"; **C** "Blood Plain Martial Competition", "Sucessão do rei
  dos feathermen"; **D** "Blood Plain Martial Competition" (curso e fim), "O 'spar'";
  **E** "Ten Great Scholars Selection"; **F** "World poetry competition", "Public challenge
  duels with staked wagers".
- **Faixa de rank:** 1 a 7 (a nota organiza-se por escala crescente).
- **Por que é jogável:** entrega quatro formatos de arena prontos com regras curtas e
  consequências longas — e a virada mais bonita da obra: descobrir que o resultado macro do
  torneio já foi combinado por cima.

---

### LOTE 2 — Heranças e masmorras (rank 2-5)

Redator do lote 2: seis notas. É o núcleo "módulo de aventura" da pasta.

---

**`08 - Aberturas de Herança.md`**

- **Cobre:** a categoria e seus formatos recorrentes. O **anúncio impossível de esconder**
  (pilares de luz visíveis a enorme distância); a **janela periódica** ("abre a cada sete
  dias, e da porta saem insetos") e o acampamento permanente de candidatos que se forma em
  volta; a **herança escondida em objeto sem valor** que exige um Gu Master de avaliação; a
  **herança no covil de uma fera**; a **herança que exige duas qualificações independentes**;
  a **defesa póstuma** (véu de sangue que drena quem se aproxima, exército de feras
  fantasma, vontades acumuladas de todos os candidatos mortos ao longo de gerações); o
  **relógio invertido** (quanto mais o cerco demora, mais o herdeiro absorve); a **regra da
  aura fraca** — numa área feroz, a aura de um Gu Imortal provoca as feras e a de um mortal
  não, então só personagens fracos entram e os poderosos esperam do lado de fora; a
  **charada de um espírito da terra** cuja condição literal é uma armadilha e cuja condição
  real é de caráter; a **aposta hereditária** aberta a linhagens rivais com gradiente de
  recompensa por profundidade e recomendação explícita de não levar tudo; e o **mercado em
  volta** (informação sobre o interior valendo centenas de milhares; os Gu de entrada
  triplicando de preço da noite para o dia).
- **Fontes:** **A** "White Bone Inheritance", "Three Kings Inheritance" (só as fases externas
  e a economia); **B** "The Scramble for the Wisdom Path Inheritance at Tai Qiu",
  "Inheritance grounds com janela periódica"; **C** "Disputa pela herança de wisdom path em
  Tai Qiu"; **D** "A disputa pelo Divine Bean Palace"; **E** "Five Xiang's Bet"; **F**
  "Sand Heap blessed land" (a charada do espírito da terra e a etiqueta de disputa).
- **Faixa de rank:** 2 a 5.
- **Por que é jogável:** é o encontro-padrão da obra e o mais fácil de multiplicar — janela
  curta, horda que sai junto com a porta, rivais acampados esperando a mesma janela, e um
  prêmio que ninguém consegue medir de fora. Faz par com `07 - Heranças e Provações`, da
  pasta `06`, que explica a instituição; esta descreve como é estar dentro.

---

**`09 - A Herança dos Três Reis.md`**

- **Cobre:** o maior acontecimento regional da faixa inicial da obra e o mais original
  mecanicamente. Fora: a corrida do ouro (pânico de compra dos três Gu de entrada, ocupação
  tirânica das entradas pelo clã mais forte, acampamento permanente onde justos e demoníacos
  se toleram, banquetes e desafios públicos). Dentro: **entra-se com um único Gu de rank 1 e
  nada mais**; cada entrante cai num ponto diferente, então grupos se separam; a estrutura em
  rodadas, em que a única forma de crescer é ganhar mais uma cópia do mesmo Gu; a névoa
  entre rodadas com três silhuetas luminosas indicando três rotas de risco diferente; o
  salto de dificuldade a cada dez rodadas; os outros Gu Masters lá dentro, também
  desarmados, e o atalho de saquear a abertura de quem cair. E o relógio: a terra abençoada
  está morrendo, as janelas encurtam, os pilares afinam e **a supressão cede em degraus** —
  a recompensa cresce na mesma curva do perigo. Fecha com a batalha final na névoa, onde
  quem defende enxerga e quem ataca não, cada grupo é uma coluna com uma rota designada, a
  rota está errada, e voltar significa encarar o comandante que já executou um insubordinado.
- **Fontes:** **A** "Three Kings Inheritance / San Cha Mountain" e "A Guerra da Névoa".
  As regras de mundo sobre terras abençoadas moribundas (calamidade decenal, espírito da
  terra, vento da assimilação) vão para `21`, com remissão.
- **Faixa de rank:** 2 a 4.
- **Por que é jogável:** é o módulo mais pronto da obra — masmorra de mecânica invertida, em
  que o rank importa menos que a perícia, com uma camada externa de economia e política que
  roda em paralelo para quem não quiser entrar.

---

**`10 - A Subida da Montanha Dang Hun.md`**

- **Cobre:** a herança íntegra de uma imortal, no Continente Central, e o torneio que a
  antecede. **Metade um:** as dez grandes seitas emitem simultaneamente a ordem de organizar
  um torneio entre discípulos de elite "para fixar um ranking" — e o ranking, que parecia
  prestígio, é a ordem de entrada. **Metade dois:** a subida. Todos os Gu selados, inclusive
  os de movimento — sobe-se com o corpo; tempo cinco vezes mais rápido lá dentro, o que
  converte segundos de fila em dias de escalada; uma montanha de cristal que ataca a alma
  com intensidade crescente rumo ao topo; **prêmio único e zero consolação**; e, por ser
  herança de caminho correto, o espírito da terra suprime a montanha e não há morte — quem
  não aguenta é expulso. Mais as regras de por que os poderosos não entram: um Gu Imortal
  que invade sofre contra-ataque, e o espírito da terra pode se autodestruir levando tudo
  junto; e a regra não escrita de que interferir de fora é permitido enquanto não quebrar
  as regras do jogo.
- **Fontes:** **A** "Hu Immortal Inheritance / Tian Ti Mountain" (caps. 365-375).
- **Faixa de rank:** 3 a 5, ou jovens de elite de qualquer rank.
- **Por que é jogável:** uma prova sem combate, sem Gu e sem morte — raríssimo neste mundo.
  Só corpo, vontade e alma contra um relógio em que cada dia perdido são cinco, e em que
  ajudar um rival custa posição.

---

**`11 - Os Cacos do Céu Estrelado.md`**

- **Cobre:** um mundo antiquíssimo se despedaça e seus fragmentos caem espalhados como
  meteoros. A regra que define tudo: os mundos-fragmento têm marcas do Dao esparsas e estão
  rasgados; como um Gu Imortal *é feito* de marcas do Dao, entrar num fragmento é um gigante
  entrando numa casinha — a casa quebra e o tesouro se destrói junto. **Nenhum imortal pode
  entrar; só discípulos mortais.** A organização da corrida: as dez grandes seitas negociam
  **horários e turnos de entrada**; cada uma monta uma equipe de elite cujo cultivo foi
  elevado de propósito; o contrato típico traz missões nominais ("capture estes três,
  de preferência vivos"), pagamento de um terço do valor e escolha de uma das presas. O
  bestiário de encomendas (o peixe-dragão desolado cuja carne é comida universal de Gu; a
  tartaruga que petrifica e vira colina falsa; a erva que converte o ecossistema inteiro).
  E a imagem que sustenta a cena: de dentro, o chão racha como espelho e, pelas rachaduras,
  veem-se os poderosos lá fora, observando, impotentes.
- **Fontes:** **C** "O estilhaçamento do Starry Sky grotto-heaven e a corrida pelos
  fragmentos" (caps. 908-916, 983). Antecedente útil (o lugar ainda inteiro) em **B**,
  "Expedition into Starry Sky Grotto-Heaven" — mas o interior detalhado dele vai para `12`.
- **Faixa de rank:** 3 a 5.
- **Por que é jogável:** é o pedido do usuário em estado puro — personagens fracos dentro de
  um acontecimento gigantesco, com hora marcada de entrada e de saída, lista de encomendas,
  equipes rivais no mesmo caco, e a tensão dramática vindo de graça: nenhum adulto pode
  entrar.

---

**`12 - As Terras Ferozes e o Subsolo do Mundo.md`**

- **Cobre:** onde um grupo fraco vai buscar fortuna num mundo já repartido. A regra que as
  justifica: as grandes forças já dividiram entre si todos os recursos, e o que sobrou foram
  as áreas ferozes — o que restou é o que é perigoso demais para ser repartido. As
  características comuns (feras desoladas em massa, marés que denunciam quem está lá, nem
  super forças montam base dentro). Os exemplares: a selva de grama gigante em que um talo
  equivale a uma árvore centenária; a caverna de nove camadas que só *parece* área feroz; a
  trincheira vertical cujo interior alarga até comportar setenta cidades, onde só a faixa
  rasa é ocupada apesar de séculos de esforço; o mar de correntes feitas de materiais vindos
  de lugares diferentes do mundo, com bolhas contendo mundos inteiros; e a abertura imortal
  órfã como masmorra clássica (salões com defesas em camadas nomeadas, mapa que mente,
  equipe rival lá dentro, reinos de sonho no fundo que se alimentam do desejo da presa). E,
  no mundo tardio, as **Dez Terras** do subsolo unificado: o abismo de mais de cem camadas,
  a ilha-veículo que viaja pela veia da terra sem controle de direção, a cripta natural de
  materiais extintos, a terra-túmulo cujas lápides puxam a vida inteira de um morto do rio
  do tempo.
- **Fontes:** **B** "Expedition into Starry Sky Grotto-Heaven" (a masmorra), "The Scramble
  ... at Tai Qiu" (a regra da área feroz); **C** "As dez grandes áreas ferozes de Northern
  Plains", "Expedição ao Earth Trench", "Turbulent flow sea area"; **F** "Earth Treasury e
  as Dez Terras".
- **Faixa de rank:** 3 a 7 (a profundidade é o dial de dificuldade).
- **Por que é jogável:** é a resposta canônica para "onde meu grupo de rank 3 vai achar
  tesouro", com um mostrador de dificuldade contínuo, guias e mapas como o recurso mais
  caro, e escoltas mais fortes que os jogadores e com agenda própria.

---

**`13 - O Paraíso da Baleia-Dragão e o Obelisco de Mérito.md`**

- **Cobre:** a herança que é um sistema de missões completo. A prova de entrada por ilusão
  coletiva em que morrer não mata; a ilha inicial onde **qualquer Gu com intenção de luta
  simplesmente falha** (mas curar não é obstruído), regra que vale até para o mais forte; o
  registro no obelisco com o risco embutido de revelar o nome verdadeiro; as faixas de
  missão com valores declarados; os **títulos como chaves** que destravam faixas superiores
  e podem ser deduzidos; o placar público atualizado em tempo real; os pontos negativos; o
  prazo de trezentos dias, findo o qual todos são expulsos — e quem fez inimigos lá dentro
  os reencontra do lado de fora, sem proteção; a proibição de conversar diretamente e o
  mural de recados improvisado ao pé do obelisco; e a natureza das missões, que **premiam
  consertar o mundo**: pacificar um monstro rende muito mais que matá-lo, e levar o cadáver
  embora reduz a recompensa porque as marcas do Dao do corpo elevariam a fundação do lugar.
- **Fontes:** **E** "Dragon Whale Paradise e o Merit Obelisk" (caps. 1648-1674, 1888-1919).
- **Faixa de rank:** escalável — na obra é 6 a 8, mas o sistema roda em qualquer faixa se o
  redator disser como reescalar as missões. Registrar isso explicitamente como `(ded.)`.
- **Por que é jogável:** é um quadro de missões canônico, copiável quase sem adaptação, que
  resolve sozinho o problema de "por que meu grupo faria o bem num cenário amoral" — aqui
  fazer o bem *é* a moeda, e o placar é público.

---

### LOTE 3 — Ciclos regionais, guerra e queda (rank 2-5)

Redator do lote 3: cinco notas. É onde a mesa deixa de reagir e passa a ter carreira.

---

**`14 - O Ciclo Decenal das Planícies do Norte.md`**

- **Cobre:** a máquina de dez anos que sincroniza o calendário político de uma região
  inteira. **(1)** A grande nevasca decenal — numa estepe sem montanhas não há abrigo
  natural; durante ela aparecem Gu selvagens fortes em massa; ela destrói qualquer herança
  deixada ao ar livre (e é por isso que todas as heranças do Norte estão guardadas dentro de
  uma terra abençoada); depois dela, tribos grandes viram médias e médias viram pequenas.
  **(2)** A assembleia dos heróis, simultânea em todas as regiões famosas, com desafios
  irrecusáveis usados para consumir os especialistas do rival um a um, e não participar
  sendo suicídio político. **(3)** A guerra entre as alianças formadas, com o desafio de
  campeões antes da carga e as suas quatro funções declaradas, o quadro de méritos auditado
  e a supressão regional que rebaixa um Gu refinado noutra região. **(4)** A entrada na
  terra abençoada: Gu Imortais proibidos, privilégio de linhagem, talismã que se autodestrói
  se sair, terreno que se regenera quando o torneio fecha, e a maioria dos participantes
  vagando à procura de heranças menores enquanto os grandes disputam o palácio. **(5)** O
  contest em escala puramente mortal, com exércitos, muralhas de duzentos li de perímetro
  que resistiram a dezenas de assaltos, e glória individual vitalícia.
- **Fontes:** **B** "The Great Blizzard of Northern Plains", "Heroes Assembly", "Imperial
  Court Contest e Imperial Court (Wang Ting) blessed land", "The Great Battle of Northern
  Plains"; **E** "O Northern Plains Imperial Court Contest" (histórico, escala mortal);
  **F** "O Imperial Court contest" (a instituição vista de fora, séculos depois, e o
  ressentimento que deixou).
- **Faixa de rank:** 2 a 5.
- **Por que é jogável:** é o melhor relógio de campanha da obra — uma contagem regressiva de
  dez anos que obriga toda facção a se mexer e que reseta o mapa político no fim de cada
  ciclo, com uma fase social, uma militar e uma de exploração.

---

**`15 - O Edifício dos Oitenta e Oito Andares.md`**

- **Cobre:** a masmorra institucional que se remonta a cada ciclo. O mecanismo: o prédio
  **saqueia a região inteira**, puxa os recursos preciosos para cima e condensa andar por
  andar, e cada formação de andar é literalmente um novo processo de refino — absorve o Gu
  mais forte disponível e o transforma na rodada final, depois o seguinte, e assim por
  diante; por isso **dificuldade e prêmio andam juntos por construção**, porque o Gu que
  forma a rodada *é* o prêmio dela. As regras jogáveis: cada rodada é um cenário fechado com
  um quebra-cabeça próprio; a avaliação em três graus (baixo = recompensa mínima e segue;
  médio = o dobro mais informação antecipada sobre a próxima rodada; alto = o dobro do médio
  mais transporte para a câmara do tesouro, onde nada é de graça, tudo é trocado); os
  talismãs de convidado, de uso único, que derretem na mão e viram mercadoria de preço
  absurdo; o talismã de dono que evolui por gumes e dá ao portador incentivo para abrir o
  prédio a uma multidão; e a regra política mais rica — **a recompensa pertence a quem limpa
  a rodada**, não ao chefe, o que torna "chamar o especialista de fora" uma decisão cara. E
  o clímax: o domínio das heranças verdadeiras, com três graus legíveis pelo tamanho do
  grumo de luz, um teste próprio por herança, e o relógio cruel — cada contato acelera as
  heranças e o espaço encolhe, até que quem hesitou não consegue mais pegar nem a menor e
  continua correndo risco de vida.
- **Fontes:** **B** "Eighty-Eight True Yang Building" e "True Inheritance Secluded Domain".
- **Faixa de rank:** 2 a 5.
- **Por que é jogável:** cada rodada é um encontro autocontido com condição de vitória em
  três níveis — os jogadores decidem toda hora se aceitam o passe baixo e seguem, ou se
  arriscam a morte por um passe alto; e o clímax é risco-contra-ganância cronometrado, sem
  inimigo pensante.

---

**`16 - A Montanha Yi Tian.md`**

- **Cobre:** o mesmo lugar em duas eras, e o achado mais importante da pasta em cada uma.
  **Era um — a zona proibida a imortais.** Uma casa imortal enterrada vaza uma zona onde a
  abertura de um Gu Imortal é comprimida: quanto mais fundo, mais fraco, até a abertura ser
  destruída em cinquenta ou sessenta passos. Como nenhum imortal pode pisar no campo,
  dezenas deles negociam por sete dias e sete noites um contrato de apostas: cada um aposta
  bens, e a aposta define **de que rank pode ser o seu peão mortal e quando ele entra**; ao
  fim, o bolo inteiro é redistribuído por desempenho, e trapaça custa confisco total. Os
  peões são Gu Masters de rank 3 a 5, equipados por patronos que não podem socorrê-los. Em
  volta, uma aldeia-fortaleza demoníaca sitiada por clãs justos, com a condição declarada de
  **aguentar cem dias**. **Era dois — o domínio de sonho cercado.** Décadas depois, uma
  batalha gigantesca deixa no lugar um domínio de sonho, e treze super forças o cercam com
  uma formação de quatro camadas concêntricas que tem **cidade habitável dentro**, dividida
  em treze setores. O peso político de cada clã é o número de Gu Imortais que ele plantou na
  formação; existe um mercado negro de acesso com quadro de nomes e fila de espera, tolerado
  porque cada clã junta provas contra o outro; e o tesouro central é inacessível de
  propósito. Depois, o assalto: camadas abandonáveis em sequência, pilar quebrado e reparado
  sob fogo com o mestre de formação indefeso durante o processo, treze comandos separados
  sem general único, e moral tratada como mecânica declarada.
- **Fontes:** **C** "Battle of Yi Tian Mountain / gambling contest" e "A armadilha de Yi Tian
  Mountain — a fase imortal"; **D** "O cerco permanente ao giant dream realm de Yi Tian
  Mountain" e "A Batalha do Domínio de Sonho"; **A**, o anúncio antecipado da grande batalha
  justo-demoníaca, só como contexto; **E** "A batalha de Yi Tian Mountain e a doutrina das
  formações autônomas" (a consequência doutrinária).
- **Faixa de rank:** 3 a 5 na primeira era; 6 a 7 na segunda.
- **Por que é jogável:** a primeira era é o cenário desenhado para personagens fracos — cem
  dias de cerco em que ninguém acima do rank 5 pode pisar no campo e os jogadores descobrem
  que são peças de aposta. A segunda é a melhor base de campanha da obra: treze facções
  rivais convivendo numa cidade fechada, com corrupção conhecida e tolerada.

---

**`17 - Caçadas, Emboscadas e Fugas.md`**

- **Cobre:** o formato mais reutilizável do cenário, jogável dos dois lados. **Como se acha
  alguém:** dedução a partir de fragmentos de informação; tabuletas de vida e lanternas de
  alma que denunciam morte e posição na hora; disfarces que falham por acúmulo de detalhes;
  prisioneiros como melhor fonte. **O que atrapalha:** as paredes regionais obstruem a
  dedução, e estar a duas paredes de distância torna o risco baixíssimo. **A composição de
  uma força-tarefa**, por funções e não por poder bruto: líder, defensor-detector sem
  ataque, caçador experiente, combatente híbrido, especialista em alma, portador da
  contramedida específica que anula o método de fuga do alvo — e, quase sempre, um infiltrado
  de outra potência. E a doutrina evoluindo entre a primeira e a segunda tentativa: dois
  chefes, um visível e outro disfarçado de subordinado. **A emboscada na parede regional:**
  o alvo a cinquenta ou sessenta por cento da força, punido se usar golpes, isolado, longe
  de socorro e obrigado a passar por ali; mais a janela anual em que a parede afina e a rota
  mapeada vira mercadoria perecível. **A fuga:** formações de teleporte que só funcionam com
  vários coordenados e treinados juntos, trocar de região, trocar de identidade, vender no
  mercado anônimo. E a versão barata do mesmo formato: o mandado de captura com dois preços
  distintos, informação e morte, e o seu ponto fraco embutido — mandados funcionam mal
  contra quem é anônimo e se move.
- **Fontes:** **A** "Arrest warrants"; **C** "Earth tide e a travessia das paredes
  regionais"; **D** "A caçada continental", "As paredes regionais: travessia e emboscada";
  **E** "Caçada coletiva regional a um imortal demoníaco", "A emboscada da Heavenly Court no
  Western Desert".
- **Faixa de rank:** 3 a 7.
- **Por que é jogável:** dá ao mestre uma força perseguidora com composição legível e ao
  grupo uma lista concreta de contramedidas — e funciona igualmente bem com a mesa no papel
  de caçada ou de caçadora.

---

**`18 - Quando uma Força Morre.md`**

- **Cobre:** o rescaldo como cenário, em três escalas. **Escala de clã:** um clã centenário
  perde a nascente espiritual e deixa de existir; os remanescentes migram, os preços da
  cidade os obrigam a vender tudo, e séculos de acúmulo vão a leilão numa tarde com os
  herdeiros arruinados na plateia. **Escala regional:** uma super força é responsabilizada
  publicamente e não tem um rank 8 para dissuadir represálias — a regra do mundo é dita com
  todas as letras, um rank 8 é o que garante a existência de uma facção. Ela recolhe todos
  os seus imortais para a sede e deixa o território sem guarnição; segue-se uma temporada de
  rapina em que imortais pobres fazem **análise de risco de saque** (que território ninguém
  forte quer, quando ir, como sair), com uma tabela pronta de lugares a pilhar. **Escala de
  campo de batalha:** o vale onde a guerra acabou, entulhado de formações semiquebradas de
  dois lados sobrepostos, com o clima natural do lugar morto pela batalha, um vigia solitário
  e mal pago no portão, e um segredo enterrado que só abre com o item certo. E a regra que
  gera aventura indefinidamente: **o cadáver de um Gu Imortal tem dois usos**, e a abertura
  dele vira uma terra abençoada órfã cujo espírito da terra nasce da maior obsessão do morto
  e cobra o preço dela — quem matou o dono não tem prioridade nenhuma.
- **Fontes:** **A** "A destruição do clã Ju ... e o leilão de liquidação" (só o rescaldo; o
  furacão fica em `04`), "O aniquilamento conjunto dos três clãs de Qing Mao Mountain";
  **C** "Chaos in Northern Plains", "Cerco de Luo Po valley", "O espólio de um Gu Immortal
  morto: a corrida pelas blessed lands órfãs"; **D** "A destruição de uma tribo-superpotência
  e a fundação de uma nova"; **F** "Extermínios de superforças".
- **Faixa de rank:** 1 a 7 (a nota organiza-se por escala crescente).
- **Por que é jogável:** é um sandbox pronto de encontros entre iguais, sem chefe final: a
  mesa não derruba a potência, a mesa chega depois e disputa os restos com gente do mesmo
  tamanho.

---

### LOTE 4 — O mundo imortal (rank 5-8)

Redator do lote 4: cinco notas. Aqui a mesa não decide o desfecho — ela sobrevive dentro
dele e escolhe lados.

---

**`19 - Cercos e Invasões de Terras Abençoadas.md`**

- **Cobre:** como se ataca e como se defende um mundo privado. **Localizar:** de fora não se
  vê sinal nenhum de que uma terra abençoada existe; é preciso um vínculo com alguém de
  dentro — um parente de sangue, a alma de um infiltrado plantado ao longo de gerações, um
  prisioneiro interrogado por anos. **Abrir:** quebra-se o espaço como vidro, ao custo de
  dezenas de pérolas de essência num instante. **A janela:** a calamidade decenal do alvo,
  que abre buracos na casca — e, como a força da calamidade é proporcional à riqueza
  guardada, **a calamidade é ao mesmo tempo o anúncio público do tesouro e a única janela
  para roubá-lo**. **A guerra de atrito:** os sitiantes jogam uma pérola de essência por vez
  pelo buraco para forçar o defensor a gastar; espíritos da terra não produzem essência, só
  gastam, então toda terra sem dono vivo é uma ampulheta que uma coalizão paciente vira.
  **A supressão do invasor** e o Gu que a anula, com a diferença econômica entre a versão
  consumível e a ilimitada. **A legitimidade como recurso mais escasso:** uma seita precisa
  de pretexto público antes de precisar de força, e se o pretexto cair, as rivais entram
  juntas. **Camadas de defesa:** labirinto de névoa com doze núcleos fixos; formação de
  batalha antiga que funde vários imortais num só corpo; caldeirão que refina à força os Gu
  dos invasores e os coleciona; defesa de terra arrasada que consome a poupança de séculos e
  não distingue amigo de inimigo; e o lixo de calamidade amputado anos antes, deixado entrar
  primeiro como aríete. E o caso extremo: uma cidade voadora sitiada por três dias cuja fuga
  é um desejo gritado em coro por toda a população, que reaparece dentro da terra abençoada
  de um estranho — e o sistema do mundo a classifica como **calamidade terrena** daquele
  lugar.
- **Fontes:** **B** "Siege of Lang Ya Blessed Land", "Assault on Hu Immortal Blessed Land";
  **C** "Defesa de Lang Ya blessed land — quarta onda", "Campanha de invasão de Yu Lu blessed
  land", "Queda de Sacred Feather City e o êxodo dos feathermen", "As sete ondas de invasão
  a Lang Ya"; **D** "A campanha de Heavenly Court contra Lang Ya blessed land"; **E** "Cerco
  de Lang Ya blessed land"; **F** "As sete ondas de ataque a Lang Ya".
- **Faixa de rank:** 5 a 7 como defensores ou mercenários; mortais como população interna.
- **Por que é jogável:** dá quatro papéis de mesa que não exigem vencer ninguém — segurar um
  inimigo mais forte por trinta minutos, tapar buracos, evacuar a população, e caçar o
  vazamento que entregou a posição antes de o ataque começar.

---

**`20 - O Cerco da Montanha Nevada e o Rio de Fluxo Reverso.md`**

- **Cobre:** duas regras de mesa que se encaixam e que são o achado mais forte da faixa
  imortal. **O cerco:** uma super formação remodela a terra abençoada inteira; cada pico
  vira núcleo; quem invade é **teleportado à força para o pico compatível com seu rank**, e
  o senhor de cada pico não pode sair do seu — inclusive o rank 8, que **não pode descer
  para esmagar invasores de rank 6 e 7**. A formação amplifica quem defende no núcleo e
  suprime quem carrega ataque; aberturas imortais não abrem lá dentro; e **todo imortal que
  morre é convertido em sacrifício** que alimenta a formação, dos dois lados. As três
  fraquezas: não se quebra de frente, mas se destrói o terreno em que está enraizada; e quem
  a construiu plantou uma porta dos fundos que o dono nunca percebeu. **O rio:** quando a
  formação colapsa, todos caem dentro de um domínio recluso onde **nenhum Gu funciona** —
  Gu viram fósseis, aberturas não abrem, um cadáver de rank 8 é peso morto, e rank 7 e rank 8
  se batem a socos e mordidas tentando emergir para respirar. A correnteza sobe contra o
  viajante e nunca acaba; não existe saída pela nascente, porque cada passo cria uma
  extensão nova; ser varrido para trás elimina, e não só fisicamente; e o único modo de
  conquistá-lo é refinar dentro do próprio corpo um Gu de perseverança.
- **Fontes:** **D** "Siege of Snowy Mountain Blessed Land" e "A prova do Reverse Flow River";
  **F** "A Reverse Flow River battle" (só o mecanismo da derrota histórica, como contexto).
- **Faixa de rank:** 6 a 7 — e o rio é o único lugar da obra onde essa diferença quase não
  importa.
- **Por que é jogável:** são as duas melhores "regras únicas" do cenário. Uma proíbe o rank 8
  de tocar nos jogadores; a outra desliga o sistema de magia inteiro e pergunta o que sobra.
  Juntas dão uma sessão dupla em que rank 6 e 7 são protagonistas de uma guerra de rank 8.

---

**`21 - Calamidades e Tribulações como Cenário.md`**

- **Cobre:** o desastre mais frequente do mundo, escrito como situação e não como teoria —
  a teoria fica em `10 - Tribulações e Calamidades`, da pasta `01`, e esta nota remete a
  ela. **O calendário como mapa do tesouro:** toda terra abençoada enfrenta calamidade a
  cada dez anos e tribulação a cada cem, e a força é proporcional à riqueza guardada. **Como
  é por dentro:** a calamidade materializa inimigos dentro do mundo privado e vem em ondas
  temáticas — flores gigantes cujo ciclo de brotar e murchar dura dez respirações e que ao
  murchar viram poça de veneno que contamina o solo; nevasca com monstros de núcleo oculto
  que se estilhaçam em menores quando mortos e crescem enquanto a nevasca durar; uma fera
  desolada cega que pare filhotes sem parar; um resíduo de calamidade anterior que nunca foi
  expulso e passeia pela terra há décadas. **A economia da defesa:** estoque finito e não
  reponível de essência; cicatrizes de calamidades antigas que a próxima ataca primeiro por
  serem o ponto fraco; buracos no céu que, se não remendados, viram porta para invasores; e
  a jogada extrema de **amputar uma região inteira** com o problema dentro. **As
  contramedidas como decisões de jogador:** empobrecer-se de propósito antes da data; elevar
  a própria sorte; desacelerar o tempo interno trocando crescimento por segurança; prever a
  próxima forma em vez de resistir a ela; usar bestas descartáveis como para-raios. **A
  tribulação de ascensão como cenário de defesa:** a cerimônia é ruidosa, visível a
  quilômetros e imobiliza o cultivador mais importante do grupo; ninguém pode ajudar na
  fusão dos três qi, só segurar as calamidades externas; escolher um lugar de qi ralo
  enfraquece a prova e sabota o futuro; cada camada tem um contra-perfil, e a fonte de cada
  camada é destrutível mas se refaz. E a fase final que rouba em vez de ferir — mãos
  imateriais que só levam Gu, com a contagem de dedos definindo o rank que conseguem levar,
  e a única janela de contra-ataque sendo o instante em que a mão fecha o punho.
- **Fontes:** **A** "Calamidade e tribulação das terras abençoadas"; **B** "The Sixth Earthly
  Calamity of Hu Immortal Blessed Land", "Immortal Ascension Tribulation dentro da Imperial
  Court e o 'Formless Hand'", "Immortal Ascension Tribulation"; **C** "Calamidades terrestres
  e tribulações celestiais"; **D** "A ascensão a Gu Imortal"; **F** "Calamities and
  tribulations", "The adaptive myriad tribulation inside an immortal aperture", "Trend of
  immortal ascension", "Chaotic disaster" (este último **só** como bloco de segredo de
  mestre).
- **Faixa de rank:** 3 a 7 como equipe contratada de um imortal; qualquer rank como
  população que mora dentro.
- **Por que é jogável:** cenário fechado com relógio, ondas escalonadas e um patrono que
  perde dinheiro a cada erro — e o raro caso em que a ordem que vem de cima é salvar as
  pessoas e abandonar os bens.

---

**`22 - Leilões, Cúpulas e Guerras de Mercado.md`**

- **Cobre:** o comércio de alto nível como cenário social. **O grande leilão** com três
  camadas de assento escritas no contrato antes do evento (salão principal, salas
  individuais, salas secretas que escondem a identidade), catálogo circulando num Gu de
  informação, incremento mínimo por lance, lotes que exigem pagamento em espécie e viram um
  quadro público de "procura-se". **A regra de ouro:** Gu Imortais não se compram com
  dinheiro — só se trocam —, o que cria um mercado de escambo puro no topo da economia. **O
  leilão como trégua diplomática:** imortais quase nunca se encontram, precisam emprestar
  Gu uns dos outros, e por isso valorizam a rede de contatos mais do que o lote. **A
  convenção fechada de escambo**, com local decidido poucos dias antes, acesso por
  recomendação, um item por pessoa por rodada em ordem sorteada, e o costume de guardar para
  o fim o que é difícil de trocar. **O banquete anual sem taxa nenhuma**, que é
  simultaneamente mercado, leilão, tribunal de duelos e clube — e cuja gratuidade é a
  jogada política. **O mercado permanente** onde se negocia por vontade e não por corpo,
  onde toda transação acende uma coluna de luz proporcional ao valor (não existe transação
  discreta), onde o anonimato é estrutural a ponto de o fugitivo mais procurado do mundo
  negociar abertamente, e onde uma aposta pode ser depositada e conferida em público como
  num cartório. **A guerra de preços**, com estoque como munição, reputação valendo mais que
  preço a preços iguais, compradores em greve tática para incentivar o corte, e um acordo
  tácito de anos sendo quebrado. E o **mercado aberto de refino** que nasce no fim da obra,
  com taxa de adesão, desconto para membros, promoção de emergência e cotas usadas para
  pressionar clãs a aderirem inteiros.
- **Fontes:** **B** "The Grand Auction of Northern Plains", "Treasure Yellow Heaven"; **C**
  "Aberturas do Treasure Yellow Heaven"; **D** "A guerra de preços do year Gu", "Eastern Sea
  Trading Convention"; **E** "Qi Sea Banquet"; **F** "O mercado aberto de refino de Gu",
  "Contribution board, mission board e exchange board".
- **Faixa de rank:** 4 a 8 como participantes; qualquer rank como agentes de quem não quer
  ser visto ali.
- **Por que é jogável:** é o único lugar onde o mapa de poder inteiro fica visível num só
  salão, e roda uma sessão completa — ou uma campanha comercial inteira — sem um golpe.
  Cruzar com `05 - Mercados e Leilões`, da pasta `06`, que dá a economia; esta dá a cena.

---

**`23 - A Cerimônia das Miríades de Tribos e a Estrada da Vida.md`**

- **Cobre:** o evento fechado mais completo da obra. Um mundo à parte onde totens são a via
  de cultivo dominante e onde se cultiva **comendo** — humanos comem materiais de Gu para
  ganhar as marcas correspondentes e vão construindo o próprio totem; onde os mortos são
  comidos porque o que sobra de valioso são os totens gravados no corpo; e onde os
  habitantes acham que aquele lugar é o mundo inteiro e chamam qualquer forasteiro de
  demônio de outro mundo. A cerimônia, uma vez a cada dez mil anos, sempre no mesmo campo:
  **um desafio não pode ser recusado**, mas pode-se pedir ajuda de terceiros — e é por isso
  que forças fracas se filiam a tribos grandes por vontade própria; só totens podem ser
  usados, o que reduz muito a mortalidade e transforma os golpes normais em trunfos
  guardados; brigar fora do formato faz do infrator inimigo de todos; e quem se rende cedo
  preserva a força para não virar alvo fácil do próximo desafiante. A camada social: a noite
  de festa e fogueira antes do torneio, as alianças costuradas em segredo enquanto de dia se
  luta, e o padrão de beleza invertido em relação ao resto do mundo. A condição de
  encerramento é mecânica: quando três imortais de rank 8 morrem no campo, a terra se acende
  e **uma estrada aparece**. E a estrada é a peça de design mais elegante da obra: cada passo
  consome força, vontade e essência **proporcionalmente à fundação de cada um**, de modo que
  a dificuldade é a mesma para todos e Gu Masters ultrapassam Gu Imortais; alterna subida
  com recompensa e descida sem recompensa; não conta distância, conta se você está dando o
  seu máximo; entidades bloqueiam o caminho engolindo quem falha; e, quando restam poucos,
  eles negociam um rodízio em que quem fica em primeiro leva o pior item e quem fica por
  último leva o melhor — se sobreviver até lá.
- **Fontes:** **F** "Myriad Tribes Ceremony e a Myriad Life Road" (caps. 2113-2117). Regras
  de contexto sobre grotto-heavens fechadas em **C** ("Hei Fan grotto-heaven": a ingenuidade
  dos isolados, o sino do espírito celeste, a coleira da tribulação adiada) — usar apenas
  como comparação, num bloco curto, para mostrar que mundos fechados são uma categoria.
- **Faixa de rank:** 1 a 8, e é o único evento da obra que funciona com o grupo todo em
  ranks diferentes.
- **Por que é jogável:** um mestre roda isso lendo só a nota — periodicidade declarada,
  local fixo, regras de torneio escritas, sistema de cultivo próprio, camada social,
  condição de encerramento mecânica e uma masmorra final onde rank não dá vantagem nenhuma.

---

### LOTE 5 — Escala de mundo (qualquer rank, como pano de fundo ou como catástrofe)

Redator do lote 5: seis notas. Aqui a mesa não é protagonista do evento — o evento é o
tabuleiro. É também onde o corte de spoiler precisa ser mais cirúrgico.

---

**`24 - A Grande Era e as Marés de Qi.md`**

- **Cobre:** a mudança estrutural que parte o cenário em antes e depois. A causa: as paredes
  regionais eram diferenças de energia entre regiões vizinhas, condensadas em fronteira; as
  veias da terra começam a se fundir e as paredes a se dissolver. Os sinais, em ordem: os
  terremotos das veias da terra, começando pela região com as marcas de terra mais densas —
  chão que treme como se houvesse uma píton rolando por baixo, cordilheiras rasgadas ao
  meio, rios bloqueados, montanhas engolidas por trincheiras de profundidade imensurável que
  se estendem por milhões de li. **Os efeitos assimétricos, que são o coração da nota:**
  para os mortais é catástrofe pura e forças inteiras são extintas; para as super forças é
  prejuízo; para o Gu Imortal individual é a maior corrida do ouro da história, porque dos
  abismos emergem materiais imortais até o topo da escala e Gu Imortais selvagens. E um
  quarto efeito que quase ninguém lembra: **terremoto é dano a projetos** — refinos de anos e
  formações em ativação são destruídos. A consequência política completa o ciclo: catástrofe
  → trégua entre rivais que passam a investigar juntos → corrida do ouro → as disputas
  voltam, agora dentro das trincheiras. Depois vêm **as marés de qi**: com as paredes
  desfeitas, os cinco tipos de energia convergem em ondas que varrem o mundo; cada maré
  passa em minutos, mata indiscriminadamente, **desestabiliza toda abertura imortal — e
  quanto mais forte a fundação, mais tempo o imortal fica recolhido em recuperação**; expõe
  esconderijos guardados por um milhão de anos; e inunda a região de marcas de um caminho só,
  revirando o valor dos recursos. Fecha com a praga que as marés deixam: um fruto do tamanho
  de uma carroça que é tesouro se colhido e sentença de morte se plantado, e cujas duas
  saídas óbvias — arrancar e destruir — são as duas armadilhas.
- **Fontes:** **D** "Os terremotos das veias da terra de Southern Border", "A chegada da
  Grande Era"; **E** "The Great Era / a fusão das cinco regiões", "As marés de qi"; **F**
  "Qi tides", "Qi harvest fruit", "Earth Treasury e as Dez Terras" (só a origem; a
  exploração fica em `12`).
- **Faixa de rank:** 1 a 8 — e é justamente o encontro das duas pontas na mesma sessão que a
  torna interessante.
- **Por que é jogável:** as marés de qi desligam os PdMs poderosos por tempo proporcional ao
  poder deles, o que resolve sozinho o problema de "por que os adultos não resolvem isto"; e
  cada fossa que se abre é simultaneamente a destruição de uma vila e a chance de uma vida.

---

**`25 - A Guerra do Destino.md`**

- **Cobre:** a guerra multi-regional descrita como arquitetura, nunca como enredo. O
  gatilho: uma instituição milenar deixa vazar que vai concluir um projeto que lhe devolveria
  o controle do mundo, e, com as paredes regionais afinando, pela primeira vez na história é
  fisicamente possível quatro regiões marcharem juntas sobre a quinta. **Quatro frentes
  simultâneas com prioridade estratégica declarada**, o que dá um mapa de campanha pronto:
  a fortaleza sagrada; a usina onde se produz o insumo do projeto; a maior cidade mortal do
  mundo, sede da final de um torneio de artesãos; e uma caverna onde se domestica uma
  criatura enorme. As cinco forças atacantes descritas como tipos, cada uma com um motivo
  incompatível com o das outras — uma unida e disciplinada que ataca o alvo estrategicamente
  correto, uma rica e desunida que vem por lucro, uma conservadora que guarda força, uma que
  vai direto ao alvo máximo, e os avulsos que parasitam o caos saqueando o que ficou sem
  guarnição. As regras que fazem a guerra funcionar: **o insumo tem de ser fisicamente
  transportado** de um ponto ao outro, e o comboio é o relógio do cenário; os defensores têm
  teleporte interno confiável e uma formação de cura dedicada que permite rodízio, e os
  atacantes não; e um cemitério de imortais adormecidos que fornece reforço praticamente
  inesgotável mas **imprevisível por regra** — ninguém escolhe quem acorda nem quando. E a
  camada mortal, que é a mais jogável: a convenção acontece do começo ao fim com Gu Masters
  mortais, sob sabotagem, com mais de dez mil mortos sem que ela pare, e com participantes
  que competem por convicção. Fecha com a fossa que se abre sob a maior cidade mortal do
  mundo — minutos entre a rachadura e a queda, nenhum poder do cenário capaz de impedir — e
  com a variante em que a cidade é convertida num mundo-pintura e salva por um arranjo
  deixado séculos antes.
- **Fontes:** **E** "A Guerra do Destino", "A fossa terrestre que engole Emperor City",
  "Central Continent Refinement Path Convention", "Despertares do cemitério imortal";
  **D** "O comunicado de Heavenly Court" (como o evento de informação que prepara o clima).
- **Faixa de rank:** 3 a 8 — mortais na convenção e no comboio, imortais nas frentes.
- **Por que é jogável:** as frentes correm em paralelo, então **o que o grupo não faz também
  acontece**; e a catástrofe final é o raro momento em que um rank 8 é tão impotente quanto
  um camponês, o que faz de salvar dez pessoas a única vitória disponível para qualquer um.

---

**`26 - A Caverna do Demônio Enlouquecido.md`**

- **Cobre:** a masmorra de nove camadas construída no ponto onde a fronteira do mundo é mais
  fina. As camadas com terreno próprio (terra amarela com feras selvagens; rochas ardentes;
  névoa com criaturas que a habitam; uma camada onde tudo brilha e as marcas do Dao se
  agrupam em manchas de arco-íris colhíveis como material puro do topo da escala; um vazio
  contendo mundos inteiros; e o núcleo). As regras: **sons demoníacos** que enlouquecem e
  embaralham as marcas do Dao, de modo que os materiais das camadas rasas viram lixo e não
  podem ser comercializados; o vazio que **encolhe**, puxando os mundos para o centro até
  restar um só; cada mundo que morre virando combustível do núcleo, o que significa que **a
  guerra alimenta o prêmio**; e a formação final, onde milhares de blocos de gelo flutuam em
  órbita, só sobre um bloco se está seguro, cada bloco tem tamanho e forma diferentes
  conforme quem olha, e pisar num deles despeja no peito uma emoção intensa e alheia que se
  intensifica quanto mais fundo se vai — **é a emoção que barra o avanço, não o combate**.
  Mais o segredo de mestre que a nota precisa isolar num bloco próprio: existe um caos fora
  da fronteira do mundo; ele chega por calendário ou por arrombamento; um buraco na fronteira
  cresce sozinho e dobrou de tamanho em poucas respirações; e se não for tapado o mundo
  inteiro é destruído.
- **Fontes:** **F** "Expedition to Crazed Demon Cave / Battle of the Three Great Worlds",
  "Chaotic disaster", "Thieving Heaven pierces the world and the four Venerables repair it";
  **C** "Crazed Demon Cave" dentro de "As dez grandes áreas ferozes" (a descrição de fora,
  e a informação de que é área feroz só na aparência).
- **Faixa de rank:** 3 a 8 — as camadas rasas servem a grupos fracos; as duas últimas são
  escala de mundo.
- **Por que é jogável:** é a "Shibuya" da obra — um lugar fechado, três potências em guerra
  dentro dele, populações nativas condenadas, e uma masmorra final onde o dano é emocional.
  **Exige o corte de spoiler mais cirúrgico de toda a pasta:** o desfecho da expedição some
  inteiro, e nenhum Venerável entra por nome.

---

**`27 - A Morte do Sol e o Céu Espectral.md`**

- **Cobre:** as três catástrofes encadeadas que reescrevem as regras ambientais do mundo no
  fim da obra. **(1) O Sol.** Ele não é um astro comum: é o maior nó de veia celestial do
  mundo, uma congregação de marcas de três caminhos, e se mantinha estável porque tinha um
  núcleo. Retirado o núcleo, explode. O mundo escurece; a temperatura despenca e um mar de
  gelo quadruplica de tamanho; e cai **chuva de fogo** — material imortal do topo da escala
  caindo do céu, que só um grande especialista pode tocar, que cai preferencialmente onde há
  marcas compatíveis, que ameaça toda formação exposta ao céu e que, reunido em quantidade
  suficiente num lugar só, vira um ponto de recurso permanente. Clãs enriquecem e clãs
  empobrecem em uma tarde. **(2) A fusão dos dois céus.** A parede de energia que os separava
  se dissipa; toda comunidade assentada sobre um nó de veia celestial sofre calamidades
  simultâneas por dentro — terremoto, enchente, erupção e chuva ácida por mais de dez dias
  seguidos —, o que produz uma crise de refugiados e uma guerra de recrutamento entre
  facções, com realocação de mundos inteiros como serviço caríssimo e um resgate registrado
  que salvou três de seis. Junto vêm as feras deslocadas, com dietas memoráveis. **(3) O céu
  novo.** Uma chama gélida varre os dois céus por dois dias e duas noites e solda os
  fragmentos num só. As cinco mudanças permanentes ficam enumeradas: um caminho suprimido e
  o oposto amplificado no mundo inteiro; uma **intenção de matar fria e constante** irradiando
  do centro do céu, da qual quase nenhum ser vivo escapa; conflitos e mortes em alta;
  criaturas de alma aparecendo em toda parte; e, em compensação, a vontade do céu enfim
  estabilizada, o que abre a maior janela de ascensão da obra. Fecha com o fenômeno inédito
  que o novo céu produz: reinos de sonho que **caçam** — têm forma de bestas, mudam de forma,
  não podem ser rastreados, engolem a presa de uma bocada, e por dentro entregam ao sonhador
  o papel de dono de um mundo pequeno, com terreno errado e calamidades no calendário.
- **Fontes:** **F** "Spectral Soul destroys the Sun", "Fusion of the two immemorial heavens
  and the crisis of the grotto-heavens", "Spectral Heaven", "Trend of immortal ascension",
  "Heaven path dream realms"; **E** "Aliança dos Dois Céus e a primeira invasão vinda de
  fora" (a política das grotto-heavens antes da crise).
- **Faixa de rank:** 1 a 8 — a chuva de fogo é de rank baixo, o resto é ambiente.
- **Por que é jogável:** um desastre natural com tesouro dentro, e depois uma nova
  normalidade que muda o tom de toda cena — brigas estouram por nada, cadáveres viram outra
  coisa, e quem encara o céu tempo demais precisa lidar com a própria vontade de matar.
- **Cuidado especial:** escrever só o **efeito**, nunca a causa. Quem destruiu o Sol e o que
  há no centro do céu novo não entram de forma alguma.

---

**`28 - O Mundo em Véspera de Guerra.md`**

- **Cobre:** o estado do cenário no fim da obra, para quem quiser ambientar ali. **Três
  potências pessoais e duas regiões sem dono:** por três milhões de anos valeu a regra de que
  dois reis não coexistem, e ela quebrou; o mapa político se redesenha em semanas, com três
  regiões submetidas, uma governada por aliança regional e uma explicitamente a mais fraca,
  sem liderança unificada. As regras sociais do período: só um igual pode enfrentar um igual,
  e todos os demais viram gente que sobrevive nas frestas; a distinção entre caminho correto
  e demoníaco perde sentido prático mas continua sendo moeda política; **nenhuma coalizão de
  fracos se forma**, porque cada um teme que um movimento brusco desperte um dos grandes; e
  nasce um comportamento novo de sobrevivência — procurar rota de fuga com o inimigo do
  próprio protetor. **A pilhagem como desastre:** um poder de topo arranca pontos de recurso
  inteiros do chão e os guarda, anunciando cada roubo publicamente como chantagem; um rio
  colossal perde a maior parte de si e o curso médio seca, com efeito sobre lavouras,
  temperatura e povoados de toda a bacia; um rio inteiro é levado com o leito, e o festival
  anual que se fazia nas margens fica sem lugar. **A guerra que nunca acontece:** a guerra
  caótica das cinco regiões é citada dezenas de vezes e a obra termina sem mostrá-la — o que
  a torna a atmosfera mais segura e mais reutilizável de todas: todo mundo se armando, todo
  mundo escolhendo padrinho, todo mundo com medo de escolher errado, caminhos antes
  desprezados recebendo verba, e a certeza compartilhada de que quem for pequeno quando
  estourar será usado como escudo. E, como contraponto luminoso, a fronteira nova que se
  abre dentro de uma cidade fechada: os mundos-pintura, onde **a diferença entre imortal e
  mortal é mínima**, onde os Gu de caminho humano funcionam como profissões, sindicatos e
  postos militares, e onde o próprio mundo criou sozinho uma profissão nova quando os
  exploradores fracassaram.
- **Fontes:** **F** "Era of the Three Venerables", "The plundering of Central Continent",
  "Five Regions Chaotic War", "The two new painting worlds of Divine Emperor City",
  "Painting world trials", "Human Sea" (**só** se a designer quiser esse registro — tema
  pesadíssimo; tratar num bloco curto e avisado); **B**, **C**, **D**, **E** para as menções
  antecipadas da guerra caótica.
- **Faixa de rank:** qualquer.
- **Por que é jogável:** é spoiler zero, porque o principal não acontece. E entrega o melhor
  drama de consequência da obra: os jogadores não podem impedir nada, e a mesa inteira cabe
  na pergunta "o que você tira de casa quando a casa vai ser roubada em três dias".

---

**`29 - Eventos Históricos de Fundo.md`**

- **Cobre:** o passado citado, reunido numa nota só, porque serve de contexto e não de
  cenário. Organizado por função, não por cronologia: **por que existem heranças em toda
  parte** (um mestre demoníaco que, sabendo que morreria, montou centenas de milhares de
  terrenos de herança baratos e fáceis de multiplicar, espalhados por todo o mundo — o
  exemplo canônico de como um indivíduo altera o mundo para sempre com logística, não com
  batalha); **por que uma montanha guarda um artefato** (um vencedor abandonou a própria casa
  imortal no chão como tampa de um caixão); **por que uma planície inteira é sagrada para
  dois caminhos**; **por que uma região tem seitas e as outras quatro têm clãs** (um decreto
  fundador que aboliu o sistema de clãs entre imortais — e a ressalva de que mortais
  continuam em clãs mesmo lá); **por que existem três corredores sem defesa dentro da
  fortaleza mais antiga do mundo** (três invasões antigas os abriram e eles continuam lá);
  **por que as formações de batalha antigas são melhores e mais difíceis que a tecnologia
  atual**; **por que campos de batalha antigos viram ecossistemas de Gu selvagens**; **por
  que um deserto grita**; **por que existe um crédito de três Gu Imortais esperando um
  herdeiro que saiba uma senha morta há eras**; e o arquétipo completo do cenário — clã
  destrói clã, sobreviventes acham herança, voltam décadas depois e apagam o vencedor do
  mapa, deixando a moral estrutural de que organizações não protegem contra indivíduos
  fortes o bastante. Mais a mitologia tratada como documentação técnica: o ciclo do primeiro
  humano, e o fato de que lugares e criaturas das lendas **existem** e funcionam exatamente
  como a lenda diz.
- **Fontes:** as seções "Eventos históricos citados" de **A**, **B**, **C**, **D**, **E** e
  **F**, integralmente.
- **Faixa de rank:** não se aplica — é nota de contexto.
- **Por que entra:** dá idade ao cenário e explica por que o mundo do "agora" tem a forma que
  tem. Nenhum destes vira aventura; todos viram resposta a uma pergunta da designer. Faz par
  com `09 - Linha do Tempo e Eras`, da pasta `10`, que dá a cronologia; esta dá as causas.

---

## 5. O que foi deixado de fora, e por quê

Registrado para que ninguém ache que foi esquecimento.

- **Cerimônia do Despertar, aposta de rochas, arena profissional, convenção de refino,
  quadros de missão, conselho orçamentário de uma seita, cerimônia mestre-discípulo, noivado
  político, disputa de ponto de recurso por linhagem, alianças juradas.** Todos já cobertos
  como **instituições** em `06 - Economia e Vida` (notas `07`, `08`, `09`, `10`) e em
  `05 - Sociedade` (notas `10`, `11`, `13`, `14`). Esta pasta trata de **acontecimentos**;
  quando um deles precisa da instituição, remete por wikilink em vez de repetir.
- **A ascensão a Gu Imortal como procedimento** — pertence a `11 - Ascensão Imortal`, da
  pasta `01`. Entra aqui só como *cenário de defesa*, dentro de `21`.
- **A teoria das calamidades** (mecanismo unificado, tabela de rendimento em marcas do Dao,
  calendário por rank) — pertence a `10 - Tribulações e Calamidades`, da pasta `01`, e a
  `02 - Tabelas de Referência Rápida`. A nota `21` descreve como é *estar dentro* de uma.
- **O projeto de obra pública que consome uma espécie inteira** (**B**) e a **campanha de
  extermínio de populações** (**F**) — temas pesadíssimos, sem mecânica de mundo nova. O
  primeiro fica registrado só como parágrafo de contexto em `18`; o segundo, como bloco curto
  e avisado em `28`, e a designer decide se quer.
- **Os combates entre figuras de rank 9** — descartados: o interesse é inteiramente "quem
  venceu", e cada cena carrega revelação de enredo.
- **O ritual secreto que sustenta a convenção de refino** e os demais segredos de
  organização — já estão em `10 - Convenção do Caminho de Refino` e em `15 - Tribunal
  Celestial`. Não se repetem aqui.

## 6. Instruções operacionais para os redatores

1. **Um lote por redator.** Os cinco lotes não se cruzam: cada arquivo tem um dono só.
2. **Escrita incremental.** Salvar em disco a cada seção concluída; nunca acumular em
   contexto.
3. **Nenhum redator roda `git add` ou `git commit`.**
4. **Frontmatter obrigatório** conforme o modelo, com `ranks:` preenchido com a faixa
   indicada aqui e `fontes:` com os capítulos que a nota bruta cita.
5. **Convenção dos quatro estados de confiabilidade** declarada no cabeçalho de cada nota,
   com a frase de que apagar tudo marcado com `*` devolve o documento a cem por cento
   canônico.
6. **Sem citação de capítulo no corpo.** Rastreabilidade só no `fontes`.
7. **Wikilinks pelo nome exato do arquivo, sempre com texto alternativo.** As notas da
   própria pasta ainda não existem quando o lote começa a ser escrito; linkar assim mesmo.
8. **Depois de a pasta fechar:** incluir os 29 arquivos na ordem de leitura de
   `_pipeline/numerar-notas.py` e rodar o script, seguido de `_pipeline/auditar-links.py`.
   Sem isso o script aborta, porque encontra notas no disco que não estão na ordem.
