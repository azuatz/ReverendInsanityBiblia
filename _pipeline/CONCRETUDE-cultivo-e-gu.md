---
tags:
  - pipeline/relatorio
status: concluido
---

# Passe de concretude física — Cultivo e Gu

Relatório do passe pedido pelo usuário: as notas explicavam bem as **regras** e mal as
**coisas**. A designer nunca leu a obra e não sabe que tamanho um Gu tem, se pega na mão,
como é a abertura por dentro, se o uso é físico ou mental. Este passe foi buscar no
texto-fonte as descrições sensoriais e acrescentá-las às seis notas.

**Método:** busca direta no texto-fonte (`/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/`,
`grep -i`, com atribuição de capítulo por varredura de `## Chapter N`). Nada foi inventado:
toda frase acrescentada tem passagem localizada, e onde a obra não descreve, a nota **diz
que a obra não informa** — o que já avisa a designer de que ali ela pode desenhar como quiser.

**Estado do passe.** Concluído nas seis notas. A maior parte da escrita foi feita em sessões
anteriores, que bateram no limite de tokens antes de redigir este relatório; esta sessão
**conferiu no texto-fonte tudo o que já estava escrito**, fechou as lacunas que sobraram e
documentou o conjunto. As seções abaixo são o registro final: o que cada nota ganhou, de onde
veio, o que a obra **não** responde e as decisões tomadas.

**Uma nota de método que vale para o vault inteiro.** A regra "nunca afirmar uma negativa sem
grep" foi aplicada literalmente: cada frase do tipo "a obra não informa" que aparece nas seis
notas foi testada com busca no texto-fonte antes de ficar lá. As buscas que sustentam cada
negativa estão listadas nas seções por nota, com o padrão usado. Nenhuma delas veio de wiki nem
de memória.

---

## 1. `01 - Cultivo/02 - Abertura.md`

### O que a nota ganhou

**Seção nova "Por dentro: o que o cultivador vê quando 'olha' para a própria abertura"** — a
paisagem interior inteira, mais um diagrama Mermaid marcado como leitura nossa.

| Pergunta do usuário | Resposta que entrou | Fonte |
|---|---|---|
| Que tamanho tem? | A obra é deliberadamente evasiva, e a evasão **é** a resposta: "infinitamente grande e ao mesmo tempo infinitamente pequena". A única medida citada é burocrática — o ancião anota "Mar Primordial medindo seis por seis", sem unidade e sem explicação | cap. 4, 6, 10 |
| Onde fica, no corpo? | Três polegadas abaixo do umbigo, **entre os dois rins**; não divide espaço com os órgãos e não aparece em dissecação | cap. 5, 6 |
| Como o cultivador percebe? | Olhos fechados, atenção escorregando para dentro. Não é contemplativo: é conferir um painel, e leva um instante — feito montado, em viagem e entre dois lances de luta | cap. 34, 106, 122, 437 |
| A parede tem espessura, cor, textura? | Sim, e é a **ficha de progressão**: luz (lisa, sem impurezas) → água (visivelmente mais grossa, com ondulações de luz correndo e piscando sobre ela) → pedra → cristal (branco, sólido) | cap. 50, 86, 115, 212 |
| O mar sobe e desce visivelmente? | Sim, é água literal: ondas, superfície de espelho em repouso, densidade, brilho metálico. Absorvendo pedra primordial o nível sobe "numa velocidade visível a olho nu" e **para de repente** no teto da aptidão, com espaço sobrando | cap. 6, 10 |
| Alguém de fora vê a abertura de outro? | **Não.** Nem por observação nem por dissecação. O único acesso é a inspeção por toque — e ela é o maior tabu social do mundo | cap. 86, 124, 153 |
| O que muda a cada rank? | Duas coisas, e só duas: o **material da parede** (por estágio) e a **família de cor do mar** (por rank). Fora isso a abertura não muda de aparência | cap. 26, 212 |

**Acrescentado nesta sessão:** a ruptura de rank ganhou **imagem e som**. As rachaduras se cruzam
sobre o cristal branco translúcido; se o cultivador para de bater, **elas se fecham sozinhas e o
cristal sara** (por isso a ruptura exige impacto explosivo, não paciência); quando a parede cede,
ela **estoura com um estrondo alto ouvido de dentro**; os estilhaços caem no Mar Primordial,
**levantam ondas ao bater na água** e viram pontinhos brancos que se apagam. Fontes: cap. 90, 92,
152. O `fontes` do frontmatter ganhou o cap. 90.

### O que a obra não responde

