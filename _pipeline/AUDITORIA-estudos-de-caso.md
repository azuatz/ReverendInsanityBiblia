# Auditoria — pasta `09 - Estudos de Caso Mecanicos`

> Relatório do agente responsável pela pasta `09`. **Estado: concluído.**
> Resultado em números: de **1 nota de 823 linhas** para **39 notas** (1 porta + 38 casos),
> ~4.400 linhas. Auditoria de links: **0 links quebrados** no vault inteiro.

## O problema de partida

A pasta tinha **uma única nota de 823 linhas** com nove casos empilhados, vários deles com
duas ou três variantes internas. O modelo do projeto
(`_pipeline/MODELOS/modelo-estudo-de-caso.md`) prevê **uma nota por caso**, e uma nota de 823
linhas não se consulta: a designer não acha o caso pelo nome na barra lateral.

Havia ainda dois desequilíbrios de conteúdo, apontados também pela revisão didática anterior
(`_pipeline/REVISAO-didatica-05-09.md`, item 08-H, "cobertura concentrada no topo"):

- **de escala** — a maioria dos casos era de rank 6+, justamente a faixa em que uma campanha
  *não* começa;
- **de resultado** — quase todos os casos eram vitórias. Fracassos ensinam os limites da
  regra, e a obra tem vários.

## Como a pasta foi desdobrada

Ordem de leitura final (é a numeração já aplicada em disco; a barra lateral do Obsidian já
está no currículo correto). Para o `_pipeline/numerar-notas.py`, a entrada da pasta `09` deve
passar a ser exatamente esta lista de títulos, na ordem:

| # | Nota | Origem |
|---|---|---|
| 01 | Estudos de Caso Mecânicos | porta reescrita |
| **Bloco 1 — rank baixo, onde a campanha começa** |||
| 02 | Punhos Contra uma Camada de Defesa | **novo** |
| 03 | O Sapo de Rank 5 Que Ninguém Podia Tocar | **novo** |
| 04 | Um Gu Implantado no Corpo | **novo** |
| 05 | O Catalisador Fora da Receita | **novo** |
| 06 | Um Gu Acima do Próprio Rank | caso 3 da nota antiga |
| 07 | Romper o Rank 2 por Teimosia e Pedras | caso 2 (versão barata) |
| 08 | O Atalho Demoníaco de Rank | caso 2 (versão cara) |
| 09 | Caçar o Que Não se Vê | **novo** |
| 10 | Roubar o Gu de um Moribundo | **novo** |
| **Bloco 2 — combate e estrutura** |||
| 11 | A Barreira Que Deixa Sair e Não Deixa Entrar | **novo** |
| 12 | O Ambiente Manda Mais que o Rank | **novo** |
| 13 | Emboscada de Um Contra Sete | **novo** |
| 14 | Guerra de Custos | **novo** |
| **Bloco 3 — dinheiro, mercado e informação** |||
| 15 | Aposta de Rochas - Heurística, Perda e Álibi | **novo** |
| 16 | Ganhar um Leilão Sem Ser o Maior Lance | **novo** |
| 17 | Colher a Flor Antes do Prazo | **novo** |
| 18 | Comprar Antes que Seja Notícia | **novo** |
| 19 | A Conta de uma Calamidade | **novo** |
| 20 | Guerra de Preços | **novo** |
| **Bloco 4 — palavra, reputação e organizações** |||
| 21 | Brechas de Contrato Mágico | caso 9 da nota antiga |
| 22 | Reputação Comprada em Prestações | **novo** |
| 23 | Chantagem e Extorsão por Informação | **novo** |
| 24 | Infiltrar-se numa Organização | **novo** |
| **Bloco 5 — criar, refinar e produzir** |||
| 25 | Uma Receita Lendária Cumprida com Substitutos | **novo** |
| 26 | Um Golpe Mal Testado Usado Além do Limite | **novo** |
| 27 | Do Golpe à Formação | **novo** |
| 28 | Todos os Multiplicadores de um Refino | **novo** |
| 29 | A Linha de Produção de Gu | **novo** |
| 30 | O Gu Que Escolhe o Portador | **novo** |
| **Bloco 6 — heranças, territórios e escala imortal `[segredo]`** |||
| 31 | As Três Chances de um Espírito Guardião | caso 5 da nota antiga |
| 32 | Tomar um Território pelas Três Vias | caso 4 + o caso do V6 |
| 33 | Um Mortal Refina um Gu Imortal | caso 1 da nota antiga |
| 34 | Anexação de Aberturas | caso 6 da nota antiga |
| 35 | Roubo de um Gu Imortal de Rank Superior | caso 7 da nota antiga |
| 36 | Curar o Dano para Repetir o Dano | **novo** |
| 37 | Escolher o Terreno da Própria Tribulação | **novo** |
| 38 | Fazenda de Tribulações | caso 8 da nota antiga |
| 39 | Explorar um Reino de Sonho | **novo** |

