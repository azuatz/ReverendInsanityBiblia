---
tags:
  - pipeline
  - revisao
status: concluido
achados: "16 bloqueadores, 25 sérios, 28 menores, 21 elogios específicos"
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

# Pasta `03 - Paths`

> **Método:** revisei a nota-porta integralmente e quatro caminhos como amostra, escolhidos
> para cobrir as três camadas de conhecimento e os dois perfis de nota: `Blood Path`
> (comum, caminho de combate), `Sword Path` (comum, caminho de vitrine), `Wisdom Path`
> (especializado, caminho transversal) e `Heaven Path` (segredo, caminho-limite).
>
> **O padrão se repete, e é bom.** Os quatro seguem o mesmo gabarito — *Em uma frase →
> Filosofia e identidade → Mecânicas típicas → Gu representativos (tabela) → Em combate e
> fora dele → Sinergias e fraquezas → Para o design → Praticantes notáveis (sem enredo) →
> Relações* — e os quatro abrem remetendo à nota-porta ("Para entender o que é um 'caminho',
> veja [[Visão Geral dos Paths]]"), que é exatamente a cortesia didática que faltou em `01`.
> Todos os quatro entregam um **arquétipo nomeado** no bloco de design. Esta é a pasta mais
> bem construída das quatro, e os problemas abaixo são de *coerência entre pastas*, não de
> forma. Presumo, pela amostra, que o mesmo valha para os treze caminhos que não li.

## BLOQUEADORES (03)

### B10. Existem duas escalas de attainment canônicas, com números de degraus diferentes

- **Arquivos:** `01 - Cultivo/Attainment.md` × `03 - Paths/Visão Geral dos Paths.md`
- **Trechos:**
  - `Attainment.md`, "A escala completa": Ordinário · Mestre · Quase-grão-mestre ·
    Grão-mestre · Quase-grande-grão-mestre · Grande grão-mestre · Quase-supremo grão-mestre ·
    Supremo grão-mestre — **oito degraus**.
  - `Visão Geral dos Paths.md`: "Escala canônica, em **nove degraus**", tabela numerada de 1 a
    9, que insere **quase-mestre** entre "comum" e "mestre".
- **Tipo:** furo lógico entre notas, ambas marcadas `status: consolidado`.
- **O problema:** o eixo de perícia do sistema tem duas versões oficiais, e elas divergem
  logo no degrau 2 — o mais usado, porque é onde estarão os personagens iniciais. Todos os
  requisitos do material são enunciados por *nome* de degrau ("exige grão-mestre", "mestre
  para anexar uma terra rank 6"), então a numeração muda o alinhamento de tudo: o
  "grão-mestre" é o 4º degrau numa nota e o 5º na outra. Não consigo montar uma tabela de
  perícia sem escolher, e escolher errado desalinha todos os pré-requisitos do material.
- **Correção:** eleger `Attainment.md` como fonte única (é a nota especializada), corrigir a
  tabela de `Visão Geral dos Paths.md` para apontar para lá em vez de reproduzir a escala, e
  decidir a existência do "quase-mestre" — se existir, ele também precisa entrar em
  `Attainment.md`, que hoje pula direto de Ordinário para Mestre.

### B11. O teto da herança é "grande grão-mestre" numa nota e "quase-supremo grão-mestre" na outra

- **Arquivos:** `03 - Paths/Visão Geral dos Paths.md` × `01 - Cultivo/Attainment.md`
- **Trechos:**
  - `Paths`, regra 8: "Legados, sonhos de mestres mortos e transmissões diretas elevam o
    domínio de alguém até **grande grão-mestre, nunca até o topo**." Repetido na tabela
    ("grande grão-mestre — **teto de qualquer herança**") e em "O que só o mestre sabe".
  - `Attainment.md`: "uma herança dessas elevou um caminho direto a **quase-supremo
    grão-mestre**; outra elevou alguém de grão-mestre a grande grão-mestre instantaneamente"
    — e a regra formulada como "**nenhum verdadeiro significado concede supremo grão-mestre**".
- **Tipo:** furo lógico — as duas notas põem o teto em degraus diferentes.
- **O problema:** a diferença é de um degrau inteiro e ela é decisiva, porque é a fronteira
  entre "o que dá para comprar/herdar" e "o que exige mérito próprio" — a decisão econômica
  central do endgame. Com o teto em grande grão-mestre, existe uma faixa de dois degraus que
  nenhuma riqueza alcança; com o teto em quase-supremo, existe uma só. Isso muda diretamente
  o desenho da curva de recompensas de uma campanha longa.
- **Correção:** adotar a formulação de `Attainment.md` (que é a mais precisa e traz o motivo:
  inovação não se herda) e corrigir as três ocorrências em `Paths`. Vale a pena manter, na
  nota de Paths, a frase que explica *por quê* — hoje ela só afirma o teto.

### B12. "Dao Lord" tem duas definições incompatíveis, e uma delas cria um degrau de rank novo

- **Arquivos:** `01 - Cultivo/Tornar-se Venerável.md` × `03 - Paths/Visão Geral dos Paths.md`
- **Trechos:**
  - `Tornar-se Venerável`: "Um Venerável com supremo grão-mestre no caminho principal alcança
    o status de Dao Lord: ele passa a sentir e refinar automaticamente todos os dao marks
    daquele caminho **no mundo inteiro**" — apresentado como consequência automática.
  - `Paths`: Dao Lord é quem "refinou as marcas daquele caminho sobre **uma porção de céu e
    terra**... *possuir uma porção de céu e terra é o que define um Dao Lord*", o status é
    "**recuperável**, o que faz dele um cargo disputável e não um troféu permanente", e vem
    numa hierarquia formal: "**Mestre Gu Imortal comum → pseudo-Venerável → Venerável → Dao
    Lord**".
- **Tipo:** furo lógico + jargão redefinido sem aviso.
- **O problema:** três divergências de uma vez. (a) **Escopo**: o mundo inteiro contra uma
  porção dele — a diferença entre "há um dono para cada caminho no planeta" e "há vários
  senhores territoriais por caminho", que são cenários completamente distintos. (b)
  **Permanência**: consequência automática do supremo grão-mestre contra cargo disputável e
  reconquistável. (c) A hierarquia de `Paths` transforma **pseudo-Venerável** num degrau da
  escada, enquanto `Tornar-se Venerável` o define como *rótulo de fracasso* — alguém que
  falhou a terceira tribulação miríade e morreu. Não são a mesma coisa, e a versão de
  `Paths` sugere uma progressão que a outra nota nega.
- **Correção:** uma seção única sobre Dao Lord (proponho em `Tornar-se Venerável.md`, com a
  nota de Paths apenas remetendo) que decida escopo e permanência, e uma frase separando
  "pseudo-Venerável" (fracasso documentado) de qualquer leitura de degrau intermediário. Se
  a obra sustentar as duas leituras, marcar como divergência e escolher uma para o jogo.

## SÉRIOS (03)

### S14. Dois caminhos diferentes são apresentados como "o primeiro/a mãe de todos"

- **Arquivo:** `03 - Paths/Visão Geral dos Paths.md`, regras 3 e 11 (e o eco em
  `03 - Paths/Heaven Path.md`, seção "História").
- **Trechos:** regra 3 — "**Espaço e tempo são os dois caminhos primordiais** — descritos como
  a base do céu e da terra desde a era imemorial. **Todos os outros vieram depois**"; regra
  11 — "O caminho da regra é a **'mãe' de todos** — o mais universal... Outros caminhos
  brotam dele como sub-ramos".
- **Tipo:** furo lógico interno à mesma nota.
- **O problema:** as duas regras se contradizem na mesma lista, com sete regras de distância.
  E `Heaven Path.md` desempata contra a regra 11 sem perceber: o caminho da regra tem um
  **criador datado** ("dois milhões de anos depois" do primeiro supremo grão-mestre de
  refinamento), portanto não pode ser a origem de caminhos que já existiam. A leitura que
  concilia tudo — regra é a mãe *conceitual*, espaço e tempo são os mais *antigos* — não está
  escrita em lugar nenhum, e eu precisaria inventá-la.
- **Correção:** distinguir explicitamente **anterioridade histórica** (espaço e tempo) de
  **generalidade conceitual** (regra), em uma frase em cada regra. É uma correção de dez
  palavras que resolve o que hoje parece um erro de pesquisa.

### S15. `Heaven Path` viola três regras de `Tribulações e Calamidades`

- **Arquivos:** `03 - Paths/Heaven Path.md` × `01 - Cultivo/Tribulações e Calamidades.md`
- **Trechos de `Heaven Path`:** "Refinar marcas do céu enfurece a vontade do céu. As marcas
  restantes se reúnem e disparam uma **tribulação de miríade**"; "o caso registrado: **três
  marcas refinadas** dispararam uma floresta de raios que cobriu **mais de cem mil
  quilômetros** em instantes"; "passar de cerca de duzentas marcas numa única pausa faz o
  processo **reiniciar** a tribulação".
- **Contra `Tribulações`:** (1) "calamidades e tribulações **só ocorrem dentro de aberturas
  imortais, nunca nas terras do mundo comum**" — mas uma floresta de raios de cem mil km
  parece o mundo externo; (2) o calendário de provações é **fixo por rank e por tempo
  interno**, enquanto aqui a tribulação é disparada por uma **ação voluntária**, quantas
  vezes o cultivador quiser; (3) "**somente dez pessoas em toda a história passaram pelas
  três miríades** — e são exatamente os dez Veneráveis", mas aqui alguém enfrenta miríades
  repetidas num único ciclo de refino, sem ser Venerável (a nota afirma que nenhum Venerável
  cultivou o caminho).
- **Tipo:** furo lógico entre notas — atinge o subsistema de progressão do reino imortal.
- **O problema:** a tribulação miríade é, ao mesmo tempo, o portão dos dez maiores da
  história e um custo operacional rotineiro de uma profissão. Não pode ser as duas coisas com
  as mesmas regras. Se eu escrever a regra de tribulação a partir de `01`, o caminho do céu
  fica impossível; se escrever a partir de `03`, o rank 9 deixa de ser raro.
- **Correção:** ou nomear a provação do caminho do céu de outra forma ("tribulação induzida",
  distinta da miríade do calendário), ou acrescentar em `Tribulações` uma seção "provações
  fora do calendário" que reconheça a categoria e diga como ela difere. E revisar a frase
  "só ocorrem dentro de aberturas imortais", que a amostra já contradiz.

### S16. A "trava de rank" é violada por um exemplo concreto que atravessa duas pastas

- **Arquivos:** `01 - Cultivo/Aptidão.md` × `03 - Paths/Blood Path.md`
- **Trechos:** `Aptidão` — "um Mestre Gu **rank 3** de grau C usou um Gu demoníaco roubado
  para converter cada morte ao seu redor em aptidão permanente"; `Blood Path`, tabela — "Crânio
  de Sangue | **4** | Eleva a aptidão do usuário permanentemente, com sangue de vítimas".
- **Tipo:** furo lógico só visível cruzando as pastas.
- **O problema:** é o mesmo Gu, e o caso mostra um rank 3 acionando um Gu de nível 4 — o que
  `Ranks e Avanço.md` diz que "destrói a abertura: morte ou transformação irreversível". Nem
  a nota de aptidão nem a de sangue registram que ali há uma exceção sendo usada. Junto com
  as outras exceções que já listei (S11), isso confirma que a trava de rank é bem mais porosa
  do que o material admite — e que os casos mais interessantes do mundo estão justamente nos
  furos.
- **Correção:** anotar no caso mecânico de `Aptidão.md` qual exceção está em jogo (é um Gu
  demoníaco roubado — provavelmente combustível alternativo ou sobrecarga deliberada), e
  incluí-lo na seção de exceções proposta em S11.

### S17. O mesmo Gu de adivinhação aparece com dois níveis diferentes

- **Arquivos:** `01 - Cultivo/Longevidade.md` × `03 - Paths/Wisdom Path.md`
- **Trechos:** `Longevidade` — "um **Gu de adivinhação de rank 9** falhava em oito de cada dez
  ativações, com backlash de dez a setenta anos"; `Wisdom Path`, tabela — "**Gu do Segredo
  Celestial** (deduz sem evidências) | cerca de 80% de falha; cada falha consome 10 a 70 anos
  de vida", e na tabela de Gu representativos: "Segredo Celestial ⭐ | **7 → 8**".
- **Tipo:** furo numérico / atribuição inconsistente.
- **O problema:** a estatística é idêntica (80% de falha, 10–70 anos), então é o mesmo Gu —
  mas ele é rank 9 numa nota e 7→8 na outra. Como o nível determina quem pode usá-lo, isso
  muda completamente quem na mesa tem acesso ao efeito de adivinhação mais importante do
  mundo. `Wisdom Path` ainda lista separadamente um "Gu da Sabedoria ⭐ | 9", o que sugere que
  `Longevidade` confundiu os dois.
- **Correção:** conferir e alinhar; se forem dois Gu distintos com números parecidos, dizer
  isso explicitamente, porque a coincidência é grande demais para o leitor não tropeçar.

### S18. As tabelas de "Gu representativos" têm colunas de nível vazias e uma notação não explicada

- **Arquivos:** `03 - Paths/Blood Path.md` (quatro linhas com `—` na coluna Nível),
  `03 - Paths/Sword Path.md`, `03 - Paths/Heaven Path.md`.
- **Trechos:** "Rastro de Sangue ⭐ | — |", "Juramento de Sangue ⭐ | — |", "Vingança de Sangue
  / Sangue Frio ⭐ | — |"; e a notação "Guilhotina de Sangue | **5 → 6**", "Segredo Celestial ⭐
  | **7 → 8**", "Lâmina Única ⭐ | **6 (máximo)**".
- **Tipo:** confusão estrutural (tabela sem instrução de leitura).
- **O problema:** (a) a legenda diz "⭐ = Gu Imortal, único no mundo", e a base já me ensinou
  que Gu Imortal significa nível 6 a 8 — então uma linha com ⭐ e nível `—` é um dado que eu
  sei ser preenchível e não foi; (b) a notação `X → Y` nunca é explicada (evolui? tem duas
  versões? sobe com o dono?) e `Gu Imortais.md` diz que **não podem coexistir** duas versões
  do mesmo Gu Imortal em níveis diferentes, o que torna `7 → 8` uma afirmação carregada;
  (c) "6 (máximo)" introduz uma terceira convenção. Três notações numa coluna só.
- **Correção:** uma legenda de duas linhas, comum às 17 notas de caminho, definindo `—`
  ("nível não informado pela obra"), `X → Y` ("existe em duas formas; a superior consome a
  inferior — ver `Gu Imortais`") e `X (máximo)` ("teto de evolução"). É a correção de melhor
  relação custo-benefício desta pasta, porque replica em 17 notas de uma vez.

## MENORES (03)

- **M15 · `Visão Geral dos Paths.md` · jargão.** "Dentro do **Rio do Tempo**, todo caminho que
  não seja o do tempo cai a menos de 10%" — "Rio do Tempo" aparece sem definição nem link.
  É citado como se eu já soubesse o que é.
- **M16 · Duas listas de caminhos com critérios diferentes.** O "Mapa desta pasta" agrupa os
  17 caminhos em quatro famílias (combate/corpo · mente/alma · fundamentais/abstratos ·
  infraestrutura), enquanto `00 - Trilha do Jogador.md` os reparte por camada de conhecimento
  (9 comuns + 5 avançados + 3 secretos). Ambas as listas estão completas e corretas, mas
  nenhuma menciona a outra — e a segunda não diz o critério (ver M9). Um "ver também" cruzado
  resolve.
- **M17 · `Blood Path.md` · afirmação forte sem contexto.** "o caminho do sangue é descrito
  como **pior que queimar almas**" — como leiga, não faço ideia de que queimar almas seja o
  pior crime de referência do mundo; a comparação só funciona para quem já conhece a escala.
  Uma cláusula ("queimar almas, que é a atrocidade-padrão contra a qual o mundo mede as
  outras") converte a frase de opaca em eficaz.
- **M18 · `Wisdom Path.md` · detalhe órfão.** "é a erudição no **caminho do fogo** que regula
  essa resistência" — o caminho do fogo não tem nota nem consta do mapa dos 17. Aparece
  também na regra 13 da nota-porta ("no do fogo, passa-se a armar armadilhas indetectáveis").
  Ou entra no mapa como caminho menor documentado, ou ganha uma nota de rodapé dizendo que é
  citado de passagem e não coberto.
- **M19 · `Heaven Path.md` · densidade no lugar certo, mas sem panorama.** É a nota mais
  conceitualmente difícil da amostra (marcas irrestritas, tribulação involuntária, teto por
  janela, restrição de abertura) e é a única que se beneficiaria de três linhas de resumo
  antes de "Filosofia e identidade" — algo como "para cultivar este caminho você precisa de X,
  paga Y e ganha Z". Hoje o leitor só monta esse quadro ao chegar ao bloco de design.

## O QUE NÃO PRECISA MEXER (03)

- **E11 · O gabarito das notas de caminho é a melhor decisão editorial do material.** Mesma
  ordem de seções, mesma primeira frase remetendo à porta, mesmo fecho com arquétipo. Depois
  da segunda nota eu já sabia onde procurar cada coisa — o que não acontece em nenhuma outra
  pasta. **Não mexer nisso.**
- **E12 · "Sinergias e fraquezas" com nomes de outros caminhos** é exatamente a informação de
  que preciso para montar composição de grupo e matriz de contramedidas. É raro um material de
  cenário entregar isso mastigado.
- **E13 · A regra de que um caminho é *inventado* por alguém** (`Visão Geral dos Paths`, "Como
  nasce um caminho") é a melhor ideia de worldbuilding da base: transforma "escola de magia"
  em "corpo de conhecimento com autor, data e lacunas", e o corolário — o caminho dos sonhos
  existe de fato mas não de direito — é um prêmio de campanha pronto.
- **E14 · `Heaven Path.md`** apesar de M19: a mecânica de progressão que convoca uma
  catástrofe adaptativa, com teto por janela e decisão de ganância a cada pausa, é a resposta
  mais completa que a base dá à pergunta "como fazer subir de nível ser dramático".
- **E15 · O bloco "Praticantes notáveis (sem enredo)"** cumpre a promessa do LEIA-ME de não
  contar a história e ainda assim me dar figuras utilizáveis. Boa disciplina de escopo.

---

# Pasta `04 - Mundo`

## BLOQUEADORES (04)

### B13. Quatro notas terminam com lixo de geração (`</content>`, `</invoke>`)

- **Arquivos:** varri a base com `grep -rln "</content>\|</invoke>"` e são **doze notas** —
  as **oito** de `04 - Mundo` (em `Visão Geral do Mundo.md` há `</content>` *e* `</invoke>`)
  e as **quatro** de `07 - Veneráveis e Legados`, que não estava no meu escopo mas está
  contaminada igual. Nenhuma nota de `01`, `02` ou `03` foi afetada.
- **Tipo:** defeito de produção.
- **O problema:** não é conteúdo, é uma etiqueta de ferramenta que vazou para dentro das
  notas finais. Não achei isso em nenhuma nota de `01`, `02` ou `03` — é específico desta
  pasta, o que sugere um lote gerado com um erro de fechamento. Coloco como bloqueador porque
  (a) me fez desconfiar, na primeira vez, se a nota tinha sido **truncada** — e eu não tinha
  como saber se faltava conteúdo depois daquilo; e (b) se este material for entregue a
  terceiros ou publicado, é o tipo de coisa que destrói a confiança no resto.
- **Correção:** apagar as linhas e varrer as outras pastas com `grep -rn "</content>\|</invoke>"`
  para confirmar que só estas quatro foram afetadas. Conferir também se algo foi perdido no
  fim de cada uma: `Visão Geral do Mundo.md` termina com um único item em "Relações", o que
  é pouco para uma nota-porta e pode ser sintoma de truncamento real.

### B14. A nota-porta do mundo apaga a distinção ontológica que a pasta `02` chama de fundamental

- **Arquivos:** `04 - Mundo/Visão Geral do Mundo.md` (regra 4) × `02 - Gu/O que é um Gu.md`
- **Trechos:**
  - `Visão Geral do Mundo`, regra 4: "**Todo Gu contém um fragmento da Grande Dao** — uma lei
    do mundo em miniatura."
  - `O que é um Gu`, "A camada metafísica": "há uma **fronteira ontológica nítida** no topo:
    Gu comuns (1–5) contêm *marcas do Dao*; Gu Imortais (6–8) contêm *fragmentos do próprio
    Grande Dao* — **categoria diferente, não apenas quantidade maior**; Gu de nível 9 não são
    feitos de marcas do Dao **de forma alguma**."
- **Tipo:** inferência disfarçada de fato numa nota-porta (mesmo padrão de S8).
- **O problema:** é literalmente a distinção que a pasta `02` declara ser a mais importante do
  domínio — a que explica por que um Gu Imortal não afeta outro Gu Imortal, por que os Gu de
  nível 9 escapam a todo método que opere sobre marcas, e por que o rank 9 é ontologicamente
  diferente. A nota-porta do mundo diz o contrário em nove palavras, sem ressalva. E é uma
  nota `conhecimento: comum`, ou seja, é a versão que vai para o manual do jogador: eu teria
  escrito a regra errada na página 12 do livro básico.
- **Correção:** trocar a regra 4 por "Todo Gu carrega um fragmento de lei do universo — as
  *marcas do Dao*. Nos níveis mais altos essa relação muda de natureza; ver [[O que é um
  Gu]]." Duas linhas, e o problema vira um gancho.

## SÉRIOS (04)

### S19. A origem das "marcas de sucesso" está em `04` e o uso está em `02`, sem link e com nomes diferentes

- **Arquivos:** `04 - Mundo/Lendas de Ren Zu.md` × `02 - Gu/Refino de Gu.md`
- **Trechos:**
  - `Lendas`, episódio "O sucesso no topo da montanha de fracassos": "existe um Gu que devora
    fracassos e absorve permanentemente o poder deles. As **'marcas de sucesso'** que circulam
    na economia do mundo vêm dessa lógica."
  - `Refino de Gu`: "as **marcas do sucesso**: marcas gravadas no corpo que, consumidas num
    refino, **eliminam a probabilidade natural de falha aleatória** ... intransferíveis e
    incomercializáveis."
- **Tipo:** confusão estrutural (definição órfã do uso) + inconsistência de nome.
- **O problema:** eu registrei em S12 que "marcas do sucesso" aparecia sem origem. A origem
  existe — está numa nota de mitologia, três pastas adiante, sob o nome ligeiramente diferente
  "marcas **de** sucesso". Nenhuma das duas notas aponta para a outra, então o leitor que
  precisa do conceito (o refinador) nunca chega à explicação, e o leitor que encontra a
  explicação (lendo mitos) não sabe que ela importa. É o exemplo mais nítido de um problema
  geral desta base: **a informação existe, mas não está onde a decisão é tomada.**
- **Correção:** unificar o nome, e cruzar os links nos dois sentidos. Idealmente, mover a
  regra operacional (o que a marca faz, quantas cobrem cada nível, por que é intransferível)
  para `Refino de Gu.md` e deixar em `Lendas` só a origem mítica com um link.

### S20. Existem duas explicações concorrentes para as paredes regionais, e as notas não escolhem

- **Arquivos:** `04 - Mundo/As Cinco Regiões.md` × `04 - Mundo/Cosmologia.md` ×
  `04 - Mundo/Visão Geral do Mundo.md`
- **Trechos:** `Cinco Regiões` explica a parede como **diferença de energia entre veias de
  terra vizinhas** ("onde duas regiões vizinhas se encontram, a diferença constante entre
  essas duas energias forma uma faixa de turbulência permanente"); `Cosmologia` a explica como
  **maré de qi congelada** ("as paredes regionais eram marés de qi permanentes e estáticas");
  e `Visão Geral do Mundo` a chama de "barreira regional invisível" sem causa.
- **Tipo:** confusão estrutural — três formulações do mesmo fato, em três níveis de
  conhecimento diferentes (`comum`, `segredo`, `comum`).
- **O problema:** as duas primeiras são compatíveis (são a mesma coisa dita de dois ângulos),
  mas o material nunca diz isso, e uma delas está marcada como segredo de mestre enquanto a
  outra está no manual do jogador. Como designer eu preciso saber **o que o personagem
  comum acredita** sobre a parede: se a explicação das veias é conhecimento público, o segredo
  de `Cosmologia` deixa de ser segredo. Hoje as duas notas se contradizem quanto ao **nível de
  sigilo** do mesmo fato, não quanto ao fato.
- **Correção:** decidir a camada. Sugestão: "atravessar enfraquece" = comum; "a causa são as
  veias de terra" = especializado; "parede e maré são o mesmo fenômeno em dois estados" =
  segredo. Escrever essa escada de três degraus explicitamente em `As Cinco Regiões.md`,
  porque é lá que o leitor chega primeiro.

### S21. A "Grande Era" é tratada como fato consumado em três notas e como opção de design em uma

- **Arquivos:** `04 - Mundo/Visão Geral do Mundo.md`, `As Cinco Regiões.md` (seção "Depois da
  Grande Era"), `Cosmologia.md` (marés de qi, Earth Trenches, Dez Terras).
- **Trechos:** a caixa "O mundo muda de estado" oferece as três opções (antes / depois /
  durante) — excelente —, mas as outras notas descrevem o "depois" no presente do indicativo,
  misturado com o "antes", em listas contínuas: "Depois da Grande Era, as trincheiras deixam
  de ser acidentes e viram uma categoria geológica inteira"; "Cada Gu Imortal carrega a aura
  da sua região natal ... **antes da Grande Era**" (a ressalva vem no fim da frase, depois de
  eu já ter anotado a regra).
- **Tipo:** confusão estrutural / densidade.
- **O problema:** o cenário tem dois estados, e as regras dos dois estados estão intercaladas.
  Como preciso escolher **um** para o livro básico, tive que reler as três notas marcando
  quais regras caem quando as paredes somem — e pelo menos quatro das regras mais úteis
  (supressão de um rank, nacionalidade do Gu, aura regional, imunidade do nativo) caem ou
  invertem. Isso é o alicerce da estrutura de campanha que a própria nota elogia.
- **Correção:** uma marcação visual consistente — sufixo `(antes da Grande Era)` /
  `(depois)` em toda regra afetada — ou, melhor, uma tabela de duas colunas "Antes × Depois"
  em `As Cinco Regiões.md` listando as regras que mudam. É meia hora de trabalho e economiza
  a releitura que eu tive que fazer.

### S22. `Cosmologia.md` é `segredo` inteira, mas contém o que o jogador precisa saber

- **Arquivo:** `04 - Mundo/Cosmologia.md`, `conhecimento: segredo` no cabeçalho.
- **Trecho:** a própria nota se corrige no corpo, com marcações internas: os dois céus são
  "`comum` na existência, `especializado` no conteúdo"; marés de qi são "`comum` no efeito,
  `especializado` na causa"; Earth Trenches são `especializado`.
- **Tipo:** confusão estrutural / classificação.
- **O problema:** a nota está catalogada como segredo em `00 - Somente o Mestre.md` e no mapa
  da pasta ("especializado / segredo"), mas metade do conteúdo é geografia que qualquer
  personagem usa — os dois céus, a muralha de vento celestial, as marés, as trincheiras. Eu
  precisaria dessa metade no manual do jogador e não posso entregar a nota. Nenhuma outra
  nota reúne essa geografia.
- **Correção:** ou dividir em `Cosmologia` (comum/especializado: céus, muralha, marés,
  trincheiras) e `A Fronteira do Mundo` (segredo: nove céus, Rio do Tempo, o furo), ou —
  mais barato — acrescentar à nota uma tabela de corte, no padrão que `00 - Somente o
  Mestre.md` já usa para outras notas, dizendo exatamente quais seções liberar.

## MENORES (04)

- **M20 · Nomes de Veneráveis em inglês, sem tradução, em nota portuguesa.** `Cosmologia.md`
  fecha com "Ver [[Thieving Heaven Demon Venerable]] e [[Limitless Demon Venerable]]" — os
  únicos nomes próprios não traduzidos que encontrei em 45 notas. `Heaven Path.md`, tratando
  das mesmas figuras, usa "**o Venerável Demoníaco Sem Limites**" e "**o Venerável Imortal do
  Paraíso Terreno**". Padronizar para o português, com o inglês entre parênteses na primeira
  ocorrência, como o resto do material faz.
- **M21 · `Lendas de Ren Zu.md` · densidade de nomes próprios.** A seção "A origem das
  espécies" despeja homens-de-pedra, homens-de-tinta, homens-peludos e homens-pena em quatro
  marcadores seguidos, sem dizer se são povos jogáveis, criaturas de encontro ou cor de
  fundo. É o único trecho da nota que li duas vezes sem tirar nada acionável. Uma coluna
  "papel no jogo" ou uma frase de enquadramento resolveria.
- **M22 · `As Cinco Regiões.md` · ranking incompleto declarado como ranking.** "Ranking de
  abertura a estrangeiros (do mais fechado ao mais aberto): Fronteira Sul → Continente
  Central → Mar Oriental. As outras duas ficam no meio, sem ordenação declarada." Um ranking
  de cinco itens com dois ausentes é mais confuso que útil; melhor apresentar como três
  extremos nomeados ("a mais fechada, a mais aberta, e o Centro que é seletivo").
- **M23 · `Visão Geral do Mundo.md` · a marcação 🔒 é local e não documentada.** A lista de
  regras marca com 🔒 as que são segredo — recurso ótimo, e o `00 - LEIA-ME` não o menciona
  (menciona 🔒 apenas para o Glossário). Vale generalizar para as outras notas-porta, que hoje
  separam o segredo por seção em vez de por item.
- **M24 · `Cosmologia.md` · uma escala sem referência.** "quando um mundo privado acumula uma
  quantidade colossal de marcas de dao — na ordem de **um milhão de um único caminho**" —
  ver a observação abaixo sobre as correções recentes.

## Interação com as correções já aplicadas (B1–B4)

Conferi as notas de `04` contra as três correções que vocês fizeram. Duas observações:

- **A regra linear nova (`multiplicador ≈ 1 + marcas ÷ 1.000`) valida as faixas novas, e vale
  registrar isso.** Com as faixas corrigidas, o topo de cada rank dá: rank 6 → ×10, rank 7 →
  ×31, rank 8 → ×301. Isso reproduz, sozinho, o salto de aproximadamente **dez vezes por
  rank** que `Essência Primeva.md` atribui à qualidade da essência, e dá base aritmética à
  frase de `Tribulações` de que "um rank 8 suprime um rank 7 com tamanha facilidade". As duas
  escadas do sistema agora batem. Sugiro escrever essa conferência numa caixa em
  `Dao Marks.md` — é um argumento de coerência forte e barato.
- **Um número de `04` ficou destoante depois da correção.** `Cosmologia.md` põe a formação
  espontânea de Earth Trenches num mundo privado em "**um milhão** de marcas de dao de um
  único caminho". Com as faixas novas (rank 9 = 300.000 ou mais), isso é mais de **três vezes
  o limiar de Venerável** — ou seja, pela aritmética corrigida, só um Venerável, ou alguém que
  anexou muitas aberturas, produziria uma trincheira dentro do próprio mundo. Isso é
  compatível com `Tribulações` ("existe registro de um imortal com mais de um milhão de dao
  marks — porque pulou todas as provações"), mas a nota apresenta o fenômeno como um processo
  geológico natural, o que sugere algo corriqueiro. Vale uma linha em `Cosmologia.md`
  dizendo que é fenômeno de escala de Venerável/anexador, para o leitor não calibrar errado.

---

## Segunda metade da pasta `04` (Vontade dos Céus · Fate Gu · Tribunal Celestial · Blessed Lands)

### B15. A abertura imortal é fixa na ascensão numa nota e evolutiva na outra

- **Arquivos:** `01 - Cultivo/Ascensão Imortal.md` × `04 - Mundo/Blessed Lands e
  Grotto-Heavens.md` — as duas tabelas de "grades", que descrevem o **mesmo** objeto.
- **Trechos:**
  - `Ascensão Imortal`: "O tamanho e a riqueza do mundo pequeno resultante são determinados
    **na formação** ... É o **boletim final** da vida mortal do personagem, e ele é
    **permanente**." Fluxo de tempo listado como propriedade da grade (média ~1:16, alta ~1:30
    a 1:33, super ~1:38 a 1:40).
  - `Blessed Lands`: "terras **jovens começam perto de 1:1 e sobem por degraus** — 1:6, 1:12,
    1:16; uma terra de grade alta comum roda em torno de 1:30" — e, adiante, "um especialista
    de rank 8 do caminho do tempo consegue **desacelerar o tempo na dimensão de terceiros**, o
    que significa que os fluxos variados pelo mundo são, ao menos em parte, **técnica
    instalada e não propriedade natural**".
- **Tipo:** furo lógico entre notas, sobre a estatística central do personagem imortal.
- **O problema:** ou o fluxo temporal é atribuído na ascensão e permanente (modelo "boletim
  final"), ou ele cresce com a terra e pode ser instalado por terceiros (modelo "infraestrutura
  desenvolvível"). São duas fichas de personagem diferentes: no primeiro caso a ascensão é uma
  rolagem definitiva que eu preciso deixar dramática; no segundo é o começo de um jogo de
  construção de base. As duas notas dizem também coisas diferentes sobre o **teto** da grade
  Super (`acima de 6.700 km²` × `6.700–13.000 km²`) e sobre o bônus da grade Média (`—` ×
  `recursos abundantes`).
- **Correção:** eleger `Blessed Lands` como fonte da tabela (é mais completa e mais recente
  em detalhe), fazer `Ascensão Imortal` remeter a ela em vez de duplicá-la, e substituir
  "determinados na formação e permanente" por algo como "o **potencial** é determinado na
  formação; a realização desse potencial é o trabalho de séculos". Isso concilia os dois
  textos e, de quebra, é a versão mais jogável.

### B16. Duas afirmações incompatíveis sobre a moeda do mundo imortal

- **Arquivos:** `04 - Mundo/Blessed Lands e Grotto-Heavens.md` × `04 - Mundo/Tribunal
  Celestial.md` × `04 - Mundo/Vontade dos Céus.md`
- **Trechos:**
  - `Blessed Lands`: "O que uma terra gera é *essência imortal* ... Essência é **pessoal e não
    fungível**: um imortal **não consegue usar a essência de outro**."
  - `Tribunal Celestial`: "**Produzir a moeda do mundo.** A Corte é a fonte única das **pedras
    de essência imortal** e restringe deliberadamente a distribuição como arma política."
- **Tipo:** furo lógico — atinge a economia inteira do reino imortal.
- **O problema:** se a essência imortal não é utilizável por terceiros, ela não pode ser
  moeda; e se as pedras de essência imortal circulam como moeda universal, então a essência
  **é** fungível em alguma forma. Falta exatamente uma frase — provavelmente "a essência
  ligada a um dono é intransferível; a essência **não reclamada**, cristalizada em pedra, é
  neutra e circula" —, e sem ela eu não consigo escrever preço de nada acima do rank 5. É o
  equivalente, no reino imortal, do que as pedras primevas resolvem no mortal.
- **Correção:** acrescentar essa distinção nos dois lugares e ligar as notas. Vale notar que
  o material mortal já resolveu o mesmo problema com elegância (`Essência Primeva.md`
  distingue essência pessoal de pedra primeva); o reino imortal só precisa herdar a solução.

### S23. O ingresso na Corte Celestial isenta de tribulações — e ninguém tira a conclusão

- **Arquivos:** `04 - Mundo/Tribunal Celestial.md` × `01 - Cultivo/Tribulações e
  Calamidades.md` × `01 - Cultivo/Dao Marks.md`
- **Trechos:** "**Isenção de desastres e tribulações** — o mundo coletivo não sofre as
  provações periódicas que perseguem todo cultivador imortal" e "**O direito de dormir** ...
  A maioria faz exatamente isso" × "sobreviver a desastres é **a via principal** de ganhar dao
  marks" e "3 miríades → rank 9".
- **Tipo:** falta de utilidade para design — a consequência mais importante não é enunciada.
- **O problema:** juntando as três notas, membros da Corte **trocaram progressão por
  segurança**: sem tribulações não há dao marks, sem dao marks não há avanço de rank, e
  dormindo não se acumula nada. A instituição mais poderosa do mundo é, por construção,
  **estagnada** — e isso explicaria de graça por que ela é conservadora, por que persegue
  reparos em vez de crescimento, e por que só três Veneráveis saíram de dentro dela em três
  milhões de anos. Nenhuma das três notas diz isso, e é o insight de campanha mais forte que
  o material contém sobre a Corte. (Se a leitura estiver errada — se houver outra via de
  progressão lá dentro — então a contradição é real e precisa ser resolvida.)
- **Correção:** um bloco `> [!note] Para o design` em `Tribunal Celestial.md` fechando o
  raciocínio, num sentido ou no outro. Do jeito que está, cada leitor vai chegar sozinho a
  essa conclusão e não vai saber se ela é canônica.

### S24. Um quarto número para "quantos Gu um Mestre sustenta"

- **Arquivo:** `04 - Mundo/Blessed Lands e Grotto-Heavens.md`, sete níveis de desenvolvimento,
  nível 1: "(Para comparação: um mortal comum sustenta **cinco ou seis** Gu.)"
- **Tipo:** furo numérico — reincidência do S9.
- **O problema:** agora são quatro valores para a mesma grandeza: **4 a 5** (`Visão Geral dos
  Gu`, `O que é um Gu`), **2 a 3 / 4 a 5 / até 7** por perfil (`Usar e Alimentar Gu`) e **5 ou
  6** aqui. Registro porque mostra que o S9 não é um deslize isolado: é um número que foi
  reescrito de memória em cada nota que precisou dele.
- **Correção:** a mesma de S9 — uma fonte única, e as outras notas citando-a. Sugiro que a
  tabela por perfil de `Usar e Alimentar Gu.md` seja declarada canônica no próprio texto
  ("esta é a tabela de referência; outras notas remetem a ela").

### S25. `Fate Gu.md` e `Tribunal Celestial.md` repetem seções inteiras uma da outra

- **Arquivos:** `04 - Mundo/Fate Gu.md` × `04 - Mundo/Tribunal Celestial.md`
- **Trechos duplicados quase palavra por palavra:** os quatro limites da vigilância (não vê
  fracos, não vê quem está em mundo privado, não vence ocultação da sabedoria, jurisdição
  regional) e o custo que "dobra sob interferência hostil"; o ciclo de reparo do Fate Gu; a
  competição centenária de refino como colheita disfarçada; a caça aos foragidos como
  manutenção.
- **Tipo:** densidade / redundância.
- **O problema:** não é erro — as duas versões concordam, o que é um bom sinal. Mas eu li a
  mesma tabela duas vezes em notas consecutivas e, na segunda, gastei tempo procurando a
  diferença que não existia. Em material de referência, repetição idêntica é ruído; e cria
  dois lugares para manter sincronizados a cada correção futura.
- **Correção:** manter a tabela de limites da Torre em **uma** nota (proponho `Tribunal
  Celestial.md`, que é a dona do artefato) e na outra deixar duas linhas mais o link.

### Sobre o B5 (unidade de energia imortal): metade resolvida, na pasta errada

Registro a atualização porque muda o diagnóstico: `Blessed Lands e Grotto-Heavens.md`
**explica** as denominações que eu não tinha encontrado — "uva verde (rank 6), tâmara vermelha
(7), lichia branca (8), damasco amarelo (9)" — e ainda dá um exemplo de orçamento doméstico
("terras que dividiam a reserva em dezesseis partes — oito para refino, quatro para
manutenção, três para operações, uma para emergência"), que é justamente o tipo de âncora que
eu pedi. Então:

- **O que se resolve:** a escada de denominações existe e está documentada. Falta apenas
  ligá-la a partir de `01 - Cultivo/Ascensão Imortal.md` e `Tornar-se Venerável.md`, que a
  usam sem explicar.
- **O que permanece em aberto:** a unidade "**conta**" continua indefinida nas duas tabelas de
  grade ("10+ contas", "50+ contas"). Uma conta é uma unidade de quê — uma pedra? uma
  ativação? um ano de ração de um Gu de rank 6? Sem isso a coluna "produção anual de energia"
  é decorativa, e é a única coluna que eu usaria para balancear a economia imortal.
- **E fica o padrão:** este é o terceiro caso (com S19 e com o B5 original) em que **a
  informação existe, mas não na nota onde a decisão é tomada**. Sugiro que isso vire uma
  passada de revisão própria: para cada termo destacado com `==...==` numa nota, garantir que
  a nota que *usa* o termo tenha o link.

## MENORES (04, segunda metade)

- **M25 · Nomes de Veneráveis em inglês — o problema é sistêmico, não pontual.** Além de
  `Cosmologia.md` (M20), aparecem `[[Red Lotus Demon Venerable]]` e `[[Star Constellation
  Immortal Venerable]]` em `Fate Gu.md`, e `[[Primordial Origin Immortal Venerable]]`,
  `[[Star Constellation Immortal Venerable]]` e `[[Genesis Lotus Immortal Venerable]]` em
  `Tribunal Celestial.md` — enquanto `Wisdom Path.md` chama a mesma pessoa de "**a Venerável
  Imortal Constelação Estelar**". Um leitor que leia as duas notas não sabe que é a mesma
  figura. Padronizar é obrigatório, não cosmético.
- **M26 · `Blessed Lands` é longa demais para o que promete no título.** Com nove seções
  grandes, ela cobre quatro assuntos separáveis: o que é uma dimensão privada, como se
  conquista uma, como uma decai (a "masmorra com relógio"), e como se desenvolve uma (os sete
  níveis). O terceiro e o quarto são sistemas de jogo inteiros e distintos — herança/dungeon
  de um lado, construção de base do outro. Vale considerar desmembrar em duas notas.
- **M27 · `Vontade dos Céus.md` · uma defesa listada não é defesa.** O item "2. Elevar o
  próprio cultivo — a defesa real de longo prazo" é, na prática, "não há defesa"; listá-lo
  entre as sete opções dilui a lista, que fora isso é excelente e diretamente jogável.
- **M28 · `Tribunal Celestial.md` · uma pista deixada solta.** "O texto marca explicitamente
  que existe uma **desvantagem oculta** nessa troca e nunca a revela." Ótimo gancho, mas
  merece um `> [!note] Para o design` dizendo que é um espaço em branco deliberado que a
  mestra pode preencher — hoje parece uma lacuna de pesquisa, não um convite.

## O QUE NÃO PRECISA MEXER (04)

- **E16 · `Vontade dos Céus.md` é a melhor nota do material depois de `Gu Imortais.md`.** A
  tabela lei × vontade resolve, em seis linhas, o "erro conceitual mais comum sobre este
  mundo"; as **duas janelas de ação direta** convertem um antagonista onipotente em antagonista
  com regras de engajamento auditáveis; e as sete defesas são todas jogáveis. É o que eu
  entregaria a um mestre como leitura obrigatória.
- **E17 · Os limites publicados da Torre que Observa o Céu.** "Um olho que tudo vê com quatro
  cegueiras publicadas vale infinitamente mais numa mesa do que um olho que tudo vê" — e a
  tabela cumpre isso, com uma coluna inteira dedicada à consequência de mesa. É o formato que
  eu gostaria de ver em todas as tabelas da base.
- **E18 · A condição de posse de uma terra abençoada ser a obsessão não realizada do morto.**
  É a melhor ideia de design de aventura do material inteiro, e a nota tem a disciplina de
  listar exemplos variados (o casal que se ama de verdade, a técnica inacabada) em vez de
  descrever a regra em abstrato.
- **E19 · `Lendas de Ren Zu.md` — o mito como manual de regras.** A tese ("se precisar decidir
  se algo é possível neste mundo, a pergunta não é 'isso faz sentido fisicamente?' e sim
  'existe uma lenda que abre precedente?'") é uma ferramenta editorial que eu vou usar durante
  todo o projeto, e a permissão explícita de inventar episódios novos resolve o problema de
  extensibilidade do cenário.
- **E20 · A anexação de aberturas é descrita de forma idêntica em `01` e `04`** — mesmos três
  requisitos, mesmos três benefícios, mesmo trade-off. Depois de tantas divergências entre
  pastas, vale registrar que este subsistema está perfeitamente sincronizado.
- **E21 · O tratamento da Corte Celestial como burocracia, e não como império do mal**, com
  protocolos desatualizados, facções herdadas e conta de consumo por consulta. É maduro e é
  exatamente o que faz uma instituição funcionar numa mesa.

---

# Veredito

**Sim, eu conseguiria projetar o jogo com este material — e não conseguiria escrever as
regras.** A distinção é a coisa mais importante deste relatório, então deixo ela explícita.

## O que este material já me dá, e é muito

Li 45 notas sem nunca ter ouvido falar da obra e, ao fim, **entendi o mundo**. Sei o que é
uma abertura, por que a aptidão é um teto e não uma velocidade, por que a magia deste mundo
é uma economia de criação de animais, por que o poder atrai punição automática, por que
roubar um artefato de topo o destrói e por que isso torna a diplomacia inevitável entre
inimigos mortais. Sei qual é a fantasia central de doze arquétipos diferentes. Isso é raro:
a maior parte dos materiais de cenário me faria decorar nomes próprios.

Mais que isso, o material **pensa como designer**, e não só como enciclopédia. Os blocos
"Para o design" não são resumos: são propostas mecânicas, várias delas melhores do que eu
teria bolado sozinha — manutenção de Gu como pressão de campanha, backlash escalonado por
progresso de conjuração, a condição de posse de uma terra sendo a obsessão não resolvida de
um morto, os limites publicados de uma máquina de vigilância, "os personagens mais fortes
não cabem nos lugares menores" como solução para o problema do chefão onipotente. Se eu
tivesse que apontar o maior valor desta base, não seria a informação: seria **o julgamento
editorial sobre o que é jogável**.

E há um ativo que nem os autores tinham percebido: a aritmética da progressão imortal
fecha. Cadência de provações × valor por provação reproduz exatamente as faixas de dao marks
por rank e a condição formal do rank 9. Com a correção que vocês já aplicaram, ela agora
reproduz também o salto de ~10× por rank da essência. **Isso é uma tabela de experiência
pronta, auditável, derivada e não arbitrada.** Poucos cenários publicados têm isso.

## O que me impede de escrever regras hoje

O padrão de falha é único e se repete em todas as pastas: **o mesmo número foi reescrito de
memória em cada nota que precisou dele**, e as versões divergiram. Quantos Gu um Mestre
sustenta tem quatro respostas. A escala de attainment tem duas. O teto da herança tem dois.
Dao Lord tem duas definições. As grades de abertura imortal têm duas tabelas. As taxas de
sucesso de refino se invertem entre notas. E "refino" nomeia duas operações diferentes na
mesma página.

Nenhum desses é um erro de pesquisa — a pesquisa é boa, e a rastreabilidade por `fontes`
está lá. São erros de **arquitetura editorial**: não existe fonte única para nenhuma
grandeza. Enquanto isso não for resolvido, qualquer regra que eu escrever vai contradizer
alguma nota, e eu não vou saber qual das duas é a certa.

As quatro coisas que eu literalmente **não posso** escrever hoje, por falta de decisão e não
de informação:

1. **A economia de ações do combate.** Se controlar dois Gu já é destaque, ninguém dispara um
   golpe de quarenta e dois. É a primeira regra de qualquer RPG e o material me dá quatro
   números incompatíveis (B9).
2. **O subsistema de fabricação.** Três verbos, duas descrições, taxas que se invertem (B7,
   B8). Não sei se estou desenhando domesticação, artesanato ou os dois.
3. **A economia imortal.** Não sei o que é uma "conta", e não sei se a essência imortal é
   fungível — mas ela é a moeda do mundo (B5, B16).
4. **A criação de personagem.** A Cerimônia do Despertar é a primeira cena de qualquer
   campanha e é a coisa menos documentada da base — sem nota própria, sem procedimento, sem
   o que acontece com quem falha (S6). E não tenho pirâmide demográfica para saber se os
   personagens dos jogadores são especiais ou são a tropa comum (S7), que é a primeira
   decisão de tom de um jogo.

## O que falta, além das correções

Três lacunas que não são erros — são material que simplesmente não existe:

- **Uma folha de números canônicos.** Um arquivo único, declarado soberano, com toda grandeza
  do sistema e uma linha por número; todas as notas passando a citá-lo em vez de repeti-lo.
  `Tabelas de Referência Rápida` talvez já queira ser isso, mas está no fim da fila de leitura
  e nenhuma nota a trata como autoridade. **Se eu pudesse pedir uma só coisa, seria esta:**
  resolve, de uma vez, a maioria dos 16 bloqueadores e dos 25 sérios deste relatório.
- **A camada de "como é uma sessão".** O material me diz como o mundo funciona e nunca me diz
  o que acontece numa terça-feira na vida de um grupo de personagens: quanto tempo passa entre
  cenas, em que escala o conflito acontece, o que um grupo de rank 2 faz durante seis meses.
  Suspeito que `06 - Economia e Vida` cubra parte disso (o LEIA-ME põe `Como um Mestre Gu
  Ganha a Vida` entre as cinco notas fundacionais, e faz sentido), mas estava fora do meu
  escopo — vale confirmar que a resposta está lá, porque no escopo que revisei ela não está.
- **A escolha do estado do mundo.** O cenário tem duas versões (antes e depois da Grande Era)
  e as regras das duas estão intercaladas nas mesmas listas (S21). Alguém precisa decidir qual
  é o padrão do livro básico — e essa é uma decisão editorial, não de pesquisa.

## Ordem de trabalho que eu recomendaria

1. A folha de números canônicos e a passada de sincronização (resolve B1–B2 já feitos, B3–B4
   já feitos, B8, B10, B11, B15, S3, S9, S17, S24).
2. Desambiguar "refino" e a economia de ações (B7, B9) — são os dois que travam subsistemas
   inteiros.
3. Limpar o lixo de geração das doze notas (B13) — é meia hora e é o que mais dana a
   confiança de um leitor externo.
4. Escrever a Cerimônia do Despertar e a pirâmide demográfica (S6, S7).
5. Resolver as duas definições de Dao Lord e o tempo interno × externo (B12, B6).
6. O resto, por ordem de severidade.

## Em uma frase

Este é o melhor material de cenário que eu já recebi como fonte única para um projeto de
adaptação, e ele está a **uma passada de consistência numérica** de ser utilizável para
escrever regras — não a uma rodada de pesquisa. O trabalho difícil já foi feito; o que falta
é o trabalho chato.

---

**Contagem final:** 16 bloqueadores · 25 sérios · 28 menores · 21 notas ou seções que não
precisam de mexida. Escopo: 3 notas de `00`, 11 de `01`, 8 de `02`, 5 de `03` (amostra de 18)
e 8 de `04`.
