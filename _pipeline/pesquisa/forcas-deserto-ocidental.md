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
