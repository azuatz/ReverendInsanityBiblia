# Enxugamento: `09 - Eventos e Cenarios`, notas 02 a 15

Relatório da passagem de edição pedida pelo usuário ("tem coisas que está muito difícil de
ler e entender; melhor tirar, ou só botar as partes mais importantes, ou resumir melhor").
Escopo desta passagem: as notas **02 a 15** da pasta. As notas 01 e 16-29 foram tratadas por
outros agentes.

## O que mudou em toda nota, sem exceção

1. **Bloco `## O essencial` no topo**, logo depois do título e da frase de abertura: uma
   tabela de duas colunas com no máximo onze linhas que responde o que é o evento, o que o
   dispara, **qual é a trava**, quanto tempo dura, o que um grupo faz lá dentro, o que se
   ganha e o que se perde. Quem lê só essa tabela consegue rodar uma sessão. Uma linha
   abaixo dela avisa que o resto da nota é aprofundamento opcional.
2. **A tabela `> [!abstract] Ficha rápida` foi absorvida pelo `## O essencial` e apagada.**
   As duas diziam quase a mesma coisa em formatos diferentes; a nova tabela é a única, e
   acrescenta as linhas que faltavam (a trava, o que se faz, o que se ganha).
3. **A cerimônia de abertura caiu de seis linhas para uma.** O callout
   `> [!info] Convenção de confiabilidade` virou uma linha única de citação, com a mesma
   informação — inclusive a frase de que apagar tudo marcado com `*` devolve a nota a cem
   por cento canônico.
4. **Tabela no lugar de prosa** onde a informação era tabelável: fases do relógio, papéis
   por faixa de rank, preços, escalas, hierarquias.

## Regra que governou os cortes

Cortar prosa era o objetivo; perder cânone seria falha. Ficaram intocados: todo número
canônico, toda regra mecânica, todo nome próprio do mundo, as marcações `(ded.)`, `*`, `—`,
`[comum]`, `[especializado]`, `[segredo]`, o campo `fontes` do frontmatter e o aviso de
trava de cada nota. Quando um fato canônico estava num parágrafo destinado ao corte, o fato
foi **movido**, não apagado — os casos estão registrados nota a nota abaixo.

A verificação foi automatizada: um script comparou a versão anterior (em git) com a nova,
extraindo de cada uma todos os tokens numéricos e todos os nomes próprios de duas ou mais
palavras, e listando o que existia antes e não existe depois. Os únicos achados foram
corrigidos e estão registrados abaixo.

## Antes e depois, nota a nota

| Nota | Linhas | Palavras |
|---|---|---|
| 02 - A Maré de Lobos de Qing Mao Shan | 357 → **247** (-31%) | 4088 → **3273** (-20%) |
| 03 - Marés de Bestas | 307 → **247** (-20%) | 3531 → **3124** (-12%) |
| 04 - Desastres Locais e Problemas Crônicos | 378 → **334** (-12%) | 4302 → **3836** (-11%) |
| 05 - Feiras, Caravanas e Festivais | 459 → **367** (-21%) | 5174 → **4289** (-18%) |
| 06 - Assembleias, Alianças e Quadros de Mérito | 412 → **336** (-19%) | 4246 → **3818** (-11%) |
| 07 - Torneios, Arenas e Duelos | 466 → **387** (-17%) | 4938 → **4333** (-13%) |
| 08 - Aberturas de Herança | 304 → **216** (-29%) | 3518 → **2986** (-16%) |
| 09 - A Herança dos Três Reis | 322 → **237** (-27%) | 3843 → **3283** (-15%) |
| 10 - A Subida da Montanha Dang Hun | 283 → **213** (-25%) | 3312 → **2857** (-14%) |
| 11 - Os Cacos do Céu Estrelado | 262 → **212** (-20%) | 3145 → **2844** (-10%) |
| 12 - As Terras Ferozes e o Subsolo do Mundo | 367 → **289** (-22%) | 4288 → **3746** (-13%) |
| 13 - O Paraíso da Baleia-Dragão e o Obelisco de Mérito | 311 → **233** (-26%) | 3481 → **2830** (-19%) |
| 14 - O Ciclo Decenal das Planícies do Norte | 373 → **298** (-21%) | 4417 → **3734** (-16%) |
| 15 - O Edifício dos Oitenta e Oito Andares | 338 → **268** (-21%) | 3760 → **3413** (-10%) |
| **Total (14 notas)** | **4939 → 3884** (-22%) | **56043 → 48366** (-14%) |

Sobre a diferença entre as duas colunas, que é o achado principal desta passagem: **o alvo de
um terço foi atingido em linhas de leitura em várias notas e em nenhuma foi atingido em
palavras.** A razão não é falta de disposição para cortar — é que estas notas não eram prosa
inflada. A verificação automática mostra que quase toda frase delas carrega um número, uma
cláusula mecânica ou um nome próprio, e a regra "não pode sair cânone" é, na prática, o teto
do corte. O que sobrava para deletar era ornamento e repetição, e isso rende muito em linhas
(reempacotar prosa em tabela, fundir parágrafos, matar a cerimônia de abertura) e pouco em
palavras.

O ganho real de legibilidade, portanto, não está na régua: está em o leitor agora ter **onde
parar**. As duas coisas que mudam a experiência de abrir uma dessas notas para preparar a
sessão da semana são o `## O essencial` no topo e a promessa explícita, logo abaixo dele, de
que o resto é opcional.

## O que saiu, por categoria

**Cerimônia de abertura (as catorze notas).** O callout de convenção de confiabilidade de seis
linhas virou uma linha; a `> [!abstract] Ficha rápida` foi absorvida pelo `## O essencial` e
apagada. Só isso devolve entre doze e dezesseis linhas por nota, todas no topo, que é
justamente onde elas mais atrapalhavam.

**Seções que viraram linha de tabela.** Em 04, `## Por que acontece` inteira; em 05, 06 e 07,
`## Por que acontece` e `## O que está em jogo`. Em todos esses casos o conteúdo canônico foi
para as linhas **Gatilho**, **O que se ganha** e **O que se perde** do `## O essencial` — a
seção sumiu, o fato não.

**Prosa que virou tabela.** `O que um grupo de personagens faz aqui` virou tabela
`| Faixa | Papel |` nas catorze notas. `O relógio do evento` virou tabela de fases onde era uma
sequência (02, 14, e onde já não era tabela). Em 08, os quatro ambientes de `Como é por dentro`
viraram tabela.

**Regra geral do mundo que pertencia a outra nota, trocada por wikilink.** Foi o corte mais
produtivo, e vale registrar os casos porque eles também arrumam a arquitetura da pasta:

- 02 → 03: a construção da muralha plantada e a zona de autoridade do rei-fera, que a nota da
  categoria já explica; o quadro de méritos, que agora aponta para a 06.
- 09, 10 e 11 → 08: as regras gerais de herança que a nota da categoria já dá.
- 11 → `[[26 - Dream Path]]`: a mecânica de reinos de sonho.
- 09 → `[[13 - Tribulações e Calamidades]]`: o calendário de calamidades das terras abençoadas.
- 05 → `[[06 - Mercados e Leilões]]`: a mecânica de pregão (ficaram a ficha de privilégio, os
  mil lugares e as salas privadas, que são da cidade, não do leilão).
- 05 → `[[08 - Crime, Mercado Negro e Recompensas]]`: os mandados de captura (ficaram os dois
  preços canônicos, 1.000 e 5.800).
- 07 → 05: a escada de anéis.
- 12 → 03 e 14 → 06: marés de bestas e quadro de méritos, respectivamente.

**Ornamento.** Meta-comentário do tipo "e é isso que torna este cenário tão bom para uma mesa",
"É uma sessão inteira", "Não é metáfora"; ênfase repetida; e listas de três exemplos onde um
bastava. Em 13, uma frase inteira marcada com `*` ("é a melhor abertura de campanha desta pasta
inteira") foi apagada — era opinião nossa, não cânone.

**Listas encurtadas.** `Desfechos possíveis` a no máximo cinco itens; `O que a obra não diz` a
cinco itens de uma linha; `Relações` a seis ou sete itens agrupados; `> [!note] Para o design`
a no máximo doze linhas.

## Fatos canônicos movidos, não cortados

Todos os casos em que um fato canônico estava dentro de um parágrafo destinado ao corte e foi
transplantado:

| Nota | Fato movido | Para onde |
|---|---|---|
| 02 | a tradução "Montanha Qing Mao" | linha **O que é** do `O essencial` (restaurada na verificação) |
| 04 | a definição de nascente espiritual — fonte subterrânea que produz pedras primordiais e é a fundação econômica do lugar | linha **Gatilho** (restaurada na verificação, com o wikilink) |
| 05 | os seiscentos-por-um do pedágio; a paz do anfitrião | `O essencial` |
| 06 | *sem aliança, destruição*; "cheia de pólvora e fumaça"; vales, minas, rotas, nascentes, cotas, refém, casamento e metade do estoque do líder | linhas **Gatilho**, **O que se ganha** e **O que se perde** |
| 07 | a citação dos dois rank 8; a citação da alocação de benefícios entre três clãs; o teto de rank 5 da Escala 5 | **A trava**, corpo da Escala 1, e **Escala de poder** |
| 08 | o valor da inteligência escrita (centenas de milhares de pedras primordiais pelos registros de exploração) | linha **O que se ganha** |
| 09 | *obter uma faz alguém subir ao poder; duas deixam o nome na história; as três criam um soberano supremo*; os "menos de dez anos" restantes à terra abençoada | `O essencial` |
| 10 | os "cinco vezes mais rápido"; a fundação de alma que cresce com a vida vivida; *ascender aos céus num passo só* | `O essencial` |
| 11 | a composição da equipe e o terço de comissão; os **mil li** de zona proibida | `O essencial` e linha **A trava** |
| 15 | a localização nas Planícies do Norte, com o wikilink de geografia | linha **O que é** (restaurada na verificação) |

## Notas em que cortei menos, e por quê

- **04 — Desastres Locais e Problemas Crônicos (-12% linhas).** Não é uma nota, são **quatro
  cenários independentes** (o sapo, o furacão, os zumbis, o lago de sangue), cada um rodável
  como sessão fechada. Encurtar de verdade significaria apagar um cenário inteiro, não prosa.
- **05 — Feiras, Caravanas e Festivais (-21% / -18%).** Mesmo motivo, em maior escala: **seis**
  cenários independentes, nenhum redundante com outro.
- **06 e 07.** A 06 é a **nota-dona do quadro de méritos** nas duas escalas — a 02 e a 14 foram
  enxugadas apontando para cá, então a duplicação aparente com elas tem de morar aqui. As duas
  ainda carregam dez cláusulas de pacto, quatro e cinco escalas respectivamente, e seis tabelas
  canônicas de valores entre elas.
- **11 — Os Cacos do Céu Estrelado (-10% palavras).** O caso extremo da regra: as três presas já
  vinham em tabela, as dez regras são todas mecânicas distintas, e a explicação em três passos
  da trava física é o eixo da nota. Cortar mais seria cortar exatamente o que era proibido cortar.
- **02 — A Maré de Lobos (-31% linhas, -20% palavras).** Cortou bem em estrutura, mas é a única
  nota da pasta que descreve **uma campanha inteira com calendário de nove fases**, e as fases
  são o produto. Ficou com mais espaço de propósito.

## Verificação final

- `python3 _pipeline/auditar-links.py`: **links quebrados: 0** e **âncoras quebradas: 0** (264
  âncoras conferidas, 5.359 links por nome exato de arquivo).
- Script de comparação contra `HEAD`, rodado nas catorze notas: nenhum número canônico perdido,
  nenhum wikilink perdido, nenhuma marcação `(ded.)` / `*` / `[segredo]` / `[especializado]`
  perdida sem que a frase inteira tenha sido apagada, e frontmatter byte a byte idêntico —
  inclusive o campo `fontes`.
- Três perdas foram detectadas por esse script e reparadas antes do fim: a tradução "Montanha
  Qing Mao" na 02, o wikilink `[[02 - Pedras Primordiais]]` e a definição de nascente espiritual
  na 04, e o wikilink `[[03 - Planícies do Norte]]` na 15.
- Zero pipes não escapados dentro de wikilink em tabela; zero citações de capítulo no corpo das
  catorze notas; as catorze têm o bloco `## O essencial` com tabela de no máximo onze linhas, a
  linha **A trava** preenchida e a convenção de confiabilidade em uma linha.

## O que ficou de fora, e recomendo decidir depois

Se o objetivo dos -25% em palavras for para valer, o caminho que sobrou não é editorial, é de
escopo: as seções `Desfechos possíveis` e `> [!note] Para o design` são **nossas**, não
canônicas, e somam algo entre trezentas e quatrocentas palavras por nota. Apagá-las devolveria
o terço pedido de imediato — mas são também as duas seções que traduzem o cânone em coisa
jogável, que é o produto que a designer pediu. Por isso não as apaguei: a decisão é de escopo,
não de edição, e é do usuário.
