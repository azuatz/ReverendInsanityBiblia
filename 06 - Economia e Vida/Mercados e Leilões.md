---
tags:
  - economia
  - economia/mercados
  - economia/leiloes
aliases:
  - Markets and Auctions
  - Auction
  - Rock gambling
status: consolidado
fontes: ["cap. 23", "cap. 39-47", "cap. 40-43", "cap. 55", "cap. 109-113", "cap. 234-238", "cap. 247-249", "cap. 259-283", "cap. 276-277", "cap. 292-296", "cap. 304-311", "cap. 322-328", "cap. 441", "cap. 466-476", "cap. 520", "cap. 712", "cap. 747-763", "cap. 764", "cap. 1441-1453", "cap. 1559", "cap. 1600", "cap. 1817", "cap. 1885", "cap. 2251", "cap. 2255"]
conhecimento: comum
---

# Mercados e Leilões

**Em uma frase:** comprar e vender neste mundo tem quatro camadas — a caravana que passa
uma vez por ano, a cidade-mercado com portões vigiados, o leilão, e a aposta de pedra — e
em cada uma delas ==o acesso importa mais que o dinheiro==.

## As camadas do comércio

### 1. Varejo local e caravanas

Nos vilarejos isolados, o comércio chega de fora. **Caravanas mercantes** percorrem
periodicamente as montanhas e povoados, tipicamente lideradas por um cultivador de rank 4,
parando três dias em cada lugar. Elas compram o excedente local — vinhos regionais, chás,
produtos de artesanato — e vendem o que a região não produz.

Nos vilarejos há lojas fixas modestas, uma estalagem, crédito informal e contas em aberto
entre conhecidos. E há uma solução arquitetônica encantadora que vale descrever numa mesa:
certas lojas são **construções vivas**, plantas de rank alto que crescem instantaneamente
em edifícios de três andares quando alimentadas com energia — e que funcionam como
cofre-forte, prendendo ladrões dentro de si.

Caravanas grandes são consórcios: um vice-líder por clã participante e um líder geral
eleito apenas para manter a ordem coletiva. Elas têm **mercados internos próprios**, um
diário para mortais e um semanal para Mestres Gu, e tratam trabalhadores mortais como
recurso reponível, recrutando substitutos nas vilas do caminho. O espólio de um desastre na
estrada é disputado em assembleia, com barganha política aberta.

**A reputação de um clã junto às caravanas é ativo estratégico:** uma rota que passa a ser
evitada condena a região ao declínio.

### 2. Venda por lance fechado

Nos vilarejos não existe leilão aberto, e o motivo é social e não técnico: seria
constrangedor competir publicamente por preço contra os próprios parentes, e reunir
representantes de vários clãs no mesmo lugar é logisticamente inviável.

A solução local é o **lance cego por escrito**: o item fica exposto por um período
proporcional ao seu rank (meio dia para rank 1, um dia para rank 2, dois dias para rank 3);
os interessados depositam bilhetes com preço e assinatura numa fenda no balcão; o sigilo é
total.

> [!note] Para o design
> O lance cego é um minijogo social de altíssimo valor por custo zero de regras. Vencer não
> depende de ter mais dinheiro — depende de **estimar a faixa do concorrente**: a motivação
> dele, o apego ao item, o poder aquisitivo. Há um caso documentado de alguém que venceu
> cobrindo o rival por dez ou vinte pedras de margem, e que **perdeu de propósito** itens-
> isca para não revelar sua capacidade real. O vendedor, impressionado, ofereceu emprego.

### 3. Cidades-mercado

O topo do comércio mortal. O modelo mais bem documentado é uma cidade construída em anéis
concêntricos numa montanha: uma cidade externa caótica e cinco cidades internas cada vez
mais restritas, em arquitetura tridimensional. Cada zona é temática e administrada por um
"jovem mestre" do clã anfitrião: culinária, aposta de pedra, pensão de Gu, combate de Gu,
zona de prazeres, refino por procuração, leilões e arena.

O que a torna interessante é o **sistema de acesso**, que separa dinheiro de autoridade:

- Existe uma escada de **fichas coloridas** — nove cores, do preto ao roxo-espinho — que
  determina onde você pode entrar e o que pode comprar.
- A ficha de topo equivale a cerca de metade da autoridade de um ancião de clã, e há apenas
  algumas centenas delas no mundo inteiro.
- As fichas são **vinculadas ao sangue** por um Gu específico, não replicáveis, e
  **degradam com o tempo** — a renovação periódica é um instrumento deliberado de controle
  de longo prazo sobre os portadores.
