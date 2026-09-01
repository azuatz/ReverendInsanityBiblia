---
tags:
  - pipeline
  - revisao
status: em-andamento
autor: "revisão externa — designer de TTRPG sem conhecimento prévio da obra"
escopo: "00 (3 notas), 01 - Cultivo (11), 02 - Gu (8), 03 - Paths (18), 04 - Mundo (8)"
---

# Revisão didática — pastas 00 a 04

Leitura crítica feita da posição de quem **nunca leu *Reverend Insanity***, não conhece
nenhum termo do universo e precisa projetar um RPG de mesa a partir *só* deste material.
Tudo que exigiu que eu adivinhasse, deduzisse ou aceitasse por fé está anotado.

Organização: **Bloqueadores** (impedem decisões de design), **Sérios** (causam erro ou
retrabalho), **Menores** (polimento). No fim, o veredito.

> Convenção: cada item traz `arquivo · trecho · tipo · correção sugerida`.

---

## BLOQUEADORES

### B1. A tabela de aptidão contradiz o limiar de 55% — e as próprias notas usam os números impossíveis

- **Arquivos:** `01 - Cultivo/Aptidão.md`, `01 - Cultivo/Ranks e Avanço.md`
- **Trechos:**
  - `Aptidão.md`, tabela: `| **D** | **20–30%** | rank 1; no máximo rank 2 |`
  - `Aptidão.md`: "passar do **rank 1 para o rank 2 exige 55%**"
  - `Aptidão.md`: "um cultivador de 44% pode ficar travado no rank 2 por mais de cem anos"
  - `Aptidão.md`, caso mecânico: "um Mestre Gu **rank 3** de **grau C** ... saltando de **43%** para mais de 90%"
- **Tipo:** furo lógico — três afirmações mutuamente exclusivas.
- **O problema:** se romper 1→2 exige 55% e a aptidão é o teto de armazenamento, então
  (a) o grau D (teto 30%) **nunca** alcança o rank 2, e a coluna "no máximo rank 2" é falsa;
  (b) alguém com 44% não pode estar "travado no rank 2", porque não teria passado do rank 1;
  (c) o rank 3 com 43% do caso mecânico é impossível por dois limiares seguidos.
  Como leiga, passei vinte minutos tentando descobrir qual das quatro frases é a verdadeira —
  e é exatamente a variável de que preciso para calibrar a curva de personagem inteira.
- **Correção:** decidir e aplicar em todas as ocorrências. Três saídas possíveis, e a nota
  deve dizer qual adotou: (1) o 55% é da essência do **estágio de pico**, não da capacidade
  total, e portanto não se compara diretamente com o grau — nesse caso explicar a conversão
  com uma conta; (2) o 55% admite "situações especiais" frequentes (itens, transfusão) e a
  coluna de teto de carreira descreve o caso *com* auxílio — dizer isso na tabela;
  (3) os números do caso mecânico são de personagem que já teve aptidão elevada — informar
  a aptidão *anterior* ao rank 3. Sem essa decisão, não dá para escrever a regra de avanço.

### B2. O único dado canônico citado para 3→4 **refuta** a escada reconstruída 65/75/85 — e a nota não percebe

- **Arquivo:** `01 - Cultivo/Ranks e Avanço.md`
- **Trecho:** "Um dado indireto útil: um Mar Primevo a **90%** de plenitude, sozinho, **não**
  bastou para uma ruptura de **3→4**; foi preciso influxo externo de essência de rank superior."
  — na mesma caixa que propõe **75%** como limiar do 3→4.
- **Tipo:** furo lógico / inferência que se contradiz.
- **O problema:** 90% > 75%. Se a reconstrução estivesse certa, o cultivador teria rompido
  sozinho. Ou o limiar do 3→4 é maior que 90%, ou o limiar não é medido em % da capacidade
  (ver B1), ou o dado canônico tem outra explicação (qualidade, não quantidade — a própria
  nota `Essência Primeva.md` diz "sem a qualidade certa não há ruptura"). A caixa apresenta
  o dado como *apoio* à reconstrução quando ele é o contra-exemplo mais forte contra ela.
- **Correção:** reescrever a caixa admitindo o conflito e propondo a leitura de duas
  variáveis (volume **e** qualidade/estágio), que é a única compatível com os dois fatos.
  Se a escada 65/75/85 for mantida, dizer explicitamente que ela vale "com essência do
  estágio de pico do rank" e que o caso dos 90% falhou por *qualidade* insuficiente.

### B3. A tabela de amplificação de dao marks não fecha, e não há regra de interpolação

- **Arquivo:** `01 - Cultivo/Dao Marks.md`
- **Trecho:** "A obra **fecha a fórmula**, e ela é limpa o bastante para ir direto para uma
  tabela de regras" → `100 = +10% · 1.000 = ×2 · 10.000 = ×10 · 50.000 = ×50`.
