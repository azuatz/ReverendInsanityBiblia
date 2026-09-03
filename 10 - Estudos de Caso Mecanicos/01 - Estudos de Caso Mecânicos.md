---
tags:
  - caso-mecanico
  - caso-mecanico/visao-geral
aliases:
  - Mechanical Case Studies
  - Casos mecânicos
status: consolidado
fontes: ["cap. 19", "cap. 40-43", "cap. 84-85", "cap. 90-92", "cap. 98-100", "cap. 110-113", "cap. 115-120", "cap. 128-129", "cap. 143", "cap. 148-159", "cap. 163", "cap. 182-183", "cap. 192-198", "cap. 278", "cap. 290-291", "cap. 294-296", "cap. 304-311", "cap. 324-325", "cap. 359-364", "cap. 404-405", "cap. 416-418", "cap. 461-465", "cap. 485-487", "cap. 515-542", "cap. 567-568", "cap. 683-687", "cap. 707", "cap. 808", "cap. 859-862", "cap. 912-916", "cap. 926", "cap. 946", "cap. 994-995", "cap. 1060", "cap. 1184-1187", "cap. 1206", "cap. 1261", "cap. 1283-1289", "cap. 1394", "cap. 1406-1410", "cap. 1450-1456", "cap. 1490-1512", "cap. 1528-1529", "cap. 1688-1690", "cap. 1790-1791", "cap. 2133-2134", "cap. 2159", "cap. 2172", "cap. 186-189", "cap. 197-199", "cap. 204", "cap. 298-301", "cap. 312-316", "cap. 325-326", "cap. 437", "cap. 451-453", "cap. 479-484", "cap. 899", "cap. 979", "cap. 986-987", "cap. 1071", "cap. 1100", "cap. 1156", "cap. 1161-1162", "cap. 1211", "cap. 1287", "cap. 1433"]
conhecimento: misto — os casos de rank baixo e de mercado são `comum`; os de escala imortal e os marcados no índice são `segredo`
---

# Estudos de Caso Mecânicos

**Em uma frase:** esta pasta é o repositório de ==precedentes== — situações concretas em que
alguém dobrou uma regra do mundo, com o método exposto passo a passo, o preço pago e um
veredito explícito sobre se aquilo é **replicável ou foi sorte irrepetível**.

## Resumo do domínio

As outras pastas do vault descrevem as regras. Esta mostra as regras **sendo usadas**, por
pessoas concretas, com números concretos. Cada nota daqui responde sempre às mesmas cinco
perguntas: *que regra este caso ilustra; qual era a situação; qual foi o método, passo a
passo; por que funcionou (ou falhou); e isso é exceção ou regra?*

Os casos servem a três usos de mesa: **virar aventura pronta**, **virar regra opcional**, ou
**avisar o mestre de um exploit** antes que um jogador o encontre sozinho. Personagens
aparecem aqui apenas como "um cultivador de rank X" — o que interessa é a mecânica, nunca a
história da obra.

> [!note] Duas convenções que valem para a pasta inteira
> - **`> [!example] Regra proposta`** — quase toda nota termina com uma regra de mesa
>   escrita em duas ou três frases, em itálico. Ela é **nossa**, não da obra: é a tradução do
>   precedente em mecânica, oferecida pronta para copiar.
> - **Marcadores de confiabilidade** — texto sem marca é o que a obra afirma; `(ded.)` é
>   dedução nossa a partir do que a obra afirma; `*` é invenção ou estimativa nossa; `—`
>   significa que a obra não informa e nada foi preenchido. **Apagar tudo marcado com `*`
>   devolve qualquer nota desta pasta a cem por cento canônico.**
>
> Os preços de referência do mundo moram em [[02 - Pedras Primordiais|Pedras Primordiais]]; os números do sistema de
> cultivo, em [[02 - Tabelas de Referência Rápida|Tabelas de Referência Rápida]]. Onde uma nota daqui divergir de qualquer uma das
> duas, elas vencem.