**A nota `01` deixou de ser depósito e virou porta de entrada:** índice comentado agrupado
por tema (uma linha dizendo o que cada caso ensina), "Resumo do domínio", "Regras do mundo"
(os quatro meta-padrões da nota antiga mais dois novos), a tabela de vocabulário mínimo, as
seções "O que todo personagem sabe" / "O que só o mestre sabe" e a tabela "exceção × regra"
com as 41 entradas. O **nome do arquivo foi preservado** de propósito: sete notas de outras
pastas apontam para `01 - Estudos de Caso Mecânicos`.

## Casos acrescentados

Vinte e nove casos novos. Fontes: `_pipeline/rascunho/estudos-de-caso.md` (o que nunca havia
chegado à nota final) e verificação direta no texto-fonte.

### Rank baixo (prioridade declarada da tarefa)

| Nota | Capítulos | Mecânica que ilustra |
|---|---|---|
| Punhos Contra uma Camada de Defesa | 34-35, 84-86, 100 | Defesa tem **capacidade de absorção medível** (16 atacantes simultâneos; a versão fundida, 30+). Excedê-la com o corpo nu funciona e custa os dois punhos (ossos dos dedos expostos). Mortais treinados vencem Mestres Gu novatos no corpo a corpo, com teto próprio. |
| O Sapo de Rank 5 Que Ninguém Podia Tocar | 117-120 | **Protocolo de instinto** de besta selvagem com gatilhos declarados. Números: força de 5-6 adultos contra os "2 bois" necessários; 300 m de empurrão; recompensa de 500 pedras + promoção. Ajuda de aliados não conta se ficarem fora da percepção do animal. |
| Um Gu Implantado no Corpo | 128-129 | Gu que **substitui um órgão**: rank 2 com desempenho de rank 3, alcance de 300 passos **se as raízes tocarem o solo**. Preço: decepar a própria orelha, sem anestesia. Mais a técnica de isca viva. |
| O Catalisador Fora da Receita | 98-100 | Os **três fatores de taxa de sucesso** de uma fusão, enumerados pela obra, e o número exato de um catalisador não documentado: **+20 pontos percentuais**. Fusão preserva uma habilidade e descarta a outra. |
| Caçar o Que Não se Vê | 115-116 | O que a invisibilidade **não** cobre (tecido, sangue, rastro); Gu Vital como alarme; feras inteligentes recuam feridas, javali/touro entram em frenesi; e a **migração do Gu do rei morto para o sucessor**, com janela de captura. |
| Roubar o Gu de um Moribundo | 143 | As três limitações do Gu de pilhagem: custo proporcional à força do alvo, contragolpe na falha, e **teto de rank** (rank 2 não extrai um rank 3). Contra alvo à beira da morte, "não era difícil de forma alguma". |

### Combate e estrutura

| Nota | Capítulos | Mecânica |
|---|---|---|
| A Barreira Que Deixa Sair e Não Deixa Entrar | 192-198 | Comparação explícita entre as duas gerações do Gu (a antiga prende o dono, a "melhorada" o deixa sair) + as três propriedades que se combinam num modo de falha. Regra irmã: dreno mútuo perde-perde decidido pela **taxa de regeneração**, não pela reserva. |
| O Ambiente Manda Mais que o Rank | 379-385, 1216-1217, 1257-1259 | Duas regras ambientais com números: terra que **sela todos os Gu** (rank 4 patrocinado mata rank 5 "como gado"; mortos não conseguem autodestruir o inventário) e muralha regional (**50-60% da força**; golpes ferem o usuário antes do alvo; corpo físico escapa da penalidade). |
| Emboscada de Um Contra Sete | 359-364 | Como se quebra um esquadrão especializado: segredo interno revelado, munição finita esgotada de propósito, **matar o investigador antes do alvo valioso**, e o membro fraco como refém funcional. |
| Guerra de Custos | 290-291, 515, 535, 542 | Atrito por **custo por ação**: atacar o tanque em vez do dono (forçando cura + troca de posição, cujo preço escala com a massa) e 280.000 lobos gastos para secar uma linha defensiva. |

