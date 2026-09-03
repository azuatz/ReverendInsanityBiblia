# Triagem da pasta `09 - Eventos e Cenarios`

Data: 2026-09-03. Estado inicial: 29 arquivos (`01` nota-porta + `02`–`29`, 28 cenários).
Estado final: **28 arquivos** (`01` nota-porta + 27 cenários). Uma nota reprovada e removida com
`git rm`, com o conteúdo reaproveitável migrado antes.

## O critério aplicado

A pergunta que decidiu tudo, na formulação do usuário: **"isso vai agregar para o mestre numa mesa
de RPG?"** As três portas do briefing não são o critério — são as três maneiras de passar nele:

1. **Fenômeno recorrente que o mestre molda** (acontece em qualquer lugar; ele só troca os detalhes);
2. **Lugar com regras próprias e permanentes** (quem chega lá encontra aquilo, sempre);
3. **Acontecimento de escala de mundo** encaixável como pano de fundo ou clímax.

Reprova o **episódio particular da trajetória de um personagem da obra**. Escala não decide: um
cenário pequeno com regras próprias e relógio vale mais que um acontecimento grandioso que só
interessa a quem queira reencenar o livro.

Duas armadilhas de leitura do critério, e como foram resolvidas nesta pasta:

- **"Específico" não é sinônimo de "reprovado".** Um lugar único e permanente passa pela porta 2.
  O que reprova é o *episódio irrepetível*, não o lugar raro.
- **Um lugar consumido uma vez na obra continua passando pela porta 2**, desde que a nota esteja
  escrita como *lugar que produz aquilo sempre que alguém chega* — e desde que diga à designer que
  a campanha dela não segue a mesma história e ela pode pôr o lugar intacto onde quiser. Onde faltava
  esse enquadramento, ele foi acrescentado (ver seção "Reenquadramento").

## Tabela de triagem

