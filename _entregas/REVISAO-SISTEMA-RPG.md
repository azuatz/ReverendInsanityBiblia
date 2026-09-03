# Revisão externa do sistema de RPG

> Documento de trabalho de um revisor externo. Destinatário: o agente que mantém
> `/home/azuatz/Documentos/REVEREND INSANITY/`. Este revisor **não editou nada** no
> sistema — só leu.
>
> **Status: FECHADA.** Dez achados numerados, mais as duas seções finais
> ("o que eu não recomendo acrescentar" e "dúvidas legítimas de escopo").
> Escrita em duas sessões; a primeira produziu o método, o panorama e o achado 1.

## Como esta revisão foi feita

**Três acervos, três papéis.**

1. **O sistema** — `/home/azuatz/Documentos/REVEREND INSANITY/` (842 arquivos, 39 MB).
   Objeto da revisão. Lido: `CLAUDE.md`, `00 — Portal/`, `01 — Fundação/`,
   `02 — Caminho do Cultivo/`, `03 — Gu/`, `04`, `05`, `06`, `07 — Terras e Facções/`,
   `08 — Crônicas/`, `11 — Sementes/`, e varreduras por termo em todos os 842 arquivos.
   As pastas `03`–`06` foram cobertas em duas passadas: um mapa de lacunas transversais
   feito antes (`_entregas/MAPA-SISTEMA-RPG-lacunas.md`, oito lacunas) e a releitura
   dirigida dos arquivos que ele apontou. **Seis daquelas oito lacunas viraram achado
   numerado** (1 e 8 → achado 3 e achado 8; 2 e 7 → achado 8; 3 e 4 → achados 2 e 7);
   as duas restantes (5, Golpe Matador Coletivo; 6, Grimório nos ranks 7-9) estão
   tratadas na seção final de dúvidas de escopo, com o motivo de eu não as promover.
2. **A Bíblia de Sistema** — `/home/azuatz/Documentos/ReverendInsanityExpert/`
   (206 notas escritas a partir da leitura integral da obra). Base de comparação.
   O material mais novo dela — as seções "A camada escondida" das notas de Caminho,
   `08 - Eventos e Cenarios/`, `11 - Forcas e Organizacoes/`, e as notas de combate,
   ferimento e perda de cultivo — foi cruzado com o sistema nesta segunda passada, e é
   a origem dos achados 4 a 10.
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

---

### 2. Reancorar um Gu a uma região nova **é canônico** — o sistema o marca como invenção própria e diz que a obra não fala disso

- **Categoria:** erro *(de atribuição de canonicidade — e o mais fácil de corrigir da lista)*
- **Tamanho do trabalho:** pequeno — trocar dois selos, reescrever um parágrafo, apagar uma pendência de design

**O que está no sistema hoje.** `03 — Gu/🗺️ Supressão Regional.md` traz um callout explícito:

> Só a queda de **um rank** vem do romance. As duas extensões abaixo — **Gu de rank 1 pararem de
> funcionar** e o **procedimento de reancoragem** (reclusão + pedras) — são **✍️ adaptação
> autoral** deste sistema. (…) não invoque "é assim no cânone" para defendê-las.

E, mais abaixo, a seção "Reancorar ✍️" abre com uma negativa:

> **Mecanismo autoral** — o romance diz que a supressão existe, **não como desfazê-la**.

**O que a obra diz.** O **capítulo 477** enuncia a regra e **as duas formas de desfazê-la**, em
quatro frases seguidas, no mesmo parágrafo:

> *"The heaven and earth of the five regions were different, whether it were **Gu worms or Gu
> Masters**, once they went into other regions, they would be suppressed.*
>
> *But different from Gu worms, human is the spirit of all living beings and had great
> intelligence and adaptability. **As long as a few years went by, Gu Masters could completely
> adapt to the environment and obtain the recognition of the region, no longer facing
> suppression.***
>
> *And for the Gu worms to not be suppressed, **Fang Yuan refined the Gu at northern plains. No
> matter where the materials were from or whatever Gu worms were used, the moment the Gu
> refinement was completed, the new (…) Gu was born in northern plains and obtained northern
> plains' recognition, not suffering from the suppression.***"

Três regras saem daí, e as três são jogáveis:

1. **A pessoa e o bicho são suprimidos separadamente.** A supressão não é do arsenal: é do Mestre
   Gu **e** de cada Gu, por vias diferentes.
2. **O humano se adapta sozinho, de graça, em alguns anos.** Não custa pedra, não custa teste:
   custa **tempo de calendário**. O termo canônico é ==reconhecimento da região== (*recognition
   of the region*) — vale adotá-lo, porque nomeia o estado e dispensa explicação.
3. **O Gu se reancora sendo refinado ali.** E a cláusula que faz a regra funcionar na mesa é a
   segunda metade da frase: **a origem do material não importa**. O que decide a "nacionalidade"
   de um Gu é **onde o refino terminou**. Um Gu comprado na Fronteira Sul e elevado de rank nas
   Planícies do Norte nasce norte-plainense.

**A consequência que mais interessa: isso desarma a pendência de design do rank 1.** O sistema
carrega um callout admitindo que "Gu de rank 1 não funcionam fora da região" desarma a mesa
inteira, já que todo grupo começa no rank 1, e que a decisão está em aberto. A obra oferece a
saída sem precisar afrouxar nada: **um grupo de rank 1–2 que muda de região refina de novo os
próprios Gu no destino** — que é exatamente o que um personagem de rank baixo faz o tempo todo
de qualquer forma, porque refino é a atividade central da fase mortal. A viagem deixa de ser
"perdi meu arsenal" e vira "tenho um lote de refinos para fazer nas próximas semanas", que é uma
cena de downtime, não uma punição. O procedimento que o sistema já escreveu (`refino dirigido`,
teste estendido de 2 sucessos, CD 15) **serve como está** — só precisa deixar de ser autoral.

**O que muda na regra escrita, em concreto:**

| Linha do sistema | Hoje | Deveria ser |
|---|---|---|
| Queda de um rank fora da região | 📕 canônico | 📕 canônico *(sem mudança)* |
| Reancorar por **refino no destino** | ✍️ autoral, "a obra não diz" | **📕 canônico** — é literalmente o método do cap. 477 |
| Reancorar por **reclusão + pedras** | ✍️ autoral | 🔧 adaptado — a obra tem o efeito (adaptação por permanência), o sistema comprimiu o prazo |
| Adaptação do **personagem** (não dos Gu) | não existe | **📕 canônico** — alguns anos morando ali, e o Mestre Gu deixa de ser suprimido |
| "Gu de rank 1 param de funcionar" | ✍️ autoral, com pendência aberta | continua ✍️ — mas agora com uma saída canônica ao lado, e a pendência pode fechar |

**Onde isso mora na nossa Bíblia:** `04 - Mundo/04 - As Cinco Regiões.md` (a escada de três
degraus de conhecimento sobre a parede, e a explicação da veia de terra) e
`02 - Gu/05 - Refino de Gu.md`.

**Onde entraria no sistema:** dentro de `03 — Gu/🗺️ Supressão Regional.md` e em nenhum outro
lugar. Trocar o callout "o que é cânone e o que é nosso", reescrever a abertura da seção
"Reancorar", acrescentar duas linhas sobre a adaptação do personagem, e **apagar** o callout de
pendência de design (ou convertê-lo em "resolvido pelo cap. 477").

**Por que recomendo.** Um sistema que se dá ao trabalho de marcar 📕/🔧/✍️ tem esse selo como
ativo de credibilidade. Uma regra marcada como invenção quando ela é cânone corrói o selo em
ambas as direções: o mestre desconfia do que é canônico e não confia no que está marcado. E, de
quebra, fecha a única pendência de design do vault que admite, por escrito, desarmar a mesa.

> [!note] Para o agente executor
> A negativa que o sistema escreveu ("o romance diz que a supressão existe, não como desfazê-la")
> é o tipo exato de afirmação que só se pode fazer depois de buscar no texto-fonte. Vale como
> aviso de método: a obra grafa tudo em minúsculas e a passagem em questão não contém a palavra
> "suppression" perto de "region" — ela foi encontrada por `grep -i "refined in.*region"`.

---

### 3. A Casa de Gu Imortal é o **único** dispositivo do mundo que soma o poder de vários imortais — e o empréstimo de Gu é o único outro

- **Categoria:** profundidade que vale a pena *(e é a resposta que o achado 1 deixou pendurada)*
- **Tamanho do trabalho:** pequeno — três parágrafos e uma tabela, dentro de notas que já existem

