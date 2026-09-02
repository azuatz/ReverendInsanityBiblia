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

### `13 - Cosmologia.md`
- **Acrescentada a seção "Sim, existe um sol — e os céus são filtros"** (L2), que resolve a
  ambiguidade mais perigosa do domínio: o mundo tem sol, lua e estrelas comuns, e os dois céus são
  **filtros** por cima deles — a luz atravessa o céu branco (dia) e não atravessa o negro (noite),
  porque a luz de hoje é um resíduo enfraquecido da luz imemorial, que atravessava os nove.
- **Acrescentado** o corolário econômico: com sete céus caídos, os trovões dos dois restantes quase
  nunca se chocam, e a pedra de refino que nascia desse choque praticamente deixou de ser produzida
  — uma catástrofe de milhões de anos atrás que ainda se manifesta como escassez de mercado.
- `fontes` atualizado com caps. 21, 34, 73, 559, 1028.

### `01 - Visão Geral do Mundo.md`
- **Corrigido o risco de leitura de L2**: a linha "existem dois céus que se alternam como dia e
  noite" agora diz explicitamente que isso **não** substitui o sol, e aponta para a seção nova de
  Cosmologia e para `16 - O Relógio do Mundo`.
- Tabela "Mapa da pasta" e sugestão de ordem de leitura atualizadas com as três notas novas.

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

> As três notas nasceram com prefixo provisório continuando o maior da pasta (`16`, `17`, `18`).
> **A posição de leitura correta é outra** — indicada abaixo. O orquestrador deve rodar
> `_pipeline/numerar-notas.py` com a ordem nova para renumerar e reescrever os wikilinks.

### `16 - O Relógio do Mundo.md` — resolve L1 e L2
Posição de leitura sugerida: **logo depois do Atlas e antes de "Escala, Distâncias e Viagem"**
(posição 6 na ordem nova). O Atlas diz onde o grupo está; esta nota diz quando e com que tempo.
Cobre: o céu ordinário (sol, lua, estrelas, fases) e a costura com os dois céus; o calendário
(meses, data corrente, calendário regional, ausência de ano numerado, eras com nome de Venerável,
Ano Novo e a idade coletiva, calendário institucional de meio e fim de ano); as três escalas de
duração (hora / sopro / vareta de incenso) e o vigia noturno como relógio público; dia e noite
(perigo por falta de luz, Gu de visão noturna, "de dia se luta, de noite se conspira"); as quatro
estações, o clima regional permanente, o zoneamento vertical de montanha e a estação mudando o que
o terreno produz; quem controla o clima; e a regra de tom mais forte do achado — **quase todo
desastre deste mundo tem culpado**.

### `17 - As Plantas e os Bichos Comuns.md` — resolve L3
Posição de leitura sugerida: **imediatamente antes de "Bestas Gu e Reis Fera"** (posição 8 na
ordem nova). É a metade não-mágica da natureza, e prepara a metade mágica.
Cobre: a regra "bicho não é Gu" com a citação decisiva; o aviso de que muita "erva" da obra é um Gu;
plantas comuns nomeadas e a grama-zarabatana como planta-que-vira-dinheiro-e-gera-Gu; a escada de
grau das plantas `(ded.)` e as três plantas de topo (árvore-bruma-das-mil-serpentes, Árvore dos Mil
Desejos, girassóis-de-rosto-fantasma); agricultura real e a **regra social** de que plantar é
trabalho de mortal de fora; os Gu de rank 1 que produzem comida e por que isso explica a estrutura
social; fauna comum e comportamento animal utilizável como regra de rastreamento; a tabela de
montarias; rebanho, couro e a especialização de criação por terreno; e a regra de que **todo ser
vivo precisa comer, imortais inclusive**.

### `18 - O Selvagem, as Ruínas e as Zonas Proibidas.md` — resolve L8 e o item "seguro × selvagem"
Posição de leitura sugerida: **imediatamente depois de "Bestas Gu e Reis Fera"** (posição 10 na
ordem nova). Fecha o movimento "o que existe fora dos muros".
Cobre: o selvagem como padrão do mapa e o assentamento como exceção; a régua **rank 3 para sair,
rank 4 para andar sozinho**, com a tabela de classes de mobilidade; a estrada como lugar; a
fronteira do seguro que recua durante uma maré de bestas; a ausência de cartografia pública e os
códigos idiossincráticos dos mapas de caçador; **os cinco sentidos de zona proibida**
(institucional, ecológica, política, fabricada, cósmica) com exemplo mecânico de cada; e a seção
sobre por que uma ruína continua perigosa — o qi de rancor como substância interrogável, o acúmulo
de morte atraindo raios, a ruína que gera população própria, e batalhas imortais que apagam
acidentes geográficos deixando os nomes órfãos.

### Ordem de leitura completa proposta para a pasta

1. Visão Geral do Mundo · 2. A Filosofia do Mundo · 3. As Duas Eras de um Mestre Gu ·
4. As Cinco Regiões · 5. Atlas das Cinco Regiões · **6. O Relógio do Mundo** ·
7. Escala, Distâncias e Viagem · **8. As Plantas e os Bichos Comuns** · 9. Bestas Gu e Reis Fera ·
**10. O Selvagem, as Ruínas e as Zonas Proibidas** · 11. Lendas de Ren Zu ·
12. Blessed Lands e Grotto-Heavens · 13. Viver Dentro da Abertura Imortal · 14. Vontade dos Céus ·
15. Fate Gu · 16. Cosmologia · 17. Lugares Fora das Cinco Regiões · 18. Tribunal Celestial.

`01 - Visão Geral do Mundo.md` **já foi atualizada** com as três notas novas na tabela "Mapa da
pasta" e no texto da sugestão de ordem de leitura, usando os nomes de arquivo atuais.

## Decisões tomadas

**D1 — Corrigir a nota 04 em vez de criar uma nota "Paredes Regionais".** O material novo sobre
as paredes é grande, mas é o assunto declarado da nota 04, que já tem a escada de conhecimento
em três degraus e as regras de travessia. Alternativa descartada: nota própria — separaria a
parede da região que ela envolve e obrigaria a duplicar a escada de conhecimento.

## Grandes eventos que encontrei

*(para os agentes de `08 - Eventos e Cenarios/`)*

## O que a obra realmente não diz

*(em andamento)*
