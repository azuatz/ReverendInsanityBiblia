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
