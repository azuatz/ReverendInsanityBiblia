# Enxugamento — `10 - Estudos de Caso Mecanicos`, nota-índice + casos 02 a 25

Escopo deste relatório: a nota-índice `01` e os casos `02`–`25`. Os casos `26`–`49` foram
enxugados por outro agente em paralelo; este relatório só os toca onde a tabela do índice
precisou acompanhar as fusões feitas lá.

Queixa que originou o trabalho: *"tem coisas que está muito difícil de ler e entender… melhor
tirar, ou só botar as partes mais importantes"*. Diagnóstico para esta pasta: o problema não era
o tamanho de cada caso, era **quantidade e triagem** — 49 notas com títulos parecidos e um índice
de 293 linhas que explicava muito antes de servir.

---

## 1. Números

### A nota-índice

| | Antes | Depois |
|---|---|---|
| Linhas | 293 | 218 |
| Palavras | 4.908 | 3.695 (**−24%**) |

### Os casos

| Nota | Palavras antes | Depois | Δ |
|---|---|---|---|
| 02 · Punhos Contra uma Camada de Defesa | 963 | 844 | −12% |
| 03 · O Sapo de Rank 5 | 1.174 | 978 | −16% |
| 04 · Um Gu Implantado no Corpo | 923 | 810 | −12% |
| 05 · O Catalisador Fora da Receita | 1.070 | 966 | −9% |
| 06 · Um Gu Acima do Próprio Rank | 982 | 889 | −9% |
| 07 · Romper o Rank 2 por Teimosia e Pedras | 1.248 | 1.133 | −9% |
| 08 · O Atalho Demoníaco de Rank | 1.086 | 953 | −12% |
| **09+10 → 09 · Os Dois Atalhos que se Anularam** | **2.752** | **2.034** | **−26%** |
| 11 · Caçar o Que Não se Vê | 1.170 | 1.067 | −8% |
| 12 · Roubar o Gu de um Moribundo | 816 | 711 | −12% |
| 13 · Fugir de um Enxame e Sair Montado | 1.669 | 1.337 | −19% |
| 14 · O Refém que Cura os Dois Lados | 1.300 | 1.109 | −14% |
| 15 · A Barreira Que Deixa Sair | 975 | 859 | −11% |
| 16 · O Ambiente Manda Mais que o Rank | 1.055 | 961 | −8% |
| 17 · Sobrecarregar o Defensor | 1.555 | 1.369 | −11% |
| 18 · Emboscada de Um Contra Sete | 1.019 | 901 | −11% |
| 19 · Perder de Propósito e Cobrar Caro | 1.404 | 1.224 | −12% |
| 20 · Guerra de Custos | 1.078 | 1.000 | −7% |
| 21 · Um Trunfo que Nunca Foi Testado | 1.621 | 1.378 | −14% |
| 22 · Aposta de Rochas | 935 | 848 | −9% |
| 23 · Ganhar um Leilão | 1.108 | 977 | −11% |
| 24 · Colher a Flor Antes do Prazo | 883 | 803 | −9% |
| 25 · Comprar Antes que Seja Notícia | 883 | 858 | −2% |
| **TOTAL (índice + casos)** | **32.577** | **27.704** | **−14%** |

**Por que os casos ficaram em −11% de média e não em −25%.** A meta de um quarto foi atingida no
índice (−24%) e na fusão (−26%), mas não caso a caso, e a razão é o que a instrução mandava
proteger. Cada nota é feita de quatro blocos intocáveis — o número canônico, o veredito
"exceção × regra", o callout `Regra proposta` e o `Para o design` — que juntos já são metade do
texto. O que sobra para cortar é a prosa de ligação, e ela foi cortada até o ponto em que o
parágrafo seguinte deixaria de fazer sentido para uma leitora que não conhece a obra. Preferi
parar aí a comprimir escrevendo telegrama para leiga.

---

## 2. O que foi cortado, por categoria

**a) Boilerplate vazio (a maior economia isolada).** Todas as 24 notas abriam com o mesmo bloco de
três linhas explicando os marcadores de confiabilidade. Verifiquei quais notas realmente **usam**
`(ded.)`, `*` ou `—` no corpo: **catorze não usam nenhum**. Nessas, o bloco era exatamente o que a
instrução chama de "seção que só existe porque o modelo previa e ali está vazia de conteúdo", e
foi removido — a convenção continua declarada, para a pasta inteira, no callout do índice, como
manda o `CLAUDE.md` ("toda nota que **use** esses marcadores explica a convenção"). Nas dez notas
que usam marcadores, o bloco foi comprimido de três linhas para duas e movido para **depois** da
frase-regra.

