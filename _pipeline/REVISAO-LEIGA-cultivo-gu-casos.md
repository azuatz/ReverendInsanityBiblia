---
tags:
  - pipeline/relatorio
  - revisao/leiga
status: concluido
data: 2026-09-02
escopo: ["01 - Cultivo (19 notas)", "02 - Gu (16 notas)", "10 - Estudos de Caso Mecanicos (49 notas)"]
---

# Revisão de leitora leiga — Cultivo, Gu e Estudos de Caso

Leitura das 84 notas do núcleo do sistema no papel da designer de TTRPG que **nunca leu
Reverend Insanity e não vai ler**. Tudo o que ela sabe vem destas páginas. Caçados, nesta
ordem: bloqueadores, sérios, menores, e o que está bom. Bloqueadores e sérios foram
corrigidos no ato; o que ficou aberto está listado no fim.

**Método.** Li integralmente `01 - Cultivo` e as notas de concretude de `02 - Gu`; a auditoria
das 49 notas de `10` foi feita em três frentes paralelas contra o modelo e contra a tabela
soberana, e **cada bloqueador foi reconferido por mim no texto-fonte** antes de virar correção.
Três achados dos auditores foram **rejeitados** depois dessa conferência, e estão registrados
abaixo — porque descartar um falso positivo também é resultado.

---

## Veredito de conjunto

**As três pastas passam.** Se a designer ler só elas, ela consegue prototipar — e, o que é mais
raro, ela consegue prototipar *sabendo o que é canônico e o que é nosso*. O material acerta as
duas coisas mais difíceis de um documento assim: separa regra de exemplo, e separa o que a obra
afirma do que nós deduzimos.

O que quase impediu isso não foi conteúdo: foi **renderização**. A nota-índice de `10` tinha 41
dos seus 48 links quebrando dentro de tabelas Markdown, e a auditoria de links do vault não
enxerga esse tipo de erro. A designer abriria a porta da pasta e encontraria quarenta e uma
linhas partidas ao meio.

Depois disso, o padrão dos problemas reais foi um só e se repetiu em toda parte: **as notas
conceituais definem tudo; as notas de caso presumem tudo**. `01` e `02` são o dicionário; `10`
escrevia como quem já leu o dicionário. Vinte e seis links de primeira ocorrência e dez glosas
inseridas resolvem isso.

---

## `01 - Cultivo` — 19 notas

### Bloqueadores corrigidos

| Nota | Achado | O que foi feito |
|---|---|---|
| `19 - Tornar-se Venerável` | Faixas de dao marks **desatualizadas**: "rank 7 entre 9.000 e 30.000; rank 8 entre 30.000 e 300.000". Contradizia `16 - Dao Marks` **e** a tabela soberana, que registra explicitamente essa versão como corrigida (o piso do rank 8 é 100.000). | Substituído pelas três faixas canônicas: 6 = 0–9.000, 7 = 10.000–30.000, 8 = 100.000–300.000. |
| `03 - Aptidão` | A nota adota grau D = **20–39%** na tabela e depois argumenta duas vezes com "teto de 30%" — contradizendo a si mesma e a `05 - Ranks e Avanço`, que diz "cujo teto é 39%". | Uniformizado em 39%. O exemplo das ativações foi recalculado (duas **ou três**, não duas). |
| `03 - Aptidão` | "Numa **população comum**, cerca de cinco em cada dez jovens têm algum talento". Lido ao pé da letra, dá um mundo com bilhões de Mestres Gu — erro de duas ordens de grandeza contra a própria pirâmide de `05`. | Reescrito para "entre os jovens que **de fato passam pela cerimônia**", com um parágrafo novo que amarra a proporção ao portão de sangue do clã e remete à pirâmide demográfica. |
| `03 - Aptidão` | Nota de rodapé `[^1]` **definida e nunca referenciada** — no Obsidian, rodapé órfão. Seu conteúdo já estava duplicado num callout do corpo. | Removida. |
| `03 - Aptidão` / `09 - Avançar com Aptidão Baixa` | Perda de aptidão do ritual demoníaco registrada como "cerca de dois pontos"; a tabela soberana adota **um**. Conferido no texto-fonte: **a obra se contradiz** (uma passagem diz 44→42, outra 44→43), e a própria nota usa 43% como ponto de partida do caso — ou seja, era incoerente consigo mesma. | Passou a "**um a dois pontos**", dizendo que a tabela de referência adota um e por que. Tabela de decisão de `09` ajustada para "−1 a −2". |
| 4 notas (`16`, `17`, `18` de `01`; `02` de `02 - Gu`) | Usavam `(ded.)` **sem nunca explicar o que significa**. Para a leitora, um símbolo mudo. | Inserido o bloco padrão "Como esta nota está marcada" logo após a frase de abertura, com os quatro estados e a garantia de que apagar tudo com `*` devolve a nota a cem por cento canônico. |
| 10 notas | Wikilinks dentro de tabelas com `\|` **não escapado** — a célula parte ao meio e o link morre na renderização. | 22 links corrigidos em `01` e `02` (mais 41 na nota-índice de `10`). |