| Nota | Veredito | Justificativa | O que foi feito |
|---|---|---|---|
| `01 - Visão Geral dos Eventos` | nota-porta | — | Reescrita: critério na abertura, contagens, "leia estes primeiro" e tabela de escolha rápida |
| `02 - A Maré de Lobos de Qing Mao Shan` | **REPROVA** | Decidido pelo usuário. É o episódio *daquela* montanha na trajetória do protagonista, e a categoria já está coberta por `03`. Na campanha da designer aquela montanha pode nunca existir; alguma maré, sim | Conteúdo migrado para `03` como exemplo trabalhado; arquivo removido com `git rm`; 6 links redirecionados |
| `03 - Marés de Bestas` | porta 1 | O caso-modelo citado pelo próprio usuário: acontece em qualquer lugar com fauna, e o mestre só decide qual é a besta | **Absorveu `02`**: nova seção "Exemplo trabalhado", frontmatter fundido (21 capítulos e 2 aliases novos) |
| `04 - Desastres Locais e Problemas Crônicos` | porta 1 | Nota de **categoria** com quatro moldes de desastre local (acidente ambiental, calamidade climática, infestação crônica de rota, terreno proibido sob a vila). O sapo do rio já está aqui como *tipo* — "a criatura no lugar errado" —, não como episódio | Só o link para `02` redirecionado |
| `05 - Feiras, Caravanas e Festivais` | porta 1 | Aprovado explicitamente pelo usuário: acontecem em todo lugar e os jogadores vão topar com um | — |
| `06 - Assembleias, Alianças e Quadros de Mérito` | porta 1 | Instituição recorrente em quatro escalas; o quadro de méritos é a peça mais reutilizável do vault | Link para `02` redirecionado |
| `07 - Torneios, Arenas e Duelos` | porta 1 | Formato recorrente em cinco escalas, com calendário fixo em várias delas | Link para `02` redirecionado |
| `08 - Aberturas de Herança` | porta 1 | Categoria: heranças abrem em qualquer lugar do mundo, por programação do dono ou por acidente | — |
| `09 - A Herança dos Três Reis` | porta 2 | Lugar com regra de porta própria (um único Gu de rank 1) e cem rodadas. Na obra é consumido: a terra abençoada morre | **Reenquadrada** |
| `10 - A Subida da Montanha Dang Hun` | porta 2 | Lugar com regra de porta própria (todos os Gu selados, sem morte, tempo acelerado). Na obra tem herdeiro único | **Reenquadrada** |
| `11 - Os Cacos do Céu Estrelado` | portas 2 e 3 | O cataclismo é de escala de mundo; o caco é um formato de lugar com prazo e trava física ("o gigante quebra a casa") reproduzível por qualquer mundo antigo que se despedace | **Reenquadrada** |
| `12 - As Terras Ferozes e o Subsolo do Mundo` | porta 2 | O caso mais limpo: "não abrem nem fecham, estão sempre lá". A nota já se abre assim | — |
| `13 - O Paraíso da Baleia-Dragão e o Obelisco de Mérito` | porta 2 | Sistema de missões que continua **sem dono** depois de várias expedições ao longo das eras | **Reenquadrada** |
| `14 - O Ciclo Decenal das Planícies do Norte` | portas 1 e 2 | Relógio declarado de dez anos sobre uma região permanente; a cadeia assembleia → guerra → torneio é molde | — |
| `15 - O Edifício dos Oitenta e Oito Andares` | porta 2 | Construção que **se remonta sozinha** a cada dez anos; ninguém a esvazia | **Reenquadrada** |
| `16 - A Montanha Yi Tian` | porta 2 (duas vezes) | Fronteiriça, resolvida pelo teste de utilidade. Era um: a zona proibida existe enquanto a fortaleza enterrada funcionar, e **cresce** — mais o contrato de apostas, peça de desenho reaproveitável inteira. Era dois: a própria nota a chama de "situação, não episódio", estável por anos. Nenhuma das duas depende de personagem nomeado | **Reenquadrada** |
| `17 - Caçadas, Emboscadas e Fugas` | porta 1 | É explicitamente um **formato**, não um acontecimento: mesma estrutura da aldeia ao continente | — |
| `18 - Quando uma Força Morre` | porta 1 | Rescaldo é consequência estrutural de duas regras enunciadas pela obra; acontece o tempo todo, em qualquer escala | — |
| `19 - Cercos e Invasões de Terras Abençoadas` | porta 1 | Categoria: procedimento geral de assalto a mundo privado, com gatilhos recorrentes (cofre sem dono, recurso estratégico, janela de calamidade) | — |
| `20 - O Cerco da Montanha Nevada e o Rio de Fluxo Reverso` | porta 2 | **A decisão de fronteira mais difícil da pasta** — ver abaixo | **Reenquadrada**, separando explicitamente as duas metades |
| `21 - Calamidades e Tribulações como Cenário` | porta 1 | Calendário: a mais comum vem a cada dez anos de tempo interno, e cai sobre todo dono de abertura imortal | — |
| `22 - Leilões, Cúpulas e Guerras de Mercado` | porta 1 | Instituição permanente do mundo, com trégua obrigatória como regra de casa | — |
| `23 - A Cerimônia das Miríades de Tribos e a Estrada da Vida` | porta 2 | Mundo fechado permanente + periodicidade declarada + regras de torneio escritas. A própria nota observa que é o material mais próximo de um módulo pronto | **Reenquadrada** |
| `24 - A Grande Era e as Marés de Qi` | porta 3 | Mudança de era: o mapa e as regras ambientais mudam para todo mundo, onde quer que a mesa esteja | — |
| `25 - A Guerra do Destino` | porta 3 | Aprovada explicitamente pelo usuário ("um evento tipo Shibuya, só que de Reverend") | — |
| `26 - A Caverna do Demônio Enlouquecido` | porta 2 | Masmorra **permanente** de nove camadas, listada entre as grandes áreas ferozes da região; as camadas rasas recebem expedições pequenas o tempo todo | **Reenquadrada** |
| `27 - A Morte do Sol e o Céu Espectral` | porta 3 | Cataclismo que deixa cinco regras ambientais **permanentes** diferentes: vira cenário-base, não episódio | — |
| `28 - O Mundo em Véspera de Guerra` | porta 3 (ambientação) | Não é cenário e a nota já avisa isso em callout. Passa como **estado do mundo**: um mestre escolhe rodar a campanha nessa era e tudo o que está aqui vale de graça | — |
| `29 - Eventos Históricos de Fundo` | porta 3 (consulta) | Não é cenário e a nota já avisa isso. Passa como **referência**: responde "por que isto está aqui no mapa?" e fornece ganchos com séculos de idade. Utilidade real para quem improvisa | — |

