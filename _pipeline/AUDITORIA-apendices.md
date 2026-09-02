# Auditoria dos apêndices de referência (`10 - Apendices/`)

Agente: auditor dos apêndices. Escopo exclusivo: `01 - Glossário EN-PT.md`,
`02 - Tabelas de Referência Rápida.md`, `09 - Linha do Tempo e Eras.md`.
Os catálogos `03`–`08` pertencem a outro agente e **não foram tocados**.

Convenção de origem usada nas três notas (a mesma do vault): texto simples =
canônico; `(ded.)` / `inferido` = dedução segura; `*` = invenção nossa; `—` = a
obra não informa.

Status: **concluído**.

---

## Glossário

### Bug crítico: o termo em inglês estava errado, e errado de um jeito que engana

A obra **nunca** escreve "primordial essence", "primordial sea" ou "primordial
stones". A grafia canônica em inglês é **`primeval essence` / `primeval sea` /
`primeval stones`**. Contagem no texto-fonte (`grep -io`, seis volumes):

| Forma | Ocorrências na obra |
|---|---|
| `primeval essence` (só no Volume 1) | 672 |
| `primeval sea` | 175 |
| `primeval stone(s)` | 1.194 |
| `primordial essence` / `primordial sea` / `primordial stones` | **0** |

"Primordial" existe na obra, mas designa **outra coisa**: o nome próprio
`Primordial Origin Immortal Venerable` (o primeiro rank 9) e o território
`Primordial Domain`. Ou seja, o falso amigo não leva a lugar nenhum — leva ao
lugar errado.

Além do erro de raiz, a grafia estava **corrompida com um L a mais**
("primordiall essence"), o que confirma a origem: uma substituição automática
`primeval → primordial` aplicada por engano também às células do termo inglês.
O rastro está em `_pipeline/REVISAO-didatica-05-09.md:803-805`, onde o vault
ainda escrevia "essência primeva" e decidiu trocar para "essência primordial".

Nada disso afeta o **português**: a tradução brasileira publicada de fato escreve
"essência primordial" / "mar primordial" / "pedra primordial", e é a forma que o
vault deve continuar usando. O erro estava só na coluna do termo em inglês.

**Corrigido no glossário**; acrescentado um callout explicando a armadilha (quem
pesquisar "primordial essence" em inglês não acha nada).

### Efeito colateral: a tabela "Onde o vault diverge da tradução" tinha três linhas falsas

