# Revisão de leitora leiga — `09 - Eventos e Cenarios` e `06 - Forcas e Organizacoes`

**Papel assumido:** designer profissional de RPG de mesa que **nunca leu Reverend Insanity** e
não vai ler. Tudo o que ela sabe vem destas 35 notas.

**Escopo:** as 29 notas de `09 - Eventos e Cenarios/`, as 6 de `06 - Forcas e Organizacoes/`.
Nenhum arquivo fora dessas duas pastas foi alterado.

**Classificação:** **bloqueador** (impede trabalhar, ou mente para a leitora) · **sério**
(pressupõe leitura da obra, regra sem uso em mesa, seção que promete mecanismo e entrega
rótulo) · **menor** (repetição, frase confusa, link para o lugar menos útil).

---

## Verificações mecânicas

| Verificação | Resultado |
|---|---|
| `python3 _pipeline/auditar-links.py` — antes e depois | **0 links quebrados** nas duas medições |
| Âncoras de seção (`[[Nota#Seção]]` e `[[#Seção]]`) — auditoria própria, o script do vault não as cobre | 1 quebrada durante o trabalho (eu mesma quebrei ao normalizar um termo), **corrigida**; 0 no fim |
| Wikilinks partidos por quebra de linha | 9 nas minhas pastas, **todos unidos** (o Obsidian não resolve wikilink que atravessa `\n`) |
| Pipes não escapados dentro de wikilink em célula de tabela | 70 nas minhas pastas — **e 223 no resto do vault**. É padrão do vault inteiro e o Obsidian resolve `[[Nota\|texto]]` em tabela. **Não é defeito; não mexi.** |
| Números conferidos contra `11 - Apendices/02 - Tabelas de Referência Rápida.md` | escala de li, tamanho de região, grades e fluxo de terra abençoada, cadência de provações, escala das essências imortais, demografia por rank, pedágios por anel, níveis de attainment. Divergências abaixo. |
| Fatos conferidos no texto-fonte com `grep` | 6 (filiais da Aliança dos Zumbis, preço do título "boa pessoa", gruta-céu de Hei Fan, sede da Chu Sect, queda de uma vila na maré de lobos, os 600 li / 8 minutos de aviso) |

---

## Veredito de conjunto

### Pasta de eventos — **muito boa, e a regra que a governa foi cumprida**

Li as 29 notas procurando enredo vazado e **não achei spoiler de história em nenhuma**. Isso é
notável, porque a matéria-prima é hostil: notas 25, 26, 27 e 28 tratam do fim da obra e as três
primeiras trazem um aviso próprio no topo dizendo exatamente o que ficou de fora. Personagens
nomeados aparecem só como função ("o fundador da herança", "o dono da montanha"); as duas
exceções — o Venerável Imortal Sol Gigante e o Venerável Paradise Earth — são figuras históricas
estruturais, e sem elas nem a Corte Imperial nem o Obelisco de Mérito se explicam. **Nenhum
desfecho de personagem, nenhuma traição, nenhuma morte nomeada.**

As três coisas que o briefing manda verificar estavam quase todas no lugar. A **trava canônica**
estava dita em 25 das 29 notas, mas nomeada e ligada ao cardápio em só 20 — corrigi as nove que
faltavam, e o cardápio da nota-porta ganhou três travas que a pasta usava sem ter listado. Os
**relógios** já estavam em fases utilizáveis em todas as notas de cenário menos uma (a de
caçadas, que era um formato sem ritmo declarado — escrevi um). A seção **"o que um grupo de
personagens faz aqui"** é concreta por faixa de rank em toda a pasta, e é o melhor conteúdo dela:
"colher olhos de lobo", "tapar buracos no céu", "guardar a entrada para o fim da tarde e caçar
quem já juntou fichas" são instruções de mesa, não adjetivos.

O que puxava a pasta para baixo era **vocabulário**: a mesma coisa aparecia com dois ou três
nomes diferentes entre notas vizinhas (gruta-céu/caverna-céu, parede/barreira/muralha regional,
pedra/pérola de essência imortal). Para quem já leu a obra isso é ruído; para quem só tem estas
notas, é a suspeita de estar diante de duas coisas distintas. Normalizado.

### Pasta de forças — **o conteúdo é excelente e a embalagem estava desalinhada**