- **Tipo:** inferência disfarçada de fato + furo aritmético.
- **O problema:** não existe fórmula que produza essas quatro linhas. De 10.000 para 50.000
  a relação é linear (`×N/1.000`), mas essa mesma relação daria `×1` em 1.000 (a tabela diz
  `×2`) e `×0,1` em 100 (a tabela diz `+10%`). São três regimes diferentes apresentados como
  uma fórmula fechada. Pior para mim: **não sei calcular 4.000 dao marks**, que é o caso que
  vai aparecer em toda ficha de personagem.
- **Correção:** (a) parar de chamar de fórmula fechada — são quatro pontos amostrais da obra;
  (b) marcar como reconstrução a curva escolhida e dar uma **regra de interpolação usável**
  (p. ex. log-linear entre pontos, ou degraus fixos por faixa); (c) dizer o que acontece
  abaixo de 100 e acima de 50.000. Sem isso, o multiplicador central do reino imortal é
  incalculável.

### B4. O "piso de 100.000 dao marks do rank 8" contradiz a aritmética das próprias tabelas

- **Arquivos:** `01 - Cultivo/Dao Marks.md`, `01 - Cultivo/Tribulações e Calamidades.md`
- **Trechos:** faixas por rank (`6: 0–9.000 · 7: 10.000–30.000 · 8: 100.000–300.000`) e a
  caixa "Uma descontinuidade que o texto não explica ... Registrado como lacuna real".
- **Tipo:** furo lógico não detectado / lacuna mal diagnosticada.
- **O problema:** as duas tabelas de `Tribulações` (cadência por rank + dao marks por
  provação) **reproduzem exatamente** os limites das faixas, e o resultado desmente a lacuna:
  - rank 6: 27 calamidades × 250 + 3 tribulações × 750 = **9.000** ✔ (bate com o teto de 9.000)
  - rank 7: 24 × 250 + 3 × 750 + 3 × 7.250 = **30.000** ✔ (bate com o teto de 30.000)
  - rank 8: 24 × 750 + 3 × 7.250 + 3 × 86.750 = **300.000** ✔ (bate com o teto **e** com a
    condição formal de 300.000 do rank 9 em `Tornar-se Venerável.md`)
  Ou seja: pela própria matemática do material, quem entra no rank 8 tem **30.000**, não
  100.000. Não há descontinuidade a explicar — há um número errado (o piso de 100.000).
- **Correção:** corrigir o piso do rank 8 para ~30.000 e **substituir a caixa de lacuna por
  uma caixa de demonstração**, mostrando as três contas acima. Isso transforma o que hoje é
  um buraco declarado no ativo mais valioso do material: uma curva de progressão fechada e
  auditável. (Ver também E1 nos elogios — este sistema numérico é bom, só está mal exposto.)

### B5. Nada explica a unidade de energia do reino imortal, e ela aparece em duas escalas diferentes

- **Arquivos:** `01 - Cultivo/Ascensão Imortal.md`, `01 - Cultivo/Tornar-se Venerável.md`
- **Trechos:** tabela de grades de abertura — "Energia produzida por ano: **10+ contas** /
  20+ / 30+ / 50+"; e condição 1 do rank 9 — "essência imortal de **terceiro grau**: uva
  verde no 6, tâmara vermelha no 7, **lichia branca no 8**, damasco amarelo no 9".
- **Tipo:** jargão nunca definido + furo de sistema.
- **O problema:** "conta" nunca é definido (conta de quê? equivale a quanto? uma ativação de
  Gu? um ano de manutenção?) e nunca reaparece. As denominações de fruta aparecem uma única
  vez, na nota mais secreta da pasta, sem que nenhuma nota diga que a energia imortal **tem
  denominações**. Como designer, não consigo escrever economia imortal nenhuma: não sei a
  unidade, não sei a taxa de câmbio entre uva/tâmara/lichia/damasco e "contas", e não sei
  quanto custa manter um Gu imortal por ano.
- **Correção:** criar uma seção "A economia de energia imortal" em `Ascensão Imortal.md`
  definindo (1) o que é uma conta, (2) a escada de denominações por rank, (3) a relação entre
  as duas, e (4) pelo menos um custo de referência (o que uma abertura de grade média
  sustenta por ano). Se a obra não fornecer, dizer isso e marcar como reconstrução.

### B6. Tempo interno x tempo externo: a interação mais importante do sistema está sem resposta

- **Arquivos:** `01 - Cultivo/Ascensão Imortal.md`, `01 - Cultivo/Tribulações e Calamidades.md`,
  `01 - Cultivo/Longevidade.md`
- **Trechos:** "o relógio das provações conta o tempo *interno*"; "o tempo de vida de um
  imortal é definido como o total que seu corpo já **experienciou**, contando a dilatação.
  É por isso que imortais ricos preferem morar **fora** da própria abertura".
- **Tipo:** furo lógico entre notas / regra ausente.
- **O problema:** se o relógio de tribulações roda no tempo interno da abertura, mas o
  cultivador pode morar **fora** dela para não gastar vida — então ele progride 30× mais
  rápido sem pagar nada. É um exploit óbvio, e o primeiro que qualquer jogador vai tentar.
  As duas notas afirmam as duas coisas e nenhuma cruza com a outra. Também não sei se as
  tribulações acontecem *com o dono ausente* (a nota diz que só ocorrem dentro de aberturas
  imortais, o que sugere que sim — o que agrava o problema).
