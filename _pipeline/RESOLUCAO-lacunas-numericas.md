# Resolução de lacunas numéricas e de cultivo — passe de verificação no texto-fonte

> Fonte: `/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/*.txt` (obra completa, 6 volumes).
> Método: busca por regex sobre o texto integral, com resolução do capítulo por indexação
> dos marcadores `## Chapter N`. Veredito por item: ✅ RESOLVIDO / ⚠️ PARCIAL / ❌ A OBRA NÃO DIZ.

**STATUS: em elaboração (gravação incremental).**

---

## 1. Descontinuidade de dao marks entre rank 7 e rank 8 (30.000 → 100.000)

**✅ RESOLVIDO — e de forma muito mais forte do que se esperava.** A obra dá a
aritmética completa, e as faixas registradas são o resultado exato dela.

### 1.1 A tabela de rendimento por calamidade (cap. 1703)

> "Normally speaking, an earthly calamity gave a Gu Immortal **two hundred and fifty**
> dao marks, heavenly tribulation was **seven hundred and fifty**, grand tribulation was
> **seven thousand two hundred and fifty**, while myriad tribulations were even higher, at
> **eighty-six thousand seven hundred and fifty**." (cap. 1703)

Confirmação independente no cap. 2071: "an ordinary grand tribulation gave about seven
thousand dao marks, while an ordinary myriad tribulation gave about eighty thousand."
E no cap. 1470: "Heavenly tribulations on average gave about seven hundred and fifty dao marks."

### 1.2 A cadência de calamidades por rank

Uma única cadência de **1 evento a cada 10 anos**, em que os eventos de tier superior
**substituem** (não se somam a) o earthly calamity daquele decênio:

| Rank | a cada 10 anos | a cada 50 anos | a cada 100 anos | Fonte |
|---|---|---|---|---|
| 6 | earthly calamity | — | heavenly tribulation | cap. 826, 1097 |
| 7 | earthly calamity | heavenly tribulation | grand tribulation | cap. 1703 |
| 8 | heavenly tribulation | grand tribulation | myriad tribulation | caps. 1007, 1703 |

Cada rank dura **300 anos** = 30 slots (caps. 826, 973, 1007).

### 1.3 A conta fecha exatamente com as faixas registradas

- **Rank 6**: 27 earthly × 250 + 3 heavenly × 750 = 6.750 + 2.250 = **9.000** ✅ (teto da faixa r6)
- **Rank 7**: 24 earthly × 250 + 3 heavenly × 750 + 3 grand × 7.250 = 6.000 + 2.250 + 21.750 = **30.000** ✅ (teto da faixa r7)
- **Rank 8**: 24 heavenly × 750 + 3 grand × 7.250 + 3 myriad × 86.750 = 18.000 + 21.750 + 260.250 = **300.000** ✅ (teto da faixa r8)

Ou seja: **os tetos 9.000 / 30.000 / 300.000 do cap. 2071 não são estimativas soltas — são
a soma aritmética exata de um ciclo completo de 300 anos naquele rank.** Isso é uma
descoberta nova e deve entrar no material.

O cap. 1817 confirma o resultado do r8 por outro caminho: "Theoretically, after three
myriad tribulations, a Gu Immortal can become venerable, they would have **at least three
hundred thousand dao marks**!"

### 1.4 Por que o salto de 30k para 100k

**O myriad tribulation é a descontinuidade.** Ele só existe a partir do rank 8 e, sozinho,
vale ~86.750 dao marks — mais de dez vezes um grand tribulation:

> "One myriad tribulation gave eighty thousand dao marks, it was **more than ten times of a
> grand tribulation**, this was also the reason why **rank eight Gu Immortals often suppressed
> rank seven, the difference in their dao marks was just too high**." (cap. 1703)

A faixa 30k–100k **existe e é povoada** — é o primeiro século de rank 8, antes do primeiro
myriad tribulation. Um imortal recém-promovido a rank 8 carrega ~30.000 e acumula, nos
primeiros 100 anos, 10 heavenly (7.500) + 2 grand (14.500) ≈ 52.000. Ao passar o primeiro
myriad tribulation, salta de ~52.000 para ~139.000 **num único evento**. O piso de 100.000
da faixa r8 descreve, portanto, o rank 8 que já passou pelo menos um myriad tribulation:

> "**A hundred and twenty thousand dao marks was not common for rank eight Gu Immortals,
> they normally would have to pass one myriad tribulation to get such an accumulation.**" (cap. 1629)

**Conclusão**: não há lacuna. A faixa 30k–100k é a janela transitória do rank 8 pré-primeiro-myriad,
e a descontinuidade é causada por um evento discreto de ~87.000 dao marks que não existe em ranks inferiores.

---

## 2. Teto / curva da fórmula de amplificação por dao marks

**✅ RESOLVIDO. A escala é rigorosamente linear e NÃO satura — mas há um teto qualitativo.**

### 2.1 A fórmula é linear até pelo menos 1.000.000 de dao marks

| Dao marks | Amplificação declarada | Capítulo |
|---|---|---|
| 100 | "+10 percent" | 1161 |
| 1.000 | "double its effect" / "a hundred percent amplification" | 1161, 1204, 1310, 1470, 2071 |
| 10.000 | "ten times the power" | 1204, 1310 |
| 16.000 | "sixteen times the amplification" | 1161 |
| 50.000 | "fifty times the amplification" | 1310 |
| **120.000** | "**amplify any time path killer move by a hundred and twenty times its power**" | **1629** |
| **1.000.000** | "**its power had risen by a thousand times**" | **1817** |

