# Auditoria de completude — `03 - Paths/`

**Data:** 2026-09-02 · **Escopo:** todas as notas de `03 - Paths/`.
**Pergunta de partida:** a pasta tem 17 caminhos com nota própria, mas o
`10 - Apendices/08 - Catálogo de Golpes - Imortais.md` organiza os golpes em ~35 caminhos.
Quantos caminhos a obra realmente nomeia, e quais ficaram sem cobertura?

**Método:** cruzamento de quatro fontes —
(a) varredura do texto-fonte com `grep -hioE "\b[a-z]+ path\b"` nos seis volumes, com
contagem de ocorrências e leitura de contexto para descartar falsos positivos;
(b) os cabeçalhos de caminho dos dois catálogos de golpes (`10 - Apendices/07` e `08`);
(c) `_pipeline/rascunho/paths.md`;
(d) **a enumeração canônica do cap. 1323**, que é a espinha dorsal desta auditoria (ver abaixo).

---

## O achado que reorganiza o domínio: a enumeração canônica do cap. 1323

A obra tem **uma passagem que enumera os caminhos principais por era de criação**, em forma
de aula. Ela estava citada no campo `fontes` da `01 - Visão Geral dos Paths.md`, mas o seu
conteúdo — a lista e a cronologia — **não estava aproveitado em lugar nenhum da pasta**.
Transcrição resumida (cap. 1323, um Imortal do caminho das formações ensinando o filho):

> - **Antiguidade Imemorial (era de Ren Zu):** *space path* e *time path* — "estes dois
>   caminhos pesquisaram e expuseram as profundidades do tempo e do espaço".
> - **Antiguidade Remota:** Primordial Origin criou *qi path* e *enslavement path*;
>   Star Constellation criou *wisdom path* e *star path*; *formation path* nasceu no período
>   tardio da era, com fundador não verificável; *refinement path* e *fire path* também.
> - **Antiguidade Passada (Olden Antiquity):** Limitless Demon Venerable criou *rule path*;
>   Reckless Savage criou *transformation path*; *strength path*, *wind path*, *light path*
>   e *dark path* também nasceram aqui.
> - **Antiguidade Medieval:** Genesis Lotus criou *wood path*; Thieving Heaven criou
>   *theft path*; Giant Sun criou *luck path*; e surgiram *metal path*, *water path*,
>   *ice and snow path*, *cloud path*, *earth path*, *lightning path*, *information path*
>   e *sound path* — "uma era em que todo tipo de caminho diverso apareceu".
> - **Era atual (Antiguidade Tardia em diante):** criou-se *bone path*; existem também
>   *phantom path* e *restriction path*.
> - E o encerramento decisivo: *"o que mencionei são apenas os caminhos **principais** de
>   Mestres Gu; caminhos menores como **enchantment path**, **illusion path** e outros ficam
>   omitidos por ora."*

Três consequências para o vault:

1. **A obra distingue formalmente caminhos principais de caminhos menores.** Essa distinção
   não existia em nenhuma nota da pasta e é a chave de organização correta do domínio.
2. **A lista de "mainstream" do cap. 1323 tem 25 caminhos** — e sete deles não tinham nota:
   qi, formation, wind, light, dark, wood, metal, water, ice-and-snow, cloud, earth,
   lightning, information, sound, theft, bone, phantom, restriction (dezoito, na verdade).
3. **A cronologia por era é canônica e estava perdida.** Ela responde sozinha a pergunta
   "de onde vêm os caminhos" que a `01 - Visão Geral` levanta e deixa em aberto.

---

## Inventário de caminhos da obra

`Ocorr.` = número de linhas-parágrafo distintas dos seis volumes que contêm a expressão
`<nome> path` (com `grep -i`, deduplicado). É uma medida de **massa textual disponível**,
não de importância no mundo.

*(tabela preenchida ao longo da auditoria — ver seções seguintes)*

### Caminhos reais confirmados

