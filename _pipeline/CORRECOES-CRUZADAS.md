# Correções cruzadas — aplicação das recomendações de outros agentes

**Data:** 2026-09-02
**Escopo (arquivos meus, exclusivos):**

- `01 - Cultivo/16 - Dao Marks.md`
- `05 - Sociedade/13 - As Grandes Forças do Mundo.md` *(o prompt chamava de `07 - …`; o vault
  foi renumerado hoje e o arquivo real é o `13 - …`)*
- `05 - Sociedade/11 - Cultura das Cinco Regiões.md` *(idem: o prompt chamava de `06 - …`)*
- `11 - Apendices/02 - Tabelas de Referência Rápida.md`

**Método:** cada recomendação foi reaberta no texto-fonte antes de virar edição. Nenhuma
foi aplicada por confiança no relatório de origem. Três não se sustentaram (seção 5).

`auditar-links.py` ao final: **4.652 links por nome exato, 0 quebrados, 0 dependentes de alias.**

---

## 1. Dao Marks — a promoção mística

**Verificação.** Capítulo 1119, cena entre três imortais do Deserto do Oeste. Duas falas
consecutivas, ambas conferidas linha a linha:

> *"Ouvi dizer que, com um certo número de marcas do Dao de sorte, o Gu Imortal terá uma
> **promoção mística**."*
>
> *"Isso mesmo. Para Gu Imortais do caminho do refino, suas capacidades de refino subiriam
> acentuadamente, e ao refinar conseguiriam perceber detalhes minuciosos. Para os do caminho
> do fogo, teriam certa percepção de Gu Imortais e feras desoladas de fogo. Para os do
> caminho da sabedoria, mesmo sem usar nenhum Gu, sua capacidade de dedução seria muito
> forte. Quanto aos do caminho da sorte, teriam alguma sensação da própria sorte e da sorte
> ao redor."*

A primeira fala nomeia só a sorte; é a **segunda** que generaliza o fenômeno para quatro
caminhos e o transforma em regra geral. Ambas foram citadas na íntegra no arquivo-fonte antes
de eu escrever a seção.

**Aplicado.** Nova seção `## A promoção mística — quando as marcas dispensam o Gu`, entre
"Como se ganham" e "Por que o dano de dao marks não regenera". Contém:

- o enunciado da regra em destaque `==…==`, com o ponto que a torna única no cenário: é a
  **única exceção estrutural** à dependência do Gu — a faculdade não se rouba, não se sela,
  não se confisca, não gasta essência e não desliga;
- tabela dos quatro caminhos nomeados e do que cada um ganha (wikilinks com texto alternativo
  e pipe escapado, `[[08 - Refinement Path\|Refino]]` etc., convenção do vault para tabelas);
- `—` explícito para o **número de marcas**: a obra só diz "um certo número". No lugar do
  número, a referência prática que ela dá — o caso de alguém **sem cultivo de rank 7** cujas
  marcas de sorte eram "não inferiores às de um imortal de sorte de rank 7", e era isso que
  justificava a expectativa da promoção;
- callout `[!warning]` fixando a lição: **a régua é a marca, não o rank**;
- `—` para todos os caminhos fora dos quatro nomeados, e o registro de que a ausência de
  promoção mística no caminho das formações é **coerente**, porque ele não gera dao marks
  próprias. **Reconferi a negativa eu mesmo**, porque negativa vinda de outra nota não vale:
  `formation path dao mark(s)` tem **zero** ocorrências reais nos seis volumes. Atenção à
  armadilha de grep — uma busca por substring devolve 92 falsos positivos, todos de
  *in**formation** path dao marks* e *trans**formation** path dao marks*; com limite de
  palavra à esquerda, o resultado é zero em todos os volumes;
- subseção `### É a mesma família dos fantasmas de fera e das feras fantasma`, ligando por
  wikilink a `[[04 - Strength Path]]` e `[[14 - Space Path]]`;