### Dinheiro, mercado e informação

| Nota | Capítulos | Mecânica |
|---|---|---|
| Aposta de Rochas | 40-43 | **Nove em dez pedras vazias**; funil de heurísticas (cor, tamanho +30%, textura, formato) que reduziu o salão a 6 candidatas com 80% de confiança; e o uso secundário — o fóssil destruído como **álibi de origem irrefutável**. |
| Ganhar um Leilão Sem Ser o Maior Lance | 110-113, 304-311, 747-763 | Três formatos: lance cego (perder por 10 pedras de propósito → convite de emprego), leilão aberto como arma (810.000 pagas por um item inutilizável, por rancor) e escambo imortal (o vendedor escolhe; a oferta temática vence a maior). |
| Colher a Flor Antes do Prazo | 163, 182-183 | **+50.000 pedras**, e a trava que faz o caso: em parcelas **falha**, porque o Gu-planta reabsorve a energia para repor a nascente. A colheita mata a nascente permanentemente. |
| Comprar Antes que Seja Notícia | 112, 324-325 | Insider trading de herança (**3× em ~10 dias**), liquidação de imóveis antes de catástrofe, e venda dupla do mesmo segredo (400.000, com pagamento **em duas parcelas, a segunda condicionada à verificação**). |
| A Conta de uma Calamidade | 416-418 | A planilha completa: **666 km²**, 68 contas de essência restantes, 4.700.000 → 310.000 raposas, ~700.000 Gu, **40 anos** de desenvolvimento — contra o corpo da besta desolada, que vale mais que tudo. Parte das perdas foi **decidida** (contenção). |
| Guerra de Preços | 1450-1456 | Custo marginal **3-4 contra 10**; 1.730.000 de capital de giro; **12 milhões** de lucro; mercado saturado por 4-5 anos. |

### Palavra, reputação e organizações

| Nota | Capítulos | Mecânica |
|---|---|---|
| Reputação Comprada em Prestações | 105, 286-293, 314 | **200.000 pedras** pagas em parcelas públicas; a citação da obra comparando reputação a um salvo-conduto que 200.000 não comprariam; a derrota calculada que destrói o patrimônio do vencedor; e a ameaça de perder de propósito. |
| Chantagem e Extorsão por Informação | 154-155, 178-179, 294-296 | O **rastro periférico** que o encobrimento não apaga (a nota fiscal do Gu de limpeza) e a extorsão existencial de **3.000.000**, com 500.000 de entrada — a estrutura parcelada é o que a torna sustentável. |
| Infiltrar-se numa Organização | 215-224, 426-434, 1115-1128, 1220 | Tabela dos **canais de verificação** e como cada um é burlado — com o achado de que **nenhuma ferramenta cobre hábitos**. O teto: passou por um Gu de verificação **rank 7**, e o próprio texto diz que rank 8 provavelmente o pegaria. |

### Criar, refinar e produzir

| Nota | Capítulos | Mecânica |
|---|---|---|
| Uma Receita Lendária Cumprida com Substitutos | 404-405 | Receita mítica satisfeita por **atributos**, não objetos — incluindo um Gu implantado por um inimigo e um golpe inimigo usado como banho de refino. Aceleração ×9 com perda de estabilidade, compensada por um item de **sucesso garantido**. |
| Um Golpe Mal Testado Usado Além do Limite | 541, 543, 1287-1289 | **Fracasso.** 14+ Gu, defesa ×4, força 800 *jun* — usado voando (condição proibida) e além do tempo teorizado: alma de 1.000 para **500**. Golpes normais amadurecem em **gerações**; a correção é trocar **um** componente. |
| Do Golpe à Formação | 1406-1410 | A escada de custo, com números: 10% removidos por uso contra regeneração total em **meio dia** = meio mês ininterrupto. Solução em dois degraus: núcleo de continuidade → formação (barata, compartilhável, transportável). |
| Todos os Multiplicadores de um Refino | 859-862, 926, 946, 982 | **Fracasso e sucesso lado a lado.** A marca de sucesso zera **a falha natural até o rank 6** e **não** protege contra erro do operador. Contraponto: três falhas seguidas por **materiais adulterados de forma indetectável** pela financiadora. |
| A Linha de Produção de Gu | 707, 815, 862 | Os quatro ganhos enumerados pelo texto (não vazar receita; taxa de sucesso por repetição; perícia exigida menor; dono só controla materiais), o gargalo (60% das salas vazias) e o limite: **receitas de execução contínua não podem ser divididas**. |
| O Gu Que Escolhe o Portador | 567-568, 1283-1287 | Travas **motivacionais**: avaliam o estado, não a moral. E o refino feito **sem material nenhum**, só com um estado psicológico sustentado. |

