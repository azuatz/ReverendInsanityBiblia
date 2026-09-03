# Enxugamento — `09 - Eventos e Cenarios`, nota-porta `01` e notas `16` a `29`

Escopo: a nota-porta `01` e as catorze notas de evento `16` a `29`. As notas `02` a `15` não foram
tocadas (outro agente cuidou delas na mesma leva).

Baseline de comparação: commit `8086bbc`, que era o `HEAD` no início desta sessão. **Aviso de
histórico:** durante o trabalho, outro agente rodou `git add -A && git commit` e levou junto as notas
`16`–`28` já reescritas — elas estão dentro dos commits `d7786fe`/`7bb326a`/`c3ba912`, cujas mensagens
não as mencionam. Nada se perdeu; só a autoria da mensagem ficou trocada.

## O que mudou em todas as catorze

1. **`## O essencial` no topo.** Cada nota abre, logo depois da frase de abertura, com um bloco de até
   quinze linhas: o que é o evento, o gatilho, **a trava**, a duração, o que um grupo faz lá dentro e o
   que se ganha. Quem ler só isso roda uma sessão decente; o resto está explicitamente marcado como
   aprofundamento.
2. **O bloco de convenção de confiabilidade virou uma linha.** Eram seis linhas de callout `[!info]` em
   toda nota; agora é uma linha em itálico, com a mesma informação e a mesma promessa (apagar tudo o que
   tem `*` devolve o documento a 100% canônico).
3. **A "Ficha rápida" foi absorvida pelo `O essencial`.** Tipo, onde, quando, duração, escala de poder e
   quem pode entrar viraram as linhas do bloco novo, em vez de uma tabela separada que repetia o corpo.
4. **Prosa virou tabela** onde a informação era tabelável: as duas eras da `16`, os temas de calamidade
   da `21`, as feras deslocadas da `27`, e o miolo inteiro da `29`.

## Linhas e palavras, por nota

| Nota | linhas antes | depois | corte | palavras antes | depois | corte |
|---|---|---|---|---|---|---|
| `01 - Visão Geral dos Eventos` | 412 | 302 | **−26%** | 5644 | 5416 | −4% |
| `16 - A Montanha Yi Tian` | 443 | 333 | **−24%** | 4521 | 3769 | −16% |
| `17 - Caçadas, Emboscadas e Fugas` | 360 | 231 | **−35%** | 4023 | 2866 | −28% |
| `18 - Quando uma Força Morre` | 415 | 310 | **−25%** | 4413 | 3635 | −17% |
| `19 - Cercos e Invasões de Terras Abençoadas` | 519 | 356 | **−31%** | 5641 | 4182 | −25% |
| `20 - O Cerco da Montanha Nevada e o Rio de Fluxo Reverso` | 363 | 286 | **−21%** | 4017 | 3470 | −13% |
| `21 - Calamidades e Tribulações como Cenário` | 472 | 363 | **−23%** | 5501 | 4689 | −14% |
| `22 - Leilões, Cúpulas e Guerras de Mercado` | 436 | 332 | **−23%** | 4676 | 4032 | −13% |
| `23 - A Cerimônia das Miríades de Tribos e a Estrada da Vida` | 362 | 277 | **−23%** | 3874 | 3162 | −18% |
| `24 - A Grande Era e as Marés de Qi` | 414 | 316 | **−23%** | 4576 | 3868 | −15% |
| `25 - A Guerra do Destino` | 360 | 280 | **−22%** | 3881 | 3398 | −12% |
| `26 - A Caverna do Demônio Enlouquecido` | 327 | 276 | **−15%** | 3666 | 3378 | −7% |
| `27 - A Morte do Sol e o Céu Espectral` | 401 | 323 | **−19%** | 4036 | 3832 | −5% |
| `28 - O Mundo em Véspera de Guerra` | 404 | 315 | **−22%** | 4293 | 3839 | −10% |
| `29 - Eventos Históricos de Fundo` | 611 | 222 | **−63%** | 6015 | 4895 | −18% |
| **TOTAL** | **6299** | **4522** | **−28%** | **68777** | **58431** | **−15%** |

