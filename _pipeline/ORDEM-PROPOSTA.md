# Ordem de leitura proposta — para substituir o dicionário `ORDEM` de `_pipeline/numerar-notas.py`

Montada em 2026-09-02, depois de o vault saltar de 98 para 216 notas. O dicionário do
script conhecia 8 pastas e 79 notas; esta proposta cobre as **11 pastas numeradas e as
212 notas** que existem hoje dentro delas (as outras 4 notas do vault estão na raiz e
fora do escopo do script).

Fontes das posições: as recomendações que cada agente registrou no fim do seu relatório
em `_pipeline/` (`AUDITORIA-*`, `PLANO-eventos.md`, `pesquisa/*`). Onde duas recomendações
se chocaram, ou onde não havia nenhuma, a decisão está registrada na última seção, com a
alternativa descartada.

**Como aplicar:** substituir o bloco `ORDEM = { ... }` de `_pipeline/numerar-notas.py`
pelo bloco abaixo, rodar `python3 _pipeline/numerar-notas.py --dry` da raiz do vault
(deve reportar **135 renomeios e nenhum problema de plano**), depois rodar sem `--dry` e
fechar com `python3 _pipeline/auditar-links.py`.

---

## O bloco pronto para colar

```python
ORDEM = {
    "01 - Cultivo": [
        "Visão Geral do Cultivo", "Abertura", "Aptidão", "Essência Primordial",
        "Ranks e Avanço", "O Corpo e a Mente do Mestre Gu", "Perder Cultivo",
        "Attainment", "Avançar com Aptidão Baixa", "As Dez Constituições Extremas",
        "Cultivo Fora do Humano", "Longevidade", "Tribulações e Calamidades",
        "Ascensão Imortal", "Essência Imortal", "Dao Marks",
        "Zumbis e Corpos Transformados", "Modificar o Próprio Corpo",
        "Tornar-se Venerável",
    ],
    "02 - Gu": [
        "Visão Geral dos Gu", "O que é um Gu", "Usar e Alimentar Gu",
        "Onde um Gu Mora", "Gu Vital", "Refino de Gu", "Fusão de Gu",
        "Killer Moves", "Formações de Gu", "Como Funciona um Combate",
        "Ferimento, Cura e Fuga", "A Morte dos Gu", "Qualidade e Fraude",
        "Espólio de Gu", "Conflito de Marcas e Compatibilidade", "Gu Imortais",
    ],
    "03 - Paths": [
        "Visão Geral dos Paths", "Como se Escolhe um Caminho",
        "Blood Path", "Strength Path", "Qi Path", "Transformation Path",
        "Enslavement Path", "Refinement Path", "Formation Path", "Poison Path",
        "Sword Path", "Soul Path", "Sound Path", "Space Path", "Theft Path",
        "Wisdom Path", "Information Path", "Time Path", "Star Path", "Food Path",
        "Rule Path", "Phantom Path", "Luck Path", "Human Path", "Heaven Path",
        "Dream Path", "Os Caminhos Elementais", "Painting Path",
        "Os Demais Caminhos",
    ],
    "04 - Mundo": [
        "Visão Geral do Mundo", "A Filosofia do Mundo", "As Duas Eras de um Mestre Gu",
        "As Cinco Regiões", "Atlas das Cinco Regiões", "O Subsolo",
        "O Relógio do Mundo", "Escala, Distâncias e Viagem",
        "As Plantas e os Bichos Comuns", "Bestas Gu e Reis Fera",
        "O Selvagem, as Ruínas e as Zonas Proibidas", "Lendas de Ren Zu",
        "Blessed Lands e Grotto-Heavens", "Viver Dentro da Abertura Imortal",
        "Vontade dos Céus", "Fate Gu", "Cosmologia",
        "Lugares Fora das Cinco Regiões", "Tribunal Celestial",
    ],
    "05 - Sociedade": [
        "Visão Geral da Sociedade", "Clãs", "Seitas e Academias",
        "Família, Ancestrais e Ritos", "Tipos de Gente e Filosofias de Vida",
        "Caminho Correto e Caminho Demoníaco", "Lei, Crime e Castigo",
        "Juramentos, Reputação e Favores", "Informação, Rumores e Espionagem",
        "Guerra Organizada", "Cultura das Cinco Regiões",
        "Povos e Variantes Humanas", "As Grandes Forças do Mundo",
        "Tribunal Celestial e Grandes Forças", "Sociedade Fora das Cinco Regiões",
    ],
    "06 - Economia e Vida": [
        "Visão Geral da Economia", "Pedras Primordiais",
        "Preços, Renda e Custo de Vida", "Como um Mestre Gu Ganha a Vida",
        "Materiais e Cadeia Produtiva", "Mercados e Leilões",
        "Crédito, Contratos e Tributos", "Crime, Mercado Negro e Recompensas",
        "Aposta de Rochas", "Vida Cotidiana", "Ritmo de Cultivo e Reclusão",
        "Heranças e Provações", "Eventos e Instituições Jogáveis",
        "Convenção do Caminho de Refino", "Economia Imortal",
        "Produzir Gu Dentro da Abertura",
    ],
    "07 - Veneraveis e Legados": [
        "Visão Geral dos Veneráveis", "Os Criadores de Caminhos",
        "Os Arquitetos da Ordem", "Os Que Romperam as Leis",
    ],
    "08 - Eventos e Cenarios": [
        "Visão Geral dos Eventos", "A Maré de Lobos de Qing Mao Shan",
        "Marés de Bestas", "Desastres Locais e Problemas Crônicos",
        "Feiras, Caravanas e Festivais", "Assembleias, Alianças e Quadros de Mérito",
        "Torneios, Arenas e Duelos", "Aberturas de Herança",
        "A Herança dos Três Reis", "A Subida da Montanha Dang Hun",
        "Os Cacos do Céu Estrelado", "As Terras Ferozes e o Subsolo do Mundo",
        "O Paraíso da Baleia-Dragão e o Obelisco de Mérito",
        "O Ciclo Decenal das Planícies do Norte",
        "O Edifício dos Oitenta e Oito Andares", "A Montanha Yi Tian",
        "Caçadas, Emboscadas e Fugas", "Quando uma Força Morre",
        "Cercos e Invasões de Terras Abençoadas",
        "O Cerco da Montanha Nevada e o Rio de Fluxo Reverso",
        "Calamidades e Tribulações como Cenário",
        "Leilões, Cúpulas e Guerras de Mercado",
        "A Cerimônia das Miríades de Tribos e a Estrada da Vida",
        "A Grande Era e as Marés de Qi", "A Guerra do Destino",
        "A Caverna do Demônio Enlouquecido", "A Morte do Sol e o Céu Espectral",
        "O Mundo em Véspera de Guerra", "Eventos Históricos de Fundo",
    ],
    "09 - Estudos de Caso Mecanicos": [
        "Estudos de Caso Mecânicos",
        "Punhos Contra uma Camada de Defesa",
        "O Sapo de Rank 5 Que Ninguém Podia Tocar",
        "Um Gu Implantado no Corpo",
        "O Catalisador Fora da Receita",
        "Um Gu Acima do Próprio Rank",
        "Romper o Rank 2 por Teimosia e Pedras",
        "O Atalho Demoníaco de Rank",
        "Comprar um Estágio de Cultivo com Todo o Futuro",
        "Comprar Aptidão com Cem Vidas",
        "Caçar o Que Não se Vê",
        "Roubar o Gu de um Moribundo",
        "Fugir de um Enxame e Sair Montado",
        "O Refém que Cura os Dois Lados",
        "A Barreira Que Deixa Sair e Não Deixa Entrar",
        "O Ambiente Manda Mais que o Rank",
        "Sobrecarregar o Defensor que Devolve o Golpe",
        "Emboscada de Um Contra Sete",
        "Perder de Propósito e Cobrar Caro",
        "Guerra de Custos",
        "Um Trunfo que Nunca Foi Testado",
        "Aposta de Rochas - Heurística, Perda e Álibi",
        "Ganhar um Leilão Sem Ser o Maior Lance",
        "Colher a Flor Antes do Prazo",
        "Comprar Antes que Seja Notícia",
        "Dar de Graça o que Vai Vazar",
        "A Conta de uma Calamidade",
        "Guerra de Preços",
        "Brechas de Contrato Mágico",
        "Reputação Comprada em Prestações",
        "Chantagem e Extorsão por Informação",
        "Infiltrar-se numa Organização",
        "Uma Receita Lendária Cumprida com Substitutos",
        "Um Golpe Mal Testado Usado Além do Limite",
        "Do Golpe à Formação",
        "Todos os Multiplicadores de um Refino",
        "A Linha de Produção de Gu",
        "O Gu Que Escolhe o Portador",
        "As Três Chances de um Espírito Guardião",
        "Tomar um Território pelas Três Vias",
        "Um Mortal Refina um Gu Imortal",
        "Anexação de Aberturas",
        "Roubo de um Gu Imortal de Rank Superior",
        "A Armadilha que Engorda a Cada Teste",
        "Quando a Adivinhação Falha",
        "Curar o Dano para Repetir o Dano",
        "Escolher o Terreno da Própria Tribulação",
        "Fazenda de Tribulações",
        "Explorar um Reino de Sonho",
    ],
    "10 - Apendices": [
        "Glossário EN-PT", "Tabelas de Referência Rápida", "Catálogo de Gu",
        "Catálogo de Gu - Mortais", "Catálogo de Gu - Imortais",
        "Catálogo de Receitas", "Catálogo de Golpes - Mortais",
        "Catálogo de Golpes - Imortais", "Catálogo de Bestas e Reis Fera",
        "Linha do Tempo e Eras",
    ],
    "11 - Forcas e Organizacoes": [
        "Visão Geral das Forças e Organizações", "Fronteira Sul",
        "Planícies do Norte", "Continente Central", "Deserto Ocidental",
        "Mar Oriental",
    ],
}
```