> [!warning] Cinco palavras que destravam a pasta inteira
> Esta é a pasta mais densa em jargão do vault. Se você está lendo do zero, estes cinco
> termos resolvem quase tudo:
>
> | Termo | Em uma frase | Nota |
> |---|---|---|
> | **Abertura** | a cavidade sobrenatural dentro de todo Mestre Gu, onde ele guarda os Gu vivos e a energia que os alimenta | [[02 - Abertura|Abertura]] |
> | **Essência primordial** | a energia interna que o Mestre Gu gasta para acionar seus Gu e para cultivar; também é a moeda, em forma sólida | [[04 - Essência Primordial|Essência Primordial]] |
> | **Refino** | sobrescrever a vontade de um Gu com a sua, para poder usá-lo; a operação mais cara e arriscada do sistema | [[06 - Refino de Gu|Refino de Gu]] |
> | **Dao marks** | fragmentos de lei do universo gravados no corpo de um imortal; o atributo de progressão do reino imortal | [[16 - Dao Marks|Dao Marks]] |
> | **Attainment** | o domínio *teórico* de um caminho — o quanto você entende, e não quanta energia você tem; eixo independente do rank | [[08 - Attainment|Attainment]] |
>
> Uma sexta, **fundação**, é definida em [[42 - Anexação de Aberturas|Anexação de Aberturas]], onde ela é decisiva.

## Regras do mundo

Os quatro princípios que quase todos os casos compartilham — e que valem como diretriz de
design para o sistema inteiro:

1. **Vitórias contra oponentes mais fortes vêm de explorar regras estruturais** — custos,
   condições, incompatibilidades —, praticamente nunca de poder bruto.
2. **Informação prévia é o recurso mais decisivo do mundo.** Conhecer uma receita, uma rota,
   um hábito ou um evento futuro vale mais que qualquer artefato isolado.
3. **Todo sistema de garantia tem letra exata, e a letra é sempre explorável.** Contratos,
   selos, proteções e juramentos leem o enunciado, nunca a intenção.
4. **Recursos têm dupla função.** Um ataque inimigo pode ser matéria-prima; um refém pode ser
   escudo; uma derrota pública pode ser investimento em reputação.

E duas regras de leitura que a pasta acrescenta:

5. **Quase nada compra certeza.** Preparação, dinheiro e talento compram **probabilidade**.
   Os pouquíssimos itens do mundo que garantem um resultado são tratados como lendários, e
   mesmo eles têm cláusulas — ver [[36 - Todos os Multiplicadores de um Refino|Todos os Multiplicadores de um Refino]].
6. **Todo atalho cobra numa estatística que não volta.** Aptidão, alma, teto de carreira,
   cronômetro de progressão. Quando um caso parece bom demais, a conta está na seção do preço.
7. **Quando dois efeitos disputam a mesma coisa, vence o de rank mais alto** — nunca o que foi
   aplicado primeiro. É a regra que impede que qualquer ganho seja definitivo, e a que permite
   desfazer o que parecia irreversível.
8. **Ninguém mede a força de ninguém; todos a inferem por sinais.** Espécie, escolta, insígnia,
   maturidade, companhia. Como a leitura é indireta, ela é manipulável dos dois lados da mesa.
9. **Atenção é um recurso à parte da energia, e é o mais escasso de todos.** Manter o que já
   está funcionando é grátis; mudar qualquer coisa custa. Quase todo mundo desanda acima de três
   tarefas simultâneas.

## O índice comentado

### Rank baixo — onde a campanha começa

Se você vai ler só uma parte da pasta, leia esta. São os casos com recursos de rank 1 a 3,
os que cabem numa primeira campanha, e os que mais ensinam sobre o funcionamento comum do
mundo.

