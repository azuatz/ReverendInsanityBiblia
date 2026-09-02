# Varredura de grandes eventos — Capítulos 801–1200

> **Faixa:** caps. 801–1200 (Volume 4, caps. 801–1021; Volume 5, caps. 1022–1200)
> **Data:** 2026-09-02
> **Status:** em andamento

## Método

1. Índice rápido pelas notas brutas da faixa (`notas-caps-0776-0817.md` … `notas-caps-1186-1226.md`)
   e pelo **dump dos títulos de capítulo** do texto-fonte — os títulos da obra nomeiam os
   próprios eventos ("Battle of Yi Tian Mountain", "Contest Over Hei Fan Grotto-heaven",
   "Hei Tribe's Huge Battle", "Blood Plain Martial Competition"), o que dá um índice de
   eventos quase pronto.
2. Greps temáticos sempre com `grep -i` (a obra grafa nomes próprios em minúsculas), contados
   por capítulo, sobre fatias do texto-fonte recortadas exatamente na faixa:
   `beast tide`, `war`, `siege`, `invasion`, `calamity`, `blizzard`, `flood`, `plague`,
   `tournament`, `assembly`, `convention`, `auction`, `inheritance`, `grotto`, `trial`,
   `expedition`, `rebellion`, `alliance`, `tribulation`, `qi tide`, `earth tide`,
   `regional wall`, `immortal war`, `battlefield`, `fortress`, `prison`, `sect`, `hunting`.
3. Para cada candidato, leitura direta dos trechos no texto-fonte (`sed -n`), nunca só a
   nota bruta.

**Critério de inclusão:** entra o que é maior que uma briga entre pessoas — algo que uma
vila, um clã, uma região ou o mundo inteiro sente. Faixa de escala imortal: aqui a maior
parte dos eventos é de nível Gu Immortal, com mortais e rank baixo entrando como
ambientação, mão de obra, tropa ou vítima.

**Convenção de confiabilidade:** texto simples = a obra afirma; `(ded.)` = dedução segura;
`*` = invenção/indução nossa sem base textual; `—` = a obra não informa.

## Eventos únicos

### Battle of Yi Tian Mountain / "gambling contest" do Yi Tian Mountain — caps. 959-971 (1ª fase) e 998-1021 (2ª fase)

- **Tipo:** guerra por procuração + torneio apostado + cerco de fortaleza. É o evento mais
  "jogável por personagens de rank baixo" de toda a faixa.
- **Onde:** Southern Border, uma montanha sem nome que passa a se chamar **Yi Tian Mountain**
  ("montanha da lealdade/justiça"), rebatizada pelos próprios ocupantes. Ao redor dela,
  Headless Mountain (acampamento dos imortais demoníacos e solitários) e Pine Tail Mountain
  (acampamento dos imortais do path reto), a mil li de distância (cap. 961).
- **Gatilho / causa mecânica:** enterrada sob a montanha há muito tempo está a Immortal Gu
  House **Graceful Chaotic Duel Stage** (rank 8-equivalente, com segredos de food path),
  usada por seu criador rank 7 para selar sob a terra um immortal zombie rank 8 (Martial Duel
  Heavenly King, Great Strength True Martial Physique) que ele não conseguia matar (cap. 959).
  A House emite para fora uma **"forbidden zone for immortals"** (zona proibida a imortais) —
  vazamento de sua própria força — e a zona **cresce com o tempo**: já cobre milhares de li e
  chega a dez mil li (caps. 961, 963, 965). Quando um Gu Master ativa um Gu específico no topo
  (evento gatilho, cap. 959), a House volta a se manifestar em **imagens fantasmas** que
  reencenam ciclicamente a batalha histórica, e o vazamento de aura de Immortal Gu atrai
  Gu Immortals de toda a Southern Border.