Contagem final: **27 cenários** — 11 entram pela porta 1 (fenômeno recorrente), 11 pela porta 2
(lugar com regras próprias) e 5 pela porta 3 (escala de mundo). Duas passam por mais de uma porta:
`11 - Os Cacos do Céu Estrelado` (2 e 3) e `14 - O Ciclo Decenal` (1 e 2). Duas das que entram pela
porta 3 — `28` e `29` — servem como ambientação e consulta, não como sessão rodável, e estão
marcadas assim na tabela de escolha rápida.

## O conteúdo migrado, e para onde

Tudo o que `02` tinha de reaproveitável foi para **`03 - Marés de Bestas`**, numa seção nova ao fim
da nota chamada **"Exemplo trabalhado: como se monta uma maré de um ano inteiro"**, reescrita de
"o que aconteceu naquela montanha" para "assim se monta uma". Nenhum nome de lugar foi mantido: o
tabuleiro é descrito por função (uma montanha florestada, três vilas-clã rivais, o clã mais fraco
embaixo e por isso sempre o primeiro atingido).

Migrou:

- **O tabuleiro e a trava local** — três clãs, aldeias mortais sem muro no sopé, teto de rank 4 na
  montanha, menos de cinquenta rank 5 na região inteira, e o rank 5 itinerante cuja justificativa
  para ajudar é doutrinária.
- **As nove fases em ordem**, como tabela — incluindo o prelúdio de um ano antes, a anomalia de
  cronograma que anuncia a maré excepcional, as semanas de negociação de aliança, os cercos de seis
  dias, a escalada de reis e o rescaldo.
- **As três coisas que só um rei de miríade de bestas faz** (cerco reverso, o Gu de fumaça que anula
  cem li de campo de batalha, a escolha deliberada de alvos).
- **As dez regras de uma montanha mobilizada** — mobilização obrigatória, regra do grupo perdido,
  interrogatório no rescaldo, trégua entre aliados, proibição de matar aliado com grupo investigador
  dedicado, entrega obrigatória do Gu tirado de cadáver, a fraqueza estrutural da espécie (visão de
  águia e olfato humano), a batalha noturna de inverno em grupos de cinco ou seis, a vila com nove
  em cada dez casas vazias, e a suspensão da fiscalização enquanto a maré durar.
- **Os números do custo** — menos de um décimo de sobrevivência estimada, metade da população
  perdida no balanço real, uma vila-clã inteira extinta, o gargalo dos pouco mais de vinte anciãos
  rank 3, e a barra de essência primordial como relógio real de cada expedição.
- **O bloco "Para o design"** (a campanha com calendário, as três engrenagens, o ritmo alternado
  floresta/vila) e **as lacunas** da obra, convertidas em callout `[!question]`.
- **Frontmatter**: 21 capítulos de `02` que faltavam em `03` foram somados ao campo `fontes`, e os
  aliases `Wolf Tide` e `Maré de Lobos` acrescentados para que buscas por eles caiam na categoria.