| Nota | O que ela ensina |
|---|---|
| [[02 - Punhos Contra uma Camada de Defesa\|Punhos Contra uma Camada de Defesa]] | Defesas têm capacidade medível, e excedê-la com o corpo nu funciona — e custa as duas mãos. |
| [[03 - O Sapo de Rank 5 Que Ninguém Podia Tocar\|O Sapo de Rank 5 Que Ninguém Podia Tocar]] | Bestas selvagens têm listas de gatilhos; um grupo de rank 1 resolve um problema de rank 5 desligando todo o equipamento. |
| [[04 - Um Gu Implantado no Corpo\|Um Gu Implantado no Corpo]] | Alguns Gu substituem um órgão: desempenho de dois ranks acima, pago com automutilação e sigilo. |
| [[05 - O Catalisador Fora da Receita\|O Catalisador Fora da Receita]] | Receitas são versões, não verdades: um ingrediente extra vale +20 pontos de taxa de sucesso. |
| [[06 - Um Gu Acima do Próprio Rank\|Um Gu Acima do Próprio Rank]] | O sistema arbitra vontades, não rótulos — e a aura de um mentor torna um refino de dias em um de segundos. |
| [[07 - Romper o Rank 2 por Teimosia e Pedras\|Romper o Rank 2 por Teimosia e Pedras]] | Aptidão baixa não fecha a porta: põe pedágio nela. O caso mais importante da pasta para a economia do cenário. |
| [[08 - O Atalho Demoníaco de Rank\|O Atalho Demoníaco de Rank]] | Um rank inteiro comprado com dois pontos permanentes de aptidão. A curva moral do caminho demoníaco em números. |
| [[11 - Caçar o Que Não se Vê\|Caçar o Que Não se Vê]] | Tudo o que a invisibilidade não esconde — e como vencer por assimetria de recuperação. |
| [[12 - Roubar o Gu de um Moribundo\|Roubar o Gu de um Moribundo]] | O custo de roubar um Gu cai conforme a vítima piora; e por que a ferramenta barata só rouba coisas baratas. |
| [[13 - Fugir de um Enxame e Sair Montado\|Fugir de um Enxame e Sair Montado]] | Uma fuga é administração de orçamento: enxames têm um nó que se corta, lixo vira isca, e uma besta adormecida vira montaria. |
| [[09 - Comprar um Estágio de Cultivo com Todo o Futuro\|Comprar um Estágio de Cultivo com Todo o Futuro]] | O atalho mais caro do sistema — e o único caso em que a obra mostra um atalho sendo desfeito, derrubando dois ranks. |
| [[10 - Comprar Aptidão com Cem Vidas\|Comprar Aptidão com Cem Vidas]] | A estatística "fixa" do sistema tem preço: sangue da própria linhagem, com rendimento decrescente. De 43% a 90% em seis horas. |
| [[14 - O Refém que Cura os Dois Lados\|O Refém que Cura os Dois Lados]] | Curar alguém com metade de um par e guardar a outra metade cria um contrato sem papel — que se renova sozinho. |

### Combate e estrutura

| Nota | O que ela ensina |
|---|---|
| [[15 - A Barreira Que Deixa Sair e Não Deixa Entrar\|A Barreira Que Deixa Sair e Não Deixa Entrar]] | Toda proteção de mão única é arma em potencial contra o próprio dono. E todo dreno "simétrico" é assimétrico. |
| [[16 - O Ambiente Manda Mais que o Rank\|O Ambiente Manda Mais que o Rank]] | Lugares que desligam categorias inteiras de ferramentas — e as isenções individuais que produzem massacres. |
| [[18 - Emboscada de Um Contra Sete\|Emboscada de Um Contra Sete]] | Como se quebra um grupo especializado: pelo detector e pela confiança, não pelo mais forte. |
| [[20 - Guerra de Custos\|Guerra de Custos]] | Compare custo por ação, não dano. O mesmo teorema num duelo de arena e numa guerra de exércitos. |
| [[17 - Sobrecarregar o Defensor que Devolve o Golpe\|Sobrecarregar o Defensor que Devolve o Golpe]] | Atenção é um recurso separado da energia, e o teto dele é três. Manter é grátis; mudar é que custa caro. |
| [[19 - Perder de Propósito e Cobrar Caro\|Perder de Propósito e Cobrar Caro]] | Uma **derrota**: quem vai perder ainda escolhe entre tentar vencer e encarecer a vitória do outro. |
| [[21 - Um Trunfo que Nunca Foi Testado\|Um Trunfo que Nunca Foi Testado]] | Ninguém mede força, todo mundo a infere — e um blefe bem montado compra dois patamares de aparência. |

### Dinheiro, mercado e informação

| Nota | O que ela ensina |
|---|---|
| [[22 - Aposta de Rochas - Heurística, Perda e Álibi\|Aposta de Rochas: Heurística, Perda e Álibi]] | Nove em dez pedras são vazias — e o verdadeiro produto da casa é o álibi de origem. |
| [[23 - Ganhar um Leilão Sem Ser o Maior Lance\|Ganhar um Leilão Sem Ser o Maior Lance]] | Três formatos de leilão, e em todos vence quem lê melhor as outras pessoas. |
| [[24 - Colher a Flor Antes do Prazo\|Colher a Flor Antes do Prazo]] | Um tesouro que cresce, um pagamento que tem de ser à vista, e uma comunidade que morre junto. |
| [[25 - Comprar Antes que Seja Notícia\|Comprar Antes que Seja Notícia]] | Informação antecipa preços, não se gasta ao ser vendida, e vale zero quando todos a têm. |
| [[27 - A Conta de uma Calamidade\|A Conta de uma Calamidade]] | A planilha completa de um desastre: 666 km² perdidos, quarenta anos de atraso — e um cadáver que paga tudo. |
| [[28 - Guerra de Preços\|Guerra de Preços]] | Por que possuir um artefato lendário é o mesmo que possuir um setor inteiro da economia. |
| [[26 - Dar de Graça o que Vai Vazar\|Dar de Graça o que Vai Vazar]] | Todo segredo tem prazo de validade. O que vai vazar em três dias se dá de graça; cobra-se o que não vaza sozinho. |