As fichas são densas do jeito certo: cada casa tem uma razão histórica para a especialidade
(quase sempre uma herança encontrada, como o briefing previa — clã Wu e a herança do caminho da
força, clã Shang e o Mar de Sangue, tribo Liu e o Campo de Sepultamento de Ossos, clã Tang e o
reino onírico achado por acaso), e as **tensões internas entraram de verdade**, inclusive as
desconfortáveis: o vassalo mais leal do sul com um espião no terceiro ancião supremo do suserano;
o clã Chai drenando a aptidão de forasteiros e sendo do caminho correto; praticantes demoníacos
como anciãos externos no norte, na arena do clã Shang e no terceiro posto da Seita da Grua
Imortal. Isso é exatamente o que faz uma mesa render.

Os problemas eram estruturais, não de conteúdo. **O gabarito prometido pela nota-porta não valia
para três das cinco notas regionais**: 04 e 05 não traziam o bloco de recorte temporal, e a
coluna "por que importa numa mesa" — que a própria nota-porta manda a designer ler para escolher
a força antagonista — só existia em 02 e 03. Corrigido nas três. E as **armadilhas de leitura**
da nota-porta tinham um erro de fato e uma lacuna grande, ambos descritos abaixo.

---

## Bloqueadores — todos corrigidos

**1. A nota-porta das forças mentia sobre a Aliança dos Zumbis.** A regra 11 dizia "a obra não
mostra filial no Continente Central". O texto-fonte diz o contrário duas vezes: *"its main
headquarters is in eastern sea, with a branch in each of the other four regions"*, e há cena com
*"central continent's Zombie Alliance branch"*. As notas 02, 05 e 06 estavam certas e a nota-porta
errada — ou seja, a nota que a designer lê primeiro contradizia as três que ela leria depois.
**Corrigido**, com a hierarquia canônica junto (só a sede é mais forte que as super forças
locais; as filiais são todas mais fracas e suprimidas).

**2. A mesma região com dois nomes.** As cinco notas regionais chamavam a região de **"Mar do
Leste"** (21 ocorrências) enquanto a nota-porta, a pasta de eventos, o glossário e o próprio nome
do arquivo dizem **"Mar Oriental"**. Uma leitora que encontra "o clã Xia do Mar do Leste" na nota
do sul e "Mar Oriental — a mais fraca das super forças locais" na nota-porta não tem como saber
que é a mesma casa. **Normalizado para "Mar Oriental"** (padrão do glossário), preservando "Mar
do Leste" como alias na nota da região, que é onde ele serve.

**3. A gruta-céu de Hei Fan, contada duas vezes de formas incompatíveis.** Na mesma nota
(Planícies do Norte), a ficha da tribo Hei dizia em "O que a obra não diz" que *"a obra não diz o
que aconteceu com a gruta-céu que Hei Fan deixou"*, e a ficha da Chu Sect, três fichas adiante,
dava essa mesma gruta-céu como **território dela**. Conferi no texto: os quatro anciãos supremos
do topo da tribo Hei **sabem** onde ela fica (é "o maior segredo da tribo") e escondem dos
próprios membros; e a Chu Sect só passa a ocupá-la **depois de um evento de enredo**, o que viola
o recorte temporal declarado da pasta. **Corrigido nas duas fichas**, com o segredo marcado e o
recorte explicitado; a tabela-resumo foi ajustada junto.