| # | Nome (inglês) | Ocorr. | Classe na obra | Tinha nota? | Decisão |
|---|---|---:|---|---|---|
| 1 | wisdom path | 2164 | principal | ✅ `12` | auditada |
| 2 | refinement path | 1692 | principal | ✅ `07` | auditada |
| 3 | strength path | 1629 | principal | ✅ `04` | auditada |
| 4 | time path | 1227 | primordial | ✅ `13` | auditada |
| 5 | luck path | 797 | principal | ✅ `18` | auditada |
| 6 | **information path** | 733 | principal | ❌ | **nota própria nova** |
| 7 | soul path | 697 | principal | ✅ `10` | auditada |
| 8 | dream path | 693 | ainda não fundado | ✅ `19` | auditada |
| 9 | heaven path | 665 | principal (incultivável) | ✅ `17` | auditada |
| 10 | **human path** | 663 | principal, "o mais singular" | ❌ | **nota própria nova** |
| 11 | blood path | 635 | principal | ✅ `03` | auditada |
| 12 | **qi path** | 625 | principal, **extinto** | ❌ | **nota própria nova** |
| 13 | enslavement path | 590 | principal | ✅ `06` | auditada |
| 14 | transformation path | 550 | principal | ✅ `05` | auditada |
| 15 | **earth path** | 466 | principal | ❌ | nota coletiva (elementais) |
| 16 | **formation path** | 447 | principal, "o mais complexo" | ❌ | **nota própria nova** |
| 17 | **fire path** | 395 | principal | ❌ | nota coletiva (elementais) |
| 18 | **water path** | 346 | principal | ❌ | nota coletiva (elementais) |
| 19 | food path | 312 | principal | ✅ `15` | auditada |
| 20 | **wood path** | 299 | principal | ❌ | nota coletiva (elementais) |
| 21 | sword path | 279 | principal | ✅ `09` | auditada |
| 22 | space path | 260 | primordial | ✅ `11` | auditada |
| 23 | star path | 214 | principal | ✅ `14` | auditada |
| 24 | **theft path** | 189 | principal, "não mainstream" | ❌ | **nota própria nova** |
| 25 | rule path | 182 | principal, "mãe" | ✅ `16` | auditada |
| 26 | **light path** | 181 | principal | ❌ | nota coletiva (elementais) |
| 27 | **wind path** | 162 | principal | ❌ | nota coletiva (elementais) |
| 28 | **sound path** | 138 | principal | ❌ | **nota própria nova** |
| 29 | **dark path** | 131 | principal | ❌ | nota coletiva (elementais) |
| 30 | **metal path** | 107 | principal | ❌ | nota coletiva (elementais) |
| 31 | **phantom path** | 99 | ramo da regra | ❌ | nota coletiva (demais) |
| 32 | poison path | 98 | principal | ✅ `08` | auditada |
| 33 | **ice path** | 83 | principal | ❌ | nota coletiva (elementais) |
| 34 | **snow path** | 75 | principal | ❌ | nota coletiva (elementais) |
| 35 | **lightning path** | 74 | principal | ❌ | nota coletiva (elementais) |
| 36 | **cloud path** | 71 | principal | ❌ | nota coletiva (elementais) |
| 37 | **painting path** | 67 | especialidade de Venerável, secreto | ❌ | **nota própria nova** |
| 38 | **blade path** | 54 | "extremamente pequeno" | ❌ | nota coletiva (demais) |
| 39 | **bone path** | 30 | principal, criado na era atual | ❌ | nota coletiva (demais) |
| 40 | **pill path** | 27 | novo, era atual | ❌ | nota coletiva (demais) |
| 41 | **emotion path** | 22 | ramo da sabedoria | ❌ | nota coletiva (demais) |
| 42 | **restriction path** | 15 | ramo da regra | ❌ | nota coletiva (demais) |
| 43 | **weapon path** | 11 | novo, "criado toscamente" | ❌ | nota coletiva (demais) |
| 44 | **killing path** | 11 | **nunca criado** | ❌ | nota coletiva (demais) |
| 45 | **moon path** | 8 | menor, com marcas próprias | ❌ | nota coletiva (demais) |
| 46 | **yin-yang path** | 7 | **criado e fracassado** | ❌ | nota coletiva (demais) |
| 47 | **shadow path** | 7 | ramo do escuro + da luz | ❌ | nota coletiva (demais) |
| 48 | **enchantment path** | 7 | menor (ramo da emoção) | ❌ | nota coletiva (demais) |
| 49 | **thunder path** | 4 | variante nominal de *lightning* | ❌ | nota coletiva (elementais) |
| 50 | **illusion path** | 2 | menor | ❌ | nota coletiva (demais) |
| 51 | **seal path** | 1 | só nomeado | ❌ | nota coletiva (demais) |

**Total: 51 caminhos de cultivo nomeados pela obra.** A pasta cobria 17 — **um terço**.

### Falsos positivos descartados (com justificativa)

