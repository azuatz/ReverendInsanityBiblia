# Auditoria dos catálogos de Gu

Relatório da leva de fechamento dos catálogos de Gu (`10 - Apendices/03`, `04`, `05`, `06`).
Escrito incrementalmente durante o trabalho.

Escopo: deduplicação dos dois catálogos, varredura de Gu ausentes no texto-fonte,
reescrita das entradas vagas e conferência da nota-índice.

---

## Duplicatas fundidas

### Catálogo de mortais — dentro do próprio arquivo

Método: extração programática da primeira célula de toda linha de tabela e contagem de
frequência. Nove nomes apareciam duas vezes. Regra adotada para escolher a casa de cada
Gu: **quando a obra atribui um caminho, a ficha mora na seção daquele caminho**; as
seções que são famílias funcionais (cura e vida, Gu lendários, linhagem lunar) ficam com
os Gu que não têm caminho atribuído — com uma exceção justificada abaixo. Toda seção que
perdeu uma linha ganhou um **ponteiro em itálico** logo antes da tabela, dizendo onde a
ficha completa está.

| Gu | Estava em | Casa final | O que foi preservado da linha apagada |
|---|---|---|---|
| Therapy Light Gu | Caminho da luz + Cura e vida | **Caminho da luz** | o cardápio inventado (pétalas brancas e água de nascente `*`), somado ao ritmo canônico por rank |
| Vitality Leaf | Caminho da madeira + Cura e vida | **Caminho da madeira** | "barata e fácil de produzir porque a planta-mãe repõe as folhas; a cura mais difundida do mundo" |
| Wood Charm Gu | Caminho da madeira + Caminho da transformação | **Caminho da madeira** | a linha da transformação era um *stub* que se descrevia por referência ("ficha principal no caminho da madeira — ver acima"). Dela veio o único conteúdo real: refino reconhecidamente mais difícil que o dos outros rank 3 da época, e a rota de avanço por fusão com Lifespan Gu de cem anos (rank 4) e de mil (rank 5) |
| Blood Moon Gu | Caminho do sangue + Linhagem lunar | **Linhagem lunar** | "caso-modelo de troca de dieta por conveniência" e "janela mensal que um inimigo informado pode explorar". A exceção à regra geral está justificada abaixo |
| Moon Poison Gu | Caminho do veneno + Linhagem lunar | **Linhagem lunar** | "debilitação **progressiva**" e a mecânica de inalação enquanto o alvo continuar respirando |
| Blood Skull Gu | Caminho do sangue + Caminho do refinamento | **Caminho do sangue** | os números que faltavam: cerca de cem corpos quando são parentes próximos, **dez pontos percentuais de aptidão por carga**, e a história do exemplar (espólio selado, refinado na hora com uma injeção de essência; versão rank 5 criada séculos depois por um Venerável) |
| Guts Gu | Caminho da alma + Cura e vida | **Caminho da alma** | "o fortalecimento de alma número um do mundo, cerca de **dez vezes** os métodos comuns" e a dependência do Airsac Gu para sair do lugar |
| Hope Gu | Caminho do homem + Gu lendários | **Caminho do homem** | que a contagem de pontos de luz absorvidos **é** a medição de aptidão do rito dos quinze anos |
| Sneak Attack Gu | duas linhas seguidas, rank 2 e rank 5 | **as duas mantidas** | não era duplicata e sim duas potências reais. O erro era outro: a história de origem (refino de rank 1 fracassado, com cadáver de bebê anômalo, Sandpit, Chimney Smoke, Clear Water e sangue da ponta da língua) estava na linha do **rank 5**, quando pertence à do rank 2. Corrigido, e a linha do rank 5 passou a descrever a elevação |

**Por que a linhagem lunar é exceção.** A seção "Linhagem lunar" não é um caminho: é um
estudo de caso de uma árvore de fusões de um clã, e seu valor didático depende de as
linhas ficarem **lado a lado para comparação de colunas** (o texto da seção manda o
leitor comparar a coluna de alimentação do Golden Moon com a do Blood Moon). Tirar dois
ramos de lá para outras seções destruiria o argumento. Os dois Gu ganharam, na própria
célula de efeito, a frase que diz que pertencem também ao caminho do sangue e ao do
veneno, e essas duas seções ganharam ponteiro.

### Catálogo de imortais — dentro do próprio arquivo