**Não migrou** (já estava melhor documentado em outro lugar): o **quadro de méritos** com o olho de
lobo valendo dez pontos, o palco da praça e o estandarte de Gu de Palavra Nadadora — a nota
`06 - Assembleias, Alianças e Quadros de Mérito` já traz tudo isso, mais completo, na seção "Escala
pequena: a vila em guerra". `03` aponta para lá.

## Reenquadramento (porta 2)

Nove notas descrevem lugares. Todas já estavam escritas como situação — sem nome de personagem, com
gatilho, trava, relógio e leque de desfechos —, mas **nenhuma dizia à designer que a campanha dela
não segue a mesma história**. Sem isso, um lugar que na obra é consumido uma vez lê-se como episódio
encerrado. Cada uma recebeu um callout `> [!note] Como pôr isto na sua campanha`, logo depois da
nota de confiabilidade e antes de "O essencial", dizendo três coisas: que aquilo é um lugar com
regras próprias e não o relato de uma vez em que alguém foi lá; se na obra o lugar é consumido,
reclamado ou destruído de uma vez só; e que o mestre pode pô-lo intacto, com outro nome e em outra
região, porque a campanha não repete o enredo.

Notas alteradas: `09`, `10`, `11`, `13`, `15`, `16`, `20`, `23`, `26`.

Duas receberam texto além do padrão:

- **`16 - A Montanha Yi Tian`** — o callout diz explicitamente que a era um pode simplesmente *ainda
  não ter terminado* na campanha da designer (na obra ela acaba quando alguém refina a fortaleza), e
  nomeia as três peças que fazem o cenário e sobrevivem à mudança de lugar: a trava de porta, o
  contrato de apostas e o condomínio de treze vizinhos armados.
- **`20`** — o callout separa as duas metades por natureza, porque elas são coisas diferentes
  (detalhe abaixo).

`12 - As Terras Ferozes` não precisou: já abre dizendo "gatilho: nenhum; estão sempre lá, não abrem
nem fecham".

## Links redirecionados

Nenhuma nota alheia foi editada além do link.

| Arquivo | Antes | Depois |
|---|---|---|
| `00 - Trilha do Jogador.md` | `[[02 - A Maré de Lobos…]] · [[02 - Marés de Bestas|03 - Marés de Bestas]] · …` | link removido da lista; `Marés de Bestas` passa a abrir a linha |
| `09/01 - Visão Geral dos Eventos.md` | linha 1 de "Leia estes primeiro" | trocada por `Marés de Bestas`, com a menção ao exemplo trabalhado |
| `09/01 - Visão Geral dos Eventos.md` | linha própria na tabela de escolha rápida | removida; a linha de `Marés de Bestas` ganhou a menção à campanha de vila |
| `09/03 - Marés de Bestas.md` | dois ponteiros "o exemplar completo está em `02`" | passaram a apontar para a seção interna nova |
| `09/04 - Desastres Locais…` | "a montanha onde os Casos A e D acontecem" | fundido com o ponteiro que já existia para `03` |
| `09/06 - Assembleias…` | "a ameaça que convoca a assembleia da escala 1" | aponta para `03`, citando o exemplo trabalhado |
| `09/07 - Torneios…` | "a crise cujo rescaldo produz a competição da escala 1" | aponta para `03` |

`python3 _pipeline/auditar-links.py`: **218 notas, 5368 links, 0 quebrados, 262 âncoras, 0 âncoras
quebradas.**

## Decisões de fronteira, com a alternativa descartada