| Expressão | Ocorr. | O que é de verdade |
|---|---:|---|
| **righteous path** | 1745 | **Posição moral, não caminho de cultivo.** É o "lado justo" — clãs e seitas ortodoxos, "righteous path allied forces", "righteous path inheritances", "the righteous path fell while the demonic path surged". Um imortal do lado justo pode cultivar qualquer caminho. |
| **demonic path** | 1081 | O oposto moral do anterior: o "lado demoníaco". "Righteous path inheritances were usually not dangerous, **demonic path** was the one with vicious set-ups and schemes" — descreve ética de herança, não tema de leis. |
| **underworld path** | 3 | Nome próprio de um Gu — a **Underworld Path Butterfly**, borboleta rastreadora de um clã. Não existe caminho do submundo. |
| **golden path** | 6 | Uma **estrada dourada** literal, aberta como via de fuga por uma organização. |
| **dao mark path** | 4 | A "estrada de marcas do dao" que um cultivador escolhe — metáfora, não caminho nomeado. Ainda assim rende regra do mundo: "*este caminho de marcas vai ficando mais estreito; há muitas escolhas no começo, e quanto mais fundo você vai, menos escolhas você tem*". |
| the/a/his/her/their/this/that/each/every/one/other/same/own path | ~600 | Uso comum de "caminho" em inglês. |
| main / specialty / secondary / mainstream / minor / cultivation / immortal / advancement path | ~110 | Termos **estruturais** do sistema (caminho principal, de especialidade, secundário, mainstream, menor) — importantes, mas não nomes de caminhos. |
| left / right / correct / wrong / true / proper / narrow / wide / hidden / tunnel / mountain path | ~90 | Caminhos físicos ou figurados de estrada. |


---

## Lacunas encontradas

Ordenadas por severidade. "Evidência" traz sempre o capítulo verificado no texto-fonte.

### 🔴 BLOQUEADORAS