### Palavra, reputação e organizações

| Nota | O que ela ensina |
|---|---|
| [[29 - Brechas de Contrato Mágico\|Brechas de Contrato Mágico]] | Quatro brechas reais. O contrato confere palavras; ele não entende nada. |
| [[30 - Reputação Comprada em Prestações\|Reputação Comprada em Prestações]] | Quanto custa uma reputação regional, como se paga, e por que ela protege melhor que um Gu. |
| [[31 - Chantagem e Extorsão por Informação\|Chantagem e Extorsão por Informação]] | Como um segredo inverte uma situação de morte certa — e por que o chantagista competente cobra parcelado. |
| [[32 - Infiltrar-se numa Organização\|Infiltrar-se numa Organização]] | Identidade é verificada por vários canais independentes, e nenhum disfarce cobre hábitos. |

### Criar, refinar e produzir

| Nota | O que ela ensina |
|---|---|
| [[33 - Uma Receita Lendária Cumprida com Substitutos\|Uma Receita Lendária Cumprida com Substitutos]] | Receitas antigas pedem atributos, não objetos — e matéria-prima pode ser o ataque do inimigo. |
| [[34 - Um Golpe Mal Testado Usado Além do Limite\|Um Golpe Mal Testado Usado Além do Limite]] | Um **fracasso**: cada peça de um golpe impõe uma condição ao conjunto, e descobri-la doeu metade de uma alma. |
| [[35 - Do Golpe à Formação\|Do Golpe à Formação]] | A escada de três degraus que transforma um efeito caro e momentâneo num estado barato e compartilhável. |
| [[36 - Todos os Multiplicadores de um Refino\|Todos os Multiplicadores de um Refino]] | Um sucesso caríssimo e três fracassos sabotados, lado a lado. O item que zera a sorte e não zera a perícia. |
| [[37 - A Linha de Produção de Gu\|A Linha de Produção de Gu]] | Fatiar uma receita em etapas protege o segredo melhor do que guardá-lo. |
| [[38 - O Gu Que Escolhe o Portador\|O Gu Que Escolhe o Portador]] | Travas que avaliam o estado interno do candidato — e não a moral dele. |

### Heranças, territórios e escala imortal `[segredo]`

O que vem abaixo é conhecimento de pouquíssimas pessoas no mundo. Um personagem jogador de
rank baixo não sabe nada disto, e a maior parte serve ao mestre.

| Nota | O que ela ensina |
|---|---|
| [[39 - As Três Chances de um Espírito Guardião\|As Três Chances de um Espírito Guardião]] | Regras de contagem assimétricas: dois herdeiros com o mesmo direito, resultados opostos. |
| [[40 - Tomar um Território pelas Três Vias\|Tomar um Território pelas Três Vias]] | Enganar, suprimir e — a via que **não funciona** — invadir e depois pedir. |
| [[41 - Um Mortal Refina um Gu Imortal\|Um Mortal Refina um Gu Imortal]] | A unicidade dos artefatos é uma verificação em tempo real, e pode ser cronometrada. |
| [[42 - Anexação de Aberturas\|Anexação de Aberturas]] | Fundação vence rank. Crescer para os lados adia crescer para cima. |
| [[43 - Roubo de um Gu Imortal de Rank Superior\|Roubo de um Gu Imortal de Rank Superior]] | O roubo é o elo fácil da corrente; o relógio de três dias é o difícil. |
| [[46 - Curar o Dano para Repetir o Dano\|Curar o Dano para Repetir o Dano]] | Ter o dano e a cura do dano converte um recurso finito em infinito — e o único freio é a fadiga do operador. |
| [[47 - Escolher o Terreno da Própria Tribulação\|Escolher o Terreno da Própria Tribulação]] | A prova é montada com o material do terreno — e o céu aprende com quem já o explorou. |
| [[48 - Fazenda de Tribulações\|Fazenda de Tribulações]] | Uma exploração em que as duas partes ganham de verdade, e mesmo assim uma delas é safra. |
| [[49 - Explorar um Reino de Sonho\|Explorar um Reino de Sonho]] | Método barato vence ferramenta melhor: um explorador com hipóteses contra trinta e seis falhas. |
| [[44 - A Armadilha que Engorda a Cada Teste\|A Armadilha que Engorda a Cada Teste]] | Um **fracasso**: há defesas que lucram com cada tentativa de arrombá-las, e só a segunda medição revela isso. |
| [[45 - Quando a Adivinhação Falha\|Quando a Adivinhação Falha]] | Outro **fracasso**: a lista fechada do que bloqueia uma dedução — e por que acertar demais denuncia um patrono oculto. |