**O que está no sistema hoje.** O motor está construído e é bom. `03 — Gu/🔷 Formações de
Gu.md` traz a Casa-Gu tripulada com três estações (mortal) e cinco (imortal, rank 6+), rank
operante = `rank da Casa − estações vazias`, casco ablativo, livro-caixa embutido — este último,
aliás, **é canônico** e o sistema acertou sem citar a fonte (cap. 818: *"This Immortal Gu House
will record how much immortal essence you put in"*). E `03 — Gu/📖 Catálogo de Gu.md` traz as
**12 Casas canônicas** com efeito e manutenção.

O que falta é a frase que explica **por que a Casa existe no mundo**, e ela é a peça de design
mais valiosa desta revisão inteira.

**O que a obra diz.**

- **Cap. 971**, dito enquanto um imortal olha para uma montanha de essência que ele não pode
  queimar: *"Giant Sun's immortal essence could not be used by Fang Yuan himself, **but the
  Immortal Gu House could absorb it**. Immortal Gu Houses could absorb immortal essence of
  others… **This was the fundamental characteristic of Immortal Gu House — integrating the power
  of a group of immortals into one!**"*
- **Cap. 1625** fecha a lista: *"The only exception was Immortal Gu Houses as **immortal essence
  from any source** could be used in them."*
- **Cap. 2297** dá o mecanismo: um Gu refinado perde a capacidade de puxar energia do ambiente e
  passa a viver de essência com vontade humana dentro. E então: *"If a Gu worm is **lent out**,
  the Gu worm can still use others' primeval essence or immortal essence. For example, an
  Immortal Gu House can use the stored immortal essence of Gu Immortals inside."*

**A regra completa, em duas linhas.** Como a essência é feita da vontade de quem a produziu
(achado 1), existem exatamente **duas** maneiras canônicas de o poder de duas pessoas virar um
poder só:

| Via | Como funciona | O que ela custa |
|---|---|---|
| **Emprestar o Gu** | O dono entrega o bicho. A vontade humana dentro do Gu **reconhece o portador novo**, que passa a ativá-lo **com a própria essência** | O dono fica sem o Gu, e o Gu passa a responder a outro. É confiança, não é cópia |
| **A Casa de Gu Imortal** | A Casa queima **essência de qualquer origem** — a da tripulação, a comprada, a **saqueada de um cadáver**, a de um Venerável morto há eras | A Casa é imóvel ou lenta, come parada, e tem um alvo prioritário: o Gu de Permanência |

E o corolário que fecha o circuito aberto no achado 1: **as contas de essência tomadas de um
imortal morto, inúteis nas mãos de qualquer personagem, viram combustível dentro de uma Casa.**
O espólio que não serve para nada tem exatamente **um** destino no mundo, e é este.

**Três detalhes canônicos que o sistema pode absorver de graça:**

- **A economia de combustível de uma Casa é contável em contas, não em porcentagem.** Cap. 640:
  um Pavilhão de rank 7 foi deixado com **vinte contas** de essência de tâmara vermelha; anos de
  operação depois, **restavam cinco** — e a dona diz, com todas as letras, que não dá para virar
  a batalha com ele. Isso é uma barra de combustível pronta para a mesa: uma Casa herdada vem com
  um número de contas, e esse número é o relógio do arco.
- **Nem toda Casa tem Gu de Permanência.** Cap. 2049 registra uma Casa do caminho da terra que
  **não tem Gu Imortal-núcleo nenhum** — o núcleo dela são golpes matadores imortais. E cap. 1989
  generaliza: *"the essence of an Immortal Gu House was immortal killer moves."* Ou seja, a regra
  "matar o Gu de Permanência apaga a Casa" tem uma classe inteira de exceções, e ela é justamente
  a classe que um mestre quer quando precisa de uma Casa que não morra num tiro certeiro.
- **A tripulação morta continua servindo.** Cap. 2062: uma Casa do Tribunal Celestial luta em
  força plena nas mãos de um operador de cultivo baixo porque carrega dentro de si a essência de
  rank 8 **e as vontades dos comandantes anteriores**. Uma Casa antiga é, mecanicamente, um
  time de mortos.

**E a regra que faltava para construir uma** (o mapa de lacunas registra que o sistema tem
manutenção diária e nenhuma regra de aquisição ou de refino). A obra dá o portão em uma frase,
cap. 559: *"he was only a mortal Gu Master, **one had to be at least a rank eight Gu Immortal to
refine the Immortal Gu house**"* — a Casa em questão era de rank 8. A regra generaliza sozinha e
é a mais barata possível:

> **Refinar uma Casa de rank N exige ser Imortal de rank N.** Não há atalho de grupo: seis rank 6
> não refinam uma Casa de rank 8. É por isso que quase toda Casa em circulação é **herdada,
> tomada ou encontrada**, e não construída — e é por isso que o Gu de Permanência de uma Casa
> famosa costuma ter o nome de quem a fez gravado na história.

Isso também explica a diferença entre **refinar** uma Casa e **pilotá-la**: o `🔷 Formações de Gu`
já permite que a tripulação seja de rank menor que a Casa (com o rank operante caindo), e isso
está certo — o portão de rank vale para quem a **faz**, não para quem a usa. Cap. 2062 mostra o
extremo: um operador de cultivo baixo tirando força plena de uma Casa que carrega essência de
rank 8 dentro.

**Dois reparos de coerência interna, de uma linha cada** (levantados no mapa de lacunas):

1. `🔷 Formações de Gu.md` diz "**Uma Casa-Gu por campanha.** Não é sugestão: é a regra",
   enquanto o Catálogo lista 12 em circulação. As duas coisas são compatíveis se a frase disser
   **"uma por grupo de jogadores"** — que é o que ela quer dizer. Como está, lida por um mestre
   novo, ela parece afirmar que só existe uma Casa no mundo.
2. As 12 Casas do Catálogo não têm ficha defensiva, e **não precisam de uma**: o motor de
   Formações já dá `Vitalidade 40 × M`, `RD 3 × M` e `Defesa 10 + rank`. Basta uma linha de
   remissão no topo da tabela das Casas. É remissão, não conteúdo novo.

**Onde isso mora na nossa Bíblia:** `02 - Gu/08 - Formações de Gu.md`,
`02 - Gu/12 - Gu Imortais.md`, `06 - Economia e Vida/11 - Economia Imortal.md`.

**Onde entraria no sistema:**
1. `03 — Gu/🔷 Formações de Gu.md`, seção "🌌 A versão imortal" — o parágrafo "**essência de
   qualquer origem**", que é a única regra nova de verdade, mais o contador de contas.
2. `03 — Gu/⛓️ Espólio de Gu Imortal.md` — a linha que liga o saque inútil à Casa.
3. `03 — Gu/🪱 Gu.md` (ou `📖 Catálogo`) — o empréstimo de Gu, três linhas.

**Por que recomendo.** O sistema já tem o motor; o que ele não tem é o **motivo**. Sem esta
regra, a Casa-Gu é mais um veículo. Com ela, a Casa é a resposta mecânica para a pergunta que o
achado 1 cria — *se ninguém pode financiar ninguém com essência, por que estes quatro imortais
andam juntos?* — e o espólio morto de um inimigo passa a ter destino. É a peça que transforma
duas regras restritivas em uma decisão de grupo.

> [!note] Para o agente executor
> O empréstimo de Gu é pequeno e resolve um problema de mesa que aparece cedo: o jogador que
> pergunta "posso dar meu Gu de cura pro tanque?". A resposta canônica é **sim, e ele ativa com a
> essência dele** — o que é generoso e ainda assim tem preço, porque quem empresta fica sem.

---

### 4. O Fantasma de Fera: o sistema acertou metade do gatilho e fechou a porta errada

- **Categoria:** erro *(parcial, e o mais delicado da lista — a regra do sistema tem âncora canônica de verdade, mas enuncia uma negativa absoluta que a obra desmente na mesma cena que ela cita)*
- **Tamanho do trabalho:** pequeno — uma tabela trocada e duas frases reescritas, dentro de uma nota que já existe

**O que está no sistema hoje.** `02 — Caminho do Cultivo/💪 Caminho da Força.md`, no callout
"👻 Fantasma de Fera", declarado **📕 canônico, cap. 280-281 e 285-286**:

> **O gatilho não é o rank — é a densidade, e o resto é sorte.** (…) Ela transborda quando você
> acumulou muita força **da mesma fera**, e **não transborda nunca quando a sua força vem de
> bichos diferentes**: o poder está lá, só não está junto o bastante pra tomar forma.

**Onde o sistema acertou, e vale dizer primeiro.** A ideia de que acumulação temática aumenta a
chance é **canônica e literal**. Cap. 319:

> *"The combination of dragon guts Gu, dragon travel tiger steps Gu, and dragon-elephant Gu
> formed a **resonance of Dao marks due to their similar law fragments**; this **greatly raised
> the probability** of bringing out his dragon-elephant phantom."*

Note o que ressoa ali: **três Gu diferentes de uma mesma família de lei** (todos "dragão"), não
três cópias do mesmo Gu. É ressonância de tema, não empilhamento de duplicata.

**Onde o sistema errou.** A negativa absoluta — *"não transborda nunca quando a sua força vem de
bichos diferentes"* — é desmentida no cap. 281, que é um dos capítulos que o próprio callout
cita. O personagem daquela cena tem **força de dois javalis e um crocodilo** (duas feras
diferentes) e **manifesta o fantasma**: *"Tang Xiong got lucky and was able to unleash the beast
phantom."*

E, junto com a negativa, o sistema perdeu **o gatilho que a obra de fato dá**, que é o estilo do
golpe. O mesmo personagem explica:

> *"I have the strength of two boars and a crocodile; **boar strength is good at charging attacks
> and crocodile strength is good at bite attacks**, but I have yet to acquire the bear strength.
> **I can't bring out the beast phantom by using my fists or palms**"* — cap. 281.

Cap. 280 completa: *"**As their proficiency in the Gu increases**, sometimes, the beast phantom
appears in battle (…) the attack method is very rigid, **only when using a specific attack style
can the beast phantom be summoned, it is easy to evade**."* Cada fera tem o seu movimento — urso
no tapa, javali na investida, crocodilo na mordida, cavalo na corrida — e quem não tem o Gu do
urso **não tira fantasma de um soco**, por mais que soque.

E o cap. 297 fecha a porta do empilhamento de **cópias**, que é justamente o que a regra atual
premia:

> *"The rank three all-out effort Gu can only summon **one** beast phantom at a time. After it
> reaches rank four, there are stronger beast phantoms available. Thus, **the strength of two
> boars would be redundant and repetitive.**"*

**A regra canônica completa, para o sistema:**

| Peça | O que a obra diz | Capítulo |
|---|---|---|
| Manifestação espontânea | Rara, movida por **proficiência** no Gu, e **só sai no estilo de golpe daquela fera** | 280, 281 |
| Ressonância | Vários Gu de **famílias de lei parecidas** (não cópias) **elevam muito a probabilidade** daquele fantasma | 319 |
| Cópias do mesmo Gu de fera | **Desperdício declarado** — soma força bruta, mas o segundo javali não vira fantasma nenhum | 297 |
| Garantia | O **Gu do Esforço Total** invoca com 100% de taxa e sob controle da vontade — o sistema já modela isso | 285 |
| Simultâneos | O corpo tem teto; o documentado é **oito**, atingidos com Gu que abrem mais torneiras conforme o usuário se fere | 293, 319 |
| Elevar o teto | **Gu do Tendão de Aço**, uso contínuo por **dois a três meses** | 293 |

**O conserto, em duas linhas de texto:**

1. Trocar *"da mesma fera"* por **"da mesma família de lei"** — e trocar a tabela "Gu de Corpo da
   mesma fera → o Fantasma sai em" por uma tabela de **famílias temáticas**. Isso mantém intacta
   a intenção de design do sistema (premiar a especialização) e passa a ser canônico de verdade:
   o caso do dragão é exatamente isso.
2. Apagar o **"nunca"** e pôr o gatilho de estilo no lugar dele: com feras diferentes o fantasma
   sai, **mas só quando o golpe é do estilo daquela fera**. Um arsenal variado dá cobertura de
   estilos; um arsenal ressonante dá probabilidade alta num estilo só. **As duas construções
   passam a existir**, e a escolha entre elas é a decisão de personagem do Caminho.

**Dois detalhes canônicos que o sistema pode aproveitar de graça** (cap. 291 e 297):

- **Fantasma é bagagem, não só ganho.** Um cultivador removeu de propósito todos os fantasmas do
  corpo **para baratear o custo de essência de um Gu de outro Caminho**. Livrar-se de um leva
  **pelo menos dezenove dias** e um método específico. Isso dá ao mestre uma alavanca real para o
  jogador que montou o bestiário errado — e é a única aparição de "marca de dao cobra preço" no
  patamar mortal (ver a seção final: **não** recomendo importar marcas mortais como subsistema).
- **Fantasmas não custam essência** enquanto apenas amplificam os golpes — o que o sistema **já
  acertou** na ficha do Gu dos Fantasmas de Guarda.

**Onde isso mora na nossa Bíblia:** `03 - Paths/04 - Strength Path.md`, seção "A camada
escondida" — com o teto de oito, o Gu do Tendão de Aço e a contraindicação dele (tendão de aço
**atrapalha a própria cura**, ver achado 6).

