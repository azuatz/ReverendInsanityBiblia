---
tags:
  - pesquisa
  - organizacao/clã
  - regiao/deserto-ocidental
status: em-andamento
---

# Pesquisa bruta — Forças e organizações do Deserto Ocidental

Arquivo de bastidor da nota final `11 - Forcas e Organizacoes/04 - Deserto Ocidental.md`.
Aqui a citação de capítulo é obrigatória; tudo que estiver na nota final tem de poder ser
rastreado até uma linha daqui.

**Fonte:** `/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/*.txt`.
Volumes → capítulos: V1 = 1–199 · V2 = 200–405 · V3 = 406–649 · V4 = 650–1021 ·
V5 = 1022–1966 · V6 = 1967–2334. Toda busca feita com `grep -i` (a obra grafa nomes em
minúsculas em boa parte do texto).

---

## 0. A premissa da tarefa, conferida — "o Oeste se organiza em templos"

**REFUTADA no texto.** O briefing desta tarefa supunha que a forma típica de organização
do Deserto Ocidental não fosse o clã nem a seita, e que a obra falasse em *templos*.
Verificação direta:

- Levantamento de todas as ocorrências de `temple` na obra inteira
  (`grep -ioh "[a-z']* temple" *.txt | sort | uniq -c | sort -rn`) devolve apenas:
  **Heaven Temple** (47), **Space Temple** (25), **Moon Temple** (12),
  **Pregnancy Temple** (6), `daoist temple` (5) e ruído ("his temple", "greying temple"
  = têmpora, no sentido anatômico).
- O único **Templo** que é organização na obra é o **Black Heaven Temple** (Templo do
  Céu Negro), e ele é **do Continente Central**, uma das dez grandes seitas antigas:
  > "It was under the control of one of Central Continent's ten great ancient sects,
  > Black Heaven Temple." — **cap. 2039** (também cap. 811 e cap. 1388)
  Ele obedece ao Tribunal Celestial (Heavenly Court) e tem "primeiro ancião supremo" como
  as demais seitas do centro. Nada a ver com o Oeste.
- Busca cruzada `western desert` a até 150 caracteres de
  `temple|shrine|priest|worship|faith|religio|monk|pilgrim|holy|sacred` devolve **zero**
  resultados de organização religiosa. Os únicos casos são "Sacred Feather City" (Cidade
  Sagrada da Pena, dos homens-pena) e um uso adjetival de "sacred moment" numa cerimônia
  de maioridade (cap. 1491).
- Não existe **nenhuma** ocorrência de `monastery` na obra inteira (zero em 6 volumes).
  `buddha` aparece ~15 vezes, todas em figuras de linguagem ("slaying buddhas"), nunca
  como instituição.

**A forma real:** o Deserto Ocidental se organiza em **clãs** (super clãs / super forças),
exatamente como a Fronteira Sul — o parentesco é a cidadania. O que muda em relação ao sul
não é a *forma* da instituição, e sim três coisas: (1) a região **nunca teve** um poder
unificador; (2) a unidade física de assentamento é o **oásis** e a **cidade**, não a
montanha; (3) a economia é de **caravanas e mercado**, com um instrumento próprio — o
*token de transação* — que transforma comércio em lealdade excludente.

> Registro para o vault: a nota `05 - Sociedade/07 - As Grandes Forças do Mundo.md` já
> descrevia o Oeste como região de clãs, o que confere. Já a nota
> `05 - Sociedade/06 - Cultura das Cinco Regiões.md` chama o Oeste de "mundo das cidades"
> e diz que a unidade social é "cidade / caravana" — isso é meia-verdade: cidades e
> caravanas são a unidade *econômica*, mas a unidade *política* é o clã, e as cidades
> pertencem a clãs (a Cidade do Lobo de Areia é uma das cidades principais do clã Mo — cap. 1973).

---

## 1. O sistema de organização da região

### 1.1 A forma: clãs, e catorze deles no topo

**A lista canônica completa das super forças do Deserto Ocidental** — o achado mais
importante desta pesquisa, porque a obra a enumera de uma vez só:

> "Western Desert's super forces had fourteen clans: Lin clan, Xiao clan, Tian clan,
> Fang clan, Dong clan, Wan clan, Sun clan, Mo clan, Tang clan, Qin clan, Shi clan,
> Gong clan, Zuo Qiu clan, and Tuoba clan." — **cap. 2255**

São **catorze super clãs**. Note que *Zuo Qiu* e *Tuoba* são sobrenomes duplos (compostos),
como no chinês; não são dois clãs cada.

Comparar com o cap. 776, que fala em "the dozen or so super forces in Western Desert" —
"a dúzia e pouco de super forças do Deserto Ocidental" —, consistente com catorze.

Abaixo das super forças existe uma escada de porte igual à do sul: cap. 674 fala em
**"upper tier force"** (força de escalão superior) com "centenas de anos de história" e em
**"small sized forces"** que se submetem a ela.

### 1.2 A unidade física: o oásis, e sua planta em anéis

O texto descreve o assentamento do oeste com a mesma clareza com que descreve o
acampamento do norte. O oásis Sha Jing, cap. 674:

> "Huang clan as an upper tier force had hundreds of years of history here, they occupied
> the most important resources at the center of this oasis."
> "At the outer parts of the oasis, there were small sized forces that submitted to this
> Huang clan."
> "At the even further outer areas, near the fringe of Sha Jing oasis, there were mortal
> villages. These mortals had a tough life, they had huge numbers and were all under the
> control of Huang clan and other forces of Gu Masters." — **cap. 674**

Ou seja: **três anéis** — clã dominante no centro (sobre o recurso), clãs vassalos no anel
médio, vilarejos mortais na franja. A hierarquia desenhada no chão, como no norte, mas
organizada em torno de água em vez de proteção contra o inverno.

Sobre por que as pessoas se aglomeram assim:

> "In western desert, humans relied on oasis to live, thus people are always gathered
> together. As long as the oasis is intact, nobody would make life difficult for themselves
> and go to another living area by making a dangerous and arduous desert journey."
> — **cap. 425**

O oásis também tem uma regra de trânsito que vale como **conhecimento comum da região**:

> "This is Zhou Xi oasis, controlled by us, Lan clan. **The sky above the oasis is a
> no-fly zone**, I hope sir can land on the ground! If you wish to enter the oasis, we have
> Gu Masters in charge of attending to visiting Gu Masters from outside. Sir just needs to
> follow the procedures…"
> "**Did sir hear me? The sky above the oasis is a no-fly zone, this is general knowledge
> in western desert. Sir flying above Lan clan can be regarded as a provocation!**"
> — **cap. 694**

Voar sobre um oásis alheio é provocação declarada. Visitantes desembarcam e passam por um
guichê de recepção com procedimento formal.

**Cidades e pedágio.** As cidades ficam no centro de oásis grandes e cobram entrada por
cabeça, em pedras primordiais:
> "The oasis was vast, and there was a stone city at the center. The city walls were short,
> but the overall length was long, there were a huge number of mortals living in the city,
> it was Sand Wolf City." … "The guard walked towards them and extended his hand:
> '**Entry fee of one primeval stone per person.**'" — **cap. 1973**

(Comparação de escala: a cidade do clã Shang, na Fronteira Sul, cobra **dez** pedras
primordiais na muralha externa e **cem** por anel interno — cap. 259–261. A cidade do
deserto é barata; ela vende acesso a água e mercado, não a serviços de luxo.)

### 1.3 A economia: caravana, escassez complementar e o token de transação

A caravana é a instituição econômica da região, e a obra é explícita sobre o *porquê*:

> "As for western desert, it's the place where **caravans flourish the most**. Cities after
> cities, surviving using the oasis in the desert. … a flourishing caravan trade means that
> **information also travels fast**." — **cap. 425**

> "Western Desert was **the place with the greatest trade economy in the five regions**."
> — **cap. 996**

A caravana mortal típica é puxada a camelo, atravessa deserto aberto, e é descrita como
"difícil, extremamente perigoso e extremamente cansativo", com a vida frágil do mercador
perdida por qualquer descuido (cap. 2015). Caravanas grandes têm escolta de Mestres Gu com
líder de caravana próprio (cap. 693: "I am Mo clan's caravan leader, Mo Yan", um rank 5).
Caravanas boas carregam Mestres Gu capazes de **criar água do nada**, o que dispensa a
rota de oásis e torna a travessia segura (cap. 1967).

**O token de transação** (*transaction token*) é o instrumento financeiro característico da
região:

> "Every super force would issue their respective transaction token. But Xiao clan's
> transaction token was the one with the most value."
> "The reason was Xiao clan and Tian clan engaged in business the most among all the super
> forces in Western Desert, with the highest numbers of trading partners."
> "**Xiao clan and Tian clan were the biggest competitors, accepting Xiao clan's
> transaction token meant being close to Xiao clan, as such, it would be difficult for
> [him] to do business with Tian clan and Gu Immortals who possessed Tian clan's
> transaction token.**" — **cap. 908**

