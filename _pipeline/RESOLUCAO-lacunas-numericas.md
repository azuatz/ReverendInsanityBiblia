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