### Sérios corrigidos

- **`03 - Aptidão` × tabela soberana — a queda de rank que parecia divergir.** A nota dizia
  "despencou de rank 3 para rank 1"; a tabela diz "de rank 3 para rank 2". Fui ao texto-fonte:
  **as duas são verdadeiras** — 3→2 no instante da primeira aplicação, e até o estágio inicial
  do rank 1 ao fim das seis horas. A nota agora conta as duas etapas, o que elimina a
  contradição aparente e **acrescenta informação** em vez de escolher um lado.
- **`05 - Ranks e Avanço`** afirmava que cruzar um rank em combate é feito extraordinário e
  parava aí — enquanto a tabela soberana publica 30% e 60% de chance para exatamente esse caso.
  A designer leria "impossível" onde o sistema diz "difícil e mensurável". Os dois números
  entraram, com a leitura de que um Gu certo dobra a chance.
- **`10 - As Dez Constituições Extremas`** dava a terra abençoada de grade super como "acima de
  6.700 km²" (sem o teto canônico de 13.000) e o fluxo de tempo como "quarenta para um" — um
  arredondamento que não está na obra. Corrigido para a faixa fechada e para os dois valores
  documentados, 1:38 e 1:46.
- **`04 - Essência Primordial`** carregava o alias **"Essência Imortal"**, que é o nome de outra
  nota (`15`). Um `[[Essência Imortal]]` resolveria para a nota errada. Alias removido.
- **`08 - Attainment`** falava três vezes em anexação de aberturas sem apontar para o caso que a
  detalha. Link para `42 - Anexação de Aberturas` acrescentado.
- **`02 - Abertura`** listava `Aptidão` duas vezes em Relações; fundido numa entrada só.
- **`10`** tinha uma frase órfã ("Sobre a variação de nome de uma das sete.") existindo só para
  ancorar uma nota de rodapé. O marcador foi para dentro da linha da tabela a que pertence.
- **`09`** tinha dois `---` seguidos, renderizando régua dupla.

### O que está bom, nomeado

- **`01 - Visão Geral do Cultivo`** é a melhor nota-porta do vault. O "esqueleto em seis linhas"
  entrega a cadeia inteira do sistema — abertura → aptidão → essência → Gu → rank → ascensão →
  dao marks → provações → tempo de vida — antes de qualquer explicação, e as 24 "regras do
  mundo" numeradas são um índice de mecânicas que se lê em cinco minutos.