Como funciona na prática (cap. 837, 907, 908): o clã observa e investiga o candidato por um
tempo; se a cooperação for satisfatória, um ancião supremo autoriza a entrega do token; o
token traz **políticas preferenciais** registradas num Gu mortal de caminho da informação;
aceitar é opcional e público. Com o token na mão, um forasteiro completo consegue fechar
negócios em toda a rede do clã emissor já no primeiro encontro. É, ao mesmo tempo,
passaporte comercial e declaração de lealdade — e por isso **exclui** o bloco rival.

### 1.4 A cultura: a região que negocia

Esta é a chave para entender o Oeste, e a obra a enuncia diretamente:

> "Moreover, Western Desert is somewhat special. **Western Desert Gu Immortals compromise a
> little more easily than those of the other four regions.**
> This was not because Western Desert Gu Immortals were soft, it was because of the
> environment.
> Different from other regions, Western Desert was filled with boundless deserts and oases.
> **If an oasis was destroyed in a battle between Gu Masters, they would have no foundation
> for survival and could easily perish together.** On the other hand, **different oases
> produced different resources, Gu Masters would need each other's help** to make up for
> what they lack in their cultivation. So Gu Masters often formed caravans and moved a long
> distance which was usually quite dangerous and exhausting. Thus, there were many
> collaborative relationships between Gu Masters as well as different forces.
> So, since long ago, Western Desert's Gu Masters were molded to compromise and make
> concessions for the survival of both sides. … This habit had sunk deep into their bones
> and was already a part of the nature of Western Desert Gu Immortals." — **cap. 1617**

E o contraste explícito, no mesmo trecho: diante de um sequestro, as forças corretas do
Oeste "teriam cedido mais rápido que a Fronteira Sul, com uma atitude mais realista e
apropriada", enquanto imortais das Planícies do Norte "são valentes e não temem a morte,
podendo até achar uma desgraça serem resgatados".

Isto é o oposto do estereótipo de deserto. O ambiente hostil do Oeste **não** produziu
guerreiros fanáticos: produziu negociadores, porque a base material de todos é frágil e
complementar. Destruir o oásis do inimigo mata os dois.

### 1.5 A política: a região sem dono

> "**And among the five regions, Central Continent's foundation is the deepest** … they
> also have a unified leader — Heavenly Court! This is something none of the other four
> regions have. Whether it be Eastern Sea, Western Desert, Southern Border or Northern
> Plains, they are all **controlled by independent super forces and are disunited**.
> Northern Plains does have Longevity Heaven, so their situation will be slightly better…"
> — **cap. 1435**

> "While Southern Border, Western Desert, and Eastern Sea were controlled by various super
> forces. They were used to abusing their powers, and **none of them wanted a force to boss
> them around**." — **cap. 1614**

**A carta de desafio como instrumento de fronteira.** O texto documenta o mecanismo num
episódio histórico (a era anterior, antes de o Venerável da Alma Espectral ascender):

> "However, when Qing clan's first supreme elder was about to set off, he received a
> challenge letter.
> **This letter came from another Western Desert super force which had deep enmity with
> Qing clan, they requested a battle with Qing clan first supreme elder, wanting to use the
> result of this battle to decide their territorial boundary.**
> 'Damn it, at this juncture!' Qing clan's Gu Immortals shouted immediately.
> '**They are doing this on purpose.** But the territorial boundary determines the ownership
> of a resource point, the benefits involved are too much. What do you think?'"
> — **cap. 2040**

Três coisas ficam registradas de uma vez: (1) fronteira territorial se decide por **duelo
entre os líderes máximos**; (2) o que está em jogo é a posse de um **ponto de recurso**;
(3) escolher deliberadamente o pior momento do rival é jogada reconhecida — e reconhecida
como suja pelos próprios alvos.

**A pressão coletiva contra quem sobe.** Quando um clã da região dá um salto de poder, os
outros se juntam contra ele por reflexo:

> "'The true reason is that our clan obtained Divine Bean Palace, once we absorb our gains
> properly, the top spot among Western Desert's righteous path forces will probably belong
> to our Fang clan. **Strength represents power and authority, and even more importantly,
> benefits. Our clan's rise will naturally be through stepping on other clans. This is why
> the other great clans are not tolerating us and are jointly pressuring us.**'"
> — **cap. 1616**

E o mesmo raciocínio antecipado no cap. 1530: "many super forces would not want Fang clan
to obtain this Immortal Gu House and became the number one super force in Western Desert!"

Isso fecha o círculo com 1.4: a região negocia porque não pode se destruir, e **impede
qualquer um de vencer** porque um vencedor acabaria com a negociação. Nunca houve poder
unificador no Oeste não por acaso, mas por um mecanismo social que se auto-reforça.

### 1.6 Escravidão e humanos variantes

- Os **homens-pena** (*feathermen*) são "escravos de alta qualidade no Deserto Ocidental.
  Super forças e forças grandes, **todas** tinham caravanas baseadas em homens-pena" —
  **cap. 870**. A razão é mecânica: nascem com marcas do dao de caminho da nuvem e são
  voadores natos (cap. 866), o que os torna a mão de obra ideal para transporte.
- Existe pelo menos **uma cidade humana no Oeste ostracizada e reprimida pelos humanos
  variantes** — a relação não é de mão única em todo lugar (**cap. 1635**).
- Um Gu Imortal do Oeste está registrado como rank 6, do caminho da terra, dono do
  *turn rock Gu* (Gu de virar rocha): "he used this Gu to **turn sand into rocks, in order
  for people to build structures in the desert**, he was very popular and received
  gratitude from the people" — **cap. 425**. Vale como retrato do que um imortal benfeitor
  faz numa região sem pedra: ele vende material de construção fabricado a partir de areia.

---

## 2. As forças, uma a uma

> Convenção deste arquivo: cada afirmação vem com o capítulo. Onde eu induzo algo, escrevo
> "INDUÇÃO" em maiúsculas — na nota final vira `*`.

### 2.1 Clã Fang (Fang clan) — a casa das Casas de Gu

A força mais documentada da região; a obra passa centenas de capítulos dentro dela.

**O que domina.** O negócio de Casas de Gu:
> "As a super force in Western Desert, Fang clan was famous in the world for the Gu house
> business. **It had its own unique wisdom path inheritance.**"
> "Fang clan researched Gu houses and designed new Gu houses, they were deducing new
> immortal killer moves, they could not do that without deep wisdom path attainment."
> "…they were truly **the number one super force in expertise of Gu houses within Western
> Desert, and perhaps even the world**." — **cap. 1521**

Repare na causalidade, que é o miolo da ficha: **projetar Casa de Gu exige caminho da
sabedoria**, porque desenhar uma Casa é deduzir golpes imortais novos. A herança de
sabedoria não é um adorno; é a ferramenta de trabalho da empresa.