- **a aproximação entre os três fenômenos foi marcada `(ded.)`**, com a frase explícita de que
  a obra nunca chama os fantasmas de fera nem as feras fantasma de "promoção mística". O que
  ela afirma, e sustenta a leitura, é a origem comum: marcas acumuladas em quantidade
  suficiente;
- callout `[!note] Para o design` com dois usos de mesa (salvaguarda contra a cena de captura;
  a faculdade como reputação que não se blefa).

`cap. 1119` acrescentado ao `fontes`.

### 1b. Correção colateral obrigatória na mesma nota

A nota trazia as faixas de dao marks por rank como **6: 0–9.000 · 7: 9.000–30.000 · 8:
30.000–300.000**, e um callout afirmando que elas "caem do calendário de provações" e que "o
sistema fecha sozinho".

Isso **contradiz a tabela soberana**, que já havia sido corrigida, e contradiz o texto.
Capítulo 2071, verificado:

> *"Em média: Gu Imortais de rank seis tinham de zero a nove mil marcas do Dao. Gu Imortais de
> rank sete, de dez mil a trinta mil. Os de rank oito, de **cem mil a trezentas mil**."*

Aplicado: faixas corrigidas para 6: 0–9.000 · 7: 10.000–30.000 · **8: 100.000–300.000** ·
9: ≥300.000; callout novo sobre o **vão de setenta mil marcas** entre o teto do rank 7 e o
piso do rank 8 (que é a expressão numérica da frase, também canônica, de que a distância
7→8 é incomparavelmente maior que a 6→7); e o callout da conta de provações reescrito para
dizer o que ela de fato faz — reproduz os **tetos** de cada faixa, não os pisos — remetendo à
tabela soberana como fonte única.

---

## 2. As catorze super forças do Deserto do Oeste

**Verificação.** Capítulo 2255, frase única e literal:

> *"As super forças do Deserto Ocidental eram catorze clãs: clã Lin, clã Xiao, clã Tian, clã
> Fang, clã Dong, clã Wan, clã Sun, clã Mo, clã Tang, clã Qin, clã Shi, clã Gong, clã Zuo Qiu
> e clã Tuoba."*

A lista dos catorze nomes levantada pelo outro agente confere **exatamente**, na ordem.

**Aplicado** em `05 - Sociedade/13 - As Grandes Forças do Mundo.md`, seção do Oeste (antes
listava oito das catorze, em bullets):

- seção renomeada para `### As catorze super forças`, com a lista em bloco de citação e a nota
  de que *Zuo Qiu* e *Tuoba* são sobrenomes compostos (dois clãs, não quatro);
- o parágrafo canônico sobre **por que não há ranking**: a força de uma super força vem de
  eixos diferentes (imortais, recursos, Casas de Gu Imortais) e cada casa é forte num e fraca
  noutro; o Oeste, ao contrário do Sul, nunca teve primeira colocada reconhecida; o consenso
  vago é que Xiao e Tian são as mais bem vistas, por maiores negócios na era de paz e rank 8
  na liderança — tudo do mesmo capítulo;
- **tabela de bolso das catorze**, uma linha por clã, com o wikilink
  `[[05 - Deserto Ocidental|Deserto Ocidental]]` dizendo em voz alta que as fichas completas
  moram lá. Li a nota de fichas inteira antes: as descrições de uma linha são **resumos** dela,
  não duplicações — e `Qin` entra com `—` porque lá também é `—`;
- os três bullets que tinham virado redundantes (Dong, Sun e a parte genérica de Mo) foram
  substituídos por uma linha de remissão à nota de fichas. Mantive o bullet do Mo pelo detalhe
  de recrutamento e pelo pedágio de uma pedra primordial, que não estão na tabela de bolso.

### As duas divergências, registradas em callout `[!warning]`