Treze nomes duplicados. Nove deles eram o mesmo padrão: um Gu de **rank 9** aparecia na
seção do seu caminho **e** na seção "Os Gu de rank 9". Decisão: a seção "Os Gu de rank 9"
passa a ser a **casa única** de todo Gu daquele patamar, e as seções de caminho ficam com
ponteiro. O motivo é estrutural e está escrito na própria nota: no rank 9 as três
aptidões se dissolvem e as fichas usam uma coluna diferente das demais (✴️ Peculiaridade
em vez de refino/vantagem/desvantagem) — manter as duas cópias garantia divergência, e de
fato havia divergência em oito dos nove casos.

| Gu | Estava também em | O que a fusão preservou |
|---|---|---|
| Fate Gu | Caminho do céu | "impõe caminhos de vida fixos" e "foi usado apenas pela vontade do céu" |
| Wisdom Gu | Caminho da sabedoria | o uso **como material de refino** (reduz drasticamente o gasto de pensamentos e eleva muito o de essência) e que o portador mais famoso nunca chegou a refiná-lo |
| Heavenly Secret Gu | Caminho da sabedoria (7 → 9) **e** Caminho do céu (9) | as três eram o mesmo Gu. Rank corrigido para **7 → 8 → 9** (a obra registra as três potências e a elevação); dieta unificada (materiais imortais de céu; nuvens esplêndidas no rank 9); e a frase que explica por que 80% de falha ainda vale a pena |
| Derivation Gu | Caminho da regra | "deriva mundos novos" e "cria marcas de lei inteiramente novas" |
| Sovereign Immortal Fetus Gu | Caminho do homem | "corpo **compatível** com a alma já existente" |
| Fire Gu · Light Gu | Caminhos elementais e menores | a atribuição explícita de caminho (fogo e luz), que a seção de rank 9 não trazia |
| Heavenly Essence Treasure Imperial Lotus | Caminhos elementais e menores | quase tudo: a faixa **6 → 9**, a linhagem mortal que produz pedras primordiais, o consumo de nascentes na fase de fusão, e a condição de um dos Dez Grandes Gu Imortais |
| Kill | Caminhos elementais e menores | nada de novo; a fusão apenas eliminou a divergência de rank (8 contra 8 → 9) |

As outras quatro duplicatas não eram de rank 9:

| Gu | Estava em | Casa final | O que foi preservado |
|---|---|---|---|
| Regret Gu | Caminho do tempo + Caminho do refinamento | **Caminho do tempo** | as duas linhas descreviam **funções diferentes do mesmo Gu** e nenhuma das duas mencionava a outra: arma de arrependimento por contato, e refazer um Gu Imortal destruído a partir da insígnia do refino original. A ficha fundida traz as duas, e diz que a segunda é a única exceção conhecida à irreversibilidade |
| Blood Asset Gu | Caminho do sangue + Caminho do refinamento | **Caminho do sangue** | as duas eram redação diferente do mesmo conteúdo; ficou a mais explícita, com a ressalva de que ele não aumenta a chance de sucesso, só reduz a perda |
| Second Aperture Gu | Caminho do céu + Gu de utilidade e estrutura de abertura | **Gu de utilidade e estrutura de abertura** | os números da linha do céu (capacidade somada: 90% + 90% = 180%; dobro da recuperação; segundo conjunto completo de Gu) e a classificação no caminho do céu, que virou nota dentro da célula |
| Human Qi Gu | Caminho do homem + Caminho do qi | **Caminho do qi** | rank corrigido para **7 → 8** (a linha do qi dizia só 8) e a explicação de por que só serve a quem ainda não ascendeu |

### Entre os dois catálogos (mortal × imortal)

Vinte e nove nomes apareciam nos dois arquivos. **Vinte e um são versões mortal e imortal
de verdade** — o caso que a obra explicita com o par mortal/imortal do Pulling Water Gu, em
que o Gu Imortal continua precisando do mortal porque um Gu Imortal é único e não serve a
dois golpes ao mesmo tempo. Foram mantidos os dois lados: Accumulate Virtue, Blood
Handprint, Blood Skull, Bone Spike, Day, Expend Strength, Extreme Light, Grass Puppet,
Gruel Mud, Justice, Luck Inspection, Man As Before, Month, Slavery, Sneak Attack, Soul
Search, Star Shoot, Strength Qi, Territory, Wealth e Year Gu (mais o Pulling Water Gu, que
o catálogo mortal já trazia com a explicação completa do par).