A fórmula fechada é **amplificação = 1 + N/1000** (i.e. o efeito vira (1 + N/1000)× o original).
Isso reconcilia todos os pontos: 100 → 1,1× ("+10%"); 1.000 → 2× ("double"). Para N grande o
autor simplesmente omite o "+1" da base (10.000 → 11× é dito "ten times"; 50.000 → 51× é dito
"fifty times"). **Nenhum ponto da obra desvia dessa reta**, do rank 6 (centenas) ao rank 9
(milhão). **Não existe saturação numérica.**

### 2.2 O teto real é qualitativo, não numérico (cap. 1817)

Fang Yuan, com **um milhão** de qi path dao marks, usa um killer move de rank 7 e obtém poder
de rank 8 "sem dúvida", ao custo de essência imortal de rank 7. Ele então testa a hipótese de
escalar para rank 9 e conclui que não:

> "**Most likely, rank nine killer moves need rank nine Immortal Gu. Dao mark amplification
> cannot reach this extent.**"
> "Or more accurately, I cannot breakthrough to that level using just a million qi path dao marks."
> "**Maybe if I have ten times the dao marks, the quantity will induce a qualitative change**,
> and reach rank nine perhaps?" — Fang Yuan was not certain. (cap. 1817)

**Leitura canônica**: a amplificação por dao marks escala linearmente sem limite conhecido,
mas **não promove o rank do killer move indefinidamente** — a partir de certo ponto, o rank do
Immortal Gu núcleo passa a ser o gargalo. A obra deixa explicitamente em aberto (pela boca de
Fang Yuan, que "was not certain") se uma quantidade dez vezes maior induziria mudança
qualitativa. Registrar como incerteza declarada pelo próprio texto, não como lacuna nossa.

### 2.3 Corolário sobre a menção "centenas a milhares de vezes" no rank 8

Não é uma quebra de linearidade: é simplesmente a leitura da mesma reta na faixa de dao marks
de um rank 8 (100.000–300.000 → 100×–300×) e de um rank 9 (300.000+ → 300×+, e o milhão de
Fang Yuan → 1000×). **A escala continua linear; só a base de dao marks é que cresceu.**

---

## 3. Item 52 — rank 7 = 24 earthly calamities (por que 24 e não 30)

**✅ RESOLVIDO. Não há reinício de contador: as tribulações de tier superior SUBSTITUEM o
earthly calamity do decênio correspondente.**

A prova está no rank 6, onde a obra faz a conta explicitamente:

> "A rank six Gu Immortal faces an earthly calamity every ten years, and a heavenly tribulation
> every one hundred years. After three hundred years, after three heavenly tribulations, they
> would become rank seven. **That means, they would have twenty-seven earthly calamities and
> three heavenly tribulations.**" (cap. 1097)

30 slots decenais − 3 ocupados por heavenly tribulations = **27** earthly calamities. A soma é
sempre 30 eventos.

Aplicando ao rank 7 (earthly/10 anos, heavenly/50 anos, grand/100 anos — cap. 1703):
- grand tribulations nos anos 100, 200, 300 → **3**
- heavenly tribulations nos anos 50, 150, 250 (os múltiplos de 50 que não são de 100) → **3**
- earthly calamities nos 24 decênios restantes → **24**
- Total: 24 + 3 + 3 = **30** ✅

Que é exatamente o que o cap. 1470 declara: "Rank seven Gu Immortals had to go through
**twenty-four earthly calamities, three heavenly tribulations, and three grand tribulations**."

**Nota sobre a aparente contradição do cap. 826**: ali se lê "facing a total of thirty earthly
calamities and three heavenly tribulations" para o rank 6 — o que somaria 33. É fraseado
impreciso (o "thirty" é o número de slots decenais, não de earthly calamities). O cap. 1097,
que faz a conta de forma explícita e detalhada, é a leitura correta e deve prevalecer. **Não é
contradição de mecânica, é imprecisão de redação num único parágrafo.**

Por simetria, o rank 8 (heavenly/10a, grand/50a, myriad/100a) tem **24 heavenly + 3 grand +
3 myriad**. A obra nunca escreve esses 24 por extenso, mas a estrutura é idêntica e a soma de
dao marks resultante (300.000) bate exatamente com o cap. 1817 — ver item 1.3.

### 3.1 O contador reinicia no avanço de rank? (busca dirigida)

**⚠️ PARCIAL — a obra nunca escreve "o contador reinicia", mas DEMONSTRA que a contagem é
por rank. Não há passagem declarativa; há prova por uso.**

Busca feita por formulações de reinício (`reset`, `start again/anew/over`, `count`) próximas de
`calamity`/`tribulation` em todo o corpus: **nenhuma declaração explícita existe.**

O que existe é a contagem regressiva em cena, que só fecha se o orçamento for **por rank**:

> "That means, they would have twenty-seven earthly calamities and three heavenly tribulations.
> And for Fang Yuan, **after this second earthly calamity, he still had twenty-five earthly
> calamities and three heavenly tribulations**." (cap. 1097)