- **A regra especial que define tudo:** dentro da zona proibida, **Gu Immortals não podem
  entrar** — quanto mais fundo vão, mais fracos ficam ("os membros amolecem", a immortal
  aperture é comprimida por uma força sem forma) e, calculado no texto, a abertura imortal
  seria destruída em "cinquenta ou sessenta passos" (caps. 961, 965). **Immortal Gu, porém,
  funcionam lá dentro** — com potência muito reduzida. Conjectura no texto (marcada como
  conjectura do personagem): a zona mira a *immortal aperture*, não os dao marks, e por isso
  quem selar a própria abertura e virar mortal de novo consegue entrar (caps. 965-966).
- **Prêmio:** tornar-se dono da Immortal Gu House. O immortal zombie rank 8 morreu tentando
  refiná-la e deixou lá dentro uma reserva enorme de **battle will (vontade de batalha)
  purificada e sem dono**. Quando gente luta na montanha, a vontade de lutar dos combatentes
  **ressoa** com essa reserva e converte parcelas dela em vontade de batalha *daquele*
  combatente; um Gu Immortal, plantando um Gu no corpo do combatente, colhe a conversão para
  si. Quem converter **mais de 50%** da reserva refina a House e vira o dono (caps. 963, 966).
- **Regras do "gambling contest" (o núcleo jogável, caps. 961, 963, 966):**
  - Dezenas de Gu Immortals de Southern Border — path reto, path demoníaco e solitários —
    negociaram por **sete dias e sete noites**, um representante de cada lado por dia, até
    fecharem o acordo. Quatro rank 8 compareceram (1 demoníaco, 1 solitário, 2 do path reto)
    e ficaram de fora da disputa, garantindo o equilíbrio.
  - Cada imortal **aposta** bens; a aposta define **de que rank pode ser o seu peão mortal**
    e **quando ele entra** na montanha (aposta maior = peão de cultivo mais alto e entrada
    mais cedo). Exemplos textuais: aposta pequena = 1 peão rank 3 estágio superior entrando
    só depois de três meses; aposta máxima (um rank 7 que apostou tudo que tinha) = 2 peões
    rank 5, um entrando primeiro, outro depois.
  - As apostas podem ser **aumentadas a qualquer momento** durante a disputa; retardatários
    podem entrar, desde que apostem.
  - No fim, **todo o bolo apostado é redistribuído** por ranking de quanta battle will cada
    imortal refinou — logo, aposta pequena com boa performance dá lucro enorme, e o evento
    premia *outras* competências que não a força de combate do imortal (é a chance de vida
    dos imortais de baixo escalão, que não têm Immortal Gu).
  - **Trapaça = confisco total da aposta.** Todos os participantes, inimigos mortais
    inclusive, cooperam espontaneamente para manter as regras; quebrá-las é declarar guerra
    a todos os Gu Immortals da região. Se aparecer uma ameaça externa ao evento, os
    apostadores se unem para bloqueá-la (cap. 966).
  - O peão pode ser preparado: recebe Immortal Gu implantado, immortal essence de reserva e
    lotes de battle will do patrono, além de "ajustes no corpo por uma técnica simples de
    wisdom path" para servir de vaso de conversão (caps. 963, 965).
- **Ambiente por dentro:** a montanha vira uma aldeia-fortaleza (**Yi Tian Village**) erguida
  por Gu Masters do path demoníaco, que recebe qualquer demoníaco fugitivo; do lado de fora,
  clãs do path reto sitiam. A guerra é travada **inteiramente por mortais de rank 3 a 5** —
  rank 5 é o teto do mundo mortal. Nenhum imortal pode pisar no campo. As imagens fantasma da
  batalha antiga continuam reaparecendo no cume durante todo o evento (cap. 961).
- **Duração:** a condição declarada da herança que move o líder da aldeia é **aguentar cem
  dias** de cerco (cap. 963). A montagem do evento (chegada dos imortais, negociação, primeiras
  entradas) toma mais de dez dias só de espera antes do acordo.
