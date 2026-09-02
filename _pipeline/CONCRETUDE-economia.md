# Passe de concretude física — pasta `06 - Economia e Vida`

**Escopo:** as quatro notas sob responsabilidade deste passe —
`01 - Visão Geral da Economia`, `02 - Pedras Primordiais`, `04 - Vida Cotidiana`,
`05 - Mercados e Leilões`.

**Motivação (pedido do usuário):** as notas explicavam as *regras* e não descreviam as
*coisas*. A designer nunca leu a obra e não sabe que tamanho tem uma pedra primordial, se
cabe na mão, quantas cabem numa bolsa, como se paga. Régua adotada: *"pense que a pessoa
que vai fazer o sistema nunca leu, então ela realmente não sabe esses detalhes se você não
explicar"*.

**Método:** cada acréscimo saiu de passagem localizada por `grep -i` no texto-fonte
(`/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/*.txt`). Onde a obra não descreve,
a nota **diz que a obra não descreve** — isso avisa a designer de onde ela pode desenhar
livremente. Nada foi reescrito: as regras que já estavam nas notas foram preservadas e a
concretude foi acrescentada em torno delas.

---

## `02 - Pedras Primordiais` (nota principal do passe)

Acrescentada a seção **"A pedra na mão"**, com sete subseções, mais dois blocos avulsos e
um diagrama Mermaid. Também acrescentado um aviso de nível `segredo`.

### O que entrou, e de onde

| Fato acrescentado | Capítulo |
|---|---|
| Pedra completa = **tamanho de ovo de pato**, **elipsoide**, **cinza translúcida** | 29 |
| **Cinza-esbranquiçada**, e **os volumes são iguais entre si** (unidade padronizada) | 18, 23 |
| Cabe **pinçada entre polegar e indicador** | 28 |
| **Três ou quatro** cabem numa palma aberta | 28 |
| Levadas soltas **"no seio da veste"** (bolso do peito do roupão), apalpadas por fora | 18 |
| **Bolsa de dinheiro = cem pedras**, "cheia até a boca"; pagamento grande = "cinco bolsas de cem" | 42, 45 |
| **300 pedras = bolsa segurada com as duas mãos** | 158 |
| Somas grandes chegam em **caixas**, uma por servo | 112 |
| **"As pedras são pesadas e um estorvo de carregar"** | 43 |
| **Cavalo de estômago grande** usado como substituto de Gu de armazenamento | 428 |
| Encolhe ao ser drenada; meio-drenada é "um círculo inteiro menor" e "menor pela metade" | 29, 43, 18 |
| **O peso diminui junto com o tamanho** (a frase que liga peso a valor) | 18 |
| Ao fim vira **um punhado de pó branco**, que se joga fora | 34, 50 |
| **Verificação = pesar na mão**: o taberneiro varre as pedras para a palma e balança a mão | 8 |
| **Contagem conferida** ("trinta pedras, nem uma a menos"); etiqueta "confira, por favor" | 53, 112 |
| **Troco:** "me devolva o que sobrar" ao entregar duas pedras cheias | 11 |
| **Conta em aberto:** "deixe o troco; quando der uma pedra, desconte da minha conta" | 23 |
| Preços em **meia pedra** (hospedagem, javali, aumento salarial), 2½, 5½ | 11, 18, 28, 320 |
| **Gesto de consumo:** sentado de pernas cruzadas, punho direito fechado sobre a pedra, olhos fechados; a reserva sobe "a olho nu"; pernas dormentes ao terminar | 10, 29, 34 |
| **Não se absorve pedra em combate** — ocupa a mente; multitarefa é perícia rara e reduz o controle dos Gu | 126, 320 |
| Ordem de grandeza do consumo: "dois dias e duas noites, doze pedras" | 18 |
| Consumo alternativo: **mastigar e triturar** pedras | 197, 424 |
| No refino, as pedras são **atiradas uma a uma na esfera de luz** | 111-113 |
| A obra compara a pedra explicitamente ao **padrão-ouro** | 8 |
| Nascente = **fonte de água em caverna subterrânea**, com **redemoinhos**, energia tão densa que se sente como **pressão física**; morta vira "poça de água parada" | 4, 5, 163 |
| Pedras são a **"cristalização da nascente"** | 163 |
| Fundar povoado sobre nascente nova exige **campanha militar** (feras se instalam na energia densa) | 218 |
| Tetos de armazenamento: **tusita flower** rank 3 = 30.000; **primeval elder Gu** rank 3 = 1.000.000 | 161, 422 |
| **Pedra de essência imortal**: mesmo tamanho de ovo de pato, mas **redonda como pérola**, lustrosa, translúcida e cintilante, "cristal com brilho de jade" | 466 |
| `[segredo]` As pedras contêm **vontade do céu**, que se infiltra nos pensamentos de quem as absorve | 2297 |