- **Tamanho absoluto.** Não há centímetros, não há litros, e a notação "seis por seis" nunca é
  explicada. A nota diz isso com todas as letras e converte a lacuna em regra útil: a abertura só
  tem tamanho **relativo**, medido em porcentagem de si mesma — que é por que o sistema fala em
  "44% de essência" e nunca em "quatro litros".
- **Onde exatamente os Gu ficam pousados no "céu" interno**, se há luz ambiente lá dentro, se há
  som. Nada disso é descrito.

### Decisões

- O diagrama Mermaid foi marcado, logo abaixo do bloco, como **leitura nossa**: a obra não
  apresenta esquema nenhum da abertura.
- A evasão da obra sobre tamanho foi tratada como **dado**, não como falha. Era a decisão mais
  arriscada do passe e é a que mais serve à designer: ela sabe que pode desenhar a escala como
  quiser sem contradizer nada.

---

## 2. `01 - Cultivo/03 - Aptidão.md`

### O que a nota ganhou

**Seção nova "A cerimônia como cena"**, com seis subseções — o lugar, o procedimento, o que a
plateia vê, o que a pessoa sente, quanto tempo leva, o registro — mais "as proporções" e "como se
frauda, fisicamente". Era o pedido mais explícito do usuário ("conte isso como cena, não só como
regra") e é a parte do passe que mais mudou de tom.

| Pergunta | Resposta | Fonte |
|---|---|---|
| Onde acontece? | Caverna subterrânea sob o pavilhão do clã. Estalactites cintilando em cores de arco-íris que jogam luz de néon nos rostos; várias centenas de passos até escurecer; um **rio subterrâneo de uns nove metros** que emite luz azul fraca no escuro, água cristalina, rasa até os joelhos e **gelada**. Na outra margem, o mar de orquídeas-lua: pétalas azuis e rosa em forma de lua crescente, miolo brilhando como pérola | cap. 4, 5 |
| Qual é o procedimento? | O ancião chama os nomes de uma lista e dá a instrução inteira numa frase: atravesse o rio e caminhe o mais longe que conseguir | cap. 4, 5 |
| O que a pessoa sente? | Pressão de parede invisível a partir do primeiro passo em terra; pontinhos de luz subindo das flores e entrando no corpo; a bola se juntando **três polegadas abaixo do umbigo, entre os dois rins**; a pressão afrouxando a cada passo e endurecendo de novo | cap. 5 |
| E no desfecho? | Um estalo que só ela ouve; pelos arrepiados, poros fechados, mente esticada; depois a mente apaga, o corpo amolece "como se caísse dentro de uma nuvem", os poros reabrem e ela está **encharcada de suor**. Parece durar muito e dura pouquíssimo | cap. 5 |
| O que os outros veem? | O corpo **banhado na luz branca dos Hope Gu**, que sobe e desce conforme ele avança — e é isso que entrega o resultado antes do anúncio. **Não veem o desfecho**: a explosão acontece só por dentro | cap. 5, 6 |
| Quanto tempo leva? | Mais de cem jovens numa única manhã, com **metade já tendo atravessado depois de uma hora** — cerca de um minuto por pessoa | cap. 4 |
| E depois? | O ancião **põe a mão no ombro, fecha os olhos e se concentra** alguns segundos, depois anota nome, grau e a medida do Mar Primordial. O selo definitivo vem **sete dias depois**, quando a essência coagula | cap. 4, 5 |

### O que a obra não responde

- **Quanto tempo passa entre o estouro e a pessoa voltar a si** — só que "parece longo e é
  curtíssimo".
- **Qual substância é passada na pele para fraudar.** A obra descreve a fraude e os sinais dela
  (movimentos rígidos, cor de pele fora do normal) mas **não nomeia o produto**. A nota diz
  isso e libera a mesa explicitamente.
- **Se a conversão passos → porcentagem é proporcional dentro de uma banda.** Não é dedutível: as
  bandas de passos têm dez unidades e as de porcentagem têm vinte pontos. A nota já resolvia isso
  antes deste passe, com a recomendação de tratar os passos como o rótulo público e sortear a
  porcentagem dentro da banda.

### Decisões

- A cena foi escrita **do ponto de vista de quem atravessa e de quem assiste ao mesmo tempo**,
  porque a informação assimétrica entre os dois é o que a torna jogável — e isso virou o bloco
  "Para o design" dos três canais desencontrados (a luz que todos veem, a contagem que só o
  ancião anuncia, a inspeção que só ele faz).