**A décima quinta.** O mesmo capítulo 2255 abre a exceção sozinho: *"Se o misterioso e recluso
clã Yi também fosse contado, seriam quinze clãs."* Fui atrás e o clã Yi do Oeste tem cena
própria (cap. 2131): *"existia um super clã oculto no Deserto Ocidental, com força poderosa e
longa história, aparentemente existindo desde tempos imemoriais — mas isso era só um boato
entre as super forças do Deserto Ocidental, e nunca houve prova clara"*; e, no cap. 2289, que
seus imortais são **homens-pena** e que a casa se esconde há eras por um método deixado por um
dos Veneráveis. Registrado, com o alerta de não confundir com o **clã Yi da Fronteira do Sul**,
que é outra casa, aberta e conhecida.

**O clã Xi.** Confirmado no texto, em três pontos independentes: cap. 673 (o ancestral de rank 8
Xi Jian Ping *"saiu da reclusão e suprimiu todos os especialistas pela força, sua majestade
impondo-se a todo o grande deserto"*, encerrando uma disputa entre super forças); cap. 1807
(o primeiro ancião supremo do clã Xi comentando a política mundial de dentro de uma sala de
cultivo fechado); cap. 1988 (o primeiro ancião supremo do clã Xi mandando um imortal presenciar
uma batalha). E o clã Xi **não está** entre os catorze. A obra não resolve. Registrei a
ambiguidade com as duas leituras possíveis, sem escolher.

`fontes` acrescido de `cap. 673`, `cap. 1807`, `cap. 2131`, `cap. 2289` (2255 já estava coberto
pelo intervalo `2239-2258`).

---

## 3. A unidade social do Deserto do Oeste

**Verificação.** A correção proposta se sustenta e é mais forte do que o relatório sugeria:

- cap. 2255 — as catorze super forças da região são catorze **clãs**;
- cap. 1973 — *"a Cidade do Lobo de Areia era uma das principais cidades do clã Mo"*, e a
  cidade tem um **senhor de cidade** que recebe os imortais do clã;
- cap. 673-674 — a anatomia do oásis: o clã dominante no centro, forças pequenas **submetidas**
  a ele no anel do meio, aldeias mortais na franja, todas sob o controle daquele clã;
- e um oásis inteiro sendo declarado como *"controlado por nós, o clã Lan"*, com regras
  próprias de espaço aéreo e procedimento de entrada.

**Aplicado** em `05 - Sociedade/11 - Cultura das Cinco Regiões.md`:

- título da subseção de "o mundo das cidades" para **"clãs que governam cidades"**;
- parágrafo novo em bloco de citação separando os dois planos: **a cidade é a unidade
  econômica; a unidade política é o clã**, e as cidades pertencem a clãs;
- e — este é o ponto que evita desfazer o que a nota acertava — a explicação de que a diferença
  real em relação ao Sul **não** é a substituição do clã pela cidade, e sim o que o clã do Oeste
  faz com o que possui: o clã sulista se define por sangue e território, o ocidental por **rede
  comercial**. Todo o resto da subseção (prestígio como lei, cartas de desafio, pedágio urbano,
  caravana como via de ascensão social, o precedente do clã extinto) ficou intacto; o bullet das
  caravanas passou a dizer "unidades **econômicas** básicas";
- tabela comparativa das cinco regiões atualizada em três células: unidade social do Oeste
  passa a "Clã (que governa cidades e caravanas)"; critério de pertencimento a "Sangue — mas a
  posição do clã se mede em comércio e prestígio"; pergunta que se faz a "De que clã — e com
  quem ele negocia?".

`fontes` acrescido de `cap. 673-674`, `cap. 1973`, `cap. 2255`.

---

## 4. Promoções à tabela soberana

Regra que segui: **entra o que é grandeza de sistema** — número que a mesa vai consultar para
resolver alguma coisa. Não entra taxonomia, nem detalhe de cor local, nem número que só descreve
um item específico. Tudo abaixo foi reconferido no texto-fonte antes de entrar.

### 4.1 Seção 7 (amplificação por dao marks) — quatro pontos canônicos novos

A tabela tinha quatro pontos (100, 1.000, 10.000, 50.000). Faltavam quatro, e dois deles são
justamente os que **provam** a fórmula:

| Ponto acrescentado | Passagem verificada |
|---|---|
| **200 → +20%** e **600 → +60%** | cap. 852: *"Duzentas marcas do Dao podem aumentar o poder em vinte por cento. Seiscentas significariam um aumento de sessenta por cento."* |
| **1.000.000 → 1.000×** | cap. 1938 (contagem) + cap. 1943 (efeito) |
| **1.500.000 → 1.500×** | cap. 1938: *"todas as suas marcas do Dao se transformaram em um milhão e quinhentas mil marcas do Dao do tempo"*; cap. 1943: *"pela amplificação das marcas do Dao de Fang Yuan, seu poder havia aumentado mil e quinhentas vezes"* |

O parágrafo explicativo foi reescrito: a fórmula `1 + marcas ÷ 1.000` agora reproduz
**exatamente** os quatro primeiros pontos e os quatro últimos com o arredondamento que a obra
faz. Acrescentei a frase que faltava e que vale ouro para a designer: **a mesma fórmula acerta
os extremos opostos da escala** — 100 marcas e um milhão e meio —, colhidos em volumes
diferentes e em caminhos diferentes. A curva é linear do começo ao fim.

**Correção de atribuição:** o relatório `PROFUNDIDADE-paths-18-22` credita o 1.500.000 ao
**caminho do qi**. Está errado. A passagem é de **caminho do tempo** — o golpe amplificado é
*visão do futuro de três respirações*, e a contagem de 1,5 milhão é de marcas de tempo. O
número está certo, o caminho não. Registrei o número sem atribuir caminho, que é o que a
tabela precisa.

### 4.2 Seção 7 — o contraponto que faltava: golpes que queimam marcas

Verificado nos caps. 819-820. Entrou como bullet ao lado das duas regras de amplificação:
**mínimo de 16 dao marks por acionamento**, *"sem limite superior — quanto maior o alcance ou
o poder, mais marcas consumidas"*, e marcas gastas não voltam. É o único número exato de
marcas queimadas por golpe em toda a obra, e ele é o contrapeso honesto da frase "a
amplificação é gratuita": existe uma classe de golpe que **come o próprio multiplicador do
usuário**.

### 4.3 Seção 1 — nova subseção 1.1: "Quanto a aptidão pode mudar"

Verificado nos caps. 197-198, com os números todos no texto: 44% → 43% (queda por método
demoníaco) → **53% → 63% → mais de 90%**, em **seis horas**, com **mais de dez** aplicações,
**cem pessoas da mesma linhagem por aplicação**, e rendimento explicitamente decrescente
(*"nas últimas vezes o efeito enfraquecia; as primeiras subiam dez por cento, mas a
porcentagem continuava caindo a cada tentativa"*). Entrou também a queda de **−10 pontos** por
um Gu de cura de rank 4 que ressuscita, do mesmo bloco.

### 4.4 Seção 1.1 — o efeito colateral, e a regra de resolução por rank

Este é o achado mais jogável do lote e vale registrar por extenso. No mesmo capítulo 198, subir
de aptidão **derrubou o rank** do cultivador, de 3 para 2. A obra dá a explicação inteira:

> *"Mas o Gu do Crânio de Sangue era rank quatro, enquanto o Gu da Abertura de Pedra era rank
> três. O Gu do Crânio de Sangue governava sobre o Gu da Abertura de Pedra."*

O efeito de rank 3 tinha sido aplicado **primeiro** e perdeu assim mesmo. Entrou na tabela como
callout `[!warning]` com a aritmética (aptidão é o denominador: aumentar o teto reduz a fração
preenchida) e com a **regra geral de resolução — vence o rank mais alto, não a ordem de
aplicação** —, repetida na nova seção 21.5 porque é regra de arbitragem de mesa.

### 4.5 Seção 16 — a parede das cem almas

Verificado no cap. 422: *"Pessoas normais só conseguiam fortalecer a alma cem vezes, chamava-se
alma de cem homens. Este era também o limite extremo. Se a alma fosse fortalecida só um pouco
mais, explodiria com um estrondo. Como um estômago que arrebenta de comer demais."* E o
destravamento, no mesmo capítulo: os Gu temáticos (divina, dragão, gelo, sonho, lua, general,
rancor, poema, lobo) *"podem refinar minha alma e permitir que eu continue a fortalecê-la, para
romper a alma de cem homens, alcançar mil, ou até dez mil"*.

Entrou como callout `[!warning]` dentro da seção 16, porque corrige uma leitura errada que a
tabela induzia: a escada decimal parecia percorrível só somando. Não é — **trava em 100, e
ultrapassar por fortalecimento dispersa a alma para sempre**. O destravamento é por **mudança
de tipo**, não por volume. Acrescentei as duas consequências: as duas terras sagradas do caminho
da alma (a que fortalece e a que refina) são as duas metades obrigatórias de uma mesma
progressão; e o corpo tem teto próprio, dado pelas dao marks de alma nele gravadas.

### 4.6 Seção 21 (nova) — "Combate: ritmo, distância e conversão entre ranks"

A tabela mediu sempre o personagem, o mundo e a economia; faltava **a cena**. Entrou como
seção 21, com o parágrafo de abertura da nota atualizado de "vinte seções" para "vinte e uma".
Cinco subseções, todas conferidas:

**21.1 — o relógio.** `≈ 1 rodada por respiração`, marcada como canônica **mas de uma única
passagem** — cap. 1346: *"Dez respirações de tempo era o bastante para uma dúzia de rodadas de
luta, com incontáveis ataques desencadeados."* Registrei a ressalva no corpo da linha, como o
relatório pedia. Junto: 3 a 10 rodadas para resolver um combate entre mortais, algumas dezenas
até um mortal ficar ofegante, dezenas a mais de cem entre imortais, meia respiração de
sobrevida para uma defesa insuficiente contra ataque acima do patamar. E, explicitamente,
**`—` para respiração → segundos**: a obra usa a unidade com precisão cirúrgica (chega a
distinguir "a décima primeira respiração em vez da décima" como causa de um fracasso) e nunca
a ancora no relógio. Qualquer valor em segundos é invenção.

**21.2 — a distância.** 10 metros no duelo padrão, 6 metros para o proficiente. Verifiquei no
cap. 83 e o achado é melhor que o número solto, então entrou junto: os dez metros são o
**alcance do projétil básico**, e o texto dá o motivo da convenção — *"mais longe que isso a
lâmina de luar se dissiparia; se lutassem mais perto, os alunos não reagiriam a tempo"*.
Encurtar para seis é a marca de quem já consegue desviar, e a obra trata isso como salto de
proficiência **comentado pelos espectadores**. Virou callout `[!note] Para o design`: a
distância que o personagem escolhe mede o quanto ele sabe, sem rolagem nenhuma.

**21.3 — conversão entre ranks.** Cap. 168: *"Para o ataque de um Gu de rank quatro, ao menos
dois Gu de rank três seriam necessários para defendê-lo."* Cap. 315, os dois lados da chance:
*"Fang Yuan estimava ter apenas trinta por cento de chance de vencer… Trinta por cento não
parece alto. Mas, considerando o vão entre os dois grandes reinos, trinta por cento já era
bastante notável"* e *"Se eu conseguir refinar aquele Gu, terei sessenta por cento de chance
com a ajuda dele!"*. Entrou com callout de design: **um Gu certo vale tanto quanto todo o resto
do personagem** — 30% é o preço de encarar um degrau acima com o que se tem, 60% é o preço de
ter feito o trabalho de casa.

**21.4 — atenção.** Cap. 314 e vizinhos. Teto de **3** tarefas simultâneas sem erro para um
praticante forte (*"nem o forte Fang Yuan conseguia dividir a mente em quatro por muito tempo
sem cometer erros"*), **5** como máximo documentado e descrito como a mente esticada até o
limite, e a escada de Gu de multitarefa começando no **rank 2** para duas tarefas. Mais a
assimetria do relatório de estudos de caso: manter é grátis, **mudar** cobra. Callout de design
com o contra-jogo que sai disso — contra um multitarefa não se somam ataques, somam-se
**ângulos**.

**21.5 — montagem de golpe.** Cap. 723: *"para formar um golpe assassino de campo de batalha
de nível imortal, ele precisa usar ao menos três Gu Imortais, e esses Gu Imortais precisam
estar conectados de alguma forma"*. Mais a definição de uma linha (quase-terra-abençoada
portátil) e o callout com a regra de resolução por rank.

`fontes` da tabela acrescido de: `cap. 83`, `cap. 314-315`, `cap. 422`, `cap. 443`, `cap. 723`,
`cap. 819-820`, `cap. 852`, `cap. 1033`, `cap. 1346`, `cap. 1938`. Tag `combate` acrescentada ao
frontmatter e a linha `conhecimento:` estendida para cobrir a seção 21 como conhecimento comum.

---

## 5. Verificado e **não** aplicado

### 5.1 A "contradição" 100 marcas ≈ +20% — **não existe**

`PROFUNDIDADE-paths-08-12` levanta, como tensão a registrar, que a obra diria **100 marcas ≈
+20%** (cap. 820) enquanto a fórmula da tabela dá 1,1×. Fui ao capítulo. O texto diz:

> *"Era o mesmo que Fang Yuan poder aumentar o poder da mão gigante em vinte por cento com
> suas marcas do Dao do caminho da força."*

**O capítulo 820 nunca menciona cem marcas.** Ele dá o percentual (20%) e não dá a contagem. E
a contagem, quando a obra a dá, é coerente: cap. 852, *"duzentas marcas do Dao podem aumentar o
poder em vinte por cento"* — ou seja, os ~20% de Fang Yuan correspondem a ~200 marcas, não a
100. Cap. 1033 confirma o outro extremo: *"cem marcas do Dao podiam amplificar o efeito dos Gu
em dez por cento"*.

**Não há contradição a registrar.** A fórmula linear está intacta em todos os pontos. O que fiz
foi o oposto do pedido: em vez de anotar uma tensão inexistente, promovi os pontos de 200 e 600
à tabela, que são justamente os que fecham a fórmula. Registro aqui para que o achado não seja
reintroduzido por uma leitura futura do mesmo relatório.

### 5.2 As sete cores da sorte — **não promovido**

Verificado e correto (caps. 1782 e 1824: *"as sete cores principais da sorte eram preto,
cinza, branco, vermelho, dourado, azul-celeste e roxo — mas havia também cores incomuns como
rosa ou vermelho-sangue"*). Mas é **taxonomia visual, não grandeza de sistema**: não há nada
para consultar nem para resolver com ela. O próprio relatório de origem a propunha condicionada
a "se houver espaço para taxonomias". A tabela soberana existe para arbitrar números que
aparecem repetidos em várias notas; uma lista de cores aparece numa nota só. **Fica em
`03 - Paths/23 - Luck Path.md`**, que já a traz.

### 5.3 O custo posicional da luz da sabedoria — **já estava lá**

O relatório o propõe como acréscimo. Ele já consta da seção 17, na tabela "O preço em anos dos
atalhos": *"Ficar exposto à luz de sabedoria de um Gu de rank 9 — ~2 anos numa exposição breve;
10+ numa longa"*. Conferido contra o texto (cap. 601: *"perdeu ao menos dois anos de vida agora
há pouco"*; cap. 639: *"esteve tão perto do Gu da Sabedoria e suportou a luz da sabedoria por
tanto tempo, e assim perdeu mais de dez anos de vida"*) — os números da tabela estão certos.
Nada a fazer.

### 5.4 O teto de sessão da luz da sabedoria — **não promovido**

O relatório pede que se registre que o teto de sete dias é **função do domínio no caminho
deduzido**, e não uma constante. A observação é correta e está verificada, mas ela é
precisamente o argumento de que **não é um número de sistema**: é um valor variável de um caso.
Uma tabela de consulta que registrasse "sete dias" estaria errada, e registrar "depende" não
serve para consulta. Fica na nota do caminho da sabedoria, que é onde a dependência pode ser
explicada.

### 5.5 O resto da `AUDITORIA-combate` — o que ficou de fora, e por quê

Dos ~60 candidatos da auditoria, promovi os quatro apontados como mais fortes mais os do
relógio, das camadas de defesa e da escada de chance. O grosso dos demais **não subiu**, e o
critério foi consistente: são números **de um item específico**, não do sistema — recarga de um
Gu de deslocamento de rank 2, preço da folha de vitalidade, doses de *guts Gu*, tamanho de uma
prisão citada, número de cativos de uma campanha. Esses pertencem aos catálogos de Gu e às
notas de evento, onde já estão ou deveriam estar; promovê-los à tabela soberana a
transformaria num segundo catálogo e diluiria justamente a função dela, que é **arbitrar
divergências entre notas**. Um número que só aparece numa nota não tem divergência para
arbitrar.

Duas exceções que **vale** alguém promover depois, e que deixo apontadas em vez de aplicar
porque tocam seções que não conferi de ponta a ponta: a escala de ferimentos em quatro degraus
(leve → médio → grave → fatal, e uma aplicação de cura desce um degrau), que é regra de sistema
e não de item; e a escada de coordenação contra um imortal (1 irrelevante · 3 resiste · 6
segura · 9 pressiona), que é a tabela de "quantos precisam" mais geral que a obra oferece.

---

## 6. Contradições registradas (não resolvidas)

1. **Clã Xi × a lista dos catorze.** Casa do Deserto do Oeste com ancestral de rank 8, primeiro
   ancião supremo citado no escalão mais alto da região e cenas próprias — e ausente da
   enumeração canônica das catorze super forças. Duas leituras possíveis (não é formalmente
   super força apesar do rank 8; ou a lista é posterior a alguma mudança). Registrada em
   callout na nota das Grandes Forças, sem escolha.
2. **Catorze × quinze.** O mesmo capítulo que fecha a lista em catorze abre a exceção do clã Yi
   e diz "seriam quinze". Registrado como está: catorze públicas, uma décima quinta oculta.
3. **Piso do rank 8: 100.000 (texto) × 30.000 (aritmética do calendário de provações).**
   Aqui **não** registrei como empate, porque não é contradição entre dois canônicos: é texto
   contra conta nossa, e a regra do vault manda o texto vencer. A conta foi rebaixada a
   "estimativa de rendimento anual" e o vão de 30.000 a 100.000 virou informação de design.
   A tabela soberana já tratava assim; a nota de Dao Marks é que estava desatualizada e foi
   alinhada.

---

## 7. Não toquei

Nada fora dos quatro arquivos meus e deste relatório. Em particular, **não** editei
`06 - Forcas e Organizacoes/05 - Deserto Ocidental.md` (li inteira, apontei para ela),
`03 - Paths/23 - Luck Path.md`, `03 - Paths/04 - Strength Path.md`,
`03 - Paths/14 - Space Path.md` nem `12 - Soul Path.md`. Nenhum `git add` ou `git commit`
partiu de mim.

**Nota de processo.** No meio do meu trabalho, outro processo da sessão rodou um commit
(`229c01f`) que capturou parte das minhas edições junto com as dele. Não é problema — o
conteúdo está em disco e versionado —, mas explica por que `git diff` mostra pouca coisa
nos meus arquivos: quase tudo já está commitado por aquele hash, e não pelo que eu fiz. Se
alguém for auditar meu trabalho pelo diff da árvore, vai achar que não fiz quase nada;
audite pelo conteúdo dos arquivos, não pelo diff.
