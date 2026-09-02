# Auditoria dos catálogos de golpes assassinos

Arquivos auditados: `10 - Apendices/07 - Catálogo de Golpes - Mortais.md` e
`10 - Apendices/08 - Catálogo de Golpes - Imortais.md`.

Estado inicial: 90 golpes mortais em 22 caminhos, 580 imortais em 35 caminhos,
677 nomes distintos somando os dois arquivos.

## Método

1. **Varredura de nomes.** Quatro famílias de expressão regular sobre os seis volumes,
   sempre em minúsculas (`grep -i`), porque a obra grafa o nome do golpe em caixa baixa
   no meio da prosa:
   - `killer move[s] — <Nome>.` (travessão, o padrão de anúncio em combate);
   - `killer move called/named '<nome>'`;
   - `killer move, <nome>,` (aposto após vírgula);
   - `(mortal|immortal|battlefield|movement|offensive|defensive) killer move <nome>`;
   - mais uma varredura de nomes gritados entre aspas com exclamação e de
     `move — <Nome>`.
2. **Cruzamento.** Os candidatos foram normalizados (minúsculas, sem pontuação) e
   comparados com os 677 nomes já catalogados, inclusive por substring nos dois
   sentidos, para não contar como novo um golpe já presente sob grafia levemente
   diferente.
3. **Filtro de ruído.** Lista de palavras funcionais do inglês descartou os falsos
   positivos gramaticais (o regex captura o começo da oração seguinte quando o nome do
   golpe não é seguido de pontuação forte).
4. **Leitura de contexto.** Cada candidato sobrevivente foi lido no texto com 3 linhas
   antes e 8 a 12 depois, em **todas** as ocorrências dos seis volumes, para (a)
   confirmar que é golpe e não Gu, formação, lugar ou método de refino; (b) extrair
   caminho, composição, efeito, custo e limite; (c) localizar o capítulo.
5. **Revisão dos rótulos.** Para cada golpe que o catálogo declarava como "a obra apenas
   nomeia", foi contada a totalidade das ocorrências nos seis volumes e lido o entorno de
   cada uma, mais buscas dirigidas pelo nome do Gu Imortal-núcleo, pelo nome do dono e
   pela família de golpes a que pertence — porque em vários casos o efeito está em
   capítulo diferente daquele em que o nome é gritado.

## Golpes acrescentados

31 golpes novos: 28 no catálogo imortal, 3 no mortal.

### Catálogo imortal

| Golpe | Caminho | Capítulo(s) |
|---|---|---|
| Fixed Luck | sorte (núcleo de regra) | 1415 |
| Gentleman's Bamboo | sabedoria | 768 |
| Broken Mirror Shard Light | luz | 1716, 1929 |
| Benevolent Equality | caminho não nomeado | 1748, 1789, 1918, 1929 |
| Golden Thread Sword | espada | 1819, 1944, 1945, 1946 |
| Soaring Fighting Spirit | sabedoria (núcleo de regra) | 1396, 1463 |
| Purple Star Broken Life 🏟 | sabedoria | 1485, 1487, 1488, 1572 |
| Blasting Qi Roar | qi | 883 |
| Rugged Fiendish Qi | qi | 2181 |
| Phoenix Chirping Divine Flame | fogo | 1937 |
| Multi-layered Five Poisons | veneno (ded.) | 2157 |
| Countless Injury Marks | humano | 1915, 2197 |
| Bow Shadow Cup | maldição (*curse path*) | 1436 |
| Collapsing Art | caminho não nomeado | 1338 |
| Extended Dark Concealment | trevas | 1346 |
| Sword Burial Abyss | espada | 1434 |
| Nine-Nine Reincarnation Blades | lâmina (*blade path*) | 1434 |
| True Stability Transformation | transformação | 1547 |
| True Stability Branch Transformation | transformação | 1547 |
| Lightning Heart Explosion | raio (ded.) | 1759 |
| Soul Armor Combat | alma (ded.) | 1759 |
| Air Lock | vento (ded.) | 1386, 1387 |
| Helpless Withering | madeira e flores | 1875 |
| Golden Heavenly Saint ⚔ | formação de batalha antiga | 883, 941 |
| Heavenly Giant Solor ⚔ | formação de batalha antiga | 883 |
| Green City Rampage ⚔ | formação de batalha antiga | 941 |
| Omni-directional Travel ⚔ | formação de batalha antiga | 1090, 1151, 1387, 1487 |
| Twelve Zodiac Battle Formation ⚔ | formação de batalha antiga (projetada) | 1609 |