## O que todo personagem sabe

Isto é conhecimento comum no mundo e pode ir direto para a mesa dos jogadores: que defesas
se quebram com força suficiente; que bestas selvagens têm gatilhos conhecidos e que se pode
pesquisá-los; que receitas têm versões melhores; que andar com um mentor de rank alto
facilita refinos; que aptidão baixa se compensa com dinheiro e tempo nos primeiros ranks;
que alguns Gu substituem um órgão do corpo, cobrando dor e sigilo em troca de desempenho acima do rank; que certos lugares do mundo desligam o uso de Gu para todos que estão dentro deles; que a aposta de rochas quase sempre dá prejuízo e serve de álibi; que leilões se ganham lendo
as pessoas; que a palavra empenhada em juramento é executada ao pé da letra; e que reputação
é o que substitui a polícia inexistente. Acrescente ainda: que manter vários Gu ligados ao mesmo
tempo consome **atenção**, e que quase ninguém sustenta mais de três coisas de uma vez sem
errar; que bandos de bestas têm um animal que os coordena, e que matá-lo dispersa o bando; que
um perdedor pode gastar a última gota destruindo o equipamento do vencedor, e que isso é
considerado uma jogada legítima; que a força de alguém é sempre **inferida** por sinais visíveis,
nunca medida — e que sinais, portanto, podem ser fabricados; e que informação tem prazo de
validade, de modo que a notícia que vai vazar sozinha vale mais como favor do que como
mercadoria.

## O que só o mestre sabe

Isto muda a leitura do cenário e não deve ser distribuído: que os artefatos únicos ocupam
"vagas" verificadas pelo mundo em tempo real, e que a vaga reabre quando o exemplar é
destruído; que os espíritos guardiões avaliam **conduta acumulada** e não podem mentir; que
a fundação vence o rank na disputa por territórios; que a provação de um cultivador é
matéria-prima colhível por terceiros, e que existe quem fabrique provações em série para
colhê-las; que possuir ao mesmo tempo um dano e a cura daquele dano torna infinito um recurso que deveria ser finito — inclusive a resistência de um prisioneiro a interrogatório; e que a vontade celeste **se adapta** a quem já a explorou. Junte a isto quatro
segredos que as notas novas trazem: que a **aptidão não é fixa** e pode ser comprada com sangue
da própria linhagem, o que significa que um clã inteiro pode ter sido plantado como safra; que,
quando dois efeitos disputam a mesma estatística, vence sempre o de **rank mais alto**,
independentemente da ordem — de modo que nenhum ganho comprado com um Gu de rank baixo é
realmente permanente; que existem defesas que **lucram** com cada tentativa de arrombá-las, e
que insistir nelas as fortalece; e que a adivinhação tem uma lista **fechada** de bloqueios,
sendo o mais forte deles simplesmente estar dentro de um mundo pequeno.

## Índice rápido: exceção × regra