Notas sem marcadores, com o bloco removido: 02, 03, 04, 11, 12, 13, 15, 16, 18, 20, 22, 23, 24, 25.

**b) A regra em uma frase, antes de tudo.** As 24 notas abriam com o boilerplate e só então com a
regra, sob o título "**A regra que este caso ilustra:**". Agora todas abrem com **A regra:** em
negrito, na primeira linha depois do título, com o `==destaque==` no termo-chave. Quem parar ali
levou o que interessa.

**c) Ordem canônica situação → método → veredito.** Corrigida onde estava embaralhada. O caso mais
afetado foi o **06**, que abria pela "versão passiva" (exceção rara) e só depois dava a "versão
ativa" (regra cotidiana, e a útil para a mesa); as duas trocaram de lugar.

**d) Prosa que repetia outra seção.** Exemplos: em **13**, três parágrafos de "Por que funcionou"
viraram três bullets sem perder nenhuma afirmação; em **19**, três citações longas do balanço
final viraram uma; em **17**, a fala do defensor aparecia duas vezes; em **21**, a admissão do
autor do blefe repetia o que o veredito já dizia.

**e) Ornamento.** Frases de moldura ("este trecho é o mais próximo de…", "vale a pena guardar
inteiro", "e a frase merece ser lida devagar") e comentários pendurados depois do callout
`Regra proposta`.

**f) Explicação alongada de ambiguidade.** Os callouts que discutem "pontos percentuais × por
cento" (**05** e **08**) e o custo estimado em pedras (**07**) mantêm integralmente a conclusão, a
marcação `(ded.)`/`*` e os números; perderam só a repetição do argumento.

**g) Listas de `Relações` acima de cinco itens**, aparadas em 13, 14, 17, 19 e 21 — sempre
descartando o link mais distante do assunto da nota.

---

## 3. Fusão feita

### `09 · Comprar um Estágio de Cultivo com Todo o Futuro` + `10 · Comprar Aptidão com Cem Vidas` → **`09 · Os Dois Atalhos que se Anularam`**

**Por quê.** Não eram dois casos: era **um só evento**, narrado duas vezes. Os dois Gu foram usados
pela mesma pessoa, no intervalo de dias, nos mesmos capítulos 197–198 — e o desfecho (o Gu de rank
4 sobrescrever o de rank 3 e derrubar o cultivo de rank 3 para rank 1 inicial) aparecia **inteiro
e quase palavra por palavra nas duas notas**: em `09` como "O epílogo: o atalho sendo desfeito", em
`10` como "O preço escondido: o cultivo desmoronou". Uma leitora que não conhece a obra lê as duas
e fica sem saber se o cultivo desabou uma vez ou duas.

**O que a fusão ganha.** A colisão passa a ser o ponto da nota, e não uma repetição: os dois
atalhos são apresentados lado a lado (liquidar o potencial da abertura; comprar aptidão com sangue
de linhagem) e a regra que os une — **quando dois efeitos disputam a mesma estatística, vence o de
rank mais alto, nunca o aplicado primeiro** — sai como conclusão, com as duas metades do exemplo à
vista. É a regra nº 7 das "Regras do mundo" da pasta, e agora tem um caso que a demonstra inteira.

**Nada de canônico se perdeu.** Continuam na nota fundida: o pó cinzento e as paredes "várias vezes
mais grossas"; a subida de essência de prata clara para prata de neve; a frase "será muito difícil
pisar no rank 4"; o uso agressivo do Gu contra terceiros e a imunidade dos Dez Extremos; o crânio
de cristal de rank 4; as cem pessoas por carga; os mais de dez ciclos em seis horas; a escada
44% → 43% → 53% → 63% → acima de 90%; a escala de graus 40–59 C / 60–79 B / 80+ A; os duzentos anos
de comparação; o rendimento decrescente; e as duas `Regra proposta`, mantidas como duas.

**Aliases.** A nota nova carrega os dois títulos antigos e os quatro apelidos (`Stone Aperture Gu`,
`Blood Skull Gu`, `Abertura de pedra`, `Crânio de Sangue`), então busca por qualquer um deles
continua achando a nota.

### Número liberado