---

## A lógica de cada pasta

### 01 - Cultivo (19)

O currículo vai do **que é cultivar** ao **topo do mundo**, e cada nota só usa termos já
definidos. Primeiro o motor (abertura, aptidão, essência, ranks); em seguida o par novo
"o que subir de rank faz com a pessoa" e "o que acontece quando se desce" — porque a nota
de ranks levanta essas duas perguntas e não as responde. Depois o bloco dos **corpos que
não são o corpo padrão** (attainment e aptidão baixa como saídas para o talento fraco, as
dez constituições, o cultivo não-humano). Só então o bloco imortal: o relógio da vida
(longevidade), o preço (tribulações), a passagem (ascensão), o combustível novo que a
passagem cria (essência imortal), o que o cultivo imortal de fato acumula (dao marks). O
fim da pasta são as duas saídas do sistema: **desistir de crescer** (zumbis, e o apêndice
da modificação corporal) e **chegar ao topo** (Venerável), nessa ordem, para a pasta
fechar no clímax.

### 02 - Gu (16)

Lê-se como a vida de um bicho e depois a economia dele. Primeiro o que é, como se usa e
alimenta, e **onde ele mora** — informação de base que três notas posteriores pressupõem.
Depois o vínculo (Gu Vital) e a produção (refino, fusão). Em seguida a combinação para o
conflito (killer moves, formações) e o conflito propriamente dito (como se luta, o que
sobra da luta). A pasta fecha na **economia do patrimônio**: as três maneiras de perder um
Gu — ele morre, foi comprado errado, foi tomado — mais compatibilidade e o degrau imortal.