**Por que as duas colunas divergem tanto.** O corte de linha é maior que o de palavra porque metade do
enxugamento foi de *estrutura*, não de texto: cabeçalhos de seção que sobravam, listas de uma linha por
item que viraram parágrafo denso, tabelas que absorveram prosa. A queixa do usuário era de leitura, e é
a linha — e sobretudo a existência de um ponto onde parar — que a resolve.

## O que foi cortado, por categoria

**Repetição entre seções da mesma nota** (a maior fatia). Casos típicos: em `21`, `26`, `27`, `28` e
`21`, a seção "O que um grupo de personagens faz aqui" reenunciava, por faixa de rank, o que a ficha
rápida e o corpo já tinham dito — foi condensada para o que é específico da faixa. Em `17`, o parágrafo
"Como é por dentro" repetia a tabela de fases logo abaixo, e foi fundido nela. Em `18` e `24`, "O que
está em jogo" repetia "Desfechos possíveis"; os dois viraram um.

**Regra geral do mundo que pertence a outra nota, trocada por wikilink.** Em `18`, o parágrafo sobre
posições internas numeradas e disputáveis das super forças → `[[13 - As Grandes Forças do Mundo]]`. Em
`18`, o segredo enterrado do vale → `[[07 - Aberturas de Herança|08 - Aberturas de Herança]]`. Em `24`, a descrição completa das
Dez Terras (cinco descritas, cinco só nomeadas) → `[[11 - As Terras Ferozes e o Subsolo do Mundo|12 - As Terras Ferozes e o Subsolo do Mundo]]`,
mantidas na nota só as quatro que rendem cenário imediato. Em `19`, a seção "A porta dos fundos: o
espírito da terra e a condição de posse" duplicava, quase palavra por palavra, o fecho de `18`: virou um
bullet com ponteiro. Em `21`, o bloco do desastre caótico foi reduzido a um parágrafo, com o
desenvolvimento completo ficando em `26`, que é a casa dele. Em `22`, o bloco dos quadros de facção foi
reduzido e aponta para `13`; em `28`, o modelo comercial do mercado aberto de refino aponta para `22`.

**Ornamento e ênfase repetida.** Frases de tipo "este é o melhor X da obra" apareciam duas ou três vezes
na mesma nota; sobrou uma. Callouts `[!note] Para o design` que diziam a mesma coisa em pontos
diferentes foram fundidos (dois em `17`, dois em `19`, dois em `24`).

**Seção vazia por obrigação de modelo.** "O que a obra não diz" era uma lista de seis a oito bullets de
uma linha em quase todas as notas; virou um parágrafo corrido em treze delas — mesmas lacunas, um terço
das linhas. As listas de "Relações" perderam os itens que repetiam o que já estava linkado no corpo.

## Fatos canônicos movidos (nenhum perdido)

- `18` → o mecanismo das posições numeradas e disputáveis foi para o ponteiro a
  `[[13 - As Grandes Forças do Mundo]]`; o texto local guarda a consequência (por que aliados se traem
  rápido no rescaldo).
- `19` → os três exemplos de condição de posse (a árvore que pede sangue de Venerável, a terra que trocou
  de dono por negociação, o espírito que só aceita dois nomes) ficaram em `18`, com `19` apontando para
  lá; a regra de que a condição **não tem relação com quem matou o dono** foi mantida nas duas.
- `21` → o desastre caótico: o calendário do rank 9 (grande tribulação a cada 10 anos, miríade a cada
  50, desastre caótico a cada 100), o crescimento espontâneo do buraco na fronteira e o fogo negro
  residual estão íntegros em `26`; `21` guarda o resumo e o ponteiro.
