---
tags:
  - pipeline/auditoria
  - economia
status: em-andamento
---

# Auditoria de completude — `06 - Economia e Vida`

> Auditoria de **completude** da pasta de economia, com correção aplicada. Método: leitura
> das 12 notas finais + `_pipeline/rascunho/economia-e-vida.md` + topo de `LACUNAS.md` +
> seção de economia da tabela soberana, seguida de varredura dirigida ao **texto-fonte**
> (`grep -i` em `/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/`) atrás dos
> assuntos que não haviam chegado às notas finais.
>
> Escopo escrito: todas as notas de `06 - Economia e Vida/` e este relatório.

## Lacunas encontradas

Severidade: **bloqueador** (a designer não consegue fazer o que a pasta promete),
**sério** (falta um assunto inteiro que a obra documenta bem), **menor** (número errado,
imprecisão, oportunidade perdida).

### Bloqueadores

1. **Não havia como montar a planilha de preços que a pasta promete.**
   A nota `02 - Pedras Primordiais` se declara "fonte única de preços do vault" e traz
   **20 linhas de preço**. Uma varredura por `<número> primeval stones` no texto-fonte
   devolve **448 ocorrências**, das quais mais de uma centena são preços de cena
   utilizáveis. A obra dá muito mais do que a pasta registrava: séries completas de preço
   por rank dentro de uma mesma família de Gu, tabela de acesso por anel de cidade,
   spread entre preço de compra e de venda, curva de inflação de um insumo ao longo de uma
   crise, capacidade de Gu de armazenamento, taxas de aluguel por padrão de imóvel.
   Evidência do tamanho do buraco: só o cap. 442 traz a escada
   `jin strength Gu (r1) 220 → strength of ten jin (r2) 690 → jun strength (r3) 4.550 →
   strength of ten jun (r4) 36.000` — a mesma linha de produto em quatro ranks, que é
   exatamente o dado que calibra uma economia de jogo, e ele não estava em lugar nenhum.

