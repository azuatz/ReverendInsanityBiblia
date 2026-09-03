# Revisão de leitora leiga — pasta `07 - Economia e Vida`

**Papel assumido:** designer profissional de RPG de mesa, competente, que **nunca leu**
Reverend Insanity e não vai ler. Tudo o que ela sabe vem destas dezesseis notas.

**Critério duro desta pasta:** a designer precisa conseguir **montar uma planilha**. Por
isso foram tratados como bloqueadores: preço sem unidade, renda sem período, custo sem
periodicidade, número que contradiz a tabela soberana
(`11 - Apendices/02 - Tabelas de Referência Rápida.md`), contradição entre duas notas da
pasta, e invenção apresentada como cânone.

**Fontes de verificação usadas:** seções 5, 13.8, 17, 18, 19.1–19.5 e 20 da tabela
soberana, lidas na íntegra; e `grep` direto no texto-fonte
(`/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/*.txt`) para cada divergência
suspeita — nenhuma negativa nem correção deste relatório saiu de fonte secundária.

---

## Cifras auditadas

| Medida | Número |
|---|---|
| Células de tabela contendo cifra, varridas uma a uma | **229** |
| Expressões monetárias distintas em prosa (`N pedras`, `N pontos`, `N pedras de essência imortal`) | **49 formas distintas**, em cerca de 120 ocorrências |
| Total de cifras conferidas contra a tabela soberana e contra as demais notas da pasta | **~350** |
| Cifras encontradas **sem unidade** | **31** — todas em tabelas de catálogo cujo cabeçalho dizia apenas "Preço" ou "Valor" (notas 02, 03 e 05) |
| Cifras encontradas **sem período** | **4** — pensão de Gu, inscrição da convenção, aluguel de imóvel na tabela de renda, estoque de materiais da convenção |
| Cifras que **contradiziam a tabela soberana** | **4** (ver bloqueadores 1, 2, 5 e 6) |
| Cifras que **contradiziam outra nota da pasta** | **3** (ver bloqueadores 3, 4 e o item sério do grau sucata) |
| Cifras corretas e bem ancoradas | a esmagadora maioria — ver "O que está bom" |

Nenhuma cifra ficou sem unidade ou sem período depois da revisão.

---

## Achados por nota

### 01 — Visão Geral da Economia

**BLOQUEADOR (corrigido) — a nota-porta não indexava a pasta inteira.** A seção "Como as
peças se encaixam" listava onze notas de dezesseis: ficavam de fora **09 (Aposta de
Rochas), 11 (Ritmo de Cultivo e Reclusão), 12 (Heranças e Provações) e 14 (Convenção do
Caminho de Refino)**. Numa pasta cuja barra lateral *é* o currículo, quatro notas órfãs
significam quatro notas que a leitora só encontraria por acidente. A lista foi reescrita
com as quinze notas, na ordem de leitura, cada uma com uma linha dizendo o que entrega.

**SÉRIO (corrigido) — regra 6 divergia da própria tabela de preços.** Dizia "rank 3 fica
na casa dos milhares a **dezenas de milhares**", enquanto a escada canônica (soberana
19.1 e notas 02/03) fecha o rank 3 em **1.000 a 10.000**. Reescrita degrau a degrau, com
os cinco ranks.

**SÉRIO (corrigido) — conflito de vocabulário.** A nota-porta apresentava a moeda só como
"pedra primordial", sem avisar que a leitora vai topar com "pedra primeva" em outras
pastas do vault (`03 - Paths`, apêndices) e em traduções publicadas. Acrescentado um
parêntese na primeira ocorrência.

**Verificado e correto:** as vinte regras do mundo; o resumo por camadas; a separação
`comum` × `segredo`; as âncoras de custo de vida; a escala de câmbio imortal
(1 : 100 : 10.000, na direção certa); a indexação das quatro notas novas (03, 05, 07, 08),
que já estavam citadas tanto no resumo quanto nas regras.

### 02 — Pedras Primordiais

**BLOQUEADOR (corrigido) — a nota de rodapé sobre tradução era incoerente.** Dizia que a
tradução brasileira usa "pedra primordial", que adotamos "pedra primordial", "mas os dois
termos designam exatamente o mesmo objeto" — **sem nunca nomear o segundo termo**. Uma
leitora que abrisse `03 - Paths` e lesse "4.500 pedras primevas" não teria como saber que
é a mesma moeda. Corrigido em dois lugares: a nota de rodapé foi reescrita nomeando os
dois pares (*pedra primordial / pedra primeva* e *essência primordial / essência primeva*),
e foi acrescentado um callout **logo abaixo do título**, onde a leitora não tem como não
ver.