- `24` → as Dez Terras: a lista nominal completa e as cinco que só existem como nome estão em `12`; `24`
  guarda o número (dez), a origem (fusão das veias), as quatro descritas e as duas regras de subsolo.
- `29` → **todos** os vinte e cinco episódios do original estão nas duas tabelas ou nos quatro blocos
  desenvolvidos. Nenhum episódio, número ou regra do mundo saiu; o que saiu foi o cabeçalho de seção de
  cada um e a prosa de ligação.
- `20` → a divergência interna sobre o número de picos (quinze duas vezes, doze numa passagem tardia)
  saiu do meio da lista de lacunas e virou um `[!warning]` próprio, para não se perder num parágrafo.

## As duas notas com tratamento próprio

**`29 - Eventos Históricos de Fundo` — cortada 63%, de 611 para 222 linhas.** Era a maior da pasta e a
que menos precisa de detalhe: existe para dar contexto e gancho, não cenário. O miolo virou **duas
tabelas de uma linha por episódio** — "A cronologia", ordenada de 3,8 milhões de anos até vinte anos
atrás, e "Os episódios sem data" —, cada linha com o que aconteceu e **o que mudou no mundo, mais o
gancho**. Só quatro episódios ficaram desenvolvidos, porque carregam lição de desenho de cenário e não
só um fato: a origem logística das heranças ubíquas, o arquétipo completo da vingança, o segredo do Gu
do Destino (origem dos imortais-zumbi e das feras de alma) e a mitologia como documentação técnica.

**`28 - O Mundo em Véspera de Guerra` — deixou de fingir que é cenário.** O `O essencial` dela abre com
um `[!warning]` que diz, com todas as letras, que a nota **não é um cenário**: não tem gatilho, trava,
relógio nem prêmio, e serve de ambientação ao lado de um cenário de verdade, nunca no lugar de um. A
"Ficha rápida" que fingia ter tipo, duração e faixa de rank foi removida; a seção "Desfechos possíveis"
virou "Como o período pode terminar", que é o que ela de fato descreve. O único trecho que funciona como
cenário — a fronteira dentro de um mundo-pintura — está sinalizado como tal.

## O recorte "leia estes primeiro" da nota-porta

Oito notas, escolhidas para cobrir o leque inteiro sem repetir formato. As outras vinte ficam
declaradas como acervo de consulta, não leitura obrigatória.

| # | Escolhida | Justificativa |
|---|---|---|
| 1 | `02 - A Maré de Lobos de Qing Mao Shan` | **A vila, rank 1-3.** É o único cenário que ensina o cotidiano do mundo enquanto roda: mérito, aliança, inverno, mobilização. Sem ele, a designer entra pela ponta errada da escada |
| 2 | `05 - Feiras, Caravanas e Festivais` | **A sessão sem combate, rank 1-4.** Prova, logo cedo, que a pasta não é um catálogo de brigas — e entrega a economia e a etiqueta que todas as outras notas pressupõem |
| 3 | `09 - A Herança dos Três Reis` | **A masmorra, rank 2-4.** A instituição mais característica do mundo na sua versão mais extrema, com uma corrida do ouro rodando por fora. A alternativa mais fácil de arbitrar (`15`) está indicada na própria linha |
| 4 | `14 - O Ciclo Decenal das Planícies do Norte` | **O ciclo regional, rank 2-5.** O modelo de como um calendário vira campanha, com fase social, militar e de exploração — e o exemplo mais limpo de trava institucional |
| 5 | `16 - A Montanha Yi Tian` | **A guerra, rank 3-5.** A melhor demonstração do que uma trava canônica faz por uma mesa: cem dias em que os fortes literalmente não podem pisar no campo |
| 6 | `17 - Caçadas, Emboscadas e Fugas` | **O formato transversal, rank 3-7.** É o que a designer mais vai reaproveitar, serve nos dois lados da mesa, e carrega a única trava do cardápio que trabalha a favor de quem é fraco |
| 7 | `18 - Quando uma Força Morre` | **O sandbox, rank 1-7.** O único cenário do mundo sem porteiro, e o único em que a oposição tem exatamente o tamanho do grupo. Responde à pergunta "o que fazemos quando não há chefe?" |
| 8 | `24 - A Grande Era e as Marés de Qi` | **A escala de mundo, rank 1-8.** Fecha o leque por cima, e é o único cenário que roda com a mesa inteira em ranks diferentes ao mesmo tempo — o problema mais difícil de qualquer campanha longa |