- **Correção:** uma caixa `> [!warning]` em **ambas** as notas fechando a questão: as
  provações exigem a presença do dono? A produção de recursos roda com ele fora? O tempo de
  vida conta o interno mesmo quando ele está fora? Se a obra não decide, dizer que é lacuna e
  **oferecer duas opções de regra**, porque sem isso a economia do rank 6+ não fecha.

---

## SÉRIOS

### S1. Nenhuma tabela de tribulações explica a regra "a provação maior substitui a menor"

- **Arquivo:** `01 - Cultivo/Tribulações e Calamidades.md`, tabela "A cadência por rank".
- **Trecho:** rank 7 — "calamidade a cada 10; tribulação celestial a cada **50**; grande a
  cada 100" → total "24 calamidades + **3** tribulações celestiais + 3 grandes".
- **Tipo:** confusão estrutural (tabela sem instrução de leitura).
- **O problema:** em 300 anos, "a cada 50" dá **6**, não 3. Levei um bom tempo até deduzir a
  regra tácita: quando duas provações caem no mesmo ano, a maior **substitui** a menor
  (celestiais em 50/150/250 = 3; grandes em 100/200/300 = 3; calamidades 30 − 6 = 24). A regra
  nunca é enunciada, e ela é o que faz todas as contas fecharem.
