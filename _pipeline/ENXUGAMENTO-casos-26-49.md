# Enxugamento — Estudos de Caso Mecânicos 26–49

Relatório do lote `26`–`49` de `10 - Estudos de Caso Mecanicos/`. Não foram tocados a
nota-índice `01` nem os casos `02`–`25`, com a única exceção documentada na seção
"Links corrigidos fora do lote".

## Resumo

- **24 notas → 22 notas** (duas fusões).
- **2.791 → 2.354 linhas**; **26.734 → 22.412 palavras**; **corte de 16%**.
- Toda nota agora abre com **a regra em uma frase, em negrito, antes de qualquer outra
  coisa** — inclusive antes da convenção de confiabilidade.
- Dez notas de escala imortal ganharam, no topo, uma linha dizendo que dá para pular.
- `auditar-links.py`: **0 links quebrados, 0 âncoras quebradas** (5.357 links, 264 âncoras).

## Linhas e palavras, nota por nota

| Nota | Linhas antes → depois | Palavras antes → depois | Corte |
|---|---|---|---|
| 26 | 143 → 119 | 1509 → 1155 | 23% |
| 27 | 123 → 102 | 1130 → 918 | 19% |
| 28 | 97 → 84 | 950 → 796 | 16% |
| 29 | 117 → 95 | 971 → 785 | 19% |
| 30 | 117 → 94 | 1034 → 869 | 16% |
| 31 | 101 → 90 | 957 → 844 | 12% |
| 32 | 111 → 103 | 1122 → 1003 | 11% |
| 33 | 109 → 95 | 977 → 848 | 13% |
| 34 | 134 → 105 | 1301 → 985 | 24% |
| 35 | 108 → 88 | 900 → 762 | 15% |
| 36 | 111 → 94 | 987 → 836 | 15% |
| 37 | 96 → 86 | 869 → 766 | 12% |
| 38 | 97 → 87 | 903 → 823 | 9% |
| 39+40 → **39** | 208 → 154 | 1876 → 1494 | 20% |
| 41 | 99 → 87 | 964 → 831 | 14% |
| 42 | 158 → 137 | 1561 → 1337 | 14% |
| 43 | 100 → 91 | 907 → 824 | 9% |
| 44 | 152 → 130 | 1681 → 1385 | 18% |
| 45 | 162 → 134 | 1879 → 1444 | 23% |
| 46 | 100 → 85 | 918 → 815 | 11% |
| 47+48 → **47** | 219 → 177 | 2046 → 1733 | 15% |
| 49 | 129 → 117 | 1292 → 1159 | 10% |
| **total** | **2791 → 2354** | **26734 → 22412** | **16%** |

### Por que 16% e não 25%

O alvo de um quarto foi atingido ou quase atingido onde havia gordura (26, 34, 45: 23–24%)
e não foi atingido nas notas que já eram enxutas (38, 43: 9%). O motivo é aritmético e
vale registrar para quem for enxugar outros lotes: numa nota média do lote, **cerca de
metade das palavras é conteúdo protegido** pelo próprio briefing — frontmatter com
`fontes`, a frase de regra, o veredito "exceção ou regra", o callout de design, o callout
de regra proposta, as tabelas de números canônicos e a lista de relações. Cortar 25% do
total significaria cortar metade de tudo o que sobra, e aí começam a cair números
canônicos. Onde o corte parou em 9–12%, é porque a nota já não tinha parágrafo redundante.

Onde o ganho de leitura foi maior do que o número sugere: a **ordem** mudou em todas as
notas (regra → situação → método → veredito, sem repetição entre as seções), e a leitora
não precisa mais atravessar quatro linhas de convenção antes de saber do que a nota trata.

## O que foi cortado, por categoria

**1. O bloco de convenção de confiabilidade (as 24 notas).** Eram quatro linhas idênticas
no topo de cada nota, antes da regra. Viraram **uma linha só**, e ela agora vem **depois**
da regra. Em **13 notas que não usam nenhum marcador** no corpo (`27, 28, 29, 31, 33, 34,
35, 36, 37, 41, 43, 46, 49`) o bloco foi **removido inteiro** — era exatamente o caso da
"seção que só existe porque o modelo previa e naquela nota está vazia de conteúdo": um
aviso sobre marcadores numa nota sem marcadores. Nas nove que usam `(ded.)`, `*` ou `—` a
linha permanece, como manda o CLAUDE.md.

**2. Definição de conceito que pertence a outra pasta → wikilink.** Os casos de escala
imortal explicavam, dentro de si, termos que têm nota própria. Trocados por wikilink com
texto alternativo:

- `34` — a escada completa de *jun* (30 / 70 / 100 por rank) e a definição longa de
  *fundação de alma* → `[[02 - Tabelas de Referência Rápida#15…]]` e `[[12 - Soul Path]]`.
  Os números canônicos que ficaram são os do próprio caso (800 jun, 1000 → 500 man soul,
  vinte anos de cultivo).
- `44` — a curva de dao marks continuou (é a chave de leitura da nota) mas passou de
  callout longo a dois períodos, apontando para `[[16 - Dao Marks]]`.
- `42` — o parágrafo que explicava o que é *attainment* → `[[08 - Attainment]]`; o callout
  de definição de *fundação* foi mantido, porque o índice da pasta declara esta nota como o
  lugar onde "fundação" é definida.
- `45` — o parágrafo de abertura que definia *abertura imortal* → `[[02 - Abertura]]`.
- `32` — a definição de *reino de sonho* e de *espírito guardião* → `[[49 - Explorar um
  Reino de Sonho]]` e `[[39 - O Espírito Guardião de um Território]]`.
- `27` — a definição de *espírito guardião* → wikilink para a nota 39.
- `49` — a definição longa de *man soul* encolheu para o mínimo que a tabela exige.

**3. Parágrafo que repetia outra seção da mesma nota.** Em `27` ("Por que isso importa"
repetia o veredito), `30` ("Por que tudo isso funciona"), `36` (o parágrafo final repetia a
seção do contraponto), `43` e `46` (o "Por que importa" repetia a regra de abertura). Em
todos, o conteúdo novo foi absorvido no parágrafo anterior e o título sumiu.

**4. Seção inteira que duplicava outra nota do vault.** Em `30`, a "Variante — a derrota
calculada" reproduzia o caso `19` com todos os detalhes; virou um parágrafo com o número
que interessa (três Gu de trunfo destruídos) mais o wikilink para `19`. A leitura
`(ded.)` sobre a reputação aumentada foi preservada com o marcador.

**5. Ornamento e ênfase repetida.** Frases do tipo "e é justamente por isso que",
"vale reparar", "duas coisas que a tabela sozinha não dá, e são importantes"; listas de três
adjetivos onde um bastava; e as aberturas de callout que anunciavam o que o callout ia
dizer. Presente em praticamente todas as notas.

**6. Citação longa reduzida ao trecho que carrega a regra.** Em `26`, `44`, `45` e `49`,
citações de três ou quatro linhas viraram a oração que continha o mecanismo. Nenhuma
citação foi eliminada por completo onde ela era a evidência da regra.

## Fatos canônicos movidos (nenhum perdido)

- `34` — a escada de força por rank (30/70/100 jun) saiu do corpo e permanece em
  `[[02 - Tabelas de Referência Rápida]]`, agora apontada por âncora de seção. O
  esclarecimento "este 800 não contradiz o 500 da tabela" foi mantido como callout, porque
  é uma reconciliação de dois números canônicos e não existe em outro lugar.
- `40` → `39` — as três vias, os custos de cada uma, a regra de que espíritos guardiões não
  podem mentir, o risco de dissolução do território e a ressalva de que a morte do dono
  anterior não a dispara: tudo migrado íntegro para a nota fundida.
- `48` → `47` — os 30% de reserva de energia por salva, as duas variantes (provação fora da
  região natal; provação dirigida ao inimigo), o ciclo de ressurreição como mortal completo
  e a ressalva `—` de que a obra não descreve o método de ressurreição: tudo migrado.
- `39` (original) → `39` (fundida) — a estimativa `*` do custo dos vinte conjuntos de
  materiais foi mantida com o marcador e com a justificativa de por que são vinte.
- `30` — as duzentas mil pedras primordiais, a comparação com o salvo-conduto oficial e o
  relato do espião ("utilizável, não vale a pena atacar") permaneceram; o que saiu foi a
  citação literal da "ponte sobre o abismo", cujo sentido está na frase que ficou.

## As duas fusões

### `39` + `40` → **`39 - O Espírito Guardião de um Território`**

**Por quê:** as duas notas tratavam do **mesmo ente** e do **mesmo mecanismo**. A `40`
descrevia a barreira de reconhecimento e as três maneiras de passar por ela; a `39`
descrevia o que se ganha quando o reconhecimento é obtido. Separadas, cada uma entregava
metade do guardião — e a `39` dependia da `40` para explicar por que existe reconhecimento.
Juntas viram uma nota com duas partes claramente rotuladas ("como se passa pela barreira" /
"o que o reconhecimento paga"), e a designer passa a ter o guardião inteiro num lugar só.

