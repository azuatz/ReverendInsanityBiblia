# Auditoria de completude — domínio Mundo (`04 - Mundo/`)

> Relatório incremental. Auditoria de **completude de conteúdo**: o objetivo declarado pelo
> usuário é que "como o mundo funciona" esteja completo o bastante para um sistema de RPG
> explicar o cenário a quem nunca leu a obra.
>
> Método: (1) leitura das 15 notas da pasta; (2) confronto com `_pipeline/rascunho/mundo-e-cosmologia.md`
> e com as pesquisas de `_pipeline/pesquisa/`; (3) leitura do topo de `_pipeline/LACUNAS.md`;
> (4) varredura dirigida do TEXTO-FONTE nos assuntos que nenhum dos dois cobria.

## Lacunas encontradas

### 🔴 BLOQUEADORES (a designer não consegue rodar uma cena sem isso)

**L1 — O relógio e o calendário do mundo não existem em nota nenhuma.** `severidade: alta`
Nenhuma das 15 notas responde "que horas são?", "que mês é?", "quanto dura um ano?".
Grep na pasta: `calendário` só aparece como metáfora ("calendário de desastre", "calendário
institucional"); `meia-noite`, `estações do ano` como sistema, `eclipse` e `hora` como unidade
não aparecem em lugar nenhum. Uma mestra que precise dizer "vocês chegam ao anoitecer do
terceiro dia do quinto mês" não tem onde consultar. Evidência de que a obra **tem** esse
material: cap. 213 mede tempo em "enough time passed for an incense stick to burn"; cap. 907
data um fenômeno anual por mês do calendário ("during May in Eastern Sea"); caps. 34, 60, 131,
205, 365 usam meia-noite como marco operacional de cultivo e de vigília.

**L2 — O mecanismo físico do dia e da noite está pela metade, e do jeito que está induz erro.**
`severidade: alta`
`01 - Visão Geral do Mundo` e `13 - Cosmologia` afirmam que os dois céus "se revezam como dia e
noite" — o que é canônico (cap. 466: "the two alternating between day and night"; cap. 740) —,
mas **nenhuma nota diz que existe um sol**, e a obra o menciona centenas de vezes ("the sun
rose from the east", cap. 21; "the blazing sun slowly descended from the highest point in the
sky", cap. 73). Uma leitora leiga conclui, das notas como estão, que este mundo **não tem sol**
— e vai desenhar um cenário errado. O texto que costura as duas coisas existe e é preciso
(cap. 389): a luz do sol da era imemorial "could pierce through the nine heavens"; hoje ela
"had weakened to the extreme, being able to pierce through **only the white heaven**". Ou seja:
o sol é real, os céus são filtros, e a noite é o céu negro barrando a luz.

**L3 — A biosfera ordinária (plantas, bichos comuns, comida, lavoura, rebanho) não tem nota.**
`severidade: alta`
`07 - Bestas Gu e Reis Fera` cobre magnificamente a fauna **que hospeda Gu**; o Atlas cobre
flora e fauna **por região**. Falta a camada transversal: o que é um animal normal neste mundo,
o que se planta, o que se come, quem cria gado, o que um mortal janta. Grep na pasta:
`agricultura`, `arroz`, `trigo`, `carroça` — zero ocorrências. `colheita` só aparece com o
sentido de colher recursos de cultivo.

**L4 — Só três das cinco paredes regionais estavam nomeadas; a obra nomeia as cinco.**
`severidade: alta` — **erro factual, já corrigido.**
`04 - As Cinco Regiões` afirmava "Três das cinco paredes são nomeadas na obra". Falso: cap. 1043
lista as cinco de uma vez (miasma / licorice / raging flame / blue water / saint), e cap. 1044
confirma a de miasma no mundo real (não só na imitação). Faltavam também **as cores** e **o
interior** de cada parede, que a obra descreve com riqueza (cap. 710).

### 🟠 SÉRIAS

**L5 — Ninguém explica que as paredes regionais se tocam.** `severidade: média`
Cap. 710: saindo da parede santa entra-se direto na parede alcaçuz. Cap. 1045: da parede de
miasma direto para a de água azul. Cap. 1211 idem. Consequência que muda o mapa: **não existe
terra de ninguém entre duas regiões**, e toda travessia é a travessia de *duas* membranas
seguidas. As notas descreviam a parede como se fosse uma só.

**L6 — A parede regional tem espessura medida em passos, se regenera enquanto se cava, e tem
pontos fracos localizáveis por adivinhação.** `severidade: média` — cap. 710. As notas tinham a
regeneração, mas não a unidade de medida (76 passos abertos por um golpe imortal; +3.000 passos
até um ponto fraco) nem o fato de que **um adivinho consegue calcular onde a parede é fina** —
o que é uma profissão e um item de mercado inteiros.

**L7 — Navegação e viagem por água não existem em nota nenhuma.** `severidade: média`
`06 - Escala, Distâncias e Viagem` tem a escada de mobilidade terrestre e aérea completa, e
nenhuma linha sobre barco. A obra tem: jangada de bambu com vela descendo rio, cinco dias de
viagem, encalhe em recifes (cap. 200); navios mercantes de clã atacados por bandidos (cap. 998);
vilas de pescadores em ilhas do Mar Oriental (cap. 894); elefantes-d'água usados como
embarcação (cap. 1297). E o Mar Oriental tem "milhões, ou dezenas de milhões" de ilhas, quase
todas desabitadas (cap. 894).

**L8 — "Zona proibida" é um conceito operacional do mundo com cinco sentidos distintos, e não
está em lugar nenhum.** `severidade: média`
A obra usa `forbidden zone / area / land` 65 vezes, em cinco acepções que uma mestra precisa
distinguir: (a) a área proibida institucional de um clã, onde nem o líder pode entrar
(caps. 178, 962); (b) a zona ecologicamente letal, cujo núcleo mata (caps. 429, 433); (c) o
cordão político de mil li em volta de um achado, com ordem de matar (cap. 908); (d) a zona
proibida **fabricada** por um Gu, que se expande sozinha e enche o lugar de intenção assassina
(caps. 958-961); (e) o interdito cósmico — Rio do Tempo, Porta da Vida e da Morte, Ordinary
Abyss — "a forbidden area in the great dao" (caps. 196, 384, 401).

## O que foi corrigido

### `04 - As Cinco Regiões.md`
- **Corrigido erro factual** (L4): a frase "Três das cinco paredes são nomeadas na obra" foi
  substituída por uma **tabela das cinco paredes** com nome em português e inglês, cor vista de
  fora e descrição do interior — com `—` explícito nas três que a obra não descreve por dentro.
- **Acrescentado** (L5): as três consequências de mapa — a parede é uma casca que envolve a
  região inteira; as paredes se tocam, logo toda travessia é de duas paredes seguidas; e nada
  vive dentro da parede, ela é o obstáculo inteiro.
- **Acrescentado** (L6): a espessura medida em passos, a regeneração durante a escavação e os
  pontos fracos localizáveis por dedução.
- `fontes` do frontmatter atualizado com caps. 1044, 1045, 1211, 1258.

## Notas novas criadas

*(em andamento)*

## Decisões tomadas

**D1 — Corrigir a nota 04 em vez de criar uma nota "Paredes Regionais".** O material novo sobre
as paredes é grande, mas é o assunto declarado da nota 04, que já tem a escada de conhecimento
em três degraus e as regras de travessia. Alternativa descartada: nota própria — separaria a
parede da região que ela envolve e obrigaria a duplicar a escada de conhecimento.

## Grandes eventos que encontrei

*(para os agentes de `08 - Eventos e Cenarios/`)*

## O que a obra realmente não diz

*(em andamento)*