- O "cerca de um minuto por pessoa" ficou marcado no corpo do texto como **conta nossa** a partir
  dos números da obra, não como dado dela.

---

## 3. `01 - Cultivo/04 - Essência Primordial.md`

### O que a nota ganhou

**Seção nova "Como ela é: a fisicalidade da essência"**, com "Quando ela acaba" e "Como ela
volta".

| Pergunta | Resposta | Fonte |
|---|---|---|
| Estado: líquida, gasosa, luminosa? | **Líquida, literalmente água.** Mar com ondas, superfície de espelho em repouso, densa, com brilho metálico. Cada gota é uma porção. Essência refinada para estágio mais denso **afunda e forma camada no fundo** — comporta-se como líquido de densidade diferente | cap. 6, 10, 34 |
| Brilha? | Sim, emite luz da própria cor. Um Gu mergulhado nela é visto do fundo "como uma lâmpada" | cap. 6, 10 |
| É visível ao sair do corpo? | Sim, e a forma depende do volume: **jato de névoa colorida** (volume grande, envolve o alvo), **nuvem/neblina escorrendo até a marca na pele** (médio), **fio finíssimo quase impossível de ver** (pequeno, ou usuário de rank alto) | cap. 22, 94, 152 |
| O que se sente quando está acabando? | Em menos de três minutos despejando essência num Gu, **o rosto empalidece** e vem "uma fraqueza que sobe rapidamente até o coração". Sem dor, sem tontura, sem visão turva — exaustão de quem doou sangue | cap. 10 |
| Como se percebe que está acabando? | **Não se percebe automaticamente.** Não há barrinha na cabeça: o Mestre Gu vira a atenção para dentro e olha o mar. As falas da obra são literalmente leituras de painel — "gastei 20% da minha essência" | cap. 106, 122 |
| Como se recupera, e o que se sente? | Natural: passiva, lenta, **nada se vê e nada se sente**. Por pedra: **pega a pedra na mão, fecha os olhos** e extrai; por dentro o nível sobe a olho nu | cap. 10, 34 |

**Acrescentado nesta sessão — duas coisas.**

**(a) O cheiro tem uma exceção canônica.** A nota dizia, corretamente, que a essência em estado
normal não tem cheiro, temperatura nem som registrados. Faltava o outro lado: a obra mostra **uma
vez** um Gu que desce pela garganta do próprio dono, entra na abertura como jorro de água preta e
vermelha e **converte o mar inteiro de uma vez** — a essência vira um preto-avermelhado sinistro
e fica **cheia de cheiro de sangue** (cap. 152). Ou seja: a essência não tem cheiro *próprio*, mas
é matéria e aceita ser tingida e perfumada, o que é exatamente coerente com a regra de que
essência alheia impregna as paredes. Para a mesa, isso autoriza narrar qualquer alteração mágica
da reserva como mudança **visível e olfativa do líquido**, e não como um número mudando de valor.

**(b) O tempo de recarga escala com o rank, e a obra dá os dois números.** No rank 1, encher do
quase-zero até o teto de 44% leva **cerca de meia hora** — número que a obra dá duas vezes, nas
mesmas palavras (cap. 10, 34). E ela enuncia a regra em voz de narrador: no rank 1 e 2 a recarga
por pedra era "bem perceptível", mas **do rank 3 em diante são precisas mais pedras e mais tempo**
para o mesmo serviço; o único cronômetro nesse patamar é um retoque parcial no meio de uma
batalha, que levou **oito ou nove minutos** (cap. 167). Os dois números não se contradizem — um é
tanque cheio de rank 1, o outro é remendo de rank 3 — e juntos dão a ordem de grandeza que a mesa
precisa: recarregar é assunto de **dezenas de minutos**, nunca de segundos. O `fontes` ganhou o
cap. 167.

### O que a obra não responde

- **Cheiro, temperatura e som da essência em estado normal.** Verificado com buscas por
  `primeval essence` cruzado com `smell|scent|odor|fragran|stench|aroma`, com
  `warm|hot|cold|chill|icy|burn` e com `sound|noise|hum|silent|whistl`: nenhuma ocorrência
  descreve a essência sendo cheirada, sentida como quente ou fria, ou ouvida. Os aromas que
  aparecem pertencem aos **Gu** (o verme do licor exala vinho), não à energia.
- **Peso.** Não há nada.

### Decisões

- A ausência foi transformada em permissão explícita no corpo da nota: "se a mesa quiser dar à
  essência um cheiro ou uma temperatura de fábrica, está inventando — o que é permitido, desde
  que declarado". É o padrão que o passe inteiro adotou para lacunas.