**Onde entraria no sistema:** só em `02 — Caminho do Cultivo/💪 Caminho da Força.md`.

**Por que recomendo.** Porque hoje a regra manda o jogador de Força comprar **três Gu de javali**,
e a obra manda comprar **um javali, um urso e um crocodilo** — ou **três Gu de dragão**, se ele
quiser apostar na ressonância. A correção não acrescenta mecânica: troca um eixo por dois, e cada
um deles produz um personagem diferente. E devolve ao selo 📕 uma frase que hoje o usa
indevidamente.

> [!warning] Para o agente executor — este é o achado com maior risco de eu estar errado
> A frase *"não transborda nunca com bichos diferentes"* pode ter saído de uma leitura defensável
> do cap. 319 (ressonância), e não de um erro de leitura. Se for o caso, o conserto continua
> valendo, porque a **negativa absoluta** é o que o cap. 281 desmente — não a ideia de
> ressonância, que está certa. Trate isto como um ajuste de fraseado com consequência de compra,
> não como uma refutação da regra inteira.
### 5. O cardápio de travas: a resposta canônica para "e por que os poderosos não resolvem isso?"

- **Categoria:** buraco que atrapalha jogar
- **Tamanho do trabalho:** pequeno — uma lista numerada dentro de uma nota que já existe

**O que está no sistema hoje.** `08 — Crônicas/🎬 Como Criar Suas Sessões.md` e
`🛠️ Como Criar Sua Lore.md` são bons guias de autoria e cobrem estrutura de cena, calibragem,
ritmo, gerador de emergência e os erros que o sistema pune. Nenhum dos dois responde à pergunta
que **trava um mestre novo mais do que qualquer outra** neste cenário específico: *se existem
imortais de rank 8 no mundo, por que este problema é dos meus jogadores de rank 3?*

O sistema tem meia resposta espalhada — `🗺️ Supressão Regional` explica por que exércitos não
invadem, e `🗺️ Arco da Campanha` organiza eventos por ato. Falta a ferramenta.

**O que a obra dá.** Ela não trata isso como conveniência narrativa: são **restrições contratuais
do mundo**, ditas com todas as letras, e a Bíblia as reuniu em quinze. As mais imediatamente
utilizáveis, com o capítulo conferido:

1. **Ser fraco é a credencial de entrada.** Nas grandes zonas selvagens, a aura de um Gu Imortal
   provoca as feras mais perigosas do mundo; a de um mortal, não. Cap. 781, dito por um imortal
   que está do lado de fora esperando: *"they are all mortal Gu Masters, **they have weak auras
   and do not attract the attentions of the desolate beasts** (…) If we go, **our Gu Immortal
   auras would leak and cause the resistance of desolate beasts**."* Os poderosos **mandam
   mortais na frente e esperam do lado de fora** — que é literalmente a premissa de uma
   expedição de jogadores.
2. **A zona que destrói quem é grande demais.** Cap. 961: quanto mais fundo um imortal entra,
   mais fraco fica — *"his immortal aperture would be destroyed before he took fifty or sixty
   steps"*. O resultado canônico foi uma guerra de cem dias travada **só por mortais de rank 3 a
   5**, com dezenas de imortais parados a dez mil li de distância apostando de fora.
3. **A supressão dentro da herança.** Heranças remodelam o interior para nivelar quem entra: uma
   admite **um único Gu de rank 1 e nada mais**; outra sela todos os Gu, inclusive os de
   movimento, e obriga a subir com o corpo.
4. **O lugar onde nada funciona.** Existe domínio em que nenhum Gu funciona e nenhuma abertura
   abre: a briga vira corpo a corpo, e um rank 6 segura um rank 8.
5. **A proibição institucional.** Um dos maiores terrenos de herança do mundo **proíbe imortais
   de entrar** — e é exatamente por isso que suas heranças sobreviveram intactas por milênios.
6. **O espírito da terra que se autodestrói.** Ninguém toma uma Terra Abençoada à força porque o
   espírito dela pode se matar levando tudo junto. Por isso as grandes seitas mandam discípulos
   jovens em vez de irem elas mesmas. *(O sistema **já tem** essa peça em `🧿 Espíritos da
   Terra` — falta só ela aparecer como trava de autoria.)*