### Catálogo mortal

| Golpe | Caminho | Capítulo(s) |
|---|---|---|
| Break Dream | sonho | 1611 |
| Limitless Search and Lock | caminho não nomeado (cooperativo, 4 usuários) | 362 |
| Turtle House | caminho não nomeado (cooperativo, 7 usuários) | 568, 1754 |

Notas de peso sobre três deles:

- **Turtle House** não é só mais um golpe: a obra o registra como **a primeira Casa de
  Gu da história**, e usa esse fato para definir o que uma Casa de Gu *é* — "golpes
  assassinos formados pela combinação e solidificação de dez ou mais tipos de Gu". Sete
  irmãos rank 5 auge somaram forças e aguentaram três ataques de um Gu Imortal,
  originando o "pacto dos três golpes". Faltava no catálogo o golpe que fundamenta uma
  categoria inteira do mundo.
- **Break Dream** é mortal e derruba um reino de sonho — enquanto golpes dos caminhos
  antigos, "mesmo de nível nove, mesmo Casas de Gu Imortal de rank nove", são pedras
  atiradas no mar dentro de um reino de sonho. É o contraexemplo canônico à regra de que
  rank alto vence rank baixo.
- **Nine-Nine Reincarnation Blades** custa **cem anos de vida por uso**, e seu dono o
  usou três vezes na vida inteira. É o preço mais alto e mais claramente numerado de
  qualquer golpe dos dois catálogos.

## Rótulos resolvidos

Dos golpes que o catálogo declarava como "a obra apenas nomeia", estes ganharam
mecânica canônica com busca dirigida:

| Golpe | O que se achou | Onde estava |
|---|---|---|
| **Slaughtering Immortal Guillotine** | O parágrafo seguinte à salva mapeia cada golpe ao seu caminho: "The wood path killer move made the leaves fly around. **The blade path killer move slashed forward without obstacles**". Confirma efeito e revela o caminho — **lâmina**, não espada | cap. 880, uma linha adiante do grito |
| **Mixed Hole Drill** | A mesma frase de fechamento da salva — "Ice path, **space path**, and dark path killer moves were used in succession" — confirma o caminho do espaço, que o catálogo só supunha | cap. 880 |
| **Shattered Ice Armor** | Idem: confirmado como caminho do gelo pela mesma frase, e situado como parte de uma rajada em que o usuário **trocava Gu mortais e Imortais "como quem troca de roupa"** entre um golpe e o seguinte | cap. 880 |
| **Wishful Shadow Sword** | Idem: confirmado como caminho das trevas pela mesma frase | cap. 880 |
| **Pursuing Flying Sword** | O núcleo da família inteira **não é** *sword escape*: é a **flying sword Gu, Gu Imortal rank 7 em forma de libélula de asas prateadas**, "o Gu Imortal mais usado em combate" por seu criador. A *sword escape Gu* é o Gu seguinte da lista, de movimento, em forma de abelha dourada | cap. 995, no inventário dos Gu Imortais do dono |
| **Heavy Soil Comeback** | É um dos **três golpes de uma Casa de Gu Imortal** (Peaceful Soil Heavy Mountain Fortress), ao lado de *accumulated soil mountain* e *peaceful burial* — e o capítulo revela que **o núcleo daquela Casa não é um Gu Imortal, e sim o golpe** *accumulated soil mountain*, um golpe de terra com efeito de formação que permite empilhar Gu de terra até formar uma Casa de Gu Imortal **mesmo com zero de proficiência em formação** | cap. 1898 |
| **Three Winged Green Bird** | A obra descreve, na mesma cena, **o modelo que o golpe imita**: a tribulação *grand clear space*, bandos de pássaros que na verdade são **poder do caminho do espaço** — por onde passam, o espaço é varrido e nada pode existir ali; circulam o alvo e abrem feridas longas e fundas como lâminas | cap. 1015 |
| **Fatal Injuries** e **Seven Laborious Injuries** | Sem efeito próprio, mas a **família inteira** ganhou origem e lógica: criados por Shen Shang sobre a *heal injury* Gu Imortal, na formação submarina de Paradise Earth dentro da baleia-dragão-azul; da série nasceu *countless injury marks*, dela foi deduzida a receita da **injury mark Gu Imortal**, que Shen Shang refinou e pôs como Gu vital — com ela, todo ataque que o fere vira marca de ferimento, e quanto mais marcas, mais forte fica *mutual injuries*, seu golpe ofensivo principal | cap. 1915 e 2197 |
| **Hidden Dragon Qi Explosion** | Sem efeito próprio, mas a obra classifica: está no grupo dos golpes **ofensivos de qi** do dono, e diz que esse grupo inteiro tem "poder de longo alcance muito mais evidente" que o grupo ofensivo do outro sistema de combate dele | cap. 1945 |
| **Heavenly Combat Cloak** | Confirmado **defensivo**: o dono recua e o manto derrete sob a fumaça negra do caminho da alma, "mas o golpe estranho acabou sendo bloqueado". Ou seja, cumpriu a função e foi consumido no processo | cap. 2033 |
| **Thought Body Defense** e **Single Thought Myriad Flow Elimination** | Sem efeito descrito, mas passaram a ter proveniência e requisito: são do arsenal de sabedoria de Purple Mountain True Monarch, usados por ele contra um rank 8 de auge; **só quem tem proficiência de grão-mestre em sabedoria está qualificado a modificá-los**, e mesmo assim exigem treino até a ativação sair certa | cap. 1463 e 1465 |
| **Snow Avalanche**, **Crashing Rock Slide**, **Great Earth Collapse** | Sem efeito, mas com cena situada: salva simultânea de cinco golpes imortais disparada pelos Gu Imortais de Green Lotus contra o grupo de Ice Crystal Immortal Monarch — os outros dois da salva são *Refine Life* e *Multi-layered Five Poisons* | cap. 2157 |

## Rótulos confirmados como silêncio real

Verificados um a um, contando **todas** as ocorrências nos seis volumes. A obra nomeia
e não explica:

| Golpe | Ocorrências | Situação |
|---|---|---|
| Pursuing Flying Sword | 1 | Só o nome, numa lista de quatro golpes irmãos. O núcleo foi corrigido; o efeito continua ausente |
| Slaughtering Immortal Guillotine | 1 | Efeito parcial resolvido (corte que avança sem obstáculo); composição e custo seguem ausentes |
| Sword Light Disintegration | 1 | Só "num instante, luz de espada voou por toda parte" |
| Life Staking Blood Print | 1 | Só o nome, como um dos três golpes construídos sobre a *blood asset* Gu Imortal |
| Thought Body Defense | 2 | Nenhuma das duas traz efeito |
| Single Thought Myriad Flow Elimination | 2 | Nenhuma das duas traz efeito |
| Mixed Hole Drill | 1 | Caminho confirmado, efeito ausente |
| Fatal Injuries | 5 (2 do golpe, 3 de prosa comum) | As duas ocorrências do golpe são a mesma lista, repetida em dois capítulos |
| Seven Laborious Injuries | 2 | A mesma lista, repetida |
| Hidden Dragon Qi Explosion | 1 | Só o nome, num inventário de sistema de combate |
| Heavenly Combat Cloak | 2 | As duas da mesma cena; papel defensivo confirmado, forma e duração ausentes |
| Shattered Ice Armor | 1 | Caminho confirmado, efeito ausente |
| Snow Avalanche | 1 | Caminho pelo nome; efeito ausente |
| Crashing Rock Slide | 1 | Idem |
| Great Earth Collapse | 1 | Idem |
| Heavy Soil Comeback | 1 | Contexto resolvido, efeito próprio ausente |
| Wishful Shadow Sword | 1 | Caminho confirmado, efeito ausente |
| Thunder Fish Totem | 2 | Só nomeado ao lado dos outros totens básicos |
| Heaven and Earth Blade | 2 | A ativação foi interrompida antes de qualquer efeito |
| Three Winged Green Bird | 1 | Efeito próprio ausente; o modelo que ele imita, porém, está descrito |
| Multi-layered Five Poisons | 1 | Novo no catálogo, e já entra como rótulo |
| Heartache Crying Blood | 2 | Já verificado em leva anterior; mantido |
| Thunder Note Stream | 2 | Já verificado em leva anterior; mantido |

Um rótulo não é falha de pesquisa: é o registro honesto de que a obra guardou o nome e
não a mecânica. Nas fichas, isso está dito com todas as letras, o que é permissão
explícita para a designer preencher sem contradizer o cânone.

## Falsos positivos descartados

| Expressão | Por que não entra |
|---|---|
| `strength path giant hand` | Não é golpe autônomo: é a **descrição** da mão conjurada por *Myriad Self — First Style — Giant Hand*, que já está no catálogo. A cena, porém, rendeu números canônicos que foram incorporados àquela ficha |
| `yama throughout the way` | Não é nome de golpe: é prosa ("manteve o golpe imortal *yama* o caminho inteiro"). O golpe é *Yama*, já catalogado |
| `wrecking dark flow giant city` | Não é nome de golpe: a frase diz que o personagem quebrou o golpe de campo de batalha, **arruinando** Dark Flow Giant City — que é uma Casa de Gu Imortal, não um golpe |
| `heavenly crystal eagle nest` | Não é golpe: é o **local/recipiente** de uma herança verdadeira, sobre o qual foram usados golpes do caminho do refino |
| `encompassed attack` | Prosa: "these immortal killer moves **encompassed** attack, defense, movement..." — verbo, não nome |
| `falling star rod transformation` | Grafia curta de *Falling Star Rod Tree Transformation*, já catalogado |
| `mountain suppression`, `one step back` | Já catalogados (o segundo sob o nome completo *One Step Back, Sea and Sky Expands*) |
| `fixed luck` como Gu | O nome coincide com um título de capítulo; verificado que a obra o chama explicitamente de "immortal killer move, fixed luck" |
| ~200 capturas gramaticais | O regex captura o início da oração seguinte quando o nome do golpe não termina em pontuação forte ("was activated", "in essence", "otherwise", "but now"). Descartadas por filtro de palavras funcionais e conferência visual |

## Correções de caminho e de composição

| Golpe | Estava | Passa a ser | Evidência |
|---|---|---|---|
| Formless Flying Sword | núcleo *Sword Escape* | núcleo **flying sword Gu**, Gu Imortal rank 7 | cap. 995: "The fourth Immortal Gu was flying sword Gu... Using this Immortal Gu as a core... he created many sword path killer moves... included the killer moves formless flying sword, cloud flying sword, pursuing flying sword, ten thousand li flying sword" |
| Cloud Flying Sword | núcleo *Sword Escape* | núcleo **flying sword Gu** | idem |
| Pursuing Flying Sword | núcleo *Sword Escape* | núcleo **flying sword Gu** | idem |
| Ten Thousand Li Flying Sword | núcleo *Sword Escape* | núcleo **flying sword Gu** | idem |
| Slaughtering Immortal Guillotine | caminho da espada | **caminho da lâmina** (*blade path*) | cap. 880: "The blade path killer move slashed forward without obstacles" — o único golpe de lâmina daquela salva é este |