- **Fases:** (1) manifestação da House e das imagens fantasma; (2) corrida e sondagem
  individual dos imortais, todos repelidos pela zona proibida, inclusive os rank 8; (3)
  negociação de sete dias e criação do contrato de apostas; (4) recrutamento e plantio de
  peões mortais dos dois lados; (5) fundação da aldeia e cerco; (6) cem dias de batalha
  escalando conforme peões de rank maior vão sendo liberados; (7) conversão da battle will e
  apuração; (8) segunda fase, anos depois, quando a disputa recomeça em escala imortal
  (caps. 998-1021) com tribulações caindo sobre o campo e várias Immortal Gu Houses em jogo.
- **Papel possível de um grupo pequeno:** este é *o* evento da faixa desenhado para
  personagens fracos. Os jogadores são exatamente os peões: Gu Masters mortais rank 3-5,
  cada um patrocinado (sabendo ou não) por um Gu Immortal distante que os equipou e não pode
  socorrê-los. Ninguém acima do rank 5 pisa no campo. Ganchos naturais: descobrir que se é
  peça de aposta; ser peão dos dois lados do mesmo patrono; a aldeia sitiada precisando de
  suprimentos, muros, recrutamento e moral por cem dias; imortais tentando burlar a zona.
- **Consequência para o mundo:** a Immortal Gu House muda de dono e o immortal zombie rank 8
  selado embaixo entra em jogo; a zona proibida some quando a House é refinada; o mundo
  imortal de Southern Border sai com um novo mapa de dívidas e alianças, porque as apostas
  redistribuídas movem fortunas entre dezenas de imortais.
- **Cuidado de spoiler:** fica de fora quem venceu a disputa, o destino dos dois peões rank 5
  do clã Xiao (a traição fratricida montada pelo supreme elder deles), a identidade do
  criador da House e o que a segunda fase (caps. 1002-1021) revela sobre uma figura de nível
  Venerável. Nada disso é necessário para rodar o evento: basta o mecanismo.
- **Lacunas:** a obra não dá o número total de peões nem de imortais apostadores ("dezenas");
  não diz qual é o piso de aposta; não descreve as regras internas de combate da aldeia.

### Defesa de Lang Ya blessed land — quarta onda de invasão — caps. 872-887

- **Tipo:** cerco/defesa de uma blessed land sem dono; batalha de imortais com mercenários
  contratados.
- **Onde:** Northern Plains. **Lang Ya blessed land** é a abertura imortal deixada por
  **Long Hair Ancestor**, rank 8, apontado como possivelmente o maior imortal de refinement
  path da história (38 Immortal Gu refinados em registro oficial; boatos falam em mais de
  cem). Ela é **ownerless** (sem dono) e é administrada pelo seu **land spirit** (espírito da
  terra) — logo é um cofre gigantesco sem proprietário para defendê-lo (cap. 872).
- **Gatilho / causa mecânica:** riqueza sem dono atrai ondas sucessivas de Gu Immortals
  invasores. Na cronologia da obra, Lang Ya resistiu a **três ondas anteriores**; esta é a
  **quarta**, e é a primeira em que o land spirit pede reforço externo. (Registro histórico
  citado de segunda mão: em outra linha temporal a blessed land chegou a resistir a **sete
  ondas**, e a sétima foi conduzida pela própria Heavenly Court — ver "Eventos históricos".)
- **Como se invade uma blessed land (regra do mundo, cap. 888, aplicada aqui):** o primeiro
  obstáculo é a **entrada** (entrance). Fechada a entrada, a abertura imortal vira um mundo
  isolado; não basta saber onde ela fica nem rasgar o espaço — é preciso *conectar-se* ao
  interior. Os métodos vistos: usar um parente de sangue do dono com técnica de blood path,
  ou usar a **alma de um agente infiltrado** que já esteja dentro. Foi o segundo método aqui:
  a organização atacante plantou, ao longo de gerações, **três Gu Immortals hairy men como
  agentes infiltrados** via killer move de possessão ("soul replacement") — processo que
  exigiu pelo menos 300 anos para plantar os três (caps. 883-885).