7. **O contrato entre os poderosos.** Quando os fortes não podem entrar, eles **apostam**: cada
   imortal aposta bens, e a aposta define **de que rank pode ser o seu peão e quando ele entra**.
   Trapaça custa confisco. Isto transforma "os PJs são fracos" em "os PJs são as peças de um
   jogo de apostas de gente enorme", que é uma premissa de campanha inteira.
8. **A trégua obrigatória.** No maior torneio de artesãos do mundo, a única regra absoluta é não
   lutar e não matar: criminosos procurados se inscrevem abertamente, mortais e imortais
   competem nas mesmas provas — e imortais escondem o próprio rank porque **perder para um
   mortal acontece de verdade**.
9. **O custo proporcional.** Existe uma estrada em que cada passo consome força, vontade e
   essência **proporcionalmente à fundação de quem anda**. A dificuldade é a mesma para todos, e
   por isso mortais frequentemente ultrapassam imortais.
10. **A janela em que os fortes estão dormindo.** Numa maré de energia, toda abertura imortal
    fica instável e o dono é forçado a se recolher — e **quanto mais forte a fundação, mais
    tempo leva a recuperação**. O mundo pertence literalmente aos fracos enquanto dura.
11. **A fronteira que pune os grandes.** Ver achado 7 — atravessar uma parede regional fere quem
    é grande, e perseguidores poderosos simplesmente não seguem alguém através do mundo.
12. **A ocupação dos poderosos.** A mais banal e a mais reutilizável: três potências empatadas
    numa disputa, uma região inteira olhando para um refino que dura sete dias, uma guerra em
    quatro frentes — e ninguém olhando para o seu grupo.

*(A Bíblia lista quinze; estas doze são as que sobrevivem sem depender de um lugar nomeado do
romance. As outras três são específicas de cenários canônicos e ficam de fora pela política de
"não use enredo" que o próprio sistema adota em `🌍 Terras e Facções`.)*

**A regra de autoria que essa lista destrava, e que é o verdadeiro produto:**

> **Escolha a trava antes de desenhar o evento.** A trava costuma sugerir sozinha o formato da
> sessão: "aura fraca é a credencial" já é uma expedição; "os fortes apostam" já é uma
> competição com patrocinadores; "o lugar onde nada funciona" já é um cenário de sobrevivência
> sem arsenal.

**Onde isso mora na nossa Bíblia:** `08 - Eventos e Cenarios/01 - Visão Geral dos Eventos.md`,
seção "As travas" — com o link para o cenário canônico de cada uma.

**Onde entraria no sistema:** `08 — Crônicas/🎬 Como Criar Suas Sessões.md`, como seção nova
logo depois de "Como calibrar dificuldade"; e uma remissão de uma linha em
`🛠️ Como Criar Sua Lore.md`. **Não** merece nota nova — o valor está em estar ao lado do
procedimento de autoria.

**Por que recomendo.** É a resposta mais barata desta revisão para o problema mais caro de um
cenário de cultivo: a diferença de escala. Sem ela, o mestre novo ou inventa desculpa (e os
jogadores sentem) ou baixa a escala do mundo (e perde o gênero). Com ela, ele escolhe uma linha
de uma lista de doze, e a desculpa vira **regra do mundo que os jogadores reconhecem**. E ela
não acrescenta uma única mecânica: é ferramenta de autoria pura.

---

### 6. A cura não tem afinidade de Caminho — e é a peça que falta para o motor de Marcas de Dao fechar

- **Categoria:** profundidade que vale a pena *(com um pedaço de buraco: o sistema declara, por escrito, que teme a cura resolver tudo — e a obra entrega o freio pronto)*
- **Tamanho do trabalho:** pequeno — uma regra de duas linhas e um callout

**O que está no sistema hoje.** `01 — Fundação/❤️ Recursos e Dano.md`:

> `Cura = M d8` (`M` = rank do Gu de cura). **Nada soma no pool de cura:** nem **B**, nem Níveis
> de Potência.

E, em `08 — Crônicas/🎬 Como Criar Suas Sessões.md`, o mestre é avisado do risco sem receber
ferramenta para contê-lo:

> **Deixar a cura resolver tudo.** A cura foi calibrada pra devolver mais ou menos o que um golpe
> tira. Se sua mesa está curando pra fora de todo problema, provavelmente há Gu de cura demais em
> circulação.

Ou seja: hoje a cura é um número indiferente a **quem cura**, a **quem é curado** e a **o que
causou o ferimento**. O único freio disponível ao mestre é tirar Gu de cura de circulação — que é
uma alavanca de fora da ficção.

**O que a obra diz.** A cura deste mundo é governada por marcas do Dao, e a regra é enunciada
três vezes, de três ângulos.

**1. O ferimento carrega as marcas de quem o causou, e essas marcas resistem à cura.**
Cap. 717, sobre feras: *"the injuries that desolate beasts cause will have dao marks lingering.
**Injuries involving dao marks were very hard to get rid of, not only did they resist the body's
self healing, they also hindered the use and effect of healing Gu.**"* E cap. 977, sobre golpes
imortais: *"the injuries were filled with dao marks, **how could they be healed by ordinary
mortal Gu?**"*

**2. Curar é um procedimento de dois passos, não um.** Cap. 718 descreve o método completo de um
curandeiro competente: *"he **first used large numbers of Gu worms to eliminate the dao marks** of
star path, wind path, dark path and other paths that had filled the wounds, **only then** did he
use healing Gu worms which showed visible effects."* Primeiro se **lava a marca**, depois se cura.
Pular o primeiro passo é gastar a ativação à toa.

**3. Quanto mais forte o ferido, pior ele cura.** Cap. 2221, sobre um dos seres mais poderosos do
mundo: *"Because she had **too many wisdom path and star path dao marks, healing methods of all
other paths were barely usable**. Human path was an exception (…) **This was the lowest
requirement to heal a venerable's injuries.**"* As marcas do próprio ferido rejeitam a cura de
Caminhos alheios. É a regra mais contraintuitiva do cenário e é canônica.

**E a escala de cura é por degraus, não por barra.** Cap. 453: *"After three rounds of healing,
**the heavy injuries had become light injuries while the light injuries were completely
healed**."* Cap. 1469, com um Gu Imortal: *"Fang Yuan's **heavy injuries became light injuries**,
but he had not completely healed."* Uma aplicação = **um degrau para baixo**.

**A regra enunciada para o sistema, no vocabulário que ele já usa.** O sistema tem o eixo de
Caminhos, tem `⚔️ Combate` sabendo o Caminho de cada golpe, e tem `☯️ Marcas de Dao` com atrito
entre Caminhos conflitantes. Isto encaixa sem peça nova:

> [!info] A afinidade é entre **Caminhos de Gu**, não entre personagens
> Isto importa porque `🌏 O Mundo em 10 Minutos` estabelece que, na fase mortal, o Caminho de um
> personagem *"é só uma tendência (…) ele não escolhe formalmente e não trava nada"*. A regra
> abaixo respeita isso: o que se compara é o **Caminho do Gu de cura** contra o **Caminho do golpe
> que causou o ferimento** — dois dados que a ficha do Gu e a do inimigo já publicam. O eixo
> "marcas do próprio ferido" só entra no rank 6+, onde o sistema já conta Marcas.

| Situação | Efeito sobre `M d8` |
|---|---|
| Gu de cura e golpe que feriu, de Caminhos **compatíveis ou neutros** | cura cheia |
| Gu de cura e golpe que feriu, de Caminhos **conflitantes** (a mesma lista que `☯️ Marcas de Dao` já usa para o atrito) | **metade** — ou uma ação prévia de "lavar as marcas" devolve a cura cheia |
| Ferimento causado por **golpe imortal**, curado com **Gu mortal** | **não cura**, ponto. Precisa de um Gu Imortal de cura |
| Ferimento causado por **fera desolada** | conta como Caminho conflitante por padrão — feras gravam marcas na ferida |
| Gu de cura do **Caminho Humano** | coringa: cura sem penalidade contra qualquer Caminho — é a exceção que a obra nomeia |
| Gu de cura do **Caminho do Sangue** | o curandeiro por excelência do cenário |
| **Rank 6+, ferido com muitas Marcas num Caminho** | cura de qualquer outro Caminho cai pela metade **nele**, some a penalidade acima. É a regra "quanto mais forte, pior cura" |

**Por que essa lista é curta de propósito.** Não estou propondo uma matriz de afinidade nova: a
lista de Caminhos conflitantes **já existe** no sistema, dentro de `☯️ Marcas de Dao`. A regra
inteira é *"a cura usa a mesma tabela de conflito que as Marcas já usam"* — uma frase, e o
subsistema fica de pé.

