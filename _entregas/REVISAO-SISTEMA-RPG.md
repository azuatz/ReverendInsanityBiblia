# Revisão externa do sistema de RPG

> Documento de trabalho de um revisor externo. Destinatário: o agente que mantém
> `/home/azuatz/Documentos/REVEREND INSANITY/`. Este revisor **não editou nada** no
> sistema — só leu.
>
> **Status: EM ESCRITA INCREMENTAL.** Blocos são gravados assim que fecham.

## Como esta revisão foi feita

**Três acervos, três papéis.**

1. **O sistema** — `/home/azuatz/Documentos/REVEREND INSANITY/` (842 arquivos, 39 MB).
   Objeto da revisão. Lido: `CLAUDE.md`, `00 — Portal/` inteiro, `01 — Fundação/`
   inteiro, `02 — Caminho do Cultivo/` inteiro, `03 — Gu/` (estrutura + notas de
   regra), `04`, `05`, `06`, e varreduras por termo em todos os 842 arquivos.
2. **A Bíblia de Sistema** — `/home/azuatz/Documentos/ReverendInsanityExpert/`
   (140+ notas escritas a partir da leitura integral da obra). Base de comparação.
3. **A obra** — `~/Documentos/Reverend-Insanity-fonte/texto/*.txt`, 6 volumes.
   **Autoridade máxima e desempate.** Toda citação de capítulo abaixo foi verificada
   por `grep -i` no texto-fonte, e o número do capítulo foi resolvido com
   `head -n <linha> <vol> | grep -oE "^## Chapter [0-9]+" | tail -1`.

