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

### Disputa pela herança de wisdom path em Tai Qiu e saque de Jade Pool blessed land — caps. 781-806 (a parte dentro da faixa: 801-806)

- **Tipo:** abertura de herança (inheritance ground) + corrida de abutres + saque de uma
  blessed land de super força.
- **Onde:** Northern Plains. A herança fica no fundo de **Tai Qiu**, uma das **dez grandes
  áreas ferozes** (ten great fierce areas) da região; a segunda metade do evento se desloca
  para **Jade Pool blessed land**, sede da tribo do dono da herança.
- **Gatilho / causa mecânica:** um Gu Immortal rank 7 de wisdom path, prevendo o fim da
  própria vida, montou dentro de Tai Qiu um **inheritance ground** e uma rota mortal
  planejada para que **candidatos mortais de seu próprio clã** a percorressem — a herança
  fazia parte do plano de renascimento por possessão dele, não de caridade. Ele fechou
  acordos com as super forças do path reto para que não interferissem, mas **não previu a
  cobiça dos imortais do próprio clã**, nem a dos imortais demoníacos.
- **A regra especial do local (excelente para mesa):** em Tai Qiu vivem desolate beasts e
  ancient desolate beasts em massa, e **a aura de um Gu Immortal vaza e provoca as feras** —
  imortais não ousam entrar fundo, nem os rank 8. **Gu Masters mortais têm aura fraca e não
  atraem as feras grandes**: seguindo a rota planejada, só encontram grupos de bestas
  comuns. Resultado: uma masmorra em que **só personagens fracos podem entrar**, com um anel
  de imortais poderosos parados na periferia, impotentes, observando e esperando a saída
  (caps. 781, 1085).
- **Escala:** grupos mortais entram em times de mais de dez pessoas e saem com três; três
  dias adentro já custaram mais de dez ondas de bestas. Do lado de fora, os métodos
  investigativos dos presentes contaram **19, 20 e 26 Gu Immortals escondidos** na periferia
  (cada personagem enxerga um número diferente conforme sua perícia — detalhe delicioso para
  mesa). Maioria de path demoníaco, com imortais do próprio clã do doador infiltrados.
- **Ambiente por dentro:** floresta primitiva formada por **grama gigante** — um talo de
  grama equivale a uma árvore centenária. Palco de batalha improvisado com o **cadáver de um
  immemorial ruin bat**, cuja aura de nível imemorial afugentava as demais feras e por isso
  permitia que imortais lutassem ali sem provocar maré de bestas (cap. 1085, retrospecto).
- **Fases:** (1) candidatos mortais atravessam Tai Qiu pela rota; (2) imortais se acumulam
  na periferia e começam a brigar entre si; (3) a herança se revela **não estar** onde
  todos pensavam ("Tai Qiu não é um terreno de herança" — o título do cap. 781 é o próprio
  aviso); (4) a briga migra para a blessed land da tribo, que é **arrombada** (um buraco
  ligando ao exterior) enquanto o dono está preso lutando longe; (5) saque aberto: recursos
  livres para quem pegar, e um imortal de enslavement path capturando os Gu Masters mortais
  da tribo em massa; (6) o dono retorna e a horda demoníaca, até então dividida, **se une
  espontaneamente** porque o saque só continua se ele morrer.
- **Prêmio:** a herança de wisdom path descrita como "a número um de Northern Plains"; e,
  na segunda fase, os recursos inteiros de uma blessed land de super força, abertos a
  qualquer um que chegue.
- **Papel possível de um grupo pequeno:** os jogadores como o time mortal contratado ou
  aparentado que percorre a rota — combate de rank 3-5 contra bandos de bestas, com o
  agravante de saber que, ao sair, dezenas de imortais estarão esperando. Ou como Gu Masters
  da tribo saqueada, tentando salvar gente enquanto imortais brigam no céu.
- **Consequência para o mundo:** uma super força regional perde a blessed land e o único
  imortal de peso; a herança de wisdom path entra em circulação; o equilíbrio político da
  região se desloca.
- **Cuidado de spoiler:** ficam de fora quem levou a herança, o truque de possessão do
  doador, quem morreu e o papel dos personagens nomeados.
- **Lacunas:** a obra não descreve a rota planejada em detalhe nem as provas internas do
  inheritance ground.

### Chaos in Northern Plains — queda de uma super força e corrida por seus territórios — caps. 1100-1110, 1163, 1169-1172, 1181-1182

- **Tipo:** colapso político de uma super força + rapina generalizada de territórios + cerco à
  sede. É o evento "mapa aberto" da faixa: dezenas de cenas simultâneas espalhadas por uma
  região inteira.
- **Onde:** Northern Plains inteira, com foco em **Iron Eagle blessed land** (sede da **Hei
  tribe**) e em seus territórios espalhados.
- **Gatilho / causa mecânica:** a Hei tribe é **responsabilizada publicamente** pela destruição
  de um Immortal Gu House lendário (Eighty-Eight True Yang Building) e não tem nenhum Gu
  Immortal rank 8 para dissuadir represálias. Regra do mundo explicitada no texto: **um rank 8
  é o que garante a existência de uma super força** — com um, a tribo pagaria uma multa pesada
  e sobreviveria; sem um, ela é presa. Ao mesmo tempo, a **Hei Fan true inheritance** (herança
  de um rank 8 morto da própria tribo) volta a ser acessível, o que faz a tribo **recolher
  todos os seus Gu Immortals para a sede** — deixando o resto do seu território **sem
  guarnição** (caps. 1101, 1103).
- **Escala e forças (como tipos):** todas as camadas do mundo imortal aparecem ao mesmo tempo.
  - *Super forças de sangue Huang Jin* (a nobreza da região) mobilizam times de 2 a 5 imortais
    cada, com uma delas trazendo a própria **Immortal Gu House** para o cerco e tentando se
    proclamar líder da aliança — proposta que ninguém aceita, porque nenhuma tribo Huang Jin
    se submete a outra.
  - *Imortais demoníacos e solitários* se juntam sob um rank 7 que tem um método específico
    para arrombar a sede, e **atacam primeiro**; os do path reto ficam de fora, esperando o
    colapso para entrar pelas brechas sem gastar recursos — divisão de trabalho involuntária
    e cínica entre facções.
  - *Imortais de baixo escalão* (rank 6 pobres, avós levando netos recém-ascendidos) escolhem
    territórios periféricos, calculando explicitamente quais são "seguros o bastante": os
    próximos à sede e os vizinhos de outras super forças são intocáveis; sobra a periferia.
  - Um **rank 8 solitário** aproveita para fundar sua própria tribo com os despojos.
- **Regra especial do local:** **Iron Eagle blessed land é uma "public blessed land"** — uma
  abertura imortal *montada* como base coletiva de uma organização, e por isso **não tem as
  defesas naturais de uma blessed land pessoal**. Fica num único ponto minúsculo e, com a
  entrada fechada, é invisível de fora; só killer moves que enxergam através de blessed lands
  (aqui, "purple jade eyes") revelam o que há dentro. É arrombável, e depois de arrombada
  fica "cheia de brechas": qualquer um entra (cap. 1105).
- **Ambiente por dentro (os territórios como cenários prontos):**
  - **Campo de trigo dourado**: terra estéril mineralizada demais para plantas comuns, onde a
    tribo plantou "golden wheat" — um trigo que na verdade é **metal essence**, material
    mortal rank 5, colhido a cada dois anos, **500 mil quilos por colheita**, vendido em
    volume. O campo é tão grande que não se vê a borda voando.
  - **Gushing Spring Forest**: floresta de pilares d'água formados por gêiseres subterrâneos,
    cheia de Gu mortais de water path e earth path.
  - **Become Dragon Mound**: elevação riquíssima em dao marks de transformation path, produtora
    histórica de "dragon Gu" (golden dragon, water dragon, earth dragon, dragon claw, dragon
    breath, dragon pearl).
  - Uma planície comum escondendo um **fragmento do immemorial red heaven**.