**BLOQUEADOR (corrigido) — preços sem unidade.** Três tabelas (âncoras de preço, preço de
Gu por rank, preços de referência) tinham cabeçalho "Preço" e células com números nus.
Todas ganharam "(em pedras primordiais)" no cabeçalho, mais uma frase dizendo que a tabela
inteira está nessa unidade.

**SÉRIO (corrigido) — a linha de pedágio urbano era vaga e não batia com a soberana.**
Dizia "100, 200 e 600 nos anéis internos" sem dizer quais anéis. A ordem importa e é
contraintuitiva (os anéis são numerados de fora para dentro em ordem *decrescente*).
Reescrita com o anel de cada preço e um ponteiro para a tabela completa da nota 03.

**SÉRIO (corrigido) — legenda de confiabilidade com escopo errado.** O callout dizia
"Convenção de confiabilidade **desta seção**", mas os marcadores `(ded.)` e
`inferido · conferido pelo autor` aparecem em toda a nota, inclusive depois. Promovido a
"valem para a nota inteira" e ampliado para incluir o `—` e o rótulo
`inferido · conferido pelo autor`.

**MENOR (corrigido):** a pensão de Gu (80 pedras) não dizia "por mês, por Gu"; a folha
medicinal (55 a 80) omitia o piso de 50 e o teto de crise de 100+ que a nota 03 documenta.
Ambos alinhados.

**O que está bom, e é excelente:** a seção "A pedra na mão" é o melhor material
descritivo da pasta — a tabela de quantidade por recipiente, o mecanismo de encolhimento,
as três soluções de troco num mundo sem moeda fracionária, o teste do peso na mão, e o
diagrama `mermaid` do ciclo ovo→pó. A tabela de peso e volume está corretamente marcada
como aritmética nossa. O aviso "são duas economias, não uma" (mortal × Mestre Gu) é a
peça que impede a leitora de somar números incomparáveis, e a coluna "Público" o
operacionaliza linha a linha.

### 03 — Preços, Renda e Custo de Vida *(nota nova)*

**BLOQUEADOR (corrigido) — a tabela de pedágios contradizia a tabela soberana.** A nota
trazia "Primeira cidade interna 100 / **Segunda** cidade interna 200 / Terceira cidade
interna 600". A soberana 19.4 diz: cidade interna 100, **quarto anel** 200, **terceiro
anel** 600, **segundo anel e além: dinheiro não entra**. Confirmado no texto-fonte
(Volume 2, linhas 12188, 12241, 12291): "enter the inner city… a hundred primeval stones
per person", depois "two hundred primeval stones per person", depois "to enter the third
inner city… six hundred primeval stones". A tabela foi corrigida, ganhou a linha do
segundo anel (a que mostra o dinheiro deixando de funcionar) e um parágrafo explicando a
numeração decrescente dos anéis — que é a razão de o erro ser fácil de cometer.

**BLOQUEADOR (corrigido) — catálogo inteiro de preços sem unidade declarada.** Oito
tabelas com cabeçalho "Preço", "Valor", "Capacidade", "Faixa típica" e células com números
nus (220, 690, 4.550, 36.000, 810.000…). Todos os oito cabeçalhos receberam a unidade, e a
seção ganhou um callout de abertura fixando que tudo dali até o fim da renda está em
pedras primordiais, é preço de varejo, e que o período (por dia / por mês / por ano) é
parte do preço.

**SÉRIO (corrigido) — um preço fora de escala apresentado sem explicação.** "Força
amarga, em leilão de ego | rank 4 | 810.000" fica oito vezes acima do teto da faixa de
rank 4, e "leilão de ego" é jargão interno do vault que a leitora não tem como decodificar
ali. Confirmado no texto (Volume 2, linhas 21706–22310) que os 810.000 saíram de uma
guerra de lances por orgulho, e que o comprador nem sabia usar o Gu. Acrescentado um
callout dizendo que aquilo é o preço de uma humilhação pública, não de uma mercadoria, e
que a planilha deve usar a faixa do rank.

