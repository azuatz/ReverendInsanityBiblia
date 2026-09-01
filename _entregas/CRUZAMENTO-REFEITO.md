# Cruzamento refeito — Gu do romance × catálogo do RPG

Substitui `GU-AUSENTES-NO-RPG.md`, cujo número (414) era ruído. **Descartem aquele arquivo.**

## O que deu para afirmar, e o que não deu

Nosso catálogo tem **617 Gu** identificados na leitura integral do romance. O catálogo
do RPG tem 424 registros, dos quais **168 carregam o nome em inglês**.

- **110 dos nossos Gu casam com a coluna inglesa de vocês** — presença confirmada.
- **507 não puderam ser confirmados automaticamente.**

O segundo número **não significa "ausentes"**. Significa apenas que a comparação
automática é cega entre idiomas: nossos nomes estão em inglês, os de vocês
majoritariamente em português, e traduzir automaticamente produziria falsos negativos
piores que o problema original. Um "Attitude Gu" nosso e um "Gu Atitude" de vocês são
o mesmo Gu e não casam por string.

## Por que não insisti numa heurística de tradução

Testei e o resultado piorou (507 contra os 414 originais), porque cada tentativa de
casar por radical cria falso positivo em Gu de nomes parecidos e falso negativo em
traduções não literais. Preferi entregar um número honesto e pequeno de certezas a um
número grande e não confiável.

## Como fechar isso do lado de vocês

A lista abaixo traz, para cada Gu não confirmado: **nome em inglês, rank e um resumo
curto do efeito**. O resumo é o que torna o casamento viável — vocês conhecem os nomes
em português, e o efeito desambigua os casos de nome parecido.

Sugestão de procedimento: varram a lista comparando por efeito, não por nome. O que
sobrar sem correspondente é o conjunto realmente ausente, e aí a curadoria vale a pena.

Fichas completas em `09 - Apendices/Catálogo de Gu - Mortais.md` e
`09 - Apendices/Catálogo de Gu - Imortais.md`.

## Convenção das fichas (importante ao importar)

Quatro estados, e eles carregam informação:

- texto simples — **canônico**, a obra afirma;
- `(ded.)` — dedução segura a partir do que a obra afirma;
- `*` — **invenção plausível nossa**, sem base textual, feita a pedido do autor para
  não deixar lacuna. Pode ser descartada inteira sem perder nada de cânone;
- `—` — a obra não informa e nada foi preenchido.