**A linha que resolve o medo declarado do sistema.** *"Ferimento causado por golpe imortal não é
curado por Gu mortal"* é, sozinha, o freio que `🎬 Como Criar Suas Sessões` pediu — e ele é
**canônico, diegético e escalonado**: a cura continua resolvendo tudo o que ela deve resolver
(cap. 516 registra um exército cujos feridos caíram **oitenta por cento em oito dias**, *"a
maioria recuperando a capacidade de lutar"*, com a ressalva decisiva: *"as long as the Gu Masters
were not inflicted with **troublesome injuries**, they could be healed"* — e naquele mesmo mundo
um membro decepado volta a crescer), e para de resolver exatamente o que
não deveria.

**Um detalhe barato que o Catálogo pode absorver.** O Gu de cura de rank 1 do cenário — a folha
de vitalidade, que o Catálogo já tem como **Gu de Grama Curativa** — tem, na obra, um **intervalo
de uma hora por pessoa**: usada uma folha em alguém, nenhuma outra faz efeito nele durante a hora
seguinte. É uma regra anti-empilhamento de uma linha, e ela é o que torna o consumível barato sem
tornar o grupo imortal.

**Onde isso mora na nossa Bíblia:** `02 - Gu/16 - Ferimento, Cura e Fuga.md`, seções "A escala de
ferimentos", "A regra que trava a cura no topo" e "O que a cura não alcança" — esta última uma
lista fechada de oito coisas que a cura não alcança, toda verificada no texto.

**Onde entraria no sistema:**
1. `01 — Fundação/❤️ Recursos e Dano.md`, seção "Cura por Gu" — a tabela acima, como está.
2. `02 — Caminho do Cultivo/☯️ Marcas de Dao.md` — uma linha dizendo que a tabela de conflito
   também rege a cura. É onde a regra pertence conceitualmente.
3. `03 — Gu/📖 Catálogo de Gu.md` — o intervalo de uma hora na ficha do Gu de Grama Curativa.

**Por que recomendo.** Porque dá **função de combate ao eixo mais caro do sistema**. Hoje o
Caminho de um personagem decide o dado de dano e pouco mais; com esta regra, ele decide também
quem consegue remendá-lo — o que faz a composição do grupo importar antes da luta, transforma
"quem é o curandeiro" numa decisão de sessão zero, e dá ao mestre uma escada de gravidade que
sobe com o mundo em vez de subir com o número de Gu que ele nega ao grupo.

> [!note] Para o agente executor
> Se for para adotar **uma só** linha desta seção, adote *"ferimento de golpe imortal não é curado
> por Gu mortal"*. Ela é a que muda mais o jogo por menos texto, e é a que separa "o ato imortal
> começou" de "o ato imortal ainda é o mesmo jogo com números maiores".

---

### 7. As Muralhas Regionais são declaradas como o limitador do ato imortal — e a obra dá todos os números que faltam

- **Categoria:** buraco que atrapalha jogar
- **Tamanho do trabalho:** pequeno — uma tabela e um procedimento de travessia, na nota que já anuncia a Muralha

**O que está no sistema hoje.** `03 — Gu/🗺️ Supressão Regional.md`, seção final, inteira:

> **Gu Imortais não sofrem Supressão Regional.** (…) O que existe pra eles é outra coisa, muito
> maior: as **Muralhas Regionais** (…). Atravessar uma Muralha não é viagem, é **cena de arco**:
> exige preparação, um método específico, ou uma janela em que a Muralha esteja enfraquecida.

Está certo e é bem escrito. Só que é **tudo o que existe**: nenhuma dificuldade, nenhum custo,
nenhuma duração, nenhuma consequência. O mestre que decidir rodar a cena de arco que a nota
promete não tem uma linha para consultar.

**O que a obra dá — e é bastante.**

**A trava principal, canônica, que o sistema desconhece.** Cap. 1043: *"**The five regional walls
targeted Gu Immortals, not Immortal Gu.**"* Na mesma passagem, o exemplo: um imortal enviou um
**Gu Imortal de informação de rank 6** de uma região a outra e ele *"could travel across (…)
going through two regional walls without obstruction"*. Consequência de mesa imediata e enorme:
**mensagens, encomendas e Gu enviados atravessam; pessoas, não.** Um mundo em que a informação
circula livremente e os corpos não é um mundo político completamente diferente daquele em que
nada passa — e é o mundo do romance.

**A tabela de baixas de uma travessia dupla.** Cap. 928, um grupo indo do Mar Oriental às
Planícies do Norte (duas paredes seguidas, porque **as paredes se tocam** — não existe terra de
ninguém entre regiões):

> *"they had to pass two regional walls, **the three rank eights were heavily injured, while four
> of the rank seven immortal zombies died** in the regional walls. In contrast, **the rank six Gu
> Immortals faced less pressure.**"*

Leia a ordem: **os rank 8 se feriram, os rank 7 morreram, e os rank 6 sofreram menos.** A pressão
da parede **escala com a fundação de quem atravessa** — é uma trava invertida, e a leitura para a
mesa é excelente: numa travessia de fronteira, **os personagens mais fracos do grupo são os mais
seguros, e o perseguidor poderoso é quem paga o preço mais alto**.