**SÉRIO (corrigido) — aritmética frouxa numa dedução marcada.** "Mais de cem milhões de
pedras ao longo de cinquenta a sessenta anos — em torno de **um milhão e meio** por ano".
A divisão dá entre 1,67 e 2 milhões. Corrigido para a faixa, mantendo o `(ded.)`.

**O que está bom, e é o coração da pasta:** esta é a nota que cumpre o critério da
planilha. A escada de referência ancorada em "uma pedra = um mês de família mortal"; o
aviso do *spread* 250/500 de compra e venda; a linha de produto de força bruta em quatro
ranks seguidos (que prova, sozinha, que é o custo de produção e não o rank que precifica);
a curva de inflação da folha de vitalidade acompanhada preço a preço ao longo de uma
crise; a tabela de renda com **rank típico e tempo gasto** nas colunas da direita — que é
o que separa uma tabela usável de uma lista de números; e o `*` explícito na extrapolação
de custo de vida para os ranks 4 e 5, com o cálculo à vista. A observação de que a renda
não cresce, **salta no rank 3**, é a melhor leitura de design da pasta inteira.

### 04 — Como um Mestre Gu Ganha a Vida

**SÉRIO (corrigido) — promessa não cumprida na tabela de renda.** A linha "Venda de
consumível cultivado" mandava a leitora a `[[02 - Pedras Primordiais]]` para achar o
preço; quem tem a curva de preço desse consumível é a nota 03. Redirecionado, e o número
(50 a 100 por unidade) posto na própria célula.

**SÉRIO (corrigido) — contradição com a nota 03.** "Missão simples de coleta | 2 a 6" sem
dizer que são 2 a 6 **no total, divididos entre cinco pessoas** (como a nota 03 registra).
Lido isoladamente, sugere 2 a 6 por cabeça — erro de fator cinco na recompensa de uma
sessão. Corrigido.

**SÉRIO (corrigido) — marcadores sem legenda.** A nota usa
`inferido · conferido pelo autor` num rodapé de tabela sem nunca explicar o que o rótulo
significa. Acrescentada a legenda-padrão dos quatro estados no topo.

**O que está bom:** as onze ocupações são um cardápio de mesa genuinamente utilizável, e
a décima primeira — "viver de patrimônio" — é a melhor decisão editorial da nota, porque
transforma a economia de pano de fundo em objetivo de campanha. O callout que compara o
salário de ancião (100/semana) com a nascente portátil (350/semana) fecha o argumento em
duas linhas. O aviso "mil por mês é renda de magnata, não de imortal comum" impede
exatamente o erro de calibragem que a cifra convidaria.

### 05 — Materiais e Cadeia Produtiva *(nota nova)*

**SÉRIO (corrigido) — wikilink com rótulo enganoso.** O texto escrevia
`[[03 - Preços, Renda e Custo de Vida|pedras primordiais]]` — ou seja, a leitora clicaria
em "pedras primordiais" e cairia na tabela de preços, não na nota que define a moeda. Pior:
a frase seguinte misturava duas moedas na mesma tabela. Redirecionado para
`[[02 - Pedras Primordiais]]`, o cabeçalho da tabela agora diz que a unidade vem em cada
linha, e foi acrescentado o aviso de nunca somar as duas colunas (uma pedra de essência
imortal vale mais de cem milhões de pedras primordiais).