- **`02 - Abertura`** é o modelo de como integrar concretude: a seção "Por dentro" não está
  colada no fim, está no meio do fluxo, e responde tamanho, localização, textura da parede, cor
  do mar, e **o que se vê e se ouve quando a parede estoura**. Onde a obra é evasiva ("infinitamente
  grande e infinitamente pequena"), a nota diz que a evasão é a resposta e converte a lacuna em
  regra útil: a abertura só tem tamanho relativo, e é por isso que tudo no sistema é percentual.
- **`13 - Tribulações e Calamidades`** fecha a aritmética inteira do calendário imortal — as três
  contas (9.000 / 30.000 / 300.000) batem exatamente com as faixas canônicas — e ainda antecipa
  a pergunta que todo jogador faz ("moro fora da abertura e progrido de graça?") com a resposta
  e o motivo. O callout que **decide por você** onde a obra não decide, oferecendo duas regras e
  recomendando uma, é o melhor gesto editorial das três pastas.
- **`08 - Attainment`** resolve um problema real de fonte: existem versões de oito e de nove
  degraus circulando, e a nota fixa a de nove, manda contar **pelo nome e nunca pela posição**, e
  se declara fonte única do vault para a escala.
- **`06 - O Corpo e a Mente do Mestre Gu`** existe para desfazer o mal-entendido mais provável do
  gênero — que subir de nível melhora o corpo — e o desfaz em uma frase ("rank é orçamento, não
  musculatura"), com a consequência de design já extraída: desarmar é condição de vitória
  legítima em qualquer patamar.

---

## `02 - Gu` — 16 notas

Foi a pasta com **menos** achados, e não por ser menos ambiciosa: é a mais bem construída das três.

### Corrigido

- `02 - O que é um Gu`: convention header ausente (ver acima).
- Wikilinks de tabela não escapados em `06`, `07`, `08`, `10`, `11`, `13`.

### O que está bom, nomeado

- **`02 - O que é um Gu`, seção "Como um Gu é, fisicamente"** — é a resposta exata ao passe de
  concretude, e está no **começo** da nota, onde precisa estar. Tabela de tamanhos do "meia unha"
  à "casa"; a observação que mais muda o design (**tamanho não escala com rank**, logo olhar um Gu
  não diz o rank dele); peso comparado a uma folha de papel; texturas específicas; e a declaração
  franca de que **nenhum Gu na obra é quente ao toque**. A pergunta "dá para pegar dez de uma
  mãozada?" é respondida com o dado canônico (oito nas mãos, numa cena) e a extrapolação marcada
  `(ded.)`. É assim que se preenche lacuna sem mentir.
- **`03 - Usar e Alimentar Gu`, seção "O gesto"** — responde em três etapas a pergunta que nenhuma
  regra respondia: *pensa, fala, toca ou aponta?* Duas etapas mentais, uma física, e a etapa física
  só existe quando o efeito sai do corpo. Fecha com o achado mais jogável das três pastas: **mirar
  é perícia, e erra-se muito** — e talento alto não melhora a mira, compra repetições.
- **`10 - Como Funciona um Combate`** é a nota mais útil do vault para prototipar, e tem uma seção
  chamada **"O que a obra não diz"**. Todos os números conferidos batem com a tabela soberana:
  30%/60% entre ranks, 10 m e 6 m de distância, dois Gu de rank 3 para conter um ataque de rank 4,
  meia respiração de defesa insuficiente, uma rodada por respiração.
- **`08 - Killer Moves`** resolve, com uma distinção só, um conflito que atravessava quatro notas:
  Gu articulados num golpe único custam **uma** tarefa; Gu com comandos independentes custam N. E
  declara a distinção como reconstrução nossa, dizendo que é a única leitura que mantém tudo de pé.
- **`04 - Onde um Gu Mora`** e **`11 - Ferimento, Cura e Fuga`** trazem o cabeçalho de
  confiabilidade e, na primeira, a frase que a designer mais precisa ouvir: a nota declara que **não
  há nenhum `*` nela**, e que a única ausência é dita como ausência "para que ninguém a preencha
  por engano".

---

## `10 - Estudos de Caso Mecânicos` — 49 notas

### A nota-índice: funciona como índice comentado?

**Agora sim; antes, não.** Ela já era boa no essencial — lista os 48 casos, cada um com uma linha
de comentário útil, agrupados por tema — mas tinha quatro defeitos de porta de entrada:

1. **41 dos 48 links quebravam na renderização** (pipe não escapado dentro de tabela). **Corrigido.**
2. **A seção "Índice rápido: exceção × regra" era resíduo do documento original de 823 linhas:**
   51 linhas com nomes que não batiam com nenhum título de nota ("Fuga por gerenciamento de
   recursos", "Blefe de patamar por aparência", três linhas separadas para "Território"), e **sem
   um único wikilink**. A designer não conseguia mapear linha → nota. **Reconstruída**: 48 linhas,
   uma por nota, com o título real, wikilink, na ordem da barra lateral, preservando todos os
   vereditos originais.
3. **Contagem quebrada:** "duas regras de leitura" seguidas de cinco itens. **Corrigido.**
4. **Linguagem de bastidor:** "quatro segredos que **as notas novas** trazem" — só faz sentido para
   quem acompanhou a redação. **Reescrito.**

E faltava o principal: **a nota não ensinava a usar a pasta.** Acrescentei a seção **"Como usar
esta pasta"**, com três caminhos de leitura (começar pelos treze casos de rank baixo; ir direto ao
índice de exceção × regra para testar uma regra já escrita; caçar o `Regra proposta` de cada nota
para material de sessão) — e uma advertência de calibragem que a designer precisa antes de tudo:
**quase todos os casos terminam em sucesso**, e os seis que terminam em fracasso limpo são os mais
didáticos do conjunto.

As tabelas do índice comentado também estavam **fora da ordem dos arquivos** (11, 12, 13 antes de
09, 10; 18, 20 antes de 17, 19). Como o prefixo numérico existe justamente para que a barra lateral
seja o currículo, índice e barra lateral discordavam. **Reordenadas.**

### Bloqueadores corrigidos nos casos

| Caso | Achado | O que foi feito |
|---|---|---|
| `28 - Guerra de Preços` | **Moeda errada por um fator de mais de cem milhões.** A tabela dizia "1.730.000 pedras primordiais" e "12 milhões de pedras"; o texto-fonte diz *immortal essence stones*. Como está na tabela soberana que riqueza mortal não compra nada no reino imortal, a nota afirmava exatamente o que o sistema proíbe. | Trocado para **pedras de essência imortal**, com callout novo explicando a diferença de escala entre as duas moedas. Lucro corrigido: **12 milhões brutos, 10 milhões líquidos** depois de quitados os empréstimos (também no texto-fonte). |
| `44 - A Armadilha que Engorda a Cada Teste` | "dezesseis mil marcas resultam em **dezesseis vezes** o efeito" — contradizia a fórmula soberana `1 + marcas ÷ 1.000` (= 17×) **e a frase seguinte da própria nota**, que dizia "dezessete vezes". | Corrigido para dezessete, com a fórmula explícita ao lado. |
| `42 - Anexação de Aberturas` | Escada de attainment quebrada como progressão ("Mestre → rank 6 e **só** eles" seguido de "Quase Grão-Mestre → **a maioria** dos de rank 6"), sem o degrau de rank 8, contradizendo `01 - Cultivo/13` e `04 - Mundo/13`. | Substituída pela escada canônica (Mestre → 6, Grão-Mestre → 7, Grande Grão-Mestre → gruta-céu 8), com os degraus "quase-" explicados como intermediários e a leitura de que o piso é **por caminho**, não por pessoa. |
| `42` | O caso afirmava sucesso ao anexar território de rank 7, mas nunca declarava o attainment do operador — que a própria tabela torna obrigatório. | Acrescentada a dedução marcada `(ded.)`: ele era necessariamente Grão-Mestre, e sem isso teria falhado mesmo com o dono morto. |
| `42` | **Contradição entre notas** sobre o calendário de provações: aqui, anexar "reseta o cronômetro" e era tratado como custo; em `01 - Cultivo/13`, o contador é **creditado** e isso é o benefício decisivo. | Fui ao texto-fonte: **as duas coisas acontecem juntas** — pula-se de uma a cinco provações **e** o cronômetro da próxima é zerado. Seção reescrita para apresentar as duas, com a tensão entre elas (provação pulada é dao mark ganho e tribulação não contada, logo rank mais lento) marcada `(ded.)` por ser leitura nossa. |
| `44` e `45` | Oito ocorrências de **"Imortal Gu"** designando a *pessoa*, ao lado de "Gu Imortal" designando o *verme*, na mesma nota. Vazamento de nota bruta. Para a leitora, indistinguíveis. | Todas trocadas por "Imortal". |
| `07 - Romper o Rank 2` | Duas frases do mesmo callout se desmentiam: "algumas centenas a cerca de mil pedras" e "de duas a dez vezes o preço de um Gu de rank 1" (que a tabela soberana fixa em ~500). | Reescrito com a âncora certa: uma a duas vezes o preço de um Gu novo, e meses do custo de vida anual (~1.500 pedras/ano). |
| `07` | "gasta de três a cinco pedras por dia **só para viver**" — a tabela atribui esse valor a manter quatro Gu **mais** cultivo e vida pessoal; o grosso é ração de Gu. | Reescrito para "para se manter em operação", listando os três componentes. |
| `11 - Caçar o Que Não se Vê` | "11% da reserva dão exatamente dois disparos" contra os **10% por disparo** canônicos da tabela. Conferido no texto-fonte: **a obra se contradiz consigo mesma** (uma cena diz dois disparos; outras três repetem 10% por uso). | Nota de rodapé nova registrando a contradição e dizendo que o vault mantém os 10% como valor de sistema. |
| `09` e `13` | "carrega um Gu de rank 6" sem dizer que rank 6 **é** a fronteira imortal, e que a regra geral é que uma abertura mortal guarda **zero** Gu Imortais — ou seja, sem sinalizar que o caso é a exceção canônica. Quem tivesse lido `04 - Onde um Gu Mora` concluiria que uma das duas notas estava errada. | Glosa e wikilink em ambas, dizendo o que é e por que é anômalo. |
| `16 - O Ambiente Manda Mais que o Rank` | Quatro termos de mundo sem definição nem link: "espírito guardião", "cultivador imortal", "céus antigos", "caminho de transformação". Era a nota mais hostil à leitora da pasta. | Os quatro glosados e linkados. |
| `05 - O Catalisador Fora da Receita` | "vinte pontos percentuais" apresentado como número da obra, quando a obra diz "20%" — ambíguo entre pontos e relativo. A nota `08` faz a mesma discussão com callout e marcação; esta resolvia em silêncio. | Marcado `(ded.)`, com o mini-callout explicando a escolha e dizendo que a leitura relativa também fecha. |
| `27 - A Conta de uma Calamidade` | A situação omitia o dado mais jogável: o administrador era um **mortal de rank 4** matando uma criatura que é problema para imortais. Também: "68 contas" sem denominação (as quatro diferem ×100 entre si), e "besta desolada"/"espírito guardião" sem definição. | Todos acrescentados. Rank declarado, denominação nomeada (uva-verde, rank 6), os dois termos glosados. |
| `27` | **Invenção apresentada como cânone:** "sacrificar 666 km² foi uma escolha de contenção". No texto, os cortes deliberados eram de meio km² por vez; os 666 km² são a perda **total**. | Reescrito para separar o que foi sacrificado do que foi destruído. |
| `21 - Um Trunfo que Nunca Foi Testado` | "Um cultivador de **rank baixo**" comandando três reis-de-miríade e queimando um Gu de rank 5 — contradizendo a tabela da própria nota. | Corrigido para **rank 4**. |
| `26 - Dar de Graça o que Vai Vazar` | **Nome de personagem no corpo** ("com seu irmão Wei aqui"), violando a política de spoilers. A nota `25` conta a mesma cena e a anonimiza corretamente. | Trocado por "o intermediário do clã". Era a única ocorrência de nome próprio nas 48. |
| 15 notas | "pedras primordiais" — a moeda do mundo — sem wikilink na primeira ocorrência. | Linkada na primeira menção em todas. |
| 9 notas | "Gu Imortal", "essência imortal", "dao marks", "attainment", "reino de sonho" sem link na primeira ocorrência. | 11 links de primeira ocorrência acrescentados, com três reposicionados à mão por terem caído dentro de citação ou de `==destaque==`. |

### Sérios corrigidos

- **`18 - Emboscada de Um Contra Sete` era anedota, não caso.** Única das 48 sem **um único
  número**: sem ranks, sem custo, sem duração, e com um "trunfo" nunca explicado. Em vez de
  inventar números, acrescentei um callout que **diz isso em voz alta** — o que é informação útil:
  avisa a designer de que ali ela pode desenhar como quiser, e a manda a `20` e `17` para a mesma
  lição com aritmética à vista.
- **`20 - Guerra de Custos`, Caso A** tinha o mesmo problema em menor grau. Callout `[!question]`
  declarando a lacuna, para a designer não procurar valores que não existem.
- **`34 - Um Golpe Mal Testado`** usava **"jun"** (a única unidade de força do mundo) e "quinhentas
  unidades da medida usada no mundo" — uma não-definição, quando a unidade tem nome canônico
  (*man soul*) e seção própria na tabela soberana. As duas foram definidas, com régua de calibragem
  (30 jun é o piso do caminho; 100 jun é rank 5; mil man soul custam ~20 anos de cultivo — logo o
  golpe cobrou uma década de progresso numa ativação).
- **`49 - Explorar um Reino de Sonho`** trazia "10 milhões / 90 milhões / 200 milhões" sem unidade,
  e uma linha ininteligível ("~9 milhões, e a corrosão derrubou pela metade"). Unidade nomeada e
  explicada, linha desfeita, e acrescentada a leitura que faltava: o segundo estágio consumiu 98%
  da fundação de entrada.
- **`41 - Um Mortal Refina um Gu Imortal`** prometia no título o que o corpo não entregava — quem
  refina é o espírito guardião. Callout novo desfaz a abreviação e nomeia o feito real (**capturar
  a vaga**, cronometragem e não técnica), que é justamente o que torna o caso replicável por
  personagens sem poder imortal. "Ritual mítico de geração", "bebida suprema" e "quatro doses
  clássicas" também foram definidos.
- **`24 - Colher a Flor Antes do Prazo`** prometia o balanço e não fechava a conta: dizia que
  matar a nascente é que era o preço, sem dizer quanto a nascente valia. Com o número da tabela
  (≥100 milhões de pedras ao longo de 50–60 anos), o dilema vira aritmética: **50 mil pagos para
  destruir um ativo que produziria duas mil vezes isso**.
- **`23 - Ganhar um Leilão`** dava 3.000 como se fosse o preço do item, quando é o **lance de
  partida** (a expectativa na cena era 5.000–8.000, e a tabela precifica o item em 8.000); e dizia
  "elevava o cultivo de um rank 2", sugerindo subir de rank quando o efeito é subir um **estágio**.
  Ambos corrigidos.
- **`48 - Fazenda de Tribulações`** entregava "revivendo subordinados como mortais completos" como
  rótulo, sem método nem custo. Acrescentada a ressalva de que **a obra não descreve o método**,
  com remissão ao repertório de revivificação — e o detalhe que fecha o ciclo: voltar *sem o rank*
  é o que torna a fazenda replantável, porque é a ascensão que produz a colheita.
- **`30 - Reputação Comprada em Prestações`** divergia de `19` no gênero da mesma pessoa, afirmava
  um ganho de reputação que `19` não registra, e trazia um colchete editorial cru
  (`[token de trânsito da região]`) no meio de uma citação. Gênero uniformizado, remissão a `19`
  acrescentada, ganho de reputação marcado `(ded.)`, colchete reescrito.
- **`32`, `35`, `47`** tinham um termo-chave cada sem definição ("reino de sonho", "existência de
  nível supremo" = Venerável, attainment de "voo"). Todos glosados e linkados.
- Padronização: três notas com `status: consolidado` fora do padrão `verificado-no-texto`; dois
  `(ded.)` sem crases em `10`.

### Falsos positivos rejeitados após conferência no texto-fonte

Registro porque descartar também é resultado, e porque duas dessas conclusões seriam danosas:

1. **Um auditor concluiu que a tabela soberana estava defasada** ao registrar 500 jun como pico
   documentado, já que `34` diz 800. **Não procede.** São montagens diferentes e as duas são
   canônicas: 500 jun com Gu de esforço total mais amplificador de rank 5; 800 jun com o golpe de
   catorze Gu deste caso. Em vez de "corrigir" a tabela, acrescentei um callout em `34` dizendo
   que os dois números medem configurações distintas — que é o que impede a designer de achar que
   um deles é erro.
2. **A divergência 3→1 × 3→2 da queda de rank** parecia contradição entre `03 - Aptidão` e a
   tabela. As duas estão certas, em momentos diferentes do mesmo episódio (ver acima).
3. **A "contradição" sobre o cronômetro de provações na anexação** também não era contradição: a
   obra afirma as duas coisas na mesma frase.

### O que está bom, nomeado

- **`44 - A Armadilha que Engorda a Cada Teste`** é a melhor nota da pasta: método numerado com
  custo e risco por passo, uso exemplar de `—` para as três lacunas reais da obra, e dois callouts
  de precisão que impedem leitura errada ("o que decidiu foi a segunda medição"). O passo "medir de
  novo" é ensino de sistema puro.
- **`02 - Punhos Contra uma Camada de Defesa`** é o modelo executado sem folga: situação por rank e
  por reserva (80% contra 44%), método em três passos com o custo declarado, números concretos, e um
  veredito que distingue corretamente "regra" de "pré-requisito raro".
- **`03 - O Sapo de Rank 5`** e **`11 - Caçar o Que Não se Vê`** são os dois melhores para a leitora
  leiga: ensinam a lógica do mundo — protocolos de gatilho de bestas; tudo o que a invisibilidade
  *não* cobre — sem exigir contexto nenhum, e as regras propostas são jogáveis como estão.
- **`17 - Sobrecarregar o Defensor`** é a mais rigorosa metodologicamente: tem um callout "O que a
  obra não diz" e outro que antecipa a leitura errada, e todos os números batem com a tabela.
- **`45 - Quando a Adivinhação Falha`** publica a tabela dos seis bloqueios **e declara
  explicitamente que sorte não aparece na lista** — a disciplina de confiabilidade que o projeto
  pede, aplicada a uma ausência.
- **`49`** fecha um conflito de fontes com "não invente um"; **`39`** é o caso mais didático da leva
  imortal; **`08`** trata a ambiguidade "2 pontos × 2%" com callout, marcação e justificativa — foi
  o padrão que usei para corrigir `05`.

---

## O equilíbrio da pasta: as duas medidas pedidas

Ambas as metas foram cumpridas, e uma delas com folga.

**Casos de rank baixo: a meta era 15; o resultado é 22 firmes** (mais dois mistos). São 14 na faixa
`02`–`18` e 8 na faixa `19`–`34`. A pasta está fortemente ancorada em protagonistas mortais de rank
1 a 3 — que é exatamente o que serve a uma designer montando a primeira campanha —, e os 15 casos
de escala imortal estão **agrupados no fim e rotulados como `[segredo]`**, o que é a organização
certa: quem lê na ordem chega neles preparado.

**Casos que terminam em fracasso: a meta era 5; são 6 fracassos limpos** — `09`, `15`, `19`, `34`,
`44` e `45` — mais quatro notas que exibem ramos de fracasso ao lado do sucesso (`36` mostra um
sucesso e três fracassos lado a lado; `40` tem uma das três vias que simplesmente não funciona;
`49` tem um caso B que fracassa; `10` termina em resultado misto).

**Ainda assim, digo que está desequilibrado**, como o briefing pediu que eu dissesse se achasse.
Seis fracassos limpos em 48 são 12,5%: a pasta ensina, majoritariamente, o que funciona. E o
problema não é moral, é de calibragem — uma designer que extraia a curva de dificuldade daqui vai
construir um sistema em que **o plano esperto quase sempre dá certo**, que não é o mundo que as
notas de `01` e `02` descrevem. Mitiguei isso na porta de entrada, com a advertência explícita na
seção "Como usar esta pasta" apontando os seis fracassos por número. A solução de verdade é
encomendar casos novos, e os fracassos mais valiosos seriam os de **rank baixo**: hoje, dos seis,
apenas `09` e `19` são de mortais de rank 3, e nenhum é de rank 1 ou 2.

---

## O que ficou aberto

1. **Bug de renderização em 189 lugares do resto do vault.** Wikilinks dentro de tabelas com `|`
   não escapado, em 33 notas **fora do meu escopo** — e as piores são justamente portas de entrada:
   `00 - Somente o Mestre` (32), `03 - Paths/01 - Visão Geral dos Paths` (25),
   `06 - Forcas e Organizacoes/04 - Continente Central` (19), `04 - Mundo/01 - Visão Geral do Mundo`
   (18), `04 - Mundo/05 - Atlas das Cinco Regiões` (16). A `auditar-links.py` **não detecta** essa
   classe de erro, porque o link está correto no arquivo e só quebra ao renderizar. Recomendo rodar
   o mesmo script de escape no vault inteiro e acrescentar a checagem ao auditor.
2. **Colisões de alias no vault** (30 pares). Corrigi a única que era armadilha nas minhas pastas
   (`Essência Imortal` apontando para `04 - Essência Primordial`). Restam pares como
   `battlefield killer move` em duas notas minhas, `gu formation` dividido com `03 - Paths/09`, e
   `rock gambling` em três notas. Hoje é latente — o vault usa nome exato de arquivo em 100% dos
   links —, mas qualquer link novo por alias resolve para a nota errada sem avisar.
3. **`22 - Aposta de Rochas` não segue o modelo de estudo de caso.** Descreve a instituição, não um
   caso: sem "Situação (mínimo necessário)", sem método numerado, e nunca diz quem fez a jogada nem
   quanto custaram as seis pedras. É boa como nota de cenário e fraca como precedente. Não reescrevi
   porque exige releitura do bloco de capítulos, não edição.
4. **`29 - Brechas de Contrato Mágico`** descreve quatro brechas em abstrato, sem rank nem recursos
   em nenhuma. Elegante, mas impossível de calibrar.
5. **`46 - Curar o Dano para Repetir o Dano`**: a metade do interrogatório não tem um único número.
   A metade econômica salva a nota, mas o veredito de replicabilidade fica apoiado em nada.
6. **A tabela soberana §12 e o caso `33`.** O caso afirma que existe um item de rank 5 que **garante**
   um refino ("once used, it allowed a Gu Master's refinement to succeed for sure") — o que contraria
   frontalmente a estrutura probabilística da seção 12. É canônico e verificado; falta a seção 12
   registrar a exceção. Não editei por estar fora do meu escopo.

---

## As três coisas que eu mudaria com mais tempo

**1. Encomendaria seis fracassos de rank baixo, e os poria no começo da pasta.** É a lacuna
estrutural, não cosmética. Hoje a designer aprende com 22 casos de rank 1–3 que quase todos dão
certo, e depois encontra o fracasso só na escala imortal, onde ele não lhe serve para calibrar uma
mesa inicial. Um fracasso de rank 1 — a emboscada que não fecha, o refino que queima o único Gu, a
fuga que termina com o grupo perdendo o mapa — vale mais para o design de um sistema do que três
duelos entre imortais, porque é ele que define o que acontece quando os jogadores erram.

**2. Faria uma passagem de "primeira ocorrência" automatizada e permanente.** O padrão que dominou
esta revisão foi um só: as notas conceituais definem, as notas de caso presumem. Corrigi 26 pontos
à mão, mas o problema volta a cada nota nova. O que resolve é um script no `_pipeline` com o
dicionário de termos-núcleo e a nota-alvo de cada um, rodando junto com o `auditar-links.py` e
falhando quando um termo aparece numa nota sem link nem glosa. É a diferença entre corrigir uma vez
e não errar de novo.

**3. Daria à pasta `10` uma segunda porta, organizada por problema de design e não por tema.** O
índice atual agrupa por assunto do mundo (rank baixo, combate, dinheiro, escala imortal), que é a
organização certa para quem lê a obra. Mas a designer chega com perguntas de sistema: *como calibro
uma economia de ações? o que impede o personagem de acumular vantagens? o que faço quando um
jogador acha um exploit?* Uma segunda tabela que mapeasse **pergunta de design → casos que a
respondem** transformaria a pasta de arquivo de precedentes em ferramenta de consulta — e é barata
de fazer, porque o conteúdo já está todo escrito nos callouts `Para o design`.

---

## Verificação final

- `python3 _pipeline/auditar-links.py` → **0 links quebrados**, 4.943 links por nome exato de
  arquivo, 0 dependentes só de alias.
- 48/48 notas de caso com o callout `> [!warning] É exceção ou regra?`, com `> [!note] Para o design`
  e com o cabeçalho de confiabilidade dos quatro estados.
- 0 citações `(cap. NN)` no corpo das 48.
- 0 wikilinks de tabela com pipe não escapado nas minhas três pastas.
- Índice: 48 notas citadas duas vezes cada (índice comentado + índice rápido), nenhuma faltando,
  nenhuma órfã.
- 21 links com âncora de seção (`[[Nota#Seção]]`) conferidos um a um contra os títulos reais no
  disco: todos resolvem.