### Escala imortal

| Nota | Capítulos | Mecânica |
|---|---|---|
| Curar o Dano para Repetir o Dano | 808, 1198-1199, 1247, 1493, 1502-1503 | Dano + cura do dano = recurso infinito; a durabilidade da vítima deixa de ser limite. O único freio é o desgaste do **operador**, que a mesma cura não repara. Versão econômica: o ciclo industrial de alma, cujo gargalo é o **insumo**, não a fábrica. |
| Escolher o Terreno da Própria Tribulação | 683-687, 1060, 1112, 1165, 1462, 1469 | Trade-off explícito: energia rala = prova branda **e** fundação pior, com Gu de estocagem de energia para desacoplar os dois. Terreno com compreensão impressa = avanço direto de attainment (transformação e voo num só evento). E o céu **se adapta**. |
| Explorar um Reino de Sonho | 912-916, 1490-1512 | **Fracasso comparado ao sucesso:** 36 falhas seguidas sem método contra grão-mestre duplo em menos de um mês com dedução por iteração. Mais as regras do lugar e a tabela de consumo de fundação de alma por estágio. Registra uma **contradição da obra deixada em aberto**. |

## Casos que fundi

| Nota | O que foi fundido | Por quê |
|---|---|---|
| **06 - Um Gu Acima do Próprio Rank** | Gu debilitado como Gu Vital (cap. 19) + refino sob aura emprestada (caps. 20-21, 116, 138, 143, 162, 167) | É a mesma regra vista pelos dois lados: o sistema arbitra o **estado real** das vontades, não o rank nominal. Separar produziria duas notas que dizem a mesma frase. |
| **11 - A Barreira Que Deixa Sair e Não Deixa Entrar** | Escudo de mão única + dreno mútuo contra um zumbi | Duas armas da mesma batalha, e a mesma lição: a **regra estrutural** decide, não a força. A segunda entra como "regra irmã", não como caso próprio. |
| **12 - O Ambiente Manda Mais que o Rank** | Terra que sela Gu (V2) + muralha regional (V5) | Idêntica estrutura: regra ambiental universal + isenção individual. Juntas, o par prova que a regra é uma categoria do sistema, e não um lugar peculiar. |
| **14 - Guerra de Custos** | Atacar o alvo "errado" num duelo + atrito com lobos numa guerra | O mesmo teorema em escalas opostas. O contraste de escala **é** o argumento. |
| **16 - Ganhar um Leilão Sem Ser o Maior Lance** | Lance cego + leilão como arma social + leilão de escambo imortal | São três **formatos** do mesmo evento; separadas, a designer não veria que a variável decisiva (quem determina o preço final) muda de formato para formato. |
| **18 - Comprar Antes que Seja Notícia** | Insider trading + liquidação pré-catástrofe + venda dupla de segredo | Três propriedades de um único ativo (informação): antecipa preço, não se gasta, expira. |
| **21 - Brechas de Contrato Mágico** | As quatro brechas + o caso da traição de longo prazo sob juramento | Já vinham juntas na nota antiga e continuam juntas: uma brecha isolada é anedota, quatro em sequência são uma regra. |
| **23 - Chantagem e Extorsão por Informação** | Chantagem por evidência circunstancial + extorsão existencial | Mesma alavanca em duas potências; a segunda só se entende contra a primeira. |
| **24 - Infiltrar-se numa Organização** | Infiltração de clã + infiltração inter-regional + fraude de linhagem | Todas são a mesma tabela de canais de verificação, preenchida em níveis diferentes. |
| **26 - Um Golpe Mal Testado** | O golpe experimental (V3) + as 21 iterações de desenvolvimento (V5) | O primeiro mostra o fracasso, o segundo mostra o processo correto. Juntos viram um caso completo em vez de dois pela metade. |
| **28 - Todos os Multiplicadores de um Refino** | O refino bem-sucedido + as três falhas sabotadas | O par é o caso: separados, um vira propaganda e o outro vira azar. |
| **30 - O Gu Que Escolhe o Portador** | Trava de autossacrifício + refino por perseverança pura | Mesma categoria de trava, nomeada pela própria obra como paralela. |
| **32 - Tomar um Território pelas Três Vias** | Enganar + suprimir + "invadir e depois pedir" (o caso do V6) | As três vias só fazem sentido comparadas; e a terceira, que **não funciona**, é o que prova que a trava de reconhecimento é independente da de força. |
| **35 - Roubo de um Gu Imortal** | Roubo de dono adormecido (V4) + a cadeia de 4 elos (V5) + o contraste do disfarce de rank | O segundo é o caso completo; o primeiro é a regra-limite ("dono consciente é intocável") que explica por que o segundo precisou ser tão elaborado. |
| **36 - Curar o Dano para Repetir o Dano** | Interrogatório infinito + ciclo industrial de alma | Mesmo padrão em duas escalas: par dano-cura convertendo finito em infinito. |
| **37 - Escolher o Terreno da Tribulação** | Escolha de local (V4) + fabricação do conteúdo (V5) + previsão do conteúdo (V5) | Três camadas de sofisticação do mesmo controle; lidas separadas, a designer não veria a progressão. |
| **39 - Explorar um Reino de Sonho** | Exploração por iteração (V4) + exploração por estágios na escala imortal (V5) | O primeiro dá o método, o segundo dá a escala. A comparação com as 36 falhas da rival é o que torna o método visível. |