### Deduções e invenções marcadas

- `(ded.)` **A pedra parcialmente drenada circula como fração.** A obra afirma, em cenas
  separadas: que existem preços de meia pedra; que pedras meio-drenadas circulam de mão em
  mão; que elas são menores e mais leves; e que comerciantes verificam pelo peso. A costura
  das quatro é nossa — mas é a única leitura que faz o sistema fechar sem moeda menor.
- `(ded.)` **Pesar é medir o valor.** A obra descreve o gesto de pesar e descreve a relação
  peso↔essência restante, mas nunca junta as duas coisas numa frase.
- `(ded.)` **Por que não se falsifica dinheiro.** A obra não registra nenhum caso de pedra
  primordial falsa (registra Gu falso e fóssil de aposta falso). A explicação proposta — a
  pedra é verificável em um segundo por qualquer pessoa, e uma imitação oca não passaria no
  teste do peso — é nossa.
- `*` **Tabela "quanto pesa e quanto ocupa"** (~120 g e ~70 cm³ por pedra, escalando até
  "10.000 pedras = uma carroça"). Aritmética nossa a partir do dado canônico do ovo de pato.
  Marcada com `*` nas duas colunas e com instrução explícita de como recalibrar.
- O **diagrama Mermaid** do ciclo de vida da pedra (completa → usada → quase vazia → pó) traz
  legenda dizendo que é leitura nossa: a obra descreve os quatro estados em cenas separadas
  e nunca os desenha como sequência.

---

## `01 - Visão Geral da Economia`

Acrescentada, **antes** de qualquer regra, a seção **"A coisa, antes das regras"**: o objeto
descrito na mão, e depois a mesma pedra gasta das duas maneiras possíveis (no balcão da
taberna e dentro do punho fechado), para que a leitora entenda de primeira que **é o mesmo
objeto**, sem taxa de câmbio nem conversão.

Fecha com três consequências para o dia a dia — pagar hoje é abrir mão do cultivo de hoje; a
pedra encolhe e denuncia o saldo; **não dá para recarregar lutando**.

Acrescentadas três regras do mundo novas à lista enumerada (a lista foi renumerada; agora
tem 20 itens):

- **2** — gastar a moeda como combustível exige estar parado e concentrado (cap. 126, 320);
- **3** — dinheiro tem peso e volume; dez mil pedras são uma carroça (cap. 43, 45, 161);
- **4** — não existe moeda menor; o troco se resolve com pedra parcial, devolução e conta em
  aberto (cap. 11, 23).

---

## `04 - Vida Cotidiana`

Passe sensorial. Acrescentadas quatro seções novas e duas subseções, todas montadas para que
a designer **consiga descrever uma vila em voz alta**.

### Seções novas

- **"Por dentro de uma casa"** (subseção de *Onde as pessoas moram*) — quatro interiores
  descritos: a casa de montanha sobre palafitas, a casa de caçador na floresta, o quarto
  alugado de um pobre, e a taberna da vila (o interior mais completamente descrito da obra).