| Caso | Veredito |
|---|---|
| Punhos contra uma camada de defesa | **Regra** — depende de conhecer a capacidade da defesa |
| O sapo de rank 5 | **Regra** — protocolos de instinto são pesquisáveis |
| Gu implantado no corpo | **Regra** — categoria conhecida de uso, com preço corporal fixo |
| Catalisador fora da receita | **Regra** — receitas são versões |
| Gu acima do próprio rank (aura emprestada) | **Regra corrente e cotidiana**; a versão passiva é exceção rara |
| Avanço forçado por disciplina e pedras | **Regra**, mas só na ruptura 1 → 2 e a preço proibitivo — troca potência por tempo e dinheiro, **nunca talento por dinheiro** |
| Avanço forçado por ritual demoníaco | **Regra** — materiais comuns, custo permanente |
| Caçar o que não se vê | **Regra** — não exige item nenhum |
| Roubar o Gu de um moribundo | **Regra**, limitada pelo rank da ferramenta |
| Barreira de mão única | **Regra universal** — toda assimetria é arma |
| O ambiente manda mais que o rank | **Regra ambiental universal**, com isenções individuais nomeadas |
| Emboscada de um contra sete | **Regra tática**, dependente de informação prévia |
| Guerra de custos | **Regra estrutural** — define um caminho inteiro |
| Aposta de rochas | **Regra** — instituição estável; o álibi é o produto real |
| Leilões | **Regra**, nos três formatos |
| Colher a flor antes do prazo | **Regra** — recurso vivo, pagamento à vista, fonte destruída |
| Comprar antes que seja notícia | **Regra corrente e legal** |
| A conta de uma calamidade | **Regra** — o balanço é sempre deste formato; o artefato da criatura decide o sinal |
| Guerra de preços | **Regra** de mercado; excepcional é possuir a fonte |
| Brechas de contrato | **Regra absoluta e universal** |
| Reputação em prestações | **Regra estruturante** — com preço de tabela |
| Chantagem e extorsão | **Regra corrente**, e simétrica contra os jogadores |
| Infiltração | **Regra dos dois lados da mesa** |
| Receita lendária com substitutos | **Regra** quanto ao princípio; exceção quanto à coincidência |
| Golpe mal testado | **Regra dura** — é a trava de equilíbrio do sistema de golpes |
| Do golpe à formação | **Regra geral de engenharia de efeitos** |
| Multiplicadores de refino | **Regra** — nenhum preparo compra certeza, exceto um item com cláusulas |
| Linha de produção | **Regra** — replicável com capital, mão de obra e receita exclusiva |
| Gu que escolhe o portador | **Regra** quanto ao princípio; exceção quanto ao lugar |
| As três chances do espírito guardião | **Regra** — depende só de informação |
| Território — enganar | **Regra** — barata e confiável |
| Território — suprimir | **Regra** — cara, deixa rastro |
| Território — invadir e pedir | **Não funciona** — trava independente |
| Refino de Gu Imortal por um não-imortal | Exceção extrema; princípio replicável |
| Anexação de aberturas | **Regra** do sistema; fundação excepcional. O limiar real é o attainment |
| Roubo de artefato de rank superior | Estrutura é regra; alvo foi exceção |
| Curar o dano para repetir o dano | **Regra econômica**; a escala industrial é exceção |
| Terreno da tribulação | **Regra** para quem escolhe onde ascender |
| Fazenda de provações | Princípio é regra; escala é exceção |
| Reino de sonho | Método é regra; a escala imortal é exceção de fundação |
| Fuga por gerenciamento de recursos | **Regra** — o que é raro é o repertório, não o poder |
| Liquidar o potencial da abertura | **Regra** do sistema; o item é que é raro e de uso único |
| Comprar aptidão com sangue de linhagem | **Regra**, com pré-requisito de séculos — é um projeto, não uma técnica |
| Refém mútuo por Gu pareado | **Regra** quanto ao princípio; exceção quanto à oportunidade |
| Sobrecarregar o defensor por multitarefa | **Regra estrutural** — o teto de atenção vale para todo Mestre Gu |
| Perder de propósito e cobrar caro | **Regra**, e das mais replicáveis; a oportunidade é que foi excepcional |
| Vender informação perecível | **Regra corrente e legal** do mercado de informação |
| Blefe de patamar por aparência | **Regra geral** — sinais de poder são leituras, e leituras se fabricam |
| Armadilha que se autoalimenta | Método é **regra**; a construção é exceção de altíssimo nível |
| Falha de adivinhação | **Regra do sistema** — a lista de bloqueios é fechada e o teto é por rank |

## Relações

- [[01 - Visão Geral da Sociedade|Visão Geral da Sociedade]] — as regras sociais que vários destes casos exploram.
- [[06 - Caminho Correto e Caminho Demoníaco|Caminho Correto e Caminho Demoníaco]] — o contexto dos métodos proibidos.
- [[14 - Tribunal Celestial e Grandes Forças|Tribunal Celestial e Grandes Forças]] — a política de alto nível em que os casos imortais acontecem.
- [[04 - Como um Mestre Gu Ganha a Vida|Como um Mestre Gu Ganha a Vida]] — o lado econômico dos mesmos recursos.
- [[15 - Economia Imortal|Economia Imortal]] — os números que tornam alguns destes custos compreensíveis.
- [[02 - Tabelas de Referência Rápida|Tabelas de Referência Rápida]] — a fonte soberana de todos os números citados aqui.