## Decisões tomadas

1. **A porta manteve o nome de arquivo `01 - Estudos de Caso Mecânicos`.** Sete notas de
   outras pastas apontam para ele. Renomear teria quebrado links fora da minha pasta.
2. **Numeração aplicada em disco, não deixada para depois.** Renomeei os 38 arquivos para a
   ordem de leitura final e reescrevi os wikilinks. Como as notas novas ainda não estavam
   todas versionadas, usei renomeação simples em vez de `git mv` em parte do lote — o
   histórico se preserva na detecção de rename do próximo commit. **Não rodei `git add` nem
   `git commit`.**
3. **Três arquivos fora da minha pasta foram tocados, e só para consertar links para notas
   minhas que eu havia renomeado:** `08 - Eventos e Cenarios/05 - Feiras, Caravanas e
   Festivais.md`, `08 - Eventos e Cenarios/17 - Caçadas, Emboscadas e Fugas.md`,
   `08 - Eventos e Cenarios/18 - Quando uma Força Morre.md` e
   `03 - Paths/29 - Os Demais Caminhos.md`. Nenhuma frase foi alterada — apenas o número no
   alvo do wikilink. Sem isso, o vault ficaria com links quebrados.
4. **Um título perdeu os dois-pontos.** `Aposta de Rochas: Heurística…` virou
   `Aposta de Rochas - Heurística…`: dois-pontos em nome de arquivo quebra o vault em
   Windows e nenhum outro arquivo do vault usa esse caractere. O texto exibido no índice
   preserva a forma com dois-pontos.
5. **Não escrevi o caso da regressão temporal** (caps. 399-404), apesar de ele estar no
   rascunho e ser mecanicamente riquíssimo. Descrevê-lo exigiria revelar a premissa central
   do enredo, o que a política de spoilers do projeto proíbe. A mecânica em si pertence à
   nota de caminho do tempo, onde pode ser tratada sem o enredo.
6. **Ordenei por curva de aprendizado, não por ordem da obra.** Rank baixo primeiro, escala
   imortal por último, com um aviso `[segredo]` no bloco final da porta. A justificativa está
   no briefing: a campanha começa embaixo, e a designer lê a barra lateral como currículo.
7. **Verifiquei no texto-fonte todos os números que carregam peso** (as 16 unidades de defesa,
   os +20% do catalisador, as 500 pedras do sapo, as 50.000 da flor, os 280.000 lobos, as
   810.000 do leilão, os 12 milhões da guerra de preços, as 36 falhas do reino de sonho, o
   666 km² da calamidade, os 10%/meio dia da escada de custo). **Duas correções resultaram
   disso** — ver a seção seguinte.