2. **Não havia como montar a planilha de renda.** A nota `03` traz 11 linhas de renda,
   todas de *trabalho*. Faltava inteiramente a **renda de patrimônio**, que é a metade
   que decide se um personagem escapa da roda-viva: quanto rende uma nascente espiritual
   (cap. 421: ≥100 milhões de pedras ao longo de 50–60 anos por nascente pequena), quanto
   rende a versão portátil dela (cap. 273: **50 pedras por dia**, número que a pasta nunca
   registrou), qual o prazo de retorno de um negócio comprado (cap. 112: "os stones
   gastos seriam repostos com **dois ou três anos** de operação"), e qual o resultado de
   uma prova de multiplicação de capital (caps. 322–333: 100.000 de capital inicial →
   440.000 em pouco mais de dois meses).

3. **Custo de vida acima do rank 1 estava marcado como inexistente na obra, e não é.**
   As notas `03` e `06` afirmam corretamente que a obra nunca *tabela* o consumo por
   rank, mas deixavam a impressão de que não há nenhuma âncora acima do rank 1. Há uma,
   explícita: cap. 278, um Mestre Gu de rank 3 em cidade-mercado calcula que
   **"420.000 pedras não me durariam nem um ano"** — duas ordens e meia de grandeza acima
   das 3 a 5 pedras/dia do rank 1, na mesma frase em que a obra repete que "quanto maior o
   rank, maiores as despesas".

### Sérios

4. **Impostos, tributos, taxas e pedágios: assunto inteiro ausente.** A obra documenta
   pedágio de entrada de cidade **escalonado por anel** (cap. 259–261), pedágio de estrada
   institucionalizado e negociado (caps. 240–241, os macacos-bandidos de Fei Hou), taxa de
   corretagem de mercado que escala com o valor do item (cap. 1885), taxa de inscrição de
   evento (caps. 829, 1698), taxa de ilha recém-conquistada (cap. 1899) e **mensalidade de
   aliança paga em pontos de recurso** (caps. 2275–2276). Nada disso estava nas notas.

5. **Crédito, dívida, penhor e agiotagem no mundo mortal: ausente.** A pasta cobria com
   cuidado o crédito *imortal* (nota `11`) e mencionava "agiota" numa linha da nota `03`.
   A obra dá o sistema mortal inteiro: agiotas a que um ancião de clã recorre por
   300.000 pedras num dia, **penhor de um Gu** para levantar os 200.000 restantes
   (caps. 295–296), casa de penhores como esconderijo de bem suspeito (cap. 284),
   empréstimo entre membros de clã com recibo assinado (cap. 155), **servidão por dívida
   com prazo** — vinte anos de serviço para quitar (cap. 329) — e a hipoteca de um imóvel
   como forma de levantar dinheiro em vinte e quatro horas (cap. 112).

6. **Contratos e a tecnologia que os faz valer: ausente.** O `poison vow Gu` (voto
   venenoso) é o instrumento contratual do mundo — rank 3, consumível, 4.500 pedras,
   exige ficha de acesso para comprar, bebe o sangue dos dois contratantes e explode em
   sangue estragado se um dos lados leu a cláusula sem a intenção verdadeira. A obra
   explicita que **contrato em papel não basta** ("não confio num acordo de papel, temos
   que jurar", cap. 268) e descreve uma **corrida armamentista contratual** — voto venenoso
   → Gu de comer as próprias palavras (quebra votos) → Gu do papel preto e branco
   (imune ao anterior) → Gu de distorcer preto e branco (cap. 278). Nada disso estava
   na pasta de economia.

7. **Corretagem e intermediação: ausente.** A obra trata o intermediário como instituição
   política, não como conveniência: paga-se *através* de um terceiro para não parecer que
   se pagou ("é o jeito do caminho correto", cap. 1305); há corretora profissional de
   oportunidades em quem tanto demoníacos quanto independentes confiam (cap. 1224); e um
   Venerável exige que um rival sirva de intermediário como prova de sinceridade
   (cap. 2251).

8. **Materiais e cadeia produtiva: assunto inteiro ausente.** Não havia nota nenhuma
   sobre de onde saem as matérias-primas, quem as extrai, quem as compra e quanto valem —
   apesar de a obra publicar o catálogo do mercado imortal item a item (caps. 466, 666:
   "Gu, receitas, golpes, rebanhos, humanos variantes, vegetação, **veios de minério,
   solo, água**, vinho fino"), o deserto de minério gerido por uma super força com
   mineiros escravos (cap. 1474), a divisão étnica do trabalho entre raças variantes
   (cap. 799) e a regra de que **o Gu pertence à região onde foi refinado, não à região de
   onde veio o material** (cap. 469) — que é a regra que decide se vale a pena transportar
   insumo entre regiões.

9. **Mercado negro, contrabando e recompensas por cabeça: cobertura de uma linha.** A obra
   dá o mercado negro mortal de bens desviados (cap. 520), o mercado negro *de revenda*
   dentro do próprio mercado imortal, criado por oferta menor que a demanda (caps. 1199,
   1451), a mecânica completa do mandado de prisão (caps. 234, 259, 271, 293) e — o dado
   que organiza tudo — a **escada canônica de lucro por grau de honestidade** (cap. 243):
   comércio honesto 7 a 8 vezes (declarado como o teto do mundo), métodos ilegais mais de
   10 vezes, fraude aberta dezenas de vezes, assalto "não precisa nem de capital".

10. **A tabela soberana e a nota `02` divergiam do texto no preço de entrada de cidade.**
    Ver a seção de divergências.

### Menores

11. Nota `02` dizia "entrada numa cidade grande: 1 a 10 pedras por pessoa". A faixa real
    documentada vai de **1 a 600** por pessoa, escalonada por anel.
12. A pasta nunca registrou o **spread entre preço de compra e de venda**, embora ele
    esteja em cena: uma loja compra um Gu de rank 1 por ~250 e o mercado o revende por
    ~500 (caps. 262 e 278). Sem isso a designer lê os dois números como contradição.
13. A pasta menciona "fichas destravam compras" sem nunca dizer que elas **também dão
    desconto quantificado**: a ficha de topo cortou 1.500 de um item de 4.500, um terço do
    preço (cap. 272).
14. A capacidade dos Gu de armazenamento de dinheiro nunca aparece, embora seja o que
    define quanto um personagem consegue carregar: 30.000 pedras num Gu de rank 3 comum,
    **1.000.000** no Gu de armazenamento especializado, que custa 6.600 em leilão
    (caps. 161, 268, 422).
15. Nenhuma nota registrava que **noventa por cento das transações do mercado imortal são
    escambo puro** (cap. 2245), o que muda a leitura de toda a nota `11`.
16. A nota `03` descreve caravanas sem dizer **quem protege a estrada** e a que preço.

## O que foi corrigido

*(preenchido arquivo por arquivo abaixo, à medida que as correções foram aplicadas)*

## Notas novas criadas

*(abaixo)*

## Decisões tomadas

*(abaixo)*

## Divergências com a tabela soberana

*(abaixo)*

## O que a obra realmente não diz

*(abaixo)*