**O que está bom:** a nota responde a pergunta que quase nenhum cenário responde — de
onde vêm as coisas — e responde com estrutura: seis famílias de material, seis fontes,
três camadas de mão de obra, cinco tipos de comprador. A regra 1 ("o Gu pertence à região
onde foi refinado, não à de onde veio o material") é o melhor gancho logístico do vault e
está bem explicada. A tabela "Quem compra" com a progressão *lote → fonte* ("um rank 2
compra um saco de ervas; uma super força compra a montanha") é didática de primeira. E o
estudo de caso do gargalo de capital × gargalo de matéria-prima é diretamente acionável.

### 06 — Mercados e Leilões

**BLOQUEADOR (corrigido) — contradição entre duas notas da pasta.** Dizia "valorização de
três vezes em cerca de **dez dias**"; a nota 03 documenta o mesmo caso como "cem mil em
trezentos mil em **vinte dias**". Verificado no texto-fonte (Volume 2, linha 24872): *"We
just need twenty days to triple your primeval stones."* A nota 06 estava errada; corrigida
e apontada para a nota 03, que é a dona do caso.

**SÉRIO (corrigido) — contradição com a nota 09 na escada de aposta de rochas.** Aqui:
"sucata (dezenas de pedras)"; na nota 09: "sucata, a partir de ~10", e a própria 09
registra balcões de aldeia a cinco pedras. Alinhado a "a partir de ~10", com unidade
explícita e ponteiro para a nota dona do assunto.

**SÉRIO (corrigido) — marcadores sem legenda.** Idem nota 04.

**O que está bom, e é o material mais evocativo da pasta:** "Como é comprar,
fisicamente". A parede de nichos em vez de prateleira; o andar da loja que *é* o preço;
os quatro recipientes; as falas literais dos avaliadores de fóssil, prontas para um mestre
interpretar; o tribunal que é a praça; a carteira viva cujo velho de nuvens muda de
expressão conforme o saldo. A escada de nove fichas está honestamente marcada como
reconstrução, com as pontas canônicas separadas do miolo inventado. E "Quando o comprador
é que tem monopólio" cobre um ângulo que praticamente nenhum cenário cobre.

### 07 — Crédito, Contratos e Tributos *(nota nova)*

**MENOR (corrigido):** um wikilink com `|` não escapado dentro de célula de tabela, que
quebrava a contagem de colunas da tabela de tributos.

**Verificado e correto:** o caso das 500.000 pedras em 24 horas (300.000 dos agiotas com a
identidade de ancião + 200.000 penhorando um Gu) bate **exatamente** com o texto-fonte
(Volume 2, linhas 19288 e 19355) — foi esta nota que permitiu flagrar o erro da nota 08.
Os pedágios (1 a 600), as taxas de inscrição (100 e 500) e as multas (30 e 49) batem com a
soberana e com a nota 03.

**O que está bom:** as seis formas de crédito organizadas **pela garantia** — reputação,
cargo, arma, imóvel, patrimônio, tempo de vida — é uma taxonomia que se converte
diretamente em decisão de jogador ("não é quanto você consegue, é o que você está disposto
a dar"). A corrida armamentista contratual em quatro gerações trata direito contratual
como tecnologia em disputa, e o mecanismo do voto venenoso (detecta má-fé **na
assinatura**, não mentira no futuro) é uma cena inteira de graça. A leitura de que a
tributação é **por portão, não por renda** amarra a pasta toda, e o `(ded.)` sobre o
"tributo em trabalho" do clã está corretamente marcado.

### 08 — Crime, Mercado Negro e Recompensas *(nota nova)*

**BLOQUEADOR (corrigido) — contradição com a nota 07 e com o texto.** Dizia que a
chantagem de três milhões teve "**metade paga em vinte e quatro horas**". O texto-fonte
(Volume 2, linha 19288) mostra a exigência de **quinhentas mil** em um dia — um sexto, não
metade — e o "quase metade já paga" (linha 25040) é o acumulado de meses. A nota 07
descreve o episódio corretamente; a 08 é que estava errada. Corrigida, com o restante
explicitado como parcelas.

**BLOQUEADOR (corrigido) — a nota se contradizia internamente.** Chamava os três milhões
de "a maior quantia isolada do mundo mortal em toda a obra" e, dez linhas adiante,
registrava um resgate de **dez milhões**. Verificado no texto (Volume 3, linha 11328): os
dez milhões existem. Reescrito: os três milhões viraram "uma das maiores quantias", e o
resgate de dez milhões recebeu o título, com a unidade explicitada.

**Verificado no texto e correto:** o "70 ou 80 vezes" da fraude aberta é canônico
literal — *"if I use unorthodox methods… I can easily jack it up by seventy or eighty
times"* (Volume 2, linha 8685) —, e o "sete a oito vezes é o limite deste mundo" também
(*"seven to eight times was the limit of this world"*). A escada de lucro bate com a
soberana 19.5. As recompensas de mandado (1.000 / 5.000–8.000 / 10.000 + ficha) batem com
a nota 03.

**O que está bom:** a escada de lucro é, como a nota diz, o item mais exportável da pasta,
e o callout que responde "por que meus jogadores simplesmente não roubam tudo?" com
custos que não aparecem na planilha é honesto e útil. A separação entre os **dois**
mercados negros — o dos mortais (bens sem procedência) e o dos imortais (revenda de
escassez, sem ilegalidade nenhuma) — é uma distinção que a leitora não teria feito sozinha
e que muda a cena. A seção das estradas, com o pedágio ritual por queda de braço, é um
modelo de instituição informal pronto para mesa.

### 09 — Aposta de Rochas

**BLOQUEADOR (corrigido) — promessa não cumprida, três vezes seguidas.** Uma tabela de
prêmio por grau foi removida em revisão anterior, mas **o texto em volta continuou falando
com ela**: "Três leituras que **a tabela** sozinha não dá"; "**Repare que ele empata**" (o
grau alto — empata com o quê, se não há coluna de retorno?); e, no callout de design, "a
perícia move a chance da **coluna 3**… com perícia de especialista, a taxa **da tabela**".
A leitora ficaria procurando uma tabela que não existe e um procedimento que não fecha.
Reescrito: as três leituras foram reancoradas nos quatro fatos canônicos que a própria
nota enumera, o argumento do grau alto foi refeito sobre a **dissecação gratuita** (com
`(ded.)` explícito), e o procedimento de mesa agora avisa de saída que a leitora vai
arbitrar as chances, dando o único número canônico (duas em dez, para pedras
**selecionadas**) e marcando a taxa de população com `*`.

**SÉRIO (corrigido) — invenção sem marcação.** O "~2%" da taxa de população aparecia como
se fosse dado; agora está `*` e vem com a conta que o sustenta.

**SÉRIO (corrigido) — parágrafo que anunciava uma reconstrução inexistente.** A abertura
da seção do prêmio dizia "A que segue é uma reconstrução deste vault" e o que seguia era
o aviso de que nada seria reconstruído. Reescrito.

**SÉRIO (corrigido) — marcadores sem legenda.** Idem nota 04.

**O que está bom:** o callout "os dois números medem coisas diferentes" (uma em dez na
população × duas em dez nas pedras selecionadas, e a diferença **é** o valor da perícia) é
a melhor explicação estatística do vault, e resolve uma contradição aparente que teria
travado a leitora. A decisão de **não** publicar a tabela de prêmio, e dizer por quê, é
editorialmente correta e agora está coerente com o resto da nota.

### 10 — Vida Cotidiana

**BLOQUEADOR (corrigido) — a nota contradizia frontalmente a tabela soberana sobre
longevidade.** Dizia: "Cultivar prolonga a vida, e cada rank estende o teto… a partir do
rank 6 o cultivador **deixa de envelhecer**". A soberana §17 abre dizendo o contrário, e o
texto-fonte confirma sem margem: *"A Gu Master's cultivation to raise his rank did not
have any effect on his lifespan"* (Volume 3, linha 15094) e *"Although advancing to Gu
Immortal realm could allow a Gu Master's life to improve qualitatively, it could not
increase his lifespan"* (Volume 3, linha 35956). Este era o erro mais caro da pasta: ele
inverte o valor dos Gu de tempo de vida, apaga a economia de anos que sustenta metade das
mecânicas de alto nível, e faria a designer construir uma progressão em que subir de rank
compra tempo. A seção foi reescrita inteira, com o método legítimo (os Gu de tempo de
vida, em cinco graus), o ponteiro para `[[12 - Longevidade]]` e para a soberana, e a
consequência social invertida — o ancião da vila é velho **de verdade**.

**BLOQUEADOR derivado (corrigido):** a seção "As duas humanidades" descrevia Mestres Gu
como tendo "vida mais longa". Corrigido e ligado à seção seguinte.

**SÉRIO (corrigido) — contradição de ordem de grandeza com as notas 02 e 03.** Tratamento
de dano permanente descrito como "centenas de milhares de pedras"; as duas outras notas e
a fonte dizem **~100.000**. Corrigido, com a comparação com o custo de vida mortal.

**SÉRIO (corrigido) — marcadores sem legenda.** Idem nota 04.

**O que está bom, e é a nota mais prazerosa de ler da pasta:** "Por dentro de uma casa" e
"Uma vila em voz alta" fazem exatamente o que prometem — a designer lê uma vez e descreve
a cena sem consultar nada. A escada de iluminação como escada de riqueza; a lista
explícita do que a obra **não** descreve (sabão, latrina, casa de banhos, agasalho), que
converte lacuna em espaço de design em vez de esconder; as casas vivas; a tabela do que
puxa a carroça, com a avestruz substituindo o cavalo. O callout final — a vila escura, e a
pedra do tamanho de um ovo que a pessoa pode gastar consigo ou com a família — é a melhor
frase da pasta.

### 11 — Ritmo de Cultivo e Reclusão

**BLOQUEADOR (corrigido) — números que contradiziam a tabela soberana.** "Os [Gu de
relíquia] de rank 2 custam na faixa de **3.000 a 8.000**; os de rank 3, de **30.000 a
50.000**". A soberana 19.1 dá pontos, não faixas: rank 2 = **8.000**, rank 3 = **50.000**
(e a nota 03 concorda). Os pisos de 3.000 e 30.000 não têm base no texto — a única
passagem próxima (Volume 1, linha 16542) prevê que o relic Gu vermelho-aço "certamente
passará de cinco mil e pode chegar a oito mil", ou seja, o oposto de um piso de 3.000.
Substituído pela escada canônica dos quatro ranks, com ponteiro para a nota 03, e
acrescentada a observação (que a soberana faz e que é ótima para mesa) de que um
consumível de rank 2 custa mais que um Gu permanente de rank 3.

**MENOR (corrigido):** "Relic Gu" aparecia em inglês sem tradução na primeira ocorrência,
embora as notas 02 e 03 usem "Gu de relíquia". Padronizado.

**Verificado e correto:** os 4% e 8% de reposição por hora batem com a soberana §1 e
§14.1; o piso de 55% para o salto 1→2 e a trava dos 44% batem com a soberana §2; a régua
de expectativa dos clãs (D/C/B/A) não conflita com a tabela de graus.

**O que está bom:** o aviso de abertura sobre o que a obra **não** dá; a separação entre
os dois relógios (estágio × rank) e a afirmação de que **tempo não compra rank**, que é a
mecânica de progressão mais incomum do cenário; a lista do que se **perde** numa reclusão
(renda, informação, posição, segurança), que é o que transforma "avançar o tempo" numa
decisão; e a logística de reclusão em quatro itens, com a comida dos Gu como o item que
mais restringe o prazo.

### 12 — Heranças e Provações

Nenhum bloqueador e nenhum achado sério. A nota quase não usa cifras — e as que usa
("centenas de milhares de heranças falsas", "triplica em dias") batem com as notas 06 e
13.

**O que está bom:** a assimetria de risco entre herança do caminho correto (pune com menos
prêmio) e demoníaca (pune com a vida) é um botão de letalidade que o mestre gira antes de
desenhar uma sala. A estrutura em quatro salões — abundância → autocontrole → caráter →
sorte — é um esqueleto de sessão pronto e sem combate. A "trava de reconhecimento", com um
guardião que não pode mentir, avalia conduta passada e **pode destruir o prêmio**, é uma
mecânica de encontro rara. E a ressalva de escopo marcada explicitamente (a obra não diz
que *toda* herança demoníaca impõe condição) é exatamente o comportamento certo.

### 13 — Eventos e Instituições Jogáveis

**BLOQUEADOR (corrigido) — promessa não cumprida no callout de abertura.** O callout
anunciava "são **seis** [eventos com prêmio quantificado], e vale saber quais são" e
listava seis nomes — mas **dois deles não têm prêmio quantificado em lugar nenhum**: a
convenção de refino ("prêmios crescentes", número só na inscrição) e os torneios entre
organizações ("vantagens territoriais concretas"). Uma designer planejando uma sessão em
cima dessa lista iria procurar números que não existem, que é precisamente o que o callout
prometia evitar. Reescrito: agora são **quatro**, numa tabela que dá o número de cada um em
vez de só o nome, e o texto explica que a convenção e os torneios entram na coluna dos não
quantificados porque só precificam a inscrição.

**SÉRIO (corrigido) — contradição com a nota 03.** "Subjugação de matilhas… recompensas na
casa das centenas de pedras mais um Gu de **rank alto**"; a nota 03 registra **500 pedras
mais um Gu de rank 3**. Corrigido para o valor preciso.

**MENOR (corrigido):** a prova de sucessão comercial não dizia quanto era o capital
inicial (100.000) apesar de estar listada entre os eventos quantificados; a inscrição da
convenção não dizia que é pagamento único.

**O que está bom:** o calendário de campanha por frequência (diária → milenar) é a tabela
mais imediatamente utilizável da nota. As regras de arena, os três níveis de sistema de
mérito e o obelisco com títulos-desbloqueio e saldo negativo são estruturas de jogo
completas. O ciclo decenal pelo trono, com a proibição explícita de os poderosos agirem
pessoalmente, é uma campanha inteira em uma página — e a proibição é justamente o que a
torna jogável por personagens de rank baixo.

### 14 — Convenção do Caminho de Refino

**SÉRIO (corrigido) — cifra sem unidade nomeada.** "Grande volume de material próprio, na
ordem de centenas de unidades **da moeda de patamar imortal**". Qual? A camada imortal tem
duas coisas contáveis (pedras de essência imortal e contas de essência) e elas não são
intercambiáveis. Nomeado como **pedras de essência imortal**, com ponteiro para a nota 15 e
com o contraste explícito contra a inscrição de cem pedras primordiais — que é a
informação útil: entrar é barato, competir não é.

**O que está bom, e é a melhor nota-evento do vault:** a regra dos "três primeiros a bater
a meta" cria pressão de tempo sem iniciativa nem turnos; o duelo marcial com escalada de
rank no ataque e defesa travada no mesmo rank é uma regra de balanceamento pronta com
justificativa interna; a trégua universal permite uma sessão inteira de tensão social com
inimigos legalmente intocáveis; e a explicação do **dao mark de sucesso** faz exatamente o
que a memória do projeto exige de um catálogo — explica o mecanismo inteiro (o que cobre,
o que não cobre, quantos por rank, por que é intransferível) em vez de dar um rótulo. O
segredo de origem, marcado `[segredo]`, é o melhor gancho de mestre da pasta: os
competidores são a matéria-prima. E o callout "o que a obra não esclarece" delimita as
lacunas em vez de preenchê-las.

### 15 — Economia Imortal

**BLOQUEADOR (corrigido) — a nota contradizia a tabela soberana num ponto que a soberana
corrige nominalmente.** O callout "Converter para cima custa mais do que a proporção
nominal" afirmava que fundir cem contas de uva verde numa de tâmara vermelha consome
"pelo menos cento e trinta". A soberana §5 diz o contrário, com todas as letras: a fusão é
100:1 limpa, e os 130 são a **penalidade de uso** de acionar um Gu de rank 7 com essência
de rank 6. Verificado no texto-fonte (Volume 5, linhas 35870, 36726 e 36730): *"One
hundred beads of green grape immortal essence could merge into a bead of red date immortal
essence"* e, separadamente, *"If green grape immortal essence was used to activate rank
seven Immortal Gu, there would be at least thirty percent additional expenditure."* O
callout foi reescrito separando as duas regras, dando a regra prática de mesa (converta a
100:1, cobre 30% de sobretaxa) e explicando por que somar as duas é o erro clássico.

**SÉRIO (corrigido) — marcadores sem legenda.** Idem nota 04.

**MENOR (corrigido):** "pedras primordials" (erro de digitação); cabeçalho da tabela de
riqueza ambíguo entre rank do cultivador e rank da moeda; um wikilink com `|` não escapado
dentro de célula de tabela.

**O que está bom:** o callout que desmonta a confusão entre as duas leituras da mesma
proporção ("1 real vale 20 centavos" × "5 moedas de 20 centavos valem 1 real"), com
exemplo fechado, é didática exemplar. A tabela de riqueza típica por rank; a grade de sete
portes de ponto de recurso com os três de baixo honestamente marcados como reconstrução; a
tabela de seis credores com termos diferentes para o mesmo tomador no mesmo dia (crédito
como função da política, não como taxa de mercado); e sobretudo os **dois** avisos que
cercam a guerra de preços — "esse lucro é o teto histórico, não calibre sua mesa por ele" e
"o princípio se replica; o número, não" — que é exatamente o cuidado que essa pasta
precisa ter com números excepcionais.

### 16 — Produzir Gu Dentro da Abertura

**SÉRIO (corrigido) — número em conflito com a tabela soberana.** "Um Mestre Gu mortal tem
**menos de dez** Gu ao mesmo tempo". A soberana §20 é específica: **3 a 5** é o comum, 7 já
é apresentado pela obra como excepcional. "Menos de dez" faria a designer dimensionar
arsenais quase o dobro do canônico. Corrigido.

**O que está bom:** o callout de cinco palavras no topo, que torna a nota autossuficiente
para quem chega sem ler o resto do vault, é o gesto didático certo. A regra fundadora ("Gu
refinados não se reproduzem", logo o rebanho é a fábrica e o Gu é o produto) e o contraste
que a prova (a imitação de poço que armazenou e não produziu) explicam o mecanismo inteiro
em duas seções. O peixe-bolha, com taxa de incubação, prazo de maturação, exigências
ecológicas e arranjo em camadas, é um sistema de produção completo. E as duas maneiras de
a fazenda falhar — consumo maior que produção, e gargalo de insumo barato — são as duas
melhores sabotagens do cenário.

---

## Veredito de conjunto

**A pasta passa no critério da planilha — agora.** Antes desta revisão, não passava: nove
bloqueadores, dos quais quatro eram números em conflito direto com a tabela soberana e
três eram contradições entre notas da própria pasta. Um deles (a longevidade da nota 10)
teria levado a designer a construir uma progressão de personagem inteira sobre uma regra
que a obra nega duas vezes.

Contagem final: **9 bloqueadores**, **16 achados sérios**, **8 menores** — todos os
bloqueadores e todos os sérios corrigidos no ato. Nada de substantivo ficou aberto.

Sobre as quatro notas novas de hoje (03, 05, 07, 08): elas **conversam** com as antigas em
vez de repeti-las, e a divisão de trabalho é clara e está declarada em ambas as pontas — a
02 guarda as âncoras e manda quem quer o catálogo para a 03; a 03 declara que a 02 é a
fonte conceitual e que ela própria vence em caso de divergência; a 04 remete à 03 para as
tabelas completas; a 05, a 07 e a 08 remetem à 03 para os números e se dividem por função
(cadeia produtiva, instituições de crédito, economia criminal) sem sobreposição relevante.
A nota-porta 01 já as indexava no resumo e nas regras do mundo, mas **não** as tinha na
ordem de leitura completa — junto com outras três notas antigas; isso foi corrigido.

Sobre o conflito de vocabulário: dentro desta pasta o texto já estava padronizado em
"pedra primordial" e "essência primordial" — a única ocorrência de "primeva" era um alias
de frontmatter e uma nota de rodapé quebrada. O que faltava era **avisar a leitora**, já
que ela vai encontrar "pedras primevas" em `03 - Paths` e nos apêndices. Isso agora está
dito em dois lugares visíveis (callout no topo da nota 02 e parêntese na primeira
ocorrência da nota 01) e na nota de rodapé reescrita.

O que essa pasta faz melhor que qualquer outra do vault é **cercar os números
excepcionais**. Os avisos de "isto é um recorde, não uma média" (o lucro de doze milhões,
as dezesseis contas por dia, o piso do tráfico, as 810.000 pedras do leilão de ego, os mil
por mês do imortal-empresário) são o que impede a designer de calibrar uma economia
inteira em cima de um outlier. Esse hábito deveria ser copiado pelas outras pastas.

---

## Três coisas que eu mudaria com mais tempo

**1. Uma folha de cálculo única, de uma página, no fim da nota 03.** Hoje a designer que
quer montar a planilha precisa costurar quatro seções (escada de referência, catálogo,
renda, custo de vida) e três notas (02, 03, 04). Falta a página que ela vai imprimir e
deixar do lado: *uma* tabela com quatro colunas — item, valor, unidade, período — e uma
linha por cifra canônica da pasta inteira, ordenada por ordem de grandeza. As cifras já
existem e já estão corretas; o que falta é a apresentação que dispensa a costura. Seria a
melhoria de maior retorno por esforço da pasta.

**2. Fechar a lacuna de custo de vida dos ranks 4 e 5 de forma assumida.** A nota 03 marca
corretamente a extrapolação `*` (×15 por rank, dando seis milhões e noventa milhões por
ano), mas o número mora num callout de aviso, não na tabela — então a designer que abre a
tabela de custo de vida vê dois travessões e não tem o que pôr na planilha. Eu levaria a
extrapolação para dentro da tabela, com o `*` bem visível na própria célula, porque a
regra do projeto é que preencher lacuna é permitido desde que marcado — e uma célula
marcada é mais útil que uma célula vazia mais um callout que a explica.

**3. Uma passagem de padronização dos rótulos de confiabilidade.** A pasta usa quatro
vocabulários para a mesma ideia: `(ded.)`, `*`, `inferido`, e
`inferido · conferido pelo autor`. Acrescentei a legenda onde faltava e expliquei o
rótulo longo como "um `*` já revisado", mas isso é remendo: o certo seria escolher **um**
esquema e reescrever todas as ocorrências do vault de uma vez, com um script, como já se
fez com a numeração das notas. Enquanto houver quatro rótulos, a promessa "apague tudo que
tem `*` e o documento volta a ser cem por cento canônico" não é literalmente verdadeira —
sobrariam os `inferido`.
