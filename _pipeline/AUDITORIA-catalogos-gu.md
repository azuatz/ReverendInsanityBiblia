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

#### Segunda leva — a reciprocidade estava só num sentido

A leva anterior registrou que as pontas faltantes tinham sido corrigidas. A conferência
programática desta leva mostrou que **a correção pegou quase só o lado mortal**: dos 22
pares, o catálogo mortal declarava a contraparte em 15 linhas e o imortal em 6. Quem
lesse a ficha imortal do Day Gu, do Slavery Gu ou do Justice Gu não tinha como saber que
existe uma versão mortal, nem chegar até ela.

Duas coisas foram distinguidas aqui, e a distinção importa: várias fichas imortais
**mencionavam** a versão mortal em prosa ("na versão mortal de rank 5, que a obra
detalha…") mas **nenhuma delas linkava**. Menção em prosa não resolve o problema de mesa
— a designer precisa do salto. Todas as 16 pontas faltantes ganharam a frase com o rank
da outra versão e o wikilink para o outro catálogo. Hoje os 22 pares são recíprocos, e
isso é verificável por script.

**Um erro de rank foi encontrado no processo, e é o achado mais sério desta leva.** O
Wealth Gu tinha, nos dois catálogos, **a mesma célula copiada** — e no catálogo de
imortais ela vinha etiquetada como **rank 5**, que é o rank da versão *mortal*. Um Gu de
rank 5 listado no catálogo dos Gu únicos do mundo é exatamente o tipo de erro que
contamina tudo que se construir em cima. As duas linhas foram separadas de verdade:

- **no catálogo imortal**, rank corrigido para `—` (a obra não dá rank ao exemplar
  lendário; diz apenas que é Gu Imortal), e a ficha passou a tratar só do Wealth Gu do
  mito fundador — a receita de Ren Zu, o efeito de virar qualquer coisa menos ser vivo,
  e a razão pela qual isso o torna o Gu que dispensa a coleta de materiais;
- **no catálogo mortal**, rank 5, e a ficha passou a tratar só do consumível de uso
  único que vira qualquer material de rank 5 — com os dois usos concretos (dinheiro
  líquido no patamar mortal e substituto do exemplar imortal dentro de receitas de Gu
  Imortal), a história do refino por sacrifício humano e a política de venda limitada a
  uma dúzia de exemplares por comprador.

#### Duas duplicatas que o casamento por nome exato não pegava

A conferência anterior comparou **nomes exatos**, e por isso deixou passar dois casos em
que o mesmo Gu aparecia com grafias diferentes:

- **Dragon Scale (rank 7) e Dragon Scales Gu** eram a **mesma ficha, duas vezes, dentro do
  catálogo imortal** — singular contra plural, com e sem o sufixo "Gu". As duas foram
  fundidas numa linha só: ficou o rank 7 e a dieta ("escamas de feras dracônicas `*`") que
  só a linha curta tinha, mais a frase que só ela trazia — que este é **uma das quatro
  peças**, com chifre, garra e olho de dragão, que compõem os golpes de transformação em
  dragão —, tudo somado ao mecanismo detalhado que só a linha longa trazia.
- **Pulling Water**, **Star Thought** e **Vajra Thought** estavam no catálogo imortal sem o
  sufixo "Gu" e, por isso, **não eram reconhecidos como pares** dos Gu de mesmo nome no
  catálogo mortal — apesar de o Pulling Water Gu ser justamente o par mortal/imortal que a
  obra explica em detalhe, e que serve de caso-modelo para a regra inteira. Os três nomes
  foram normalizados e os três pares fecharam.

Ao fim, os pares mortal × imortal passaram de 22 para **28** e todos são recíprocos, com
rank e link nos dois sentidos — verificável por script, comparando nomes **normalizados**
(sem o sufixo, sem a estrela, sem maiúsculas), que é a comparação que devia ter sido feita
desde o início.

#### Seis duplicatas que só a comparação agressiva de nomes encontrou

Depois das inserções desta leva, a conferência foi refeita com uma normalização mais
dura — minúsculas, sufixo "Gu" removido e **toda pontuação e espaço descartados** — e
apareceram seis pares que nenhuma comparação anterior pegaria, porque a obra grafa o
mesmo Gu de mais de uma maneira:

| Ficou | Era também |
|---|---|
| Jade Bone Gu | Jade Bones Gu |
| Giant Mountain Puppet Gu | Mountain Giant Puppet Gu (as palavras trocadas de lugar) |
| Moon Scar Gu | Moonscar Gu (com e sem espaço) |
| Breath Concealment Gu | Breath Concealing Gu |
| Ironfist Grappling Gu | Iron Fist Grappling Gu |
| Iceblade Gu | Ice Blade Gu |

Em todos os seis a fusão **preservou o conteúdo das duas linhas**: a célula que ficou
recebeu, entre parênteses e em itálico, a grafia alternativa e o que a obra registrava só
sob aquele nome. Isso importa para além da higiene do arquivo: quem procurar "Ice Blade"
no catálogo precisa cair na mesma ficha de quem procurar "Iceblade", senão o catálogo
mente por omissão.

A lição para a próxima varredura está no método, e é curta: **comparar nomes exatos não
basta, e comparar sem maiúsculas também não.** É preciso descartar pontuação, espaços,
o sufixo "Gu" e considerar troca de ordem entre as palavras — foi assim que apareceram
seis duplicatas depois de duas auditorias que se declararam concluídas.

Um sétimo caso não era duplicata e sim uma **célula na coluna errada**: a ficha do *Edge
Gu* trazia um parágrafo inteiro dentro da coluna de rank, explicando que o Gu existe em
versões mortais sem rank declarado e numa versão imortal de rank 7. A explicação foi para
a célula de efeito, o rank mortal virou `—`, e a versão imortal ganhou **ficha própria no
catálogo imortal** — onde, a propósito, já havia um *Edge Gu* de rank 7 descrito só como
"um dos núcleos do golpe de corte temporal", que foi fundido na ficha nova. A dieta que
essa ficha antiga trazia ("limalha de gumes gastos") era invenção nossa marcada com `*`,
e foi substituída pelo dado canônico: **extrato de aço branco**, material imortal de rank
7 do qual um bloco inteiro de aço branco rende uma tigelinha.

#### Um defeito de sintaxe que atingia os dois catálogos

Os wikilinks dentro de célula de tabela precisam do pipe escapado. Os dois catálogos
usavam `\\\|` (três barras) onde o resto do vault inteiro usa `\|` (uma) — 53 ocorrências,
e **só nestes dois arquivos**. Três barras fazem o Obsidian renderizar uma barra invisível
sobrando dentro do texto do link. Todas as 53 foram normalizadas para a convenção do vault.
A conferência estrutural das tabelas (contagem de colunas por linha, respeitando o escape)
passou a devolver zero linhas fora do padrão nos dois arquivos, e o auditor de links do
projeto devolve zero links quebrados.

O mesmo teste, aplicado às outras duas notas desta pasta, encontrou o defeito **oposto**
e mais grave: nove linhas de tabela — duas na nota-índice `03` e sete no catálogo de
receitas `06` — traziam wikilinks com o pipe **sem escape nenhum**. Num arquivo comum
isso é inofensivo; dentro de uma célula de tabela, o pipe **parte a célula em duas** e a
linha inteira sai desalinhada na renderização. Todas as nove foram escapadas. Hoje as
quatro notas passam no mesmo teste: zero linhas com número de colunas divergente do
cabeçalho da sua tabela.

Outras três linhas tinham célula idêntica nos dois arquivos (Dragon Scales, Expend
Strength e Territory Gu). Nesses casos a duplicação **não** era erro: cada célula rotula
explicitamente qual trecho é da versão mortal e qual é da imortal, e o conteúdo é
verdadeiro dos dois lados. Foram mantidas como estavam, ganhando apenas o wikilink
recíproco — apagar metade de cada uma deixaria a designer sem o contraste, que é
justamente o que a comparação mortal × imortal ensina.

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

### Segunda leva — a colheita dos relatórios de profundidade e da varredura

As subseções abaixo cobrem **os dois catálogos**, e não apenas o imortal. A fonte foi
dupla: os cinco relatórios `_pipeline/PROFUNDIDADE-paths-*.md`, cada um com uma seção
listando Gu que talvez faltassem, e uma varredura de frequência refeita do zero sobre os
seis volumes. Ao todo entraram **cerca de cem linhas novas** e o catálogo mortal foi de
589 para 649 Gu; o imortal, de 255 para 273 Gu mais 45 Casas.

#### Segunda leva — o caminho da sorte

Os cinco relatórios `_pipeline/PROFUNDIDADE-paths-*.md` chegaram depois da primeira leva,
cada um com uma seção listando Gu que talvez faltassem. A colheita do caminho da sorte
rendeu **sete Gu Imortais novos**, todos verificados no texto:

| Gu | Rank | O que a obra dá |
|---|---|---|
| Conceal Luck Gu | 6 | esconde a própria sorte; defende contra inspeção de rank 6; besouro de casca branca de meia palma |
| Good Luck Gu | — | armazena a boa sorte **sem dono** que o céu e a terra dissipam — cata o residual, não rouba de ninguém |
| Peach Blossom Luck Gu | — | sorte **amorosa**. Da obra vem só o nome e o preço alto; o efeito é dedução a partir da descrição canônica e detalhada da *sorte* de flor de pessegueiro, e está marcado como dedução na célula |
| Leave Luck Gu | — | gasta depressa a sorte de alguém. A obra dá uma frase e nada mais, e a célula diz isso |
| Seal Luck Gu | — | sela a sorte. Idem: uma frase |
| Transfer Luck Gu | — | transfere sorte. Idem — e a célula explica a diferença para o Connect Luck Gu, que **liga** duas sortes em mão dupla em vez de mover de A para B |
| Luck Deduction Gu | — | híbrido de sorte e sabedoria: **consome a própria sorte** para deduzir perigos e oportunidades futuros. Adivinhação paga em sorte |

Os quatro últimos vieram do mesmo leilão, e a obra dá dali um detalhe de mercado que vale
mais que o efeito: os vendedores exigiam pagamento em Gu Imortal de **caminho
convencional** (metal, madeira, água, fogo, terra), o que barrou da disputa quem era
especialista em caminho exótico — sem uma peça mainstream na mão, o imortal não podia nem
dar lance.

**Um erro de efeito foi corrigido, e era grave.** O **Fortune Rivalling Heaven** — o Gu de
rank 8 do topo da herança da "sorte de todos os seres vivos" — tinha ficha genérica. O
texto descreve o efeito com todas as letras, pela boca de uma autoridade máxima do Tribunal
Celeste: ele **absorve continuamente a sorte de todas as formas de vida ao redor** e a
concentra numa pessoa só. A ficha reescrita traz também o que faltava e que muda a mesa:
tem poder de quase rank 9; quem age contra o portador vê a **própria sorte piorar** (é o
teste canônico para descobrir quem o carrega sem conseguir enxergá-lo); um Gu de inspeção
mortal não o detecta; ele enfraquece calamidades e tribulações; grava marcas do Dao **no
próprio corpo** do portador, o que o torna praticamente inseparável dele; e o efeito
**se dissipa por completo quando o portador morre**.

**Três Casas de Gu Imortais ganharam mecanismo no lugar do rótulo**: Cooking Luck Pot,
Calamity Luck Altar e Luck Suppression Heavenly Palace — as três estavam descritas numa
linha cada. Do Cooking Luck Pot saiu, de quebra, uma **regra do mundo** que não estava em
lugar nenhum do vault: *o rank de uma Casa é ditado pelos seus Gu-núcleo*, não pelo Gu mais
forte que ela contém — a Casa nasceu rank 6 porque o núcleo era rank 6, mesmo abrigando Gu
de rank 7, e subiu a rank 8 quando o núcleo subiu.

Um alvo foi **reclassificado**: o "Luck Jade" não existe. A grafia canônica é *lucky jade*,
e a obra o descreve como **material imortal de rank 8**, não como Gu — por isso não entrou
em catálogo de Gu nenhum.

#### Segunda leva — as Casas do caminho do tempo e o caminho das estrelas

A esquadra de Casas de Gu Imortal que navega o Rio do Tempo estava representada por
**três linhas de uma frase** e faltavam quatro membros. A colheita fechou a esquadra
inteira, com rank confirmado para cada uma:

| Casa | Rank | O que ela é |
|---|---|---|
| Golden Age Platform | 7 | a única **fixa**: não navega. Construída dentro de uma terra abençoada, vira uma lua que nasce e se põe no céu dela |
| Present and Past Pavilion | 7 | vigilância: examina passado e presente |
| Eternal Yacht | 7 | velocidade e transporte; a mais rápida, e de defesa fraca |
| Three Autumn Yellow Crane Platform | 7 | patrulha e apoio de linha |
| Shark Flow Lever | 7 | tração animal — sete tubarões desolados puxando uma alavanca gigante. É o **único** estilo de construção assim na obra: combina feras desoladas com Gu Imortais na mesma estrutura |
| Moment Stage | 8 | a casa **pesada**, feita para segurar a linha de frente |
| Myriad Year Flying Warship | 8 | a completa: rápida, resistente e armada |

Vale registrar a ressalva metodológica, porque ela vale para toda pesquisa futura de
Casas: **a obra nunca dá ficha técnica dessas construções**, com a única exceção da
Golden Age Platform. O que existe é uma enumeração em série, num capítulo, como projeto
da corte celestial — e depois cenas de batalha esparsas, de onde saíram aparência,
Gu-núcleo, um ou outro golpe e comparações relativas de velocidade e defesa. Um único
parágrafo de saque revela os **Gu Imortais-núcleo** de quase todas, e é o achado mais
útil do conjunto: Permanence no Eternal Yacht; Instant e That Time no Moment Stage;
Early, Mid e Late Autumn no Yellow Crane; Years Flow Like Water, Precaution e Fight no
Myriad Year Flying Warship. **A obra nunca informa a capacidade em número de imortais**
de nenhuma delas.

No **caminho das estrelas** entraram quatro Gu mortais, e dois deles são o exemplo mais
limpo do que a política de preenchimento deste projeto significa na prática:

- **Star Shield Gu** e **Bane Star Gu** existem — e a obra dá **só o nome**, numa única
  linha, como ingredientes de um golpe mortal comum. Sem rank, efeito, dieta ou refino.
  As duas linhas dizem exatamente isso, com `—` nas colunas, em vez de inventar. A cena
  de onde saem é ela própria informativa: é um golpe anunciado numa vitrine, e o anúncio
  omite tudo — que é como um comprador do mundo enxerga a maior parte do mercado.
- **Brilliance of Two Stars Gu** (rank 2) e **Three Stars in the Sky Gu** (rank 3) fecham
  os degraus que faltavam da escada de amplificação estelar, cujos extremos já estavam
  catalogados. A obra descreve a série **sempre em bloco**, nunca degrau a degrau, então
  a gradação por rank ficou marcada como dedução. A função canônica é amplificar
  — a obra especifica: **ofensivamente** — Gu do caminho das estrelas, com taxa de
  sucesso de refino muito maior que a do amplificador genérico e materiais
  extremamente comuns, a ponto de a obra afirmar que, se circulassem livremente,
  mudariam a posição relativa de todos os caminhos do mundo.

Entraram ainda dois Gu Imortais de fora desses caminhos: o **Cook Gu** (rank 7, comida),
que está **travado no rank 7** porque não existe material imortal de rank 8 do caminho da
comida — e a obra usa esse travamento para enunciar uma regra do mundo, o ciclo entre a
prosperidade de um caminho e a existência de materiais dele; e o **Heaven Qi Gu**
(rank 8, qi), um dos três "Gu dos três qi" e núcleo insubstituível do golpe de retração
tripla de qi, que é o Gu que a obra liga explicitamente ao caminho do céu.

Cinco alvos foram **reclassificados como material ou espécie, e não entraram em catálogo
de Gu**: Star Night Mucus (material imortal rank 6), Black Oil (material imortal de
comida, que grava marcas do Dao em quem toca e digere lentamente o coletor), Qi Harvest
Fruit (consumível — e a grafia do enunciado estava invertida: a obra escreve *qi harvest
fruit*), Truthful Floating Ice (material do caminho do céu: cada bloco é *uma verdade*
boiando no Rio do Tempo) e o **Dragonfish**, que é o falso positivo mais instrutivo da
leva — não é Gu, é uma **espécie artificial criada pelo criador do caminho da comida**
para servir de comida universal de Gu, e é a fera desolada mais fraca do mundo.

#### Segunda leva — o caminho da regra

O caminho da regra tinha dezesseis fichas, e faltavam sete Gu que a obra nomeia. Todos
entraram, e o resultado dividiu-se limpo em dois grupos que vale distinguir, porque é a
distinção que a designer precisa fazer:

**Com mecanismo de verdade** — *Region* + *Limit* (o par de núcleos do golpe supremo do
caminho, com os custos opostos explicitados: a formação fixa exige veia de terra e meio
ano de montagem; a versão portátil de qi de luz gasta uma quantidade colossal de qi da
terra por uso, e o praticante começa conseguindo emitir só uma cor por vez), *No* +
*Care* (o par de rank 7 que anula o contragolpe de quebrar um pacto: acionados ao mesmo
tempo — luz negra vazia e luz vermelha quente —, fundidos por um terceiro numa formação,
gerando um pilar espiralado que cobre o corpo sem fresta, e protegendo só enquanto os
dois estiverem ativos) e *Disintegrate*.

**Só o nome e o contexto**, e as células dizem isso com todas as letras — *Departure*
(rank 8, uma ocorrência, componente de um golpe composto), *Main* (uma ocorrência; o que
a obra descreve é a regra de sorte principal contra sorte subordinada que o golpe
explora) e *Ripe* (uma ocorrência, com a grafia exata "rule path ripe Immortal Gu";
"ripen" e "ripening" dão zero — núcleo de super formação que acelera a proficiência em
golpes imortais já treinados).

**Duas fichas antigas foram substituídas por mecanismo.** A linha *Cause / Effect*
descrevia os dois como "núcleo estrutural" e dizia que a obra não descrevia o mecanismo —
mas descreve, e em detalhe. Foi **desdobrada em duas fichas**, com o golpe de karma
inteiro: uma árvore de fumaça verde que usa **destino como solo e sorte como água**, e
que dá frutos de bom e de mau efeito; o fruto de mau efeito assume a forma do alvo e o
subjuga sem retaliação possível; e a contabilidade de custo é explícita — golpe fraco
custa zero frutos, golpe forte custa um, um Gu Imortal de rank 7 custa um, e quando os
frutos acabam a árvore se desfaz. O *Permanence Gu*, que só dizia "serve de núcleo de
Casas de tempo", ganhou a ficha própria.

> [!warning] Uma divergência interna da obra ficou registrada na ficha
> Um capítulo chama Cause e Effect de "os dois Gu Imortais do caminho da regra"; dois
> capítulos posteriores dizem "Gu de regra *Cause* e Gu do **caminho da madeira**
> *Effect*". A obra se contradiz, e a ficha diz isso em vez de escolher em silêncio.

Da mesma leva saíram duas coisas que valem mais que qualquer linha isolada. A primeira é
uma **regra do mundo** que não estava em lugar nenhum do vault: contra-atacar o caminho
da regra com o próprio caminho da regra é o método mais eficaz, e nesse duelo **o rank
decide** — um *Small* de rank 7 anula um *Disintegrate* de rank 6. A segunda é a ficha
de alimentação mais completa que apareceu em qualquer caminho: o *Addition Gu*, casulo
negro como ferro, come **água de fio de pérola**, um material de rank 8 do *caminho da
água* — o que obriga seu dono, um imortal de regra, a construir um ponto de recurso de
água dentro da própria abertura. Fica submerso oito dias comendo, e a refeição seguinte
é oitenta anos depois. É o retrato do que "alimentar um Gu Imortal" significa como
projeto de infraestrutura, e não como despesa.

Entrou também no catálogo mortal o **Primeval Break Gu**, que corta a ligação entre a
energia primeva do ar e um Gu selvagem — com um ajuste de classificação: a obra o coloca
no **caminho da restrição**, um sub-ramo do caminho da regra que ainda não se separou
dele.

#### Segunda leva — força, alma, profissões e armas

Dezenove Gu novos, dos quais vale destacar o que muda contas de mesa:

- A **escala de "jun"** do caminho da força foi reconstruída inteira, e é a melhor régua
  numérica de força do catálogo: um jin (rank 1, +1 jin, 220 pedras) → dez jin (rank 2,
  690) → um jun, que são 30 jin (rank 3, 4.550) → dez jun, 300 jin (rank 4, 36.000) →
  cem jun, 3.000 jin (rank 5) → **Strength of a Thousand Jun**, Gu Imortal de rank 6,
  30.000 jin. Todos são descartáveis e **empilháveis sem limite de espécie**.
- O **Black and White Boar Gu** é, na verdade, **dois Gu irmãos** que empilham — branco
  mais preto dão a força de dois javalis. O ganho é **permanente**, sobrevive à morte do
  Gu e **é transferível a outra pessoa**; e a dieta é brutal: um porco adulto inteiro a
  cada cinco dias. Rank 1 declarado, e "rank 1 raro", a 600 pedras.
- O **Edge Gu** é o Gu-raiz comum ao caminho da lâmina **e** ao da espada, consta da
  lenda do Ancestral da Humanidade e é **gerado espontaneamente** por terreno saturado de
  marcas do Dao. A versão imortal, rank 7, come extrato de aço branco.
- A **série das profissões** ganhou fichas próprias para Doctor, Constable, Commander,
  Farmer, Dancer e Talented Girl. O Constable é o único da série com **infraestrutura
  própria**: os Police Gate Gu, de rank 1 a 6, ficam mutuamente conectados e
  teletransportam os beleguins criados de um portão a outro.

Três correções de nomenclatura, todas verificadas com busca direta:

| O que se procurava | O que a obra tem |
|---|---|
| "Impregnate Gu" | **não existe**; o nome canônico é **Become Pregnant Gu** |
| "Dancer Gu" | `grep -i "dancer gu"` devolve **zero**. O Gu existe na lista dos Gu de rank 6 do caminho do homem, mas a única cena parecida — três dançarinas que enfraquecem inimigos com mangas longas — **não nomeia o Gu**, e a ficha marca essa ligação como leitura nossa `*` |
| "Reincarnation Gu" | existe, com **uma única ocorrência**, numa lista. Não confundir com o "Reincarnation Battlefield", que é golpe de campo de batalha de outro Venerável e responde por todas as outras ocorrências da palavra |

Confirmou-se de passagem que o **Sky Strength Gu está extinto** — é o único da série
elemental de força nessa condição.

**Quatro linhas duplicadas nasceram desta leva e foram fundidas na hora** (Golden Aurora,
Become Pregnant, Reincarnation e Heaven Qi): a pesquisa devolveu ficha rica para Gu que
já tinham linha curta em outra seção. Em cada caso ficou a ficha rica, absorvendo o que
só a linha antiga tinha — o refino do Golden Aurora ("correnteza de fragmentos de ouro"),
a aparência do Heaven Qi (libélula verde de oito pares de asas), a nota do Templo da
Gravidez e a ressalva de que o nome "Reencarnação" promete mais do que o cânone entrega.
O Golden Aurora ainda mudou de casa: estava no caminho da luz e foi para o **caminho do
metal**, que é o que a obra lhe atribui.

#### Segunda leva — a família dos Gu de alma, lida na fonte

Um capítulo enumera a família inteira dos Gu que refinam a alma, e o catálogo tinha só
parte dela. A lista canônica traz quinze nomes — divine, dragon, ice, dream, moon,
general, grudge, poem, horse e heroic **soul** Gu, mais qi, body, cloud, wind e tiger
**spirit** Gu — e o catálogo cobria seis. **Oito entraram nesta leva** (o dragon soul
veio pela pesquisa do caminho da força, com rank 3 declarado e mecanismo próprio).

Sobre a lista inteira a obra diz uma frase só: *"esses Gu podiam refinar a alma, todos
tinham seu uso próprio"*. Nenhum efeito individual é descrito, e as oito fichas novas
dizem isso com todas as letras em vez de inventar oito efeitos plausíveis — o que teria
sido fácil e seria exatamente o erro que a política dos quatro estados existe para
impedir. O que elas trazem de aproveitável é o mecanismo da **classe** e o preço de
mercado da categoria (7.700 pedras primevas por um Gu de alma de rank 3).

Duas observações ficaram registradas nas células porque a designer vai tropeçar nelas:
a obra alterna *soul* (alma) e *spirit* (espírito) dentro da mesma enumeração **sem
explicar se é sinônimo ou subclasse**; e há um paralelo canônico útil para quem quiser
inventar em cima — nove exemplares do wolf soul Gu convertem uma alma de cem homens em
**alma-lobo**, o que sugere que empilhar exemplares do mesmo tema seja a mecânica da
família toda, mas isso é dedução nossa e está marcado como tal.

#### Segunda leva — a varredura final por frequência

A varredura foi refeita do zero, em duas passadas: uma exigindo maiúsculas (nomes de Gu
são nomes próprios) e outra insensível a maiúsculas. **A segunda foi indispensável** e
confirma o achado que abre este relatório: Ice Blade Gu e Moonhand só aparecem em
minúsculas na obra. Sobraram 392 candidatos, dos quais cerca de noventa foram verificados
um a um com leitura de contexto.

**Trinta e sete Gu novos, todos mortais.** O lado imortal não devolveu nenhum nome
inédito, o que é em si um resultado: o catálogo imortal está fechado por este método.

O achado mais volumoso foi a **escada inteira dos Gu de zumbi do caminho da
transformação**: Roaming e Flying Zombie já estavam catalogados, mas faltavam os degraus
intermediários (hairy, hopping) e os **cinco grandes zumbis voadores** nomeados — asura,
demônio celeste, pesadelo, praga — mais um sexto, o Earth Chief Zombie. Entraram também
famílias inteiras que existiam pela metade: os Beast Enslavement Gu (tigre, cervo,
touro), o par Black Hair / Steel Hair, e o Golden Coat, que a varredura reencontrou por
conta própria.

Duas entradas foram **redigidas e depois retiradas** na verificação final, e o motivo
vale como aviso metodológico: *Scar Stone Gu* e *Thunderwings Gu* já estavam catalogados
sob outra grafia — o primeiro como "Stone Scar", o segundo com ficha própria de rank 3.
No sentido inverso, o *Ironfist Grappling* foi descartado como falso positivo e depois
**reabilitado**: o contexto mostra um Gu real de rank 5 — uma mão de ferro negro que rasga
o céu, persegue o alvo e só se solta se ele a estilhaçar, pagando com quase todos os
ossos.

Os falsos positivos previstos reapareceram todos, e um deles merece registro permanente:
**"Yellow Earth Gu" e "Green Lotus Gu" não existem** — a busca devolve zero ocorrências
nos seis volumes. São facções, e já haviam entrado por engano numa lista de Gu antes.
"Nu Er Gu" é pessoa da tribo Nu Er; "Rising Purple Lightning Gu Ting" é epíteto mais nome
próprio; e "righteous" precisou de leitura caso a caso — quinze das vinte e duas
ocorrências são a facção dos Mestres Gu do caminho justo, e apenas três são o Righteous
Gu de verdade.

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

A tabela abaixo trazia a coluna de veredito **em branco** na primeira leva, o que
contradizia o texto que a apresenta. Ficou preenchida: cada descarte agora diz qual
padrão o explica, e a designer (ou uma sessão futura) pode conferir em vez de confiar.

| Candidato | Padrão | Veredito |
|---|---|---|
| `nu er` | 4 | "Nu Er Gu" é **pessoa** da tribo Nu Er, não Gu |
| `wan` | 4 | recorte de "Wan Gu Chou", **nome próprio** |
| `level year` | 5 | recorte de "mortal/immortal **level** year Gu" — o Gu é o **Year Gu** |
| `level day` | 5 | idem, para o **Day Gu** |
| `recon Gu` | 1 | **categoria funcional** (Gu de reconhecimento), não nome |
| `mystical Gu` | 1 | categoria: os "Gu místicos" são uma **classe** de dez Gu Imortais, e cada um tem nome próprio |
| `great movement Gu` | 1 | categoria funcional (Gu de movimento de grande porte) |
| `great flying zombie` | 3 | adjetivo + **Flying Zombie Gu** |
| `incomplete ghost fire Gu` | 3 | é o **Ghost Fire Gu** num estado de refino incompleto |
| `wild lightning` · `wild light` · `wild year Gu` · `wild wisdom Gu` | 3 | "wild" (selvagem) diz apenas que o exemplar **nasceu na natureza** em vez de ter sido refinado; os Gu são Lightning, Light, Year e Wisdom |
| `human shaped life` | 1 | descreve uma **forma de vida humanoide**, não um Gu |
| `ideal healing` | 3 | recorte de "um Gu de cura ideal" — adjetivo do narrador; o Gu da cena é o **Accumulating Ash Gu** |
| `lifebound Gu` | 1 | é o termo genérico para **Gu vital** (o Gu ao qual a vida do Mestre está atada), e não o nome de um Gu |
| `purple digital shade` | 3 | os **Digital Shade Gu** são Gu-registro de receitas, e a **cor indica o rank das receitas guardadas** — verde para as baixas, amarelo para rank 4, roxo para rank 5. "Purple" é atributo, não nome |

**Falsos positivos desta segunda leva**, todos verificados com leitura de contexto:

| Candidato | Veredito |
|---|---|
| `Yellow Earth Gu` · `Green Lotus Gu` | **não existem**: a busca devolve zero ocorrências nos seis volumes. São **facções**, e já haviam entrado por engano numa lista de Gu numa leva anterior — este é o registro definitivo de que não são Gu |
| `Rising Purple Lightning Gu Ting` | epíteto seguido de **nome próprio** (padrão 4) |
| `righteous` | exigiu leitura caso a caso: **quinze das vinte e duas ocorrências** são a facção dos Mestres Gu do caminho justo. As outras três são o **Righteous Gu** de verdade, que entrou no catálogo |
| `Dragonfish` | **não é Gu**: é uma espécie artificial criada pelo criador do caminho da comida para servir de comida universal de Gu, e é a fera desolada mais fraca do mundo |
| `Star Night Mucus` · `Black Oil` · `Truthful Floating Ice` · `Lucky Jade` · `Qi Harvest Fruit` · `Nether Grass` | **materiais e consumíveis**, não Gu. Ficam fora dos catálogos de Gu por definição — e duas correções de grafia saíram daí: a obra escreve *lucky jade* (não "luck jade") e *qi harvest fruit* (não "harvest qi fruit") |

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


---

## Entradas reescritas

O critério do projeto para uma linha de catálogo é que ela responda **o que acontece,
quanto, por quanto tempo, em quem e com que limite** — o teste é "um mestre consegue
rodar isto com o que está escrito?". Descrição curta não é defeito; vaga é. O pior caso
é a entrada que se descreve por referência a outra ("versão menor da mesma série"), e
essas foram caçadas primeiro.

**Método.** Extração programática da célula de efeito de toda linha dos dois catálogos,
com dois filtros: (a) células com menos de setenta caracteres, e (b) células que
contêm construção referencial (*"da mesma série"*, *"mais denso que os comuns"*,
*"versão menor"*, *"ver acima"*). Deram 180 entradas, divididas em três levas de
pesquisa no texto-fonte, cada uma obrigada a devolver mecanismo com números ou a
declarar explicitamente que a obra cala.

**As sete piores — entradas que só se descreviam por referência a outra:**

| Gu | Como estava | Como ficou |
|---|---|---|
| Dragon-elephant Huge Strength Gu | "fantasma de dragão-elefante, mais denso que os comuns" | mecanismo do fantasma de fera, escala de força e o que "mais denso" significa em combate |
| Ancient Bronze Skin Gu | "pele de bronze antigo, muito superior às versões comuns" | efeito próprio, mais o dado de que submergir o usuário em bronze fervente acelera a instalação em 30% |
| Essence Iron Bone Gu | "esqueleto duas a três vezes mais firme que o do Iron Bone" | efeito próprio e o lugar dele na regra do teto corporal |
| Big Strength Defecate Gu | "mesma função do Defecate Gu, mesma aparência, três vezes mais forte" | função descrita por inteiro, sem depender da linha vizinha |
| Star Thought Gu | "o combustível de dedução mais eficiente da série" | o que ele faz e quanto rende por unidade |
| A Bit of Star Gu | "o degrau mais baixo da série de amplificação estelar" | efeito próprio e a escada completa nomeada |
| Wine Drinker Gu | "equivalente imortal da série de Gu de profissão" | ficha própria de mecanismo |

**Entradas que a pesquisa corrigiu, e não apenas ampliou.** Estas são as mais
importantes do relatório, porque o catálogo estava **errado** nelas:

| Gu | O que estava escrito | O que a obra diz |
|---|---|---|
| **Aurora Bird** | listado como Gu de rank mortal no caminho da luz | **não é um Gu**: é um golpe combinado mortal do caminho da luz, transmitido de mestre para discípulo, cujos Gu componentes a obra nunca nomeia. A linha foi **removida** do catálogo, e a seção da luz ganhou o registro do erro |
| **Wolf Care Gu** | "cura em massa de lobos, e compartilha a visão de uma fera" | a cura em massa é do **Wolf Smoke Gu**. O Wolf Care Gu faz uma coisa só: compartilhar visão — e reside como uma segunda pupila no olho esquerdo do dono |
| **Rock Skin Gu** | rank `—` | **rank 1**; a versão de corpo inteiro é o Monolith Gu, rank 2 |
| **Ghost Fire → Ghost Flame → Ghost Blaze** | classificado como fogo | é **caminho da alma**: o fogo azul não fere o corpo, queima a alma direto. Ranks 2 → 3 → 4 confirmados |
| **Iceblade Gu** | lâmina de "um metro e setenta" | pouco mais de **um metro** no rank 3, dois metros num patamar acima |
| **Lifespan Gu** | "cem ou quinhentos anos, conforme o grau" | os graus canônicos são **cem** e **mil** anos; os seiscentos anos de vida de um caso famoso vieram de **acumular cinco** Gu de cem |
| **Second Aperture Gu (série)** | rank 1-5 | a série vai de **rank 1 a 6** — o original era um Gu Imortal de rank 6, convertido depois em série mortal |
| **Dragonpill Cricket Gu** | "salto de cerca de dez metros" | **três metros** na esquiva lateral, **dez** no recuo |
| **Inch of Time** | "paga o pedágio de tempo no lugar do tempo de vida do usuário" | esse uso **fracassou** no cânone: funciona em teoria, mas o consumo é intenso demais. E o Gu **não pode ser usado em humanos nem no próprio usuário** |
| **Space Thought Gu** | "pensamentos criptografados, ilegíveis a leitores de mente" | a obra não afirma isso; o que ela mostra é armazenamento de informação em forma de pensamento e **refino reverso** de um Gu inimigo alojado no crânio |
| **Wealth Gu** | uma linha só | são **dois** Gu: o lendário (imortal, vira qualquer coisa menos ser vivo) e o mortal de rank 5 (vira qualquer material de rank 5) |
| **Landscape As Before** | "restaura o terreno" | o rank 8 é o **teto absoluto** deste Gu, e ele só age sobre **montanha e corpo d'água** — móveis e construções ficam de fora |
| **Territory Gu** | "raio de até mil li" na linha mortal | os mil li são da versão **imortal de rank 7**; as versões de aldeia são rank 3-4 |
| **Heart Blood Gu** | "emite um batimento que sincroniza o de quem o ouve" | não corresponde ao texto: é o núcleo de um golpe de **premonição** — o sangue se choca contra as paredes do próprio coração e daí nasce a percepção de perigo |
| **Instant / That Time** | dois Gu de rank 7-8 do caminho do tempo | **os nomes não existem no texto-fonte**. A varredura não achou nenhuma ocorrência: vieram de fonte secundária. O que a obra descreve é uma **Casa de Gu Imortal** de rank 8 que comprime o tempo do trajeto. A linha foi mantida com o aviso explícito de que o nome é não canônico |
| **Musician Gu** e a série das profissões | listados sem separação de patamar | a obra divide a série em dois níveis: **Mestre Gu** (doctor, pill refiner, constable, craftsman) e **Gu Imortal de rank 6** (shadow puppet, talented girl, soldier, sergeant, musician, thief, farmer, dancer, blacksmith). E acrescenta o mecanismo: o que esses Gu produzem é um **clone** cuja abertura só **armazena** essência, nunca a produz, e que **não consegue cultivar** — o rank do Gu decide a força do clone, mas o clone herda os níveis de domínio do dono |

**Entradas ampliadas com números que faltavam** (amostra do que a leva de aprofundamento
devolveu, e que agora está nas células): Green Silk Gu custa 30% da essência de bronze
verde por ativação; Frost Breath Gu custa 5% e foi leiloado por 38.000 pedras; Bitter
Strength Gu tem preço de mercado por volta de 380.000 e foi arrematado por 810.000; Ice
Crystal Gu custa 28.000; Bone Wings Gu custou 180.000 de refino e exige de dois a três
anos de treino para voar e mais de cinco para lutar voando; Sight Blow Gu tem limite
rígido de trezentos passos; Wolf Smoke Gu cobre mais de cem li de raio; Flash Blink Gu
trava o Shadow Follower Gu por três horas; Moonshadow Gu suprime 60% da essência de um
rank 3, 30% de um rank 4 e 15% de um rank 5; Soft Bones Gu amolece ossos num raio de
vinte e cinco quilômetros e atravessa até ossos de ferro-essência; Bone Spike Gu devolve
ao próprio usuário cerca de 80% do dano que causa e é vendido por 6.700 pedras; Golden
Lion Fur Gu, fundido num golpe defensivo, eleva a defesa em 150% e em 200% contra o
caminho do metal; Biao Strength Gu concede cinco vezes a força de um tigre; e a série
Bone Flesh Unity tem cinco qualidades com perdas de transferência de 4/5, 3/5, 2/5, 1/5
e **zero**.

**Uma regra do mundo apareceu repetidamente durante o aprofundamento** e vale mais que
qualquer linha isolada: abaixo do rank 6, o corpo mortal é descrito como "uma tigela que
não contém um lago" — há um **teto rígido** de quanta força de fera e de quanta alma ele
suporta. Os Gu de osso, tendão, pele e músculo existem exatamente para levantar esse
teto, e as rotas são **mutuamente excludentes**: tendões de aço somados a ossos de ferro,
ou músculos de gelo somados a ossos de jade, ou ossos da impermanência para quem investe
em alma. Escolher uma fecha as outras.

### Segunda leva — mecanismo no lugar do rótulo

Esta é a frente que mais muda a experiência de mesa, e o método foi o mesmo da primeira
leva: extração programática das células de efeito, corte por comprimento e por construção
referencial. O catálogo mortal saiu limpo — as seis linhas que o filtro pegou eram falsos
positivos, células longas que casavam com o padrão. **O catálogo imortal tinha
quarenta e três**, e foram todas resolvidas.

**Vinte e um Gu Imortais** que se descreviam numa linha ganharam ficha inteira. Nove
delas eram **erro, e não apenas escassez**:

| Gu | O que a linha dizia | O que a obra diz |
|---|---|---|
| **Fate Armor** | "armadura de luz que resiste a feras imemoriais" | o mecanismo é **checagem do destino**: invencível se o portador não estiver fadado a morrer, papel se estiver. E o Gu é, de propósito, um **farol de rastreamento** para quem o emprestou. O limite de "cinquenta respirações" era da reserva de essência do portador, não do Gu |
| **Blacksmith** | "Gu vital" | **não é Gu vital de ninguém**. O Gu vital era o *craftsman Gu*; o Blacksmith foi receita adicional, obtida por ressonância com uma herança do caminho do metal |
| **Shadow Puppet** | rank `—` | **rank 6** — e é o único da série das profissões cujo perfil de caminhos a obra declara: homem + transformação + sombra |
| **Liquor Worm** (rank 8) | "a única rota conhecida para essência de rank 9" | é a única rota **para quem não é Venerável**: a abertura imortal de um Venerável produz essência de rank 9 sozinha |
| **Self Love** | "faz a vontade dentro de um Gu roubado amar a si mesma" | esse é o uso menor. O principal é ser **núcleo do golpe de auto-limpeza de marcas de lei**, que apaga rastreamentos e **rompe acordos de aliança** — e o critério do que apagar é do Gu, não do usuário: só sai o que for "prejudicial" |
| **Perceivable Dao** | "mede as marcas de um caminho" | mede **todos os caminhos de uma vez**, é do **caminho da informação**, funciona em terras abençoadas inteiras e **não funciona em Gu Imortais** (que são fragmentos do Grande Dao, não marcas de lei) |
| **Practice** | só a escultura do núcleo de formação | falta o uso maior: aplicado a uma pessoa, incha o corpo até o tamanho de um gigante e **oculta a aura por completo** — foi o passo com que um Venerável tentou ultrapassar o próprio patamar. E a origem está no mito fundador |
| **Formation Spirit** | "gera uma inteligência que gerencia a formação" | o espírito **morre se a formação morrer**, **remenda a formação sozinho**, **opera formações melhor que um grão-mestre** — e **pode ser enganado, porque é ingênuo** |
| **Dark Limit** | consumo genérico | a reserva de ocultação é **gasta por cada adivinhação inimiga** que incide sobre o portador, e há tempo de recarga longo depois de cada uso |

Três dos vinte e um a obra **realmente só rotula**: Medicine Fragrance, Eat Fragrance e
Dew — uma ou duas frases cada, sem raio, duração nem limite. As células dizem isso.

Um número novo que vale sozinho: o **Snack Gu** alimenta outro Gu Imortal em **6% da
refeição de um Gu de rank 6 por dose, com teto de 40%**, recarga de dias, e **morre se
for forçado**. E um alerta de honestidade que o relatório precisa carregar: entre esses
vinte e um Gu, a **única dieta canônica** é a do Vajra Thought (fruto de veado divino,
rank 6, cerca de 1.350 pedras de essência por alimentação, que cresce nos chifres de uma
fera desolada). Todas as demais dietas dessas linhas continuam sendo invenção nossa e
seguem marcadas com `*`.

**As vinte Casas de Gu Imortais** que tinham descrição de uma frase ganharam mecanismo
completo, e nenhuma ficou no rótulo. Seis das descrições antigas estavam **erradas**:

| Casa | Correção |
|---|---|
| Eternal Yacht | rank **7**, não 8 — a obra a classifica junto com o Present and Past Pavilion como "apenas rank sete" |
| Cooking Luck Pot | **6 → 7**, não 7 → 8. A regra por trás: uma casa de rank N governa sorte de rank N e apenas *influencia* rank N+1 |
| Thieves Den | rank **8**, não "pico" |
| Star Constellation Chessboard | o teleporte em massa é função **secundária e cara** (exige a formação, as estrelas e a força de outro imortal; sozinha é ineficiente e derruba a dedução do operador). A função principal é ser a **número um do mundo em dedução** |
| Winding Light Platform | o rótulo tinha invertido o fato: quem esmagou os Gu internos foi um inimigo **contra ela**, não ela contra o alvo |
| Dragon Palace | a obra **não descreve teste formal de candidatos por reino de sonho** — o reino de sonho é barreira e isca, e a escolha do dono é decisão do **espírito da casa**. A célula diz isso com todas as letras |

**Quatorze Casas ausentes entraram**, entre elas a **Turtle House**, que é a primeira
Casa de Gu Imortal da história, e a **Demon Judgment Board**, que ao incorporar um único
Gu Imortal de rank 8 de "relação de sangue" passou a **detectar todo cultivador do
caminho do sangue do mundo que não seja de rank 9** — o exemplo mais claro do que
acrescentar uma peça faz por uma Casa já pronta. A seção passou de 27 para **45 Casas**.

A seção das Casas ganhou também **dez regras do mundo** no cabeçalho, que respondem à
maioria das perguntas que uma mesa faz e que estavam espalhadas por dezenas de
capítulos: a função vem do arranjo e não de um Gu; uma casa de rank 7 pode ter mais de
três mil Gu; a potência é proporcional à essência gasta; perder o núcleo inutiliza a
casa, mas o núcleo costuma sobreviver aos destroços e pode ser resgatado; construir uma
casa pode fracassar; **a fraqueza genérica de toda casa é a previsibilidade** — "os
métodos de uma casa são fixos e difíceis de mudar", e depois de mapeada a ameaça cai um
patamar; o rank não é teto de desempenho; casas hospedam vontades residuais de imortais
mortos; **uma casa pode ter espírito próprio, que escolhe o próprio mestre**; e refinar
uma casa alheia é sobretudo compreendê-la, contra a resistência ativa dela.



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

## Decisões tomadas

Cada decisão abaixo resolveu uma ambiguidade real. Estão registradas para que uma
sessão futura não as refaça em sentido contrário.

1. **A casa de um Gu é a seção do caminho que a obra lhe atribui.** As seções que são
   famílias funcionais (cura e vida, armazenamento, furtividade, Gu lendários) ficam
   apenas com os Gu para os quais a obra não declara caminho nenhum. Quando um Gu com
   caminho declarado estava numa seção funcional, a ficha mudou de casa e a seção
   funcional ganhou um ponteiro em itálico.
2. **Exceção deliberada à regra 1: a linhagem lunar.** Aquela seção não é um caminho, é
   um estudo de caso de árvore de fusões de um clã, e seu valor didático depende de as
   linhas ficarem lado a lado para comparação — o texto da seção manda o leitor comparar
   colunas entre ramos. Blood Moon Gu e Moon Poison Gu ficaram lá mesmo tendo caminho
   declarado (sangue e veneno), e as duas seções de caminho ganharam ponteiro.
3. **Todo Gu de rank 9 mora na seção "Os Gu de rank 9", nunca na seção do caminho.**
   O motivo é estrutural: naquele patamar as três aptidões se dissolvem e as fichas usam
   colunas diferentes das demais. Manter cópias nas seções de caminho produzia
   divergência — e produzia de fato, em oito dos nove casos.
4. **Gu com versão mortal e versão imortal ficam com uma linha em cada catálogo**, e
   cada linha declara a existência da outra com o rank dela e o link. Não é duplicata: a
   obra explicita que ter a versão imortal **não dispensa** ter a mortal, porque um Gu
   Imortal é único e não serve a dois golpes ao mesmo tempo.
5. **Gu cujo único rank conhecido é 6 ou mais saem do catálogo mortal**, mesmo quando a
   tradição do vault os listava lá por serem Gu do mito fundador. A seção de origem
   ganhou ponteiro em vez de linha.
6. **Três seções novas no catálogo mortal**: caminho do vento, caminho do metal e "outros
   caminhos com poucos Gu". As duas primeiras são caminhos reais que agora têm massa
   crítica; a terceira evita criar seções de uma linha só para qi, yin-yang, sonhos e
   comida, e recebe também os Gu cujo caminho a obra nunca declara. Cada linha de lá diz
   a que caminho pertence.
7. **Nome truncado pela varredura não é descarte, é correção.** Quando o n-grama cortou o
   começo do nome (`hole jade flute` → Five Hole Jade Flute Gu), a entrada foi para o
   catálogo com o nome canônico completo, não descartada como falso positivo.
8. **Quando a obra só dá o nome, a célula diz isso com todas as letras.** Nada de
   descrição inventada disfarçada de canônica e nada de traço mudo. A frase "a obra cita
   o nome e nada mais" é informação útil: marca exatamente onde a designer pode inventar
   sem contradizer o cânone.
9. **Dieta ausente vira ritmo por rank, marcado `(ded.)`.** A obra dá a frequência de
   refeições por rank como regra geral do mundo, então uma linha sem cardápio ao menos
   informa o **ritmo da despesa**, que é a metade que importa para orçamento. O cardápio
   continua em branco, ou aparece como invenção marcada com `*`.
10. **Nenhum nome de personagem no corpo das fichas.** A pesquisa devolveu dezenas de
    exemplos mecânicos com nomes próprios do enredo; todos foram convertidos em papéis
    ("um Mestre Gu do caminho da força", "o dono da terra abençoada"). Ficaram apenas os
    nomes do mito fundador e os Veneráveis, que são figuras estruturais do mundo e não
    personagens do enredo — é o que a política de spoilers do projeto permite.
11. **Nenhuma citação de capítulo no corpo das fichas.** As que a pesquisa trouxe foram
    removidas das células; a rastreabilidade fica no `fontes` do frontmatter e neste
    relatório.
12. **Um nome que a varredura não encontra no texto-fonte fica no catálogo, mas com
    aviso.** Foi o caso do par "Instant / That Time": em vez de apagar a linha, ela diz
    que o nome vem de fonte secundária e não é canônico, e descreve o que a obra de fato
    mostra. Apagar teria escondido a dúvida; manter sem aviso teria propagado um erro.
13. **Comparar nomes exatos não basta para achar duplicata — nem comparar sem
    maiúsculas.** A regra que passa a valer: normalizar para minúsculas, **remover o
    sufixo "Gu", descartar toda pontuação e todo espaço** e considerar troca de ordem
    entre palavras. Foi só assim que apareceram seis duplicatas reais (Jade Bone/Jade
    Bones, Giant Mountain Puppet/Mountain Giant Puppet, Moon Scar/Moonscar, Breath
    Concealment/Breath Concealing, Ironfist/Iron Fist Grappling, Iceblade/Ice Blade)
    depois de duas auditorias que se declararam concluídas.
14. **Duplicata se funde preservando as duas células, e a grafia alternativa fica
    visível.** A ficha que sobrevive recebe, entre parênteses e em itálico, o outro nome
    e o que a obra registrava só sob ele. O motivo é de uso: quem procurar "Ice Blade"
    precisa cair na mesma ficha de quem procurar "Iceblade", senão o catálogo mente por
    omissão.
15. **Reciprocidade de par é obrigação dos dois lados, e menção em prosa não conta.**
    Várias fichas imortais diziam "na versão mortal de rank 5, que a obra detalha…" e não
    linkavam. Para uso em mesa isso não resolve: a designer precisa do salto. Toda ficha
    de um par declara o rank da outra e traz o wikilink.
16. **Quando duas fichas do mesmo Gu existem e uma é mais rica, fica a rica — mas ela
    absorve o que só a pobre tinha.** Nunca se apaga uma linha sem transplantar o
    conteúdo exclusivo dela, mesmo que seja um detalhe pequeno como a aparência do Gu ou
    a rota de coleta.
17. **Rank vai na coluna de rank; explicação vai na coluna de efeito.** Uma ficha trazia
    um parágrafo inteiro dentro da célula de rank. Quando o rank é ambíguo, a célula leva
    `—` mais uma nota curta entre parênteses, e a explicação inteira migra para o efeito.
18. **Sintaxe de wikilink em tabela segue a convenção do vault**, que é o pipe escapado
    com **uma** barra. Os dois catálogos usavam três, e eram os únicos arquivos do vault
    a fazê-lo.
19. **Um efeito que a obra descreve em detalhe nunca fica registrado como "a obra não
    descreve".** Foi o erro do par Cause / Effect, cuja ficha afirmava que a obra calava
    o mecanismo enquanto ela o descrevia por inteiro em três capítulos. Negativa também
    se verifica antes de ser escrita — a regra do projeto vale nos dois sentidos.
20. **Material, consumível e espécie não entram em catálogo de Gu.** Star Night Mucus,
    Black Oil, Truthful Floating Ice, lucky jade, qi harvest fruit, nether grass e o
    dragonfish foram identificados, descritos e **deixados de fora**, com o registro do
    que são — para que uma varredura futura não os reencontre como "Gu faltando".
21. **A regra de "nenhum nome de personagem nas fichas" foi auditada, não só declarada.**
    A decisão 10 existia desde a primeira leva, mas quatro nomes tinham sobrevivido nas
    células (dois membros de um clã, o epíteto de um pesquisador e um parente de um
    portador). Todos viraram papéis — "o chefe daquela facção", "um Mestre Gu de clã", "um
    pesquisador solitário do caminho do refino", "um parente idoso do portador". Uma
    varredura por nomes próprios de três sílabas nos dois arquivos hoje devolve só nomes
    de Gu. Vale como método: **decisão de política se verifica com busca, não com
    memória**.

---

## Cobertura estimada

Os números do fim desta leva, todos conferidos por script sobre os arquivos:

| | Antes da leva | Depois |
|---|---|---|
| Gu no catálogo mortal | 589 | **649** |
| Gu no catálogo imortal | 255 | **273** |
| Casas de Gu Imortais | 27 | **45** |
| Pares mortal × imortal | 22 (só 6 recíprocos) | **28, todos recíprocos** |
| Linhas com dieta preenchida — mortais | 402 (68%) | **537 (83%)** |
| Linhas com dieta preenchida — imortais | 251 (98%) | **261 (96%)** |
| Linhas com efeito de uma frase, catálogo imortal | 43 | **0** |
| Duplicatas internas | 1 intencional + 6 ocultas | **1 intencional** |
| Linhas com número de colunas errado | não medido | **0 nos dois arquivos** |
| Links quebrados no vault | 0 | **0** |

A queda percentual da dieta imortal é aritmética, não perda: entraram dezoito Gu novos
cuja dieta a obra não informa, e a política proíbe inventá-la sem marcar. O aumento no
lado mortal vem do ritmo por rank aplicado como dedução declarada.

**Quanto do acervo real isto cobre, não dá para saber, e é honesto dizer.** O que dá para
afirmar é o que cada método esgotou:

- A **varredura por n-grama sobre a palavra "Gu"** foi rodada duas vezes, em duas
  passadas de sensibilidade a maiúsculas, e na segunda rodada os quarenta candidatos mais
  frequentes já não devolviam nomes inéditos no lado imortal. Para os Gu que a obra nomeia
  com o sufixo "Gu", este método está perto do fim do que rende.
- Ele **não pega** o Gu que a obra menciona sem o sufixo, nem o que aparece só dentro de
  uma lista de composição de golpe. A colheita dos relatórios de profundidade existiu
  justamente para cobrir esse ângulo, e ela devolveu mais de cinquenta nomes que a
  varredura não tinha achado — o que mostra que os dois métodos são complementares e que
  **nenhum dos dois sozinho fecha o catálogo**.
- O terceiro ângulo, ainda **não explorado**, são os **catálogos de golpes**
  (`07` e `08`): todo golpe combinado lista os Gu que o compõem, e essa é a maior fonte
  de nomes de Gu que resta no vault. Uma leva futura que cruze a lista de componentes dos
  golpes com estes dois catálogos é a próxima coisa a fazer, e provavelmente ainda rende.

Sobre a **profundidade** das linhas, o número que interessa é o das quarenta e três
células de uma frase do catálogo imortal, que agora são zero. O catálogo mortal já estava
limpo nesse critério antes da leva. Isso não quer dizer que toda linha responda "o que
acontece, quanto, por quanto tempo, em quem e com que limite" — quer dizer que **onde ela
não responde, a célula diz que a obra cala**, em vez de disfarçar o silêncio com um
rótulo. É a diferença entre um catálogo incompleto e um catálogo enganoso.

---

## O que a obra realmente não diz

Registro das negativas, todas verificadas com busca direta no texto-fonte (sempre
insensível a maiúsculas) e não em fonte secundária. Uma negativa só entra aqui depois
de o grep voltar vazio.

**Sobre Gu falsificados.** A obra confirma que **falsificar Gu é prática corrente** e
mostra a cena inteira: um vendedor passou um Smelly Fart Fat Worm por Black Boar Gu, o
comprador só descobriu ao tentar refinar, e não obteve reparação nenhuma. Mas a obra
**não** diz, em nenhum lugar, que um Gu falso **se autodetona** nem que isso seja causa
de morte registrada. Buscas por `fake gu`, `counterfeit`, `self-destruct`, `self-detonate`
e por Gu explodindo não devolvem nada nesse sentido. A afirmação circula, mas não está no
texto — e por isso o aviso escrito no cabeçalho do catálogo mortal fala só do que é
canônico: a fraude existe, o preço é o único sinal prévio, e a descoberta vem no refino.

**O que a obra diz, e que é ainda mais útil:** *não é incomum um Mestre Gu ser morto pelo
próprio Gu*. Quem força a ativação de um Gu além do que a essência comporta sofre o
contragolpe da força daquele Gu e morre — e a obra afirma que "incidentes assim estão por
toda parte". O mesmo vale para o refino, que **sempre** produz contragolpe quando falha, e
para os golpes combinados, cujo contragolpe não se pode evitar, só atenuar. Isso entrou no
cabeçalho do catálogo mortal como aviso próprio.

**Efeito não descrito, apesar do Gu existir.** Uma família inteira de Gu tem nome, rank e
lugar no sistema, e nenhum efeito declarado. As células desses Gu dizem isso
explicitamente, em vez de inventar:

- a **escada de fogo de cinco degraus** (single orifice charcoal → double orifice stove →
  three orifices fire hut → four orifices fire tower → five orifices fire pagoda): a obra
  descreve a cadeia de refino inteira, degrau por degrau, e **nunca diz o que qualquer um
  deles faz** quando acionado;
- os **Gu de alma temáticos**, que na segunda leva passaram de seis para **quinze**:
  divine, dragon, ice, dream, moon, general, grudge, poem, horse e heroic **soul** Gu,
  mais qi, body, cloud, wind e tiger **spirit** Gu. Todos aparecem apenas em duas listas
  do mesmo capítulo, e sobre a lista inteira a obra diz uma frase só — "esses Gu podiam
  refinar a alma, todos tinham seu uso próprio". O mecanismo da **classe** está descrito;
  o efeito individual, **de nenhum deles**. Repare de passagem que a obra alterna *soul*
  (alma) e *spirit* (espírito) dentro da mesma enumeração sem explicar se é sinônimo ou
  subclasse — e as fichas dizem isso em vez de escolher em silêncio. O único da família
  que escapa da regra é o wolf soul Gu, cujo mecanismo a obra descreve (nove exemplares
  convertem uma alma de cem homens em alma-lobo), e agora também o dragon soul Gu, que
  turbina todo o arsenal de tema dragão;
- o **Kill**, Gu de rank 8 → 9: a obra registra a origem (nasceu sozinho no corpo de um
  Venerável, como reação do céu a um massacre) e a dieta (massacres), e **não descreve o
  efeito**;
- **Wooden Chicken Gu**, **Eight-faced Prestige Wind Gu**, **Exert Strength Gu**,
  **Afterlife Grass Gu**, **Abortion Gu**, **Reincarnation Gu** e **Snowy Plain Gu**: só o
  nome, e no máximo o contexto de uma transação ou de um passo de refino.

**Dados que a obra nunca fornece, para nenhum Gu.** Vale saber de antemão o que não
adianta procurar: tempo de recarga entre ativações; peso ou tamanho da maioria dos Gu;
quanto exatamente um Gu come por refeição em unidade de massa; taxa de mortalidade de um
Gu mal alimentado; e prazo de vida natural de um Gu mortal. O ritmo de refeições por rank
existe; a quantidade por refeição, não.

**A dieta da maioria dos Gu mortais.** A obra a cala porque no mundo ela é trivial —
hoje **cerca de um sexto** das linhas do catálogo mortal continua sem cardápio (eram um
terço), e é onde a designer vai precisar inventar. O ritmo por rank, esse sim, é canônico
e está em todas.

No lado imortal a situação é a inversa e vale um aviso: a dieta de um Gu Imortal costuma
ser parte da identidade dele, mas **as fichas dos Gu de caminho da sorte são a exceção
quase completa** — a obra declara a dieta de apenas **dois** deles (areia da gaivota de
areia mundana, para o Connect Luck; fezes de seis espécies de cães desolados, para o Dog
Shit Luck). Tudo o mais naquele caminho está marcado com `*`. O mesmo vale para os vinte e
um Gu Imortais aprofundados nesta leva, entre os quais só o Vajra Thought tem dieta
canônica (fruto de veado divino, cerca de 1.350 pedras de essência por refeição).

**Silêncios novos, registrados nesta leva.** Todos verificados com busca direta:

- **A capacidade das Casas de Gu Imortais**, em número de imortais que comportam, **nunca
  é informada** — para nenhuma das quarenta e cinco.
- **As Casas da esquadra do Rio do Tempo** só existem como enumeração: a obra as lista em
  série, num capítulo, como projeto da corte celestial, e **não dá ficha técnica de
  nenhuma** exceto a Golden Age Platform. Aparência, Gu-núcleo e comparações de
  velocidade e defesa tiveram de ser garimpados em cenas de batalha esparsas.
- **A série dos números do caminho da regra** — one, two, three, four, five… — é descrita
  como o maior conjunto de Gu do caminho e "praticamente ilimitada", a obra mostra um One
  Gu e um Three Gu de rank 7 nominalmente, e **nunca descreve o efeito de nenhum deles**.
- **Star Shield Gu** e **Bane Star Gu** têm uma ocorrência cada, na mesma linha, como
  ingredientes de um golpe. Sem rank, efeito, dieta ou refino.
- **Medicine Fragrance**, **Eat Fragrance** e **Dew Gu**: uma ou duas frases cada, sem
  raio, duração, número ou limite.
- **Peach Blossom Luck Gu**: a obra dá o nome e o preço alto, e nada mais. O efeito na
  ficha é dedução a partir da descrição canônica da *sorte* de flor de pessegueiro, e está
  marcado como dedução.
- **Departure**, **Main** e **Ripe Gu** do caminho da regra: uma ocorrência cada, com
  rank em um caso, contexto de uso, e **efeito nunca enunciado**.
- **Os Gu de zumbi voador de topo** (asura, demônio celeste, pesadelo, praga): a obra os
  nomeia como os "cinco grandes" e descreve a escada que leva até eles, mas o efeito
  individual de cada um fica de fora.
- **Iron Rod Gu** e **Leather Whip Gu**: uma ocorrência cada, na mesma frase. Só a
  origem — o bastão é conversão do caminho do metal para o das armas, o chicote é
  combinação de transformação com armas.

**Preço.** A obra dá preço em pedras primordiais para poucas dezenas de Gu, e quase nunca
para Gu Imortais — no patamar imortal ela é explícita em que **não há preço**, só troca,
o que é uma resposta e não uma lacuna.