2 já passadas + 25 restantes = **27**, o total exato do rank 6. Fang Yuan conta rumo ao rank 7,
não desde o início da vida imortal. A numeração ordinal acompanha ("first earthly calamity",
caps. 1043, 1056, 1066, 1068; "fifth earthly calamity", cap. 1148) e é sempre interna ao rank.

Ao chegar ao rank 7, o cap. 1470 apresenta um orçamento **novo e de composição diferente**
(24 + 3 + 3), não um resto do anterior. Logo:

**Modelo canônico**: cada rank tem um orçamento fechado de **30 eventos em 300 anos**, cuja
composição muda com o rank; ao avançar, começa um novo ciclo de 30. Os **dao marks acumulados
NÃO reiniciam** (são cumulativos por toda a vida — é o que sustenta a aritmética do item 1);
o que reinicia é o **calendário de calamidades**. Registrar essa distinção explicitamente no
material, porque é a fonte provável da confusão original.

---

## 4. Item 51 — escala de soul foundation (10 mi → 90 mi → 200 mi)

**✅ RESOLVIDO. Não é elipse narrativa nem erro do autor: é (a) uma escada decimal
explícita e (b) uma inconsistência da TRADUÇÃO inglesa num punhado de capítulos.**

### 4.1 A escada é explícita e decimal

> "From low to high, there was single man soul, ten man soul, hundred man soul… **million
> man soul, ten million man soul, hundred million man soul**…" (cap. 1460)

> "First layer was human soul, the cultivation starting from single man soul to hundred man
> soul, thousand man soul... until the highest **hundred million man soul**. Hundred million
> man soul was **the limit of human soul**, where it turned from phantom to solid and could
> interfere with the material world." (cap. 2128)

### 4.2 A progressão de Fang Yuan É narrada passo a passo — sem lacuna

| Cap. | Soul foundation | Observação |
|---|---|---|
| 1460 | 1.000.000 (million man soul) | temperado por Luo Po wind + bewilderment fog |
| 1462 | 5.000.000 | "+500.000 por sessão"; meia dose de ano para chegar a 10 mi |
| 1465, 1467 | 10.000.000 | |
| 1470 | 50.000.000 | "signs of turning solid" |
| 1471 | 70.000.000 | prova interna: "**I am thirty million man soul away from hundred million**" (70+30=100 ✅) |
| 1476 | 80.000.000 | abaixo do esperado: perdas por praticar o killer move *split soul* |
| 1481, 1494, 1495, 1502 | **queda brutal** | *split soul* + corrosão do dream realm de Thieving Heaven |
| 1495, 1505 | 90.000.000 | recuperado com guts Gu sem economia |
| 1508, 1509 | **100.000.000** | "From phantom to solid… I have finally reached hundred million man soul!" |
| 1509 | **200.000.000** | "dozens of days passed… increased to two hundred million!" |
| 2128 | 60.000.000 **desolate** soul | segunda camada, já no Volume 6 |

**Não há salto sem evento.** Cada degrau tem cena, custo (guts Gu, soul cores) e recuo narrado.

### 4.3 Os "200 milhões" NÃO são erro — a obra dá a sub-escada acima de 100 milhões

> "But… I am only at one hundred million man soul, I will need to continue to accumulate
> further, **two hundred million, three hundred million, four hundred million… until nine
> hundred million**. After nine hundred million was **not one billion, but was a breakthrough
> to desolate soul**." (cap. 1509)

E depois da ruptura, a escada recomeça: "Ten desolate soul, hundred desolate soul, thousand
desolate soul, ten thousand desolate soul, hundred thousand desolate soul, million desolate
soul, ten million desolate soul, and hundred million desolate soul!" (cap. 2128), sendo
*hundred million desolate soul* = Three Headed Thousand Arms Demon Soul de Spectral Soul,
com poder quase-rank 9 (caps. 1869, 2128, 2265).

### 4.4 ⚠️ A ressalva real: a tradução inglesa perde uma casa decimal nos caps. 1481–1503

Nesse bloco, o mesmo estado de alma é chamado ora de "ninety million", ora de "nine million"
ou "ten million". Exemplos no MESMO capítulo:

- cap. 1495: "his soul foundation once again rose to **ten million** man soul. He previously had
  **nine million** man soul…" — e, meia dose de mês depois, "Fang Yuan's soul foundation had
  increased to **ninety million** man soul, only a slight distance away from hundred million."
- cap. 1502: "When I passed the first stage, my soul foundation was over **nine million** man
  soul" — mas o cap. 1495 dizia **ninety million** para esse mesmo momento.