### 03 - Paths (29)

Porta de entrada (visão geral, como se escolhe) e depois os 27 caminhos em quatro blocos:
os **de corpo e combate** (sangue, força, qi, transformação, escravização, refino,
formação, veneno, espada), os **de mente e alma** (alma, som, espaço, roubo, sabedoria,
informação), os **fundamentais e abstratos** (tempo, estrela, comida, regra, fantasma,
sorte, humano, céu, sonho) e as **duas notas coletivas** como apêndice temático, com o
caminho da pintura entre elas por ser criação do mesmo Venerável dos elementais. Cada
ramo fica colado à sua mãe: qi depois de força (o que reinou e o que o substituiu),
formação depois de refino, som depois de alma, roubo depois de espaço (a defesa canônica
contra ele), informação depois de sabedoria (a obra os chama de "os mais compatíveis"),
fantasma depois de regra, e **humano imediatamente antes de céu** — o caminho humano só se
entende lido contra o do céu.

### 04 - Mundo (19)

Do abstrato ao concreto e de dentro para fora. Filosofia e as duas eras primeiro, porque
enquadram tudo; depois o mapa (as cinco regiões, o atlas), e logo em seguida as duas notas
que viram o mapa de outros ângulos: **o subsolo** (o mapa de cabeça para baixo) e **o
relógio do mundo** (quando, com que calendário e que clima). Só então a viagem, e a
natureza em dois degraus — a metade não-mágica antes da metade mágica, e as ruínas e zonas
proibidas fechando o movimento "o que existe fora dos muros". O último terço é o material
de mestre: mito, terras abençoadas, viver dentro da abertura, e o bloco cosmológico
(Vontade dos Céus, Fate Gu, cosmologia, o que há fora das cinco regiões, Tribunal
Celestial).