- **Fases:** (1) a acusação pública e o recolhimento das tropas; (2) semanas de rapina nos
  territórios periféricos, com brigas de dez imortais por um bosque; (3) cerco à sede, path
  demoníaco arrombando e path reto esperando; (4) queda; (5) redistribuição — um recém-chegado
  rank 8 absorve a tribo derrotada mas **precisa ceder a maior parte dos despojos** às outras
  super forças para ser aceito, porque é de fora do sangue Huang Jin; (6) anos depois, a
  autoridade suprema da região emite o **Longevity Edict** — um Immortal Gu de information path
  que viaja sozinho de tribo em tribo transmitindo a ordem e recolhendo a resposta de cada
  supreme elder — mobilizando *todas* as tribos Huang Jin contra o novo entrante (cap. 1181).
- **Papel possível de um grupo pequeno:** exemplar. A obra mostra explicitamente imortais
  fracos fazendo **análise de risco de saque**: que território ninguém forte quer, quando ir,
  como sair. Um grupo de rank 6 pobres pode rodar a campanha inteira sem nunca ver o cerco
  principal — só a corrida pelos restos, com encontros aleatórios contra outros grupos de
  igual para igual. Para mortais: os Gu Masters e camponeses da tribo caída, cujas fazendas,
  minas e florestas viram campo de batalha.
- **Consequência para o mundo:** uma super força milenar desaparece do mapa; uma nova nasce do
  nada; o equilíbrio da região se reorganiza e gera, anos depois, uma guerra de coalizão.
- **Cuidado de spoiler:** ficam de fora os nomes dos vencedores, quem herdou o quê, e a
  identidade do verdadeiro culpado pela destruição que desencadeou tudo.
- **Lacunas:** a obra não dá o número total de territórios da tribo nem quanto tempo durou a
  fase de rapina.

### Hei Fan grotto-heaven e a Immortal Succession Mountain — caps. 1114-1133, 1177-1182

- **Tipo:** abertura de herança (true inheritance) + mundo-prisão fechado + disputa armada
  posterior pelo território conquistado.
- **Onde:** **Hei Fan grotto-heaven**, um grotto-heaven (grau acima de blessed land) sem
  localização física acessível — flutua fora do mundo de Northern Plains e só se entra
  rasgando o espaço num ponto exato. O único meio mostrado é uma besta capaz de atravessar
  espaço para dentro de grotto-heavens (um **upper extreme heavenly eagle**, filhote de
  immemorial desolate beast que, adulto, terá força de rank 8) (cap. 1119).
- **Gatilho / causa mecânica:** Hei Fan foi um Gu Immortal rank 8 de time path que levou sua
  tribo ao auge. Antes de morrer, deixou o próprio grotto-heaven como **true inheritance** —
  *o prêmio é o mundo inteiro*: quem herda vira o dono do grotto-heaven. Nenhum descendente
  conseguiu herdá-lo em séculos.
- **Ambiente por dentro:** um mundo completo e vasto, com céu permanentemente **azul** (um
  fragmento do immemorial azure heaven fundido nele), floresta antiga de **musical trees**
  (folhas multicoloridas, aves canoras), **qi death birds**, **tea streams** (riachos verdes
  fumegantes com folhas que parecem chá), montanhas veneradas pelos locais, e recursos
  acumulados por gerações — porque o lugar **não tem ligação com o mercado imortal
  (treasure yellow heaven)**: muita quantidade, pouca variedade.
- **Quem mora lá dentro:** descendentes de **imortais criminosos** exilados pelo fundador, mais
  uma população mortal local. No momento do evento havia **nove Gu Immortals** — dois rank 7 e
  sete rank 6 — divididos em um clã de sangue (quatro), um trio de irmãos jurados e dois
  solitários. Traço decisivo para a mesa: **isolados há gerações, são ingênuos** — péssimos em
  confronto verbal, sem malícia política, com métodos de combate desatualizados, e **nem sabem
  que o mercado imortal existe**.
- **Regras especiais do local (a jaula):**
  - Os moradores **não conseguem sair**; o texto os descreve dizendo "para romper esta gaiola".
  - **Immortal Succession Mountain**: uma montanha solitária, artificialmente talhada em **dez
    níveis**, cercada de florestas ricas. Cada nível guarda uma herança (uma delas, no primeiro
    patamar, é de luck path). Subir a montanha é uma prova; a cada nível vencido, o **sino do
    heavenly spirit toca uma vez, e o som se espalha pelo mundo inteiro** — todos os moradores
    ouvem e sabem exatamente até onde o candidato chegou. **Dez toques** significa que apareceu
    alguém qualificado para a herança principal (caps. 1119, 1121).
  - **Heavenly spirit** (espírito celestial — o equivalente, num grotto-heaven, do land spirit
    de uma blessed land): aqui um **sino de bronze** que se pendura num gancho do pavilhão. É
    **sem mente própria** (mindless), mas executa fielmente as instruções deixadas pelo
    fundador. A informação do lugar está gravada num **tablete de pedra** do tamanho de um
    elefante; perguntas ao sino fazem **novas linhas aparecerem** no tablete.
  - **A coleira**: todo Gu Immortal nascido lá dentro enfrenta calamidades e tribulações
    normalmente. Quando não consegue passar de uma, recorre ao heavenly spirit, que usa um
    Immortal Gu da primeira herança para **adiar a tribulação** dele. A partir daí, aquele
    imortal está sob controle do espírito, porque **o adiamento pode ser removido a qualquer
    momento — e aí ele morre**. Como o grotto-heaven não tem variedade de recursos, cedo ou
    tarde *todos* falham numa tribulação e caem na armadilha. É assim que um morto governa um
    mundo há séculos (cap. 1121).
- **A prova final (o coração jogável):** o tablete revela que, além de subir a montanha, o
  candidato precisa **obter o voto de metade dos Gu Immortals do grotto-heaven, dentro de três
  anos** contados no tempo interno do lugar. O fundador projetou isso para escolher um
  **líder**, não um lutador: a prova é de política e persuasão, e obriga o herdeiro a acolher
  os exilados em vez de exterminá-los (cap. 1122). Para uma mesa, é uma campanha inteira de
  intriga com nove PNJs bem definidos e um relógio de três anos.
- **Prêmio:** a propriedade de um grotto-heaven inteiro, mais o conjunto de tesouros do
  fundador ("as quatro maravilhas de Hei Fan", caps. 1128-1129) e o método de **desacelerar o
  tempo dentro de uma abertura imortal** — o que, no sistema do mundo, significa **espaçar as
  calamidades e tribulações** de quem o usa. Era esse método que sustentava a antiga era de
  ouro da tribo: o rank 8 desacelerava a abertura dos subordinados, e por isso a tribo tinha
  mais imortais sobreviventes que qualquer outra.
- **Fase posterior — Contest Over Hei Fan Grotto-heaven (caps. 1177-1182):** com o dono novo
  instalado, o grotto-heaven vira alvo. Um **rank 8** de fora ataca **enviando ondas de
  desolate beasts para dentro** em vez de entrar pessoalmente; o defensor contrata mercenários
  imortais para guardar setores. Detalhe mecânico rico: **os recursos transplantados precisam
  de tempo para "pegar"** — plantas imortais recém-instaladas precisam absorver earth qi antes
  de poderem ser movidas de novo, e arrancá-las cedo as destrói. Ou seja, o defensor **não pode
  simplesmente fugir com o saque**; tem de segurar o terreno por um prazo. O conflito termina
  **por acordo político**, não militar: uma ameaça maior aparece para os dois lados e o
  inimigo vira aliado.
- **Papel possível de um grupo pequeno:** (a) os jogadores como o grupo que entra e precisa
  conquistar votos — cada um dos nove imortais locais é um problema social distinto; (b) os
  jogadores como os *próprios* moradores, gente presa num mundo pequeno descobrindo que a
  reverência ao ancestral é uma coleira; (c) na fase posterior, mercenários defendendo setores
  contra ondas de bestas enquanto uma plantação criticamente valiosa amadurece.
- **Consequência para o mundo:** um grotto-heaven de rank 8 muda de dono e passa a ser
  desenvolvido; o método de desaceleração de tempo entra em circulação.
- **Cuidado de spoiler:** ficam de fora quem herdou, como os votos foram obtidos, as mortes
  entre os imortais locais e a identidade real do herdeiro.
- **Lacunas:** a obra não descreve o conteúdo dos dez níveis da montanha um a um, nem a
  população mortal interna em números, nem o que aconteceu com os moradores depois.