**A regra de combate dentro da parede.** Cap. 1216: *"Inside the regional wall, when Gu Immortals
use their **immortal killer moves**, their **immortal apertures would shake and they would get
injured before even harming the enemy**."* Lutar dentro de uma parede é lutar sem golpes — o que
faz da parede uma **arena de emboscada**, e o romance a usa exatamente assim (cap. 1257: *"I can
get rid of you all in the regional wall"*). E há criaturas que ignoram a supressão da parede
inteiramente, movendo-se lá dentro *"as if it did not feel any resistance or pressure"* — o que
dá ao mestre um monstro de fronteira pronto.

**A parede tem espessura, e ela se mede em passos.** Um golpe imortal abre um corredor de **setenta
e poucos passos**; um grupo avança revezando golpes; um trecho fino pode exigir mais de **três mil
passos** de escavação. E ela **se regenera enquanto se cava** — um corredor recém-aberto já
encolheu dois passos quando o último da fila entra. Existem **pontos fracos**, e localizá-los é
trabalho de **dedução**: um especialista calcula onde a parede é mais fina, e essa informação vale
uma travessia inteira. Isso é um procedimento de cena inteiro, e ele encaixa direto no
`🧠 Dedução` e no `🕵️ Preparação e Informação` que o sistema já tem.

**A consequência de longo prazo, que é a mais dura.** Cap. 1236: *"when he passed the regional
walls, **his immortal aperture's foundation was damaged**."* E cap. 1172, sobre morar fora:
*"when a Northern Plains Gu Immortal leaves Northern Plains, a foreign region's heaven and earth
qi would cause their **immortal aperture to become unstable, it might even break apart**, trying
to undergo tribulation was **courting death**."* Ou seja: **um imortal expatriado não pode
tribular com segurança** — e tribular é como um imortal sobe. Isso transforma "mudar de região"
de uma decisão logística numa decisão de carreira, e é o motivo canônico pelo qual imortais
voltam para casa.

**E a consequência social, de graça.** Cap. 1253: *"**Foreign region Gu Immortals would be
marginalized in other regions and even be hunted.**"* O grupo que atravessa não chega a um lugar
novo: chega a um lugar que sabe o que ele é pelo cheiro.

**A tabela que eu recomendo escrever, com o que está acima:**

| Peça | Valor canônico |
|---|---|
| O que a parede pega | **Gu Imortais, não Gu Imortal** — objetos, mensagens e Gu enviados passam |
| Quantas paredes por viagem | **duas**, sempre — as paredes se tocam |
| Escala do dano | **cresce com o rank do viajante**: rank 6 sofre pouco, rank 7 morre, rank 8 sai gravemente ferido |
| Lutar lá dentro | golpe imortal **fere o próprio usuário** antes de atingir o alvo |
| Espessura | dezenas a **milhares de passos**; regenera enquanto se escava |
| Como se encurta | achar um **ponto fraco** por dedução — é a informação que vale a travessia |
| Depois de atravessar | **fundação da abertura danificada**; e, morando fora, **tribular é suicídio** |
| Ao chegar | marginalizado, possivelmente caçado |

**Onde isso mora na nossa Bíblia:** `04 - Mundo/04 - As Cinco Regiões.md` — inclusive a tabela
com **nome, cor e interior de cada uma das cinco paredes** (parede santa, alcaçuz, miasma, chama
ardente, água azul), que é o material descritivo que falta ao sistema para a cena existir na
mesa; e `08 - Eventos e Cenarios/17 - Caçadas, Emboscadas e Fugas.md`.

**Onde entraria no sistema:** dentro de `03 — Gu/🗺️ Supressão Regional.md`, expandindo a seção
"Gu Imortais e as Muralhas Regionais" que já está lá. **Não** merece nota nova: ela pertence ao
lado da supressão mortal, e o achado 2 já reescreve essa mesma nota — as duas correções entram
numa passada só.

**Por que recomendo.** Porque o sistema já **prometeu** essa cena ("é cena de arco") e não a
entregou, e porque o Ato 3 do `🗺️ Arco da Campanha` depende dela: sem números, "o mapa está
fechado no ato imortal" é uma afirmação que o mestre precisa sustentar no grito. Com a tabela, a
travessia vira uma das melhores cenas do ato — uma em que **o membro mais fraco do grupo é o
herói**, o que quase nenhum sistema consegue produzir.

---

### 8. Há **treze Casas de Gu Imortal canônicas** escondidas dentro do índice corrompido — o sistema já as tem e não sabe

- **Categoria:** buraco que atrapalha jogar *(disfarçado de bug de conversão — e o achado de melhor razão trabalho/retorno da lista)*
- **Tamanho do trabalho:** pequeno — recortar dezessete linhas de uma tabela e colá-las noutra

**O que está no sistema hoje.** `03 — Gu/📇 Índice de Gu do Romance — Consulta.md`, na "Camada B —
200 Gu", tem uma **tabela de Casas de Gu Imortal fundida por engano dentro da tabela de Gu**,
junto com a linha de cabeçalho dela. O resultado é visível a olho nu:

```
| Calamity Luck Altar | 8 | sorte |
| Casa | Rank | Caminho |          ← cabeçalho da outra tabela virou "um Gu chamado Casa"
| Chamber Pot | 7 | trevas |
| Cook | 7 | comida |
```

A coluna "Efeito" desses registros não contém efeito nenhum: contém o **Caminho**, porque a tabela
de origem tinha as colunas `Casa · Rank · Caminho`. Elas são fáceis de encontrar em bloco: são as
únicas linhas da tabela cuja terceira coluna é uma palavra só e essa palavra é o nome de um
Caminho (`sorte`, `trevas`, `comida`, `tempo`, `sabedoria`, `roubo`, `luz`). São **dezesseis linhas de Casa mais a linha de
cabeçalho** (linhas 53, 55, 57, 60, 61, 65, 81, 87, 109, 144, 149, 161, 175, 204, 216, 217 e 230
do arquivo), e há ainda pelo menos duas células **cortadas no meio da frase**: *"Converte marcas de lei de qualquer caminho em
marcas de"* (Adaptation Gu) e *"…ataques de pens"* (Battle Thought Gu).

**Por que isso é mais do que um erro de digitação.** Três das dezesseis já estão no
`📖 Catálogo de Gu` (Calamity Luck Altar, Dark Prison, Graceful Chaotic Duel Stage). **As outras
treze não estão em lugar nenhum do sistema** — e o Catálogo afirma, na linha de fecho da seção,
*"Total: 12 Casas de Gu Imortal (nenhuma inventada — todas aparecem no romance)"*. São treze Casas
canônicas a mais que o sistema já levantou, escreveu num arquivo seu, e perdeu na conversão:

| Casa | Rank | Caminho | Ocorrências no texto-fonte |
|---|---|---|---|
| Chamber Pot | 7 | trevas | verificada |
| Cook | 7 | comida | verificada |
| Cooking Luck Pot | 7 → 8 | sorte | 117 |
| Eat Fragrance | 6 | comida | verificada |
| Eternal Yacht | 8 | tempo | 78 |
| Luck Suppression Heavenly Palace | 8 | sorte | 88 |
| Medicine Fragrance | 8 | comida | verificada |
| Myriad Age Building | 7 | tempo | 25 |
| Present and Past Pavilion | 7 | tempo | 111 |
| Star Constellation Chessboard | 8 → 9 | sabedoria | 135 |
| Thieves Den | pico | roubo | 30 |
| Thought Expelling Pavilion | 7 | sabedoria | 9 |
| Winding Light Platform | 7 | luz | 29 |

*(A coluna da direita é a contagem bruta de ocorrências do nome nos seis volumes, feita com
`grep -ric`. Nenhuma delas é uma menção isolada: todas são estruturas recorrentes do romance.)*

**O que isso resolve, além da higiene.** O mapa de lacunas registra que o Catálogo lista 12 Casas
enquanto `🔷 Formações de Gu` afirma "uma Casa-Gu por campanha, é regra". Com treze Casas a mais,
a leitura correta fica óbvia e a contradição some sozinha: **o mundo tem dezenas de Casas; a mesa
tem uma.** E dá ao mestre um repertório de Casas **inimigas** — hoje ele só tem as doze que o
grupo poderia querer.

Repare, ainda, no que a lista revela do próprio mundo: há **três Casas do caminho da comida**
(Cook, Eat Fragrance, Medicine Fragrance), **quatro do tempo** e **três da sorte**. É uma
distribuição que diz muito sobre quais Caminhos constroem estruturas neste cenário — informação
de cenário que não custa nada porque já está paga.

**Mais dois reparos de higiene, da mesma família e igualmente baratos:**

1. **`03 — Gu/🍖 Sustento e Alimento.md` fala de Gu Imortal faminto e não diz o que acontece.**
   A nota manda o leitor para `🌾 Ecologia e Economia da Terra Abençoada`, que tem a seção
   "Penalidade por Fome" com os degraus e a regra — excelente, aliás — de que **realimentar cura
   um degrau por ciclo, nunca mais de um** *(que é, de quebra, exatamente a mecânica de cura da
   obra: ver achado 6)*. Falta só **repetir os quatro degraus na nota de sustento**, porque é
   nela que o mestre vai olhar no meio da sessão. Duas dessas notas se conhecem; o mestre em
   cima da hora não.
2. **As duas células truncadas do índice** precisam ser recompletadas ou marcadas com `—`.
   Uma entrada de consulta cortada no meio é pior do que uma entrada vazia: ela parece
   informação.

**Onde isso mora na nossa Bíblia:** `10 - Apendices/05 - Catálogo de Gu - Imortais.md` e
`02 - Gu/08 - Formações de Gu.md` — que trazem as Casas com efeito, e podem preencher a coluna
"Efeito" das treze linhas se o executor quiser promovê-las a fichas.

**Onde entraria no sistema:** recortar as dezessete linhas (as dezesseis Casas e o cabeçalho) de
`📇 Índice de Gu do Romance — Consulta.md` e colá-las como **tabela própria** no mesmo arquivo
(ou no `📖 Catálogo de Gu`, seção "Casas de Gu Imortal", como lista de nomes sem ficha — que é o
que a Camada B é). Ajustar o total declarado de 12 para 25.

**Por que recomendo.** Porque é conteúdo canônico que o sistema **já pagou o custo de levantar** e
está perdendo por um erro de tabela — e porque um índice de consulta com cabeçalho vazando é a
coisa que mais rápido faz um mestre desconfiar de um vault inteiro. É meia hora de trabalho.

---

### 9. A "promoção mística": acúmulo de Marcas concede faculdade inata — e o sistema diz que isso **nunca** acontece

- **Categoria:** profundidade que vale a pena *(com um "nunca" a corrigir)*
- **Tamanho do trabalho:** pequeno — uma linha de regra e quatro exemplos canônicos

**O que está no sistema hoje.** `02 — Caminho do Cultivo/☯️ Marcas de Dao.md` separa os dois eixos
com muita clareza, e a separação é boa:

> ```
> Marcas sobem sozinhas, com o tempo e o risco.
> Domínio só sobe quando o personagem entende alguma coisa.
> ```
> (…) sobe **em salto**, quando a mesa reconhece um feito real de compreensão (…) **Nunca por
> acúmulo.**

**O que a obra diz.** Cap. 1119 registra, como saber corrente entre imortais, exatamente a coisa
que o sistema nega:

> *"I heard that **with a certain number of luck path dao marks, the Gu Immortal will have a
> mystical promotion**."*
>
> *"That's right, **for refinement path Gu Immortals, their Gu refinement abilities would rise
> sharply, when refining Gu, they would be able to sense minute details. For fire path Gu
> Immortals, they would have a certain sense towards fire path Immortal Gu and desolate beasts.
> For wisdom path Gu Immortals, even without using any Gu, their own deduction abilities would be
> very strong. As for luck path Gu Immortals, they would have some sensation towards their own
> luck or the luck around them.**"*

Quatro Caminhos, quatro faculdades, e o padrão é o mesmo nos quatro: **um sentido passivo, sempre
ligado, que funciona sem Gu e sem custo**. Não é poder de combate — é percepção.

**Onde o sistema já acertou, e vale dizer.** A **Simulação de Marca** do nível Mestre (*"você
replica o efeito de um Gu do seu Caminho sem ter o Gu"*) e o **Improviso cruzado** do
Grão-Mestre são a versão ativa e balanceada desta mesma ideia canônica — inclusive a frase de
fecho da nota, *"a partir de Mestre, o personagem para de depender do que carrega"*, é
praticamente a tradução de *"even without using any Gu"*. Se essas regras estiverem marcadas como
✍️ autorais, **elas merecem 📕**.

**O que falta, e é o que recomendo:** a versão **passiva e por contagem**. Uma linha:

> **Sentido do Caminho.** Ao cruzar o topo da faixa de Marcas do seu rank num Caminho, o Imortal
> ganha um sentido inato daquele Caminho — permanente, sem custo de essência, sem rolagem, sem
> Gu. Não causa dano e não substitui um Gu: ele **percebe**. Refino sente detalhes minúsculos ao
> refinar; Fogo sente Gu Imortais e feras de fogo por perto; Sabedoria deduz sem Gu de dedução;
> Sorte sente a própria sorte e a alheia. Para um Caminho não listado, o mestre escolhe o sentido
> equivalente `*`.

**Por que recomendo, apesar de ser pequeno.** Porque hoje o sistema tem um Imortal "denso" — o de
contagem alta e Domínio baixo — que é **puramente defensivo**: ele só ganha Vitalidade. É a
categoria de personagem que o próprio vault chama de "o veterano que ninguém consegue matar", e
ela não tem nada para *fazer*. O sentido do Caminho dá a ela uma competência fora de combate que
custa zero de balanceamento e que os jogadores vão usar toda sessão — e transforma "acumulei
Marcas sem entender nada" de um beco sem saída num tipo de personagem.

E, junto, **conserta um "nunca"**: o sistema pode continuar dizendo *"Domínio nunca sobe por
acúmulo"* — é uma boa regra —, desde que pare de dizer que **nada** sobe por acúmulo. Sobe: o
sentido.

**Onde isso mora na nossa Bíblia:** `01 - Cultivo/12 - Dao Marks.md`, e as seções "A camada
escondida" de `03 - Paths/` (o caminho do qi, o da sorte e o da formação discutem a promoção
mística cada um do seu ângulo — o da formação notavelmente por **não** ter uma).

**Onde entraria no sistema:** `02 — Caminho do Cultivo/☯️ Marcas de Dao.md`, junto da tabela de
Densidade Imortal — porque é o mesmo eixo (contagem) e o mesmo público (o Imortal denso).

---

### 10. A escada também desce: idade, atalhos empilhados e aptidão que cai

- **Categoria:** profundidade que vale a pena
- **Tamanho do trabalho:** pequeno — três linhas, cada uma numa nota diferente que já existe

**O que está no sistema hoje.** O sistema **já tem** as duas pontas: `❤️ Recursos e Dano` tem a
**Destruição da Abertura** (o caso terminal, com Aptidão a 0%), e o `📖 Catálogo de Gu` cobra
*"um estágio de cultivo permanente"* de quem é ressuscitado pelo Gu do Ressurgir dos Mortos. O que
não existe é o **meio da escada**: nada no sistema faz um personagem descer sem ser destruído.

**O que a obra dá — três vetores, todos verificados, todos baratos de escrever.**

**1. A idade derruba o rank.** Cap. 145, sobre um veterano:

> *"At his peak period, he had reached Rank three. However, **because of injuries, his cultivation
> dropped down to Rank two peak stage** and now **due to his old age, his cultivation had further
> dropped down to Rank two upper stage**."*

Duas quedas, duas causas diferentes, na mesma ficha. A carreira de um cultivador é **um arco, não
uma reta**: sobe, estaciona e desce antes de acabar. Isso conversa direto com `⏳ Longevidade`, que
é a melhor nota do vault e que hoje trata a idade **só** como um relógio de morte. Uma linha na
tabela dela — *a partir de certo ponto da vida, o personagem começa a perder estágios* — devolve
ao ancião de clã a forma canônica dele: alguém que **já foi** mais forte, e que sabe disso.

**2. Atalhos empilhados brigam entre si.** Cap. 198, e este é o caso mais espetacular do gênero:

> *"Fang Yuan had used the **Stone Aperture Gu** to squeeze out all his potential, causing his
> cultivation to rise to Rank three peak stage. But this **Blood Skull Gu** injected the quality
> blood stream into him, raising the aperture's potential and raising his aptitude."*

Resultado: a aptidão saiu de **43% para mais de 90%**, e o cultivo caiu de **rank 3 para rank 1**.
O texto até faz a pergunta que o leitor faria — *"First gen Gu Yue evidently retained his
cultivation level as his aptitude rose, so why (…) when it came to Fang Yuan?"* — e a resposta é
a regra: **quem forçou a abertura com um método artificial perde tudo o que aquele método
sustentava quando um método de rank maior age sobre a mesma abertura.** Quem chegou lá
naturalmente não perde nada.

Isso é **exatamente o freio que a tabela de onze desvios de `⏳ Longevidade` já quer ter**. Hoje
ela cobra `+2` de CD por método heaven-defying acumulado, que é um custo abstrato; a obra oferece
um custo diegético e muito mais assustador: **o atalho novo apaga o atalho velho, e o personagem
desaba junto**. O sistema pode manter o `+2` e acrescentar a consequência.

**3. Aptidão desce, e não só na destruição da Abertura.** `🌟 Aptidão e Abertura` tem uma seção
"Aptidão não é 100% fixa" com **três formas de subir** e nenhuma de descer. A obra tem as duas
direções, e a mais elegante é um preço de milagre — cap. 199, sobre um Gu de cura de rank 4 que
ressuscita:

> *"It is a Rank four healing Gu and has the effect of bringing the dead to life. It has a weak
> point though, and that is — **the Gu Master's aptitude will be lowered by 10% once it is
> used**."*

E há a via lenta: **essência alheia deixada dentro da abertura impregna a parede e derruba a
aptidão** quanto mais tempo ficar — que é, aliás, a outra face do achado 1 (essência de outro não
é só inútil: é tóxica).

> [!note] Uma sugestão de troca, não de acréscimo
> O Gu do Ressurgir dos Mortos, no Catálogo do sistema, cobra hoje *"um estágio de cultivo
> permanente"*. A obra cobra **10% de aptidão, para sempre**, pelo Gu equivalente. Trocar um pelo
> outro **não acrescenta regra nenhuma** e é estritamente melhor: estágio se recupera jogando,
> aptidão não se recupera nunca — e a aptidão é o número que o mundo inteiro deste cenário
> enxerga e julga. É a diferença entre "atrasei" e "sou outra pessoa agora".

**Onde isso mora na nossa Bíblia:** `01 - Cultivo/15 - Perder Cultivo.md` — as cinco formas de
perder cultivo, o que volta e o que não volta, e a seção "Perder de propósito".

**Onde entraria no sistema:** uma linha em `⏳ Longevidade` (idade), um callout de aviso em
`⏳ Longevidade` na tabela dos desvios (atalhos empilhados), e três bullets em
`🌟 Aptidão e Abertura` (aptidão descendo). **Nenhuma nota nova.**

**Por que recomendo — com a ressalva de que este é o achado mais fácil de recusar.** O sistema é
construído sobre uma catraca que sobe, e isso é uma escolha de design defensável para uma mesa
que quer jogar. O que eu recomendo **não** é abrir a porta de o personagem do jogador decair: é
dar ao **mestre** o vocabulário canônico para NPCs — o ancião que já foi rank 3, o gênio que
trocou poder por potencial, o velho mestre que enfraquece a cada ano. Se o executor adotar só
isso e não mexer nas regras dos PJs, o achado já valeu.

---

## O que existe na obra e eu NÃO recomendo acrescentar

Esta seção é parte do produto. Cada item abaixo é material canônico, real, verificado — e cada um
foi **recusado por mim**, com o motivo escrito, para que o agente executor não gaste uma sessão
reabrindo a discussão. Se ele discordar de alguma, que discorde com o argumento na mão.

**1. As fichas de clãs, seitas, tribos e cidades das cinco regiões.**
A Bíblia tem seis notas com o inventário político das cinco regiões, nome por nome. O sistema
**recusa deliberadamente** ter cenário: `🌍 Terras e Facções` diz, em callout, *"Nada nesta pasta
é obrigatório (…) o cenário é seu pra inventar"*, e `🛠️ Como Criar Sua Lore` ensina a construir o
próprio em quatro passos. Importar cinco regiões de facções nomeadas **contradiria a arquitetura
do vault** e acrescentaria mais volume do que qualquer outro item desta revisão inteira. O que
vale importar dali já está no achado 5 (as travas), que é ferramenta e não cenário.

**2. Os vinte e nove cenários jogáveis da Bíblia.**
Mesma razão, mais uma: eles são **acontecimentos do romance**, e o sistema tem uma política
explícita de spoiler (*"Não use — é enredo: eventos específicos da trama, mesmo disfarçados de
lenda antiga"*). Extraí deles a única camada que atravessa a política — as travas — e ela cabe em
uma seção.

**3. As vinte e oito trilhas de cultivo que faltam.**
A obra nomeia cerca de cinquenta e um Caminhos; o sistema joga com vinte e três. **A curadoria
está certa** e é o tipo de decisão que um sistema de mesa precisa tomar. Vinte e oito Caminhos a
mais seriam vinte e oito dados, vinte e oito vias de avanço e vinte e oito seções de Catálogo —
pelo ganho de poder dizer que a lista está completa.

**4. Marcas de Dao no patamar mortal.**
Isto é canônico e eu tropecei nele no achado 4: o fantasma de fera **é** uma marca de dao no corpo
de um cultivador de rank 2, e removê-lo barateia o custo de Gu de outro Caminho (cap. 291). Ou
seja, no romance a economia de marcas existe desde o começo. **Mesmo assim, não importe.** O
sistema fez a escolha oposta de propósito — marcas começam no rank 6 — e ela sustenta duas coisas
boas: a fase mortal é leve de rastrear, e a virada para imortal ganha um subsistema inteiro só
dela. Um contador de marcas mortais duplicaria o que os Níveis de Potência já fazem e cobraria
rastreamento de todo jogador desde a sessão 1.

**5. As proporções canônicas de "quantos fracos derrubam um forte".**
A obra publica números: três rank 3 para um rei-fera; dois rank 4 no pico para um rank 5; contra
um imortal, um é irrelevante, três resistem, seis seguram e nove pressionam. São ótimos de ler e
**péssimos de importar**, porque o sistema já responde a essa pergunta com 3.000+ iterações de
simulação por cenário e uma tabela de composição de cena medida. Números de prosa não devem
brigar com números medidos. *(A frase que vale copiar, se alguma: **"número decide dentro do mesmo
patamar; contra um patamar acima, número é combustível"** — mas ela já está implícita no molde de
Horda.)*

**6. O bestiário de oitenta e sete criaturas.**
O `⚔️ Ameaças Genéricas por Rank` tem seis moldes que escalam por `M` até o rank 9 e uma receita
de variação ("troque o Caminho da especial"). Um bestiário nomeado é sabor, e sabor é exatamente
o que o mestre inventa mais rápido do que consulta. **Exceção:** se em algum momento o executor
quiser exemplos prontos, o lugar barato é a linha de "como variar sem refazer a ficha", com cinco
nomes, não uma nota nova.

**7. A medicina mortal sem Gu, e a perda de sangue como condição própria.**
A obra tem salão de medicina como departamento de clã, triagem (estancar, desinfetar, imobilizar,
enfaixar), kits que acabam no meio da campanha, e **perda de sangue progredindo sozinha** —
lentidão, saída de combate, inconsciência, morte — independente da gravidade do ferimento. É
excelente ficção e é **mais uma condição para rastrear numa mesa que já rastreia Vitalidade, Alma,
Essência, Ferimento, Exposição e alimentação de Gu**. O orçamento de rastreamento do sistema está
cheio. Vale como descrição do mestre, não como regra.

**8. A "promoção mística" escrita Caminho por Caminho.**
A obra nomeia quatro (refino, fogo, sabedoria, sorte). Escrever as outras dezenove seria inventar
dezenove faculdades e marcá-las `*`. O achado 9 propõe deliberadamente **a regra geral com os
quatro exemplos canônicos** e "o mestre escolhe o equivalente" para o resto. Não expanda.

**9. As paredes regionais como cinco fichas separadas.**
No achado 7 recomendo a **tabela de efeito**, que é regra, e menciono que a Bíblia tem nome, cor e
interior de cada uma das cinco. Isso é uma tabela de cinco linhas para descrição — **não** cinco
seções. A parede é um obstáculo, não um lugar.

**10. O repertório canônico de fuga e contra-rastreamento.**
A Bíblia tem páginas sobre como se foge, como se rastreia e como se anula um rastreio neste mundo.
O sistema tem `🏃 Fuga e Perseguição` fechado, com teste, custo e procedimento, medido em
simulação. Não mexa: o que a obra acrescentaria é repertório de Gu, e repertório de Gu é assunto
do Catálogo, que já é o maior arquivo do vault.

---

## Dúvidas legítimas de escopo

Casos em que mais de uma decisão é defensável. Descrevo as opções e digo qual eu tomaria — mas a
decisão é do autor do sistema, não minha.

**1. A cura por afinidade de Caminho (achado 6) mexe com a matemática medida?**
Sim, potencialmente. Metade da cura muda a curva de atrito, e a curva de atrito foi calibrada em
simulação.
- *Opção A — adotar só a linha imortal:* "ferimento causado por golpe imortal não é curado por Gu
  mortal". **Impacto zero na matemática mortal**, porque nenhum combate mortal contém golpes
  imortais. Ganho: a fronteira mortal/imortal passa a doer.
- *Opção B — a tabela inteira, incluindo a metade por conflito de Caminho.* Ganho maior, custo de
  remedição.
- **Recomendo A agora e B depois de medir.** A é grátis e já entrega a maior parte do valor.

**2. Aptidão que desce (achado 10) vale para os personagens dos jogadores?**
- *Opção A — só NPCs.* O mestre ganha vocabulário (o ancião decaído, o gênio que trocou poder por
  potencial) e nenhum jogador perde ficha por causa do calendário.
- *Opção B — vale para todos*, como na obra.
- **Recomendo A como padrão e B como regra opcional declarada na sessão zero.** A obra é impiedosa
  porque é um romance sobre uma pessoa só; uma mesa tem quatro, e uma delas vai ser a azarada.

**3. A Casa de Gu Imortal queimando essência saqueada (achado 3) quebra a economia?**
Pode. Se cada imortal derrotado render um estoque de contas que a Casa converte em combustível, o
grupo que caça imortais nunca mais fica sem gasolina — e o achado 1 existe justamente para que
combustível seja escasso.
- *Opção A — sem teto*, como na obra.
- *Opção B — teto por cena*: a Casa queima essência de terceiros até um limite por cena, e o
  excedente fica guardado. **Recomendo B**, porque preserva o achado 1 (roubar essência continua
  sendo desarmamento, e não abastecimento) e mantém o ganho de design (o espólio inútil passa a ter
  destino).

**4. O rank 1 e a Supressão Regional (achado 2).**
- *Opção A — manter a linha autoral "Gu de rank 1 não funcionam" e apontar o refino no destino como
  a saída canônica.* A pendência fecha sem mudar a regra.
- *Opção B — apagar a linha do rank 1 e deixar só a queda canônica de um rank.* Mais limpo, mas um
  Gu de rank 1 a "rank 0" precisa de um valor definido de `M`, que hoje não existe.
- **Recomendo A**, porque não exige tocar em nenhuma fórmula.

**5. A economia de prisioneiros — o único assunto que fiquei em dúvida se deveria ter virado
achado numerado.**
A obra é explícita em que **prisioneiro vale mais que cadáver**: memória se rouba, escravo se usa,
resgate se cobra, mandado se resgata — e um morto não dá nada disso. O sistema tem
`⛓️ Espólio de Gu Imortal` (excelente) e `🕵️ Preparação e Informação`, mas o incentivo de mesa
hoje aponta para matar.
- *Opção A — um parágrafo em `⛓️ Espólio`:* "o que um prisioneiro rende que um cadáver não rende",
  com quatro linhas. Custo mínimo, e muda o comportamento da mesa na primeira vez que é lido.
- *Opção B — deixar de fora*, porque é assunto de mestre e não de regra.
- **Recomendo A.** Não virou achado numerado porque não consegui demonstrar que a ausência trava
  alguém na mesa — mas é o item que eu promoveria primeiro se sobrasse orçamento.

**6. Duas pendências do sistema que eu não consigo ajudar a fechar, e que continuam abertas.**
Registro para que não pareçam esquecidas:
- **O Golpe Matador Coletivo** está com custo e benefício marcados como **PROVISÓRIOS** por um bug
  de motor de simulação, com remedição pendente. Isso é medição interna: eu não tenho os dados da
  simulação e não deveria opinar. **Continua sendo, na minha leitura, a pendência mais urgente do
  vault** — mais do que qualquer achado meu, porque é um número em uso que se sabe errado.
- **O Grimório de Ameaças** tem exemplos prontos só até o rank 6. Eu **não** recomendo escrever
  fichas de rank 7 a 9 (ver a seção anterior, item 6), mas recomendo **declarar isso por escrito**
  na nota: "dos ranks 7 a 9 o sistema oferece a matriz de diferencial de domínio e o molde por `M`,
  e não oferece exemplos, porque nesse patamar o confronto é resolvido por trava, terreno e
  política — ver o cardápio de travas". Uma frase transforma uma lacuna aparente numa decisão
  declarada, que é o padrão que este vault já aplica em toda parte.

---

*Fim da revisão.*