As linhas de `primeval essence`, `primeval stones` e `primeval sea` traziam a
mesma palavra nas duas colunas ("a tradução escreve *essência primordial*; o
vault escreve **essência primordial**") e mesmo assim eram apresentadas como
divergências, com uma coluna "Por quê". As seções 9.4 e 9.5 repetiam a
contradição, chegando a afirmar "o que o vault escreve é outra coisa: essência
primordial". **As três linhas foram removidas** e as duas seções reescritas para
dizer o que é verdade: aqui não há divergência nenhuma.

### Termos acrescentados

| Onde | Termos |
|---|---|
| §1 Cultivo | `pseudo venerable`; sub-tabela **das sete constituições extremas nomeadas**, mais as duas categorias que se parecem com elas e não são (*Pure Dream Reality Seeker*, *Righteous Virtue*) |
| §2 Gu | `self-harming move`, `refinement insignia` |
| §4 Reino imortal | `Primordial Domain` |
| §5 Cosmologia | `fragment world`, `Longevity Heaven`, `Earth Abyss`, e uma sub-tabela com **as cinco paredes regionais nomeadas** (*saint / licorice / miasma / raging flame / blue water regional wall*) |
| §6 Sociedade | `ultimate force`, `ten great ancient sects`, `slave Gu Immortal`, `fairy` (título) |
| §7 Raças | `mutated beast` |
| §8 Unidades | `zhang`, `chi`, `breath` (unidade tática de tempo), mais um aviso separando *jin* de *jun* |
| **§9, nova** | **Os dez Veneráveis, por nome** — os dez nomes em inglês, leitura literal e o que cada um fundou |
| **§10, nova** | **Organizações nomeadas** — as dez grandes seitas ancestrais com nome EN e PT, mais Tribunal Celestial, Longevity Heaven, Lang Ya, Shadow Sect, Zombie Alliance, Demon Expelling Sect, Imperial Court, Demon Judgment Board, Treasure Yellow Heaven; e a distinção formal *super force* × *ultimate force* |
| §11 (antiga §9) | seção de avisos renumerada; subseções 9.1–9.9 → 11.1–11.9; as referências internas a "seção 9" foram reescritas |

Também acrescentado ao verbete `immortal essence stone`: **só o Tribunal Celestial
consegue produzi-las** (cap. 466), que é fato de sistema e não estava em lugar nenhum
do glossário.

### O que a obra não define (registrado, não preenchido)

- **A décima, a nona e a oitava constituições extremas.** A obra afirma que são dez
  e nomeia **sete**. A nota temática `01 - Cultivo/08` já registrava isso; o glossário
  agora repete o aviso, porque listas de dez nomes circulam em fontes secundárias e
  contêm invenção.
- **O fundador de seis das dez grandes seitas** e **o tamanho de nove delas**.
- **Quantos segundos é uma "respiração".** A obra usa a unidade o tempo todo e nunca a
  converte. Registrada com `*` como "da ordem de um segundo".
- **`zhang` e `chi` em metros.** A obra nunca os converte (ao contrário do `li`, que tem
  nota de tradução fixando 500 m). Registrados com `*` pelo valor chinês tradicional.

### Decisão de escopo: nomes de lugar não entraram em massa

Uma varredura das notas finais devolveu **mais de mil** nomes próprios em inglês, a
esmagadora maioria topônimos do `04 - Mundo/05 - Atlas das Cinco Regiões.md`. Listá-los
no glossário duplicaria o Atlas inteiro e envelheceria mal. Entraram apenas os nomes de
**alcance sistêmico** (as cinco paredes regionais, as dez seitas, os dois territórios de
categoria máxima, os mundos-fragmento, o Abismo da Terra). O Atlas continua sendo o
lugar dos topônimos.

---

## Tabelas

### Números corrigidos

**1. As faixas de dao marks por rank estavam erradas em dois dos quatro ranks — e a nota
declarava "erro nosso" justamente o valor certo.**

A obra enuncia as quatro faixas de uma vez só (cap. 2071), e uma segunda passagem
independente reconfirma a do rank 7 (cap. 1310):

> "on average: rank six Gu Immortals had zero to nine thousand dao marks. Rank seven Gu
> Immortals had **ten thousand to thirty thousand**. Rank eights had **one hundred
> thousand to three hundred thousand**." (cap. 2071)

| Rank | A tabela trazia | A obra diz |
|---|---|---|
| 6 | 0 – 9.000 | 0 – 9.000 ✅ |
| 7 | 9.000 – 30.000 | **10.000 – 30.000** |
| 8 | **30.000** – 300.000 | **100.000 – 300.000** |
| 9 | ≥ 300.000 | ≥ 300.000 ✅ |

O agravante: a nota trazia um callout afirmando que "uma versão anterior desta tabela
trazia 100.000 como piso do rank 8; era erro nosso, sem base no texto, e foi corrigido".
**O 100.000 era o valor canônico**, e foi restaurado. O que produziu o engano foi uma
reconstrução aritmética elegante (calendário de provações × rendimento por provação) que
reproduz bem o **teto** de cada rank e não reproduz o **piso** do rank 8.

Consequência de leitura que a correção revela e que ficou registrada na nota: entre o
teto do rank 7 (30.000) e o piso do rank 8 (100.000) há um **vão de 70.000 marcas** que
nenhuma provação de rank 7 preenche — passar de 7 para 8 é um salto, não uma continuação.

**2. A quarta coluna da tabela de cadência (seção 8) era conta nossa apresentada como
texto, e a obra a contradiz uma vez.** Agora está marcada `inferido`, com as duas
passagens em conflito registradas:

- a favor da regra "a provação mais alta substitui a mais baixa": um imortal recém-ascendido
  enfrenta **exatamente nove** calamidades terrenas antes da primeira tribulação celestial;
- contra: "After three hundred years, facing a total of **thirty** earthly calamities and
  three heavenly tribulations, they could advance to a rank seven Gu Immortal" (cap. 826)
  — trinta e três provações, sem substituição nenhuma.

Mantivemos a substituição (é a única leitura que faz as três linhas baterem com os tetos
canônicos), mas a alternativa está registrada.

**3. A grade super de terra abençoada tem teto, e a tabela a dava como aberta.**
"Super grade blessed lands had a territory of over 6700 km2 but **did not exceed
13000km2**" (cap. 1027). Corrigido nas seções 9 e 13.3.

**4. As grades descrevem o tamanho de nascimento — e a obra diz isso literalmente.**
Nota do autor, entre parênteses, logo após a tabela: "(The above information refers to
the starting size after immortal ascension.)" (cap. 1027). Acrescentado, porque é o que
reconcilia todos os exemplos concretos que aparecem fora da faixa da própria grade.