- A proteção que a ficha oferece vale **apenas dentro da cidade**, e não cobre o que
  acontece dentro da arena. Assassinar alguém na cidade custa a ficha.

Há ainda um cofre ancestral notável: uma porta viva, obra de um cultivador imortal, que só
**troca Gu por Gu de valor igual ou superior**. Nem o líder do clã retira nada sem pagar. E
um Gu retirado tem poucas respirações antes de reverter ao estado selvagem — o cofre não
guarda propriedade, guarda equilíbrio.

> [!note] Para o design
> A **moeda dupla** — dinheiro mais autorização política — é a mecânica mais exportável
> desta nota. Ela permite ao mestre colocar itens incríveis à vista dos jogadores sem
> precisar torná-los caros: o problema não é o preço, é a ficha. E como a ficha expira,
> conquistá-la nunca é definitivo.

## Leilões

Nas cidades grandes, os leilões operam em camadas por frequência e por porte:

| Tipo | Frequência | O que entra |
|---|---|---|
| Pequeno | Diário | Itens comuns; portadores de ficha alta compram antecipadamente |
| Médio | Quinzenal | — |
| Grande | Mensal | Somente rank 3 ou acima |
| Super leilão | Bienal | O acervo excepcional da região |

Os grandes leilões vendem Gu, comida rara de Gu, materiais, **receitas**, informação sobre
localização de heranças, pedras de aposta de qualidade perfeita, escravos e até feras-reis
capturadas vivas.

**Táticas documentadas de leilão**, todas prontas para mesa:

- **Inflar lances para drenar um rival por orgulho.** Um caso registrado: elevar o preço de
  um item inútil para um adversário raivoso até que ele pagasse o dobro do valor de mercado,
  e então desistir "graciosamente". Humilhação pública e dreno de recursos, sem gastar nada.
- **Empréstimos informais milionários na palavra**, entre aliados, para cobrir um lance.
- **Uso de informação privilegiada.** Saber de antemão quais itens triviais serão exigidos
  como chave de uma herança permite comprá-los baratos e revendê-los no pico da
  especulação — há um caso de valorização de três vezes em cerca de dez dias.

> [!warning] O ego é um recurso do oponente
> A regra generalizável dos leilões deste mundo: em disputa pública, **o orgulho do
> adversário é um ativo que você pode gastar**. Todas as táticas acima exploram isso, e
> nenhuma delas exige poder de compra superior.

## Aposta de pedra

O jogo de azar profissional do cenário, e um sistema completo por si só.

**O princípio:** Gu feridos ou famintos às vezes hibernam e se **fossilizam** dentro de
rocha. A pedra fechada é vendida sem que ninguém saiba o conteúdo — os métodos de detecção
disponíveis ou não funcionam através da casca, ou matariam o ocupante.

**As probabilidades são péssimas e públicas:**

- cerca de nove em cada dez pedras são maciças, sem nada dentro;
- entre as restantes, a maioria guarda um Gu já morto;
- um especialista com séculos de prática acerta algo em torno de duas em dez.

**As cinco categorias de preço:** sucata (dezenas de pedras primevas), baixo (~100), médio
(~1.000), alto (~10.000) e super (centenas de milhares).

**Como se melhora as chances:** heurísticas de tamanho relativo — o fóssil costuma ser
cerca de 30% maior que o Gu dentro dele —, textura, formato e padrão mineral. Certos
minerais indicam famílias específicas de Gu, e o formato externo frequentemente denuncia a
espécie.

**Abrir é uma segunda perícia, e ela pode destruir o prêmio já ganho.** Desgasta-se camada
por camada com um Gu de precisão; leva de dois a três anos para dominar; um movimento
brusco mata o ocupante hibernando. Existe a profissão de **dissecador de fósseis**, com
métodos distintos por tipo de rocha — magnetismo, ácido, fogo, vento — e o método errado
mata. As casas grandes oferecem a dissecação de graça nas categorias caras e cobram nas
baratas.

**Dois bônus estruturais:**

- Um Gu recém-tirado de fóssil nasce **fraquíssimo**, o que torna o refino dele muito mais
  fácil que o normal.
- E o mais valioso socialmente: como o fóssil é destruído ao ser aberto e não deixa rastro,
  **"tirei de um fóssil" é o álibi perfeito para a origem de qualquer Gu**. Ninguém pode
  refutar sorte. É a lavagem de dinheiro deste mundo, e fica ainda mais sólida se houver
  testemunhas de um acerto real anterior.