Cobertura resultante: vila (1), social (2), masmorra (3), ciclo regional (4), guerra (5), formato
transversal (6), sandbox (7), mundo (8). Faixa de rank contínua de 1 a 8, sem buraco.

## O resto da nota-porta

- **Tabela única de escolha rápida**, uma linha para cada um dos vinte e oito cenários, com seis colunas:
  nome, tipo, faixa de rank, quanto dura, **a trava que usa** e o tipo de sessão que entrega. A coluna da
  trava foi preenchida com a redação da própria linha "A trava" de cada nota, para que a tabela e a nota
  não divirjam. É o que a designer vai consultar de verdade, e substitui o antigo "Mapa da pasta".
- **O cardápio das travas** foi mantido inteiro (dezoito itens, que é o melhor conteúdo da pasta) mas
  enxugado para consulta, com um ponteiro de nota ao fim de cada item. O título da seção continua
  `## As travas`, deliberadamente: quinze notas do vault linkam para a âncora `#As travas`, e trocá-lo
  quebraria todas.
- **As regras do mundo** foram de doze para onze itens, com a fortificação e a informação fundidas num
  só (eram a mesma regra dita de duas maneiras) e cada item comprimido para uma frase-regra seguida do
  exemplo canônico.
- **Jogador × mestre** deixou de ser duas listas de bullets e virou dois parágrafos densos, com as
  mesmas seis e sete afirmações. As três recomendações de "como usar um evento como espinha de campanha"
  foram mantidas, porque são a única coisa da nota que ensina método.

## Onde decidi NÃO cortar (e por quê)

- **`16 - A Montanha Yi Tian` (−24% em linha, −16% em palavra).** São **dois cenários completos** numa
  nota só, separados por décadas dentro da ficção e independentes na mesa. Cortar um terço significaria
  amputar um dos dois. O `O essencial` dela é uma tabela de duas colunas — uma por era — justamente para
  que a designer decida qual das duas quer antes de ler qualquer outra coisa.
- **`20`, `23` e `26` (−21%, −23%, −15%).** São notas de **lista de regras**, não de prosa: as catorze
  regras do Rio de Fluxo Reverso, as seis da Estrada da Vida mais as dos Predicamentos, e as sete da
  Caverna. Cada item é uma regra mecânica distinta, e a instrução era explícita em que regra mecânica não
  sai. O que dava para cortar era a moldura em volta, e foi cortada.
- **`27 - A Morte do Sol` (−19% em linha, −5% em palavra).** São três catástrofes encadeadas mais cinco
  regras ambientais permanentes mais um fenômeno inédito, todos com mecânica própria e nenhum redundante.
  A compressão possível foi de estrutura.
- **O cardápio das travas na `01`.** É a seção mais citada do vault (quinze notas apontam para ela) e a
  que o próprio usuário identificou como o melhor conteúdo da pasta. Foi enxugada frase a frase, mas
  nenhum dos dezoito itens saiu.

## Verificação

- `python3 _pipeline/auditar-links.py`: **219 notas, 5378 links por nome exato, 0 links quebrados, 264
  âncoras de seção resolvidas, 0 âncoras quebradas.**
- Varredura própria nas quinze notas: **0** pipes não escapados dentro de wikilink em tabela, **0**
  citações de capítulo no corpo (`(cap. NN)`), e `## O essencial` presente nas catorze notas de evento.
- Campo `fontes` do frontmatter preservado sem alteração em todas as quinze.