**Preservado:** os três vereditos das vias (enganar / suprimir / invadir-e-pedir), a tabela
assimétrica dos pedidos, o contraste histórico dos dois herdeiros, os **dois** callouts de
regra proposta (as duas travas; os pedidos a um guardião) e os dois callouts de design,
fundidos num só sem perda de conteúdo.

**Número liberado: `40`.**

### `47` + `48` → **`47 - A Tribulação Como Matéria-Prima`**

**Por quê:** as duas partiam da **mesma regra do mundo** — a provação não é punição
arbitrária, é o mundo redistribuindo energia, montada com o material do terreno. A `47`
explorava isso do ponto de vista de quem vai enfrentar a prova (configurar o terreno); a `48`
do ponto de vista de quem assiste (colher a energia). Como a segunda só faz sentido depois
de aceita a premissa da primeira, e a `48` repetia a premissa para poder usá-la, a fusão
elimina a repetição e torna a lógica visível: **configurável e colhível são a mesma
propriedade, vista dos dois lados**.

**Preservado:** o trade-off de densidade de energia, os ganhos de attainment medidos
(transformação → Mestre; voo Mestre → Quase Grão-Mestre; 8 ou 9 imortais em 10 são Mestres
de voo), o callout "O céu aprende", o custo de 30% de reserva por salva, as duas variantes
piores, o ciclo replantável com a ressalva `—`, e os **dois** callouts de regra proposta.

**Número liberado: `48`.**

### Fusões avaliadas e recusadas

- **`28` + `37`** (vantagem de custo por artefato × por fatiamento da produção) — recusada:
  as regras finais são diferentes (dumping de mercado × proteção de segredo por arquitetura),
  os vereditos também, e o par já se referencia mutuamente.
- **`41` + `43`** (conseguir um Gu Imortal sem poder para tanto) — recusada: a situação é
  parecida, mas as regras são distintas (a vaga verificada em tempo real × o artefato que
  se autodestrói nas mãos do ladrão) e cada uma tem a sua regra proposta.
- **`44` + `45`** (dois fracassos instrutivos) — recusada: o que elas têm em comum é o
  *gênero*, não a regra.
- **`46` + `49`** (uma produz a fundação de alma que a outra consome) — recusada: relação de
  cadeia produtiva, não de regra comum; resolvida com wikilink recíproco.

## Casos marcados como "só para quem já domina o cenário"

Linha em itálico no topo, logo abaixo da regra: *"Escala imortal: se você ainda está montando
o começo da campanha, pode pular esta nota sem culpa."*

`28`, `36`, `41`, `42`, `43`, `44`, `45`, `46`, `47`.

A nota `49` recebeu uma variante da linha, porque só a segunda metade dela é de escala
imortal: a primeira (o contraste entre os dois exploradores) serve a qualquer mesa.

Não foram marcadas `27` (a escala é imortal, mas o operador é um mortal de rank 4 — é
justamente esse o valor do caso para uma mesa), `39` e as notas de mercado e sociedade.

## Links corrigidos fora do lote

As duas fusões renomearam arquivos, e dois links apontavam para os nomes antigos a partir de
arquivos fora do meu lote. Ambos foram corrigidos, cirurgicamente, sem tocar em mais nada
desses arquivos:

- `10 - Estudos de Caso Mecanicos/16 - O Ambiente Manda Mais que o Rank.md` — o link para a
  antiga `39 - As Três Chances de um Espírito Guardião` passou a apontar para
  `39 - O Espírito Guardião de um Território`. **Atenção:** este arquivo é do lote `02`–`25`;
  se o agente daquele lote reescrever a nota inteira a partir de uma cópia anterior, o link
  volta a quebrar e precisa ser reaplicado.
- `00 - Somente o Mestre.md` — a linha que citava `47` e `48` juntas passou a citar a nota
  fundida `47 - A Tribulação Como Matéria-Prima`, com a descrição ajustada para dizer que
  ela cobre os dois lados.

A nota-índice `01` **não foi tocada** por mim; quando a auditoria final rodou, ela já
apontava para os dois novos nomes.

## Verificações finais

- `python3 _pipeline/auditar-links.py` → **0 links quebrados, 0 âncoras quebradas**
  (219 notas, 5.357 links por nome exato, 264 âncoras conferidas, 0 links dependentes só de
  alias).
- Todas as 22 notas abrem com `**A regra:** …` imediatamente após o título.
- Todas as 22 mantêm `fontes` no frontmatter, o callout `É exceção ou regra?`, o callout
  `> [!note] Para o design` e ao menos um `> [!example] Regra proposta` (as duas notas
  fundidas mantêm dois cada).
- Nenhuma citação de capítulo no corpo das notas (`cap. NN` só no frontmatter).
- Nenhum pipe não escapado dentro de wikilink em tabela.