A distinção importa: a obra trata **espada** e **lâmina** como dois caminhos separados,
com dois grandes especialistas rivais nomeados (Xi Yuan, do caminho da espada, e Dao Jiu
Lang, do caminho da lâmina), e Red Lotus Demon Venerable usou a aura de espada de um e a
aura de lâmina do outro para proteger um mesmo trecho do Rio do Tempo.

## Categorias especiais aplicadas

- 🏟 **campo de batalha** aplicado a *Purple Star Broken Life*, que a obra chama
  literalmente de "immortal battlefield killer move" e cujo funcionamento ela descreve
  em detalhe (cap. 1485 e 1572).
- ⚔ **formação de batalha antiga** é uma categoria nova, criada nesta auditoria porque a
  obra a nomeia com todas as letras ("ancient battle formation") e a distingue tanto do
  golpe comum quanto da formação de Gu do presente: usa **pessoas** (ou feras) como
  núcleos de formação, soma as forças dos participantes num só corpo e sobreviveu à Era
  da Antiguidade Remota. Cinco entradas.
- **Cooperativo/multiusuário** aplicado a *Turtle House* (7 usuários) e *Limitless Search
  and Lock* (4 usuários), ambos declarados pela obra como golpes formados pela combinação
  de várias pessoas.
- 🔗 **composto** não foi acrescentado a nenhum golpe novo: nenhum dos 31 recebeu da obra
  a declaração de dois caminhos principais.

## Decisões tomadas

1. **Formação de batalha antiga entra nos catálogos.** A obra as chama de golpes
   assassinos de fato ("Gu houses were killer moves formed by the combination and
   solidification of ten or more various kinds of Gu worms" — cap. 568) e as ativa com a
   mesma gramática de cena ("Ancient battle formation — Omni-directional Travel!").
   Deixá-las de fora seria omitir a forma cooperativa mais poderosa do sistema.
2. **Twelve Zodiac Battle Formation entra marcada como projeto.** A obra a descreve em
   detalhe como um dos três planos considerados, e diz explicitamente que o plano
   escolhido foi outro. A ficha registra isso: é uma formação **projetada e descrita, não
   construída**.
3. **Slaughtering Immortal Guillotine fica na seção da espada, com o caminho corrigido no
   corpo da ficha.** Criar uma seção de uma linha só para o caminho da lâmina espalharia
   o repertório de espada em duas seções para a leitora sem ganho nenhum; a ficha diz o
   caminho certo, e a nota de abertura da seção passa a avisar que espada e lâmina são
   caminhos distintos na obra.
4. **True Stability Branch Transformation entra como golpe separado**, e não como nota de
   rodapé do original: a obra o trata como golpe próprio, com criador próprio, processo de
   criação próprio (dedução por luz da sabedoria) e potência declaradamente menor.
5. **Benevolent Equality fica sem caminho.** A obra nunca o nomeia, e o Gu-núcleo
   (*benevolence*) é de uma herança de Venerável cujo caminho ela também não declara.
   Preferido o travessão à indução.
6. **Helpless Withering entra apesar de a obra dizer "move" e não "killer move".** O
   contexto é uma troca de golpes assassinos entre dois rank 8, a moça o dispara entre
   dois golpes nomeados, e o efeito é composto (pétalas que anulam ataques de longo
   alcance). A ficha registra a ressalva.
7. **Golden Heavenly Saint entra com quase tudo em branco.** A obra só informa que é a
   formação de batalha antiga **número um** da Era da Antiguidade Remota, acima das duas
   que ela descreve. Um nome com posição no ranking é informação de mundo útil, mesmo sem
   mecânica.