**Liderança.**
- **Primeiro ancião supremo: Fang Gong**, **rank 8** (nome em **cap. 1867**; rank em
  **cap. 1505**, **cap. 2222**: "their first supreme elder has rank eight cultivation level
  and they most excel in Immortal Gu Houses"). É quem governa.
- **Segundo ancião supremo: Fang Di Chang**, **rank 7**, o estrategista — e
  **grão-mestre supremo de caminho da sabedoria** (*wisdom path great grandmaster*):
  > "Fang clan had wisdom path inheritors through each generation, but **for the last
  > thousand years, Fang Di Chang was the only great grandmaster that emerged**."
  > — **cap. 1521**
  > "The current Fang clan was governed by the first supreme elder, while the second
  > supreme elder was the strategist. **These were the two people in power.**" — **cap. 1520**
- **Terceiro ancião supremo: Fang Hua Sheng**, **rank 7**, "specialized in **healing
  methods**", roupa e cabelos brancos, cara severa que vira sorriso caloroso — e é o
  **negociador** da casa, o que o clã manda quando quer conversar sem comprometer os dois
  de cima (**cap. 1775**; **cap. 1520**: "Fang clan sent their third supreme elder, it gave
  him some leeway"). Fang Yuan o classifica internamente como "an old sly fox" (**cap. 1519**).
- Nomes de quadro: **Fang Yun** e **Fang Leng**, rank 6, elites; um é bisneto direto do
  primeiro ancião supremo e o outro é filho adotivo do segundo — a obra não diz qual é qual
  (**cap. 1504**); Fang Leng é "a talent among rank sixes, **and is a possible successor of
  Fang clan**". **Fang An Lei**, rank 7, aparência comum, gorducha, sorriso amável e ar
  acolhedor (**cap. 1513**). **Fang Chen**, genro do clã (*in-law*), **Fang Zhi**,
  **Fang Dong Xi** (**cap. 1519**, **1616**, **2259**).

**Porte.** No episódio do deserto assombrado o clã coloca **mais de dez Gu Imortais** em
campo ao mesmo tempo, **metade deles rank 7**, mais três Casas de Gu Imortais — e um
observador estranha justamente isso: "Since when did Fang clan have so many Gu Immortals to
mobilize at will?" (**cap. 1520–1521**). Ou seja: dez imortais destacáveis **não** é o total
da casa, é o que ela pode tirar do quintal sem descuidar do resto ("Fang clan had many
assets and networks, their Gu Immortals needed to defend the territories" — **cap. 1507**).

**Assinatura — as Casas de Gu.** Três Casas de Gu Imortais de rank 7:
**Fallen Flower Hall** (Salão da Flor Caída), **Chicken Dog Coop** (Galinheiro-Canil) e
**Inquiry Dock** (Doca da Indagação). Combinadas, ativam o golpe de campo de batalha
**peach blossom maze** (labirinto de flor de pessegueiro) — "incredibly powerful"; as três
Casas ficam ocultas como núcleos que sustentam o labirinto, e os imortais lutam dentro dele
(**cap. 1518–1523**). Chicken Dog Coop solta em massa bestas desoladas ancestrais, "most
were dogs and chickens" (**cap. 1708**). Há ainda uma Casa de Gu Imortal **de caminho da
terra** que se move por baixo do solo, frágil na defesa (**cap. 2248**), e o golpe
**roof tile breaker** (quebra-telha), que restringe Casas de Gu alheias (**cap. 2258**).

**O tesouro estragado — Thieves Den.** O clã possui uma Casa de Gu Imortal de **caminho do
roubo** que pertenceu ao Venerável Demoníaco Ladrão do Céu:
> "**Fang clan has Thieving Heaven Demon Venerable's inheritance and that Immortal Gu House
> Thieves Den.**" … "it was very damaged because it involved theft path which Fang clan was
> not proficient in. When Fang clan obtained this Immortal Gu House, they had not obtained
> its complete contents so they had not been able to restore it." — **cap. 1865**
> "**My theft path attainment level is great grandmaster while none of Fang clan's Gu
> Immortals have such attainment. So even though Fang clan's superiority lies in
> constructing Immortal Gu Houses, they have always been without options to repair Thieves
> Den and left it incomplete.**" … "Fang Yuan only took a few glances at the relevant
> contents of Thieves Den and saw the efforts **Fang clan's successive generations** had
> made — they had all tried to repair this Immortal Gu House." — **cap. 1857**

Golpe associado: **steal dao** (roubar o dao), que suga as marcas de dao de um ponto de
recurso para dentro da Casa — poder de rank 8, mas com desgaste enorme sobre a Casa
danificada, não podendo ser usado extensivamente (**cap. 1779–1780**). Foi com ele que o clã
**apagou da existência** um oásis-ponto de recurso rival (**cap. 1780**).

Este é o melhor gancho de mesa da região inteira: **os melhores construtores de Casas de Gu
do mundo têm, na garagem, a Casa de um Venerável que não conseguem consertar**, porque lhes
falta o caminho — e só o caminho — do roubo.

**Território.** O clã faz fronteira com o **deserto do fantasma verde** (*green ghost
desert*) e é "a super força mais próxima" dele (**cap. 1504–1507**, **1512**). Seu ponto de
recurso mais precioso é o **oásis do orvalho celeste** (*heavenly dew oasis*), "um dos dez
maiores oásis do Deserto Ocidental" (**cap. 1779**): produz o próprio orvalho celeste e, no
centro do lago, **água branco-e-preta**, material imortal de rank 7; a defesa é feita por
várias centenas de **árvores-agulha** plantadas de propósito em anel, porque a formação que
o clã montou ali serve principalmente para **aumentar a produção de orvalho**, não para
defender (**cap. 1778–1779**). Trinta gotas de orvalho celeste equivalem a **três meses** de
acumulação do oásis. O clã tem também vários pontos de recurso pequenos, e sob pressão
regional "os pequenos são afetados e até tomados" (**cap. 1778**).

**A obsessão de gerações.** Ver §3.1 (deserto do fantasma verde e a herança do clã Qing).

**Por dentro.**
- O clã mantém **registro da alma** de seus Gu Imortais, usado para detectar impostores:
  > "You think a split soul cannot be inspected? **The details about my soul are recorded in
  > Fang clan**, any difference will result in you getting exposed." — **cap. 1860**
- Conspirações de cúpula existem e são restritas a três pessoas: "The people who were in on
  the plan … were limited to Fang clan's first supreme elder, second supreme elder, and
  third supreme elder" (**cap. 1861**) — os anciãos supremos escondem planos até dos
  próprios rank 6 de elite.
- O clã **recruta ativamente** cultivadores solitários fortes, sobretudo de caminho da
  sabedoria: "With this personality and ability, he is not blindly arrogant, there is great
  benefit in getting him to join Fang clan" (**cap. 1521**); "Fang clan was already very
  polite, of course, the reason was that Fang Yuan had great strength and was a rare wisdom
  path Gu Immortal, **Fang clan wanted to recruit him**" (**cap. 1520**).
- E é **implacável com aliado que passa a estorvar**: em **cap. 1860** os três anciãos
  supremos conspiram para eliminar um aliado com quem tinham acordo, "we used almost all our
  strength to scheme against him and even **detonated an Immortal Gu House**".

**Alinhamento.** Caminho correto, e é chamado de "uma das forças centrais do caminho correto
do Deserto Ocidental" (**cap. 2251**). Mas o clã fecha acordos de aliança com cultivadores
demoníacos quando lhe convém, e o texto registra que basta o rumor disso para as demais
casas apertarem: "there have been rumors that you are actually the demon Fang Yuan …"
(**cap. 1775**), e depois "Fang clan was immediately met with difficulties from other
Western Desert righteous path forces" (**cap. 1616**).

### 2.2 Clã Xiao (Xiao clan) — a logística e o dinheiro

**O que domina.** O transporte e o mercado. O ativo é uma Casa de Gu Imortal em forma de
corredor:
> "Xiao clan possessed an Immortal Gu House, **Ten Thousand Li Silk Corridor**, 'ten
> thousand li' was only a general name, the entire Immortal Gu House was **far longer than
> ten thousand li**."
> "Xiao clan was **one of the richest among Western Desert's super forces**. The most
> important reason was because Xiao clan possessed this Ten Thousand Li Silk Corridor."
> "Xiao clan spread Ten Thousand Li Silk Corridor everywhere, transporting goods and
> earning a fortune. **However, Ten Thousand Li Silk Corridor's usage consumed large
> numbers of mortal spider Gu.** … Ten Thousand Li Silk Corridor was **Xiao clan's economic
> lifeline**, thus Xiao clan had to gather a very large quantity of mortal spider Gu every
> year to maintain [it]. Despite Xiao clan's own management fulfilling a portion of the
> requirement, **there was still a shortfall left, which would have to be filled by
> purchasing large numbers of mortal spider Gu from the market**." — **cap. 837**

Isto é uma **vulnerabilidade econômica declarada**, e a mais jogável da região: a espinha
logística do clã mais rico do Oeste roda a consumo de Gu-aranha mortais, e o clã **não
consegue produzir tudo o que gasta**. Quem controla oferta de Gu-aranha tem a mão na
garganta do clã Xiao.

**A caçada às rainhas.** Para produzir Gu-aranha, o clã caça **rainhas de aranha de areia
oculta** (*hidden sand spider queens*) — operações com **cinco Gu Imortais de rank 6** em
campo mais Mestres Gu em formação de batalha contra enxames de trinta mil aranhas; "Xiao
clan Gu Masters had exemplary skill in battle, they also had **rich experience in dealing
with hidden sand spiders**" (**cap. 836–837**).

**Liderança e quadros.** Um **primeiro ancião supremo** que decide sobre parcerias e sobre a
entrega de tokens (**cap. 837**); **cap. 2255** registra que Xiao e Tian "had many Gu
Immortals and even had **rank eight Gu Immortals leading them**". Na ponta operacional, a
dupla **Xiao Hu Chi** (o braço) e **Xiao Shi Rang** (a cabeça — "stable personality and
quite wise"), conhecidos como "Xiao clan's **brains and brawn duo**" (**cap. 907**).

**Do que vive.** Transporte por corredor + a maior rede de parceiros comerciais da região,
empatada com a do clã Tian (**cap. 908**). Além do token de transação, existe um **token de
nó** (*node token*) que dá acesso aos nós do corredor (**cap. 837**).

**O lado sujo.** Comércio de almas:
> "Xiao clan was a super force, it was not hard for them to obtain souls. **But if the soul
> transactions were exposed, Xiao clan would never admit they were involved. The trading of
> souls could not be done openly, Xiao clan was, after all, a righteous path super
> force.**" — **cap. 996**

**Rivalidades.** Concorrente principal: **clã Tian** (**cap. 908**). Disputa aberta com o
**clã Dong** pelo mercado do noroeste da região — e a arma dessa disputa é a velocidade de
expansão do corredor: "The most important thing right now is the contest with Dong clan to
occupy the market in the northwest side. **We need to spread Ten Thousand Li Silk Corridor
as fast as possible.**" (**cap. 837**).

> Cuidado de leitura: existe também um **clã Xiao na Fronteira Sul**, decaído, e a obra diz
> que corre o rumor de terem a mesma origem, separados há mil anos por conflito interno,
> com o lado perdedor migrando para o sul (**cap. 962**). São duas casas distintas; quase
> tudo que se lê sobre "Xiao clan" nos capítulos 300–1000 do lado sul é do clã sulista.

### 2.3 Clã Tian (Tian clan) — a administração de aberturas imortais

> "First is Tian clan. This clan **mainly cultivates wood path and earth path**, and are
> mainly renowned for their **immortal aperture management**, and even have good reputation
> in the other four regions. In the current Western Desert Gu Immortal world, it is
> **one of the super forces with the most solid foundations**." — **cap. 1436**

- Controla um dos **três afluentes do Rio do Tempo** existentes no Deserto Ocidental
  (**cap. 1436**).
- Empata com o clã Xiao no maior número de parceiros comerciais; os dois são
  **os maiores concorrentes** entre si, e os dois tokens de transação são mutuamente
  excludentes na prática (**cap. 908**).
- **cap. 2255:** Xiao e Tian "were normally thought of highly by Gu Immortals, because
  during the past peaceful era, **these two had the largest businesses**. They had many Gu
  Immortals and even had **rank eight Gu Immortals leading them**."
- Recruta fora da linhagem: um de seus imortais "was not a lineal descendant of Tian clan,
  he had been a lowly young boy with no cultivation aptitude whose only fate was to become a
  farmer. He cultivated secretly at first, but was discovered soon after, and **had no
  choice but to offer the Gu Immortal inheritance to Tian clan**" (**cap. 2258**) — retrato
  de como uma super força do Oeste absorve uma herança encontrada por um plebeu.

Por que caminho da madeira e da terra: INDUÇÃO — a obra não dá a razão histórica. Mas
madeira é o recurso mais escasso do Oeste (o atlas registra a afirmação canônica de que a
escassez de plantas é o maior ponto fraco da região), e "gestão de abertura imortal" é
exatamente o serviço de fazer uma abertura render — solo, plantio e terreno. Combina.

### 2.4 Clã Tang (Tang clan) — a aposta no caminho do sonho

**Estado presente.** Casa em declínio, escalão médio-baixo entre as super forças:
> "Tang clan is a **declining clan**, its strength is **mid-lower tier** among Western
> Desert's super forces. But they still have an Immortal Gu House and **has control over a
> tributary of the River of Time, which is right by their headquarters**. With their
> powerful defensive strength, other forces cannot easily seize it." — **cap. 1436**

**A estratégia de casa.** "**Tang clan's grand strategy was to develop dream path.**"
(cap. 1436). A origem é um achado:
> "As a super force of Western Desert, Tang clan had **accidentally discovered Thieving
> Heaven Demon Venerable's dream realm** many years ago. This discovery triggered the
> enthusiasm of Tang clan in researching dream path." — **cap. 775**

**O retorno até agora é magro, e a obra faz questão de dizer:**
> "our Tang clan has already explored the dream realm for **sixty years**, we have only
> created **over a dozen dream realm mortal Gu, they are all rank three and below. More than
> half of them have extremely limited use.** More specifically, only four or five are suited
> for dream realm exploration." — **cap. 775**

**Liderança.**
- **Primeiro ancião supremo: Tang Yang** (**cap. 775**). Sua doutrina, dita em reunião:
  > "**If Tang clan wants to rise, we must take such risks. Riches and fortune are found in
  > danger** … As for [os dois enviados], they are already aware. **Sacrificing for the clan
  > is the greatest honor.**" — **cap. 1438**
- **Segundo ancião supremo** — a voz cautelosa, que se opôs à aposta arriscada e sofre com
  a pressão externa (**cap. 1438**).
- **Terceiro ancião supremo** — aparece defendendo o gasto do clã na manutenção da vida de
  um membro precioso (**cap. 775**).
- **Tang Fang Ming** — "Tang clan's **number one genius Gu Immortal**", o criador da maior
  parte dos Gu de caminho do sonho da casa: "These dozen or so dream path mortal Gu were
  mostly his creation. One could say that he was **the main force behind Tang clan's dream
  realm exploration**" (**cap. 775**).
- **Tang Lan Ke** — rank 7, **caminho do tempo**, encarregada do afluente do Rio do Tempo
  (**cap. 1437**).
- **Tang Miao** — irmã de Tang Fang Ming, feita imortal com ajuda da casa (**cap. 775**).

**Assinatura.** O golpe imortal **Steal Dream** (Roubar Sonho): permite **retirar um reino
onírico de dentro de uma gruta-céu e movê-lo para outro lugar**, para depois devorá-lo no
próprio ritmo (**cap. 776**). É a única técnica da região descrita como capaz de arrancar um
reino onírico do lugar.

**Cultura interna — a mais dura do Oeste.**
> "Tang clan was weak, the external pressure on them was enormous. Such an environment made
> almost all the Tang clan Gu Immortals possess **the spirit of going all out, taking risks,
> bearing hardships, and enduring patiently**." — **cap. 1436**

E a contraface: a casa **sacrifica os seus** com frieza contábil. Tang Fang Ming, ainda
mortal, foi "stripped of his status and mercilessly abandoned by Tang clan's Gu Master
higher-ups when he was young"; quando virou imortal, os anciãos supremos **sacrificaram
aqueles mesmos dirigentes mortais** para comprar sua volta (**cap. 1437**, **cap. 775**). E
quando o clã negocia algo comprometedor, escala dois membros como **bodes expiatórios
prontos**: "Tang clan threw him and Tang Lan Ke out as scapegoats to maintain their
righteous path identity. **They would be the cover to hide the clan's disgrace if this
matter was exposed in the future**" (**cap. 1437**) — e os dois sabem, e coletam provas um
contra o outro para o dia em que a conta chegar.

**Alinhamento.** Caminho correto no papel, e a obra mostra a casa **negociando em segredo
com uma organização do caminho demoníaco** para conseguir pesquisa de caminho do sonho,
sabendo que a exposição a destruiria: "After all, Tang clan was a righteous path force but
was cooperating with the demonic path's Shadow Sect, **if this was exposed, they would be
denounced and there would be immense trouble**" (**cap. 1436**).

**Do que vive.** A obra não descreve base econômica própria além do afluente do Rio do Tempo
e da Casa de Gu Imortal; registra, ao contrário, **gasto**: o clã pagou "a huge sum" para
tomar emprestado um Gu Imortal de rank 7 de caminho da emoção do "Xiao tribe" e comprou no
mercado, com somas enormes, todo o estoque de *guts Gu* disponível para manter um membro
vivo, até secar a oferta (**cap. 775**). É uma casa **descapitalizando-se por uma aposta**.

> Nota de recorte temporal: a obra descreve um futuro possível em que o caminho do sonho
> floresce e essa casa vira a força número um do Oeste — a chamada "Era Tang" (**cap. 776**,
> **1437**). **Isso fica fora da nota final**: é evolução de enredo, não estado presente. O
> que entra é o que a designer precisa: uma casa em declínio que apostou tudo num caminho
> exótico e ainda não recuperou o investimento.

### 2.5 Clã Dong (Dong clan) — a terra e a roda

- **Super clã**, especializado em **caminho da terra**: "Dong clan **specialized in earth
  path**" (**cap. 1780**).
- **Primeiro ancião supremo: Dong Lu Chen**, ele próprio um Gu Imortal de caminho da terra
  (**cap. 1780**, **cap. 1851**).
- **Assinatura:** a Casa de Gu Imortal **Red River Wheel** (Roda do Rio Vermelho), rank 7,
  "obtained by Dong clan from **a mysterious inheritance**"; ganhou grande fama.
  Sua fraqueza tática é declarada: "**Red River Wheel is strongest at the front and back,
  but the sides are the weakest**" (**cap. 1708**, **1925**). O clã a fortalece com
  **pássaros de chama derretida** capturados, sobretudo em velocidade (**cap. 1708**).
- **Território:** faz fronteira com o clã Fang; o **oásis da lua do tesouro** (*treasure moon
  oasis*) é um ponto de recurso de porte médio seu — e ali está **o túmulo da esposa de
  Dong Lu Chen** (**cap. 1779–1780**).
- **Rivalidades:** disputa o mercado do noroeste com o clã Xiao (**cap. 837**); vizinhança
  tensa com o clã Fang, com a lógica explicitada pelo próprio Dong Lu Chen: "**Dong clan and
  Fang clan shared borders, when Fang clan gets stronger in the future, they would first eat
  into Dong clan's territory and benefits**" (**cap. 1851**).
- **Como a região faz política, num exemplo só:** quando o clã Fang perdeu um imortal por
  mão desconhecida e o método usado era de caminho da terra, Dong Lu Chen percebeu na hora
  que estava sendo **incriminado** — e concluiu que não podia se defender em público, porque
  "if he shouted about his innocence now, wouldn't it show that he was afraid of Fang clan?
  That would not only taint Dong Lu Chen's reputation, **the whole of Dong clan's prestige
  would be affected**". Manteve postura dura por fora e cobrou indenização, torcendo por
  dentro para que a investigação do rival o inocentasse (**cap. 1780–1781**). Ambos os clãs
  acabaram concluindo que terceiros os manipulavam, "**but Fang clan and Dong clan were
  calm, they did not go to question the others, they only remembered this in their hearts**"
  (**cap. 1851**). É o retrato exato do jogo de prestígio do Oeste.

### 2.6 Clã Wan (Wan clan) — a luz e o juízo político

- **Super clã** do caminho correto, com **rixa profunda e antiga com o clã Fang**: "Wan clan
  and Fang clan have **deep grudges**" (**cap. 2222**).
- **Primeiro ancião supremo: rank 7**, sem força de combate notável, mas com uma qualidade
  rara e nomeada: "Wan clan's first supreme elder **only had rank seven cultivation and did
  not have outstanding battle strength, but he possessed an intuitive view of the big
  picture**" (**cap. 2248**). É o líder-político da região, não o líder-lutador.
- **Assinatura:** a Casa de Gu Imortal **Winding Light Platform** (Plataforma da Luz
  Sinuosa), manejada pessoalmente pelo primeiro ancião supremo; seu método mais forte prende
  um alvo sob um feixe de luz amarela e o esmaga em cerca de dez respirações (**cap. 2248–2249**).
- **Quadros:** **Wan Hao Guang**, coberto por uma armadura de luz que emite calor
  extremíssimo (**cap. 1799**); **Wan Xiao**, rank 7, guardião de ponto de recurso
  (**cap. 2247**); **Wan Liang Han**, Gu Imortal de caminho da sabedoria (**cap. 1801**);
  **Wan Zhui Qing** (**cap. 1802**).
- **A casa cultiva caminho da sabedoria**: "It was not easy to raise a wisdom path Gu
  Immortal, Wan Liang Han's death was **a heavy loss to Wan clan**" (**cap. 1801**).
- **Território:** o **oásis dos pinheiros altos** (*tall pine oasis*) é seu ponto de recurso
  (**cap. 2248**) — segundo o atlas do vault, um "super ponto de recurso" renomado nas cinco
  regiões.
- **O esqueleto no armário:** **Old Man Lie Shen**, Gu Imortal de caminho da sabedoria do
  próprio clã Wan que, por acidente de cultivo, "**lost himself and became a lunatic**";
  rank 7, ficou mais forte depois de enlouquecer, "caused huge losses to Wan clan and even
  slaughtered Gu Immortals of other righteous path forces" (**cap. 1799**). Um monstro
  produzido pela casa e solto no mundo — gancho pronto.
- **Como faz política:** o clã Wan é quem **articula coalizões** contra quem cresce demais,
  visitando clã por clã e usando linguagem moral: "Fang clan is the biggest demon's nest in
  Western Desert! **Your clan is one of the core forces of Western Desert's righteous path,
  can you stand by and watch this situation?**" (**cap. 2251**).

### 2.7 Clã Shi (Shi clan) — o minério

- **Super força do caminho correto** (**cap. 1474**).
- **O que domina:** o **deserto das miríades de minérios** (*myriad ore desert*), "famous"
  na região, sob seu controle; o clã destaca um Gu Imortal para guardar o lugar "while
  simultaneously **excavating immortal ores**" (**cap. 1474**, **cap. 2222**).
- **Primeiro ancião supremo** decide as designações de guarda (**cap. 1474**).
- **Quadros e política interna, um caso exemplar:** **Shi Zhong**, rank 7, é **ostracizado**
  pelos próprios: herdou por regra familiar uma herança com **vários Gu Imortais**, o que
  deixou os demais imortais do clã com inveja — "It was a pity that **taking over the
  inheritance had rules and could not be broken**" —, e por isso foi mal tratado desde
  jovem e acabou **enviado para guardar o deserto de minérios**, um posto que faz fronteira
  com super forças inimigas, perigoso, vigiado por formação o tempo todo e sem margem para
  lucro pessoal (**cap. 1474–1475**). Exílio disfarçado de promoção.
- No outro extremo, **Shi Kang**, "a popular person in Shi clan", estrela em ascensão,
  defensivamente muito forte, que venceu todos os concorrentes e ficou com a **terra
  abençoada Monte de Areia** (*Sand Heap blessed land*) (**cap. 2222**, **cap. 2255**).
- **Território:** o clã Shi faz vizinhança com os clãs Zuo Qiu e Tuoba, e os três circulam
  juntos e caçam juntos (**cap. 2222**).

### 2.8 Clã Mo (Mo clan) — o senhorio do deserto dos lobos

- "**Mo clan was a super force in western desert, an overlord that dominated a territory**"
  (**cap. 675**).
- **Território:** o **deserto do lobo** (*wolf desert*); "this place was wolf desert, the
  territory of Mo clan. **Stealing this ancient desolate plant was the same as stealing the
  Mo clan**" (**cap. 1973**).
- **Cidades:** **Cidade do Lobo de Areia** (*Sand Wolf City*), "one of the main cities of Mo
  clan" — cidade de pedra no centro de um oásis vasto, muralhas baixas e longas, população
  mortal enorme, entrada a **uma pedra primordial por pessoa**, com um **senhor da cidade**
  (*city lord*) que recebe os imortais visitantes com banquete (**cap. 1973**).
- **Caravanas próprias**, com líder de caravana identificado e de rank 5 (**cap. 693**).
- **Composição de caminhos:** o clã tem Gu Imortais de **caminho da sabedoria** (que cobram
  essência imortal até de colegas de clã pelas deduções — "the wisdom path deductions would
  still cost Immortal essence, they could not work for Plump Lady for nothing, right?") e de
  **caminho da formação** (**cap. 1973**).
- **Recrutamento — o traço mais jogável da casa:** o clã manda os senhores das cidades
  selecionarem **Mestres Gu de aptidão grau A e lealdade comprovada** para serem nutridos
  como sementes de futuros imortais, e a ordem vem "dos superiores". A frase de uma moradora
  resume o critério: "**Aptitude is not too important, loyalty to Mo clan is most
  important.** If we show enough loyalty, our son might be selected." (**cap. 1973**)
- **Figura conhecida:** a imortal apelidada **Plump Lady** (Senhora Rechonchuda), com título
  próprio no mundo dos Gu Imortais do Oeste; monta uma nuvem amarela, mantém uma "fazenda de
  areia" própria (**cap. 1973**).

### 2.9 Clã Gong (Gong clan) — a maldição a distância

> "Second is Gong clan. Gong clan Gu Immortals are **proficient in long range fighting
> methods, especially their curse related killer moves**, which are imperceptible and can
> silently take their enemy's life even when they are separated by an enormous range. Their
> most famous immortal killer move, **bow shadow cup**, had terrorized the whole of Western
> Desert's Gu Immortal world. **They only need a trace of the target's shadow, after which,
> they can activate the killer move and can kill their target no matter how far apart the
> distance.**" — **cap. 1436**

- Controla um dos **três afluentes do Rio do Tempo** do Deserto Ocidental (**cap. 1436**).
- Quadro citado: **Gong Jiao Che**, conhecido por seus feitos de batalha, que ataca a
  distância (**cap. 2255**, **cap. 2259**). Há também menção a "Gong clan's second young
  miss Gong Wu Hua" (**cap. 1682**).
- **Por que essa especialidade cabe no Oeste (INDUÇÃO):** a obra não explica a origem, mas
  numa região de campo aberto sem cobertura, onde qualquer um é visto de longe, a arma
  decisiva é a que **mata sem aproximação e sem testemunha**. Uma casa de maldição a
  distância é a resposta lógica ao terreno.

### 2.10 Clã Lin (Lin clan) — o osso

- Uma das catorze super forças (**cap. 2255**).
- **Território nomeado:** a **Montanha do Esqueleto** (*Skeleton Mountain*), **ponto de
  recurso de caminho do osso**, defendida por **Lin Lun Zhou**, Gu Imortal **rank 7 de
  caminho do osso** com "huge territorial advantage" ali; e o **oásis do espírito gigante**
  (*giant spirit oasis*), descrito como **super ponto de recurso** do clã, "heavily protected
  and could not be lost" (**cap. 2303**).
- **Primeiro ancião supremo** existe e é figura de peso regional, citado com reconhecimento
  por imortais do Tribunal Celestial; num momento estava em **cultivo fechado**, e o
  **segundo ancião supremo** assumiu, mobilizando **duas Casas de Gu Imortais** do clã
  (**cap. 2302–2303**).
- **Doutrina defensiva:** sob ameaça, o clã "reinforced the immortal formations in many
  resource points, and **almost all the formations had the ability to transport people**"
  (**cap. 2303**) — a rede de formações do clã Lin é também uma rede de teleporte interno.

### 2.11 Clã Sun (Sun clan) — a casa medrosa

- Uma das catorze (**cap. 2255**). Tem **primeiro ancião supremo** e sede própria
  (**cap. 2251**).
- **Caracterização canônica, e é ótima:** "**Sun clan is the most timid among Western
  Desert's super forces.** It is not strange for Sun clan's first supreme elder to say that.
  It is already his greatest sincerity to be here expressing his stance." — **cap. 2251**.
  A tática da casa é declarar apoio moral e adiar o compromisso material: promete entrar
  "se" os outros entrarem primeiro.
- Seus imortais são **os mais conservadores em combate**: ao primeiro sinal de risco, o
  representante "immediately ran away with an astonishing speed" (**cap. 2259**).
- **Quadro citado:** **Sun Wang**, sem grande força de combate mas "extremely proficient in
  **investigative killer moves**" (**cap. 2255**) — a casa medrosa é, coerentemente, a casa
  dos olheiros.
- **Um imortal de sobrenome Sun que é o oposto do clã:** **Sun Cu**, **rank 6**, caminho da
  terra, **caminho correto**, dono do *turn rock Gu* (Gu de virar rocha), com o qual
  **transforma areia em rocha para que se possa construir no deserto**; "he was very popular
  and received gratitude from the people". Descrito como bondoso mas sem firmeza, apegado à
  família e à neta. Já era imortal havia mais de uma dúzia de anos (**cap. 425**,
  **cap. 545**). INDUÇÃO: a obra **não** diz que ele pertence ao clã Sun — só compartilha o
  sobrenome. Registrar como imortal do Oeste, não como membro do clã.

### 2.12 Clãs Zuo Qiu e Tuoba — os vizinhos do minério

- Ambos entre as catorze (**cap. 2255**). Sobrenomes compostos.
- **Territórios contíguos** aos do clã Shi; os três se frequentam, caçam em conjunto e
  alinham posições políticas antes de decidir qualquer coisa (**cap. 2222**).
- **Zuo Qiu San Sha** criou o golpe imortal **state of disunity** (estado de desunião), que
  **restringe Casas de Gu Imortais** — a contrapartida do *roof tile breaker* do clã Fang;
  é descrito como "the key person to suppress Fang clan" (**cap. 2258–2259**).
- **Zuo Qiu Yan Ming** — imortal mulher, voz política ponderada da casa (**cap. 2222**).
- **Tuoba Feng Yan** — analista político da casa: sua leitura sobre a dificuldade de
  mobilizar clãs de fronteira é tratada como referência pelos vizinhos (**cap. 2222**).
  **Tuoba Cheng Feng** — combatente (**cap. 2258–2259**).

### 2.13 Clã Qin (Qin clan) — só o nome

Uma das catorze (**cap. 2255**). A obra dá **apenas o nome** e um quadro, **Qin Lang**,
enviado a uma expedição conjunta (**cap. 2255**). Nenhuma especialidade, território ou
liderança declarada. `—`

### 2.14 Clã Xi (Xi clan) — a divergência de lista

Aqui há uma **inconsistência que vale registrar**, em vez de esconder:

- **cap. 673:** "Xi clan's **rank eight ancestor, Xi Jian Ping**, exited his seclusion and
  **suppressed all the experts forcefully, his might awing the entirety of the great
  desert**; the thousand wish tree was taken away by Xi clan and planted at Xi clan's
  blessed land." — um dos raros momentos em que um único imortal impõe ordem à região.
  (Contexto: memória de uma linha do tempo anterior narrada pelo protagonista.)
- **cap. 1727:** entre os grandes que ficaram em casa numa mobilização mundial, "**Many
  experts like Xi clan's first supreme elder** did not join the battle, they were staying in
  Western Desert" — o primeiro ancião supremo do clã Xi é citado como exemplo do escalão
  mais alto da região.
- **cap. 1807** e **cap. 1988:** o clã Xi tem cena própria e seu primeiro ancião supremo
  comenta a política mundial de dentro de uma sala de cultivo fechado.
- **Mas o clã Xi não aparece na lista das catorze super forças do cap. 2255.**

Duas leituras possíveis, e a obra não decide: ou o clã Xi não é formalmente "super força"
apesar de ter um rank 8, ou a lista do cap. 2255 é posterior a alguma mudança. Para a nota
final: listar Xi como **casa nomeada de primeira grandeza fora da lista das catorze**, com a
divergência declarada.

### 2.15 Clãs Lan e Huang — a escala de baixo

Duas casas pequenas, e as duas valem ouro para a designer porque mostram **como é a vida
abaixo das super forças**.

**Clã Lan** (*Lan clan*), do **oásis Zhou Xi** — um oásis pequeno, com lago azul e mercado
próspero, e **sem nenhum Gu Imortal** ("According to normal circumstances, such a small
oasis would not be a strong force, there should not be Gu Immortals here. If there were,
they would have expanded or modified this oasis already" — **cap. 694**).
- **Manda quem:** um **líder de clã idoso** (*elderly clan leader*), mortal-Mestre Gu.
- **Doutrina declarada:** "**Our Lan clan has been neutral for many generations, we have not
  meddled with the outside world.**" — neutralidade explícita, geração após geração
  (**cap. 694**).
- **Reflexo de honra apesar da fraqueza:** diante de uma exigência monstruosa, os
  clânicos gritam "**our Lan clan has no cowards**", enquanto o líder tenta comprar a paz —
  o conflito entre a prudência do chefe e a honra da base é encenado na hora (**cap. 694**).
- **Do que vive:** cria **gaivotas-de-areia** (*sand gulls*) em número muito maior que outras
  forças do mesmo porte, com um criadouro subterrâneo cheio de ovos; a suspeita registrada é
  que possuam uma **técnica secreta para aumentar a fertilidade** dessas montarias
  (**cap. 695**). Guardam também um **tesouro de Gu mortais** atrás de porta de pedra com
  alarme e lâminas de luz douradas — "**Lan clan's Gu worm treasury, the foundation of their
  entire clan**" (**cap. 695**), e uma reserva estimada em **ao menos cem mil pedras
  primordiais**.

Por que a gaivota-de-areia importa: "Sand gulls could **run rapidly in the desert, while
also flying in the sky and carrying people**, they only ate grass and drank clean water,
they were easy to feed. With a mild temperament, they were **the most common steed among
western desert Gu Masters**. The only problem was, sand gulls had **very low fertility**.
Three to four out of ten sand gull eggs would usually hatch" (**cap. 695**). Ou seja: um
clã pequeno e neutro que domina em segredo a reprodução da montaria padrão da região é
**dono de um gargalo econômico regional** — e é exatamente por isso que ele é um alvo.

**Clã Huang** (*Huang clan*), do **oásis Sha Jing** — "**an upper tier force** [with]
hundreds of years of history here, they occupied the most important resources at the center
of this oasis", com forças pequenas submetidas no anel externo e aldeias mortais na franja
(**cap. 674**). É o modelo canônico do senhorio de oásis. (Atenção: existe um clã Huang
homônimo na Fronteira Sul, em Huang Jin Mountain, nos caps. 241–244 — não é o mesmo.)

---

## 3. O que não é clã: heranças sem dono, uma cidade não-humana e os demoníacos

### 3.1 Clã Qing (Qing clan) — a super força extinta, e o buraco que ela deixou

> "This Qing clan was also a super force, but a **long exterminated one**. The one who
> slaughtered the entire Qing clan was none other than the young Spectral Soul Demon
> Venerable. Before Spectral Soul Demon Venerable became a venerable, because of a certain
> irreconcilable conflict, he fought against the **entirety of Qing clan alone**. …
> Unfortunately, **Qing clan belittled Spectral Soul because of their superiority in numbers
> and assets.** … In the end, he arrived at Qing clan's headquarters and fought an intense
> battle, slaughtering the entirety of Qing clan." — **cap. 1507**

- **Que casa era:** um **clã supremo do caminho da madeira** — "he murdered all of the Gu
  Immortals in this **Western Desert wood path clan overlord**" (**cap. 1412**). Base no
  **oásis Qing** (**cap. 2035**).
- **Como era por dentro** (do episódio histórico dos caps. 2035–2055, narrado como passado):
  cúpula reunida em salão frio deliberando sobre vingança e reputação; **primeiro ancião
  supremo rank 8**; **segundo ancião supremo**; imortais de rank 7 de elite tratados como
  ativos caros ("A rank seven Gu Immortal was not easy to nurture"). A preocupação declarada
  do clã ao decidir o que fazer é **a opinião das outras super forças**: mandar o rank 8
  contra um rank 7 seria "bullying the weak" e gerar boato; perder de novo era pior, porque
  "**all of the super forces in Western Desert were watching them like a joke**"
  (**cap. 2035**, **cap. 2040**). Prestígio como moeda, outra vez.
- **O que ficou:** o campo de batalha virou o **deserto do fantasma verde** — as marcas de
  dao dos golpes, os cadáveres dos Gu Imortais e as marcas da destruição de aberturas
  imortais gravadas no terreno (**cap. 1507**). O nome "fantasma **verde**" é referência ao
  próprio nome Qing (**cap. 1507**).
- **A herança condicionada:** o primeiro ancião supremo do clã Qing, antes de morrer, selou
  todos os recursos do clã e os enterrou em algum ponto do deserto do fantasma verde,
  deixando uma herança com **uma única condição para herdá-la: vingar o clã matando o
  agressor — e, se ele já estiver morto, matar sua família, amigos e discípulos**
  (**cap. 1507**). Uma herança que é um contrato de vendeta.

### 3.2 O deserto do fantasma verde (*green ghost desert*) — o maior território sem dono

- Céu coberto de nuvens escuras densas o ano inteiro, quase sem luz solar; "**a famous place
  of danger in Western Desert**" (**cap. 1412**, **1503–1504**).
- **Incontáveis feras da alma**, incluindo exemplares desolados, ancestrais e imemoriais; a
  fonte de **núcleos de alma** mais fácil do mundo — "It hasn't even been long since I
  entered green ghost desert, and I have already obtained so many soul cores" (**cap. 1503**).
- **Por que ninguém o toma:** "**most of the Western Desert Gu Immortals and clans lacked
  methods to develop it**" (**cap. 1505**). Não é falta de vontade; é falta de método. Um
  cultivador de caminho da alma que apareça ali está diante de um continente vazio.
- Recurso de superfície colhível: **impermanence rock** (rocha da impermanência)
  (**cap. 1513**).
- **Quem está de olho:** o clã Fang, por vizinhança e por gerações de busca; e cultivadores
  solitários de caminho da alma, como o citado **Old Ghost Bai Jun** (Velho Fantasma Bai
  Jun), portador de um **Gu Imortal de rank 8, o Soul Beast Token** (Ficha da Fera da Alma),
  cujo plano é controlar uma fera da alma imemorial, usá-la para controlar um exército de
  feras da alma, e por meio dele **controlar o deserto inteiro** (**cap. 1504**, **1507**).
  Ele negocia de igual para igual com o primeiro ancião supremo do clã Fang e exige, como
  compensação, "you will not be allowed to take a single step in green ghost desert for the
  next few hundred years" (**cap. 1504**).

### 3.3 O Palácio do Feijão Divino (*Divine Bean Palace*)

- **Casa de Gu Imortal de rank 8**, criada pelo **Venerável Imortal Lótus Gênese** e deixada
  no Deserto Ocidental (**cap. 1507**, **1508**).
- Passou por mãos mortais depois que uma vila foi soterrada por tempestade de areia, e
  acabou com o clã Qing — que se orgulhou disso de forma arrogante, o que ajudou a
  desencadear seu extermínio (**cap. 1516**).
- Antes de cair, o primeiro ancião supremo do clã Qing **enfiou a herança do clã dentro do
  Palácio** e montou ali um método de renascimento que não entendia por completo; os
  fragmentos de alma dos Gu Imortais do clã foram atraídos e armazenados dentro dele
  (**cap. 1516**) e acabaram formando uma **fera da alma imemorial lendária, com inteligência
  superior à humana**, chamada **Qing Chou** (**cap. 1526**, **cap. 2016**).
- **Quem o persegue:** o clã Fang, "not a matter of a generation or two, but **carried by
  generations after generations**" (**cap. 1507**) — e faz sentido, porque é o clã das Casas
  de Gu. E, de fora, o Tribunal Celestial dá ordem expressa a uma das dez grandes seitas
  antigas do Continente Central para vir subjugá-lo: "**Divine Bean Palace is making an
  appearance in Western Desert … we can't let it fall into Western Desert's hands**"
  (**cap. 1508**). O Oeste tem um tesouro que o centro do mundo não quer que o Oeste fique.

### 3.4 A Cidade Sagrada da Pena (*Sacred Feather City*) — a única organização não-clânica

- **O que é:** ao mesmo tempo uma cidade, um povo e **uma Casa de Gu Imortal** — "Sacred
  Feather City **was a huge Immortal Gu House!**" (**cap. 865**); "Immortal Gu House Sacred
  Feather City was **the strongest headquarters of these featherman descendants**"
  (**cap. 977**).
- **Onde fica:** dentro de um **mundo-fragmento de céu verde**, isolado do mundo exterior,
  no Deserto Ocidental — "They are a **featherman clan in Western Desert**, living for
  generations in a fragment world of green heaven" (**cap. 870**). É "um paraíso para os
  homens-pena, um dos maiores assentamentos da raça que restam no mundo".
- **Como se escolhe quem manda — o sistema mais original da região:** morto o rei, o
  sucessor é decidido **por combates numa arena**, diante de dezenas de milhares de
  espectadores, com um **ancião apresentador** anunciando o vencedor. Mas a luta é a segunda
  etapa: **para ser candidato é preciso ser reconhecido pela maioria dos habitantes da
  cidade**, e o reconhecimento se ganha com boas ações e contribuições. "The feathermen did
  not want a fierce or tyrannical ruler, **they wanted a compassionate hero**. … In most
  cases, **the evaluation of the citizens was accurate**. In the history of Sacred Feather
  City, very few evil and cruel feathermen were chosen to be king." (**cap. 864**)
- **O freio institucional:** "**there were three featherman supreme elders in Sacred Feather
  City, they were Gu Immortals who could control the situation**" — mesmo que um tirano
  passasse pelo filtro popular (**cap. 864**). Os três passam o tempo semi-adormecidos,
  conversando por sentido divino, e comentam o novo rei como quem comenta o tempo.
  Nomeados: **Zhou Zhong** e **Zheng Ling** (**cap. 865–869**).
- **A tensão interna pronta:** existe uma **linhagem real** que reivindica o trono por
  sangue — "I am the **prince** of Sacred Feather City, I will inherit the throne and defend
  the honor of our **Dan surname**!" (o príncipe **Dan Yu**) — e ela **pode perder** para um
  plebeu (**Yu Fei**, "he was originally a commoner"), e perdeu (**cap. 864**, **866**).
  Mérito contra dinastia, com o mérito ganhando, e o príncipe derrotado virando conselheiro
  do vencedor.
- **A fraqueza declarada:** "Sacred Feather City had been **peaceful for too long**, they had
  no competition with the outside world, it was like life inside a utopia. This caused their
  **defenses to be very lax**, and with the crowning of a new king, the **non-militarized**
  feathermen could not respond properly." (**cap. 864**) A utopia isolada é, do lado de fora,
  um alvo.
- **Assinatura:** o golpe imortal **heavenly wish** (desejo celeste), que **teletransporta
  todos os homens-pena da cidade de uma vez** — mas sem a Casa de Gu funcionando, exige
  essência imortal enorme e muito tempo de ativação (**cap. 865–866**). E uma **herança
  completa de caminho do vento** guardada por um dos anciãos supremos (**cap. 903**).
- **Por que são cobiçados:** homens-pena **nascem com marcas de dao de caminho da nuvem** e
  são voadores natos, com os melhores deles sendo mestres de voo (**cap. 866**) — daí serem
  "escravos de alta qualidade" e a base de todas as caravanas de super força do Oeste
  (**cap. 870**).
- **A cultura:** "even suiciding rather than lowering their heads to become slaves"; e a obra
  faz uma leitura amarga do mesmo traço — "A life of peace with plentiful resources, a
  united clan without any powerful external enemies, this instead **corroded the minds** of
  these feathermen" (**cap. 870**).

### 3.5 A filial ocidental da Aliança dos Zumbis (*Western Desert Zombie Alliance*)

A Aliança dos Zumbis é uma super força de zumbis imortais com sede no Mar do Leste e filiais
nas cinco regiões; o vault já a cobre em `05 - Sociedade/07 - As Grandes Forças do Mundo.md`.
O que é específico do Oeste:

- **Território:** o **deserto do fantasma feroz** (*fierce ghost desert*), maior produtor de
  **madeira fosforescente** (*phosphorescent wood*), material imortal de rank 6; o estoque
  acumulado da filial "was the accumulation of the Western Desert Zombie Alliance branch
  after countless years" (**cap. 1395**).
- **A base:** ao contrário da filial do norte, a do Oeste tinha por base uma **terra
  abençoada de caminho da terra**, com a **Cidade Cadáver** (*Corpse City*) — uma Casa de Gu
  **mortal** gigante — dentro dela (**cap. 1394**).
- **A manobra de sobrevivência, que é um plano de contingência exemplar:** a terra abençoada
  foi **abandonada de propósito**; os recursos foram escondidos dentro da Cidade Cadáver; a
  cidade inteira foi **movida para debaixo do deserto da translocação** (*translocation
  desert*); e uma **formação Gu defensiva** foi ativada por cima. "This method allowed
  Western Desert Zombie Alliance to **preserve most of its foundation**" — e, de fato, quando
  os Gu Imortais do Oeste invadiram a antiga terra abençoada, acharam uma casca
  (**cap. 1394**).
- **A formação:** montada com o **Gu Imortal de rank 7 Fight** (Luta, caminho da regra) e o
  **Gu Imortal de rank 6 Yellow Sand** (Areia Amarela) mais Gu mortais, aproveitando o qi de
  terra denso das cavernas e as marcas de dao de terra do local (**cap. 1395**). Um rank 6
  invasor de caminho da transformação foi morto por ela (**cap. 1393**).
- **Estado presente:** a filial foi destruída e sua herança virou **caça aberta** — "It was
  normal for the Western Desert Gu Immortals to come to search for its inheritance. **Even
  super forces would pay attention to it**" (**cap. 1395**). É o segundo grande tesouro sem
  dono da região, ao lado da herança do clã Qing.

### 3.6 Os demoníacos e os solitários do Oeste

A região **não tem um polo demoníaco organizado** como a Montanha Nevada tem no norte —
verificado: nenhuma organização demoníaca do Deserto Ocidental é nomeada na obra. O que
existe são **figuras individuais**, e a obra as trata como fenômenos meteorológicos:

- **Xi Yuan** — cultivador de **caminho da espada**, **criou o "sword abyss"** (abismo da
  espada) e **matou três Gu Imortais de rank 8** (**cap. 1432**).
- **Dao Jiu Lang** — imortal demoníaco de **caminho da lâmina**, "he had overwhelming demonic
  might, **rampaging in Western Desert**, he managed to **break the expulsion formation** and
  shook the world". Ele e Xi Yuan lutaram entre si, num combate de grande destruição
  (**cap. 1432**).
- **Wan Zi Hong** — mulher, "originally a demonic immortal of Western Desert", "a famous
  demonic path expert in Western Desert's history", **recrutada pelo Tribunal Celestial** e
  de rank 8 (**cap. 2178**, **cap. 2255**). Prova de que o centro do mundo **recruta** os
  demoníacos do Oeste em vez de só executá-los.
- **Ling Hu Xu** — "a Western Desert demonic immortal who cultivated **theft path**"
  (**cap. 2130**), nome usado como identidade reconhecível na região desde o **cap. 675**.
- **Old Ghost Bai Jun** — cultivador solitário de caminho da alma com Gu Imortal de rank 8
  (§3.2).
- **Um grande especialista de caminho do sangue de rank 8** que surge no Oeste "purposely
  finding trouble with super forces and **repeatedly attacking various resource points**",
  agindo com arrogância extrema e métodos aterrorizantes (**cap. 1915**). A obra não o nomeia.
- **Han Li** — cultivador solitário que começou **mortal**, subiu por encontros fortuitos até
  o **auge do rank 7** e virou "a famous powerhouse of western desert", causando prejuízo a
  figuras influentes das dez grandes seitas do Continente Central (**cap. 673**). O caso
  canônico de ascensão do nada no Oeste.
- **Zheng Jing Shen** — "a legendary lone cultivator tens of thousands of years ago" que
  recebeu apoio financeiro do clã Fang no início do cultivo e teve um caso de amor com uma
  ancestral do clã, mas **nunca se juntou a ele** (**cap. 1507**).

**Uma observação de peso sobre participação política:** quando o mundo inteiro se mobilizou
por um evento de escala mundial, "Over at Western Desert, even though they knew that the
issue … was severe, **only super forces participated in this**. Fang Yuan did not see any
Western Desert **lone immortals or demonic path members**" (**cap. 1708**). No Oeste, quem
faz política externa são as casas; solitários e demoníacos não têm assento.

---

## 4. Números, escalas e verificações soltas

- **Fronteira decidida por duelo entre líderes:** cap. 2040 (episódio histórico); a norma
  também aparece resumida na nota do vault `05 - Sociedade/06 - Cultura das Cinco Regiões.md`.
- **Coalizão que se desfaz:** num esforço de reunir o caminho correto do Oeste, "Western
  Desert's righteous path did not come together, **only Fang clan, Tian clan, Dong clan, Shi
  clan, and Tang clan are here**"; e no fim "**he only gathered four super clans**"
  (**cap. 1876**). Depois, quando cada casa recebeu má notícia de casa — uma besta desolada
  imemorial atacando o oásis de uma, um imortal demoníaco de caminho do sangue causando caos
  em outra —, "a portion of Sun clan and Mo clan left. **With the departure of a portion of
  Sun clan and Mo clan, the other clans also wanted to leave, otherwise, their balance would
  be disrupted**" (**cap. 1923**). Coalizão do Oeste em uma imagem: quatro de catorze
  aparecem, e basta um sair para os outros saírem.
- **O Oeste guarda seus rank 8 em casa:** numa mobilização mundial, "**Western Desert sent
  rank six and seven Gu Immortals as well as Immortal Gu Houses but did not send rank eight
  Gu Immortals**" (**cap. 1727**).
- **Casa de Gu Imortal é obrigatória no topo:** "Whether it be Southern Border, Northern
  Plains, Eastern Sea, Western Desert or Central Continent, **all powerful super forces had
  at least one Immortal Gu House as their trump card**" (**cap. 971**). Confirmado no Oeste:
  Fang (3+), Xiao (1), Tang (1), Dong (1), Wan (1+), Lin (2).
- **Cerimônia de maioridade:** "Today was the most important day of their lives, it was the
  most sacred moment, **according to Western Desert's customs, all of the youngsters had to
  be reverent and not speak unnecessarily**" (**cap. 1491**). É a única prática ritual
  regional que a obra registra — e não é religiosa, é de passagem.
- **Tempo de resposta e informação:** o comércio de caravanas faz a informação viajar rápido
  no Oeste, e um forasteiro é "marcado no momento em que entra numa cidade" (**cap. 425**).

---

## 5. O que a obra NÃO diz sobre o Deserto Ocidental

Declarado, para a designer saber onde pode inventar sem contrariar nada:

- **Nenhum templo, mosteiro, igreja, sacerdócio ou religião organizada** — verificado com
  busca exaustiva (§0). O Oeste **não** é a região religiosa da obra; não existe região
  religiosa na obra.
- **Nenhuma seita e nenhuma academia** no Oeste (a nota do atlas já registra a mesma lacuna).
- **Nenhum poder unificador**, nunca, em toda a história da região (**cap. 1435**, **1614**).
- **Nenhuma organização demoníaca nomeada** na região — só indivíduos.
- Sete dos catorze super clãs vêm **quase sem conteúdo**: Qin (só o nome), Zuo Qiu e Tuoba
  (dois nomes de imortais e a vizinhança com Shi), Lin (dois territórios e uma doutrina de
  formação), Sun (uma caracterização e um olheiro), Mo (território, cidade e recrutamento),
  Gong (uma especialidade e um golpe). Nenhum deles tem história de fundação declarada.
- **Nenhuma casa tem contagem total de Gu Imortais declarada** — só instantâneos de
  mobilização.
- **Nenhuma fronteira interna do Oeste é mapeada**; sabe-se apenas quem faz divisa com quem
  (Fang–Dong, Shi–Zuo Qiu–Tuoba, Fang–deserto do fantasma verde).
- **Nenhuma razão histórica declarada** para as especialidades de caminho de Tian, Dong,
  Gong e Lin — só o fato da especialidade. (Fang, Tang, Xiao e Shi têm a razão declarada:
  herança própria, achado de reino onírico, Casa de Gu herdada, e território mineral.)