- **"As casas que estão vivas"** — casa-lagarto, casas-cogumelo, casa-árvore de semente,
  joaninhas-cristal que servem bebida.
- **"Luz, calor e água"** — a escada de iluminação por riqueza, aquecimento, higiene, e a
  lista do que a obra não descreve.
- **"O que está de fato na mesa"** (subseção de *Comida*).
- **"Como as pessoas se vestem"** — o sistema de cinto e placa de rank, e o contraste
  mortal × Mestre Gu.
- **"O que puxa a carroça"** (subseção de *Viagem*) — o bestiário de transporte.
- **"Uma vila em voz alta"** — seção de fechamento que remonta tudo na ordem de um dia,
  para leitura única antes de uma sessão.

### Achados principais, e de onde

| Fato | Capítulo |
|---|---|
| Casa de montanha: 2 andares, primeiro andar são **estacas grossas**, moram no segundo | 3 |
| Paredes de bambu "como jade" ao luar | 17, 100 |
| Casa de caçador: casca grossa, musgo verde, cerca de bambu-lança, hortas, poço cavado à mão; 4 quartos + sala + cozinha; fogueira de chão ligada à chaminé | 67, 68 |
| Quarto de pobre: assoalho que range, cobertor remendado com algodão amarelo escapando; lista de compras completa para mobiliar (mesa, cadeira, colchão, lençóis, 2 cobertores, lamparina, 2 potes de óleo, fogão) | 90, 91, 92 |
| Cabana de sapé, esteira de palha, um único conjunto de roupas remendadas | 1318 |
| Taberna: adega subterrânea, ladrilho preto quadrado, 8 mesas, balcão marrom-escuro com pincel/tinta/**ábaco**, jarros de cerâmica preta e porcelana clara, 16 livros-caixa em papel de bambu verde-claro | 103 |
| Pátio com árvore-alfarroba cobrindo tudo como dossel | 63 |
| **"Lanternas eram um luxo para gente comum; a casa ficava escura à noite, a única luz vinha da lua pela janela"** | 229 |
| Lamparina a óleo que apaga quando o óleo acaba; óleo vendido em potes | 90, 91 |
| Velas que iluminam o centro do cômodo e deixam os cantos escuros, encolhendo ao queimar | 17 |
| **Pedra de carvão** na cidade interna: queima muito, sem fumaça, em nichos a cada cem passos; deixa a cidade mais quente e mais seca | 261 |
| Fogão de ferro com fuligem, lenha seca ao lado, chaleira de bronze em cima | 74 |
| Mina de carvão de graça fora da vila | 92 |
| Limpeza sazonal do fogão de inverno, bacia de água suja | 129 |
| Higiene matinal: bacia de água morna, bochecho, **galho de salgueiro com sal fino** nos dentes | 3 |
| Bacia de água quente + toalhas de pano levadas ao quarto da hospedaria | 17 |
| Poço, balde, "encher o tanque de água" e rachar lenha como rotina | 67, 229 |
| **Casa-lagarto**: rank 2, tamanho de ônibus, olhos são janelas, boca é a porta, corredor com duas fileiras de quartos, privada no fim, defeca levantando a cauda, anda quando a tribo migra | 439 |
| **Casas-cogumelo**: chapéu cinzento redondo escoando a chuva, caule circular, paredes brancas com janelas; dezenas formam um bosque; ali moram os anciãos e os ricos | 439 |
| **Casa-árvore**: 18 m, raízes como cobras enroscadas, três andares no tronco, cresce de semente com essência primordial e volta a ser semente | 439 |
| **Joaninhas-cristal** do tamanho de cestos nas paredes de pano, corpo transparente mostrando o licor; o atendente encosta a taça no bocal e faz carinho no casco | 44 |
| Arrozal amarelo-alaranjado no outono, canteiros de folha gorda | 119 |
| "O ar cheio de aroma de comida; famílias reunidas à mesa conversando alegremente" | 229 |
| Pão no vapor distribuído em cesto | 235 |
| Porco só no ano novo (topografia íngreme impede criar gado) | 64 |
| Carne salgada + biscoito seco como ração de viagem | V2 |
| Chá em xícara de bambu, folhas sopradas antes de beber; chá específico contra ressaca; café da manhã reaquecido a pedido | 17 |
| Carta de mais de cem vinhos, com cinco nomes citados literalmente | 44 |
| Hospitalidade nômade: **kumis** em odre de couro; o chefe corta olhos de vaca e ovelha e a carne do dorso, serve em **prato de ouro com as duas mãos** | 439 |
| **Cinto de rank**: r1 azul/verde com placa de bronze "1"; r2 vermelho com placa de aço "2"; r3 branco com peça quadrada de prata "3" | 12, 31, 110 |
| Uniforme completo r1: traje azul-escuro, perneiras de bambu, sapatos de bambu, faixa azul-viva, cinto azul-marinho | 87 |
| Variante de luxo: roupão dourado, cinto rendado, peça quadrada de jade em vez de placa | 42 |
| Rua com descalços, lavradores enlameados, colhedores de ervas, caçadores com faisões e javalis — e Mestres Gu "limpos e animados" | 31 |
| Mestre Gu na miséria tecendo as próprias sandálias de palha para vender | 61 |
| Estepe: túnicas de pele; fios de ouro/púrpura para os melhores; pobres de roupa rasgada remendada; **escravos quase sem roupa**, magros e pálidos | 439 |
| Vestidos bordados a ouro e prata na dança em torno da fogueira | 524 |
| Roupão de pele de raposa-da-neve | V3 |
| Transporte: avestruz puxando carroça de duas rodas | 39 |
| Caravana: besouros pretos gordos com gente e carga nas costas, avestruzes de penas coloridas, aranhas peludas de montanha, serpentes aladas | 109 |
| **Lobo-corcunda**: as duas corcovas formam a sela | 437 |
| **Cavalo de estômago grande**: dois estômagos, um para comer e outro para carga; usado em mudanças | 427 |
| Boi de chifre curvo para famílias remediadas | V3 |
| Jangada de bambu com corda de cânhamo, mastro tosco, vela branca puída | 200 |
| Vias da cidade interna largas para **dez carroças lado a lado** | 261 |
| **Vigia noturno batendo matracas de madeira** antes do amanhecer | 3 |
| Galo cantando ao amanhecer | 231 |
| Feira: barracas provisórias em volta da vila ao entardecer, pregões gritados com preço | 39 |
| Depois da feira: grama pisoteada virando lama, buracos com água de chuva, lixo | 40 |

### Marcações

- `(ded.)` **A progressão do cinto de rank.** A obra descreve três degraus em cenas
  separadas (r1, r2, r3) e nunca publica a tabela; a regra implícita — a cor muda a cada
  rank e o metal da placa fica mais nobre — é leitura nossa e está marcada como tal na nota.
- Todo o resto é descrição literal de cena.

### Lacunas registradas na própria nota

**Sabão não existe** na obra (a única ocorrência da palavra é expressão idiomática);
**latrina e penico domésticos** nunca descritos (a única privada descrita no mundo é a da
casa-lagarto); **casa de banhos** não existe como instalação de vila; **objetos de toucador**
(pente, espelho doméstico) inexistentes; **roupa de inverno de mortal** nunca descrita — o
frio se resolve sempre com fogo. Também não há, em nenhum lugar da obra: **Gu doméstico de
iluminação** de uso civil, cena de **casamento** ou de **funeral de aldeão** em andamento, e
nenhuma menção a **instrumentos musicais ou canções**.

---

## Perguntas que a obra NÃO responde

Registradas nas próprias notas como lacunas explícitas, para que a designer saiba que ali
pode desenhar como quiser:

1. **A pedra brilha?** Não há passagem alguma. Procurado com `grep -i` por `glow`, `shine`,
   `shimmer`, `light up` cruzado com `primeval stone`: zero resultados descritivos.
2. **É quente ou fria ao toque? Qual é a textura?** Idem — `warm`, `cold`, `smooth`, `rough`,
   `texture`, `touch`: nada.
3. **Quanto pesa, em unidade real?** Nunca dito. Só "pesadas e um estorvo".
4. **Como as pedras são colhidas da nascente?** A obra descreve a nascente (caverna, água,
   redemoinhos, pressão) e diz que as pedras são a cristalização dela — mas **nunca mostra
   ninguém recolhendo**. Não se diz se elas se formam no fundo, se boiam, se são garimpadas.
5. **Existe falsificação de moeda?** Nenhum caso registrado em toda a obra.
6. **Quanto tempo leva absorver uma pedra inteira?** Só há a medida agregada ("dois dias e
   duas noites, doze pedras"), nunca o tempo de uma pedra isolada.
7. **A pedra pode ser fisicamente quebrada em pedaços para fazer troco?** A obra nunca
   mostra isso. (Cuidado com o falso positivo: a tradução usa "pieces" como classificador —
   "seis pieces of primeval stones" = seis unidades, não seis cacos.)

---

## Números novos que talvez devam subir para a tabela soberana

Candidatos para `10 - Apendices/02 - Tabelas de Referência Rápida.md` — **não** foram
escritos lá por este passe, que só mexe nas suas quatro notas:

| Número | Valor | Capítulo |
|---|---|---|
| Capacidade de uma bolsa de dinheiro | **100 pedras** | 42, 45 |
| Bolsa que exige as duas mãos | 300 pedras | 158 |
| Teto do Gu de armazenamento comum de rank 3 (tusita flower) | 30.000 pedras (≈15.000 na prática, se levar mais coisas) | 161 |
| Teto do Gu de armazenamento de dinheiro (primeval elder Gu, rank 3) | 1.000.000 pedras | 422 |
| Câmbio de pontos de mérito em economia de guerra | **25 pontos = 1 pedra**; 10 pontos = um olho de lobo; 5 pontos = saco de 500 g de arroz | 132 |
| Pedra de essência imortal × pedra primordial | 2 pedras imortais > 200.000.000 primordiais | 466 |
| Consumo documentado de refino | 12 pedras em 2 dias e 2 noites de trabalho contínuo | 18 |

> **Atenção ao câmbio de guerra (cap. 132).** 1 pedra = 5 sacos de 500 g de arroz = 2,5 kg de
> arroz. Isso não fecha com a âncora de paz (1 pedra = 1 mês de sustento de uma família de
> três). Não é contradição da obra: o cap. 132 é um **quadro de racionamento durante um
> cerco**, e a diferença mede a inflação de guerra. Quem levar esse número para a tabela
> soberana precisa levar a ressalva junto.

---

## Decisões tomadas

1. **"Ovo de pato", não "ovo de pata".** Tecnicamente *duck egg* seria "ovo de pata", mas o
   restante do vault já usa "ovo de pato" e a consistência para a leitora vale mais.
2. **A tabela de peso/volume foi mantida apesar de ser invenção**, porque sem ela a designer
   não consegue responder "cabe na mochila?" — que é exatamente a pergunta do usuário. Ficou
   marcada com `*` nas colunas calculadas e com instrução de recalibragem ("se preferir
   pedras mais leves, divida tudo por dois").
3. **O segredo da vontade do céu dentro da pedra (cap. 2297) entrou**, em callout
   `> [!warning]` de nível `segredo`, e o campo `conhecimento:` da nota 02 passou de `comum`
   para `misto`. É informação de mundo (mecânica), não de enredo, e portanto passa na
   política de spoilers — mas é conhecimento de mestre.
4. **Não foi criada nota nova.** Toda a concretude entrou nas notas existentes, como pedido.
5. **Nenhum `git add`/`git commit`** foi executado, conforme instrução.