- O achado do cap. 152 foi escrito como **complemento** da negativa, não como revogação dela — a
  distinção entre "não tem cheiro próprio" e "não pode adquirir cheiro" é justamente o tipo de
  precisão que evita que a designer conclua a coisa errada.

---

## 4. `02 - Gu/02 - O que é um Gu.md` — o mais importante da lista

### O que a nota ganhou

**Seção nova "Como um Gu é, fisicamente"**, com sete subseções: tamanho, aparência, "nem todo Gu é
inseto", "estão vivos, e dá para perceber", ao toque, cheiro, "ele morde?" e o que muda quando o
bicho dorme ou passa fome.

**Tamanho — uma tabela do menor ao maior, com exemplo canônico em cada degrau:** meia unha
(pentagrama de luz branca leitosa) · uma unha · ponta de dedo (gafanhotos vermelhos) · um polegar
(pérola dourada; bonequinho de lobo cinzento) · um dedo (uma "centopeia" prateada e azul de pelos
finos, que é **Gu Imortal**) · **uma palma** (o Gu de luar, "do tamanho de um pingente de jade
comum"; libélula de quatro cores; caule de bambu oco e frio) · um punho (besouro preto como ferro;
aranha gorda de patas peludas; joaninha verde-jade) · uma bacia · duas mãos (besouro-serra tão
pesado que nem um cultivador de corpo excepcional o segura) · um antebraço (centopeia dourada
coberta de espinhos, rank 7) · corpo de montaria (aranha-lobo rank 5, cavalgável) · **uma casa**
(a "casa de Gu" das caravanas: árvore de dezoito metros com três andares de lojas por dentro) ·
uma montanha (formiga dourada, caso extremo e explicitamente excepcional).

As duas conclusões que a tabela existe para sustentar:

1. **Um Gu de rank 1 cabe na palma.** O Gu de luar ocupa um pedaço da palma, pesa **o equivalente
   a uma folha de papel** e é semitransparente a ponto de o dono **ver as linhas da própria mão
   através dele**; não refinado, vai no bolso como moeda. Um verme do licor pesa **meio ovo de
   galinha** (cap. 8, 17).
2. **Tamanho não escala com rank.** Gu Imortais de rank 6, 7 e 8 são do tamanho de um dedo, de um
   punho, de meia palma — a mesma faixa do rank 1. Consequência direta: **olhar um Gu não diz o
   rank dele**, e identificar um Gu é perícia, não percepção.

**Aparência:** a forma é de bicho real (percevejo, joaninha, aranha, cigarra, pulga, formiga,
libélula, escorpião, centopeia…); o que estranha é o **material**, quase sempre mineral — cristal,
jade, safira, porcelana vitrificada, bronze, ferro, pedra; semitransparentes; salpicados de
estrelas que piscam. **Quase todos brilham**, com luz própria da cor do efeito.

**Existe Gu que não é inseto?** Sim, e a nota lista três famílias com exemplos: **plantas** (grama
de nove folhas, caule de bambu, lótus do tamanho de um rosto, ginseng com raízes que parecem
pernas, uma árvore inteira), **objetos** (máscara de bronze, crânio de criança em cristal com
veios de sangue, noz do tamanho de uma melancia, peixe seco, cebola vermelha, ovo de cisne
translúcido) e **partes de corpo** (uma palma de bebê, macia e gorducha, translúcida, com veias
vermelhas por dentro). A frase-resumo é da obra: "Gu existem em todas as formas e tamanhos."

**Se mexem e fazem barulho:** um Gu recém-pego **treme na mão** enquanto luta contra a essência do
dono; um Gu escorpião anda devagar pela palma, tão leve que mal se sente, e **as pernas fazem um
ruído fininho**; um verme do licor solto no Mar Primordial nada, mergulha, sacode cabeça e cauda e
espirralha água "como quem toma banho quente". E o depósito de Gu de um clã soa como uma criação
de animais: alguns Gu silenciosos, outros **piando, cacarejando e farfalhando** (cap. 8, 17, 20).

**Ao toque:** frio e duro metálico · frio **antes mesmo de tocar** (um ovo de cisne translúcido
irradia frio que chega aos ossos) · macio e fresco como jade azul · liso e escorregadio como
porcelana boa, "gostoso de segurar" · áspero · frio como jade. Não há padrão único.

