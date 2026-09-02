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

