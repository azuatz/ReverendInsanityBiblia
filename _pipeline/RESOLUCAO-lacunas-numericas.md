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