**`20 - O Cerco da Montanha Nevada e o Rio de Fluxo Reverso` — a mais difícil.** O paralelo com o
caso já decidido é exato: assim como `02` era o exemplar específico da categoria `03`, o cerco da
montanha nevada é o exemplar específico da categoria `19 - Cercos e Invasões de Terras Abençoadas`.
*A alternativa descartada era reprovar a nota, migrar o cerco para `19` como exemplo trabalhado e
abrir uma nota só para o rio.* Não foi feito por duas razões. A primeira é que as duas metades não
são da mesma natureza: **o rio é um lugar** — um domínio autônomo com leis próprias que continua
existindo no mundo depois, muda de dono uma vez a cada centenas de milhares de anos e faz a mesma
coisa com todo mundo que cai nele; passa pela porta 2 sem discussão, e reprovar a nota exigiria
recriá-la. A segunda é que **o cerco não é um episódio, é um conjunto de regras de porta**: a
formação teleporta qualquer invasor para o pico do rank dele e proíbe o senhor de cada pico de sair
— inclusive o rank 8, proibido de descer para esmagar os fracos. Isso é pendurável em qualquer terra
abençoada que a campanha precise sitiar, e é a trava mais limpa do vault para o problema real de uma
mesa de alto nível. Solução adotada: manter a nota e **dizer no próprio texto qual metade é o quê** —
o cerco como exemplar trabalhado da categoria `19`, o rio como lugar —, avisando que os dois podem
ser usados separados.

**`16 - A Montanha Yi Tian`.** *A alternativa descartada era reprovar a era um* (uma guerra de cem
dias que na obra acontece uma vez) *e migrar o contrato de apostas para `06 - Assembleias, Alianças
e Quadros de Mérito`.* Descartada pelo teste de utilidade: a zona proibida é uma propriedade
permanente daquela montanha, cresce com o tempo e só termina se alguém refinar a fortaleza — quem
chegar lá antes disso encontra exatamente aquilo. E o pacote inteiro (mortais de rank 3 a 5 como
único poder em campo, patronos imortais que lucram com o quanto o peão luta, escalada programada por
contrato) é a demonstração mais completa da pasta do que uma trava canônica faz por uma mesa.
Reprovar teria destruído mais valor do que o desmembramento devolveria.

**`09` e `10` (as heranças nomeadas).** *A alternativa descartada era fundir as duas em
`08 - Aberturas de Herança` como exemplos e apagá-las.* Descartada porque cada uma carrega um
**conjunto de regras próprio e completo** — a de rank 1 único com cem rodadas de um lado, o
selamento total de Gu com prova de fundação de alma do outro — que uma nota de categoria não
comporta sem virar duas notas grudadas. São lugares, e lugares passam pela porta 2; o problema real
delas era só de enquadramento, e foi corrigido.

**`28` e `29` (as duas que não são cenário).** *A alternativa descartada era mover as duas para
`04 - Mundo` por não terem gatilho, trava nem relógio.* Descartada pelo teste de utilidade: o mestre
que abre esta pasta para montar uma campanha usa `28` para escolher a era em que vai jogar e `29`
para responder "por que isto está aqui?" e pendurar ganchos antigos. As duas já se declaram não
cenário em callout próprio e estão marcadas como tal na tabela de escolha rápida — não há risco de a
designer procurar uma sessão ali e não achar.

**`04 - Desastres Locais e Problemas Crônicos` e o sapo.** O sapo que entupiu o rio é o outro exemplo
de reprovação que o usuário deu, e ele **não** foi removido: já está aqui como *tipo* — "Caso A: a
criatura no lugar errado" — dentro de uma nota de categoria que traz quatro moldes de desastre
local. É exatamente o destino que o critério prescreve para material reprovado como cenário próprio.
O estudo mecânico correspondente vive em `10 - Estudos de Caso Mecanicos` e é assunto de outra
triagem.

## Pendência para o coordenador

O arquivo `02` foi removido e a entrada correspondente foi tirada da lista `ORDEM` em
`_pipeline/numerar-notas.py`, mas **a renumeração não foi rodada**: `python3 _pipeline/numerar-notas.py`
renumera o vault inteiro e outras pastas estão sendo triadas em paralelo — rodá-lo agora poderia
colidir com trabalho em andamento. A pasta está hoje com os prefixos `01`, `03`–`29` (um buraco no
`02`), o que é cosmético e não quebra nenhum link. Quando todas as triagens fecharem, rodar
`numerar-notas.py` e depois `auditar-links.py` fecha o assunto.