### Queda de Sacred Feather City e o êxodo dos feathermen — caps. 864-871, 977-978

- **Tipo:** cerco e destruição de uma cidade de humanos-variantes + êxodo de um povo inteiro,
  que chega ao destino **na forma de uma calamidade**.
- **Onde:** **Sacred Feather City**, "a cidade no céu" — uma cidade inteira que é ao mesmo tempo
  um **Immortal Gu House**, flutuando dentro de um **mundo-fragmento do immemorial green
  heaven** (céu levemente esverdeado, vento perpétuo nas quatro estações), isolado do mundo
  exterior e tratado pelos moradores como paraíso.
- **Gatilho / causa mecânica:** um grupo de Gu Immortals **humanos** cerca a cidade para tomar
  o Immortal Gu House e escravizar a população. O comandante do cerco **imobiliza a cidade
  primeiro** e depois ataca sem pressa — e, quando percebe que os defensores vão fugir,
  **manda deliberadamente não interromper**: ele quer o edifício vazio, não a matança.
- **Duração e escala:** bombardeio contínuo por **três dias e duas noites**, com killer moves
  mortais em massa e alguns imortais. Mais da metade das tropas da cidade morre. A cidade tinha
  **três Gu Immortals** (um rank 7, dois rank 6); um morre no cerco. População na casa das
  **dezenas de milhares**.
- **Regra especial: o desespero como recurso.** O escape é o immortal killer move **Heavenly
  Wish** (desejo celestial): toda a população se reúne na arena e **grita desejos em coro** —
  "que meu povo sobreviva", "que meu povo tenha liberdade", "que meu povo tenha um lugar no
  mundo" — e a cidade inteira se acende em luz branca que cresce de alguns metros a dezenas de
  metros até teleportar todos para longe. É um golpe de **fuga em massa**, não de combate, e
  custa a cidade em si.
- **A consequência mais interessante para uma mesa:** o destino do teleporte **não é
  escolhido**. O povo inteiro reaparece dentro da blessed land de um Gu Immortal qualquer — e
  o sistema do mundo os classifica como uma **earthly calamity** daquela abertura imortal. Ou
  seja: *uma calamidade que cai sobre uma blessed land pode ser um povo refugiado desesperado,
  armado e liderado por dois Gu Immortals*. Do lado de dentro, os refugiados avaliam
  imediatamente matar o dono e tomar o mundinho para si — "é pior que o fragmento do green
  heaven, mas dá para o nosso povo viver".
- **Prêmio / o que se ganha:** para os sitiantes, um Immortal Gu House inteiro sem gastar quase
  nada; para os defensores, a sobrevivência do povo e nada mais; para o dono da blessed land
  onde eles caem, um problema e uma oportunidade (mais tarde, os feathermen viram população
  submetida dentro de uma abertura imortal, caps. 977-978).
- **Papel possível de um grupo pequeno:** os jogadores como feathermen mortais da cidade —
  defender muralhas por três dias sabendo que a derrota significa escravidão, evacuar civis,
  decidir se apoiam o desejo coletivo. Ou, do outro lado, como o pequeno grupo que de repente
  encontra dezenas de milhares de refugiados armados materializados no próprio quintal.
- **Consequência para o mundo:** um povo variante perde seu último território independente; um
  Immortal Gu House muda de mãos; reforça-se a regra social de que **o mundo é dos humanos e
  os variant humans não têm onde viver**.
- **Cuidado de spoiler:** ficam de fora quem eram os sitiantes, o destino dos dois Gu Immortals
  feathermen e o que acontece com o povo depois.
- **Lacunas:** a obra não diz quantos feathermen sobreviveram, nem por que o teleporte escolhe
  aquele destino específico.

### Cerco de Luo Po valley e a herança de Thieving Heaven — caps. 886, 898, 922-923, 952-953, 990-992

- **Tipo:** cerco de fortaleza entre grandes forças de duas regiões + abertura de herança de
  Venerável escondida dentro do próprio campo de batalha.
- **Onde:** **Luo Po valley**, em Northern Plains. É um **"secluded domain of heaven and earth"**
  (domínio isolado de céu e terra) — categoria rara de lugar, não uma blessed land: um vale
  onde sopra o ano inteiro uma **névoa de desnorteamento** (bewilderment fog) e o **Luo Po
  wind**, e onde vivem em massa os **white lotus giant silkworm Gu**. Servia de **base e
  fortaleza** de uma organização secreta que atravessa duas regiões.
- **Gatilho / causa mecânica:** as **dez grandes seitas antigas de Central Continent** montam
  uma expedição a outra região para investigar a destruição de um Immortal Gu House lendário e
  cercam o vale. O lado de dentro tem **vantagem territorial** (as formações e o próprio
  domínio); o lado de fora tem números e determinação e **não recua**.
- **Duração:** o cerco vira a **"hundred days battle"** (batalha dos cem dias) — cem dias
  exatos, e o nome entra para o vocabulário do mundo. Metade dos defensores morre; do lado
  atacante, o desgaste de immortal essence é descrito como enorme e vários ficam
  "falidos".