**Cheiro:** o verme do licor exala aroma de vinho tênue e enevoado — **que não é o vinho que ele
bebeu, é o cheiro do bicho** (cap. 17). E a obra encara a pergunta de frente: existem Gu
repulsivos em aparência, cheiro e toque, do tipo Gu de excremento e Gu de peido — categorias
formais, com rank e uso, que um refinador tem de pegar na mão.

**Acrescentado nesta sessão — duas correções de precisão.**

**(a) A pergunta "dá para pegar dez com uma mãozada?" foi reescrita.** A nota afirmava, em texto
simples (portanto como canônico), que "dá para segurar dez numa mão fechada". Isso é dedução, não
afirmação da obra, e estava marcado no nível errado. Corrigido: o dado canônico mais próximo é uma
cena com **oito Gu ao mesmo tempo nas mãos** de um cultivador, manuseados como peças miúdas sobre
uma mesa (cap. 598); a obra nunca conta quantos cabem numa mão fechada, e "uns dez nas duas mãos
em concha" ficou explicitamente marcado `(ded.)`.

**(b) A resposta sobre morder ficou à prova de dúvida.** A varredura completa do verbo *bite* no
texto inteiro devolve **um único tipo de ocorrência, e ela é mitológica**: nas fábulas de fundação
do mundo, um Gu "dá uma mordida" em outro Gu para roubar-lhe a propriedade (o self Gu mordendo o
strength Gu, o love Gu, o wisdom Gu — cap. 845, 870, 1230, 1619, 2053, 2177). É alegoria sobre a
origem da força, do amor e da sabedoria, não zoologia. Na camada onde os personagens vivem,
**nenhum Gu morde nada**: um Gu que prende, corta ou devora faz isso como **efeito acionado**. O
`fontes` ganhou os caps. 598 e 845.

### O que a obra não responde

- **Nenhum Gu morde, pica ou fere fisicamente o próprio dono.** Verificado com
  `Gu worm (bit|bites|biting)`, com `(bit|bite) (his|her) (hand|palm|finger|wrist|arm)` e com
  varredura de `bite` cruzada com termos de Gu: zero ocorrências reais. O perigo de manejar um Gu
  é o **contra-ataque de vontade** no refino, que atinge a mente e não a carne. Feras selvagens
  picam; Gu, não.
- **Nenhum Gu é descrito como quente ao toque.** Verificado com `warm to the touch` (zero
  ocorrências no texto inteiro) e com `(hot|scalding|burning|warm) (to the touch|in his palm)` — o
  único retorno é fogo ardendo numa palma como **efeito**, não a temperatura de um bicho. Frio,
  fresco e gelado aparecem com fartura; quente, não.
- **Quantos Gu cabem numa mão fechada.** Ver acima.

### Decisões

- A ordem da nota foi invertida em relação ao original: **a fisicalidade vem antes das regras**,
  porque, como diz a abertura da seção, nenhuma regra do sistema faz sentido antes dela.
- A tabela de tamanhos foi organizada por **unidade corporal** (unha, dedo, palma, punho,
  antebraço), não por rank — precisamente para que a designer veja com os olhos que rank e
  tamanho não se correlacionam.
- A liberação para inventar um Gu que morda ficou dita no corpo do texto, junto da negativa.

---

## 5. `02 - Gu/03 - Usar e Alimentar Gu.md`

### O que a nota ganhou

**Seção nova "O gesto: o que exatamente se faz para acionar um Gu"**, com diagrama Mermaid, e
**"Alimentar, na prática: o gesto e o ritmo"**.

**O gesto vem de uma aula** — literalmente uma aula, dada por um ancião a cinquenta e sete
adolescentes num campo de treino, com demonstração (cap. 22). São três etapas:

1. **Mover o Gu até o ponto de uso — só com a mente.** O ancião abre a mão direita, dedos bem
   afastados, palma virada para os alunos: "primeiro vocês usam a mente para mobilizar o Gu,
   levando-o até o centro da palma" — e a marca de lua crescente **desce pelo braço dele** até a
   palma. Sem gesto, sem palavra, sem toque.
2. **Empurrar essência para dentro do Gu — também só com a mente.** Um **fio de essência
   branco-prateada tão fino que quase não se vê** sai do corpo e entra no Gu. O Gu **acende**:
   brilha cada vez mais forte e, mesmo em dia claro, emite luz azul-pálida nítida. A cor da luz é
   a do efeito; a do fio é a do rank de quem aciona.
3. **Lançar — esta é física.** Ensinada como golpe de esgrima: os cinco dedos abertos se fecham
   devagar, o braço sobe e se estende, a palma faz um **corte leve no ar**. *Swoosh*, e a luz sai
   voando.