**L1 — Dois terços dos caminhos da obra não tinham cobertura alguma.**
A pasta cobria 17 de 51 caminhos nomeados. Ficavam de fora, entre outros, **os dois caminhos com
mais massa textual depois dos já cobertos** (*information path*, 733 ocorrências; *human path*, 663)
e **o caminho que dominou a história inteira do mundo** (*qi path*, 625 — "oito em cada dez Mestres
Gu trilhavam o caminho do qi", cap. 315). Também faltavam *formation path* (cap. 1323: "talvez o
caminho **mais complicado** de todos") e *theft path*, o caminho cujo golpe de assinatura **faz o
golpe do inimigo falhar no meio da ativação** — mecânica que o próprio catálogo de golpes do vault
já descrevia sem ter nota que a explicasse.
**Corrigido:** dez notas novas (ver seção "Notas novas criadas").

**L2 — A enumeração canônica do cap. 1323 estava citada e não aproveitada.**
A `01 - Visão Geral dos Paths.md` listava o cap. 1323 em `fontes`, mas a nota **não continha** nem a
cronologia de criação por era, nem a distinção mainstream × menor, nem a informação de que o
fundador do caminho das formações **é canonicamente não verificável**. Era o achado estrutural mais
importante do domínio, perdido dentro de um campo de metadados.
**Corrigido:** nova seção "Quantos caminhos existem, e quando cada um nasceu", com tabela por era.

**L3 — Erro factual: "só dois caminhos deixam significado verdadeiro".**
Afirmado em **quatro lugares** (`01` regra 12, `12 - Wisdom Path`, `16 - Rule Path`, e por
implicação em `17 - Heaven Path`). O texto diz outra coisa (cap. 2028):

> *To leave behind true meaning, wisdom path and rule path had **the greatest ease**. As for other
> paths, they had to **reach a certain level of mimicking these paths** to leave their true meaning
> behind. For example, **Long Hair Ancestor's refinement path true meaning** or Reckless Savage's
> transformation path true meaning.*

"Maior facilidade" ≠ exclusividade. E a ressalva que a `16 - Rule Path` usava para se salvar ("as
únicas exceções sendo os dez Veneráveis") **também é falsa**: o ancestral citado é um imortal rank 8
que não é um dos dez (cap. 1448, 1560). A obra registra significados verdadeiros de **força,
transformação, refino, regra, formação, sorte, fantasma e humano**.
**Corrigido** nos quatro lugares, com o erro anterior declarado em callout `[!warning]` para que a
leitora saiba que houve mudança.

**L4 — A árvore de derivação de sub-caminhos não existia em lugar nenhum.**
O cap. 1787 é uma passagem-mãe e estava inexplorada:
> *Because rule path was a huge concept, it had many branching smaller paths as a result. (…) rule
> path had many smaller paths derived from it, it was truly **the number one path** without question
> in this regard. The more famous ones were **restriction path and phantom path**.* (…) *It was like
> the **emotion path derived from wisdom path**.*

Com a consequência mecânica decisiva (cap. 1869): *advancing phantom path attainment level was
**essentially still rule path true meaning***. E (cap. 1340): *there are **no enchantment emotion
path dao marks in this world, only wisdom path dao marks***.
**Corrigido:** árvore completa em `29 - Os Demais Caminhos`, resumo e "teste do caminho real" na
`01`, seções novas em `12 - Wisdom Path` e `16 - Rule Path`.

### 🟠 SÉRIAS

**L5 — A tabela canônica de caminho principal + especialidade dos Veneráveis não estava na pasta.**
A `01` explicava a *arquitetura* sem dar os *pares*, que a obra enumera (caps. 2203 e 2204):
sabedoria+estrela, madeira+pintura, roubo+espaço, sorte+sangue, terra+céu, transformação+força.
**Corrigido:** tabela acrescentada à `01`. Note o achado colateral: **um dos dez tinha o caminho do
céu como especialidade**, o que precisa ser lido junto com a regra de que nenhum o cultivou "de
verdade".

**L6 — O caminho do céu era apresentado sem o fato que o define.**
Cap. 2028: *"Because **nobody can cultivate heaven path**"… No Gu Immortal could cultivate heaven
path, therefore, **heaven path true meaning had never existed!**"* — e nem a maior instituição do
mundo jamais viu um. A `17 - Heaven Path` já dizia "não existe significado verdadeiro", mas **sem a
razão nem a fonte**, o que a deixava parecendo asserção nossa.
**Corrigido** com a citação e a implicação (reinos de sonho do caminho só mantêm uma *conexão* com
esse significado ausente; e nele a vontade do céu e o significado verdadeiro estão *entrelaçados*).

**L7 — A nota de rodapé sobre "caminhos não cobertos" estava factualmente errada.**
Ela dizia que fogo, água, gelo, metal "existem no mundo, mas o material disponível não sustenta uma
nota". São **caminhos principais canônicos** do cap. 1323, o fogo é o mais antigo dos elementais
(mesma era do refino), a água tem **criador nomeado** (cap. 1226) e a madeira foi criada por um
Venerável. Havia material de sobra — 1.180 linhas de brief, 350 citações.
**Corrigido:** rodapé reescrito, apontando para a nota coletiva nova.

**L8 — A pergunta "existe ciclo de cinco elementos?" nunca fora respondida.**
Nenhuma nota da pasta a levantava, e é a primeira pergunta que uma designer faz. Verificado por
busca direta no texto-fonte: **não existe**. Não há enunciado do ciclo de geração/destruição em
lugar nenhum. O que existe é **densidade de marcas do Dao**, e ela é **recíproca**: marcas de fogo
no corpo enfraquecem Gu de terra (cap. 721), **e** marcas de terra mais densas restringem o fogo
(caps. 2140, 2312). Exceções honestas: fogo subjuga madeira (caps. 595, 802) e água × fogo se opõem
(caps. 1324, 1328).
**Corrigido:** seção dedicada em `27 - Os Caminhos Elementais`, com o veredito e as exceções.

**L9 — Gelo e neve estavam implicitamente tratados como dois caminhos.**
A obra escreve "**ice and snow path**" como unidade única, inclusive no cap. 1323, conta as marcas
como um tipo só (caps. 1091, 1146, 1161) e é explícita (cap. 874): *snow path and ice path were
**twins, almost indistinguishable***, a ponto de um Gu Imortal de gelo ser adequado a um praticante
de neve **sem a penalidade de marcas conflitantes**.
**Corrigido:** verbete único com aviso destacado.

**L10 — "Caminho das trevas" e "caminho demoníaco" eram confundíveis, e a pasta não avisava.**
São eixos diferentes: um é caminho elemental, o outro é **posição moral** (1.745 ocorrências de
*righteous path* e 1.081 de *demonic path* no texto — as duas expressões mais frequentes da busca,
e nenhuma das duas é caminho de cultivo).
**Corrigido:** callout `[!warning]` no verbete das trevas e tabela de falsos positivos em
`29 - Os Demais Caminhos`.

### 🟡 MENORES

**L11 — Caminho da espada sem o irmão de raiz.** Cap. 1563: *edge Gu was the origin of both **blade
path and sword path***; e cap. 1865 traz a profecia de um caminho futuro que **englobaria os dois**.
**Corrigido** com seção nova em `09 - Sword Path`.

**L12 — Sabedoria sem a formulação dos três elementos.** Cap. 1649: *wisdom path had three elements
of **thoughts, wills, and emotions***. A nota tinha a escada (pensamento → vontade → emoção) sem a
frase que a nomeia como a estrutura do caminho, e sem a consequência (o caminho da emoção é o
terceiro elemento destacado).
**Corrigido.**

**L13 — Relação caminho × attainment dispersa.** A regra do cap. 1787 — *when **any** path reaches
great grandmaster in attainment level, a qualitative change would occur* — confirmava a regra 13 da
`01` mas não estava citada; e os efeitos por degrau **por caminho** não estavam tabelados em lugar
nenhum. As notas novas de formação, elementais, roubo, fantasma, humano e informação trazem essa
tabela.

**L14 — Custo de trocar de caminho: já estava bem coberto.** A `02 - Como se Escolhe um Caminho`
trata o assunto com profundidade (seção "Dá para mudar depois?"). **Nada a corrigir** — registro
aqui porque era item explícito da auditoria. Complementos acrescentados nas notas novas: um clã
inteiro cogitando trocar de caminho por ter ganho um domínio recluso (`20 - Qi Path`) e um imortal
planejando trocar o Gu vital para pintura (`28 - Painting Path`).

**L15 — Cultivo duplo: coberto, mas sem os números.** A `02` cobre bem. Acrescentei os dados que
faltavam: *almost all Gu Immortals only had **one immortal aperture***, e o Gu usado na ascensão é o
que decide o caminho principal (cap. 1080); *it was **not that rare** for Gu Immortals to cultivate
two paths* — o raro é ser **bom nos dois** (cap. 1901); e a lista de efeitos concretos de marcas
conflitantes (cura pior, Gu de outro caminho rendendo menos, cooperação entre imortais piorando,
acúmulo travado — caps. 1097, 1273, 2140). Esses dados entraram nas notas novas, sobretudo em
`27 - Os Caminhos Elementais`, regras 4 e 7.

**L16 — Links quebrados alheios (não são meus, registro para o orquestrador).** A auditoria de links
aponta 32 quebrados, **nenhum vindo de `03 - Paths/`**. Todos partem de
`08 - Eventos e Cenarios/01 - Visão Geral dos Eventos.md` (29 deles, apontando para notas ainda não
criadas), de `09 - Estudos de Caso Mecanicos/` (2) e de `04 - Mundo/` (1). Provavelmente são notas em
produção por outro agente.

---

## O que foi corrigido — arquivo por arquivo

### `01 - Visão Geral dos Paths.md`
- **Regra 12 reescrita** (erro L3): "só dois caminhos" → "dois caminhos com muito mais facilidade,
  e os outros mediante imitação".
- **Seção nova "Quantos caminhos existem, e quando cada um nasceu"**: tabela de criação por era
  (cap. 1323), com aviso de que **não existe lista fechada** e de que a obra chega a ~50 nomes.
- **Subseção nova "Caminhos principais e caminhos menores"** — a distinção canônica.
- **Subseção nova "Caminhos brotam de outros caminhos"**, com o **teste do caminho real** ("este
  caminho tem marcas do Dao próprias?") em callout `[!important]`.
- **Subseção nova "Significado verdadeiro: quem consegue deixar um"**, com a citação do cap. 2028 e
  o caso do caminho do céu em `[!warning]`.
- **Tabela dos seis pares principal+especialidade dos Veneráveis** (caps. 2203-2204), com as duas
  ressalvas (o sigilo é ideal, não fato; e a especialidade "céu" de um deles).
- **Mapa da pasta atualizado** de 17 para 25 notas próprias + 2 coletivas, reagrupado por função.
- **"O que só o mestre sabe"**: três itens novos — o caminho da matança abortado, a ausência de
  significado verdadeiro do céu, o caminho fundado que fracassou, e a existência de caminhos sem
  marcas próprias.
- **Nota de rodapé sobre elementais reescrita** (erro L7).
- `fontes` ampliado com 10 capítulos.

### `16 - Rule Path.md`
- Seção "Significado verdadeiro" **reescrita** com a formulação correta, mais as duas vantagens
  extras do caminho (extrair e **criar** o próprio significado verdadeiro) e um `[!warning]`
  declarando o erro anterior.
- **Seção nova "Os caminhos que brotaram deste"** — a passagem do cap. 1787 que faz deste "o caminho
  número um" em gerar ramos, os dois ramos nomeados, e o gancho de design da "progressão escondida".
- Relações e `fontes` atualizados.

### `12 - Wisdom Path.md`
- Frase canônica dos **três elementos** acrescentada.
- **Seção nova "O ramo que brotou daqui: o caminho da emoção"**, com a citação do cap. 1340 (o
  caminho da emoção **não tem marcas próprias**).
- Correção do link sobre significado verdadeiro; remoção de uma frase agora redundante; correção da
  remissão ao caminho do fogo (que agora tem verbete).
- Relações e `fontes` atualizados.

### `17 - Heaven Path.md`
- Bullet "Impossibilidade de herança" **expandido** com a citação do cap. 2028, a razão declarada e
  o comportamento dos reinos de sonho do caminho. `fontes` atualizado.

### `09 - Sword Path.md`
- **Seção nova "Um irmão de sangue: o caminho da lâmina"** (cap. 1563) e `[!question]` com a
  profecia do caminho-guarda-chuva das armas (cap. 1865). Relações e `fontes` atualizados.

### `04 - Strength Path.md`
- Duas linhas novas na tabela de Gu (Puxar Água imortal e mortal).
- **Callout `[!example]` novo** com as duas regras do cap. 1248 (repassadas pelo orquestrador e
  verificadas por mim no texto): (1) ter a versão imortal **não dispensa** a mortal, porque um Gu
  Imortal é único e não serve a dois golpes ao mesmo tempo; (2) **o domínio que destranca a receita
  de um Gu híbrido é o do caminho secundário**, não o do principal — um grão-mestre da força não
  conseguia deduzir a receita, e só a grão-mestria na **água** a destrancou.
- Relações e `fontes` atualizados.

### `02 - Como se Escolhe um Caminho.md`
- Uma remissão desatualizada ("o mapa dos dezessete caminhos") corrigida. Nada mais: a nota já
  cobria bem o custo de troca de caminho e o cultivo duplo.

### Cross-links acrescentados (12 notas)
`03 - Blood`, `05 - Transformation`, `06 - Enslavement`, `07 - Refinement`, `08 - Poison`,
`10 - Soul`, `11 - Space`, `13 - Time`, `14 - Star`, `15 - Food`, `18 - Luck`, `19 - Dream` —
todas ganharam entradas em "Relações" apontando para as notas novas, sempre com **uma frase que diz
por que** a relação importa (e não só o link).

---

## Notas novas criadas

Todas seguem o gabarito exato das 17 existentes (frontmatter · "Em uma frase" · Filosofia e
identidade · Mecânicas típicas · Gu representativos com o callout de legenda · Em combate e fora
dele · Sinergias e fraquezas · `[!note] Para o design` fechando com **"Arquétipo entregue"** ·
Praticantes notáveis sem enredo · Relações). Todas declaram os quatro estados de confiabilidade no
cabeçalho e **nenhuma contém um único `*`** — são cem por cento canônicas ou dedução declarada.

| Arquivo criado | Tamanho | **Posição de leitura sugerida** | Por que ali |
|---|---:|---|---|
| `20 - Qi Path.md` | 17 KB | **depois de `04 - Strength Path`** | É o caminho que a força substituiu; a `01` já apresenta os dois como par histórico, e ler qi logo depois de força fecha a narrativa "o que reinou e morreu → o que o substituiu e já cai" |
| `21 - Formation Path.md` | 21 KB | depois de `07 - Refinement Path` | É o outro grande caminho de infraestrutura e disputa terreno com o refino |
| `22 - Information Path.md` | 26 KB | depois de `12 - Wisdom Path` | A obra os chama de "os mais compatíveis"; um busca, o outro deduz |
| `23 - Human Path.md` | 24 KB | **imediatamente antes de `17 - Heaven Path`** | O caminho humano só faz sentido lido contra o do céu; a ordem certa é humano → céu |
| `24 - Theft Path.md` | 21 KB | depois de `11 - Space Path` | O espaço é a defesa canônica contra o roubo e era o caminho de especialidade do fundador dele |
| `25 - Sound Path.md` | 20 KB | depois de `10 - Soul Path` | A canção-assinatura do caminho é composta de som, alma, sabedoria e escravização |
| `26 - Phantom Path.md` | 19 KB | **imediatamente depois de `16 - Rule Path`** | É ramo formal da regra, e a nota só se entende depois de ler a mãe |
| `27 - Os Caminhos Elementais.md` | 40 KB | **penúltima da pasta** | Coletiva; funciona como apêndice temático dos doze caminhos naturais |
| `28 - Painting Path.md` | 12 KB | depois de `27` | Curta e secreta; lê-se bem depois dos elementais, já que seu criador é o do caminho da madeira |
| `29 - Os Demais Caminhos.md` | 24 KB | **última da pasta** | É o inventário de fechamento: os menores, os ramos, o que fracassou, o que nunca nasceu e os falsos positivos |

**Ordem de leitura completa proposta para a pasta** (para o script de renumeração):

```
01 - Visão Geral dos Paths
02 - Como se Escolhe um Caminho
03 - Blood Path
04 - Strength Path
05 - Qi Path                 (novo — era 20)
06 - Transformation Path
07 - Enslavement Path
08 - Refinement Path
09 - Formation Path          (novo — era 21)
10 - Poison Path
11 - Sword Path
12 - Soul Path
13 - Sound Path              (novo — era 25)
14 - Space Path
15 - Theft Path              (novo — era 24)
16 - Wisdom Path
17 - Information Path        (novo — era 22)
18 - Time Path
19 - Star Path
20 - Food Path
21 - Rule Path
22 - Phantom Path            (novo — era 26)
23 - Luck Path
24 - Human Path              (novo — era 23)
25 - Heaven Path
26 - Dream Path
27 - Os Caminhos Elementais  (novo)
28 - Painting Path           (novo)
29 - Os Demais Caminhos      (novo)
```

A lógica da ordem: os dois primeiros são a porta de entrada; depois vêm os caminhos **de corpo e
combate**, os **de mente e alma**, os **fundamentais e abstratos** (com cada ramo colado à sua mãe:
fantasma depois de regra, humano antes de céu), e por fim as duas notas **coletivas** como apêndice.
Se o orquestrador preferir manter a ordem atual e apenas anexar as novas ao fim, nada quebra — mas
a barra lateral deixa de ser o currículo.

---

## Decisões tomadas

**D1 — Nota própria × verbete coletivo.** Critério aplicado: um caminho ganha nota própria se tem
**(a) mecânica própria descrita**, **(b) Gu ou golpes nomeados**, **(c) praticantes com feitos
mecânicos** e **(d) um preço estrutural declarado**. Sete caminhos passaram nos quatro critérios
(qi, formação, informação, humano, roubo, som, fantasma); a pintura passou em três com folga
(mecânica singularíssima, três golpes nomeados, criador e preço) e ganhou nota própria por ser
**conceitualmente única** — é a única escola do mundo que não sofre conflito de marcas.
**Descartado:** dar nota própria a *bone path* e *blade path*, que passariam em (b) e (c) mas falham
em (a) — nenhum dos dois tem mecânica própria descrita além de "corta" e "é feito de osso". Ficaram
como verbetes longos em `29`.

**D2 — Os doze elementais numa nota só.** Alternativa descartada: doze notas curtas. Três razões,
todas textuais: a obra os cria **em bloco** na mesma passagem; os agrupa numa mesma **categoria de
refino** (cap. 757: "os cinco elementos, a luz ou as trevas"); e lhes dá a **mesma fraqueza
estrutural** (cap. 1081: corpo frágil, sem métodos defensivos). Doze notas repetiriam essa moldura
doze vezes e esconderiam o que há de comum. Cada um tem verbete próprio dentro dela, com "o que a
obra não diz" explícito.
**Risco assumido:** a nota ficou grande (40 KB). Mitigado com sumário por regras no topo e verbetes
independentes.

**D3 — Gelo e neve como um caminho.** Decisão contra a intuição da leitora, tomada por evidência
(cap. 874, "gêmeos quase indistinguíveis" + Gu de um funcionando nas mãos do outro **sem penalidade
de marcas**). Registrado em callout para que a designer possa discordar sabendo por quê.

**D4 — Fantasma com nota própria apesar de ser "caminho menor".** Ele tem duas profundidades
supremas, um subsistema institucional inteiro (a abertura fantasma) e um monopólio técnico no refino.
"Menor" na obra significa pouco praticado, não pouco importante.

**D5 — Caminho da matança e caminho do yin-yang tratados como casos especiais, não como caminhos.**
Um **nunca foi criado** (a tentativa falhou e produziu o caminho da alma); o outro **foi criado e
não pegou**. Colocá-los na lista normal daria a impressão falsa de que são escolas cultiváveis.
Ficaram numa seção própria em `29`, sinalizada.

**D6 — Não corrigi a `02 - Como se Escolhe um Caminho` além de uma remissão.** Ela já cobria bem os
itens 4 e 2 da auditoria (custo de troca, cultivo duplo), e reescrever seria sobreposição. Os dados
novos que encontrei sobre o assunto foram para as notas novas, onde encaixam sem duplicar.

**D7 — Marquei o erro corrigido em vez de apagá-lo.** Nos três lugares onde a pasta afirmava algo
falso (significado verdadeiro, rodapé dos elementais), deixei um callout dizendo **que havia um erro
e qual era**. Motivo: a designer pode ter lido a versão anterior, e uma correção silenciosa a
deixaria com duas verdades incompatíveis na cabeça. É o padrão que a própria pasta já usava (ver o
callout do "pseudo-Venerável" na `01`).

**D8 — Nenhum `*` em nenhuma das dez notas novas.** Havia muito espaço para inventar (o caminho da
pintura não tem **um Gu nomeado sequer**), e escolhi **declarar o vazio** em vez de preenchê-lo,
sinalizando à designer que aquele é o maior orçamento de liberdade da pasta. Cada nota tem uma seção
"O que a obra não diz".

**D9 — O que fiz com a mensagem do orquestrador sobre o cap. 1248.** A regra "um Gu Imortal não
dispensa a versão mortal" interessa a `02 - Gu/12 - Gu Imortais.md` e `02 - Gu/07 - Killer Moves.md`,
que **não são meus arquivos** — não os toquei. Verifiquei a passagem no texto-fonte e aproveitei a
**parte que é do meu domínio**: o *pulling water Gu* é do caminho da força **e** do caminho da água,
e a obra usa esse par para estabelecer uma segunda regra que o orquestrador não mencionou e que é a
mais interessante para a pasta de caminhos — *ainda que ele fosse um **grão-mestre do caminho da
força**, ele não conseguia deduzir a receita do Puxar Água mortal; só quando seu domínio no
**caminho da água** chegou a grão-mestre* é que ele passou a detalhá-la instintivamente.
==**O domínio que destranca um Gu híbrido é o do caminho secundário, não o do principal.**== Está em
`04 - Strength Path`. A parte sobre unicidade de Gu Imortais fica pendente para quem cuida de
`02 - Gu/`.

---

## O que a obra realmente não diz

Consolidado das dez notas novas — este é o **orçamento de liberdade** da designer.

**Lacunas de fundação (o mundo não sabe):**
- **Quem criou o caminho das formações.** A obra afirma explicitamente que *seu verdadeiro fundador
  **não pôde ser verificado*** (cap. 1323). É lacuna **canônica**, não omissão nossa — e um gancho de
  campanha pronto.
- **Quem criou** os caminhos da informação, do som, do fogo, da terra, do metal, do gelo-e-neve, do
  relâmpago, do vento, da luz, das trevas, da nuvem, do osso, da lâmina, da lua, da sombra, da
  ilusão, do selo e da restrição.
- **Não existe lista fechada de caminhos.** A obra enumera os principais e diz que omite os menores
  "por ora".

**Lacunas de doutrina:**
- **Significado verdadeiro / essência não enunciados** para: qi, informação, som, roubo, humano
  (a obra confirma que existe e foi obtido, mas nunca o formula), fantasma (idem, e ainda diz que no
  fundo é o da regra), e nove dos doze elementais.
- **O mecanismo interno do caminho da regra** — a lacuna teórica mais antiga da pasta, já registrada
  antes desta auditoria e confirmada por ela.
- **O que o degrau de supremo grão-mestre destranca** em formação, e o que **grão-mestre** destranca
  no roubo.

**Lacunas de catálogo:**
- **O caminho da pintura não tem um único Gu nomeado.** É o maior espaço em branco da pasta, e é
  consequência direta do segredo do criador.
- **O caminho fantasma não tem um único golpe assassino nomeado** — não existe ali o equivalente a
  "mão sem forma".
- **Não existe Gu Imortal de nível 9 conhecido do caminho do qi** — a obra afirma isso em tom de
  lamento e especula que talvez haja um no tesouro pessoal do fundador.
- **Quatro das nove canções** do caminho do som não são nomeadas, e a obra confirma que sete foram
  criadas.
- **O caminho das formações não tem catálogo de Gu temáticos** — só quatro ferramentas de
  meta-nível. **Isso é o desenho do caminho, não uma falha:** o conteúdo temático vem emprestado.
- **A maioria dos Gu do caminho humano é classificada e não descrita.**

**Lacunas de regra:**
- **Não existe ciclo de cinco elementos.** Verificado por busca direta no texto-fonte.
- **Se o vácuo detém o som** — nenhuma passagem trata o som como precisando de meio material.
- **Se existem Gu Imortais selvagens de caminho humano.** A pergunta é feita **textualmente pela
  própria obra** e fica sem resposta.
- **A causa do declínio do caminho fantasma**, depois de ele ter florescido na antiguidade.
- **Fraqueza estrutural declarada** dos caminhos da terra, do vento e da nuvem — as notas as marcam
  como dedução nossa.
- **Se o caminho das armas criado no fim da obra é a realização da profecia** do caminho que
  englobaria espada e lâmina.

**Uma divergência interna que a obra não reconcilia:**
- O **caminho fantasma** é datado da Antiguidade Tardia (cap. 1323), mas a obra também menciona uma
  herança dele *da Era Imemorial* (cap. 364) e outra *"antiga"* (cap. 395). Registramos a dúvida em
  vez de escolher.

---

## Método e rastreabilidade

- **Varredura do texto-fonte:** `grep -hioE "\b[a-z]+ path\b"` e a variante de duas palavras nos seis
  volumes, deduplicado e contado. Todos os candidatos com ≥3 ocorrências tiveram o **contexto lido**
  antes de serem aceitos ou descartados.
- **Dumps de trabalho** (linhas-parágrafo por caminho) e **briefs de pesquisa** com citação
  obrigatória de capítulo ficaram em
  `…/scratchpad/paths/` — cinco briefs somando cerca de **4.500 linhas** e mais de **1.100 citações
  de capítulo**, todas com o mapeamento linha→capítulo feito pelo cabeçalho `## Chapter N`.
- **Nenhuma negativa foi afirmada sem grep no texto-fonte.** As três negativas fortes desta auditoria
  — não existe ciclo de cinco elementos, não existe significado verdadeiro do caminho do céu, não
  existe criador nomeado do caminho das formações — foram verificadas diretamente na obra, e as duas
  últimas são **afirmadas pela própria obra**, não inferidas de ausência.
- **Auditoria de links:** `_pipeline/auditar-links.py` roda limpo para `03 - Paths/` — **zero links
  quebrados** partindo desta pasta, e zero links dependendo só de alias.