A conferência descobriu um defeito silencioso nesse conjunto: **dezesseis dessas linhas não
diziam que a outra versão existe**. Quem lesse só o catálogo mortal do Day Gu não teria como
saber que há um Day Gu imortal, e vice-versa — o que, num catálogo de mesa, é o mesmo que a
informação não existir. Todas as dezenove pontas faltantes (dezesseis no mortal, três no
imortal) receberam a frase que declara a outra versão, com o rank dela e o wikilink para o
outro arquivo.

**Oito estavam no catálogo mortal indevidamente**, porque a obra só lhes dá rank imortal —
em vários casos a própria célula do catálogo mortal admitia isso ("o exemplar registrado é
de rank 6, portanto imortal"). Removidos do mortal, com ponteiro na seção de origem:

| Gu | Rank canônico | Onde estava | Como se resolveu |
|---|---|---|---|
| Derivation Gu | 9 | Gu lendários e conceituais | ficha só no imortal; ponteiro na seção lendária |
| Ability Gu | 8 | Gu lendários e conceituais | idem |
| Strong Gu | 7 | Gu lendários e conceituais | idem |
| Pride Gu | — (Gu Imortal) | Gu lendários e conceituais | a linha mortal era **muito mais rica** que a imortal; o conteúdo dela foi transplantado para a ficha imortal antes da remoção (ocupa área enorme na mente, recusa-se a sair, só o Humility o expulsa, e o expulso voa para outra mente) |
| Humility Gu | — (Gu Imortal) | Gu lendários e conceituais | idem (é o único meio de expulsar o Pride Gu, e expande a capacidade da abertura já desperta) |
| Master-Servant Gu | 7 | Caminho da escravização | ficha só no imortal; ponteiro |
| Formation Plate Gu | 6 | Caminho da formação | ficha só no imortal; ponteiro |
| Musician Gu | 6 | Caminho do homem | ficha só no imortal; e a seção do caminho do homem ganhou a divisão canônica da série das profissões (ver "Entradas reescritas") |

Dois ranks estavam vazios e foram preenchidos com o texto: **Justice Gu → rank 5** na
versão mortal (a própria célula dizia "o exemplar descrito é de rank 5") e **Expend
Strength Gu → rank 4** (o texto lista "rank four bitter strength, expend strength Gu and
charging crash Gu").

---

## Gu acrescentados

Método da varredura: extração de **todos** os n-gramas do texto-fonte que precedem a
palavra "Gu" (nos seis volumes, sempre com busca insensível a maiúsculas, porque a obra
grafa nomes de Gu em minúsculas), corte por lista de palavras vazias e por contexto à
direita (para descartar "Gu Master", "Gu worm", "Gu recipe"), contagem de frequência e
cruzamento com todo o texto dos catálogos já existentes. Sobraram 194 candidatos
plausíveis, verificados um a um no texto-fonte.

Resultado: **157 linhas novas** — 150 no catálogo mortal, 8 no imortal (o Dragon Scales
Gu entrou nos dois, por ter as duas versões). O catálogo mortal saiu de 447 para 589
linhas; o imortal, de 292 para 255 linhas de Gu mais 27 Casas (a queda do imortal é a
deduplicação, que sozinha removeu 45 linhas repetidas).

A tabela abaixo lista o que entrou, com o rank que a obra dá, a seção que recebeu a
linha e os capítulos de referência.

### No catálogo mortal

| Gu | Rank | Seção que recebeu | Capítulos |
|---|---|---|---|
| Water Strength Gu | — | Caminho da força | 560, 650, 782, 1561, 1774 |
| Wind Strength Gu | — | Caminho da força | 560, 650, 782, 1561, 1774 |
| Wolf Strength Gu | — | Caminho da força | 431, 442, 452 |
| Stone Turtle Strength Gu | — | Caminho da força | 297, 304, 317 |
| Sky Strength Gu | — | Caminho da força | 560 |
| Turtle Tire Gu | — | Caminho da força | 305, 306 |
| Violent Strength Gu | — | Caminho da força | 340 |
| Biao Strength Gu | 4 | Caminho da força | 342, 343, 345, 442 |
| Kunlun Bull Strength Gu | 4 | Caminho da força | 368, 442, 443 |
| Green Bull Labor Gu | 3 | Caminho da força | 297, 304, 317 |
| Exert Strength Gu | — | Caminho da força | 939, 940, 951, 961, 972 |
| Grand Chaotic Dance Gu | 5 | Caminho da força | 583, 584, 586 |
| Azure Wolf Skin Gu | 4 | Defesa e reforço corporal | 442, 444, 457, 459 |
| Fox Skin Gu | 5 | Defesa e reforço corporal | 409 |
| Five Element Bear Skin Gu | 5 | Defesa e reforço corporal | 583, 584, 586 |
| Ice Muscles Gu | 3 | Defesa e reforço corporal | 137, 209, 223, 225, 230, 233, 378 |
| Jade Bones Gu | — | Defesa e reforço corporal | 205, 214, 225, 228, 232, 233, 378 |
| Soft Bones Gu | 5 | Defesa e reforço corporal | 373, 380, 417, 581 |
| Iron Hand Gu | 3 | Defesa e reforço corporal | 298, 362 |
| Golden Lion Fur Gu | 5 | Defesa e reforço corporal | 712 |
| Water Shell Gu | 2 | Defesa e reforço corporal | 1654, 1655, 1656, 1894 |
| Dragon Scales Gu | — | Defesa e reforço corporal | 442, 1197, 1198, 1377 |
| Broadsword Light Gu | 3 | Caminho da luz | 265, 280, 288 |
| Light Fences Gu | 3 | Caminho da luz | 563 |
| Lightning Flash Gu | 5 | Caminho da luz | 563 |
| Revealing Light Gu | 4 | Caminho da luz | 856 |
| Burning Firefly Gu | 3-5 | Caminho da luz | 1780 |
| Water Cage Gu | — | Caminhos do gelo e da água | 167, 358 |
| Spiral Water Arrow Gu | 3 | Caminhos do gelo e da água | 427, 428, 429 |
| Spring Rain Gu | 3 | Caminhos do gelo e da água | 428 |
| Fog Sparrow Gu | 3 | Caminhos do gelo e da água | 428, 433 |
| Three Claw Water Dragon Gu | 3 | Caminhos do gelo e da água | 427, 428, 452, 1166 |
| Current Charge Gu | 5 | Caminhos do gelo e da água | 566 |
| Backwater Battle Gu | 5 | Caminhos do gelo e da água | 470, 473 |
| Dried Pond Gu | 4 | Caminhos do gelo e da água | 465 |
| Water Walking Gu | — | Caminhos do gelo e da água | 1247 |
| Clam Gu | — | Caminhos do gelo e da água | 473 |
| Frost Fish Gu | — | Caminhos do gelo e da água | 227 |
| Water Spider Gu | — | Caminhos do gelo e da água | 47 |
| Flying Snow Gu | 5 | Caminhos do gelo e da água | 539, 583 |
| Snowy Plain Gu | — | Caminhos do gelo e da água | 378 |
| Water Source Gu | — | Caminhos do gelo e da água | 2295 |
| Double Orifice Stove Gu | 2 | Caminho do fogo | 123, 853 |
| Firelight Gu | — | Caminho do fogo | 452 |
| Pill Fire Gu | — | Caminho do fogo | 461, 472, 532 |
| Kerosene Gu | 1 | Caminho do fogo | 152 |
| Pine Island Gu | — | Caminho da madeira e das plantas | 671, 672 |
| Grass Tree Army Gu | 4 | Caminho da madeira e das plantas | 296 |
| Rice Bag Grass Gu | — | Caminho da madeira e das plantas | 211, 212, 214, 231, 273, 278 |
| Afterlife Grass Gu | — | Caminho da madeira e das plantas | 176 |
| Wood Origin Gu | — | Caminho da madeira e das plantas | 2295 |
| Mushroom Gu | — | Caminho da madeira e das plantas | 439 |
| Blood Scar Gu | — | Caminho do sangue | 669 |
| Snake Poison Gu | — | Caminho do veneno | 2143 |
| Dove Poison Gu | — | Caminho do veneno | 2143 |
| Bee Poison Gu | — | Caminho do veneno | 2143, 2145 |
| Ghost Face Gu | 4 | Caminho da alma | 428, 429, 442, 446 |
| Vajra Stare Gu | 5 | Caminho da alma | 379, 504, 581 |
| Divine Soul Gu | 3 | Caminho da alma | 422, 442 |
| Dream Soul Gu | 3 | Caminho da alma | 422, 442 |
| Moon Soul Gu | 3 | Caminho da alma | 422, 442 |
| General Soul Gu | 3 | Caminho da alma | 422, 442 |
| Grudge Soul Gu | 3 | Caminho da alma | 422, 442 |
| Poem Soul Gu | 3 | Caminho da alma | 422, 442 |
| Nauseous Crying Baby Gu | 4 | Caminho da alma | 507, 508, 516 |
| Ghost Cry Gu | 3 | Caminho da alma | 428, 429, 442, 446 |
| Fish Enslavement Gu | 1-2-3 | Caminho da escravização | 557 |
| Five Hole Jade Flute Gu | 5 | Caminho da escravização | 656, 703 |
| Divine Sense Gu | 5 | Caminho da sabedoria | 462, 465, 466, 537, 570, 581, 650, 665, 666, 667, 682, 712, 1027, 1028, 2295 |
| Sharp Intent Gu | — | Caminho da sabedoria | 580, 652 |
| Hostile Intent Gu | — | Caminho da sabedoria | 580 |
| Contact Heart Gu | 1-5 | Caminho da sabedoria | 1589, 1590, 1591, 1770 |
| Awaken Cloud Gu | 4 | Caminho da sabedoria | 486 |
| Mind Reading Gu | — | Caminho da sabedoria | 427, 436 |
| Battle Space Gu | 5 | Caminhos do espaço e do movimento | 584, 585, 586 |
| Swift Shadow Gu | — | Caminhos do espaço e do movimento | 298, 360, 362 |
| Wolf Sprint Gu | 4 | Caminhos do espaço e do movimento | 436, 444, 459, 504 |
| Flying Cloud Gu | 4 | Caminhos do espaço e do movimento | 429, 441 |
| Swift Ghost Cloud Gu | — | Caminhos do espaço e do movimento | 488 |
| Location Swap Gu | 4 | Caminhos do espaço e do movimento | 471, 548 |
| Scarlet Pill Cricket Gu | — | Caminhos do espaço e do movimento | 82, 93 |
| Messenger Dove Gu | 5 | Caminho da informação e da investigação | 653, 2023 |
| Butterfly Letter Gu | 5 | Caminho da informação e da investigação | 528, 2023 |
| Star Letter Gu | 4 | Caminho da informação e da investigação | 556 |
| Snake Communication Gu | — | Caminho da informação e da investigação | 127, 133 |
| Beast Language Gu | — | Caminho da informação e da investigação | 127, 2023 |
| Shadow Image Gu | — | Caminho da informação e da investigação | 838, 2020 |
| Starshine Fake Eye Gu | — | Caminho da informação e da investigação | 718, 719 |
| Return Heart Gu | — | Caminho da informação e da investigação | 427, 428, 433 |
| Life Tablet Gu | — | Caminho da informação e da investigação | 1214, 1220, 1229, 1338, 2035 |
| Water Text Gu | — | Caminho da informação e da investigação | 1595, 1596, 2023 |
| Pitch Black Gu | 5 | Furtividade e disfarce | 373, 380, 417, 504, 581, 642 |
| Zither Gu | 1-5 | Caminhos do som e do raio | 703, 1667, 1668, 1971 |
| Lightning Current Gu | — | Caminhos do som e do raio | 132, 149 |
| Earth Mound Gu | 2 | Caminho da terra | 501 |
| Unprocessed Jade Gu | — | Caminho da terra | 2295 |
| Small Swamp Gu | — | Caminho da terra | 671, 672 |
| Mountain Giant Puppet Gu | — | Caminho da terra | 185, 186, 202, 302 |
| Earth Bacteria King Gu | — | Caminho da terra | 505 |
| Turn Phantom Gu | — | Caminho da transformação | 586 |
| Turn Gold Gu | 5 | Caminho da transformação | 373, 374, 379, 417, 504, 581 |
| Raise Eyebrows & Exhale Gu | — | Caminho da transformação | 192, 193, 194, 196 |
| Indissoluble Relation Gu | 3 | Caminho do refinamento e do avanço de cultivo | 230 |
| Star Arrow Gu | 2 | Caminho das estrelas | 276, 361, 717 |
| Four Stars Cube Gu | 4 | Caminho das estrelas | 550, 711 |
| Stellar Fire Gu | — | Caminho das estrelas | 378, 666, 851, 1291, 1343 |
| Falling Meteor Gu | — | Caminho das estrelas | 666, 851, 1291, 1343 |
| Wolf Swallow Gu | 4 | Armazenamento e logística | 459, 464, 465, 504 |
| Flesh Laughter Gu | — | Armazenamento e logística | 224, 225 |
| Tortoise Breath Gu | 4 | Armazenamento e logística | 431 |
| Gold Cup Gu | 3 | Armazenamento e logística | 422 |
| Silver Cup Gu | 3 | Armazenamento e logística | 422, 425 |
| Fish Bubble Gu | — | Armazenamento e logística | 211, 629 |
| White Cloud Cushion Gu | 5 | Armazenamento e logística | 698, 699 |
| Connecting Heaven Gu | 5 | Armazenamento e logística | 420, 462, 463, 465, 466, 467, 468, 469, 475, 476, 485, 486, 487, 491, 492, 581, 616, 642, 649, 650, 656, 666, 667, 706, 712, 723, 739, 952, 1027, 1028, 1030, 1032, 1033, 1114, 1324, 1554, 2300 |
| Meat Bone Gu | — | Cura e vida | 228 |
| Pig Iron Gu | — | Cura e vida | 176, 180, 431 |
| Faith Gu | — | Gu lendários e conceituais | 144, 410, 411, 435, 845, 1175 |
| Courage Gu | — | Gu lendários e conceituais | 123, 348, 410, 411, 435, 722, 845, 1175, 2041, 2052, 2053 |
| Fairness Gu | — | Gu lendários e conceituais | 410, 411, 646, 944, 2192 |
| Vanity Gu | — | Gu lendários e conceituais | 357, 1774 |
| Betrayal Gu | — | Gu lendários e conceituais | 1175, 2052, 2184 |
| Regulation Gu | — | Gu lendários e conceituais | 58, 59, 87, 131, 2041, 2052, 2053, 2294 |
| Worry Gu | — | Gu lendários e conceituais | 1473, 1474 |
| Difficulty Gu | — | Gu lendários e conceituais | 1473, 1474 |
| Sadness Gu | — | Gu lendários e conceituais | 1473, 1474 |
| Disappointment Gu | — | Gu lendários e conceituais | 939, 940, 972 |
| Familial Emotion Gu | — | Gu lendários e conceituais | 2189, 2203, 2210, 2294 |
| Benevolence Gu | — | Gu lendários e conceituais | 1693, 1748, 1789, 1915, 1918, 1946, 2047 |
| Moonscar Gu | 3 | Linhagem lunar | 156 |
| Wind Barrier Gu | 5 | Caminho do vento | 472 |
| Clear Wind Wheel Gu | 1 | Caminho do vento | 2072 |
| Eating Wind Gu | 2 | Caminho do vento | 308 |
| Wind Flower Gu | — | Caminho do vento | 629, 631, 633, 634, 636, 639, 640, 650 |
| Wind Tiger Cloud Dragon Gu | 5 | Caminho do vento | 582, 584 |
| Treacherous Cloud Wave Gu | 5 | Caminho do vento | 531, 534, 538 |
| Golden Dragon Gu | 4 | Caminho do metal | 373, 379, 380, 426, 430, 434, 581, 1155, 1166 |
| Hand Blade Gu | 3 | Caminho do metal | 298, 302, 360, 362 |
| Golden Silkworm Gu | 3 | Caminho do metal | 243 |
| Blade Qi Gu | — | Caminho do metal | 361, 362 |
| Iron Fist Grappling Gu | — | Caminho do metal | 185, 202 |
| Sword Sheath Gu | 5 | Caminho do metal | 1059 |
| Small Family Qi Gu | 5 | Outros caminhos com poucos Gu | 683, 684, 685, 689, 690, 692, 693, 732, 735, 863, 1644 |
| Multiple Pregnancy Gu | 1-5 | Outros caminhos com poucos Gu | 2298, 2300 |
| Safe Pregnancy Gu | — | Outros caminhos com poucos Gu | 2298, 2300 |
| Abortion Gu | — | Outros caminhos com poucos Gu | 2298, 2300 |
| Dead Fetus Gu | — | Outros caminhos com poucos Gu | 2298, 2300 |
| Dream Pillow Gu | 5 | Outros caminhos com poucos Gu | 1619 |
| Big Smoke Tea Gu | — | Outros caminhos com poucos Gu | 1093 |
| Exploding Egg Gu | 1 | Outros caminhos com poucos Gu | 323, 324, 346, 376 |

### No catálogo imortal

| Gu | Rank | Seção que recebeu | Capítulos |
|---|---|---|---|
| ⭐ Wooden Chicken Gu | — | Caminhos elementais e menores | 543, 587, 588, 590, 593, 594, 630, 638 |
| ⭐ Eight-faced Prestige Wind Gu | 8 | Caminhos elementais e menores | 1218, 2079, 2151 |
| ⭐ Earth Net Gu | 7 | Caminhos elementais e menores | 602 |
| ⭐ Earth Prison Gu | 7 | Caminhos elementais e menores | 602 |
| ⭐ Doting Mother Gu | — | Caminho do homem | 1156, 2111 |
| ⭐ Traveling Son Gu | — | Caminho do homem | 1156, 2111 |
| ⭐ Star Desolate Hound Strength Gu | 6 | Caminho da força | 714  , 752 |
| ⭐ Dragon Scales Gu | — | Caminho da transformação | 442, 1197, 1198, 1377 |

---

## Falsos positivos descartados

A varredura por n-grama pega tudo que precede a palavra "Gu", e boa parte disso não é
nome de Gu. Cada candidato foi conferido no texto antes de ser descartado; nenhum caiu
por suspeita. Os motivos se repetem em cinco padrões, e vale conhecê-los porque
qualquer varredura futura vai reencontrá-los:

1. **Categoria funcional, não nome** — "defensive Gu", "movement Gu", "consumable Gu",
   "recon Gu", "storage Gu", "attack type Gu". A obra classifica Gu por função o tempo
   todo, e essas expressões parecem nomes.
2. **Verbo + nome de outro Gu** — "destroy Fate Gu", "use Wisdom Gu", "refine Attitude
   Gu". Foi o padrão mais numeroso.
3. **Adjetivo + nome de outro Gu** — "wild year Gu" e "wild wisdom Gu" são o Year Gu e
   o Wisdom Gu; "wild" só diz que o exemplar nasceu na natureza. "Incomplete ghost fire
   Gu" é o Ghost Fire Gu num estado de refino.
4. **Nome de pessoa, clã, tribo ou região** coladas à palavra Gu — "Fang clan's Gu",
   "Hei tribe's Gu", "Ha Tu Gu", "Nu Er Gu", "Wan Gu Chou".
5. **Nome truncado** — o n-grama cortou o começo do nome verdadeiro. Estes **não** são
   descartes: são correções, e entraram no catálogo com o nome canônico completo.

| Candidato | Veredito |
|---|---|
| `nu er` | — |
| `wan` | — |
| `level year` | — |
| `level day` | — |
| `recon Gu` | — |
| `mystical Gu` | — |
| `great flying zombie` | — |
| `human shaped life` | — |
| `wild lightning` | — |
| `wild light` | — |
| `ideal healing` | — |
| `great movement Gu` | — |
| `incomplete ghost fire Gu` | — |
| `wild year Gu` | — |
| `wild wisdom Gu` | — |
| `purple digital shade` | — |
| `lifebound Gu` | — |

### Nomes truncados, corrigidos em vez de descartados

| Como saiu da varredura | Nome canônico na obra |
|---|---|
| `exhale` | **Raise Eyebrows & Exhale Gu** |
| `faced prestige wind` | **Eight-faced Prestige Wind Gu** (e o Seven-faced, irmão de rank 7) |
| `breath concealing` | **Breath Concealment Gu** (a obra alterna as duas grafias) |
| `element bear skin` | **Five Element Bear Skin Gu** |
| `hole jade flute` | **Five Hole Jade Flute Gu** |
| `orifices fire hut` / `orifices fire tower` | **Three Orifices Fire Hut Gu** / **Four Orifices Fire Tower Gu** |
| `stars cube` | **Four Stars Cube Gu** |
| `beast placenta` | **Beast Strength Placenta Gu** |
| `claw water dragon` | **Three Claw Water Dragon Gu** |
| `rice bag` | **Rice Bag Grass Gu** |
| `big lizard house` | **Large Lizard House Gu** (a obra usa as duas formas) |
| `earth communication flesh ear` | **Earth Communication Ear Grass** (grafia dominante) |
| `life retaining jade burial` | **Life-preserving Jade Burial Gu** (já catalogado) |
| `level year` / `level day` | recorte de "mortal/immortal **level** year Gu"; os Gu são o **Year Gu** e o **Day Gu** |