E as respostas diretas: **nem todo Gu exige a etapa 3** (defensivos e de reforço se acionam só com
a mente — a armadura simplesmente aparece sobre o corpo); **falar não é obrigatório** (a obra
mostra as duas coisas, e dizer o nome do Gu é hábito ou teatro, nunca requisito); **o Gu não
precisa estar visível** (muitos são acionados de dentro do corpo ou da abertura, e o gesto
informal para trazer o bicho para fora é **dar um tapinha na própria barriga** — cap. 156, 563);
**mirar é perícia e erra-se muito** (depois de cinco minutos de prática a turma já produzia
lâminas de luar, mas quase nenhuma acertava o boneco: umas se apagavam no caminho, outras
colidiam entre si, outras voaram para fora do campo — e a observação amarga do ancião é que quem
tem aptidão alta **treina mais vezes por dia**, porque tem mais essência para gastar errando).

**Alimentar é físico, não mental.** Chama-se o Gu para fora e põe-se a comida junto dele: o verme
do licor sai da abertura "virando um risco de luz branca", desenha um arco no ar e cai **com um
*ploc* dentro da taça de vinho**; o Gu de luar recebe as pétalas na palma da mão. Sem ritual, sem
fórmula, sem preparo. **O ritmo é doméstico:** o Gu de luar come **duas refeições por dia, duas
pétalas cada, de manhã e à noite**; o verme do licor bebe de um jarro que dura quatro dias,
guardado embaixo da cama; as pétalas são compradas na loja ao lado da academia, **dez por uma
pedra primordial**, entregues num **saquinho de papel**, e **murcham em poucos dias** — o que
impede estoque e obriga compra recorrente (cap. 23, 39).

**Acrescentado nesta sessão — a subseção "Quanto tempo leva, e o que se gasta além de essência",
que fechava a única pergunta do usuário ainda em aberto nesta nota.**

- **Acionar é instantâneo**, e a obra **enuncia o contraste** em vez de deixar deduzir: as
  formações de Gu são consideradas inferiores aos golpes combinados justamente porque **não podem
  ser acionadas instantaneamente** — levam muito tempo e não servem numa troca rápida (cap. 923).
  Se o texto precisa dizer que a formação é a exceção lenta, o acionamento normal não custa tempo.
- **O que ele custa é atenção, e essa é a moeda escondida do combate.** No instante em que alguém
  aciona um golpe combinado, **a atenção inteira dele vai para os Gu que o compõem**; um Mestre Gu
  comum obrigado a desviar a atenção naquele momento **perderia o controle do que estava fazendo**
  (cap. 854). Dividir atenção é perícia: a obra descreve um cultivador **"dividindo a mente em
  três"** para conduzir um Gu, mobilizar essência e injetá-la num terceiro ao mesmo tempo (cap.
  297), e o fato de a cena ser digna de nota diz que não é o padrão. Um Mestre Gu soltou **mais de
  oitocentos Gu** da abertura numa sequência, e o custo registrado foi exatamente esse — "com
  frequentes deslocamentos da mente" (cap. 575).
- Isso fecha três coisas de uma vez: por que recarregar no meio da luta é quase suicídio, por que
  controlar muitos Gu é caro sem ser lento, e por que **interromper a atenção de um inimigo é um
  ataque**. Veio com bloco "Para o design" propondo linhas de atenção em vez de economia de ações.
- O `fontes` ganhou os caps. 575, 854 e 923.

### O que a obra não responde

- **Quanto tempo leva uma refeição de um Gu comum.** Verificado com
  `(finished|took|spent) …(eating|feeding|devouring)`: não há uma única passagem que cronometre o
  ato. O único número existe no patamar imortal e é a exceção do topo — um Gu Imortal que se sacia
  depois de **oito dias e oito noites** submerso na água de que se alimenta. A nota diz que para o
  dia a dia é campo livre.
- **Se dá para alimentar em combate.** A obra **nunca mostra** e **nunca proíbe**. O que ela mostra
  sempre é o contrário: alimentação é rotina de casa, em horário fixo, e o que se faz em pausa
  tática é recarregar essência com pedras. A nota registra a leitura prática — tratar alimentação
  como atividade de tempo livre — **explicitamente marcada como leitura nossa**.

### Decisões

- O diagrama Mermaid do acionamento ficou marcado como **leitura nossa da cena de aula**; a obra
  não apresenta fluxograma nenhum.
- A subseção nova foi posicionada **depois** do diagrama, para não partir ao meio a exposição das
  três etapas e sua legenda.

---