8. **Mantive todas as "Regras propostas" da nota antiga**, marcadas como invenção nossa, e
   escrevi uma nova para cada caso novo em que ela não forçava a barra.

## Correções feitas em relação ao rascunho interno

- **Aposta de rochas:** o rascunho diz "~80% de perda". A obra diz **nove em cada dez** pedras
  maciças; os 80% do rascunho são, na verdade, a **confiança** do apostador de que o alvo
  estava entre as seis pedras selecionadas. Duas grandezas diferentes, corrigidas na nota.
- **Escada de custo (golpe → formação):** o rascunho diz "exigiria 1 mês de uso contínuo". O
  texto diz **cerca de meio mês**, com regeneração total em **meio dia** (o rascunho dizia
  12 h, que bate). Corrigido para meio mês.
- **Punhos contra a defesa:** o rascunho fala em "fraturas expostas nas mãos" — confirmado no
  texto de forma ainda mais forte ("os ossos ensanguentados dos dedos podiam ser vistos",
  "ambos os punhos quase inutilizados"), e o tratamento posterior também está registrado.

## O que a obra realmente não diz

Registrado aqui para que ninguém preencha essas lacunas em silêncio numa próxima passagem.

1. **O custo em pedras da ruptura 1 → 2 por atrito.** A obra diz "uma quantidade grande de
   pedras primordiais" e nunca publica o número. A estimativa de "algumas centenas a cerca de
   mil" está marcada com `*` na nota 07 e é **nossa**.
2. **Se a perda de aptidão do ritual demoníaco é de 2 pontos percentuais ou de 2% do valor
   que se tinha.** A obra não desfaz a ambiguidade. O vault adota pontos percentuais e diz
   por quê, marcado como dedução na nota 08.
3. **Por que o limiar do ritual é 38% quando o padrão é 55%.** A obra dá os dois números e a
   expressão "quebra e substitui", mas nunca explica a relação. A leitura é nossa, marcada.
4. **O preço de um "conjunto de materiais de refino" de rank 4-5.** A ordem de grandeza dos
   vinte conjuntos da nota 31 é estimativa nossa, marcada com `*`.
5. **Qual fator determina se um Gu de desfazer sonhos funciona num reino de sonho.** A obra se
   contradiz: a hipótese do tamanho aparece duas vezes e é desmentida numa terceira (funcionou
   no reino de um rank 9, não funcionou no de um rank 8). A nota 39 registra a contradição e
   **não** inventa a explicação.
6. **Se o método de ruptura por atrito funciona acima do rank 2.** A obra só o documenta na
   primeira ruptura, e registra em outro ponto alguém com 90% de reserva que não rompeu a
   barreira 3 → 4 sem ajuda. Isso sustenta a leitura de que o método não escala, mas a obra
   **não afirma** o limite — a nota 07 apresenta isso como leitura, não como regra.
7. **Se alguma organização consegue bancar um Gu de verificação de linhagem de rank 8.** O
   texto só registra o alívio do infiltrado por ter enfrentado um de rank 7. A conclusão de
   que o teto de verificação é **orçamentário** está marcada como dedução na nota 24.
8. **O custo de aquisição da maioria dos artefatos citados nos casos imortais.** A obra
   descreve os efeitos e quase nunca os preços; as notas dizem "—" ou omitem, em vez de
   estimar.

## Verificação final

- `python3 _pipeline/auditar-links.py` → **206 notas, 4.350 links exatos, 0 dependentes de
  alias, 0 quebrados.**
- Todas as 38 notas de caso seguem o modelo (`regra ilustrada → situação → método → por que
  funcionou/falhou → exceção ou regra → para o design`), trazem o cabeçalho de convenção dos
  quatro estados de confiabilidade, e não têm nenhuma citação "(cap. NN)" no corpo — os
  capítulos vivem no `fontes` do frontmatter.
- **Pendência para o orquestrador:** acrescentar a lista da seção "Como a pasta foi
  desdobrada" à entrada `"09 - Estudos de Caso Mecanicos"` de `_pipeline/numerar-notas.py`,
  que hoje ainda registra uma única nota. A numeração em disco já está correta; o script só
  abortará por divergência enquanto a lista dele não for atualizada.