**Achado de método que vale registrar para o agente executor:** a obra grafa nomes
de Gu, essências e golpes **em minúsculas** ("all-out effort Gu", "green grape
immortal essence bead"). Buscar com `grep` sensível a maiúsculas produz falsos
negativos em massa. **Use sempre `grep -i`.** E o termo canônico em inglês é
**primeval** (essence / stone / sea) — "primordial essence" **não existe na obra**,
embora "essência primordial" seja a tradução PT correta.

**O que ficou de fora, e por quê.**

- `09 — Lore de Vespéria/` — é cenário autoral do usuário, não Reverend Insanity.
  Divergência ali não é erro. Não revisado.
- `10 — Referência Canônica/` e `_Fontes/` — imutáveis por regra do próprio vault.
  Usados só como leitura, para entender de onde vieram os números do sistema.
- `_Processo/🎯 Simulação de Combate — Resultados.md` (330 KB) e
  `_Processo/🧭 Log de Decisões.md` (500 KB) — consultados por busca dirigida, não
  lidos linha a linha. **Consequência honesta:** é possível que um achado abaixo já
  tenha uma decisão registrada que o justifica. Onde suspeitei disso, avisei.
- Balanceamento numérico interno (o sistema tem simulação própria com 3.000+
  iterações). Não é o meu papel e eu não tenho os dados dela.

**O critério de corte.** O pedido do usuário foi explícito: *"há coisas que não
precisa colocar por já estar muito cheio, mas coisas que você achar que estão
incompletas e crê ser o recomendado, envie para ele adicionar."* Portanto isto
**não é uma lista do que falta** — é uma lista curada. Um achado só entrou se
passou por um destes três filtros:

1. **contradiz a obra** (erro de canonicidade),
2. **falta algo sem o qual o mestre trava na mesa** (regra sem número, recurso sem
   economia, procedimento sem passo a passo), ou
3. **o sistema já tem o assunto, mas raso, e a obra dá material que o torna muito
   melhor** — e o ganho é grande o bastante para pagar o volume que acrescenta.

Tudo que não passou nos três filtros virou a seção **"O que existe na obra e eu NÃO
recomendo acrescentar"**, no fim. Essa seção é parte do produto: ela poupa o agente
executor de reabrir discussões já fechadas por mim.

---

## Panorama: o que o sistema já cobre bem

Isto não é cortesia — é a lista do que **não se deve mexer**. O sistema é maduro, e a
maior parte do que eu poderia "acrescentar" já está lá, muitas vezes melhor resolvido
do que eu resolveria.

**Motor de jogo (`01 — Fundação/`).** Fechado e medido. Dois trilhos de dano
(Vitalidade e Alma), fórmula de tanque por rank e estágio (`(18 + 3×CON + 4×Grau) × M`),
Teste de Morte com sequela, escada de M por rank (`1·2·4·8·16·32·64·128·256`),
calibragem declarada ("um personagem CON +3 aguenta ~6,5 golpes de um Gu d10 do próprio
rank"). `⚔️ Combate`, `🏃 Fuga e Perseguição`, `👁️ Exposição`, `🧠 Dedução` e
`🕵️ Preparação e Informação` formam um conjunto coerente, com CDs, custos e
procedimento. Vinte e seis rodadas de simulação por trás.

**Cultivo mortal.** Aptidão em quatro graus com % de abertura, distribuição
populacional separada da rolagem de criação (o furo dos 25% está identificado e
corrigido no próprio texto), regeneração de essência por grau e por hora com
procedência canônica citada (cap. 10), fórmula de essência
(`% de abertura × 4 × 2^(estágio−1)`), e o aviso de sessão zero para quem tira Grau D.
Isto é bem melhor do que a média do gênero.

**Longevidade.** `⏳ Longevidade` é uma das melhores notas do vault: o teto de 100 anos,
o Gu de Longevidade como único caminho limpo, **onze desvios tabelados** com o que cada
um cobra, as duas regras de amarração (exclusividade e `+2` de CD por método
heaven-defying acumulado), e anos de vida como moeda gastável. Inclui a divergência
canônica declarada em callout (cap. 563 e 519 dizem que ascender não estende a vida; o
sistema criou o relógio novo por necessidade estrutural e **diz que criou**). É o modelo
de como este vault deve tratar divergência: assumida, justificada, rastreada.

**Terra Abençoada e Dilatação Temporal.** Quatro qualidades com área canônica conferida
contra os capítulos 609, 690, 939 e 1027; fluxo de tempo por rank (10×–30× no rank 6 até
60×–120× no rank 9); tanque de essência e regeneração por qualidade; Calamidade Terrestre
a cada 10 anos internos convertida para o calendário externo; Ferimento da Terra com
custo de reparo; e a regra de anquilosar a fenda (parar o tempo interno para parar as
tribulações). A `🌾 Ecologia e Economia da Terra Abençoada` transforma isso num ciclo
anual de cinco passos com Sintonia elemental, Capacidade de Carga, cadeia alimentar,
trilha de Desequilíbrio 0–5, Teste de Gestão e eventos ecológicos em `1d6`. **É o
subsistema mais bem construído do vault** e não precisa de nada meu.

**Marcas de Dao (61 KB).** Progressão imortal inteira: faixas por rank, seis níveis de
domínio, quatro fontes de Marca, atrito interno entre Caminhos conflitantes (com o nome
canônico *internal friction*), escalada da Vontade do Céu por excesso de Marcas, e as
quatro condições de Venerável com a distinção — canônica e bem explicada — entre
**Marcas são estoque, Domínio é compreensão**.

**Espólio de Gu Imortal.** Os três estados (Tomado → Suprimido → Refinado), o dono vivo
que sente onde o Gu está, a exclusividade do Caminho da Sabedoria para suprimir a vontade
(citação literal do texto), e a assimetria "duas falhas encerram a supressão, uma falha
destrói no refino". Resolve sozinho o problema de "matar um imortal equipa a mesa".

**Catálogo e arsenal.** 391 KB de Catálogo de Gu com perfil ⬆️/⬇️ e tags de Peculiaridade
em três aptidões (⚡Uso · 🍖Alimentação · 🔨Refino), 12 Casas de Gu Imortal — **todas
canônicas, nenhuma inventada** —, Índice de Gu por Caminho, Livro de Receitas, Gu
Lendários com linhagens de evolução, Catálogo de Heranças e Gerador de Heranças.

**Caminhos.** 23 Caminhos jogáveis com dado por Caminho (`d12`/`d10`/`d8`/`d6`), tabela de
subcaminhos que mapeia cada rótulo do Catálogo ao Caminho-mãe, sinergias, e a "via de
avanço" de cada um. A regra que equilibra a tabela — *quanto maior o dado, menos o
Caminho faz além de dano* — é elegante.

**Higiene de processo.** `🧭 Log de Decisões` (500 KB) como contrato, `🎯 Simulação de
Combate` com 3.000+ iterações por cenário, `🩺 Lint do Vault`, `🔍 Playtest de Leitura —
Mestre Novo`, `🏁 Revisão Final`, e o `_Arquivo/` com as versões substituídas. As sete
lições de método da Revisão Final são melhores que a maioria das auditorias que eu
escreveria.

**Consequência prática para o agente executor:** quase tudo o que segue é **acréscimo
cirúrgico dentro de notas que já existem**, não nota nova. Onde eu proponho nota nova, eu
digo por que a caixa existente não serve.

---

## Achados, em ordem de prioridade

### 1. Essência imortal é **pessoal e intransferível** — e o sistema hoje diz o contrário

- **Categoria:** erro *(e, junto, o buraco mais caro do sistema: a economia de rank alto)*
- **Tamanho do trabalho:** médio — mas é o achado de maior retorno da revisão inteira

**O que está no sistema hoje.** Em `02 — Caminho do Cultivo/🪜 Ranks e Estágios.md`,
seção "A hierarquia da Essência Imortal":

> **Você produz apenas a essência do seu rank.** Um Imortal de rank 6 gera Uva Verde e
> mais nada; **se ele quiser Jujuba, tem que comprar, roubar ou receber.**

A primeira frase é canônica e está certa. A segunda inverte a regra do mundo: na obra,
**comprar, roubar e receber essência imortal alheia não serve para nada**, porque
essência alheia **não se usa**.

**O que a obra diz — a regra, em três enunciados diretos e independentes.**

1. **Cap. 638** — o enunciado mais explícito, e vale para os dois níveis de cultivo:
   > *"Gu Masters cannot use the primeval essence of others. Gu Immortals were also
   > unable to use the immortal essence of others."*

2. **Cap. 1625** — o enunciado com as exceções embutidas:
   > *"Immortal essence contained the Gu Immortal's will and had to belong to themselves,
   > if they died, their heavenly spirit or land spirit could use their immortal essence.
   > The only exception was Immortal Gu Houses as immortal essence from any source could
   > be used in them."*

3. **Cap. 2297** — o **porquê**, dito pelo próprio mundo:
   > *"Our aperture produces primeval essence while our immortal aperture produces
   > immortal essence, they all contain our human will."*

   A essência é feita da vontade humana de quem a produziu. É por isso que ela não é
   fungível: usar essência alheia seria usar a vontade de outra pessoa.

**A regra exata, enunciada para o sistema (o que é transferível, o que não é, e o que
acontece quando alguém tenta):**

| Forma | Quem a produz | Transferível? | O que se faz com ela |
|---|---|---|---|
| **Conta de essência imortal** (uva verde · tâmara vermelha · lichia branca · damasco amarelo) | O **núcleo de origem** da própria abertura do cultivador | **A posse física, sim. O uso, não.** | Só o dono a queima. Nas mãos de outro imortal é um objeto inerte |
| **Pedra de essência imortal** | **Só o Tribunal Celestial** — não existe fonte natural | **Sim, integralmente.** É a moeda | Qualquer imortal a converte **na essência do próprio rank** |

- **Contas são pessoais.** Cap. 666: *"immortal essence stones are worth more than green
  grape immortal essence, the former is used as currency while **the latter can only be
  used by an individual**."* É exatamente a tese do usuário, dita pelo texto.
- **A pedra é a ponte.** Ela é a forma neutra: cap. 683, *"he used almost all his immortal
  essence stones and **converted them into his** green grape immortal essence"*; cap. 666,
  um imortal zumbi de abertura morta *"could extract immortal essence from immortal
  essence stones and turn them into **his own** green grape immortal essence"*.
  **Conversão é sempre para a essência do próprio rank de quem converte** — cap. 1468:
  *"Fang Yuan was not rank eight, he could not produce rank eight immortal essence at
  all."*
- **Quem produz as pedras.** Cap. 466: *"only the heavenly court could produce immortal
  essence stones."* Cap. 2298 explica o mecanismo e por que só saem no grau 6. Isso faz da
  única moeda transferível do mundo um **monopólio político**, não um recurso natural — e
  é a alavanca de campanha mais subaproveitada que existe aqui.

**As quatro exceções — e só estas quatro.**

1. **Espírito da terra / espírito celestial do falecido.** Cap. 638: Fang Yuan herdou a
   terra abençoada de Hu Immortal com muita uva verde dentro, e *"**only the land spirit**,
   Little Hu Immortal, could use this immortal essence"*. O espírito da terra é feito da
   obsessão do morto — é a vontade dele que continua ali. Cap. 407 mostra o uso prático: um
   imortal escapa porque *"with the help of land spirit to use the blessed land's immortal
   essence"* seu Gu é ativado.
2. **Casa de Gu Imortal.** Cap. 971: *"Giant Sun's immortal essence could not be used by
   Fang Yuan himself, **but the Immortal Gu House could absorb it**. Immortal Gu Houses
   could absorb immortal essence of others... **This was the fundamental characteristic of
   Immortal Gu House — integrating the power of a group of immortals into one!**"*
   (Ver achado 3 — é a peça de design mais valiosa desta revisão.)
3. **Essência acompanhada de um fragmento da vontade do dono.** Cap. 943: antes de morrer,
   Su Xian Er deixou à filha *"a sum of immortal essence, as well as this familial
   emotion"*, e **é a soma dos dois** que permite o uso: *"It was because of the familial
   emotion **and** immortal essence that Hei Lou Lan could activate Immortal Gu while she
   was still a mortal."* Não é exceção à regra — é a regra: a vontade veio junto.
4. **Possessão do corpo do dono.** Cap. 789: *"after possession, **the immortal aperture
   would be the target's immortal aperture**"* — você não recebe a essência dele, você
   passa a ocupar a fábrica.

**As duas passagens que parecem contradizer, e não contradizem** — resolvê-las é metade do
valor deste achado, porque elas são exatamente o que um leitor atento vai levantar:

- **Cap. 460, as contas jogadas para dentro do buraco.** Cinco imortais atiram contas de
  uva verde, uma a uma, carregadas por um Gu voador, dentro de uma terra abençoada sitiada.
  Lendo a passagem inteira: a conta **explode ao entrar** e *"caus[a] the immortal essence
  in Lang Ya blessed land to be expended"*. **Não é transferência — é guerra de atrito.**
  Cada conta que o atacante queima obriga a terra a queimar da reserva dela; ganha quem
  tiver mais reserva. (O sistema, aliás, **já modela isso corretamente** em
  `🗝️ Terra Abençoada`, na regra de cerco: *"os atacantes despejam Essência Imortal ou
  Pedras de Essência Imortal contra a Reserva"*. A regra está certa; falta só dizer que
  esse é o **único** uso ofensivo direto de uma conta contra outro imortal.)
- **O Tribunal Celestial que "dá" abertura fantasma, Gu Imortais e essência imortal.**
  Cap. 1252: a abertura fantasma (*phantom aperture*) *"could only store immortal essence,
  Gu worms and will, but could not be managed and developed like normal immortal
  apertures. It also had to be replenished at set intervals of time"*. É um **armazém
  emprestado, sem fábrica**: quem o recebe depende de reabastecimento periódico do
  Tribunal justamente porque não produz nada. Não contradiz a regra — é a demonstração mais
  cara dela.

**O que acontece quando alguém tenta usar essência alheia:** nada. O Gu não ativa. E
**mesmo assim tomar a essência do inimigo é uma das jogadas mais fortes do mundo** —
cap. 638, Fang Yuan corre atrás da essência de um Venerável que ele *sabe* que não poderá
usar: *"I can't use it, but as long as I seize all this immortal essence, the power of
Giant Sun's will will drop down to twenty to thirty percent!"*. E cap. 2271: *"the most
drastic method against immortal zombie Bo Qing was to **take away all of his rank eight
immortal essence**"*. **Roubar essência não é saque: é desarmamento.**

**Onde isso mora na nossa Bíblia:** `06 - Economia e Vida/11 - Economia Imortal.md`,
`06 - Economia e Vida/02 - Pedras Primordiais.md`, `04 - Mundo/10 - Viver Dentro da
Abertura Imortal.md`, e a pesquisa bruta com as citações em
`_pipeline/PESQUISA-essencia-imortal.md`.

**Onde entraria no sistema:**
1. `02 — Caminho do Cultivo/🪜 Ranks e Estágios.md` — **corrigir a frase** "tem que
   comprar, roubar ou receber" para "**tem que subir de rank**: comprar pedras e convertê-las
   na essência do próprio rank é a única via, e é o que empobrece quem sobe".
2. `02 — Caminho do Cultivo/💠 Economia das Pedras Primordiais.md`, seção "Pedra de
   Essência Imortal" — acrescentar a distinção **conta (pessoal) × pedra (moeda)** e a
   tabela das quatro exceções. É a caixa natural.
3. `03 — Gu/⛓️ Espólio de Gu Imortal.md` — na lista "Matar um Imortal continua valendo
   muito", acrescentar a linha: *as contas de essência dele **não** entram no espólio
   utilizável, mas tomá-las é o golpe mais duro que se pode dar num imortal.*
4. `00 — Portal/📔 Dicionário do Sistema.md` — a entrada **Pedra de Essência Imortal** hoje
   diz "1 = uma unidade de essência de rank 6". Certo, mas incompleto: acrescentar que a
   pedra circula e a conta não.

**Por que recomendo (o efeito prático na mesa).** Sem esta regra, a economia de rank 6+
desmonta em uma sessão: o jogador rico compra essência do NPC e o custo de ativação de Gu
Imortal — que é o único freio da fase imortal — deixa de existir. Com ela, três coisas
acontecem de graça:

- **Essência vira orçamento pessoal, não dinheiro.** Cada imortal tem uma torneira própria
  (a abertura) e um tanque próprio. Ninguém socorre ninguém com essência. É isso que faz
  cada ativação doer.
- **O grupo precisa de um motivo mecânico para agir junto** — e a obra dá exatamente um:
  a Casa de Gu Imortal (achado 3).
- **Aparece um alvo de assalto que não é loot.** Queimar o estoque do inimigo passa a ser
  objetivo tático legítimo, com precedente canônico, e não dá item nenhum ao grupo — o que
  é ótimo para o balanceamento.

> [!note] Para o agente executor
> Esta regra é **densa mas curta**: cabe numa tabela de duas linhas mais um callout de
> quatro exceções. Não é preciso escrever uma nota nova. E ela **retira** complexidade do
> sistema em vez de acrescentar, porque fecha a porta de "comprar essência", que hoje está
> aberta e não tem preço definido.