## 6. `02 - Gu/13 - Onde um Gu Mora.md`

### O que a nota ganhou

**Três subseções novas:** "Onde exatamente, no corpo" e "O dono sente que eles estão lá?" dentro
de "A abertura: o cofre-forte"; "Como a marca é, de perto" dentro de "O corpo: o Gu como
tatuagem"; e a seção "Entrar e sair: dói? demora?".

| Pergunta | Resposta | Fonte |
|---|---|---|
| Onde ficam? | Três polegadas abaixo do umbigo, entre os rins. Por dentro, os Gu **pairam imóveis no "céu" vazio acima do mar**; os aquáticos boiam na superfície; um verme do licor solto ali nada e se espreguiça "como quem toma banho quente" | cap. 5, 6, 20 |
| O dono sente que estão lá? | **Não.** A obra nunca descreve peso, coceira, calor, pressão ou qualquer sensação corporal. A prova é pelo avesso: um Mestre Gu experiente andou com um Gu que um inimigo plantara no próprio antebraço e **só descobriu quando lhe contaram** | cap. 398, 399 |
| A única exceção | A sensação de **excesso**: um Gu de rank muito acima do seu pressiona a abertura por dentro, continuamente, e essa pressão é sentida e temida | cap. 397, 424 |
| Como é a tatuagem? | **Desenho colorido na pele**, com a forma do próprio Gu, do tamanho de uma tatuagem pequena: lua crescente azul na palma; estrela de cinco pontas; lanterna vermelha na língua; dois raios nas costas; pérola vermelha no peito; insígnia de escamas do ombro à cintura; um diamante de oito faces enfiado no antebraço, projetando através da carne uma **luz azul semitransparente e sinistra** | cap. 20, 22, e o catálogo de casos |
| A marca se mexe? | **Sim, e é mecânica.** O dono a **move pelo corpo com um pensamento**, e ela desliza pela pele. O mesmo Gu de luar aparece, em momentos diferentes, na testa, no braço, na palma e na língua | cap. 20, 22 |
| A marca acende? | Sim, com a cor do efeito, forte o bastante para ser vista em pleno dia | cap. 22 |
| Tirar dói? Demora? | **Depende de quem pôs, e a diferença é brutal.** O seu próprio Gu: instantâneo e indolor, "com um pensamento", sem dor, esforço ou espera registrados — mais de oitocentos Gu saíram numa sequência. O Gu que **outra pessoa** plantou em você: praticamente irremovível; as duas únicas saídas listadas são **quem plantou retirar pessoalmente** ou o alvo **decepar o próprio antebraço** — e ele considera seriamente a segunda. O Gu de um cadáver: extrai-se com a mão, trabalho físico e imediato | cap. 398, 399, 575 |

Também entrou o depósito de Gu do clã como **inventário descrito**: paredes de nichos quadrados,
do tamanho de um punho ao de um caldeirão; dentro deles bacias de pedra cinzenta, pratos de jade
verde, gaiolas de grama trançada, fornos de barro, potes de jade, porcelana, tigelas de bronze;
alguns Gu em silêncio, outros piando, cacarejando e farfalhando — a sala inteira soando como uma
criação de animais. Mais os detalhes de operação, que descrevem uma instituição e não um armário:
sala guardada, estudantes entrando **um de cada vez** em fila, estoque reposto **uma vez por ano**,
nichos frequentemente vazios porque a espécie popular acabou (cap. 8).

Nada foi acrescentado nesta sessão: a verificação não encontrou lacuna nem imprecisão.

### O que a obra não responde

- **Nenhuma sensação corporal de carregar Gu.** Verificado com `(feel|felt) the gu worm` (zero
  ocorrências) e com `(under|beneath) his skin` (retorna só descrições de ferimento, nada de Gu se
  movendo sob a pele). A negativa é sólida.
- **Número de vagas por rank de abertura.** A obra **nunca** dá um número. Isso já estava dito na
  nota, e de propósito na última linha da tabela de capacidade, para que ninguém o preencha por
  engano: qualquer tabela de "slots por rank" seria invenção.
- **Se o Gu que reside num objeto é categoria formal ou exceção isolada.** Registrado uma única
  vez; a nota diz que a obra não esclarece.

### Decisões

- A nota abre com um bloco explicando a própria marcação e afirmando que **não há nenhum `*` nela**
  — ela é inteiramente canônica. Isso foi mantido, e por isso nenhuma das lacunas acima foi
  preenchida com invenção nossa: elas ficaram declaradas como ausências.

---