- **Ambiente por dentro / regras especiais:**
  - O vale acumula, ao longo do cerco, **formações de Gu de ambos os lados sobrepostas** —
    primeiro as do defensor, depois as do atacante que invadiu e destruiu as anteriores. O
    resultado é um terreno **entulhado de armadilhas antigas meio quebradas**: quem entrar
    depois precisa **contornar umas e desmontar outras** (o texto conta: "contornou quatro
    formações e desmontou três").
  - Efeito ambiental: tanta formação sobreposta **matou o clima natural do domínio** — a névoa
    perpétua e o Luo Po wind simplesmente **desapareceram**. Excelente detalhe de mundo: uma
    guerra de imortais altera permanentemente um fenômeno natural.
  - Os white lotus giant silkworm Gu, recurso famoso do lugar, foram **quase exterminados**
    pela batalha e o resto foi varrido pelos vencedores.
- **O prêmio escondido:** dentro do vale, sem nenhuma pista externa detectável mesmo por
  métodos de investigação de grandmaster, existe a entrada para o **espaço da true inheritance
  do Thieving Heaven Demon Venerable**. A entrada **só abre com um Gu específico** (o
  "open door Gu"), e a dica de onde usá-lo chegou por um canal místico independente. A
  entrada aparece como um portal de luz que **encolhe progressivamente** depois de aberta —
  relógio embutido. O espaço interno é descrito como vastíssimo.
- **Fases:** (1) cerco e cem dias de batalha; (2) queda e ocupação pelos vencedores, que
  deixam um único vigia contratado à força; (3) janela de oportunidade — os ocupantes são de
  outra região e **não podem ficar muito tempo**; (4) terceiros entram para saquear o campo de
  batalha, disputando os despojos e a herança; (5) o domínio inteiro acaba sendo **arrancado do
  chão e levado embora** por um killer move que move montanhas.
- **Papel possível de um grupo pequeno:** o cenário clássico do "campo de batalha esfriando":
  os jogadores entram depois do fim da guerra, num vale arruinado, cheio de formações
  semiquebradas, cadáveres, Gu selvagens e outros saqueadores — com um vigia solitário e mal
  pago no portão, e um segredo enterrado que só abre com o item certo.
- **Consequência para o mundo:** uma organização secreta perde a base; um domínio natural raro
  é destruído como ecossistema; uma herança de Venerável entra em circulação.
- **Cuidado de spoiler:** ficam de fora quem sitiou, quem morreu (inclusive uma morte muito
  importante), quem herdou o legado do Venerável e o que a organização guardava lá.
- **Lacunas:** a obra não descreve as provas internas do espaço da herança nem o número total
  de combatentes dos dois lados.

### Blood Plain Martial Competition — caps. 1190-1197

- **Tipo:** torneio de campeões usado como substituto formal de uma guerra regional.
- **Onde:** **Blood Plain**, uma planície de Northern Plains escolhida como terreno neutro, a
  meio caminho entre os dois blocos.
- **Gatilho / causa mecânica:** a autoridade suprema da região emite o **Longevity Edict** e
  convoca **todas as onze tribos de sangue Huang Jin** contra um bloco novo formado por uma
  tribo recém-fundada e uma seita demoníaca. Os dois líderes rank 8 se encontram, concluem que
  uma guerra frontal não resolveria nada e **combinam um "martial competition"**: em vez de
  lutarem eles próprios, mandam **os juniores** lutar e deixam o atrito subir devagar. É guerra
  por procuração formalizada por acordo entre os dois maiores poderes.
- **Formato (o que uma mesa precisa):**
  - Série de **duelos individuais, um de cada lado por vez, até a morte ou rendição**, sob os
    olhos de todos os presentes.
  - Cada lado escolhe internamente quem sobe a cada rodada; do lado da coalizão maior, uma
    figura preside e **autoriza** quem vai — com política interna pesada, porque cada tribo
    quer glória para os seus e nenhuma quer gastar seus melhores.
  - **Vitórias consecutivas contam**: um campeão que vence três vezes seguidas domina a rodada.
  - O placar não é por número bruto de vitórias, mas pelo **peso do que se derrubou**: matar um
    rank 7 vale mais que vencer três rank 6.
  - **Os despojos do morto pertencem ao vencedor** — corpo, Gu, abertura imortal —, e isso está
    **escrito no acordo da competição**; o lado perdedor não pode impedir.
  - Fora do acordo, cada bloco tem **planos de resgate**: um patrono pode romper as regras para
    salvar o próprio junior, ao custo da reputação.
- **Escala:** onze super forças de um lado, com pelo menos **três Immortal Gu Houses** (salões
  voadores) pairando simultaneamente sobre a planície — cena descrita como rara no mundo
  imortal da região. Do outro lado, uma coalizão menor que compensa **recrutando mercenários,
  solitários e demoníacos** — e a notícia da competição se espalha até as outras regiões,
  atraindo forasteiros que vêm construir reputação.
- **Prêmio:** para os indivíduos, **fama** — o motor declarado: juniores desconhecidos entram
  justamente para ter o nome espalhado pelo mundo — e os despojos dos derrotados, incluindo
  aberturas imortais inteiras (um degrau de avanço de rank). Para os blocos, vantagem
  psicológica e política antes da guerra de verdade.
- **Papel possível de um grupo pequeno:** perfeito para personagens ambiciosos de rank 6: são
  exatamente "juniores sem nome" que a mesa acompanha subindo à arena. Também rende papéis não
  combatentes: apostadores, agentes recrutando mercenários, espiões medindo a força alheia.
- **Consequência para o mundo:** define quem tem a moral mais alta antes da guerra e cria (ou
  destrói) reputações de uma geração inteira.
- **Cuidado de spoiler:** ficam de fora quem venceu cada duelo, quem morreu e como a guerra
  maior terminou.
- **Lacunas:** a obra não diz quantas rodadas ao todo, nem se havia limite de rank para os
  participantes, nem quanto tempo o torneio durou.

### Expedição ao Earth Trench — caps. 927-938

- **Tipo:** expedição de exploração em zona proibida; caça a materiais imortais e Gu selvagens.
- **Onde:** o **Earth Trench** (a Trincheira da Terra) de Northern Plains. Regra geral do
  mundo: **cada uma das cinco regiões tem o seu Earth Trench** — fendas gigantescas no solo,
  algumas com milhões de li de extensão, dezenas de milhares de quilômetros de profundidade,
  algumas **imensuráveis**; contam entre as maiores maravilhas naturais conhecidas.
- **Regras especiais / ambiente:** o interior alarga vertiginosamente conforme se desce —
  poucos minutos de voo e a fenda já comporta "setenta ou oitenta cidades gigantes". Paredes
  lisas e nuas, com plantas em forma de agulha esparsas como grãos de gergelim; escuridão
  permanente pontuada de brilhos; **óleo negro escorregadio** cobrindo o fundo (que certas
  bestas usam para se mover como peixe na água). **Quanto mais fundo, mais feras, plantas
  misteriosas e Gu selvagens** — e mais fortes: desolate beasts em bandos, ancient desolate
  beasts nada raros, e nas profundidades, immemorial desolate beasts.
- **Quem controla:** apenas **super forças** conseguem ocupar um Earth Trench como ponto de
  recurso, e mesmo assim só a faixa mais rasa — no caso descrito, **cerca de 160 km** a partir
  da superfície, apesar de séculos de esforço. Cidades inteiras são construídas na boca da
  fenda só para explorá-la, e a entrada é vigiada permanentemente por pelo menos um rank 7.
- **Por que se desce mesmo assim:** é um dos poucos pontos de recurso realmente ricos numa
  região pobre. Ali dentro há **materiais imortais** que não existem em outro lugar (o
  "star night mucus" só pode ser colhido acompanhando uma besta específica que só vive no
  fundo, e processado **na hora**, em janela curtíssima), **Gu selvagens**, um **"mar de restos
  de materiais imortais"** e **formações de Gu antigas gigantescas** — uma delas exigiria
  "vários meses" para ser desvendada, e só espiar por uma fresta já consumiu tudo que um
  grandmaster de wisdom path conseguia fazer.
- **Como se monta uma expedição (útil como modelo de missão):** negociação política com quem
  controla a entrada; escolta designada (no caso: **cinco imortais zumbis — dois rank 7 e três
  rank 6**); dias de preparação em que os membros **pegam Immortal Gu emprestados** da
  organização para a missão; guias locais que conhecem o terreno; e um objetivo declarado que
  serve de pretexto para um objetivo real.
- **Perigo característico:** as feras fortes têm **território e rotina** — o ponto alto do
  bloco é um grupo trabalhando numa formação enquanto a besta dona do ninho está fora, com
  contagem regressiva até a volta dela; ao voltar, ela **fareja auras residuais** deixadas
  pelo trabalho investigativo e patrulha desconfiada até as auras se dissiparem.
- **Papel possível de um grupo pequeno:** modelo de masmorra vertical. O grupo desce por
  camadas de perigo crescente, com um teto natural de profundidade dado pela própria força; o
  prêmio é proporcional à profundidade; a escolta é mais forte que os jogadores e tem agenda
  própria.
- **Consequência para o mundo:** local, não estrutural — o Earth Trench é permanente e nunca
  é conquistado.
- **Cuidado de spoiler:** ficam de fora o objetivo real da expedição, o que foi encontrado na
  formação antiga e a revelação sobre uma abertura imortal específica.
- **Lacunas:** a obra nunca descreve o fundo do Earth Trench — ninguém jamais chegou lá.

### A armadilha de Yi Tian Mountain — a fase imortal — caps. 967-971 e 998-1021

- **Tipo:** emboscada em massa contra a elite imortal de uma região inteira, dentro de um campo
  de batalha selado, sob chuva de tribulações. É o evento mais próximo de um "incidente" no
  sentido de mesa: um lugar, uma noite, todo mundo dentro, e as regras do mundo virando do
  avesso.
- **Onde:** ao redor de **Yi Tian Mountain** (Southern Border), a dez mil li do cume — a
  distância mínima que a zona proibida a imortais permite. Todos os Gu Immortals apostadores da
  disputa mortal (ver a entrada do "gambling contest") estão acampados exatamente ali, parados,
  esperando o resultado.
- **Escala:** a elite imortal de uma região inteira num só lugar — **quatro rank 8, nove rank 7
  e mais de dez rank 6**, mais os mortais dentro da zona proibida.
- **Gatilho / causa mecânica (duas camadas):**
  1. **Chuva de tribulações.** Do céu começam a cair provações em série — a primeira delas uma
     versão monstruosa de uma tribulação conhecida (a "thousand pearl-light tribulation" tem,
     pelo nome, mil pérolas de luz; a que cai tem **cem mil**). Ninguém sabe quem está sendo
     provado. Pela cláusula do contrato de apostas, **se aparece uma ameaça, todos os
     apostadores se unem para bloqueá-la** — então a elite inteira, inimiga entre si, passa a
     defender coletivamente o mesmo pedaço de céu, e ainda **puxa camadas de nuvem** para que os
     mortais lá embaixo não percebam nada. Ficam presos ao lugar: sair seria abandonar a aposta.
  2. **A armadilha.** Enquanto todos estão ocupados servindo de para-raios, uma organização
     oculta ativa em volta deles uma **Gu formation gigantesca** que os prende. É a **"ten
     extreme immortal zombie lifeless formation"**. Detalhe mecânico central: montada apenas em
     parte, ela **não chega a um décimo da própria força**, e as tribulações que caem a
     **desgastam continuamente** — ela não duraria. Para completá-la, vários Gu Immortals da
     organização **sacrificam a própria alma**, fundindo-a na formação, que salta para **noventa
     por cento** da potência. A partir daí não há mais fuga.
- **Regras especiais do local:** a zona proibida a imortais continua valendo (ninguém pode
  descer à montanha); as tribulações caem sobre **todos**, aliados e inimigos, e não distinguem
  lados — o texto descreve rank 7 sendo carregados "como jangadas em mar revolto", sem controle
  da própria situação. Uma formação controlada por pessoas é explicitamente **mais flexível**
  do que um battlefield killer move fixo, e é isso que a faz aguentar as tribulações.
- **Fases:** (1) chuva de tribulações e defesa coletiva improvisada; (2) caça interna — todos
  se acusam de estar escondendo o parente que está ascendendo e usando os outros de escudo;
  (3) selamento pela formação; (4) sacrifício de almas e formação a 90%; (5) inimigos mortais
  **abandonam suas rixas e cooperam** para tentar romper; (6) muito depois (caps. 998-1021), o
  lugar reúne de novo **três facções** de escala continental ao mesmo tempo, com Immortal Gu
  Houses em campo e uma **grande tribulação** (grand tribulation, acima do nível das "dez
  grandes catástrofes") caindo sobre o campo de batalha inteiro.
- **Papel possível de um grupo pequeno:** o cenário é feito para grupos de rank 6 ou 7 que não
  decidem nada, mas precisam **sobreviver e escolher lados** dentro de um selo, com tribulações
  caindo, um plano alheio em curso e a certeza de que quem ficou parado morre. Também rende o
  contraponto: os mortais na montanha, que só veem o céu ficar estranho porque alguém puxou
  nuvens para escondê-los.
- **Consequência para o mundo:** a elite imortal de uma região inteira é dizimada num único
  lugar e numa única noite; o mundo imortal daquela região fica "em turbulência por décadas"
  (frase textual). Um Immortal Gu House troca de dono e um immortal zombie rank 8 sai da prisão.
- **Cuidado de spoiler:** fica de fora tudo o que importa dramaticamente — quem armou a
  emboscada, o que a organização queria, quem estava ascendendo, quem morreu, e as revelações
  de identidade das duas fases. O evento **funciona sem nada disso**: um exército de imortais
  preso num selo enquanto o céu desaba é situação suficiente.
- **Lacunas:** a obra não descreve a estrutura completa da formação nem quantos sobreviveram.

## Eventos recorrentes e institucionais

### Refinement Path Convention (Convenção do Caminho do Refino) — caps. 828-859

- **Tipo:** torneio/feira mundial de artesanato, com trégua universal. É o maior evento
  institucional descrito na faixa e o mais fácil de pôr jogadores dentro.
- **Onde:** **Central Continent**, a região mais forte do mundo. Não tem sede única: são
  **centenas de locais de inscrição** espalhados, quase todos seitas médias ligadas às **dez
  grandes seitas antigas** ou representantes delas. As rodadas acontecem simultaneamente em
  vários desses locais.
- **Periodicidade:** **uma vez a cada cem anos**. Consequência social explícita: sem métodos
  especiais de prolongar a vida, **a maioria dos Gu Masters participa uma única vez na vida**.
- **Quem pode participar:** *qualquer um*. O cultivo de um Gu Master tem três facetas —
  **nutrir, usar e refinar** — e basta ter perícia ou experiência na terceira. Não é evento
  só de refinement path. Path reto e path demoníaco entram lado a lado; criminosos procurados
  se inscrevem abertamente **sem risco de prisão durante o evento**; mortais e Gu Immortals
  competem nas mesmas provas. A única regra absoluta é **não lutar e não matar** — só técnicas
  de refino decidem.
- **Por que o evento é assim tão aberto (o segredo por trás):** [segredo] a estrutura por trás
  do Convention colhe os **fracassos** dos participantes. Cada tentativa fracassada de refino,
  de qualquer competidor, em qualquer rodada, alimenta um mecanismo antigo que condensa
  fracassos em **success dao marks**. Mais participantes = mais fracassos = mais colheita. Por
  isso os organizadores impulsionam deliberadamente a escala e não filtram ninguém.
- **Como se entra:**
  - **Quatro tarefas de entrada** (four entry tasks): provas básicas de refino, iguais para
    todos naquela edição, feitas ali na hora. Servem só para barrar incompetentes — qualquer
    Gu Master com alguma experiência passa. Exemplo real de tarefa: refinar um Gu específico
    cujo antepenúltimo passo exige entrelaçar cem hastes de uma erva com cem fios de outra
    **em trinta respirações**; passou disso, o fogo do refino incinera tudo.
  - **Inscrição:** paga-se **100 primeval stones** e recebe-se um **token**. Os dados são
    deliberadamente flexíveis: nome pode ser inventado, seita e path podem ser omitidos. Só o
    token importa; perdê-lo é ficar de fora até conseguir outro.
  - **Vagas automáticas:** seitas e indivíduos que se colocaram bem na edição anterior (cem
    anos antes) recebem vagas sem prova — mas **só de Central Continent** (favoritismo regional
    declarado). Uma seita pequena que ficou perto do fim da lista ganhou **três vagas**
    (1 discípulo, 1 elder, 1 elder externo), disputadas internamente por competição de refino.
- **Estrutura da competição:**
  - **Rodadas eliminatórias sucessivas**, cada uma com uma tarefa de refino específica e um
    corte por **quantidade ou por tempo**. Recompensas em camadas: quanto maior a meta batida,
    melhor o prêmio.
  - Regra decisiva para mesa: **primeiro a chegar, primeiro a servir**. Só os **três primeiros**
    a bater cada meta levam 1º, 2º e 3º lugar — desempenho posterior **não conta**, mesmo que
    seja superior. Velocidade vale tanto quanto qualidade.
  - **A partir da 8ª rodada** o formato muda: cada local de prova produz **um único vencedor**
    (eliminação direta), e trocar de local significa abandonar a posição já acumulada.
  - Ainda na 8ª rodada em diante, cada competidor recebe **uma "chance de remoção"** por
    rodada: pode obrigar o adversário a revelar e entregar **um material de refino específico**
    dele — mesmo já escondido ou secretamente usado. Recusar implica revista completa, o que
    arruinaria a reputação em público.
  - Há uma competição **de grande escala** (as cinco regiões juntas, com eliminatórias
    regionais antes da final) e competições **de pequena escala** (uma por região) e até
    disputas informais entre amigos.
- **Formatos de disputa paralelos (paralelos ao torneio, e ótimos para mesa):**
  **sect contests** (times equivalentes resolvendo conflitos entre seitas), **duels** (desafio
  individual, com a aposta acordada pelos dois lados; um lado pode ceder ao outro a escolha da
  tarefa como desvantagem deliberada), **task contests** (um lado propõe um problema difícil,
  o outro tenta resolver) e **arena contests** (um perito monta a arena e a aposta, e
  desafiantes apostam também). Podem ser **abertas** (com público) ou **privadas** (sem público
  e sem divulgar o resultado). Nas abertas de grande escala, **espectadores são proibidos de
  usar qualquer Gu** durante a observação.
- **Economia paralela:** existe em Central Continent um **mercado legítimo de corretores de
  informação** que vende abertamente enunciados vazados de edições passadas, rankings e
  previsões (exemplos: 50 pedras por um "shadow image Gu" com o ranking dos cem primeiros; 10
  pedras por fofoca política). Competidores sérios treinam **décadas** em cima desses
  enunciados; um caso registrado fala em **80+ anos** de treino antecipado. Apostas em duelos
  são precedidas de espionagem sobre **de que material o adversário está precisando**, para
  montar a aposta mais tentadora possível.
- **Prêmios:** crescem por rodada — primeiro materiais e Gu mortais de rank crescente; nas
  rodadas finais, **immortal essence stones, materiais imortais, receitas de Immortal Gu e até
  immortal killer moves** para o primeiro lugar. E o prêmio máximo: os **seis primeiros
  colocados** recebem cada um **um success dao mark**, gravado no corpo ali mesmo. Um success
  dao mark **elimina a chance natural e aleatória de falha** de um refino (não cobre erro de
  técnica nem interferência externa), cobre **um Immortal Gu de até rank 6** e é
  **absolutamente intransferível** — nunca foi extraído de ninguém à força, nem pela maior
  potência do mundo. Quem quiser usá-lo só pode **contratar o próprio vencedor** para refinar
  em seu nome.
- **Hierarquia de perícia relevante ao evento:** ordinário → master → grandmaster → great
  grandmaster → supreme grandmaster. Só **três pessoas em toda a história** chegaram ao topo.
  Diferença de um *tier* inteiro é intransponível por preparação. Detalhe delicioso: Gu
  Immortals escondem o próprio rank ao competir, porque **perder para um mortal acontece de
  verdade** — o refino de Gu mortal é puramente técnico e não reflete a diferença de poder.
- **Papel possível de um grupo pequeno:** o evento é feito sob medida para personagens
  mortais de qualquer rank. O grupo se inscreve numa sede provinciana, atravessa as quatro
  provas de entrada, sobe rodadas, é desafiado para duelos com aposta, negocia materiais,
  compra enunciados no mercado cinza, e convive numa trégua forçada com criminosos famosos.
  Nada disso exige poder de combate.
- **Consequência para o mundo:** redistribui receitas, materiais e reputação em escala mundial
  a cada século; e alimenta, sem que os participantes saibam, um projeto de uma potência
  oculta.
- **Cuidado de spoiler:** ficam de fora quem venceu a edição descrita, os duelos nominais entre
  personagens da trama, e a identidade de quem colhe os fracassos e para quê.
- **Lacunas:** a obra não dá o número total de rodadas de uma edição inteira, nem o calendário
  detalhado, nem como as eliminatórias regionais se conectam à final.

### Calamidades terrestres e tribulações celestiais (earthly calamities / heavenly tribulations) — caps. 809, 824-826, 1053-1057, 1096-1099, 1111-1113, 1164

- **Tipo:** cataclismo periódico e privado — a "conta" que o céu cobra de todo Gu Immortal.
  Não é um evento do mapa: acontece **dentro** da abertura imortal da vítima. Mas é o desastre
  mais frequente do mundo imortal e o melhor cenário fechado da faixa.
- **Os quatro graus de provação, em ordem crescente de força:** **earthly calamity**
  (calamidade terrestre) → **heavenly tribulation** (tribulação celestial) → **grand
  tribulation** (grande tribulação) → **myriad tribulation** (miríade de tribulações, apelidada
  no mundo de "myriad tribulations apocalípticas").
- **Calendário completo por rank (dado numérico direto, cap. 1007):**

  | Rank | Essência imortal | Calamidade terrestre | Tribulação celestial | Grande tribulação | Miríade | Avanço de rank |
  |---|---|---|---|---|---|---|
  | 6 | green grape (uva verde) | a cada 10 anos | a cada 100 anos | — | — | após 300 anos / 3 tribulações celestiais → rank 7 |
  | 7 | red date (tâmara vermelha) | a cada 10 anos | a cada 50 anos | a cada 100 anos | — | após 300 anos → rank 8 |
  | 8 | white litchi (lichia branca) | — | a cada 10 anos | a cada 50 anos | a cada 100 anos | após 3 miríades → rank 9 |

  Em toda a história da humanidade **apenas dez pessoas passaram por três miríades de
  tribulações — os dez Veneráveis**. Sobreviver a uma única miríade já é glória mundial.
  Casos anômalos aceleram brutalmente o relógio: um corpo "que desafia o céu" pode receber
  **uma calamidade a cada dois meses**.
- **A saída extrema e seu preço (cap. 1007):** é possível pagar uma fortuna para **remover por
  completo o tributário do Rio do Tempo** da própria abertura imortal. O tempo interno para,
  e **as calamidades deixam de chegar**. Em troca, a abertura **para de produzir immortal
  essence** e, sem provações, os dao marks do dono não aumentam: o cultivo congela junto.
  Métodos de time path que apenas *pausam* têm limite de duração e custo crescente. Mesmo
  assim, **a maioria dos Gu Immortals do mundo atual usa time path para desacelerar** a própria
  abertura — e os rank 8 de uma certa potência passam o tempo normal **hibernando**, que é
  descrito como um dos melhores métodos de desaceleração existentes.
- **Causa mecânica (a regra que governa tudo):** "o caminho do céu tira dos excedentes e repõe
  aos deficientes, com ênfase no equilíbrio". **Quanto mais rica e profunda a fundação de uma
  abertura imortal, mais forte a calamidade que ela atrai.** Prosperar é perigoso.
- **Contramedidas conhecidas (ótimas como decisões de jogadores):**
  - **Empobrecer-se temporariamente:** mover os recursos mais preciosos para a abertura de um
    aliado antes da data, para atrair uma calamidade mais fraca.
  - **Elevar a própria sorte** com métodos de luck path: quanto maior a sorte pessoal, mais
    branda a calamidade.
  - **Desacelerar o tempo interno** da própria abertura com métodos de time path — as
    calamidades ficam mais raras, mas **a produção de recursos cai na mesma proporção**. Trocar
    crescimento por segurança é uma decisão econômica explícita, e o serviço é **contratado de
    especialistas**, não improvisado.
  - **"Pôr a abertura para fora"** (procedimento padrão): o corpo do Gu Immortal é puxado para
    dentro; a abertura ocupa um ponto físico do mundo externo e fica invisível. Enquanto isso
    ele **não pode sair** — é como um land spirit dentro do próprio mundo —, mas a abertura
    **suga qi do céu-e-terra externo** para se estabilizar (em três fases decrescentes:
    cachoeira, grande rio, riacho, até o "apetite" se esgotar), e o tempo interno **desacelera
    temporariamente para quase 1:1** com o exterior.
  - **Aviso prévio:** toda calamidade dá um pressentimento sensorial universal, sentido por
    qualquer Gu Immortal — a comparação do texto é com animais que sentem o terremoto chegando.
- **Ambiente por dentro (como rodar uma na mesa):** a calamidade se manifesta como um
  **desastre ambiental temático** que ataca justamente o maior trunfo da terra, e vem em
  **ondas**. Exemplos completos registrados:
  - **Blood Poison Kerria** (caps. 824-826): flores gigantes do tamanho de um rosto, com umas
    cem pétalas em seis ou mais camadas, brotando explosivamente pela terra inteira; o ciclo de
    brotar-a-murchar dura **dez respirações**, e ao murchar viram poça de sangue venenoso que
    contamina o solo e mata em larga escala. Só técnicas de wood path lidam com as flores em
    si; qualquer outro método de destruição **também** gera o veneno. A limpeza exige remover
    fisicamente a camada superficial de solo em poucos dias, antes que apodreça e contamine o
    resto.
  - **Nevasca com snow monsters** (caps. 1053-1057): a nevasca é o meio de nutrição. Os
    monstros têm um **núcleo oculto**; feridas comuns cicatrizam na hora. O tamanho dá o tier:
    10-20 pés = trivial; 60 pés = nível desolate beast (rank 6); 70 pés = ancient desolate
    (rank 7). E há a regra hidra: **matar um grande o estilhaça em vários menores**, que
    **crescem com o tempo** enquanto a nevasca durar — mas abaixo de dez pés a cadeia termina.
    Suprimir localmente a nevasca desacelera o crescimento, e a nevasca **responde
    intensificando-se** e destrói a supressão. Ondas posteriores trazem criaturas de neve
    específicas (águias, grous em grupo de nove, um morcego de space path que distorce o espaço
    a ponto de um passo custar centenas e que pode **estilhaçar as paredes da própria abertura**
    se não for contido).
  - **Wind Flower Snow Moon** (caps. 1096-1099) e uma calamidade em que **a ordem das duas
    metades foi invertida** deliberadamente pelo céu (caps. 1111-1113) — o sistema não é
    previsível nem justo.
- **Regra especial importante:** **battlefield killer moves de nível imortal não podem ser
  usadas dentro da própria abertura** (os dao marks colidem e danificam a terra); só as de
  nível mortal, que carregam poucos dao marks, são seguras. Isso fecha a saída óbvia de
  "prender os monstros num campo de batalha".
- **Prêmio:** sobreviver rende **dao marks novos e temáticos**, que remodelam o ecossistema da
  abertura e habilitam recursos melhores. Registro concreto de uma terra que começou sem água
  e sem vento: calamidades sucessivas trouxeram dao marks de madeira e terra (ervas e flores
  básicas), depois de fogo, depois de água, depois de sangue — e a de sangue habilitou gramas e
  flores de rank 3, uma espécie nova de raposa criável, e a mutação espontânea de parte dos
  peixes num tipo várias vezes mais valioso. "A boa sorte se esconde na má."
- **Papel possível de um grupo pequeno:** os jogadores como a equipe que um Gu Immortal
  contrata (ou escraviza) para atravessar a calamidade dentro da terra dele: conter as ondas,
  salvar plantações e populações, remover solo contaminado sob prazo, caçar núcleos. Cenário
  fechado, com relógio, ondas escalonadas e um patrono que **perde dinheiro a cada erro**.
- **Consequência para o mundo:** estrutural e constante — é o mecanismo que impede que
  riquezas se acumulem indefinidamente e que mata a maioria dos Gu Immortals.
- **Cuidado de spoiler:** ficam de fora quem sobreviveu a quê e a razão específica pela qual um
  personagem em particular é perseguido pelo céu.
- **Lacunas:** a obra não dá a tabela completa de calamidades por rank acima de 6, nem como o
  tipo de calamidade é sorteado.

### Marés de bestas (beast tides) — caps. 850, 1034-1036, 1085-1089, 1093, 1138, 1183

- **Tipo:** desastre natural regional; é o desastre-padrão que ameaça aldeias e clãs mortais.
- **Gatilho / causa mecânica:** acúmulo excessivo de bestas selvagens na vizinhança de um
  assentamento. Duas regras explícitas e muito úteis:
  1. **Uma maré natural é de uma espécie só** — maré de lobos, maré de tigres. Uma maré em que
     lobos, tigres, leopardos, touros, veados, raposas e cobras avançam **misturados e sem se
     atacarem** é o sinal inequívoco de que **não é um desastre natural, é um desastre humano**
     (cap. 1034).
  2. É preciso **haver população de bestas suficiente** nos arredores para formar uma. Um clã
     que acabou de sobreviver a uma maré há um ano sabe que **não há bestas bastantes** para
     outra — anomalia que deve ser investigada.
- **Periodicidade:** irregular; o texto registra clãs que enfrentam uma maré séria a cada
  poucos anos e uma "de uma escala não vista em décadas" como marco de catástrofe.
- **Defesa típica de um clã mortal (pronta para mesa):** **três camadas de defesa** ativadas em
  sequência; uma **Gu formation ofensiva** operada pelos elders e pelas elites (no caso citado,
  uma "heavenly fire Gu formation"); um **salão de medicina** com equipe médica mobilizada; e
  uma **Gu formation de transporte** conferida com antecedência, para **evacuar os jovens** se
  a muralha cair. Batedores de elite são enviados para procurar a *causa* enquanto a defesa se
  arma.
- **Escala imortal — as fierce areas:** nas grandes zonas selvagens, uma maré de bestas não é
  de bestas comuns: é de **desolate beasts e ancient desolate beasts**, com possibilidade de
  atrair **immemorial desolate beasts**. Nessa escala, **nenhum Gu Immortal quer causar uma** —
  o texto é explícito de que até um rank 8 precisa de cuidado, e que super forças evitam operar
  nessas áreas exatamente por isso. Uma maré nesse nível arrasta quem estiver dentro como "uma
  tábua flutuando em água revolta": não se luta contra ela, anda-se junto com ela.
- **Uso como arma:** [segredo] uma maré de bestas pode ser **fabricada** — como cobertura para
  um massacre, ou como ferramenta de caça: quando a vontade do céu (heaven's will) sabe a
  região aproximada de um alvo mas não a posição exata, ela **provoca uma maré enorme para
  varrer a área e expor o alvo**. Nesse caso a maré muda de direção conforme o alvo se move.
- **Papel possível de um grupo pequeno:** o cerco de aldeia clássico, e a investigação que vem
  junto — a maré errada é uma pista.
- **Lacunas:** a obra não dá números de bestas nem duração típica.

### Earth tide e a travessia das paredes regionais — caps. 818-819, 928, 987, 1042-1048

- **Tipo:** fenômeno natural periódico que abre a única janela de viagem entre regiões.
- **Regra de base:** as cinco regiões são separadas por **paredes regionais** (regional walls),
  e atravessá-las é "extremamente difícil" para um Gu Immortal em condições normais. Cada
  parede tem sua natureza e cor: a de Southern Border é a **miasma regional wall**
  (púrpura-negra), a de Eastern Sea é a **blue water regional wall** (azul profunda). Dentro
  da parede **não há criaturas nem obstáculos** — a parede *é* o obstáculo. Efeito curioso e
  aproveitável: ao atravessar, **a aura regional do viajante muda sozinha** — a aura da região
  de origem enfraquece e a da região de destino se fortalece, sem killer move nenhum.
- **Quem passa e quem não passa:** **desolate beasts, ancient e immemorial desolate beasts
  quase não conseguem sair da própria região** — eles carregam a essência dela, e as paredes
  são grilhões para eles. **Bestas comuns, beast kings e bestas mutantes circulam livremente.**
  A exceção são criaturas originárias dos **nove céus imemoriais**, que não pertencem a região
  nenhuma e por isso ignoram as paredes.
- **O evento:** **uma vez por ano**, uma **earth tide** (maré da terra) sobe do fundo do mar em
  Eastern Sea, agita a água e **enfraquece e afina a parede regional** daquela região. É a
  janela em que Gu Immortals de Central Continent, Northern Plains e Southern Border entram em
  Eastern Sea — e alguns saem. (Os de Western Desert quase nunca aparecem: estão do outro lado
  do mundo, separados pelas outras regiões, e um deles em Eastern Sea chama muita atenção.)
- **Perigo e regra especial:** mesmo enfraquecida, a passagem é letal. A área fraca fica cheia
  de **forças de maré sem forma** (formless tidal forces) que funcionam como recifes e vórtices
  invisíveis; ser atingido por uma, no julgamento de uma personagem, faz "ossos quebrados serem
  o menor dos problemas — é bem possível morrer violentamente na hora".
- **A economia do evento (o gancho de mesa):** atravessar exige uma **rota mapeada com
  precisão**. Idealmente deduzida por um Gu Immortal de wisdom path; sem isso, só por tentativa
  e erro, pagando com vidas. Mapas de rota são **mercadoria valiosa**, negociáveis por pontos
  de contribuição junto a super forças — e são **perecíveis**: depois de algumas earth tides as
  forças de maré mudam e a rota velha não vale mais nada. Um viajante com rota própria **recusa
  escolta** para não revelá-la.
- **Papel possível de um grupo pequeno:** ser os cartógrafos. Vender travessias. Roubar mapas.
  Ou simplesmente: a janela abre uma vez por ano, e o grupo precisa estar do lado certo antes
  de ela fechar.
- **Consequência para o mundo:** é o que faz o comércio, a migração e a espionagem entre
  regiões existirem. Northern Plains, pobre em recursos e rica em guerras, exporta gente para
  Eastern Sea a cada maré.
- **Lacunas:** a obra não descreve a earth tide das outras quatro regiões, nem a duração exata
  da janela.

### Aberturas do Treasure Yellow Heaven — caps. 1032-1033, 1104

- **Tipo:** mercado imortal transregional que **abre e fecha**, e cujas aberturas param o mundo
  imortal.
- **O que é:** um espaço de mercado acessado por consciência (via um Gu de conexão), onde Gu
  Immortals das cinco regiões negociam **atravessando as paredes regionais** — o transporte
  real é feito por um Gu mortal capaz de mandar objetos através das paredes, chamado no texto
  de "Gu mortal supremo" por causa dessa capacidade.
- **Mecânica de mercado (excelente para mesa):**
  - Toda transação gera uma **coluna de luz visível** cuja **altura é proporcional ao valor**
    do que foi negociado — e a **taxa de transporte é cobrada com base nessa altura**. Ou seja:
    **não existe transação discreta**; negociar grande é anunciar publicamente que se negociou
    grande.
  - É um mercado **aberto**: dezenas de imortais percebem a coluna simultaneamente. Vender
    material de rank 8 causa "comoção" e especulação generalizada; vender um Immortal Gu é raro
    o bastante para virar notícia mundial.
  - **Não existe moeda obrigatória**: as partes podem combinar pagar um Immortal Gu rank 7 com
    uma pedra comum, porque o sistema só registra e taxa a *transação*, não o valor combinado.
    Isto é, o mercado pode ser usado para **disfarçar** presentes, subornos e pagamentos.
  - Fica **fechado por períodos** e a **reabertura** é um evento: todos os que esperavam
    explodem em atividade ao mesmo tempo, e mensagens acumuladas chegam de uma vez.
- **Quem fica de fora:** mundos isolados (grotto-heavens fechados) **não conseguem se conectar**
  — e o texto trata isso como uma condenação: sem o mercado, uma comunidade acumula quantidade
  mas não variedade, os métodos ficam desatualizados e o conhecimento estagna.
- **Papel possível de um grupo pequeno:** ninguém precisa lutar. Um grupo pode viver de
  arbitragem entre regiões, de encomendas, de descobrir quem vendeu o quê pela altura da
  coluna de luz, ou de ser o intermediário que um cliente rico usa para não aparecer.
- **Lacunas:** a obra não explica o que determina quando o mercado abre e fecha.

### Sucessão do rei dos feathermen — torneio de arena — cap. 864

- **Tipo:** torneio institucional de sucessão, em escala mortal.
- **Onde:** **Sacred Feather City**, a cidade flutuante dos feathermen.
- **Gatilho:** a morte do rei. Pelo costume do povo, o novo rei é **escolhido em combate**.
- **Regras (curtas e completas, prontas para uso):**
  1. Para ser **candidato**, é preciso ser **reconhecido pela maioria dos cidadãos** — e o
     critério declarado é **reputação de boas ações e serviços prestados à cidade**, não força.
     O povo não quer um tirano, quer um herói compassivo.
  2. Os candidatos aprovados lutam em **combates de arena**, diante de **dezenas de milhares**
     de espectadores, até a final.
  3. Existe uma trava institucional: **três supreme elders Gu Immortals** do povo, que
     controlam a situação caso um cruel vença mesmo assim.
- **Observação de mesa:** os finalistas descritos são **rank 5** (o teto mortal) e o combate é
  puramente de Gu Masters; o público torce em coro, e a narrativa da cidade sobre quem "parece
  um rei" pesa tanto quanto o resultado. É um evento inteiro rodável sem nenhum imortal em cena.
- **Lacunas:** a obra não descreve o processo de endosso popular em detalhe nem a periodicidade
  (é por morte do rei, não por calendário).

### As dez grandes áreas ferozes de Northern Plains (ten great fierce areas) — caps. 781, 1085-1091, 1173-1176

- **Tipo:** zonas de perigo permanentes; não são um evento com data, mas são o motor de
  incontáveis expedições e o único lugar onde ainda há o que pegar.
- **Regra de mundo que as justifica (cap. 1085):** "Northern Plains é vasta, mas as grandes
  forças e super forças **já dividiram entre si todos os recursos de cultivo** da região. O que
  restou foram, principalmente, as dez grandes áreas ferozes." Ou seja: **num mundo já
  repartido, a fronteira é o que é perigoso demais para ser repartido.**
- **Característica comum:** habitadas por desolate beasts e ancient desolate beasts em massa,
  com immemorial desolate beasts nas profundezas. **A aura de um Gu Immortal provoca as
  feras**; mortais passam despercebidos. Qualquer combate de escala mínima ali dentro
  desencadeia uma maré de bestas — e a maré, sendo perceptível de longe, **denuncia quem está
  lá**. Consequência estratégica explícita: nem super forças querem montar base dentro delas.
- **Exemplos descritos na faixa:**
  - **Tai Qiu**: selva primitiva de **grama gigante** (um talo equivale a uma árvore centenária).
    Foi usada como terreno de herança justamente porque só mortais atravessam. Existe um **mapa
    detalhado de Tai Qiu**, fruto de viagens repetidas de um grande imortal somadas a deduções
    de terceiros — um item de campanha por si só.
  - **Earth Trench** (ver entrada própria em "Eventos únicos").
  - **Crazed Demon Cave** (caps. 1173-1176): [segredo] é uma área feroz **apenas na aparência**.
    Foi **construída de propósito** por um dos rank 9 Veneráveis nos últimos anos de vida, para
    perseguir o segredo da vida eterna. Estrutura em **nove camadas**: (1) floresta tropical com
    desolate beasts; (2) terreno de rochas incandescentes; (3) névoa perpétua produzida por
    bambu-nuvem em larga escala, contendo a **Fog City**, cidade formada por almas vingativas de
    Gu Immortals mortos — entrar é morte quase certa; camadas seguintes progressivamente
    piores. Os **três eremitas** que moram lá há séculos **não ousam entrar nas três últimas
    camadas**. Os "sons demoníacos" que dão nome ao lugar são **efeito colateral** de uma
    super Gu formation montada em torno de um Gu lendário na camada mais funda: o objetivo do
    Venerável não era enlouquecer ninguém, era **transformar e misturar dao marks** de seres
    vivos em busca de dao marks nunca vistos, como material de pesquisa.
- **Papel possível de um grupo pequeno:** as áreas ferozes são a resposta da obra para "onde um
  grupo fraco vai buscar fortuna num mundo já dividido". A profundidade é o dial de
  dificuldade; a superfície é acessível e já perigosa; guias locais e mapas são o recurso mais
  caro.
- **Lacunas:** a obra não lista as dez áreas; nomeia apenas algumas.

### Turbulent flow sea area — zona de encontros fortuitos — caps. 1150-1159

- **Tipo:** zona de perigo e tesouro permanente, em escala imortal; o equivalente marítimo das
  áreas ferozes.
- **Onde:** Eastern Sea, perto da parede regional daquela região.
- **Como se formou:** acúmulo de **dao marks de batalhas históricas intensas** entre muitos Gu
  Immortals de rank 6 e 7. Superfície aparentemente calma, correntes caóticas por baixo, e
  **nuvens permanentes** que impedem orientação por sol ou estrelas.
- **Ambiente por dentro (um dos cenários mais vistosos da faixa):** múltiplas **correntes**,
  cada uma feita de um material vindo de um lugar diferente do mundo — água do rio dos mortos,
  água de mil ilusões (que exige wisdom path para atravessar), uma corrente de **magma** vinda
  de uma cratera do Western Desert que entra em erupção a cada cem anos, água de almas negras
  carregada de dao marks de soul path e dark path, uma corrente de fragmentos de ouro que
  sobrou de um rio celestial de um dos nove céus imemoriais, e uma corrente de água-relâmpago.
  Onde as correntes colidem e se equilibram formam-se **"olhos de furacão"** (espaços vazios
  temporários, onde dá para descansar) e **"bolhas"** — cada bolha contendo um **mundo
  fragmentado inteiro**, com ilhas, ruínas e heranças.
- **Por que se vai lá:** atrai caçadores de "fortuitous encounters" das cinco regiões, porque
  historicamente guarda heranças e riquezas de Gu Immortals mortos ali.
- **Sociedade local:** existe um circuito social de imortais solitários que **organiza leilões
  privados** entre si — mercado paralelo ao mercado aberto, com acesso por indicação, e onde se
  usa **Gu de longevidade como moeda**. Grupos veteranos abordam recém-chegados oferecendo
  acesso à rede em troca de ajuda em buscas de longo prazo (uma delas dura mais de dez anos e,
  por natureza, "não depende de cultivo, depende de sorte").
- **Papel possível de um grupo pequeno:** navegação por correntes hostis, cada uma exigindo um
  path diferente para ser atravessada com segurança; bolhas como mini-cenários auto-contidos;
  e uma rede social de exploradores para dar missões e comprar informação.
- **Lacunas:** a obra não mapeia a zona nem diz quantas bolhas existem.

## Eventos históricos citados

## Candidatos a nota própria