### 05 - Sociedade (15)

Primeiro as **instituições** (clã, seita, família), depois **as pessoas** (tipos de gente,
o eixo correto × demoníaco). Em seguida o bloco transversal do **que segura a sociedade de
pé**, na ordem em que cada camada falha: a lei, a palavra dada quando a lei não obriga, a
informação que faz a reputação circular, e a guerra quando as três falham. Por fim a
**escala grande**: cultura regional, os povos variantes que existem em todas as regiões,
as grandes forças, o Tribunal Celestial e o mundo fora das cinco regiões.

### 06 - Economia e Vida (16)

Segue o dinheiro. A moeda (pedras primordiais), o que as coisas custam, como se ganha,
de onde vem a matéria-prima, onde se troca, o crédito que sustenta a troca e o crime que
vive na borda dela, com a aposta de rochas fechando o bloco de mercado. Depois o
**cotidiano** (vida diária, ritmo de reclusão, heranças, instituições jogáveis, a
convenção de refino) e, no fim, a **camada imortal** da economia, que é outro sistema com
outra moeda.

### 07 - Veneraveis e Legados (4)

Inalterada: a porta e os três agrupamentos por tipo de feito — quem criou caminhos, quem
construiu a ordem do mundo, quem a quebrou.

### 08 - Eventos e Cenarios (29)

Ordem já planejada em `_pipeline/PLANO-eventos.md` e igual à do disco: **escala + faixa de
rank**. Abre com o que uma mesa iniciante de rank 1 joga na primeira sessão (a maré de
lobos, os desastres locais, as feiras) e fecha com o que muda o mundo inteiro (a Grande
Era, a guerra do destino, a véspera de guerra), com a nota de eventos históricos de fundo
como apêndice de contexto.

### 09 - Estudos de Caso Mecanicos (49)

Ordem transcrita literalmente do bloco Python de `_pipeline/AUDITORIA-estudos-de-caso.md`,
que é a autoridade da pasta. Seis blocos: rank baixo (onde a campanha começa), combate e
estrutura, dinheiro e mercado, palavra e organizações, criar/refinar/produzir e, por fim,
a escala imortal marcada como segredo de mestre.

### 10 - Apendices (10)