## Perguntas do usuário que a obra **não** responde — lista consolidada

Reunidas aqui porque é a informação mais acionável do relatório: onde esta lista diz "não
informa", a designer pode desenhar como quiser sem contradizer o cânone. Cada uma foi testada com
busca no texto-fonte, não presumida.

| Pergunta | Situação |
|---|---|
| Que tamanho **absoluto** tem a abertura? | A obra é evasiva de propósito ("infinitamente grande e infinitamente pequena"); a única medida, "seis por seis", nunca é explicada |
| Há luz, som ou "clima" dentro da abertura? | Nada descrito além do mar, das paredes e do céu vazio |
| Quanto tempo passa entre o estouro da cerimônia e a pessoa voltar a si? | Só "parece longo e é curtíssimo" |
| Que substância se passa na pele para fraudar a cerimônia? | Nunca nomeada |
| A essência primordial tem cheiro, temperatura ou som? | Não, em estado normal — mas **pode ser tingida e perfumada** por um Gu (cap. 152) |
| A essência primordial tem peso? | Nada |
| Quantos Gu cabem numa mão fechada? | Nunca contado; o dado mais próximo é oito Gu nas mãos de um cultivador |
| Algum Gu é quente ao toque? | Não. Frio, fresco e gelado aparecem; quente, nunca |
| Algum Gu morde o dono? | Não. A única "mordida" do texto inteiro é mitológica, nas fábulas de fundação |
| Quanto tempo leva a refeição de um Gu comum? | Nunca cronometrada |
| Dá para alimentar um Gu em combate? | Nunca mostrado e nunca proibido |
| O dono sente os Gu dentro do corpo? | Não — e a obra prova pelo avesso, com um Gu plantado que passou despercebido |
| Quantos Gu cabem por rank de abertura? | Nunca há número. Qualquer tabela de slots seria invenção |

## Decisões transversais do passe

1. **Ausência virou permissão explícita, não silêncio.** Toda lacuna ficou escrita no corpo da
   nota, com a frase que libera a mesa ("se você precisar de um na mesa, é campo livre"). Uma
   lacuna não declarada seria lida pela designer como coisa que ela não entendeu.
2. **Concretude foi acrescentada, regra nenhuma foi reescrita.** As seções novas são blocos
   inseridos; as seções de regra, tabelas e blocos "Para o design" que já existiam foram
   preservados intactos.
3. **Onde a cena existia, a cena venceu o resumo.** A cerimônia do despertar, a aula de
   acionamento e o depósito de Gu do clã foram narrados como cena, com o detalhe sensorial que a
   obra dá, porque é assim que uma leitora que nunca leu a obra consegue imaginar o mundo.
4. **Dois diagramas Mermaid foram acrescentados** — o corte da abertura e o fluxo do acionamento —
   e **os dois trazem, logo abaixo, a ressalva de que são leitura nossa**: a obra não apresenta
   esquema nenhum.
5. **Precisão de marcação foi tratada como bug.** A afirmação "dá para segurar dez numa mão
   fechada" estava em texto simples, isto é, apresentada como canônica, sendo dedução. Foi
   rebaixada para `(ded.)` com o dado canônico ao lado. É o tipo de erro que corrói a confiança na
   convenção inteira.
6. **Todo capítulo usado entrou no `fontes` do frontmatter** e **nenhuma citação foi para o corpo
   do texto**, conforme a regra do vault.

## Pendência encontrada, fora do escopo deste passe

O auditor de links do vault (`_pipeline/auditar-links.py`) foi rodado duas vezes durante este
trabalho, e nas duas acusou **um link quebrado**, sempre na pasta de estudos de caso e sempre num
arquivo que não é meu — a cada rodada num par diferente, porque outros agentes estavam
acrescentando notas ao vault ao mesmo tempo (207 notas na primeira medição, 211 na segunda). Os
dois flagrados foram:

> `41 - Comprar um Estágio de Cultivo com Todo o Futuro` ← `40 - Fugir de um Enxame e Sair Montado.md`
> `45 - Perder de Propósito e Cobrar Caro` ← `44 - Sobrecarregar o Defensor que Devolve o Golpe.md`

O padrão sugere que a pasta de estudos de caso está com **notas encadeadas apontando para a
seguinte antes de a seguinte existir** — vale uma passada de `numerar-notas.py` seguida do
auditor quando os agentes daquela pasta terminarem. Fora isso, os mais de 4.400 links do vault
resolvem por nome exato de arquivo e nenhum depende só de alias. **As seis notas deste passe não
introduziram link quebrado nenhum.**