- **`10`** — livre. É o único número que este agente liberou.
- Para conhecimento do orquestrador, o agente dos casos 26–49 liberou em paralelo o **`40`**
  (fundido em `39 - O Espírito Guardião de um Território`) e o **`48`** (fundido em
  `47 - A Tribulação Como Matéria-Prima`). A pasta ficou com **44 casos** e três buracos de
  numeração: 10, 40, 48.
- `_pipeline/numerar-notas.py` vai abortar até que a ordem de leitura dele seja atualizada com os
  três títulos novos e sem os três antigos.

### Fusões avaliadas e recusadas

- **07 + 08** (romper por atrito × atalho demoníaco). São as duas saídas para aptidão baixa e se
  citam mutuamente, mas cada uma carrega um conjunto próprio de números (55%/44%/13% de um lado;
  38% e −2 pontos do outro) e o **07** é o caso que sustenta a economia inteira do cenário. Fundir
  produziria uma nota gigante e diluiria justamente o argumento mais importante da pasta. O
  panorama das duas já existe em `09 - Avançar com Aptidão Baixa`, fora desta pasta.
- **02 + 17** (quebrar defesa por capacidade × por atenção). Tentador, porque são os dois jeitos de
  vencer uma defesa e já se cruzam. Recusada porque o **17** não é sobre defesas: é a nota que
  estabelece o **teto de atenção igual a três**, uma das nove regras do mundo da pasta, e fundi-la
  num caso de rank 1 enterraria essa regra. Em vez da fusão, cruzei as duas notas explicitamente
  nas `Relações` de ambas.
- **23 + 25** (leilões × informação como ativo). Vizinhas de assunto, mas ensinam coisas
  diferentes: uma é negociação, a outra é precificação de segredo. Manter separadas custa pouco e
  a tabela de triagem já resolve a escolha entre elas.

---

## 4. A nota-índice, reconstruída

Estrutura antiga: prosa de abertura longa → "Como usar esta pasta" (três parágrafos) → advertência
de calibragem → dois callouts de convenção → nove regras do mundo com 2–3 linhas cada → **índice
comentado em seis tabelas temáticas** → conhecimento de jogador/mestre em dois parágrafos corridos
→ **segunda tabela com o veredito de cada caso** → relações. Ou seja: dois índices, um deles
redundante, e a informação de triagem no fim.

Estrutura nova, na ordem:

1. Uma frase do que a pasta é, e a instrução de uso em duas linhas.
2. **Os dez essenciais** — tabela de dez linhas, cada uma dizendo por que aquele caso está na lista.
3. **Aviso de calibragem** comprimido num callout (os seis casos que terminam em fracasso: 09, 15,
   19, 34, 44, 45).
4. **A tabela de triagem** — uma linha por caso, quatro colunas: *caso · a regra que ilustra ·
   patamar · exceção × regra*. Substitui os dois índices antigos de uma vez.
5. **Como usar isto em mesa** — os três usos, em um parágrafo.
6. **Regras do mundo** — as nove, uma linha cada (eram 2–3 linhas cada).
7. **O que todo personagem sabe** / **O que só o mestre sabe** — o mesmo conteúdo, convertido de
   dois parágrafos corridos (que eram, provavelmente, o trecho mais ilegível da pasta) em listas.
8. **Convenções e vocabulário mínimo** — o callout das duas convenções mais a tabela dos cinco
   termos, movida para o fim: é consulta, não leitura.

**A coluna "patamar"** é nova e resolve a triagem por nível de campanha: `baixo` (ranks 1–3),
`médio` (4–5), `imortal` (6+) e `qualquer` (independe de rank). O cabeçalho da tabela declara a
convenção. Ela substitui o agrupamento temático antigo, que obrigava a designer a ler seis tabelas
para saber se um caso servia ao grupo dela.

### Os dez essenciais — o recorte e o motivo de cada escolha

Critério: ensinar mais por linha lida, e cobrir cultivo, refino, uso de Gu, combate, economia e
vida social sem deixar buraco.