Consulta, não leitura corrida. Primeiro as duas ferramentas de tradução e de mesa
(glossário, tabelas), depois os **cinco catálogos de coisas** agrupados (Gu, receitas,
golpes, bestas) e, fechando, a linha do tempo — que é um apêndice de outra natureza e
serve melhor como pano de fundo histórico no fim.

### 11 - Forcas e Organizacoes (6)

A nota-porta assume a posição `01`, como manda a convenção do vault (hoje ela está em
`06`, por ter sido escrita depois das cinco fichas). As cinco regiões seguem na ordem que
o resto do vault já usa — Sul, Norte, Central, Oeste, Leste — e é essa mesma ordem da
tabela "Mapa da pasta" dentro da nota-porta. A recomendação didática de começar pela
Fronteira Sul e ir daí para o Continente Central continua entregue **em prosa**, dentro da
nota-porta, que é onde ela não custa consistência.

> **Observação de nome de pasta.** Se `11 - Forcas e Organizacoes` for movida para a
> posição `06` do vault (o lugar dela na leitura é logo depois de Sociedade), empurrando
> Economia, Veneráveis, Eventos, Estudos de Caso e Apêndices um número adiante, muda
> apenas a **chave** deste dicionário — a ordem interna acima continua valendo intacta.
> Nesse caso, renomear a chave e as das cinco pastas deslocadas antes de rodar o script.

---

## Decisões que tomei, e conflitos entre agentes

**1. `02 - Gu`: "Onde um Gu Mora" na 4ª posição, e não no bloco final.** Conflito real
entre dois relatórios. `AUDITORIA-gu.md` pede a 4ª posição (três notas posteriores passaram
a apontar para ela, e a leitora precisa saber onde os bichos ficam antes de ler sobre
vínculo, morte e espólio); `AUDITORIA-combate.md`, ao propor sua própria ordem, descreve o
bloco final da pasta como "morte, espólio, compatibilidade, imortais, **onde moram**,
qualidade". Fiquei com a 4ª: o argumento de dependência é explícito e verificável, o do
combate era apenas descritivo do estado do disco na hora. *Alternativa descartada:* deixar
a nota junto do bloco de patrimônio, o que agruparia melhor por tema e pior por
pré-requisito.

**2. `02 - Gu`: as duas notas de combate entram na 10ª e 11ª, e o bloco de patrimônio
desce.** É o que `AUDITORIA-combate.md` recomenda, e casa com a inserção acima:
killer moves e formações são pré-requisito das notas de combate, e as notas de combate são
pré-requisito de "A Morte dos Gu" e "Espólio de Gu", que falam do que sobra de uma luta.
*Alternativa descartada:* a saída conservadora que o próprio relatório oferece — deixar as
duas em 15/16 e registrar a ordem ideal só na nota-porta. Descartada porque a regra do
vault é que a barra lateral **é** o currículo.

**3. `01 - Cultivo`: "Zumbis e Corpos Transformados" fica em 17, não em 16.** A instrução
recebida dizia "posição 16, entre Dao Marks e Tornar-se Venerável"; a inserção de
"Essência Imortal" logo depois de "Ascensão Imortal" (a outra decisão já fechada) empurra
tudo um número. **A restrição que importa — estar entre Dao Marks e Tornar-se Venerável —
está respeitada**; só o número absoluto mudou, e ele é consequência da outra decisão.

**4. `01 - Cultivo`: "Modificar o Próprio Corpo" em 18, logo depois de Zumbis, e não como
última da pasta.** Conflito parcial: `AUDITORIA-corpos-e-povos.md` pede "manter no fim da
pasta", mas o argumento que dá é de **dependência** (a nota usa termos de "Cultivo Fora do
Humano" e de "Zumbis"), não de fecho; `AUDITORIA-cultivo.md` argumenta que a pasta deve
fechar em "Tornar-se Venerável", que é o clímax do currículo. Atendo os dois: a nota vem
depois de todas as suas dependências, e o Venerável continua fechando. *Alternativa
descartada:* deixá-la literalmente por último, o que encerraria a pasta com a rota de quem
desistiu de crescer, logo depois da nota sobre o topo do mundo.