- **Forças presentes (como tipos):**
  - *Atacantes:* um grupo de **sete Gu Immortals** — cinco rank 7 (entre eles o mais forte
    lone cultivator da região, um imortal de transformation path com três transformações de
    lobo desolado, e um imortal de uma super força trazendo a Immortal Gu House **Dark
    Prison**, rank 6, com um ancient desolate beast dentro) e dois rank 6 (cap. 873). O
    líder possui um método raro para **arrancar Immortal Gu alheios à força** sem provocar
    autodetonação — exceção notável à regra geral de que roubar Immortal Gu é quase
    impossível.
  - *Defensores:* o land spirit; **doze desolate beasts** (um sob cada cloud building); um
    contingente oculto de **Gu Immortals hairy men** criados dentro da blessed land como
    refinadores — excelentes em refino, **péssimos em combate** (choram, entram em colapso
    mental diante de inimigos: tropa de apoio, não de linha); e **mercenários imortais
    contratados de fora**, recrutados por pedido de socorro com pagamento negociado
    individualmente.
- **Regras especiais do local:**
  - **Twelve Wave Cloud Confusion Formation** (formação das doze ondas de nuvem): uma Gu
    formation de névoa em forma de labirinto, cujos **núcleos são doze "cloud buildings"**
    (edifícios de nuvem) fixos e imóveis. Dentro dela, os cinco sentidos de um Gu Immortal se
    embaralham: perde-se a noção de direção, anda-se em círculo. Só um **immortal killer move
    investigativo** permite navegar; sem ele, achar um cloud building é pura sorte. A formação
    só cai quando **todos os doze** forem destruídos. Está "a um passo" de ser um battlefield
    killer move, mas o land spirit deliberadamente **não** usa battlefield killer moves dentro
    da própria blessed land: gravar dao marks novos conflitaria com os dao marks do mundo
    interno e **danificaria a própria terra** (cap. 873) — regra geral valiosa.
  - **Ancient battle formation "Heavenly Giant Solor"** — o trunfo. Categoria distinta e quase
    extinta ("enterrada no rio do tempo"): permite a **vários Gu Immortals somarem forças em
    um único corpo de batalha**, com fundações de alma somadas (o que anula ataques de soul
    path mirados num indivíduo), immortal essence virando um **pool compartilhado** e
    comunicação telepática entre todos. Funciona melhor quando **todos são do mesmo path** e
    quando já treinaram juntos; um grupo misto e inexperiente desperdiça o potencial e vai
    melhorando durante o próprio combate. Ativação: o núcleo grita o nome três vezes; forma um
    gigante metálico de **três cabeças e seis braços**, cada membro podendo canalizar o killer
    move de um participante diferente. Custo citado: 100 contas de immortal essence do pool
    comum em um único golpe amplificado (caps. 883-885).
  - **Refinement Cauldron** (rank 8 Immortal Gu House) foi **fundida ao próprio mundo interno**
    da blessed land: o mundo inteiro é o interior do caldeirão, e tudo que vive dentro está ao
    alcance do refino da House. Efeito: o espaço interno inchou até virar um oceano com **três
    continentes** e **milhões** de hairy men vivendo uma civilização completa — maior que a
    maioria dos grotto-heavens. É com ela que o land spirit **refinou à força os Immortal Gu**
    dos invasores das três ondas anteriores, capturando-os vivos. Contrapartida: arrancar Gu
    dela faz o mundo interno **encolher violentamente**, gerando tsunamis, furacões e
    afundamento de terras que matam multidões de mortais lá dentro (caps. 882-884).
- **Ambiente por dentro:** névoa branca infinita cortada por doze torres de nuvem; espelhos de
  observação dentro de cada torre mostrando só o entorno imediato daquela torre; abaixo da
  fachada, um oceano com continentes povoados.
- **Prêmio / o que se ganha:** para o atacante, o conteúdo de um cofre de rank 8 e a própria
  Immortal Gu House. Para o **mercenário defensor**, pagamento negociado caso a caso — no
  caso registrado, uma **receita de Immortal Gu rank 6** já acordada antes mais o **método
  completo de relocação de blessed land** arrancado na negociação pós-batalha (cap. 887).