| # | Caso | Domínio | Por que entrou |
|---|---|---|---|
| 1 | 03 · O Sapo de Rank 5 | mundo / bestas | A melhor aventura pronta da pasta e a única que ensina a categoria mais reutilizável do cenário: bestas têm **lista de gatilhos**, não ficha de combate. Um grupo de rank 1 resolve um problema de rank 5. |
| 2 | 06 · Um Gu Acima do Próprio Rank | uso de Gu | A técnica mais **cotidiana** do mundo (a aura emprestada de um mentor) e o princípio que governa todo o sistema: ele arbitra estados reais, não rótulos. |
| 3 | 07 · Romper o Rank 2 por Teimosia e Pedras | cultivo | O caso que define a economia inteira: aptidão é **teto duro no topo e imposto embaixo**. Sem ele a designer não sabe precificar progresso. |
| 4 | 09 · Os Dois Atalhos que se Anularam | cultivo | Os atalhos mais caros do sistema **mais** a regra de colisão por rank, que reaparece em toda a pasta. Dois pelo preço de um. |
| 5 | 17 · Sobrecarregar o Defensor | combate | O teto de atenção igual a três e a assimetria manter/alterar. É a única trava do sistema contra empilhar defesas. |
| 6 | 20 · Guerra de Custos | combate / economia | Custo por ação em vez de dano, provado em duas escalas — e é a lógica que sustenta um caminho de cultivo inteiro. |
| 7 | 36 · Todos os Multiplicadores de um Refino | refino | A pilha completa de multiplicadores, com um sucesso e três fracassos sabotados lado a lado. Nenhum preparo compra certeza. |
| 8 | 25 · Comprar Antes que Seja Notícia | economia | As três propriedades da informação como ativo. É a regra do mundo nº 2 em forma jogável. |
| 9 | 29 · Brechas de Contrato Mágico | social / palavra | A regra do mundo nº 3, "a letra vence a intenção", com quatro brechas reais. Vale para juramentos, selos e proteções. |
| 10 | 30 · Reputação Comprada em Prestações | social | Não há polícia neste mundo; há reputação, e ela tem preço de tabela. É o que decide toda negociação de mesa. |

Ficaram **de fora, deliberadamente**, casos fortes que a tabela cobre: 05 (receita é versão) e 21
(sinais de força são fabricáveis) perderam a vaga para 36 e 25 por serem mais estreitos; os seis
fracassos têm callout próprio logo acima, porque servem a outra função (calibragem) e não a de
esqueleto.

---

## 5. Fatos canônicos movidos, não perdidos

Nenhum número, nome, citação ou marcação de confiabilidade saiu do vault. Onde um parágrafo foi
cortado, o fato mudou de lugar:

| Fato | De | Para |
|---|---|---|
| Epílogo do colapso de cultivo (rank 3 → 2 → 1 inicial; "o Gu de rank 4 governava sobre o Gu de rank 3") | duplicado em `09` e `10` | seção única "A colisão" em `09 - Os Dois Atalhos que se Anularam` |
| Escala de graus de aptidão (40–59 C / 60–79 B / 80+ A) e os duzentos anos de comparação | `10` | callout próprio em `09` |
| Uso agressivo do Gu de abertura de pedra contra terceiros + imunidade dos Dez Extremos | `09`, em parágrafo longo | `09`, comprimido, sem perda de conteúdo |
| Escavação manual a meio metro por várias horas | parágrafo de custo de `13` | mesma frase de custo, condensada |
| Definição de essência primordial para leiga | parágrafo solto no topo de `19` | parêntese no passo 1 do método, com wikilink |
| Convenção dos marcadores de confiabilidade | repetida em 24 cabeçalhos | callout "As duas convenções da pasta" no índice + cabeçalho reduzido nas dez notas que usam marcadores |
| Contradição dos "dois disparos com 11%" | nota de rodapé de `11` | intacta, a nota de rodapé foi preservada inteira |

---

## 6. Links e integridade

- `python3 _pipeline/auditar-links.py`: **5.360 links por nome exato, 0 quebrados, 264 âncoras de
  seção, 0 âncoras quebradas.**
- Todo wikilink dentro de tabela usa pipe escapado (`[[Nota\|texto]]`).
- Referências às duas notas fundidas foram reescritas em: `00 - Somente o Mestre.md` (raiz),
  `13`, `14` e o próprio índice. A menção do `00 - Somente o Mestre` à seção "Heranças,
  territórios e escala imortal" — seção que o índice novo não tem mais — foi trocada por uma
  referência ao patamar **imortal** da tabela de triagem.
- A tabela de triagem foi conferida contra o disco: os 44 casos existentes estão todos nela, e
  ela não aponta para nenhum arquivo inexistente. Como o agente dos casos 26–49 trabalhou em
  paralelo, as linhas 39 e 47 foram atualizadas depois das fusões dele.
- Nenhum `git add` ou `git commit` foi executado.