**4. Preço do título "boa pessoa" — as duas pastas se contradiziam.** A nota de evento 13 listava
o preço como desconhecido ("O preço do primeiro título… Sabe-se o dos outros dois") e a nota do
Mar Oriental dava **100 pontos**. O texto-fonte confirma os 100 (*"Chu Ying spent a hundred merit
points"*). **Corrigido na nota 13**, e aproveitei para explicar por que o terceiro título é mais
barato que o segundo — o que parece erro de digitação e é canônico.

**5. "Caverna-céu" × "gruta-céu" para a mesma coisa.** As notas 19, 21, 22 e 23 usavam
*caverna-céu*; as notas 11, 12, 24, o glossário e a nota que **define** o conceito usam
*gruta-céu*. Pior: a nota 21 apresentava "caverna-céu (*grotto-heaven*)" como se estivesse
introduzindo um termo novo. **Normalizado**, mantendo o inglês entre parênteses nas definições.

**6. Wikilinks cujo texto nomeia uma região e cujo destino é outra nota.** Na nota do Mar
Oriental, `[[11 - Cultura das Cinco Regiões|Planícies do Norte]]` e a mesma coisa com "Fronteira
Sul": a leitora clica no nome de uma região e cai numa nota de cultura. Na nota do Deserto
Ocidental, `[[02 - Clãs|Fronteira Sul]]`. **Corrigidos os três**, e rodei uma varredura própria
para garantir que não havia mais nenhum caso nas duas pastas.

---

## Sérios — todos corrigidos

**7. A conta das Dez Terras não fechava.** A nota 12 dizia "**Seis** das Dez Terras aparecem
apenas na lista" e listava **cinco** nomes — e contava como não descrita a Trincheira da Terra,
que tem seção própria na mesma nota. A nota 24 repetia o erro com "**Quatro**", esquecendo o
Túnel da Terra. **Corrigido nas duas** (cinco descritas, cinco só como nome), e as dez ganharam o
mesmo nome em português nas duas notas — a 24 as listava em inglês, a 12 em português.

**8. O gabarito prometido não valia para três notas regionais.** A nota-porta afirma que *"toda
organização das cinco notas regionais é descrita no mesmo formato, na mesma ordem"* e manda ler
*"a coluna 'por que importa numa mesa'"* das tabelas-resumo. Na prática: 04 e 05 não tinham o
bloco de gabarito nem o recorte temporal, 06 tinha o recorte só no fim e sobre outro assunto, e a
coluna prometida existia em 2 de 5 tabelas. **Escrevi o bloco em 04, 05 e 06** e **acrescentei a
coluna nas três tabelas** — as 21 linhas do Continente Central com conteúdo novo, as de 05 e 06
renomeadas porque o conteúdo já respondia à pergunta.

**9. A lista de homonímias da nota-porta cobria dois casos de mais de uma dúzia.** Ela registrava
"Yao e Gong" como clã no sul/oeste e tribo no norte. As notas regionais trazem também Qiao, Chai,
Yang, Fei, Tang, Song, Su, Lin, Shen, Ba e Ni repetidos entre regiões, com diferenças de porte
brutais — o Song do Mar Oriental é a casa com mais Gu Imortais de toda a obra e o Song da
Fronteira Sul é um nome numa lista. **Substituí o item por uma tabela de treze pares**, marcada
`(ded.)` como homonímia.

**10. A nota "Quando uma Força Morre" não tinha trava nem desfechos.** Era a única nota de
cenário da pasta sem "Desfechos possíveis", e a única que descrevia a sua trava (o rank 8 morreu,
saiu ou nunca existiu) sem dizer que era uma trava. **Acrescentei as duas seções**, os desfechos
construídos só com o que a própria nota já afirma.

**11. Nove notas descreviam a trava sem nomeá-la nem ligar ao cardápio.** Notas 03, 14, 15, 16,
17, 19, 20, 22, 23, 25, 26, 27 e 28. Sem o número e o link, a leitora não consegue fazer o que a
nota-porta manda: *escolher a trava antes de desenhar o evento*. **Todas ganharam a marcação e o
link.** No caminho, descobri que **três travas que a pasta usa não estavam no cardápio** e as
acrescentei: *o poderoso é o alvo, não o socorro* (calamidades — a provação é calibrada pelo
poder de quem a sofre, então pôr um personagem mais forte no grupo não facilita nada), *o lugar
que enlouquece quem entra* (a caverna, onde a profundidade depende de attainment e não de rank) e
*o prêmio que os fracos não podem tocar* (a chuva de fogo, em que os fracos não competem pela
posse e sim pelo mercado que ela cria).

**12. A escada de attainment em cinco degraus, contra os nove nomeados da tabela soberana.** A
nota das Planícies do Norte dava "comum, mestre, grão-mestre, grande-grão-mestre, supremo
grão-mestre" — e duas linhas adiante usava "quase-grande-grão-mestre", degrau que a própria
escada não listava. A tabela soberana avisa explicitamente que **são nove degraus** e que omitir
os "quase" desalinha tudo. **Corrigido**, com link para a tabela.

**13. Três nomes para a parede regional.** *Parede regional* (glossário e nota 24/25), *barreira
regional* (nota 17 e a nota-porta) e *muralha regional* (notas de forças 01 e 06) conviviam nas
minhas pastas para a mesma membrana. **Normalizado para "parede regional"**, que é o termo do
glossário — preservando a âncora `#13.7 Travessia de barreira regional, por rank`, que é o título
real de uma seção fora do meu escopo.

**14. "Pérola de essência imortal" — uma quarta unidade monetária que não existe.** Notas 19 e 21
usavam esse termo; o vault define duas unidades (a **pedra** de essência imortal, que circula, e a
**conta**, que é combustível pessoal e intransferível) e nenhuma se chama pérola. A própria nota
19 usava "pedra" três parágrafos adiante. **Normalizado para "pedra".**

**15. A Aliança dos Zumbis com dois alinhamentos.** "Neutra" nas notas do Norte e do Mar Oriental,
"demoníaca `(ded.)`" na tabela-resumo do Deserto Ocidental — e "filiais nas cinco regiões" na
mesma nota, contra "uma em cada uma das outras quatro" das demais. **Uniformizado.**

---

## Menores — corrigidos

- **Nota 29** dizia que a destruição de três clãs centenários era "notícia de mesa de bar a
  algumas centenas de **quilômetros**", enquanto as notas 02 e 18 dizem "centenas de **li**" para
  o mesmo fato. Como a regra da pasta manda marcar toda conversão, ficou em li com a conversão
  `(ded.)` ao lado.
- **Nota 05 (feiras)**, tabela de pedágios: listava "Primeiro anel interno pago — 100" **antes**
  de "Quarto anel interno — 200", sem dizer que os anéis são numerados de dentro para fora. Lido
  de cima para baixo, parecia que o primeiro anel era mais barato que o quarto. Acrescentei a
  regra de numeração e identifiquei cada anel.
- **Nota 21:** "perdeu seiscentos e sessenta e seis quilômetros quadrados de quatro mil e quarenta
  anos de desenvolvimento" — a frase se lê errado na primeira passada. Reescrita.
- **Nota 28** anunciava "**spoiler zero**". É verdade sobre a guerra que dá nome à nota (ela nunca
  é encenada), mas a nota descreve o estado do mundo no **fim da obra**. Mantive a promessa
  correta e acrescentei a ressalva de que esta é a nota a entregar por último a quem ainda vá ler.
- **Nota 02 (Maré de Lobos):** a fase 8 afirmava que uma vila-clã cai, e a seção de desfechos —
  que declara listar "o leque estrutural, não o que a obra registrou" — oferecia a mesma queda
  como escolha da mesa. Conferi no texto (é canônico, o clã Xiong é exterminado pelo lycan) e
  reconciliei as duas: a fase descreve a curva de pressão, a decisão é da mesa.
- **Nota 02 (Fronteira Sul):** a ficha do clã Wu dava "caminho da força" como caminho de casa e,
  meia página adiante, dizia que **uma única pessoa na região inteira** fez carreira nele. As duas
  coisas são verdade (o clã *detém* a herança, não a pratica em massa), mas juntas se leem como
  contradição. Explicitado — e virou um gancho melhor do que era.
- **Nota 02 (Fronteira Sul):** o clã Fei aparece três vezes no corpo da nota (suprimido pelo Wu,
  rival do Yi, citado ao lado de Wu/Tie/Shang) e **não está na lista dos treze**, o que a leitora
  só descobre 1.100 linhas depois. Acrescentei a remissão no ponto em que a lista é dada.
- **Nota 04 (Continente Central):** "Fronteira do Sul" → "Fronteira Sul"; "Deserto do Oeste" →
  "Deserto Ocidental".
- **Notas 02, 03 e 06 (forças):** *grotto-heaven*, *blessed land*, *Hai Shi blessed land*, *Jian
  Wen blessed land* apareciam crus no meio de prosa que já usava as formas em português, às vezes
  no mesmo parágrafo. Normalizados, com o inglês preservado em itálico onde ele identifica o nome
  original.
- **Nota 17 (Caçadas):** era a única nota de cenário sem relógio. Escrevi um de sete fases, todo
  derivado do que a nota já afirmava, marcado `(ded.)`.

---

## O que ficou aberto, e por quê

1. **"Mar do Leste" persiste em `05 - Sociedade/13 - As Grandes Forças do Mundo.md`** (15
   ocorrências) e em duas outras notas fora do meu escopo. Enquanto isso não for normalizado, a
   designer que sair da minha pasta vai reencontrar o nome antigo. Não toquei: não são meus
   arquivos.
2. **"Muralha regional" persiste em 47 lugares no resto do vault**, contra "parede regional" (48)
   e "barreira regional" (19, incluindo o título da seção 13.7 da tabela soberana). O glossário
   fixa "parede regional". Isso pede uma passada única no vault inteiro, com cuidado com o título
   daquela seção, porque ele é alvo de âncora.
3. **A tabela soberana registra que o tamanho do Continente Central "não fecha"** e que o Atlas
   propaga a leitura ruim. Minhas notas não citam o número, então não há nada a corrigir aqui —
   fica o registro de que a lacuna existe a montante.
4. **A tag `mundo/grotto-heaven`** continua no frontmatter da nota 23. Mexer em tag é mexer em
   busca transversal do vault inteiro; deixei para uma decisão de conjunto.
5. **Sete das dez grandes áreas de mar, seis das dez super forças do Mar Oriental e cinco das Dez
   Terras** continuam sem nome ou sem descrição. Isso **não é defeito**: as notas declaram cada
   uma dessas lacunas em "O que a obra não diz", que é exatamente o comportamento certo.
6. **A nota 22 não tem um relógio único**, só um por formato (e são cinco formatos). Achei
   defensável e não mexi — mas se a pasta quiser uniformidade absoluta, é o último furo.

---

## As três coisas que eu mudaria com mais tempo

**1. Um índice de "onde está cada número" no topo da pasta de eventos.** As notas repetem, com
razão, o aviso de que a tabela soberana vence em caso de divergência — mas nenhuma diz *quais*
números ela contém. Conferi 29 notas contra ela à mão e encontrei divergências reais (a escada de
attainment, o preço do título, três unidades monetárias). Um bloco de dez linhas na nota-porta
dizendo "escala e viagem: seção 13; provações: seção 8; terras abençoadas: seção 9; attainment:
seção 10; preços: seção 19" pagaria a si mesmo na primeira sessão — e teria evitado sozinho dois
dos sérios acima.

**2. Uma passada de vocabulário no vault inteiro, com o glossário como juiz.** Normalizei quatro
termos dentro das minhas pastas e descobri, ao fazer isso, que três deles estão divergentes
também fora delas — em números maiores. Enquanto isso não for feito de uma vez só, cada agente
que trabalhar numa pasta vai normalizar para o padrão que encontrar primeiro, e a inconsistência
migra em vez de sumir. O jeito certo é um script que leia o glossário e reporte desvios, rodado
como o `auditar-links.py`.

**3. Estender o `auditar-links.py` para conferir âncoras de seção.** Escrevi essa verificação à
mão para este trabalho e ela pegou um link que eu mesma quebrei ao normalizar um termo — o script
atual reportava zero quebrados, porque só olha o nome do arquivo. Com quase cinco mil links no
vault e âncoras que citam títulos de seção inteiros ("13.7 Travessia de barreira regional, por
rank"), qualquer renomeação futura de seção quebra links em silêncio. São vinte linhas de Python
e resolve para sempre.

---

## O que está bom, com nome e sobrenome

Não é preenchimento de seção: estas seis coisas são o motivo de as duas pastas valerem a leitura,
e nenhuma delas foi tocada.

**O cardápio de travas da nota-porta dos eventos.** É a melhor ideia editorial do vault inteiro.
Ela transforma a pergunta que derruba toda campanha de nível baixo — *por que o ancião não resolve
isso sozinho?* — numa lista de dezoito respostas canônicas, com endereço. E a instrução prática
("escolha a trava **antes** de desenhar o evento; ela costuma sugerir sozinha o formato da
sessão") é conselho de designer, não resumo de leitor.

**O Obelisco de Mérito, na nota 13.** Faixas de missão com valores declarados, títulos compráveis
que formam uma série dedutível, placar público que mostra o gasto além do ganho, pontos negativos,
prazo com reencontro do lado de fora, proibição de combate na base, e uma recompensa que **desconta
por levar o cadáver embora**. Mais a instrução de reescalagem para rank 1 a 3 que mantém os
números e troca só a escala dos problemas. É um sistema de jogo pronto, e a nota sabe disso.

**A Montanha Yi Tian, era um, na nota 16.** Cem dias, campo fechado, ninguém forte pode pisar, e
cada personagem com um patrono invisível que lucra proporcionalmente ao quanto ele lutar. A
sugestão de entregar a cada jogador, em segredo, a ficha da aposta do próprio patrono é o tipo de
ideia que um manual comercial cobraria caro.

**A tabela de funções da força-tarefa, na nota 17.** Líder que não é o mais forte, um
defensor-detector sem nenhum método ofensivo, e o portador da contramedida declarado como o membro
mais importante do grupo. E a recomendação de **entregar essa tabela aos jogadores quando eles
forem os caçados**, que converte uma fuga desesperada num assalto cirúrgico.

**O clã Chai, na nota da Fronteira Sul.** Um super clã do caminho correto que drena a aptidão de
forasteiros mantidos felizes e bem alimentados numa montanha da qual não podem sair, e ninguém na
região vê problema nisso. A nota entrega o dilema inteiro sem julgar, com a saída dramática já
embutida. É a melhor ficha das duas pastas.

**As seções "O que a obra não diz".** Presentes em toda ficha e em quase toda nota, e escritas
como espaço declarado em vez de desculpa. Uma designer que precisa inventar sabe exatamente onde
pode — e essa é, no fim, a diferença entre uma bíblia de sistema e um resumo.