**5. `05 - Sociedade`: "Povos e Variantes Humanas" na 12ª.** `AUDITORIA-corpos-e-povos.md`
pediu "posição 07", mas contando sobre a numeração **antiga** da pasta (9 notas), em que
"Cultura das Cinco Regiões" era a 06. A regra que ele expressa é relativa — *logo depois de
Cultura das Cinco Regiões e antes de Sociedade Fora das Cinco Regiões* — e na ordem de 15
notas de `AUDITORIA-sociedade.md` isso dá a 12ª. As duas recomendações são compatíveis
assim que se lê a segunda como posição relativa; não há conflito de fato, só de número.

**6. `10 - Apendices`: "Catálogo de Bestas e Reis Fera" na 09ª e "Linha do Tempo e Eras"
na 10ª.** Decisão minha. `pesquisa/bestas-catalogo.md` propôs deixar o catálogo de bestas
em `10` "porque assim nenhum wikilink precisa ser reescrito" — economia de trabalho que o
script faz sozinho e de graça. Troquei os dois para que os **cinco catálogos de coisas**
fiquem contíguos e a linha do tempo feche a pasta como pano de fundo histórico.
*Alternativa descartada:* manter como está, ao custo de a linha do tempo partir o bloco de
catálogos ao meio.

**7. `11 - Forcas e Organizacoes`: a ordem das cinco regiões fica como está.** Decisão
minha, na ausência de recomendação formal. A nota-porta sugere, em prosa, ler Fronteira Sul
→ Continente Central → a região da campanha; poderia ter transformado isso na ordem da
barra lateral. Não fiz: a ordem Sul, Norte, Central, Oeste, Leste é a que a tabela "Mapa da
pasta" já usa e a que o resto do vault emprega ao listar as regiões, e a recomendação
didática continua entregue no texto, onde ela cabe sem custo de consistência.
*Alternativa descartada:* reordenar para Sul → Central → Norte → Oeste → Leste.

**8. Pastas sem recomendação nenhuma.** `07 - Veneraveis e Legados` e `08 - Eventos e
Cenarios` já estavam no disco na ordem certa — a primeira nunca mudou, e a segunda foi
escrita direto na ordem de `PLANO-eventos.md`. Transcrevi as duas como estão, sem
alteração. `04 - Mundo` e `06 - Economia e Vida` vieram inteiras dos respectivos relatórios,
sem conflito.

---

## Validação

Script temporário rodado no scratchpad da sessão (fora do vault): para cada uma das 11
pastas, compara o **conjunto** de nomes da `ORDEM` acima com o conjunto de nomes de `.md`
no disco, ambos sem o prefixo numérico e normalizados em NFC, e checa duplicatas.

```
pasta                              ordem  disco  status
01 - Cultivo                          19     19  OK
02 - Gu                               16     16  OK
03 - Paths                            29     29  OK
04 - Mundo                            19     19  OK
05 - Sociedade                        15     15  OK
06 - Economia e Vida                  16     16  OK
07 - Veneraveis e Legados              4      4  OK
08 - Eventos e Cenarios               29     29  OK
09 - Estudos de Caso Mecanicos        49     49  OK
10 - Apendices                        10     10  OK
11 - Forcas e Organizacoes             6      6  OK

total: 212 na ORDEM, 212 no disco
RESULTADO: conjuntos identicos pasta a pasta
```

Confirmação independente: uma cópia de `numerar-notas.py` com este `ORDEM` foi rodada em
`--dry` a partir da raiz do vault (modo seco: **nada foi alterado no disco**). Saída:

```
renomeios planejados: 135
arquivos com wikilinks a reescrever: 223
```

Sem nenhuma linha de `PROBLEMAS NO PLANO` — ou seja, **zero** notas no disco fora da ordem
e **zero** notas na ordem sem arquivo correspondente. O script não abortaria.
