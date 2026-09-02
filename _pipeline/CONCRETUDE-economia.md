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