**5. O teto do fluxo de tempo estava defasado.** A seção 9 dava "1:5 a 1:38". A obra
descreve uma terra abençoada de grade super rodando a **1:46** e chama isso de "the
standard of a super grade blessed land, there was nothing out of the norm" (cap. 2090).
Corrigido para 1:5–1:46, com quatro pontos de calibração canônicos (1:33, 1:36, 1:38, 1:46).

**6. A faixa do grau D estava marcada como canônica e não é.** A obra define C, B e A num
bloco só ("40-59 é C, 60-79 é B, 80+ é A", cap. 198) e define o D noutro capítulo, isolado,
como "**twenty to thirty percent**" (cap. 1491). Sobra a faixa 31–39% sem grau atribuído, e
varredura completa do corpus não devolve **nenhum** personagem nela. Mantivemos **20–39%**
como número do projeto — porque é a leitura mais defensável e porque o vault inteiro já a
usa —, mas a linha agora diz explicitamente que a metade de cima é convenção nossa.

**7. Duas divergências internas que a nota registrava como abertas já estavam resolvidas**
(o piso 2.700 da grade média, hoje correto em `04 - Mundo/06`; e o fluxo de tempo). Os dois
avisos obsoletos foram substituídos por um registro de resolução.

### Linhas acrescentadas às seções existentes

- **§2 (limiar de ruptura):** o contraexemplo documentado de uma ruptura de rank 2 para
  rank 3 gasta com **38%** da reserva, usando um Gu consumível que converte toda a essência
  da abertura numa essência especial mais agressiva (cap. 152) — e que cobra o atalho em
  **queda permanente de aptidão**. É o que a ressalva "sem situações especiais" está
  segurando.