A causa provável é a unidade chinesa 千万 (= 10 milhões): 九千万 (90 mi) foi renderizado ora
como "ninety million", ora como "nine million". **Os valores narrativamente consistentes são os
altos** (70 → 80 → 90 → 100 → 200 milhões), porque só eles fecham com o cheque interno do
cap. 1471 ("thirty million away from hundred million" estando em setenta milhões) e com o
cap. 1505 ("My soul is at ninety million man soul currently, the soul cores harvested in this
trip will be enough to advance me to hundred million man soul level").

**Veredito**: usar a progressão alta; anotar os caps. 1481/1494/1495/1502/1503 como ruído de
tradução, não como mecânica. A lacuna registrada era artefato de ter ancorado nas cifras baixas.

---

## 5. Item 61 — a zona de aptidão 31–39%

**❌ A OBRA NÃO DIZ — e agora sabemos exatamente por quê: a tabela oficial da obra tem um
buraco literal ali.**

A obra dá a tabela de graus em duas passagens complementares e apenas essas duas:

> "A Gu Master's aptitude, **40-59% was C grade, 60-79% was B grade, and 80% and above was A
> grade**." (cap. 198)

> "the aptitude that he had was only the worst D grade. **D grade aptitude Gu Masters had only
> twenty to thirty percent primeval essence** in their apertures, most could become rank one but
> few could reach rank two." (cap. 1491)

E o número de graus é fechado: "**Cultivation aptitudes were divided into four grades; A grade,
B grade, C grade and D grade.** Everyone knew this." (cap. 135). Não existe grau E ou F.

Portanto a tabela canônica completa é:

| Grau | Faixa declarada |
|---|---|
| A | 80–99% (o máximo é 99%; 100% só nas dez constituições extremas, cap. 135) |
| B | 60–79% |
| C | 40–59% |
| D | 20–30% |
| — | **31–39%: sem grau atribuído** |
| — | **0–19%: sem grau atribuído** |

**Busca exaustiva feita**: varredura de todo o corpus por `3[1-9]%` e por todos os ordinais
"thirty-one/…/thirty-nine percent" cruzados com "aptitude". **Zero ocorrências.** Nenhum
personagem da obra tem aptidão declarada entre 31% e 39%.

A passagem que MAIS se aproxima é o cap. 305, onde Shang Xin Ci sobe "from the lowest twenty
percent D grade aptitude… slowly rose to C grade fifty-nine percent" — ela necessariamente
atravessou a faixa 31–39%, mas o texto passa por cima dela sem citar um único valor.

**Confirmado**: registrar como não-descrito. Não interpolar. É provável arredondamento
narrativo do autor (a faixa D foi fixada em "20 a 30" como número redondo, sem alinhar com o
piso 40 do grau C).

---

## 6. Item 62 — quanto o "polished gold Gu" eleva a aptidão

**❌ A OBRA NÃO DIZ. Confirmado por varredura completa: o termo aparece só 6 vezes em toda a
obra (caps. 1155, 1160 ×3, 2295) e nenhuma delas dá número.**

O máximo que se obtém é qualitativo:

> "a rare mortal Gu that could make all mortal Gu Masters go crazy — polished gold Gu, it was a
> **one time consumable Gu** that could increase a Gu Master's aptitude!" (cap. 1155)

### 6.1 Achado colateral útil: a obra dá o RANKING dos Gu de aptidão

> "**Blood skull Gu's ability to raise aptitude is even more outstanding than unprocessed jade
> Gu, wood origin Gu, water source Gu, and polished gold Gu.** Maybe I can use blood skull Gu to
> undergo a massive slaughter before reviving them using Human Sea and slaughtering them again.
> In that case, I can create a large number of A grade aptitude Gu Masters." (cap. 2295)

Isso dá um **limite superior** para o polished gold Gu: ele é estritamente inferior ao blood
skull Gu, que é o único Gu de aptidão quantificado na obra —

> "He was bathed in blood over ten times… **The first few raised his aptitude by 10%**, but the
> percentage continued to drop with each try." (cap. 198)

Ou seja: o blood skull Gu rende +10% por uso com **rendimentos decrescentes** (44% → 90% em
"mais de dez" banhos, caps. 198-199), e o polished gold Gu rende **menos que isso** por uso,
com a diferença adicional de ser consumível de uso único. **Este é o teto inferido; a obra não
declara o valor.**

---

## 7. Item 41 — taxa de conversão entre denominações de essência imortal

**✅ RESOLVIDO — a obra DÁ a taxa, de forma explícita e mais de uma vez. A lacuna estava errada.**

### 7.1 A taxa nominal é 100:1 por rank, declarada literalmente

> "**One hundred beads of green grape immortal essence could merge into a bead of red date
> immortal essence.**" (cap. 1206)

> "**One bead of white litchi immortal essence was in some sense a hundred beads of red date
> immortal essence, which was ten thousand beads of green grape immortal essence.** That was to
> say, ten thousand immortal essence stones could be converted into one white litchi immortal
> essence bead, the conversion rate was simply too bad." (cap. 1644)

> "**One immortal essence stone was equivalent to one green grape immortal essence bead, each of
> Fang Yuan's yellow apricot immortal essence beads were worth a million immortal essence
> stones!**" (cap. 2228)

### 7.2 Tabela fechada resultante

| | green grape (r6) | red date (r7) | white litchi (r8) | yellow apricot (r9) |
|---|---|---|---|---|
| em immortal essence stones | 1 | 100 | 10.000 | 1.000.000 |
| razão para o rank anterior | — | ×100 | ×100 | ×100 |

**Fator constante de 100 por rank**, verificado em três pontos independentes e por dois
caminhos distintos (fusão direta, cap. 1206; e equivalência em immortal essence stones,
caps. 1316, 1644, 2228). O cap. 1316 reconfirma o elo r6→r7: "one hundred immortal essence
stones were required to turn into one bead of red date immortal essence."

### 7.3 ⚠️ Correção importante: o "130 green grape por red date" NÃO é uma taxa de conversão

A cifra existente no material vem, quase certamente, de uma leitura equivocada desta passagem:

> "If green grape immortal essence was used to activate **rank seven Immortal Gu**, there would
> be **at least thirty percent additional expenditure**. After merging them into red date
> immortal essence, there won't be any meaningless loss in this aspect." (cap. 1206)

Esses 30% são a **penalidade por acionar um Gu acima do rank da essência**, não o custo da
fusão. A fusão em si é 100:1 limpo (mesmo capítulo, dois parágrafos antes). O "130" é um número
derivado (100 × 1,3) que a obra nunca escreve. **Corrigir no material**: a taxa é 100:1; a
sobretaxa de 30% é uma regra separada, sobre USO direto de essência sub-rank.

Busca por "hundred and thirty green grape" / "130 green grape" em todo o corpus: **zero ocorrências.**

### 7.4 Nota de valor (não de conversão)

Do ponto de vista de um rank 6, o cap. 460 usa a formulação retórica "One hundred green grape
immortal essence beads cannot compare to one white litchi immortal essence" — que é retórica de
qualidade, não taxa (a taxa real green grape→white litchi é 10.000:1, cap. 1644). Não confundir.

---

## 8. Estágio de essência imortal × rank do cultivador — é enunciado de forma fechada?

**✅ RESOLVIDO. SIM: o cap. 1007 enuncia a correspondência de forma fechada e sistemática, num
único bloco contínuo, junto com a cadência de calamidades.**

> "Among which, **rank six Gu Immortals had green grape immortal essence**. They faced an earthly
> calamity every ten years, and a heavenly tribulation every one hundred years. After three
> hundred years, after three heavenly tribulations, they would become rank seven.
>
> **Rank seven Gu Immortals had red date immortal essence.** They faced an earthly calamity every
> ten years, a heavenly tribulation every fifty years, and a grand tribulation every one hundred
> years. After three hundred years, they would become rank eight.
>
> As for **rank eight Gu Immortals, their immortal apertures would create white litchi immortal
> essence**. They faced a heavenly tribulation every ten years, a grand tribulation every fifty
> years, and a myriad tribulation every one hundred years. After three myriad tribulations, they
> would become the invincible rank nine Gu Immortals!" (cap. 1007)

O rank 9 fica de fora desse bloco porque o capítulo trata do caminho até lá, mas é enunciado com
igual clareza noutro lugar:

> "Giant Sun Immortal Venerable was rank nine, the immortal essence he had left behind was the
> **yellow apricot immortal essence that only rank nine venerables could form**." (cap. 971)

Reforços: "rank nine yellow apricot immortal essence" (caps. 607, 634); "This was something only
rank six Gu Immortals had — green grape immortal essence!" (cap. 409); "Hei Cheng's **rank seven**
blessed land… produced red date immortal essence that was one rank higher than green grape
immortal essence" (cap. 681).

**Portanto: a relação NÃO é apenas implícita.** O cap. 1007 é a passagem-âncora e deve ser citado
como tal no material. Bônus: ele é a mesma passagem-âncora da cadência de calamidades do item 1 —
a obra trata "denominação de essência" e "tier de calamidade" como duas faces do mesmo degrau de rank.

**Nuance a registrar**: a produção da denominação segue o rank do **immortal aperture / blessed
land**, não apenas o do cultivador — daí Fang Yuan produzir white litchi "in advance" por ter o
sovereign immortal aperture (caps. 681, 1644), e daí um blessed land de rank 7 produzir red date.

---

## 9. As cinco contradições menores (itens 2, 3, 10, 11, 14 de LACUNAS.md)

Resumo dos vereditos antes do detalhe:

| # | Contradição | Veredito |
|---|---|---|
| 2 | Prêmio do exame: 150 vs 100 pedras | ⚠️ **Erro do autor/tradução.** Sem reconciliação no texto. Adotar **100** |
| 3 | Cinto de rank 1: azul vs verde | ✅ **Leitura errada nossa.** É **verde**; o azul é a cor do UNIFORME |
| 10 | Tokens roxo-espinho: 200 vs "algumas centenas" | ✅ **Nuance real, não contradição.** Estoque ativo vs. total já emitido |
| 11 | Vertical crash Gu: 5 vs 3 respirações | ✅ **Nuance real.** 5 = cooldown; 3 = defasagem entre os DOIS Gu |
| 14 | Bone Flesh Unity "Indissoluble": 60% vs 6% | ✅ **Consistente.** A hipótese do material está confirmada literalmente |

---

### 9.1 — Item 2: prêmio do exame de fim de ano (150 vs 100 pedras)

**⚠️ ERRO DO AUTOR / DA TRADUÇÃO. Sem reconciliação possível no texto — mas a assimetria de
evidência é clara.**

Ocorrências exaustivas (todo o Volume 1 varrido):

**Lado "150" — duas menções, ambas no cap. 81, ambas ANTES do exame (promessa/expectativa):**
> "But if I get first for the year end exam, I can get **a hundred and fifty primeval stones**
> as reward," Fang Yuan contemplated in his heart. (cap. 81)
> "Getting first place, not only is it **a hundred and fifty primeval stones**, but you also get
> an advantage in picking Gu worms!" — o professor, na véspera. (cap. 81)

**Lado "100" — duas menções, caps. 86 e 89, ambas DEPOIS do exame (pagamento e repercussão):**
> "Becoming first place, you have **a hundred primeval stones** as reward and also Gu worm
> choosing priority." — Gu Yue Bo, clan leader, entregando o prêmio. (cap. 86)
> "just being the first place in the year end exam gave him **a hundred primeval stones** as
> reward right?" — fofoca entre Gu Masters, dias depois. (cap. 89)

**Análise**: não há no texto qualquer menção a desconto, taxa, retenção, punição ou mudança de
regra que explique a diferença. Os dois pares são internamente consistentes e mutuamente
incompatíveis. Note-se ainda que o prêmio de **30 pedras** dado por Gu Yue Bo "em nome pessoal"
no cap. 78 é de um evento ANTERIOR e distinto, não serve de compensação (e 150 − 30 = 120, não 100).

**Recomendação para o material**: adotar **100 pedras** como valor operativo, porque (a) é o valor
efetivamente pago em cena, (b) é repetido de forma independente por um segundo personagem no
cap. 89, e (c) o valor 150 aparece só em fala prospectiva. Registrar a divergência em nota de rodapé
como inconsistência do original, não como mecânica.

---

### 9.2 — Item 3: cor do cinto de rank 1 (azul vs verde)

**✅ RESOLVIDO — e a contradição é nossa, não da obra. A cor do cinto de rank 1 é VERDE.
O "azul" nas duas passagens dissidentes é a cor do UNIFORME, não do cinto.**

O sistema completo de insígnias, reconstruído por varredura de todas as ocorrências de "belt"
no Volume 1:

| Rank | Cor do cinto | Placa | Capítulos |
|---|---|---|---|
| 1 | **verde** | cobre/bronze, nº "1" | 12, 40, 64, 93, 107 |
| 2 | **vermelho / escarlate** | aço, nº "2" | 31, 32, 69, 93, 101, 107 |
| 3 | **branco** | prata, nº "3" | 110 |

O **uniforme** (peça separada) é azul: "They wore a **blue uniform**… a headband and a waist belt
completing their appearance" (cap. 31); "she wore a **dark blue uniform**, and a **red belt**"
(cap. 32); "wearing a **deep blue uniform**, and there was a **scarlet belt**" (cap. 69).

**A passagem dissidente do cap. 31** é a frase imediatamente seguinte à descrição do uniforme azul:
"The belt had a specific function, for Rank one Gu Masters it was a blue belt. There was a bronze
plate at the front, and the number '1'… For Rank two Gu Masters, their belt was red." — ou seja,
a mesma frase que erra o rank 1 acerta o rank 2. É contaminação da cor do uniforme mencionada
uma linha antes.

**A segunda dissidência** (que o material ainda não tinha registrado) está no cap. 87, descrevendo
Fang Yuan recém-formado: "This was a **dark blue coloured battle attire**… On his head there was a
**bright blue headband**… The belt was **navy blue** with a bronze plate on it, carved with the
number '1'". Mesmo padrão: o parágrafo inteiro está saturado de azul (traje, faixa de cabeça) e o
cinto é arrastado junto.

**Evidência decisiva de que é verde** — o cap. 93 mostra a TRANSIÇÃO, e é a prova mais forte porque
contrasta as duas cores na mesma frase:
> "His belt was **no longer the green coloured Rank one belt**, but a Rank two Gu Master's **red
> coloured belt**." (cap. 93)

E o cap. 107 repete o contraste com dois personagens lado a lado: Fang Yuan "his belt was also red
colour… a Rank two Gu Master! However, he himself was still a Rank one, carrying a **green coloured
belt**."

**Veredito**: verde é canônico (5 ocorrências, incluindo as duas cenas comparativas); azul é lapso
de redação em 2 passagens descritivas onde a paleta do uniforme domina o parágrafo.

---

### 9.3 — Item 10: contagem de tokens roxo-espinho (200 vs "algumas centenas")

**✅ RESOLVIDO — NÃO é contradição. São duas grandezas diferentes, e a própria obra fornece o
mecanismo que as separa.**

As duas frases:
> "The purple thorn token could only be given out when the clan leader, or ten elders came to an
> agreement. There were only **two hundred purple thorn tokens in the world now**." (cap. 271)

> "Shang Clan has existed for thousands of years but **the number of purple thorn tokens it has
> given out** is mere a few hundred." (cap. 277)

A primeira é **estoque válido no presente** ("in the world **now**"). A segunda é **total emitido
ao longo de milhares de anos** ("has **given out**"). São métricas distintas e a segunda tem de ser
maior que a primeira.

**O mecanismo que garante isso está declarado no mesmo cap. 271** — os tokens **expiram**:
> "the purple thorn token was not a Gu worm, it only had the power of the token Gu remaining in it.
> **As time passed, the token Gu's power would decrease, and the purple thorn token would lose
> effect.** … If Fang Yuan's purple thorn token lost effect, he would have to return to Shang clan
> city and ask them to create a new one. This was a way Shang clan controlled their tokens."

Ou seja: o Shang clan emitiu "algumas centenas" em milhares de anos; a caducidade dos tokens (e a
morte dos portadores) mantém o estoque ativo em ~200. **As duas cifras são exatamente o que a
mecânica prevê.**

**Recomendação**: remover da lista de contradições e registrar como exemplo canônico do mecanismo
de caducidade/renovação dos tokens Shang.

---

### 9.4 — Item 11: recarga do vertical crash Gu (5 vs 3 respirações)

**✅ RESOLVIDO — NÃO é contradição. As "3 respirações" nunca foram um cooldown: são a DEFASAGEM
entre os cooldowns de dois Gu diferentes.**

O cooldown real, declarado sem ambiguidade:
> "He knew very clearly the vertical crash Gu could only charge fifty steps ahead. **Every time it
> is used, there is a cooldown period of five breaths.**" (cap. 290)

E o cap. 290 confirma o número na prática, duas cenas depois: "**Five breaths had long passed**,
Fang Yuan looked at Li Hao, and activated the vertical crash Gu, charging over."

A frase do cap. 291, lida por inteiro, diz outra coisa:
> "He was always paying attention to the cooldown period of **horizontal charge Gu and vertical
> crash Gu**. **There were three breaths of time interval between them.** Taking into account the
> time taken to charge fifty steps, he would always have a movement Gu to use." (cap. 291)

"Between **them**" = entre os dois Gu, não entre dois usos do mesmo. Fang Yuan mantém os dois Gu
**fora de fase em 3 respirações**: cada um recarrega em 5, mas como estão defasados, nunca há uma
janela em que ambos estejam em cooldown ao mesmo tempo. É por isso que o parágrafo conclui
"he would always have a movement Gu to use" — uma conclusão que só faz sentido sob a leitura da
defasagem, e que seria falsa se 3 fosse o cooldown.

O cap. 288 já tinha estabelecido a prática do revezamento: "Not only did he use horizontal charge Gu
or vertical crash Gu **alternatively**, he also simultaneously used all-out effort Gu."

**Veredito**: cooldown do vertical crash Gu = **5 respirações**, valor único e estável. As 3
respirações são um dado tático sobre a rotação dos dois Gu de movimento — e são, na verdade, um bom
exemplo didático de gestão de cooldowns escalonados.

---

### 9.5 — Item 14: Bone Flesh Unity "Indissoluble" (60% vs 6%)

**✅ RESOLVIDO — a leitura provável do material está CONFIRMADA literalmente. As duas formulações
são consistentes: 60% é a eficiência de conversão, 6% é o resultado sobre o total do doador.**

A tabela completa das cinco qualidades (cap. 230) — e note que o texto usa **frações**, não
porcentagens:
> "The worst quality was the **fratricidal** Gu which converted ten percent primeval essence into
> **one-fifth** of it; above it was **friendly relation** Gu which converted ten percent of primeval
> essence into **two-fifth** of it; **indissoluble relation** Gu could transfer **three-fifth**;
> **familial relation** Gu could transfer **four-fifth**; and the top **blood kin relation** Gu could
> transfer **a hundred percent** of the primeval essence without any loss in conversion." (cap. 230)

| Qualidade | Fração transferida | Equivalente % | % do total do doador (base 10%) |
|---|---|---|---|
| fratricidal | 1/5 | 20% | 2% |
| friendly relation | 2/5 | 40% | 4% |
| **indissoluble relation** | **3/5** | **60%** | **6%** |
| familial relation | 4/5 | 80% | 8% |
| blood kin relation | 5/5 | 100% | 10% |

A cena de uso fecha a conta exatamente:
> "Bone flesh unity Gu shone with green and red light respectively, converting the primeval essence;
> **six percent** of snow silver primeval essence entered Fang Yuan's aperture." (cap. 245)

0,10 × 3/5 = **0,06**. ✅

**Duas notas para o material:**
1. A base de doação é sempre **10% da essência primeval do doador** — esse 10% é fixo em todas as
   cinco qualidades; o que varia é só a fração que sobrevive à conversão.
2. O "60%" nas nossas tabelas é uma tradução correta de "three-fifth", mas **a obra escreve em
   quintos**. Vale citar a fração original, porque a escada 1/5–2/5–3/5–4/5–5/5 torna o sistema
   imediatamente legível como uma progressão regular de cinco degraus — o que a versão em
   porcentagem esconde.

A qualidade obtida depende da profundidade do vínculo entre os dois refinadores (cap. 230); Fang
Yuan e Bai Ning Bing obtiveram "indissoluble" (o degrau do meio) porque adulteraram a receita, e
porque a relação real entre eles teria rendido a pior qualidade, "fratricidal".

---

## 10. Itens 63/48 — faixa da grade "high" de blessed land (4.000 vs 6.700 km²)

**✅ RESOLVIDO — os números não divergem entre capítulos. A "divergência" era leitura nossa:
4.000 é o TETO da grade *medium* e 6.700 é o PISO da grade *super*. A grade *high* fica entre
as duas, em 4.700–6.000 km², e é declarada com esses mesmos valores em todas as passagens.**

### 10.1 A tabela canônica das quatro grades

As grades aparecem em três passagens que **se complementam sem se contradizer** (caps. 690, 939,
1027). Nenhuma delas dá as quatro grades de uma vez; juntas, dão:

| Grade | Área (km²) | Tributário do River of Time | Essência imortal / ano | Capítulos |
|---|---|---|---|---|
| low | **até 2.000** (máximo) | small tributary | mais de 10 contas | 939, 1027 |
| medium | **2.700 – 4.000** | slightly bigger tributary | mais de 20 contas | 939, 1027 |
| **high** | **4.700 – 6.000** | **large** tributary | mais de 30 contas | **690** |
| super | **acima de 6.700**, sem passar de **13.000** | gigantic tributary | mais de 50 contas | 690, 939, 1027 |

Citações literais:

> "A **low grade** blessed land has a size of **two thousand square kilometers at the maximum**, it
> can draw in a small tributary of the river of time and create over ten beads of immortal essence,
> while being a land of few resources.
> A **medium grade** blessed land can have a size of **two thousand and seven hundred square
> kilometers to four thousand square kilometers**, draw in a slightly bigger tributary of the river
> of time, create over twenty beads of immortal essence and have plentiful resources." (cap. 939)

> "**High grade** blessed lands were formed with a size of **4700km2 to 6000km2**, drew in a large
> tributary of the river of time and created **over thirty beads** of immortal essence. There would
> be plenty of heaven and earth qi remaining which could mutually interact and refine the vital Gu
> and core Gu into Immortal Gu.
> **Super grade** blessed lands were even larger with a territory of **over 6700 km2**. The tributary
> of the river of time it drew in would be gigantic and the amount of green grape immortal essence
> created would **surpass fifty beads**! If there was nothing unexpected, it could create at least
> two Immortal Gu." (cap. 690)

> "**Super grade** blessed lands had a territory of over 6700 km2 but **did not exceed 13000km2**."
> (cap. 1027)

### 10.2 O teto de 13.000 km² e a nota do autor — dois achados novos

O cap. 1027 acrescenta **duas informações que não estavam no material**:

1. **A grade super TEM teto: 13.000 km².** As outras passagens diziam apenas "over 6700 km2", o que
   sugeria uma grade aberta. Não é. A faixa super é 6.700–13.000 km².
2. **Uma nota explícita do autor**, entre parênteses, logo depois da tabela:
   > "**(The above information refers to the starting size after immortal ascension.)**" (cap. 1027)

   Isso é decisivo para o material: **as grades descrevem o tamanho NA FORMAÇÃO**, no momento da
   ascensão a imortal — não o tamanho corrente. Um blessed land cresce (por calamidades, anexações,
   gestão) e encolhe (por dano, amputação voluntária), e depois disso a grade original deixa de
   descrever a área. Isso reconcilia todos os casos concretos aparentemente fora de faixa.

### 10.3 Há lacunas ENTRE as grades — e são reais

Somando as faixas, aparecem três intervalos sem grade atribuída:

- **2.000 – 2.700 km²** (entre low e medium)
- **4.000 – 4.700 km²** (entre medium e high)
- **6.000 – 6.700 km²** (entre high e super)

A obra nunca comenta esses vãos. É **exatamente o mesmo padrão de arredondamento narrativo do
item 5** (a faixa 31–39% de aptidão, entre o topo do grau D e o piso do grau C): o autor fixa
extremos redondos por grade e não se preocupa em fazê-los encostar. Registrar como não-descrito,
com a observação de que o padrão se repete em pelo menos dois sistemas de graduação distintos —
o que reforça que é maneirismo do autor, não erro pontual.

### 10.4 Casos concretos, para conferência cruzada

Todos os blessed lands nomeados caem nas faixas certas (ou fora delas pela razão da nota do autor):

| Blessed land | Área | Grade | Fonte / observação |
|---|---|---|---|
| Hu Immortal | 4.000 km², fluxo 5× | medium (no teto) | perdeu >1.300 km² em combate; F.Y. amputa mais 600 km² |
| Tai Bai | ~4.700 km², fluxo 33× | **high** (no piso) | "Tai Bai blessed land was a high grade blessed land" |
| Lian Yun | 5.700 km² | **high** (miolo da faixa) | cap. 1449 |
| Hei Lou Lan | >6.700 km², fluxo 38× | super | Great Strength True Martial Physique (constituição extrema) |
| dream path (super) | 8.000 km², fluxo 46×, 55 contas/ano | super | bate com "surpass fifty beads" |
| aperture imortal de F.Y. (ascensão forçada) | 3.500 km², fluxo 16× | medium | "the foundation for his immortal aperture was not high" |
| sovereign immortal aperture | 335.000 km² | fora de escala | não é blessed land comum |

**Regra estrutural confirmada**: a constituição extrema (ten extreme physique) produz
automaticamente um blessed land de grade **super** na ascensão — "Once a person of the ten extreme
physiques became a Gu Immortal, like Hei Lou Lan, they would obtain a super grade blessed land!"
(cap. 1027), reforçado pelo cap. 901 (foi Thieving Heaven quem tornou isso possível).

E a **maioria dos rank 6 fica em low ou medium**: "Most rank six Gu Immortals had medium or low
grade blessed lands." (cap. 1027) — útil como calibragem: high e super são exceções, não a norma.

### 10.5 Correção a aplicar no material

- Substituir a faixa "high = entre 4.000 e 6.700 km², extremos divergem entre capítulos" por
  **high = 4.700–6.000 km²**, sem divergência: os caps. 690, 939 e 1027 são complementares e
  concordam integralmente.
- Acrescentar o **teto de 13.000 km² da grade super** (cap. 1027).
- Acrescentar a **nota do autor** de que os números são o tamanho na formação (cap. 1027).
- Registrar os três vãos entre grades como não-descritos.