| Gu (inglês) | Rank | Efeito (resumo) | Camada |
|---|---|---|---|
| A Bit of Star Gu | 1 | O degrau mais baixo da série de amplificação estelar | mortal |
| Ability Gu | — | Manifesta capacidade | mortal |
| Accumulate Virtue Gu | — | Refina-se sozinho conforme o dono pratica bondade | mortal |
| Accumulating Ash Gu | 3 | Cura que consome cinzas | mortal |
| Adaptation Gu | 8 | Converte marcas de lei de **qualquer** caminho em marcas de transforma | imortal |
| Addition Gu | 8 | Casulo preto-ferro | imortal |
| Advance Refinement | 8 → 9 | Reduz a dificuldade de elevar outros Gu Imortais de rank 8 a rank 9 | imortal |
| Affection Gu | — | Rastreia a localização de outro Gu, mesmo dentro de aberturas imortais | imortal |
| After Gu | 7 → 8 | Adia a provação atual, fundindo-a com a próxima | imortal |
| Airsac Gu | 3 | Preserva, fora do local de origem, um Gu que normalmente não sobrevive | mortal |
| Alert Bell Gu | mortal | Alarme de clã contra perigo iminente | mortal |
| Ancient Bronze Skin Gu | 4 | Pele de bronze antigo, muito superior às versões comuns | mortal |
| Ant Nest Gu | 8 | Cria e amamenta formigas-exército | imortal |
| Arm Bone Wings Gu | 3 | Asas ósseas nos antebraços que aumentam a velocidade de ataque | mortal |
| Attitude Gu | 8 | Altera a percepção da identidade | imortal |
| Aura Restraint Gu | 3 | Camufla a natureza real de uma fera | mortal |
| Aurora Bird | mortal | Pássaro de luz-arco-íris que ataca em alta velocidade | mortal |
| Autumn Gu | 7 | Grilo de canto altíssimo | imortal |
| Backtrack Gu | 5 | Reconstitui cenas passadas | mortal |
| Bamboo Gentleman | 4 | Detector de mentiras | mortal |
| Battle Thought Gu | 3-4 | Resistência mental coletiva de tropas contra ataques de pensamento | mortal |
| Bear Enslavement Gu | 2 | Controla ursos gigantes comuns | mortal |
| Beast Enslavement Gu | 7 | Subjuga qualquer besta do mundo, inclusive as imemoriais | imortal |
| Beast Skin Gu | 1 | Defesa básica por endurecimento da pele | mortal |
| Beast Strength Placenta Gu | 5 | Devora aberturas de mortos, convertendo-as em aptidão | mortal |
| Beast Tamer Gu | — | Domesticação de feras | mortal |
| Become Real | — | Cria uma trilha prateada persistente | imortal |
| Beggar Gu / Merchant Gu | — | Dariam mão de obra sem risco de traição | mortal |
| Berserk Gu | 4 | Dobra força, velocidade e agilidade por tempo limitado | mortal |
| Big ("Da") | — | Aumenta o tamanho físico do usuário | imortal |
| Big Family Qi | 7 | Armazena qi de tribulação para uso posterior | imortal |
| Big Qi | 8 | Absorve e manipula qualquer tipo de qi do mundo | imortal |
| Big Soul Worm | 2 | Versão maior e **intangível** do anterior | mortal |
| Black Mane Gu | 2 | Armadura de pelos que brota de todos os poros | mortal |
| Black and White Paper Gu | — | Contrato imune ao Eating One's Words | mortal |
| Blacksmith Gu | 6 | Gu vital que ressoa com o caminho do metal | mortal |
| Blessing in Disguise | 7 | Dobra as marcas de lei ganhas numa provação | imortal |
| Blood Asset Gu | 6 → 8 | Protege parte dos materiais num refino e permite restaurá-los se falha | imortal |
| Blood Battle Gu | — | Herança verdadeira | imortal |
| Blood Frenzy Gu | 4 | Infecta outros Gu, dando-lhes absorção de essência do ambiente | mortal |
| Blood Oath Gu | — | Forma pactos vinculantes de divisão de recursos | imortal |
| Blood Qi Gu | 6 | Uma das nove heranças verdadeiras | imortal |
| Blood Relation Gu | 8 | Detecta todo praticante do caminho do sangue abaixo do rank 9 | imortal |
| Blood Revenge / Cold Blood | — | Par que congela e captura o alvo vivo | imortal |
| Blood River Python | 5 | Regeneração extrema | mortal |
| Blood Rope Gu | mortal | Deduz a localização exata de um membro do clã pelo sangue | mortal |
| Blood Shadow Gu | — | Herança verdadeira | imortal |
| Blood Sweat Gu | — | Herança verdadeira | imortal |
| Blood Trace Gu | — | Reconstrói as ações passadas de um alvo como sombras de sangue | imortal |
| Blood Wight Gu | 5 | Primeiro estágio da linha de zumbi de sangue | mortal |
| Blood-sense Pair | — | Selo hereditário de contrato entre linhagens | mortal |
| Bloodline Gu | 7 | Testa uma gota de sangue e verifica parentesco verdadeiro | imortal |
| Blue Farm Slug Gu | 3 | Caramujo-cargueiro | mortal |
| Blue Sky Gu | 4 | Versão superior do anterior | mortal |
| Bookworm Gu | 1 | Transfere catálogos e conhecimento direto para a mente | mortal |
| Brave Fight Gu | 4 | Ignora a dor e dobra a força | mortal |
| Break Luck Gu | — | Rompe vínculos de sorte estabelecidos | imortal |
| Breath Concealment Gu | 3 | Oculta a aura e mascara o nível de cultivo | mortal |
| Bright Pearl Gu | 4 | Selagem de aura em duas camadas | mortal |
| Broadsword of Light Gu | 3 | Espadas largas luminosas | mortal |
| Brute Force Longhorn Beetle Gu | 1 | Força de touro por cinco respirações | mortal |
| Burial Soul Toad | 4 | Armazena almas | mortal |
| Bury Gu | — | Esconder-se sob o solo | mortal |
| Calamity Beckoning Gu | 7 | Atrai para si a calamidade destinada a outro | imortal |
| Calamity Luck Altar | 8 | sorte | imortal |
| Calm Gu / Fortitude Gu | — | Par de estabilização mental | mortal |
| Canopy Gu | 3 | Camada de luz branca sobre o corpo | mortal |
| Capture Wind Gu | 7 | Gu de movimento | imortal |
| Casa | Rank | Caminho | imortal |
| Cauldron Strength | — | Defesa em forma de vaso sem forma fixa | imortal |
| Cause / Effect | — | Par de causa e efeito | imortal |
| Chamber Pot | 7 | trevas | imortal |
| Change Form Gu | — | Disfarce por mudança de forma | mortal |
| Change Soul | 7 | Troca completa de almas entre dois corpos | imortal |
| Charging Crash Gu | 4 | Fusão das duas investidas | mortal |
| Chase Smoke Gu | — | Fumaça que prova contato físico ocorrido meses antes | mortal |
| Chasing Wind Gu | 4 | Velocidade "de perseguir o vento" | mortal |
| Clairaudience Gu | — | Audição extremamente sensível | mortal |
| Cleanse Soul | 6 | Limpa e refina almas | imortal |
| Clear Mind Gu | 4 | Reverte a fúria induzida | mortal |
| Clear Water Gu | mortal | Produz água limpa | mortal |
| Close Door Gu | 5 | Fecha o mesmo tipo de passagem | mortal |
| Clothing Gu | mortal | Transforma-se instantaneamente em roupa ao ser vestido | mortal |
| Cognition Gu | — | Refina informação bruta em conhecimento | mortal |
| Connect Luck | 6 | Liga a sorte de duas pessoas como vasos comunicantes | imortal |
| Consecutive Gu | 8 | Permite encadear golpes de **caminhos diferentes** entre si | imortal |
| Cook | 7 | comida | imortal |
| Cooking Luck Pot | 7 → 8 | sorte | imortal |
| Coptis Rhizome Gu | — | Fortalece a alma | mortal |
| Corrosion Blood Grass Gu | — | Tentáculo que desce pela garganta do alvo e o corrói por dentro | mortal |
| Crane Enslavement Gu | 5 | Controla um rei-fera de grous | mortal |
| Crazed Demon Formation | 9 | regra/céu | imortal |
| Create Dream Gu | — | Cria estruturas ilusórias dentro de um reino de sonho | imortal |
| Crystal Ladybug | — | Dispensador vivo de líquidos preciosos | mortal |
| Dark Limit | — | Sela a aura de uma constituição extrema e bloqueia adivinhação | imortal |
| Dark Prison | 6 | trevas | imortal |
| Dazzling Light Gu | mortal | Emite uma aurora vermelha usada para cultivar frutos de luz | mortal |
| Death Sentence Awaits | 7 | Fixa o momento exato da morte de um alvo | imortal |
| Delight in Water and Mountain | 6 | Gera "vontade alegre" em grande volume | imortal |
| Derivation Gu | — | Da explosão do seu estômago nasceu a humanidade comum | mortal |
| Destiny Gu | 10 (rumor) | Rank 10 lendário | imortal |
| Devour Soul Gu | 7 | Extrai e sela almas | imortal |
| Dew | 7 | Acelera a recuperação de essência imortal dentro de uma formação | imortal |
| Distorting Black and White Gu | — | Anularia o anterior | mortal |
| Distracting Thoughts | — | Gera pensamentos distrativos progressivos num raio | imortal |
| Divert Disaster Gu | 7 | Desvia calamidades e tribulações | imortal |
| Divination Tortoise Shell Gu | 7 | Defende contra deduções alheias | imortal |
| Divine Bean Palace | 8 | madeira | imortal |
| Divine Emperor City | 8 | pintura/homem | imortal |
| Divine Travel Gu | 6 | Teleporta o usuário para um lugar aleatório | imortal |
| Djinn Heart / Body / Mind Gu | 4 | Trio que triplica força física e mental | mortal |
| Do or Die Gu | 5 | Recarrega a essência instantaneamente | mortal |
| Dog Enslavement Gu | 1-2 | Domina um cão implantando-se na alma dele | mortal |
| Dog Shit Luck | 6 → 8 | Eleva a sorte, suavizando calamidades e ajudando refinos | imortal |
| Dragon Breath | 7 | Sopro de dragão | imortal |
| Dragon Palace | 8 | escravização | imortal |
| Dragon Scale | 7 | Componente de fusões de forma dracônica | imortal |
| Dragon Strength | 6 | Componente de formações de recurso de larga escala | imortal |
| Dragon Travel Tiger Steps Gu | 4 | Movimento de carga e impacto | mortal |
| Dragon-elephant Huge Strength Gu | 4 | Fantasma de dragão-elefante, mais denso que os comuns | mortal |
| Dragonpill Cricket Gu | 1 | Salto ou recuo instantâneo de cerca de dez metros | mortal |
| Dream Armor | 7 | Resiste às tribulações específicas do caminho dos sonhos | imortal |
| Dream Butterfly Gu | 6 | Pré-visualiza o resultado de uma escolha | imortal |
| Dream Token | 8 | Escraviza até quatro Imortais de rank 8 simultâneos | imortal |
| Dream Travel | — | Exploração de reinos de sonho | imortal |
| Dream Wings | 6 | Voo dentro de sonhos | imortal |
| Dreaming Gu | 7 | Núcleo de golpes de investigação e de defesa mental | imortal |
| Eagle Rise Gu | 4 | Voo | mortal |
| Earth Communication Ear Grass | 2 | Orelha-implante cujas raízes no solo estendem a audição a duzentos ou  | mortal |
| Earth Qi Gu | 8 | Borboleta marrom | imortal |
| Earth Refinement Gu | 4 | Refina e quebra um selo sólido **a partir de fora** | mortal |
| Earth Treasury Flower Gu | — | Plantada, sela e conserva outro Gu num "coração de flor" | mortal |
| Earth Vein Gu | 7 | terra | imortal |
| East Window Gu | 4 | Joaninha-arquivo de grandes volumes de informação | mortal |
| Eat Fragrance | 6 | comida | imortal |
| Eat Strength | — | Converte materiais em ganho gradual de marcas de lei | imortal |
| Eating One's Words Gu | — | Anula o juramento acima | mortal |
| Edge Gu | 7 | gume | imortal |
| Effort Gu | — | Garante um resultado a qualquer esforço | mortal |
| Eighty-Eight True Yang Building | 8 | múltiplo | imortal |
| Electric Brain Gu | — | Modificador de golpes de armadura | mortal |
| Embroidered Tower | 8 | — | imortal |
| Emotion Poetry Gu | 4 | Armazena emoções | mortal |
| Essence Iron Bone Gu | 4 | Esqueleto duas a três vezes mais firme que o do Iron Bone | mortal |
| Estrus Gu | — | Pó que induz cio em massa | mortal |
| Eternal Gu | 10 (rumor) | Rank 10 lendário | imortal |
| Eternal Yacht | 8 | tempo | imortal |
| Everlasting | — | Fixa uma transformação permanentemente | imortal |
| Expand Space | — | Abre acesso a terras abençoadas | imortal |
| Expend Strength Gu | — | Dobra o gasto de estamina dos inimigos ao se moverem | mortal |
| Extreme Past | 8 | A vontade do usuário observa qualquer evento já ocorrido | imortal |
| Fallen Flower Hall | 7 | madeira | imortal |
| False Emotion Fake Will Gu | 6 | Fabrica amor verdadeiro falso | imortal |
| Fan Wind Gu | 7 → 8 | vento | imortal |
| Fate Armor Gu | 8 | Armadura de luz que resiste a feras imemoriais | imortal |
| Fiery Claw Gu | 3 | Garra de fogo para corpo a corpo | mortal |
| Fiery Snake Gu | 4 | Serpentes de fogo grandes, controláveis uma a uma | mortal |
| Fifteen Year Lifespan Gu | — | Soma quinze anos de vida | mortal |
| Fight Gu | 7 | Núcleo de golpes de combate e de escravização pós-vitória | imortal |
| Fire Cape Gu | 5 | Envolve o corpo em chamas intimidantes | mortal |
| Fire Dragon Gu | 4 | Dragão de fogo | mortal |
| Fire Pellet Gu | 3 | Bolas de fogo | mortal |
| Fire Pupil Gu | 4 | Incendeia aquilo que o usuário mirar | mortal |
| Five Stars Aligned Gu | 5 | O topo da série de amplificação | mortal |
| Fixed Immortal Travel Gu | 6 → 7 | Teleporte global | imortal |
| Fixed Luck (Stubborn + Main) | — | Estabiliza a própria sorte contra vínculos assimétricos | imortal |
| Fixed Space Gu | — | Força todo teleporte da área a chegar num único ponto pré-fixado | imortal |
| Flame Heart Gu | 3 | Aloja-se no coração do usuário e fortalece os outros Gu de fogo | mortal |
| Flame Stomach Gu | 3 | Defesa térmica | mortal |
| Flash Blink Gu | 1 | Explosão de luz branca que anula furtividade por sombra em área | mortal |
| Flash Bug Gu | 5 | Teleporte de esquiva de cerca de quinhentos passos | mortal |
| Flash of Inspiration Gu | 3 | Insight súbito | mortal |
| Flower Boar Gu | 1 | Força de javali por dez respirações | mortal |
| Flowerbud Gu | 2 | Flor-cofre | mortal |
| Flying Bear Phantom Gu | 6 | Transforma o portador no fantasma da fera | imortal |
| Flying Bear Strength | 6 | Concede força de urso voador | imortal |
| Flying Smoke Gu | 5 | Voo | mortal |
| Flying Zombie Gu | 5 | Primeiro estágio voador da linha | mortal |
| Footless Bird | 3 | Ave óssea sem pernas que voa milhares de li | mortal |
| Forceful Refinement | 8 | Refina à força os Gu Imortais de quem invadir a área | imortal |
| Formation Chart Gu | — | Registra as informações de uma formação | mortal |
| Formation Flag | 7 | Guarda uma formação já montada e permite remontá-la em outro lugar | imortal |
| Formation Heart Gu | 1 | Núcleo universal em torno do qual os demais Gu de uma formação se orga | mortal |
| Formation Plate Gu | — | Monta a formação automaticamente a partir dos Gu fornecidos | mortal |
| Formation Spirit | — | Gera uma inteligência que gerencia a formação | imortal |
| Fortitude Gu | 8 | Suprime emoções | imortal |
| Fortune Rivalling Heaven | 8 | Concede sorte permanente rivalizando a do próprio céu | imortal |
| Four Elements Square Regret Blood Refinement Pool | 9 | refinamento | imortal |
| Four Flavors Liquor Worm | 2 | Versão de rank 2 da mesma destilação | mortal |
| Freedom Gu | — | Concede liberdade | mortal |
| Frost Arrow Gu | 4 | Flecha de gelo | mortal |
| Frost Breath Gu | 3 | Sopro congelante que causa queimadura de frio e lentidão | mortal |
| Frost Moon Gu | 3 | Lâmina lunar gélida que aplica lentidão | mortal |
| Fuel Oil Gu | 3-4 | Espalha óleo inflamável em área | mortal |
| Fur Zombie Gu | 3 | Estágio seguinte da linha zumbi | mortal |
| Galloping Horse Strength Gu | 3 | Força e velocidade de cavalo: trinta por cento a mais em investidas | mortal |
| Gamble Gu | — | Produz um número aleatório e o vencedor leva tudo | imortal |
| Gather Light Gu | 4-5 | Concentra luz; peça de composição | mortal |
| Ghost Fire → Ghost Flame → Ghost Blaze Gu | 2-4 | Cadeia evolutiva de fogo-fantasma azulado e gélido | mortal |
| Ghost Official Garment | — | Veste de alma | imortal |
| Giant Mountain Puppet Gu | 5 | Transforma o usuário num títere de rocha de até dezoito metros | mortal |
| Golden Aurora Gu | 4 | Concede voo | mortal |
| Golden Breeze Gu | 4 | Cura de alto nível | mortal |
| Golden Moon Gu | 3 | Lâmina dourada de cerca de um metro | mortal |
| Golden Steel Tendon Gu | — | Versão dourada e superior do anterior | mortal |
| Gourmet Food Box Gu | 5 | Preserva pratos prontos | mortal |
| Graceful Chaotic Duel Stage | 7 | tempo | imortal |
| Great Thief Gu | 7 | O Gu central do caminho do roubo | imortal |
| Green Mountain Remains Gu | 4 | Protege o Gu-núcleo quando um refino fracassa | mortal |
| Groundmat Grass Gu | — | Induz sono instantâneo em seres vivos | mortal |
| Guts Gu | — | Fortalece a fundação da alma | mortal |
| Habitual Strength Gu | 4 | Acumula força durante o combate sem exigir imobilidade | mortal |
| Hard Liver Gu | 6-8 | Energia contínua sem necessidade de descanso | imortal |
| Hatred Gu | 8 → 9 | Ódio encarnado | imortal |
| Heal Injury | 8 | O Gu puro do caminho do homem | imortal |
| Heart Blood Gu | 7 | Emite um batimento que sincroniza o de quem o ouve | imortal |
| Heart Engraved Gu | 1-5 | Grava permanentemente uma receita ou informação na memória | mortal |
| Heart Sound Gu | 2 | Comunicação mental a cem passos | mortal |
| Heaven Overseeing Tower | 9 | investigação | imortal |
| Heaven Qi Gu | 8 | Libélula de oito pares de asas | imortal |
| Heaven's Envy Gu | 7 | Amplifica calamidades, mirando preferencialmente os mais talentosos 🔒 | imortal |
| Heaven's Rage | — | Da mesma família 🔒 | imortal |
| Heaven's Sorrow | — | Da mesma família 🔒 | imortal |
| Heavenly Birth Gu | — | Revive o próprio usuário 🔒 | imortal |
| Heavenly Essence Treasure Imperial Lotus | 6 → 9 | recursos | imortal |
| Heavenly Mugwort Gu | 3 | Corpo duro como jade branco; reduz dano cortante | mortal |
| Heavenly Pool | 8 | cura | imortal |
| Heavenly Secret Gu | 7 → 9 | Obtém a resposta do céu sobre qualquer evento | imortal |
| Heavenly Web Gu | 8 → 9 | Aranha de cristal cuja teia prende 🔒 | imortal |
| Hints and Clues Gu | 5 | Rastreia Gu previamente marcados | mortal |
| Horizontal Charge Gu | 3 | Variante lateral do anterior | mortal |
| Human Qi Gu | 7 → 8 | Coleta e purifica o qi humano alheio para somar ao próprio na ascensão | imortal |
| Human Torch Gu | 4 | O corpo inteiro do usuário vira fogo vivo | mortal |
| Humility Gu | — | Faz o portador sentir que sempre lhe falta conhecimento | mortal |
| Hundred Ghost Night Travel Gu | 5 | Cem fantasmas que destroem almas | mortal |
| Hundred Li Eye | — | Visão de longuíssimo alcance | mortal |
| Ice Edge Gu | 2-3 | Lâminas de gelo arremessáveis | mortal |
| Ice Heart | — | gelo | imortal |
| Ice Soul Immortal Gu | 6 | Aranha branca | imortal |
| Iceblade Gu | 3 | Lâmina de gelo de cerca de um metro e setenta, autorregenerativa | mortal |
| Illusory Moon Gu | 3 | Clone-sombra para distração | mortal |
| Imitation Gu | 8 | Deixado perto de qualquer Gu Imortal, transforma-se nele | imortal |
| Immediate Success Gu | — | Eleva a taxa de sucesso de um refino | mortal |
| Immortal Slave | 6 | Acrescenta marcas de escravização ao usuário | imortal |
| Impermanence Bone Gu | 4 | Ossos que ampliam a capacidade do corpo de conter uma alma poderosa | mortal |
| Inch of Time | 1-5 | Paga o "pedágio de tempo" no lugar do tempo de vida do usuário | mortal |
| Injury Mark Gu | — | Converte automaticamente o dano recebido em marcas acumuláveis | imortal |
| Innocent Mushroom | — | Purifica o ar; serve de mobília viva | mortal |
| Instant / That Time | 7-8 | Par que permite teleporte por compressão temporal | imortal |
| Intuition Gu | — | Insights súbitos de investigação | mortal |
| Investigative Gu | 5 | Vê o "qi de talento" sobre a cabeça de mortais e de Mestres Gu | mortal |
| Iron / Bronze / Stone Skin Gu | 1 | Variações do anterior, com tonalidades diferentes | mortal |
| Iron Bone Gu | 3 | Ossos pretos permanentemente duros como ferro | mortal |
| Iron Cabinet Gu | — | Barreira de contenção de mil metros, ou cofre de ferro instantâneo | mortal |
| Iron Thorn Thistle Gu | 3 | Veste de espinhos: defesa somada a arma contra quem ataca desarmado | mortal |
| Iron Wall Gu | 6 | metal | imortal |
| Ivory Armor Gu | 4 | Armadura que cresce e se regenera ao longo da batalha | mortal |
| Jin Strength Gu | 1 | Soma um jin (~600 g) de força | mortal |
| Jumping Zombie Gu | 4 | Estágio seguinte | mortal |
| Jun Strength Gu | 3 | Soma um jun (trinta jin) de força | mortal |
| Justice Gu | — | Golpe coletivo de retidão | mortal |
| Kill | 8 | matança | imortal |
| Kindness Thought | 6 | Combustível de dedução | imortal |
| Landscape As Before | 6 → 8 | Restaura o terreno ao estado anterior a uma calamidade | imortal |
| Large Belly Frog | 2 | Barriga-armazém que engole e vomita itens | mortal |
| Lava Explosion Gu | 3 | Bola de lava | mortal |
| Learning Gu | 8 | Aprendizado | imortal |
| Letter Gu (série) | 3-5 | Correio mágico | mortal |
| Letter Seal Gu | 7 | Sela outro Gu Imortal dentro de uma rocha | imortal |
| Life-Saving Recovery Pill | — | Revive mesmo a partir de destruição total, em poucas respirações | mortal |
| Life-preserving Jade Burial Gu | 5 | Animação suspensa dentro de um caixão de jade quase inquebrável | mortal |
| Lifespan Gu | — | Estende o tempo de vida em cem ou quinhentos anos, conforme o grau | mortal |
| Light Gu | 9 | luz | imortal |
| Light Source Gu | — | Reduz à metade o custo de essência dos outros Gu de luz | mortal |
| Lightning Eye Gu | 3 | Vê através de qualquer furtividade | mortal |
| Lightning Gu | 8 → 9 | raio | imortal |
| Longevity Edict | — | Token que viaja sozinho de tribo em tribo transmitindo ordens | imortal |
| Longevity Gu | — | Rejuvenesce quem o consome | mortal |
| Looking Back | — | Observa eventos passados pelo Rio do Tempo | imortal |
| Love Life Separation Gu | 2 | Unhas de cerca de cinquenta centímetros que injetam veneno fatal ao me | mortal |
| Luck Plan | 6 | Otimiza uso de recursos e tática de batalha | imortal |
| Luck Suppression Heavenly Palace | 8 | sorte | imortal |
| Main Luck | — | Formaliza o papel de "sorte principal": ganha mais, perde menos | imortal |
| Malicious Thought Gu | 1-5 | Combustível de dedução especializado em tramar | mortal |
| Man As Before | 5 | Restaura terceiros a um estado passado | mortal |
| Man Triumphing Heaven Gu | 5 | Desperta a abertura de um mortal sem nenhum talento | mortal |
| Man-beast Life Burial Gu | 3 | Força o avanço de um rank inteiro | mortal |
| Master-Servant Gu | — | Vínculo formal de senhor e servo | mortal |
| Mature Bamboo | 6 | madeira | imortal |
| Medicine Fragrance | 8 | comida | imortal |
| Melt Ice | — | gelo | imortal |
| Memory Gu | — | Armazena informação bruta | mortal |
| Memory Thought Gu | 1-5 | Combustível de dedução especializado em memória | mortal |
| Menses Blood Gu | — | Herança verdadeira | imortal |
| Moat Gu | — | Parede de cristal permeável ao redor de uma nascente | mortal |
| Moon Poison Gu | 3 | Lâmina lunar que se dissolve num miasma roxo venenoso, inalado pelo al | mortal |
| Moon Raiment | 2 | Defesa de luz azul-lunar | mortal |
| Moon Scar Gu | — | Lâmina lunar de alcance dobrado, cerca de vinte metros | mortal |
| Moonlight Treasure King Gu | 5 | O ápice da receita de rank 5 do clã | mortal |
| Moonshadow Gu | 4 | Implantado na abertura do alvo, suprime a essência utilizável dele | mortal |
| Moonwhirl Gu | — | Projétil verde de trajetória curva | mortal |
| Mountain As Before | 5 | Reverte o terreno ao estado original | mortal |
| Mountain Pledge Gu | 6 | O mesmo, ancorado a uma montanha | imortal |
| Muddy Gu | mortal | Cria e expande uma poça de lama que prende o alvo | mortal |
| Mudskin Toad | 2 | Sapo de carga | mortal |
| Musician Gu | — | Gu vital que ressoa com o caminho do som | mortal |
| Mutation Gu | 8 | Muta partes do corpo do alvo em plantas e animais | imortal |
| Mutual Sense | — | Percepção mútua entre duas partes | imortal |
| Myriad Age Building | 7 | tempo | imortal |
| Myriad Self Immortal Gu | 7 | Centopeia metálica de dez metros com dez mil pernas | imortal |
| Nine Eyes Liquor Worm | 4 | Versão de rank 4 | mortal |
| Nine Leaf Vitality Grass | 2 | Tatuagem-planta na palma da mão, com nove folhas de cura destacáveis | mortal |
| Nine Leaf Vitality Grass → Wood Charm Gu | 3 | Transformação vegetal progressiva | mortal |
| No Loss Gu | 6 | Teleporta os Gu do dono para longe no instante da morte dele | imortal |
| Normal Gu | — | Restaura o alvo à condição normal | imortal |
| Oil Dragon Gu | 4 | Dragão de óleo | mortal |
| Old Removal Gu | — | Desfaz modificações corporais anteriores | mortal |
| One / Three ("Number Gu") | 7 | Exemplos de uma série potencialmente infinita | imortal |
| One's Own Way Gu | 6 → 7 | Mantém Gu mortais funcionando dentro de território alheio que normalme | imortal |
| Onion Explosion Gu | 2 | Enfurece bestas em massa | mortal |
| Open Door Gu | 5 | Abre a entrada de espaços de herança | mortal |
| Overturn River | — | Vira o curso de rios | imortal |
| Painting Idea Gu | — | Grava cenas na memória permanentemente | mortal |
| Paper Crane Gu | 1-2 | Mensageiro voador que também guia o caminho | mortal |
| Pass Gu | 7 | Barata metálica; núcleo de formações de contenção | imortal |
| Perceivable Dao | 6 | Mede a quantidade exata de marcas de lei de um caminho num corpo ou ob | imortal |
| Permanence | 8 | Núcleo de estruturas de tempo | imortal |
| Pill Refiner Gu | 1-5 | Produz especialistas em refinar Gu de pílula | mortal |
| Pine Needle Gu | — | Chuva de agulhas de pinheiro disparada do cabelo | mortal |
| Pink Boar Gu | 1 | Apenas engorda o usuário | mortal |
| Poem Wall Gu | 7 | Ergue uma parede defensiva a partir de versos recitados | imortal |
| Poison Flower Gu | — | Flores de muralha que envenenam as feridas abertas pelas vinhas | mortal |
| Poison Heart Gu | — | Veneno transmitido por fragrância | mortal |
| Poison Liquid Gu | — | Veneno líquido; par do anterior | mortal |
| Poison Scorpion Gu | 3 | Produz o veneno acima — sua única habilidade é defecar | mortal |
| Police Gate Gu | 1-6 | Portões conectados entre si | mortal |
| Polished Gold Gu | mortal | Aumenta a aptidão do usuário | mortal |
| Possession Gu | 6 | Permite que uma alma possua um corpo novo 🔒 | imortal |
| Prairie Fire Gu | 5 | Incêndio de larga escala | mortal |
| Precaution Gu | 7 | Defesa de primeira linha | imortal |
| Present and Past Pavilion | 7 | tempo | imortal |
| Pride Gu | — | Ocupa espaço mental | mortal |
| Pulling Mountain | — | Ergue montanhas inteiras | imortal |
| Pulling Water Gu | mortal | Puxa e remove volumes enormes de água à distância | mortal |
| Puppet Control Gu | — | Controle de corpos vivos à distância | mortal |
| Purple Smoke Cicada | 5 | Emite fumaça roxa que obscurece uma área inteira de céu e terra | mortal |
| Qi Escape Gu | — | Movimento de altíssimo nível | imortal |
| Qi Flow Gu | 6 | Barata pétrea, mas leve | imortal |
| Qi Luck | — | Núcleo de golpes que repelem atacantes e puxam fugitivos | imortal |
| Quantity Change Gu | 8 | Multiplica a quantidade de um alvo | imortal |
| Rainbow Light Gu | 3 | Transforma o usuário num facho de luz | mortal |
| Red Copper Fire Ant | 6 | Cospe fogo e espinhos | imortal |
| Refinement Cauldron | 8 | refinamento | imortal |
| Region Gu | 8 | Com o Limit Gu, replica o contragolpe das paredes que separam as regiõ | imortal |
| Regret Gu | 8 | Extrai arrependimento infinito de quem o toca sem proteção | imortal |
| Regret Pool | — | tempo/refino | imortal |
| Relic Gu (green copper) | 1 | Consumível que avança um pequeno estágio dentro do rank 1 | mortal |
| Relic Gu (purple crystal) | 5 | O mesmo, para o rank 5 | mortal |
| Relic Gu (red steel) | 2 | O mesmo, para o rank 2 | mortal |
| Relic Gu (white silver) | 3 | O mesmo, para o rank 3 | mortal |
| Relic Gu (yellow gold) | 4 | O mesmo, para o rank 4 | mortal |
| Reminiscence | 6 | Combustível de dedução ligado à memória | imortal |
| Remnant Life Gu | 5 | Ressurreição depois da morte | mortal |
| Reputation Restriction Gu | 7 | Corda que restringe feras | imortal |
| Response Gu | 8 | Emite uma voz | imortal |
| Responsibility Gu | — | O peso que acompanha a liberdade | mortal |
| Responsive Luck | 8 | Sorte responsiva | imortal |
| Return to Childhood Gu | — | Acumula e libera força vital lentamente | mortal |
| Rice Pouch Grass Gu | 1 | Produz arroz dentro de uma bolsa vegetal | mortal |
| Right Gu / Wrong Gu | — | Permitem classificar conhecimento como certo ou errado | mortal |
| River As Before | 5 | O mesmo, para águas artificiais | mortal |
| River Swallowing Toad | 5 | Engole rios inteiros | mortal |
| Rock Skin Gu | — | Pele de pedra espessa nos braços, resistente a corte | mortal |
| Rules Gu / Regulations Gu / Practice Gu | — | Trio lendário que, no mito, criou o gelo flutuante original | mortal |
| Running Corpse Gu | 2 | Transforma um cadáver num zumbi capaz de **evoluir** por estágios de c | mortal |
| Sandpit Gu | 1 | Cria um buraco de areia instantâneo no chão | mortal |
| Scorpion Faeces Gu | 2 | Veneno diferente para cada indivíduo | mortal |
| Sea Oath Gu | 6 | Juramento ancorado a um mar físico | imortal |
| Second Aperture Gu | 6 | Abre uma segunda abertura | imortal |
| Second Aperture Gu (série) | 1-5 | Cria uma **segunda abertura** do rank correspondente | mortal |
| Self Gu | — | Representa a individualidade do portador; é extremamente pequeno | mortal |
| Self Love | 7 | Faz a vontade dentro de um Gu roubado amar a si mesma | imortal |
| Self Strength | 6 | Núcleo do golpe de mãos gigantes | imortal |
| Serious Gu / Learning Gu / Talent Gu | — | Reconhecem o verdadeiro significado, convertem conhecimento em entendi | mortal |
| Seven Fragrances Liquor Worm | 3 | Versão de rank 3 | mortal |
| Shadow Follower Gu | 2 | Movimento pelas sombras | mortal |
| Shadow Puppet Gu | — | Gu vital que ressoa com o caminho da sombra | mortal |
| Shared-sense Gu | — | Selo invisível implantado às escondidas, que transmite o ambiente ao r | mortal |
| Sight Blow Gu | 3 | Ataque à alma pelo olhar, a cerca de trezentos passos | mortal |
| Sight Light Gu | — | luz | imortal |
| Silent Step Gu | — | Oculta o som dos passos | mortal |
| Single Gate Poison Gu | — | Mata a vítima em sete dias, que "vira pus e sangue" | mortal |
| Sky Granary Gu | 3 | Armazenamento de grande capacidade | mortal |
| Sleep Lurk Gu | 4 | Ocultação equiparável à de rank 5 | mortal |
| Slow Slicing Gu | — | Remove as impurezas da alma | mortal |
| Slumbering Lightning Python | 8 | Tritura materiais imortais em pó finíssimo | imortal |
| Small (Big to Small) | 7 | Campo que encolhe e enfraquece qualquer ataque que se aproxime | imortal |
| Small Soul Gu | 1 | Veículo de "vontade" para investigar sem expor a consciência do dono | mortal |
| Smell Lock Gu | — | Ocultaria o odor corporal | mortal |
| Smelly Fart Fat Worm | 1 | Gu comum de efeito irrelevante | mortal |
| Smelly Fart Fatworm | — | Transporta fertilizante congelado | mortal |
| Snack | 6 | comida | imortal |
| Snake Tongue Gu | 2 | Radar térmico de curto alcance | mortal |
| Sneak Attack Gu | 2 | Fantasma de bebê azul, velocíssimo, que atravessa defesas físicas e at | mortal |
| Snow Fairy Gu | 3 | Variante feminina da mesma transformação | mortal |
| Soldier / Sergeant / Lieutenant / Captain Gu | mortal | Hierarquia militar completa | mortal |
| Sole Blade Gu | 6 | lâmina | imortal |
| Soul Beast Token | 8 | Escraviza feras de alma, inclusive imemoriais | imortal |
| Soul Howl Gu | 7 | Sacode almas inimigas à distância | imortal |
| Soul Language Gu | — | Permite entender a fala de almas sem corpo | mortal |
| Soul Lantern Gu | — | Verifica à distância se um membro do clã teve a alma alterada | mortal |
| Soul Search Gu | 3 | Lê as memórias contidas numa alma | mortal |
| Soul Shackle | — | Arma que se manifesta na mão esquerda da alma | imortal |
| Soul Shaking Flag | — | Arma que se manifesta na mão direita da alma | imortal |
| Sound Amplification Gu | — | Projeta a voz sobre um campo de batalha inteiro | mortal |
| Sovereign Immortal Fetus Gu | 9 | Fabrica um corpo compatível com a alma já existente do cultivador 🔒 | imortal |
| Space Escape Gu | — | Deslocamento — em tese | imortal |
| Space Piercing Gu | — | Teleporte de centenas de passos, rasgando o espaço | mortal |
| Space Thought Gu | 5 | Pensamentos criptografados, ilegíveis a leitores de mente | mortal |
| Space Travel | 7 | Esfera de jade com asas | imortal |
| Spirit Peach Gu | 5 | Cura de renome regional | mortal |
| Spring Gu | 8 | Traz a primavera a uma área: derrete gelo, faz brotar | imortal |
| Star Constellation Chessboard | 8 → 9 | sabedoria | imortal |
| Star Dart Gu | — | Projétil estelar | mortal |
| Star Thought Gu | 1-5 | O combustível de dedução mais eficiente da série | mortal |
| Stargate Gu | 5 | Portal entre as cinco regiões, aberto por luz estelar | mortal |
| Steal Life Gu | 6 → 8 | Rouba tempo de vida de todos os tocados | imortal |
| Stealth Rock Gu | 1 | Invisibilidade do corpo | mortal |
| Steel Mane Gu | 3 | Endurece o cabelo, servindo de ataque e de defesa | mortal |
| Steel Tendon Gu | — | Converte os tendões do usuário em tendões de aço | mortal |
| Steel Vine Gu | — | Vinhas de aço embutidas em muralhas | mortal |
| Store Strength Gu | 3 | Acumula força ao longo do combate e a libera em picos | mortal |
| Stream Gu | — | Gu de assinatura de um clã de água | mortal |
| Strength of Ten Jin Gu | 2 | Soma dez jin de força | mortal |
| Strength of Ten Jun Gu | 4 | Soma dez jun (trezentos jin) de força | mortal |
| Strength of a Thousand Jun | 6 | Soma mil jun de força ao usuário | imortal |
| Strong Gu | — | Recusa engolir a derrota | mortal |
| Sub Luck | — | Formaliza o papel oposto: ganha menos, perde mais | imortal |
| Summary Gu | — | Deduz o resumo geral de uma informação complexa | imortal |
| Summer Gu | 8 | Força floração fora de época | imortal |
| Suppress Space Gu | 7 | Congela a força de espaço numa área ampla | imortal |
| Suppression | 8 | Núcleo de formações que selam trechos do Rio do Tempo | imortal |
| Swallow Fire Gu | 4 | Armazenamento que engole o fogo alheio | mortal |
| Swamp Gu | — | Transforma o chão em lama | mortal |
| Swimword Gu | 1 | Texto mutável em estandartes | mortal |
| Sword Legged Dragon Centipede | 7 | espada | imortal |
| Sword Qi Gu | 8 | espada | imortal |
| Sword Tongue Gu | — | Dispara luz de espada pela ponta da língua | imortal |
| Territory Gu | 3-4 | Plantado no solo, afirma e controla domínio territorial | mortal |
| Thieves Den | pico | roubo | imortal |
| Third Watch Gu | 5 | Triplica o tempo pessoal do usuário | mortal |
| Thought Expelling Pavilion | 7 | sabedoria | imortal |
| Thousand Li Earthwolf Spider | 5 | Montaria escavadora | mortal |
| Thread Trace Gu | 5 | Revela marcas de lei residuais | mortal |
| Three Star Cave | 3 | Árvore-loja de três andares que cresce instantaneamente | mortal |
| Thunder Shield Gu | 3 | Escudo semicircular de raio | mortal |
| Tiger Poison Gu | 3 | Escorpião preto que emite veneno de tigre | mortal |
| Time Anchor | 6 | Ancora um ponto do tempo para retorno posterior | imortal |
| Time Concealment | 7 | Oculta rastros | imortal |
| Time Luck | 6 | Compra sorte pagando com tempo | imortal |
| Time Needle | 7 | Dispara agulhas finíssimas | imortal |
| Treasure Brass Toad | — | Montaria blindada | mortal |
| Treasure Light Gu | 8 | Mede o valor de qualquer item | imortal |
| True Sight Gu | — | Contramedida contra furtividade | mortal |
| Turn Sand Gu | — | terra | imortal |
| Tusita Flower | 3 | Armazém alojado na língua do usuário | mortal |
| Unravel Mystery | 6 | Deduz rastros de heranças perdidas | imortal |
| Vajra Thought Gu | 5 | Milhares de "pensamentos" em forma de casco dourado que interceptam at | mortal |
| Vertical Crash Gu | 3 | Investida em linha reta de até cem passos, com a força do próprio corp | mortal |
| Vine Information Gu | 1 | Registro público de vitórias e derrotas de arena | mortal |
| Vitality Leaf | 1 | Cura instantânea | mortal |
| Vivid Recollection | — | Par do anterior na mesma dedução | imortal |
| Water Armor Gu | — | Defesa especializada em combate aquático | mortal |
| Water Curtain Skyflower Gu | 4 | Esfera que sela o interior e o exterior ao mesmo tempo | mortal |
| Water Harmony Gu | 7 | água | imortal |
| Water Image Gu | 4 | Dublê líquido realista | mortal |
| Water Pavilion | 7 | água | imortal |
| Water Prison Gu | 3 | Bola de água que aprisiona o alvo | mortal |
| Water Refinement | 8 | Converte marcas de lei em "água de refino" | imortal |
| Weak Chicken Gu | 8 | Concede força | imortal |
| Wealth Gu | 5 | Consumível que se transforma em **qualquer material Gu de rank 5** | mortal |
| Whale Enslavement Gu | — | Controla baleias-voadoras-azuis | mortal |
| White Lotus Giant Silkworm Gu | — | Base de formações de alma | mortal |
| White Noodle Immortal Ant | 6 | Formiga-rainha que produz rapidamente as demais castas | imortal |
| Wild Immortal Gu | — | Categoria, não Gu individual: Gu Imortal **nunca refinado**, achado em | imortal |
| Winding Light Platform | 7 | luz | imortal |
| Wine Drinker Gu | — | Equivalente imortal da série de Gu de profissão | imortal |
| Wine Sack Flower Gu | 1 | Secreta néctar e vinho de dentro de uma flor | mortal |
| Winter Gu | 7 | Pupa que emite rajadas de ar frio | imortal |
| Wisdom Obstacle | 7 | Implanta obstáculos na mente do alvo | imortal |
| Wisdom Sword Gu | 8 | Arma anti-sabedoria | imortal |
| Wish Power Gu | mortal | Poder de desejos coletivos acumulado por gerações | mortal |
| Wolf Care Gu | — | Cura em massa de lobos, e compartilha a visão de uma fera sob comando | mortal |
| Wolf Enslavement Gu | 1-5 | Fumaça que escraviza lobos | mortal |
| Wolf Howl Gu | 4 | Fortalece a matilha inteira | mortal |
| Wolf Soul Gu | 3-5 | Refina a alma rumo à "alma de homem-lobo" | mortal |
| Wolf Totem Gu | 5 | Guarda lobos de elite como tatuagens invocáveis | mortal |
| Wood Charm Gu | 3 | Transforma o usuário num espírito de árvore, que absorve essência do a | mortal |
| Wood Sprout | — | madeira | imortal |
| Worldly Wave Trace | 6 | água | imortal |
| Years Flow Like Water | 8 | Produz Gu de ano continuamente, na proporção da essência gasta | imortal |
| Yellow Camel Longhorn Beetle Gu | 1 | Resistência por quinze minutos | mortal |
| Yellow Sand | 6 | terra | imortal |
| Yes or No | — | Extrai respostas binárias do céu 🔒 | imortal |
| Yin Cloud Gu + Yang Cloud Gu | 3 | Par de nuvens que geram raios com lei da destruição | mortal |
| Yin Yang Rotation Gu | 4 | Troca o sexo do corpo do usuário; a versão Yin ainda cura estados de q | mortal |
| Zombie Heart Gu | 3 | Coração de bronze de sete buracos | mortal |