- **Correção:** enunciá-la em uma linha acima da tabela ("quando duas provações coincidem no
  calendário, só a maior ocorre") e acrescentar uma coluna "duração do rank (300 anos
  internos)". Com isso a tabela vira derivável em vez de decorável.

### S2. A linha do rank 8 na mesma tabela está incompleta

- **Arquivo:** `01 - Cultivo/Tribulações e Calamidades.md`
- **Trecho:** rank 8 → "Total ao completar o rank: **3 tribulações miríades**".
- **Tipo:** densidade/omissão — a coluna promete o total e entrega parte dele.
- **O problema:** as linhas 6 e 7 dão o total completo; a linha 8 omite as 24 celestiais e as
  3 grandes que a própria cadência implica — e são elas que fazem o total bater em 300.000
  (ver B4). O rank 9 tem a linha inteira vazia sem explicar por quê (não há provações? não se
  sabe?).
- **Correção:** completar a linha 8 ("24 celestiais + 3 grandes + 3 miríades") e escrever na
  linha 9 "não há calendário: o rank 9 é o teto" em vez de travessões.

### S3. "Grau D chega ao rank 2" aparece em três notas com números diferentes

- **Arquivos:** `01 - Cultivo/Aptidão.md` (tabela e "regra de bolso"), `01 - Cultivo/Ranks e
  Avanço.md` ("Esse é o número que exclui a maior parte dos graus C e D"), `01 - Cultivo/
  Visão Geral do Cultivo.md` (regra 2).
- **Tipo:** furo lógico / imprecisão que muda a decisão de design.
- **O problema:** "exclui a **maior parte** dos graus C e D" é falso para D: exclui **todos**
  (teto 30% < 55%). Para C exclui 15 dos 20 pontos da faixa. A imprecisão importa porque é
  ela que define quantos NPCs de cada rank existem no mundo — e eu preciso disso para
  distribuir oposição.
- **Correção:** trocar por "exclui **todo** o grau D e cerca de três quartos da faixa C",
  e alinhar a coluna "teto de carreira" da tabela de `Aptidão.md`.

### S4. A conversão passos → porcentagem é apresentada sem explicação e com faixas sobrepostas

- **Arquivo:** `01 - Cultivo/Aptidão.md`
- **Trecho:** "Menos de dez passos: nenhum talento. Dez a vinte passos: grau D. Vinte a
  trinta: grau C. Trinta a quarenta: B. Quarenta a cinquenta: A."
- **Tipo:** confusão estrutural + furo numérico menor.
- **O problema:** (1) os limites se sobrepõem — vinte passos é D ou C? (2) as faixas de
  passos são todas de largura 10, mas as faixas percentuais correspondentes são 10 (D), 20
  (C), 20 (B) e 20 (A), sem que nada explique a não-linearidade; (3) a lacuna 31–39% é
  admitida em nota de rodapé, mas a lacuna equivalente **não** existe do lado dos passos.
  Não consigo escrever a regra de criação de personagem ("role X, converta em %") sem isso.
- **Correção:** usar intervalos fechados/abertos explícitos (10–19, 20–29...) e acrescentar
  uma frase dizendo se a conversão passos→% é linear dentro da faixa ou apenas um rótulo.
  Idealmente, uma coluna a mais na tabela principal com os passos, para haver **uma** tabela
  em vez de duas descrições.

### S5. `Attainment.md` — a escala de oito níveis tem uma célula vazia e nenhum ancoradouro numérico

- **Arquivo:** `01 - Cultivo/Attainment.md`, tabela "A escala completa".
- **Trecho:** `| Quase-grande-grão-mestre | — |`
- **Tipo:** confusão estrutural / falta de utilidade para design.
- **O problema:** a coluna "o que significa" está vazia justamente num dos oito degraus, e a
  tabela não diz **quanto tempo** ou **que esforço** separa um degrau do outro. Como perícia
  do sistema, attainment é o eixo que eu mais preciso graduar (é o que destranca conteúdo), e
  a única âncora numérica da nota é a taxa de sucesso de refino (1% → 50%).
- **Correção:** preencher a célula (ainda que com "degrau real, efeitos não descritos pela
  obra — marcado como lacuna") e acrescentar, para cada degrau, uma âncora: quantas pessoas
  no mundo o têm, ou quanto tempo típico leva. Duas colunas resolvem.

### S6. Falta a nota "Cerimônia do Despertar" que dez outras notas pressupõem

- **Arquivos:** todas as notas de `01`, além de `00 - Trilha do Jogador.md`.
- **Trecho:** `[[Cerimônia do Despertar]]` aparece como link em 5 notas; resolve para um
  *alias* de `Abertura.md`.
- **Tipo:** confusão estrutural.
- **O problema:** o link não está quebrado, mas o destino engana: eu cliquei esperando o
  ritual (quem conduz, quanto custa, o que acontece com quem falha, se dá para repetir, o que
  a sociedade faz com os reprovados) e caí numa nota sobre o órgão. A cerimônia é
  **a cena de criação de personagem** do jogo inteiro — provavelmente a primeira sessão de
  qualquer campanha — e é a que tem menos texto dedicado.
- **Correção:** ou uma nota própria, ou uma seção nomeada em `Abertura.md` com âncora, com o
  procedimento completo e um bloco "Para o design" sobre como converter isso em criação de
  personagem na mesa.

### S7. Números de densidade populacional sem denominador utilizável

- **Arquivo:** `01 - Cultivo/Ranks e Avanço.md`
- **Trecho:** "numa região de bilhões de habitantes existem apenas várias centenas de rank 4
  e menos de cinquenta rank 5 ... Entre dez milhões de Mestres Gu, talvez nenhum consiga
  ascender ao rank 6."
- **Tipo:** falta de utilidade para design.
- **O problema:** tenho o topo da pirâmide e nenhuma das bases. Quantos rank 1 existem por
  cem mil habitantes? Que fração da população passa na cerimônia? Sem isso não consigo
  dimensionar nem um clã, nem uma cidade, nem a raridade dos PCs — que é a primeira decisão
  de tom de um RPG ("vocês são especiais ou são a tropa comum?").
- **Correção:** uma tabela "pirâmide demográfica" com números por 100.000 habitantes, mesmo
  que reconstruídos e marcados como tal. É o tipo de reconstrução que vale mais que a
  ausência.

### S8. `Visão Geral do Cultivo.md` afirma como regra o que outras notas marcam como incerto

- **Arquivo:** `01 - Cultivo/Visão Geral do Cultivo.md`, regra 3 e regra 14.
- **Trechos:** "A densidade dobra a cada estágio; a qualidade **multiplica por dez a cada
  rank**" / "Cem dao marks de uma especialidade dão +10%; mil dobram; dez mil multiplicam por
  dez".
- **Tipo:** inferência disfarçada de fato.
- **O problema:** `Essência Primeva.md` diz que o ×10 só é declarado até o rank 3 — nos ranks
  4 e 5 a tabela registra "sem número declarado". E a lista de dao marks omite os 50.000 e a
  ausência de interpolação (B3). A nota-porta, que é a primeira que eu li, me passou como
  regra fechada duas coisas que as notas de detalhe depois relativizam. Numa nota-porta isso
  é grave: é dela que eu tirei a primeira versão da minha planilha.
- **Correção:** sufixar as duas regras com "(confirmado até o rank 3; ver `Essência Primeva`)"
  e "(quatro pontos amostrais, sem curva fechada; ver `Dao Marks`)".

---

## MENORES

- **M1 · `Visão Geral do Cultivo.md` · densidade.** O "Resumo" tem sete parágrafos de fôlego
  longo e cada um introduz de três a cinco conceitos novos. É bom texto, mas é o *quarto*
  lugar do material onde eu deveria estar quando ainda não sei o que é abertura. Sugestão:
  um diagrama textual de seis linhas ("abertura → essência → Gu → rank/estágio → dao
  marks/attainment → longevidade") antes do resumo em prosa.
- **M2 · `Abertura.md` · jargão.** "grau A", "grau B" aparecem antes de qualquer explicação
  de que existe uma escala de graus (a explicação está em `Aptidão.md`). Uma aposta de meia
  linha resolve: "grau A (o melhor da escala de talento D→A; ver `Aptidão`)".
- **M3 · `Essência Primeva.md` · tabela de tons.** A linha do rank 4 lista dois tons quando
  todas as outras listam quatro. Ou completar, ou dizer "a obra só nomeia dois".
- **M4 · `Ranks e Avanço.md` · jargão.** "Relic Gu" entra em negrito numa tabela sem
  tradução nem definição prévia; só o parágrafo seguinte explica. Inverter a ordem.
- **M5 · `Dao Marks.md` · densidade.** A seção "Efeitos colaterais e detalhes que valem ouro"
  tem oito marcadores densos, cada um com regra própria (selagem de Gu mortais, pureza de
  origem, limite de entrada, pactos, materiais, medidor, autodetonação). São sete regras
  distintas fantasiadas de curiosidades. Promover pelo menos as três primeiras a subseções.
- **M6 · `Longevidade.md` · falta de "Para o design" onde seria óbvio.** A tabela de nove
  métodos alternativos é excelente e não tem bloco de design, quando é literalmente uma lista
  de nove mecânicas de personagem prontas. Um bloco curto ligando cada método a um arquétipo
  jogável rende muito.
- **M7 · `Tornar-se Venerável.md` · números soltos.** "nos últimos milhares de anos, apenas
  duas pessoas conseguiram resistir a um rank 8 sendo rank 7" — sem contexto de quantos rank
  7 existem, o número não calibra nada. Ou ancorar, ou converter em regra ("um rank 7 não
  vence um rank 8; trate como diferença de categoria").
- **M8 · `00 - LEIA-ME.md` · promessa não cumprida.** Diz que a designer pode projetar "sem
  precisar ler a obra", e o material de fato tenta isso — mas a ordem de leitura sugerida
  (as cinco notas) começa por `Visão Geral do Cultivo`, que pressupõe o vocabulário que ela
  mesma introduz. Sugerir antes o `Glossário EN-PT` como leitura zero resolveria.
- **M9 · `00 - Trilha do Jogador.md` · critério não explicado.** A divisão dos Paths entre
  camada 1 e camada 2 ("caminhos avançados: Wisdom, Time, Star, Food, Rule") não diz **por
  que** esses cinco são avançados. Como eu decido onde encaixar um Path novo que eu inventar?
  Uma frase com o critério (raridade? conhecimento restrito? rank mínimo?) basta.

---

## O QUE NÃO PRECISA MEXER (pasta 01)

- **E1 · A aritmética de progressão imortal é o melhor ativo do material.** Cadência de
  provações × valor por provação reproduz exatamente as faixas de dao marks por rank e a
  condição de 300.000 do rank 9 (ver B4). É um sistema fechado, auditável e diretamente
  conversível em tabela de XP. Só precisa ser *mostrado* — hoje está espalhado por três
  notas e nenhuma faz a conta.
- **E2 · `Longevidade.md`** é a melhor nota da pasta. Conceito central enunciado na primeira
  linha, tabela de expectativa, tabela de métodos com preço, escalada de usos (adivinhação →
  aceleração → combate → arma), camada secreta separada e um fecho filosófico que ainda
  entrega gancho de campanha. Serviria de modelo para as outras.
- **E3 · `Attainment.md`** acerta o essencial: separa perícia de poder, dá três consequências
  concretas logo no começo e explica o modo de falha (o poder vira contra o usuário). Só
  faltam as âncoras de S5.
- **E4 · `Abertura.md`** — o bloco "Para o design" (mana + inventário + ficha num objeto só)
  é exatamente o tipo de síntese que eu precisava e não teria feito sozinha.
- **E5 · A separação `conhecimento: comum/especializado/segredo`** funciona e é aplicada com
  consistência. A tabela de "o que cortar" em `00 - Somente o Mestre.md` é um acerto raro.

---

# Pasta `02 - Gu`

## BLOQUEADORES (02)

### B7. "Refino" nomeia duas operações completamente diferentes, e a nota não as separa

- **Arquivo:** `02 - Gu/Refino de Gu.md` (e o eco em `Visão Geral dos Gu.md`, regra 3 e 10)
- **Trechos, todos na mesma nota:**
  - definição de abertura: "refinar um Gu é **substituir a vontade interna do bicho pela
    sua**" — uma guerra de atrito contra um bicho que já existe; "um refino comum leva horas";
    "refinar um Gu banal de nível 1 consome entre **cinco e dezesseis pedras**".
  - e, adiante, na mesma nota: "um refino registrado tinha **mais de dez mil passos**";
    "**uma receita perfeita** é aquela que reduz o número de etapas cruciais ao mínimo";
    "cada tentativa consome um **conjunto completo de materiais imortais**"; "um único Gu de
    nível 5 pode levar **onze anos** para ser refinado"; "taxa de sucesso do nível 5:
    **abaixo de 1 em 1.000**".
- **Tipo:** jargão não desambiguado + furo lógico — o problema mais grave da pasta.
- **O problema:** essas duas coisas não podem ser a mesma operação. Domar um bicho capturado
  não tem receita, não tem materiais, não tem dez mil passos e não custa onze anos. Fabricar
  um Gu a partir de materiais não é uma "guerra de vontades" com um bicho que ainda não
  existe. A nota escorrega de uma para a outra sem aviso, e o leitor leigo só percebe quando
  as contas param de fazer sentido. Pior: `Fusão de Gu.md` diz que fundir é "o principal
  caminho de evolução **e de fabricação** do mundo", enquanto `Refino de Gu.md` descreve um
  segundo processo de fabricação, com receita e materiais, sem nunca dizer como os dois se
  relacionam. Eu tenho **três** verbos (refinar, fundir, fabricar-por-receita) e **duas**
  descrições, e não sei qual mecânica de crafting estou desenhando.
- **Correção:** dividir explicitamente, de preferência em duas seções nomeadas dentro da
  nota (ou duas notas): **(A) Subjugação** — dominar um Gu que já existe: custo em pedras,
  horas, contra-ataque, atalho de aura superior. **(B) Fabricação por receita** — produzir um
  Gu novo a partir de materiais: etapas cruciais/de processamento, taxas, marcas do sucesso,
  regra de unicidade. E uma frase no topo dizendo que o mundo usa a mesma palavra para as
  duas, que é justamente a informação que me faltou.

### B8. As taxas de sucesso não formam uma curva: elas se invertem entre notas

- **Arquivos:** `02 - Gu/Refino de Gu.md`, `02 - Gu/Fusão de Gu.md`, `02 - Gu/Gu Imortais.md`
- **Trechos:**
  - `Refino`: mortais — "nível 5: **abaixo de 1 em 1.000**" (isto é, < 0,1%); imortais —
    "6: **menos de 1%** · 7: ~0,1% · 8: ~0,01%".
  - `Fusão`: "1 a 3: fácil · **4 a 5: abaixo de 10%** · 6 (Gu Imortal): **cerca de 1%**".
- **Tipo:** furo numérico entre notas.
- **O problema:** (a) produzir um Gu de **nível 5** aparece como `<0,1%` numa nota e
  `<10%` na outra — duas ordens de grandeza de diferença para o mesmo resultado, sem que
  nenhuma das duas mencione a outra; (b) juntando as tabelas, um Gu **mortal** de nível 5
  (<0,1%) seria **dez vezes mais difícil** que um Gu **Imortal** de nível 6 (<1%), o que
  contradiz frontalmente a tese das duas notas de que o nível 6 é uma mudança de categoria;
  (c) "abaixo de 10%" é um limite superior inútil para calibrar — 9% e 0,01% cabem os dois.
- **Correção:** uma única tabela consolidada, provavelmente em `Refino de Gu.md`, com uma
  linha por nível (1 a 8), uma coluna por operação (subjugar / fundir / fabricar) e valores
  centrais em vez de tetos. Onde só houver teto, escrever "entre X e Y". Sem isso não consigo
  precificar nada: a taxa de sucesso é o parâmetro que define a economia inteira do mundo, e
  a própria nota diz isso ("Este é o número que define a economia inteira do mundo").

### B9. Não existe economia de ação: os limites de multitarefa se contradizem em três notas

- **Arquivos:** `01 - Cultivo/Visão Geral do Cultivo.md` (regra 7), `02 - Gu/Refino de Gu.md`,
  `02 - Gu/Killer Moves.md`, `02 - Gu/Fusão de Gu.md`
- **Trechos:**
  - regra 7: "Controlar **dois** Gu ao mesmo tempo já é destaque; **três** é o teto da elite;
    quatro é excepcional; cinco só com constituições extremas."
  - `Refino`: "Refinar **dois** Gu simultaneamente já destaca alguém; três é raro; quatro é o
    teto excepcional."
  - `Killer Moves`: "A escala típica de um golpe mortal é de cerca de **três Gu**. Mas
    existem golpes com **catorze** Gu, e um documentado com cerca de **quarenta e dois**." E
    ainda: "o limite pessoal citado é de cerca de **cinco golpes simultâneos**".
  - `Fusão`: durante a fusão "o Mestre precisa controlar **cada Gu envolvido separadamente e
    ao mesmo tempo**".
- **Tipo:** furo lógico estrutural / falta de utilidade para design.
- **O problema:** se controlar dois Gu simultaneamente já é destaque, ninguém consegue
  acionar um golpe de quarenta e dois. Ou os golpes combinados **não** contam como
  multitarefa (porque são coreografados como uma unidade), ou o limite de dois só vale para
  ações independentes — mas nenhuma nota diz qual das duas. Essa é a decisão de que depende
  a **economia de ações do combate inteiro**: quantas coisas um personagem faz por turno é
  literalmente a primeira regra que eu preciso escrever, e o material me dá quatro números
  incompatíveis.
- **Correção:** um bloco `> [!warning]` em `Killer Moves.md` (com espelho na regra 7) que
  enuncie a distinção: `N Gu articulados num golpe único = 1 tarefa` contra `N Gu com
  comandos independentes = N tarefas`, e diga onde o limite de 2–5 se aplica. Se a obra não
  resolve, marcar como reconstrução e escolher — mas escolher.

## SÉRIOS (02)

### S9. Quantos Gu um Mestre carrega: três números diferentes, e o argumento de design usa o errado

- **Arquivos:** `02 - Gu/Visão Geral dos Gu.md` (regra 6), `02 - Gu/O que é um Gu.md`,
  `02 - Gu/Usar e Alimentar Gu.md`
- **Trechos:** "Um Mestre médio sustenta **quatro ou cinco** Gu do próprio nível" (repetido
  nas duas primeiras notas) contra a tabela da terceira: "Mestre comum de nível baixo:
  **2 a 3** · nível 4 a 5: 4 a 5 · veterano de nível 5: até cerca de 7".
- **Tipo:** furo numérico + conclusão de design construída sobre ele.
- **O problema:** "Mestre médio" e "Mestre comum de nível baixo" descrevem a mesma pessoa e
  recebem números diferentes. E a inferência mais citada do domínio — "o teto é de quatro ou
  cinco slots e as funções necessárias são seis, então a matemática não fecha e Mestres Gu
  operam em grupos" — usa 4–5 quando o personagem inicial típico tem **2 a 3**. Com o número
  certo, o argumento fica ainda mais forte (2–3 slots contra 6 funções), mas o tamanho do
  grupo que ele implica muda completamente: 2 pessoas contra 5.
- **Correção:** adotar a tabela por perfil como fonte única, corrigir as duas ocorrências de
  "quatro ou cinco" para "2 a 3 no início da carreira, 4 a 5 no auge mortal" e refazer o
  argumento das seis funções com os números por faixa. Isso me dá diretamente o tamanho
  recomendado de grupo por nível de campanha, que é ouro puro.

### S10. "Formação" é um conceito central e nunca é definido

- **Arquivos:** `02 - Gu/Killer Moves.md` (dezenas de ocorrências), `02 - Gu/Gu Imortais.md`,
  `02 - Gu/Refino de Gu.md`
- **Trechos:** "formação de Gu", "formação de batalha antiga", "formações imortais",
  "montado como uma **formação** dedicada", "criar uma **formação** grande e complexa
  (milhões de Gu comuns e vinte Gu Imortais)", e na tabela da escala: "Formação de batalha
  antiga / formação de Gu / casa de Gu | territorial".
- **Tipo:** jargão nunca definido.
- **O problema:** eu não sei o que é uma formação. É um golpe grande? Uma construção física?
  Um arranjo permanente no terreno? A tabela de escala junta três coisas de nomes diferentes
  numa linha só, como se fossem sinônimos, e uma delas (casa de Gu) tem definição própria em
  outra seção — o que sugere que as outras duas **não** são sinônimos. É provavelmente o
  segundo sistema mais importante da pasta (é o que produz território defendido, e o que
  aparece em quase todo conflito de grande escala) e não tem uma linha de definição.
- **Correção:** uma subseção "Formações" em `Killer Moves.md` com três frases: o que é, como
  difere de um killer move e de uma casa de Gu, e quem consegue montar uma. E desmembrar a
  linha da tabela de escala em três linhas com escopos distintos.

### S11. A regra "só se usa Gu do próprio rank" tem exceções espalhadas por cinco notas

- **Arquivos:** `01 - Cultivo/Ranks e Avanço.md`, `01 - Cultivo/Abertura.md`,
  `02 - Gu/O que é um Gu.md`, `02 - Gu/Gu Vital.md`, `02 - Gu/Refino de Gu.md`
- **Trechos:** a regra dura ("forçar um Gu acima do próprio rank destrói a abertura") contra:
  o Gu de rank 5 movido a medula óssea; os Gu que exigem **estado mental** e não recurso; o
  caso do Gu Vital de nível 6 carregado por um cultivador de **nível 1**; os Gu Imortais do
  "estilo do isolamento humano" que "foram **desenhados para serem usáveis por mortais**"; e
  o Gu de nível 6 que se camufla de uma inspeção de nível 4 na abertura de um rank 1.
- **Tipo:** confusão estrutural — a regra e suas exceções nunca aparecem juntas.
- **O problema:** a regra que mais estrutura o poder do sistema tem pelo menos cinco furos
  documentados, cada um numa nota diferente, e nenhuma nota os lista. Ao ler `Ranks e
  Avanço.md` eu escrevi "trava rígida de rank" na minha planilha; três notas depois descobri
  que a trava é porosa e que **a porosidade é onde estão os personagens interessantes**.
- **Correção:** uma seção "As exceções à trava de rank" em `Ranks e Avanço.md` listando as
  cinco, cada uma com a mecânica que a permite (trocar o combustível · requisito de
  convicção · vínculo de Gu Vital · Gu projetado para mortais · Gu adormecido/debilitado).
  Cinco linhas resolvem, e viram cinco arquétipos jogáveis.

### S12. Jargão introduzido sem definição dentro de `02`

- **`Refino de Gu.md`:** "as **marcas do sucesso**: marcas gravadas no corpo que, consumidas
  num refino, eliminam a probabilidade natural de falha" — de onde vêm? Como se ganha uma?
  São dao marks? São únicas por pessoa? A nota diz que são intransferíveis e que cobrem até o
  nível 6, e nada mais. É o item mais valioso da profissão e não tem origem.
- **`Gu Imortais.md`:** "refazer um Gu Imortal destruído a partir da **insígnia deixada no
  refino original**" — "insígnia" aparece uma única vez em todo o material.
- **`Killer Moves.md`:** "**quase-campo de batalha**" entra direto na tabela de escala sem
  definição, e "**dedução passiva**" (em "observadores com dedução passiva") idem.
- **Correção:** meia linha de definição em cada primeira aparição, no padrão que o resto do
  material já usa (`==termo (original em inglês)== = definição`).

### S13. `Killer Moves.md` — a nota mais longa da base e a mais difícil de usar

- **Arquivo:** `02 - Gu/Killer Moves.md` (~3.500 palavras, a maior das 45 notas revisadas)
- **Tipo:** densidade excessiva / confusão estrutural.
- **O problema:** o conteúdo é excelente, mas a nota empilha nove sistemas distintos —
  categorias por operador, por efeito, por relação com os Gu, totens, escala, criação,
  melhoria, backlash, condensação — cada um com regras próprias, e o leitor só descobre
  quantos são ao chegar ao fim. Não há mapa no começo. A seção de totens sozinha (com
  hierarquia de três graus, procedimento de aquisição, dois modos de uso e uma tabela de
  vantagens) é uma nota inteira disfarçada de subseção, e ela trata de um sistema que **não
  usa Gu** — ou seja, é a única forma de poder do mundo que foge da premissa da pasta.
- **Correção:** (a) uma lista de cinco linhas no topo dizendo o que a nota cobre; (b)
  promover **Golpes Totêmicos** a nota própria — é matéria de arquétipo (o guerreiro que
  grava poder no corpo, sem bocas para alimentar) e hoje está enterrada; (c) mover
  "Condensação" e "A unificação final" para o fim como apêndice teórico, já que são
  `segredo` e não afetam a mesa no dia a dia.

## MENORES (02)

- **M10 · `Visão Geral dos Gu.md` · promessa quebrada.** A nota-porta diz "um único exemplar
  no mundo inteiro para cada tipo" na lista de tópicos, mas a nota de destino esclarece que
  isso vale só dos níveis 6 a 8 e que **variantes** contam como Gu distintos. A ressalva
  (que é a válvula que impede o sistema de travar) deveria estar já na porta.
- **M11 · Marcadores `conhecimento:` no meio do corpo.** Várias notas de `02` usam uma linha
  solta `conhecimento: especializado` / `segredo` para marcar seções. É um recurso ótimo —
  mas o `00 - LEIA-ME` só documenta o campo do **cabeçalho** e os três tipos de destaque.
  Acrescentar um parágrafo lá ("seções internas podem ter marcação própria, que prevalece
  sobre a da nota") evita que eu distribua a nota inteira por engano.
- **M12 · `Fusão de Gu.md` · tabela sem âncora.** "Engenharia reversa: mestre · deduzir
  receita nova: grão-mestre · criar série nova: quase-grande-grão-mestre" não linka para
  `[[Attainment]]`, onde esses níveis são definidos. É a única tabela do material que usa a
  escala de attainment sem apontar para ela.
- **M13 · `Usar e Alimentar Gu.md` · a melhor tabela da base merece um total.** A tabela de
  dietas é excelente, mas para orçar uma campanha eu preciso de **custo por mês em pedras
  primevas** por nível de Gu — que existe disperso no caso mecânico ("um Gu comum de nível 2
  custa cerca de uma a duas pedras por dia"). Promover isso a uma coluna ou a uma tabela de
  custo mensal por nível 1–5 tornaria a nota diretamente jogável.
- **M14 · `Gu Vital.md` · uma pergunta óbvia sem resposta.** A nota diz que o Gu Vital é
  escolhido na adolescência com "um Gu barato que o clã pôde pagar" e que trocar depois é uma
  cirurgia com risco de morte — mas nunca diz **quando** a consagração acontece nem se é
  automática (o primeiro que você refina) ou deliberada. `Visão Geral dos Gu.md` diz "o
  primeiro Gu que você refina vira seu Gu Vital"; a própria nota diz que a definição
  precisa **não** é essa. Uma frase resolvendo isso é obrigatória: é uma escolha de criação
  de personagem.

## O QUE NÃO PRECISA MEXER (02)

- **E6 · `Gu Imortais.md` é a melhor nota do material inteiro.** A regra de unicidade, a
  trava de autodestruição e a conclusão de que "roubar destrói o item, logo negociar vira a
  via dominante" formam um argumento causal completo que eu poderia levar direto para o
  documento de design. O bloco "Para o design" acerta o ponto certo (unicidade global =
  geopolítica de objetos, não corrida de estatísticas).
- **E7 · A tabela de backlash por progresso de ativação** (`Killer Moves.md`: leve / médio /
  grave / fatal conforme o lampejo em que o golpe é interrompido) é a melhor mecânica pronta
  de toda a base. Vai para o jogo praticamente sem tradução.
- **E8 · O quadro comparativo killer move × casa de Gu Imortal** é exemplar: seis linhas,
  eixos opostos, decisão de build imediata. É o modelo que as outras notas deveriam seguir
  quando comparam duas coisas.
- **E9 · `Gu Vital.md`** é curta, completa e honesta — inclusive registra a contradição que a
  obra deixa em aberto (a abertura imortal sem Gu Vital) em vez de escondê-la.
- **E10 · O bloco "Para o design" de `Usar e Alimentar Gu.md`** ("um cerco derrota um mago
  não por dano, mas por fome dos bichos dele") é o melhor insight de campanha da base.

---