**Riscos do setor:** falsificação em massa já derrubou o valor da categoria mais barata numa
região inteira. E esconder Gu valiosos dentro de pedras é técnica reconhecida de
espionagem.

> [!note] Para o design
> A aposta de pedra é um minijogo pronto com todas as peças no lugar: custo fixo por
> tentativa, tabela de resultados, uma perícia que melhora as chances sem nunca garanti-las,
> uma **segunda** perícia que pode estragar o prêmio conquistado, e um uso social — o álibi
> — que gera intriga sozinho.

## O mercado de informação

Informação é mercadoria de primeira classe, com um traço que a distingue de todas as
outras: **ela não se gasta ao ser vendida**. O mesmo segredo pode ser vendido duas vezes,
inclusive a facções rivais — o risco não é o estoque acabar, é os compradores se
encontrarem.

O que se comercializa: intel de arena (rankings e prognósticos de lutadores), segredos
comprometedores de clã, localizações prováveis de heranças, enunciados de competições
passadas e fofoca política. Existe até uma seita inteira construída sobre esse único
negócio, erguida do zero à relevância regional em cerca de um século.

Um caso documentado: uma informação estratégica **não confirmada** — a possível existência
de um território de cultivo — foi vendida a uma potência por centenas de milhares de pedras
e revendida, numa versão alterada, à rival, com uma fonte falsa plantada como cobertura.

## Como a informação move os preços

Três padrões documentados que servem de regra de mesa:

1. **Anúncios de requisito criam bolhas instantâneas.** Divulgar quais itens são a chave de
   uma herança triplica o preço deles em dias.
2. **Inovação valoriza insumos da noite para o dia.** Quando um novo Gu passa a consumir
   determinado material, aquele material dispara.
3. **Compra em atacado é detectável e denuncia quem compra.** Varrer todo o estoque de um
   material em poucas horas alarma todos os que dependem daquele mercado e revela a
   existência de um comprador riquíssimo.

## O mercado imortal: por que artefatos não têm preço

Acima do rank 6, o comércio muda de natureza, e a diferença é estrutural.

**Os Gu Imortais não podem ser comprados.** A autoridade máxima do mundo declara
formalmente que eles não se vendem — "mal há o suficiente para nosso próprio uso" —, mas
**podem ser emprestados**. Na prática, transações de artefatos entre imortais são **trocas
diretas**, artefato por artefato, e não lances em dinheiro. Num leilão documentado de um
artefato cobiçado, todos os interessados ofereceram outros artefatos do mesmo tipo, e
ninguém fez uma única oferta em moeda.

**Já as receitas e as técnicas de combate imortais se vendem normalmente.** O conhecimento
circula; o objeto, não.

**Isso inverte a lógica do leilão: é um mercado de vendedor.** O dono escolhe a oferta que
prefere — não a maior. Um leilão de artefato documentado funcionava assim: três espaços
distintos (salão aberto, salas individuais, salas secretas anônimas), ordem de apresentação
sorteada por Gu neutros que qualquer um podia inspecionar, e juramento formal contra mentir
sobre o item, com punição física automática para quem mentisse. E uma advertência que diz
tudo sobre o mundo: **encerrado o evento, emboscar os participantes na saída é
comportamento esperado**.

**Consequência prática:** num mercado de vendedor, informação sobre a **necessidade do
vendedor** vale mais que poder de compra. Num impasse entre três ofertas de valor
equivalente, venceu quem ofereceu ativos tematicamente relevantes para o vendedor — cativos
do tipo exato que ele precisava — derrotando lances nominalmente maiores.

As regras completas dessa camada, incluindo a praça de comércio imortal e seu curioso
mecanismo de precificação por feixe de luz, estão em [[Economia Imortal]].

> [!example] Caso mecânico
> Um vendedor num mercado imortal pode **recusar lances altíssimos e manter o item exposto
> apenas para humilhação pública** — usando o mercado como palco de propaganda contra um
> rival que quer o item e não vai tê-lo. E como toda transação nesse mercado é publicamente
> revelada, esconder o que se vende exige negociar em segredo fora dele. O mercado é
> simultaneamente bolsa, fórum, cartório e arma.

## Relações

- [[Pedras Primevas]] — a unidade em que os preços mortais são medidos.
- [[Economia Imortal]] — a praça de comércio da camada superior e suas regras maduras.
- [[Como um Mestre Gu Ganha a Vida]] — o que se vende nesses mercados e quem produz.
- [[Eventos e Instituições Jogáveis]] — leilões, feiras e convenções como eventos de mesa.
- [[Visão Geral da Economia]] — o quadro geral.