- **§5 (essências imortais):** a linha do **yellow apricot** (rank 9), que faltava; a tabela
  de câmbio completa em pedras de essência imortal (1 / 100 / 10.000 / 1.000.000, fator ×100
  por rank, verificado em três passagens independentes); a **sobretaxa de ~30%** por acionar
  um Gu com essência de rank inferior (cap. 1206), que **não** é câmbio e vinha sendo somada
  ao câmbio em material antigo do projeto; e o aviso de que riqueza mortal **não converte na
  prática** em riqueza imortal (cap. 668: uma imortal com "bilhões de pedras primordiais e
  nenhuma pedra de essência imortal" simplesmente não consegue comprar).
- **§6 (dao marks):** a coluna de origem, e o aviso de que os quatro valores são **médias**
  explícitas — a obra mostra tribulação celestial rendendo 1.000 em vez de 750 e calamidade
  terrena rendendo 9.000 de um caminho, sempre pela mesma regra ("quanto mais perigosa,
  maior o pagamento").
- **§8 (cadência):** o calendário pertence à **terra abençoada, não à pessoa**, e continua
  correndo depois da morte do dono até desfazê-la; quanto maior a fortuna, mais forte a
  provação (a nevasca decenal que castiga uma região é a calamidade de uma única terra
  abençoada transbordando); e a "idade" de um imortal se conta **em tribulações**, que é a
  forma corrente de informar patamar dentro de um rank.
- **§9 (grades):** coluna do afluente do Rio do Tempo, e o dado de calibragem de que **a
  maioria dos rank 6 tem terra de grade baixa ou média** (cap. 1027) — alta e super são
  exceção, não norma.
- **§12 (refino):** a linha de **50–60% de sucesso em rank 8** para quem opera uma Casa de
  Gu Imortal construída para refinar (caps. 2079-2080), taxa alta o bastante para produzir
  em série e por isso mesmo motivo de guerra.
- **§19.2 (manutenção):** as âncoras de custo de vida trazidas pelo coordenador, todas
  conferidas — família mortal de três pessoas vive com **1 pedra por mês** (cap. 11); dois
  Gu de rank 1 comem **~0,9 pedra por dia** (cap. 23); quatro Gu custam mais de 2 pedras/dia
  só de comida e **~5 pedras/dia** somando cultivo e sustento (cap. 64); refinar um Gu de
  rank 1 custa **~7 pedras** em média (cap. 11).

### Números vindos das auditorias irmãs (`02 - Gu/` e `06 - Economia e Vida/`)

Todos foram reconferidos no texto-fonte antes de gravar. Um foi recusado.

| Item | Veredito | Onde entrou |
|---|---|---|
| **3 a 5 Gu** para um Mestre Gu comum; 7 como caso explicitamente excepcional (cap. 137) | ✅ confirmado literalmente | nova seção 20 |
| A abertura tem **limite físico** de quantos Gu comporta, separado do limite financeiro (cap. 222); abertura mortal não guarda um segundo Gu Imortal (cap. 969) | ✅ confirmado | nova seção 20 |
| **0,9 pedra por dia** para dois Gu de rank 1; **1 pedra por mês** para uma família mortal de três (caps. 11, 23) | ✅ confirmado, e a obra dá ainda mais: 4 Gu = 2+ pedras/dia só de comida, ~5 pedras/dia com cultivo e sustento (cap. 64); refinar um Gu de rank 1 custa ~7 pedras (cap. 11) | §19.2 |
| **Escada de pedágio urbano 1 / 10 / 100 / 200 / 600** por anel (caps. 260, 261, 293, 1973) | ✅ confirmado nos cinco degraus, mais um sexto que é o mais interessante: **do segundo anel interno para dentro o dinheiro não entra**, só ficha de autoridade (cap. 261) | nova §19.4; a linha antiga da §13.8 virou remissão |
| **Escada de lucro por honestidade** — 7 a 8× no comércio honesto ("o limite deste mundo"), 10+× no ilegal, dezenas de vezes na fraude, e o assalto que "não precisa de capital" (cap. 243) | ✅ confirmado literalmente, nos quatro degraus | nova §19.5 |
| **Spread de compra e venda de Gu** (loja paga ~250, mercado vende ~500) | ✅ confirmado, e a aparente contradição entre os caps. 262 e 278 se resolve: o 262 é uma cena de **venda ao balcão**, o 278 é a tabela de **preço de mercado** | §19.1, num callout |
| **Custo de vida por rank**: rank 3 calcula que 420.000 pedras "não durariam um ano" (cap. 278); ranks 4 e 5 em silêncio | ✅ confirmado. O valor do rank 1 (~1.500/ano) **não** é literal: é aritmética sobre as ~5 pedras/dia do cap. 64, e entrou marcado `(ded.)` | §19.3 |
| **Nascente portátil: 50 pedras por dia** (cap. 273) e **negócio de vila que se paga em 2–3 anos** (cap. 112) | ✅ confirmado | §19.3 |
| **Desconto de um terço por ficha de autoridade** (cap. 272) | ❌ **não incluído** | ver abaixo |

**Por que a ficha de autoridade entrou sem o desconto de um terço.** Busquei o texto por
"one-third", "discount", "cheaper" e "reduce the price" no bloco dos caps. 259–280 e não
encontrei nenhuma passagem associando a ficha a uma redução percentual de preço. O que a
obra documenta sobre a ficha é outra coisa, e mais forte: ela **destrava acesso** (há Gu,
imóveis e anéis inteiros da cidade que "não são mais problema de pedras primordiais" e
exigem ficha de nível suficiente, cap. 261) e **isenta pedágio** (uma ficha específica
dispensa três pessoas das taxas de entrada, cap. 293). Registrei essas duas funções e
deixei o desconto de fora. Se ele existir num capítulo que não localizei, é fácil
acrescentar depois — mas, pela regra do projeto, não gravo número que não vi.

**Efeito colateral: a escada de preços de Gu da §19.1 foi refeita inteira.** Eu a tinha
montado por agregação de casos avulsos (250 / milhares / 100.000 / 250.000). O cap. 278
publica a escada completa num parágrafo só — **500 / 500–1.000 / 1.000–10.000 /
10.000–100.000 / 100.000–1.000.000, e rank 6 nunca vendido** — e é ela que passou a valer,
com os casos avulsos rebaixados a pontos de calibragem. O mesmo parágrafo deu de brinde a
escada dos Gu de relíquia (2.000 / 8.000 / 50.000 / ~300.000), que não estava em lugar
nenhum do vault.

### Seções novas

| # | Seção | O que traz |
|---|---|---|
| 14 | **Recuperação e custo de essência primordial** | reposição natural por grau (4%/h no C, 8%/h no A — canônico, cap. 10; B e D interpolados); custo em % de ações típicas (10% por lâmina de luar, 20% por folha de vitalidade, 70% para vencer um duelo de rank 2); supressão de essência por rank do alvo (60/30/15%, cap. 156); e a escada completa de **transferência de essência entre pessoas** (1/5 → 5/5 conforme o grau de parentesco do Gu usado, cap. 230) |
| 15 | **Força do caminho da força, em jun** | 1 jun = 30 jin ≈ 15 kg; 30 jun = estreante; 70 jun = "apenas passável" num rank 4 inicial; 100+ jun = faixa do rank 5; 500 jun = pico documentado com amplificador; e a regra de que **o corpo tem teto próprio**, separado da força gerada |
| 16 | **Fundação de alma** | a escada decimal completa até 100 milhões de *man soul* (o teto humano, onde a alma solidifica), a sub-escada até 900 milhões, a ruptura para *desolate soul* e o teto absoluto de 100 milhões de *desolate soul*; mais o aviso sobre o ruído de tradução nos caps. 1481-1503 |
| 17 | **Longevidade** | ~100 anos para humano e para Mestre Gu de qualquer rank (subir de rank **não** estende vida); ~1.000 para homens-de-pedra; milhares para alguns rank 7/8; 25.000 / 19.000 / ~7.000 / ~3.000 para os Veneráveis; 100.000+ por hibernação selada; os cinco graus documentados de lifespan Gu (15/100/300/500/1.000 anos); e a tabela de **atalhos pagos em anos de vida** |
| 18 | **Demografia** | bilhões de habitantes por região, várias centenas de rank 4, menos de 50 rank 5 (cap. 538), cinco rank 8 "à vista" numa região (cap. 736); e o registro de que a base da pirâmide a obra não dá |
| 19 | **Preços de referência** | escada de preço de Gu por rank (250 → 100.000 → 250.000 pedras), custo de manutenção, e rendimento de uma nascente espiritual (≥100 milhões de pedras em 50–60 anos) |
| 19.4 | **Pedágios urbanos por anel** | a escada 1 / 10 / 100 / 200 / 600 pedras, mais o degrau em que o dinheiro deixa de funcionar e só a ficha de autoridade abre a porta; e os aluguéis do anel caro |
| 19.5 | **A escada de lucro por honestidade** | 7–8× honesto (declarado como o teto do mundo), 10+× ilegal, dezenas de vezes na fraude, ilimitado e sem capital no assalto |
| 20 | **Capacidade da abertura** | **3 a 5 Gu** para um Mestre Gu comum (cap. 137), 7 como caso explicitamente excepcional; nenhuma escala por rank na obra; abertura mortal não comporta um segundo Gu Imortal (cap. 969); e a distinção entre o limite **físico** da abertura e o limite **financeiro** da alimentação (cap. 222) |

### Divergências encontradas em notas de outras pastas (NÃO corrigidas por mim)

Todas de números que a tabela soberana agora contradiz. O orquestrador precisa mandar
corrigir:

| Arquivo | Linha(s) | O que está lá | O que deveria estar |
|---|---|---|---|
| `01 - Cultivo/12 - Dao Marks.md` | 67, 68 | rank 7 = 9.000–30.000; rank 8 = **30.000**–300.000 | rank 7 = **10.000**–30.000; rank 8 = **100.000**–300.000 |
| `01 - Cultivo/12 - Dao Marks.md` | 80-81, 91-92 | a derivação aritmética apresentada como origem das faixas | manter como estimativa `inferido`; a origem das faixas é texto direto (cap. 2071) |
| `01 - Cultivo/13 - Tornar-se Venerável.md` | 61 | "um rank 7 fica entre 9.000 e 30.000; um rank 8, entre 30.000 e 300.000" | idem acima; e a frase "os 300.000 são o que o calendário rende, nem um a mais" precisa virar `inferido` |
| `01 - Cultivo/10 - Tribulações e Calamidades.md` | 53 | a contagem "27 calamidades + 3 celestiais" dada como canônica | marcar `inferido` e registrar o cap. 826 ("trinta calamidades terrenas e três tribulações celestiais") |
| `04 - Mundo/09 - Blessed Lands e Grotto-Heavens.md` | 63 | grade super = "acima de 6.700 km²" | **6.700 a 13.000 km²** (cap. 1027) |
| `04 - Mundo/06 - Escala, Distâncias e Viagem.md` | 145 | grade super = "mais de 6.700 km²" | idem |
| `01 - Cultivo/08 - As Dez Constituições Extremas.md` | 82 | grade supra "acima de 6.700 km²"; fluxo de tempo "quarenta para um" | acrescentar o teto de 13.000 km²; o fluxo documentado de uma terra super é **1:38 e 1:46**, não 1:40 |
| `04 - Mundo/09 - Blessed Lands e Grotto-Heavens.md` | tabela de grades | falta a nota do autor de que as áreas são o **tamanho na ascensão** | acrescentar (cap. 1027) |
| `01 - Cultivo/03 - Aptidão.md` | 28, 58-60, nota 191 | argumenta que 20–39% é o D e que "20-30%" caracteriza o D típico | a decisão (20–39%) fica mantida no vault, mas a nota afirma que a faixa é canônica; precisa marcar a metade superior como convenção do projeto, como a tabela soberana agora faz |
| `05 - Sociedade/04 - Tipos de Gente e Filosofias de Vida.md` | 187, 196, 759 | D = 20–39% sem ressalva | idem |

| `04 - Mundo/06 - Escala, Distâncias e Viagem.md` | 458 | "Pedágio de cidade-clã \| 10 pedras por pessoa" | são cinco degraus, de 1 a 600 pedras conforme o anel — ver §19.4 das Tabelas |

**Não é divergência, é lacuna:** a pasta `08 - Eventos e Cenarios/` estava vazia no
momento desta auditoria (outros agentes escreviam em paralelo; pode ter mudado desde então).

**Conferido e sem divergência:** `06 - Economia e Vida/13 - Preços, Renda e Custo de Vida.md`
e `06 - Economia e Vida/02 - Pedras Primordiais.md` já trazem o spread de 250/500 e a escada
de pedágio corretos — batem com a tabela soberana.

---

## Linha do tempo

### Marcos acrescentados

**1. Uma régua de datas, que a nota declarava não existir.** A nota afirmava que "as eras
não têm datas de fronteira precisas na obra". Isso é verdade para as *fronteiras*, mas a
obra ancora **quatro das cinco eras** em distâncias redondas do presente, e o fazia de
forma consistente em dezenas de passagens:

| Era | Distância | Passagens |
|---|---|---|
| Antiguidade Imemorial | **—** a obra nunca a data | (varredura sem resultado) |
| Antiguidade Remota | **~3 milhões de anos** | caps. 490, 956, 1005, 1070 |
| Antiguidade Antiga | **~1 milhão de anos** | cap. 1337 |
| Antiguidade Medieval | **~300 mil anos** | caps. 653, 1073, 1128, 1191, 1249, 1285 |
| Antiguidade Tardia | **~100 mil anos** | caps. 695, 1012 |

Duas leituras derivadas entraram na nota: **as eras encurtam** (2 milhões → 700 mil →
200 mil → 100 mil), e **a era atual já dura cerca de 100 mil anos sem produzir um
Venerável**, o intervalo mais longo desde que existem rank 9.

**2. Quem destruiu os sete céus.** A nota dizia apenas que "sete foram destruídos". A obra
nomeia os responsáveis: os **dez filhos do Ancestral Humano** (caps. 740, 871, 912) — que
são, ao mesmo tempo, **as dez constituições extremas** (caps. 135, 181). Isso amarra o
sistema de aptidão à cosmologia num único fato, e não estava em lugar nenhum da nota.

**3. Como a Antiguidade Imemorial termina.** O Ancestral Humano reuniu os corpos dos dez
filhos e se sacrificou com eles dentro de um Gu específico, cujo estômago arrebentou e
**espalhou vida** pelo mundo (caps. 181, 730). É o fecho do livro fundador e o mito de
origem da abundância biológica do mundo atual.

**4. Os mundos-fragmento.** Pedaços dos céus destruídos que caíram sobre as cinco regiões
e viraram pequenos mundos visitáveis — a única fonte dos materiais que já não existem
(caps. 740, 871, 912). Boa parte deles terminou de cair durante a Antiguidade Remota.

**5. Os três Supremos Grão-Mestres de refinamento da história** (cap. 598), um por era:
Old Eccentric Tian Nan (Remota, morreu tentando refinar o céu — a nota já tinha o feito,
sem o nome), **Old Immortal Kong Jue** (Antiga, a pesquisa mais profunda já feita sobre
aberturas imortais e o tratado que ainda é referência — **estava inteiramente ausente**) e
Long Hair Ancestor (Medieval, já presente). Nenhum dos três foi Venerável: é o registro
mais limpo de que attainment e rank são eixos independentes.

**6. A evolução institucional clã × seita, era a era** (cap. 704), que virou seção própria:
Remota — as seitas são inventadas e são raras; Antiga — os clãs superam as seitas;
Medieval — **empate**, os dois avançam no mesmo ritmo; Tardia — os clãs enfraquecem e as
seitas florescem; era atual — quase não restam clãs no Continente Central.

**7. Marcos menores por era:** o mercado universal dos imortais foi fixado num ponto do
mundo há 300 mil anos e nunca mais se moveu, e **onde ele fica é mistério em aberto**, com
gerações de imortais do caminho da sabedoria tentando deduzir sem sucesso (cap. 1073); a
aliança mundial dos zumbis é da Antiguidade Medieval (cap. 653); as feras imemoriais mais
antigas do mundo aparecem na Antiguidade Antiga e atravessam três eras (cap. 1337).

**8. A tabela-resumo ganhou coluna de datas** e os marcos institucionais novos.

### O que já estava certo (conferido)

- A sequência das cinco eras nomeadas está correta e completa: **Immemorial → Remote →
  Olden → Medieval → Late Antiquity → hoje** (caps. 522, 552). Não falta nenhuma era.
- A alocação dos dez Veneráveis por era bate com o texto, e a trava de conferência
  (a soma tem de dar dez) funciona.

---

## Decisões tomadas

1. **Manter "essência primordial" em português e corrigir só o inglês.** A alternativa
   seria voltar a "essência primeva" (mais fiel a *primeval*), o que exigiria reescrever
   dezenas de notas e afastaria o vault da tradução publicada, que a designer pode
   consultar. Descartada.
2. **Manter o grau D como 20–39%**, marcando a metade de cima como convenção do projeto,
   em vez de recuar para os 20–30% canônicos. O recuo tornaria erradas cinco notas
   temáticas e deixaria um décimo da escala de aptidão sem grau nenhum, num sistema que a
   obra afirma classificar todo mundo em quatro graus. A alternativa (mostrar 20–30% e uma
   linha "sem grau" para 31–39%) foi escrita e depois descartada por isso.
3. **Adotar a regra da substituição de provações** na seção 8, apesar do cap. 826, porque é
   a única leitura que faz os tetos de dao marks fecharem. A alternativa fica registrada
   dentro da própria nota, não escondida aqui.
4. **Não inchar o glossário com topônimos.** Entraram só os nomes de alcance sistêmico; o
   Atlas continua sendo o lugar dos mais de mil nomes de lugar.
5. **Não criar apêndice novo.** Considerei um índice remissivo e uma tabela de conversão de
   unidades. O índice seria duplicata do buscador do Obsidian e envelheceria a cada nota
   nova; a conversão de unidades cabe inteira na seção 8 do glossário mais a 13.1 das
   tabelas, e separá-la só criaria um terceiro lugar para o mesmo número divergir. **A
   pasta continua com nove notas e nenhuma renumeração é necessária.**
6. **Ordem de leitura das seções novas das Tabelas:** foram acrescentadas ao fim (14 a 20),
   sem renumerar as existentes, para não quebrar os links com âncora de seção que outras
   notas já usam (por exemplo `[[02 - Tabelas de Referência Rápida#5. Escala de valor das
   essências imortais]]`, citado em `01 - Cultivo/13`).
7. **Registrar, não corrigir, os números errados de outras pastas.** Conforme o escopo.

---

## O que a obra realmente não diz

Tudo abaixo foi buscado no texto-fonte com busca case-insensitive antes de ser declarado
ausente. São lacunas do texto, não da pesquisa.

- **Uma escala de quantos Gu se carrega por rank.** A obra dá "três a cinco" para o Mestre
  Gu comum e nada mais. Qualquer tabela por rank é invenção.
- **A faixa de aptidão 31–39%.** Nenhum personagem em toda a obra tem aptidão declarada
  nessa faixa, e a obra afirma que os graus são quatro.
- **Os limiares percentuais de ruptura acima do 55%.** A obra enuncia **um só** limiar, o
  do rank 1 → 2. Os 65/75/85 da seção 2 continuam marcados como invenção, e há um
  contraexemplo de ruptura 2 → 3 com 38%.
- **O desconto percentual da ficha de autoridade de clã.** Ela destrava acesso e isenta
  pedágio; nenhuma passagem localizada a associa a um abatimento de preço.
- **O custo de vida de um Mestre Gu de rank 4 e de rank 5.** Os ranks 1 e 3 têm âncora.
- **O custo de refino em porcentagem de essência acima do rank 1**, e o **tempo de refino
  por rank**. A obra cronometra um único refino em detalhe (rank 1, meia hora para 1/12 do
  trabalho) e nunca fecha a escala.
- **A taxa de reposição de essência usando pedras primordiais.** A obra afirma repetidas
  vezes que é o método rápido e nunca dá o número.
- **A base da pirâmide demográfica** (quantos rank 1, 2 e 3 existem). O topo é canônico e
  detalhado; a base, não.
- **A expectativa de vida de um Gu Imortal de rank 6.**
- **Quantos segundos dura uma "respiração"**, a unidade tática do mundo.
- **A conversão de `zhang` e `chi`** (o `li` tem nota de tradução; esses dois, não).
- **A força em jun nos ranks 1 a 3 e 6 a 9.** A escada existe entre 30 e 500 jun e não é
  ancorada fora dessa faixa.
- **A área do Mar Oriental e do Deserto Ocidental** (as outras três regiões têm número).
- **O preço de uma passagem de caravana** — e aqui o silêncio é informativo: não se compra
  passagem, entra-se como pessoal contratado ou mercador com carga.
- **A localização do mercado universal dos imortais.** É mistério declarado *dentro* da
  ficção, não lacuna nossa: gerações de especialistas em dedução tentaram e falharam.
- **A data da Antiguidade Imemorial.** As outras quatro eras têm âncora; essa não, e o nome
  é literal.
- **Os nomes de três das dez constituições extremas** e **o fundador de seis das dez grandes
  seitas**.

### Uma contradição interna da obra, registrada e não resolvida

A obra afirma, em dois lugares, densidades de rank 5 que diferem por duas ordens de
grandeza:

- "in the entire northern plains, there were billions of people… but only several hundred
  rank four Gu Masters, and **less than fifty rank five** Gu Masters" (cap. 538);
- "only **one or two rank five** Gu Masters might appear among a million people" (cap. 409).

Numa região de bilhões, a segunda daria milhares de rank 5. **Adotamos a contagem
regional** (cap. 538), porque é específica e nomeada, e tratamos a outra como figura de
linguagem ilustrando o formato de pirâmide. A divergência está registrada dentro da
própria seção 18 das Tabelas, com a justificativa — não escondida aqui.