- **Fases:** pedido de socorro → contratação de reforços → invasores entram pela conexão do
  agente infiltrado → luta dispersa dentro do labirinto de névoa, torre a torre → queda das
  torres e revelação do verdadeiro mundo interno → trunfo (ancient battle formation) →
  saque parcial / retirada dos invasores por causa de uma emergência externa.
- **Papel possível de um grupo pequeno:** mercenários imortais de rank baixo contratados
  para *segurar* um inimigo muito mais forte por um tempo determinado ("aguente trinta
  minutos"), não para vencê-lo — a missão é atrito e sobrevivência. Alternativamente: os
  jogadores como habitantes mortais do mundo interno, para quem a batalha dos imortais chega
  como cataclismo natural (a obra é explícita: "um caso clássico de mortais sofrendo por causa
  de uma luta entre imortais").
- **Consequência para o mundo:** metade da Immortal Gu House rank 8 sai do lugar; a blessed
  land perde dao marks de forma irreparável e sofre desastres internos; o land spirit passa a
  precisar de aliados externos.
- **Cuidado de spoiler:** ficam de fora a identidade e o destino dos invasores nomeados, a
  revelação sobre a natureza dupla do land spirit, quem eram os agentes infiltrados e por que
  o cerco foi abandonado (uma emergência da organização atacante em outro lugar).
- **Lacunas:** a obra não descreve as três ondas anteriores em detalhe, nem o intervalo de
  tempo entre ondas, nem quantos mercenários foram contratados ao todo.

### Campanha de invasão de Yu Lu blessed land — caps. 888-889, 897-898, 903-905, 917-922

- **Tipo:** expedição repetida de saque a uma blessed land sem dono; "masmorra em camadas"
  de campos de batalha. Estruturalmente é o evento mais parecido com uma *dungeon* de várias
  sessões em toda a faixa.
- **Onde:** Eastern Sea. A entrada é uma **porta circular no fundo do mar**, de aparência
  de porcelana ou jade, com cortinas de contas de cristal d'água (cap. 888).
- **Gatilho / causa mecânica:** **Yu Lu blessed land** pertenceu a Fairy Yu Lu, rank 8,
  discípula do Paradise Earth Immortal Venerable e mestra reconhecida em **battlefield
  killer moves**. Morta, a blessed land ficou sem dono, dentro do território da **Eastern Sea
  Zombie Alliance** (super força), que a explora sem disputa externa — pode ir no próprio
  ritmo, tentativa após tentativa (cap. 818).
- **Periodicidade:** ataques em levas com **intervalo declarado de trinta dias** entre uma
  investida e a seguinte, para recompor immortal essence e recrutar mais especialistas
  (cap. 898). A campanha inteira dura anos e consome a fortuna acumulada dos organizadores.
- **Regras especiais do local — as quatro camadas (o coração do evento):**
  1. **Freezing rain frozen earth** (battlefield killer move de gelo). Depois de um tempo,
     começa uma garoa de chuva congelante cujas gotas são agulhas de gelo, e da chuva se
     formam **snow monsters** que atacam em onda. Descrito como "sem falhas, perfeitamente
     equilibrado": não expõe nenhum ponto de partida ao investigador (cap. 889).
  2. **Fighting soul battlefield** (o mais letal). Criado pelo Paradise Earth Immortal
     Venerable tomando por base uma herança do Spectral Soul Demon Venerable, e por isso o
     único das criações dele que **não deixa saída**. Produz **soul beasts (bestas de alma)
     infinitas**, que ficam mais fortes com o tempo: em sete minutos já surgem soul beasts de
     nível *ancient desolate*, e em trinta minutos surgiriam de nível *immemorial desolate*,
     possivelmente mais de um. Ao contrário do primeiro, **expõe** de saída vários esconderijos
     de Gu mortais: a dificuldade não é decifrar, é **desmontar dezenas de milhares de
     esconderijos antes que as bestas matem todo mundo** — corrida entre a velocidade de
     desmonte e a curva de crescimento das bestas (cap. 898).
  3. **Eight doors labyrinth** (labirinto das oito portas) — camada de navegação (cap. 917).
  4. **Unmoving Troops** (tropas imóveis) — criação pessoal do Paradise Earth Immortal
     Venerable, **sem nenhum poder ofensivo**: quem entra portando **intenção de luta,
     pensamento malicioso ou desejo/luxúria** simplesmente **não consegue avançar** — é
     teleportado de volta à posição exata de origem, indefinidamente. A contramedida óbvia
     tentada no texto é esvaziar a mente. Precedente histórico citado: com ele, o Venerável
     subjugou um rank 7 sem se mover nem uma vez (cap. 917).
- **Regra do mundo revelada aqui (importante):** normalmente **battlefield killer moves e
  blessed lands são incompatíveis** — o campo grava dao marks temporários que conflitam com os
  dao marks que *formam* a abertura imortal, danificando-a. Yu Lu blessed land é a exceção:
  ela **não tem céu, chão, vegetação, seres vivos nem recursos acumulados**, é apenas um espaço
  amplo atravessado por faixas de luz colorida; é justamente esse vazio que permite empilhar
  campos de batalha de paths diferentes sem conflito (cap. 917).
- **Por que os invasores não quebram tudo na força:** os campos são feitos com os **dao marks
  internos** da própria blessed land. Destruí-los à força destrói o prêmio — e ainda custaria
  immortal essence em quantidade proibitiva. A doutrina é **desvendar**, não arrombar
  (cap. 889). Regra de ouro para o mestre: numa invasão de abertura imortal, a violência
  bruta destrói o tesouro.
- **Forças presentes (como tipos):** um casal de imortais zumbis organizadores, que
  **investiram quase toda a poupança própria** na empreitada e respondem por ela; uma escolta
  de imortais zumbis de rank 6-7 da aliança; e — o recurso escasso do evento — **Gu Immortals
  com attainment em wisdom path**, contratados a peso de ouro porque são raríssimos e são os
  únicos capazes de desmontar os esconderijos. Cada especialista tem um método próprio e uma
  taxa própria de desmonte (um por vez; cinco a seis por vez; um método que alcança o exterior
  a partir de dentro de um Immortal Gu House). Há também um **Immortal Gu House incompleto
  (Profound Ice House)** usado como abrigo móvel e rota de fuga, alimentado pela força somada
  de todos os presentes.
- **Prêmio:** os Immortal Gu de Fairy Yu Lu — visíveis circulando pelo espaço interno, ainda
  soltos — e as **próprias receitas de battlefield killer move**; aprender o método dela seria
  o maior ganho de todos. A distribuição é por **contribuição declarada**: o organizador leva
  um ou dois Immortal Gu e uma soma grande de pontos de contribuição da super força; o resto
  é rateado. Um único Immortal Gu rank 7 já pagaria toda a expedição (cap. 917).
- **Papel possível de um grupo pequeno:** os jogadores como a equipe contratada de
  especialistas — cada personagem com um método diferente de investigação, correndo contra o
  relógio das bestas de alma enquanto o abrigo aguenta. É um cenário de perícia sob pressão,
  não de força bruta, e serve para grupos que não têm poder de combate. Variante: os
  jogadores como a escolta descartável que segura as bestas enquanto os especialistas
  trabalham.
- **Consequência para o mundo:** a queda de Yu Lu blessed land põe em circulação Immortal Gu
  e conhecimento de battlefield killer moves de nível Venerável.
- **Cuidado de spoiler:** ficam de fora quem levou o quê, as rivalidades e sabotagens internas
  entre os especialistas contratados, e o destino dos organizadores.
- **Lacunas:** a obra não diz quantas investidas ao todo a campanha levou desde o começo, nem
  quanto exatamente custou; não descreve a camada 3 (eight doors labyrinth) por dentro.

## Eventos recorrentes e institucionais

## Eventos históricos citados

## Candidatos a nota própria

