# Vagueza defensiva — varredura e conserto

**O que é este arquivo.** Registro de uma varredura do vault inteiro atrás de um padrão de
escrita que o usuário detectou lendo a nota `10 - Estudos de Caso Mecanicos/13 - O Refém que
Cura os Dois Lados`: notas que, **com medo de dar spoiler, ficaram vagas sobre mecânica** —
falam de "um certo Gu", "um determinado método", "um dos Veneráveis", "uma ilha específica" —
e com isso perdem clareza sem comprar proteção nenhuma, porque **quem nunca leu a obra não é
spoilado por mecânica**.

**A regra que a varredura aplicou.** A política de spoiler do projeto proíbe contar o
**enredo**, não explicar o **sistema**.

- Continua fora: arcos, reviravoltas, mortes, traições, planos e destino de personagens
  nomeados. Personagens seguem anônimos — isso o vault já fazia bem e não foi mexido.
- Entra sem rodeio: o nome do Gu, do golpe, do lugar, da instituição, do caminho, do material,
  do Venerável — e o mecanismo completo de cada um, com custo e limite.

**O que NÃO é alvo.** As marcações honestas do vault: `—` ("a obra não informa") e `(ded.)`
(dedução). E a vagueza que é **da própria obra**: "um certo número de marcas do Dao", "um certo
raio" são tradução literal do texto e ficam como estão.

---

## 1. O caso que originou a varredura — o Gu da Rotação Yin-Yang

**Onde estava vago.** `11 - Apendices/07 - Gu de Rank 4.md`, ficha *Yin Yang Rotation Gu*. A
ficha inteira cabia em quatro linhas: "troca o sexo do corpo do usuário; a versão Yin ainda cura
estados de quase-morte", com `Como é.` marcado `—` e `Dieta.` marcada como "não informada". O
estudo de caso que o usuário estava lendo (`10 - Estudos de Caso Mecanicos/13`) descrevia a
mesma cena inteira sem nunca dizer o nome do Gu — falava de "um par de Gu de rank 4, de cura,
com fama de trazer o morto de volta à vida", "a metade que cura", "a metade retida". O nome só
aparecia no campo `aliases` do frontmatter, invisível na leitura.

**O que a obra diz** (caps. 199, 200, 201, 202, 353 e 1380/1462, verificado no texto-fonte):

- São **dois** vermes-Gu, um **preto** e um **branco**, girando em órbita um em torno do outro e
  formando uma **esfera de luz com o desenho do taiji**. O Gu Yang é descrito como "de armadura
  branca".
- **Gu Yin em corpo masculino**: converte yang em yin, o alvo é curado por completo e **vira
  mulher**. **Gu Yang em corpo feminino**: o inverso. Cada metade só age no corpo oposto ao que
  a outra tratou — por isso só existem em par.
- É **"Gu de cura de rank 4 com o efeito de trazer o morto de volta à vida"**. Aplicado a uma
  pessoa congelada e com a consciência já se dissipando, devolveu um corpo inteiro, de braços
  intactos. **Não ressuscita os Gu do alvo** — esses continuam mortos.
- Ao ser acionado, o Gu **funde-se no corpo do alvo**; explode luz da cor da metade usada, o qi
  correspondente é sugado de toda a volta formando um **vórtice de energia**, e dentro do corpo
  nasce uma força vital nova que cresce a olhos vistos.
- **Custo: dez pontos percentuais de aptidão, permanentes, por uso.**
- Isso é o que permite **desligar uma constituição extrema**: elas exigem aptidão de cem por
  cento, e a 90% param de se manifestar. Mas a aptidão **volta a crescer com o cultivo** e a
  constituição retorna, exigindo a outra metade e mais dez pontos. É ciclo, não conserto.
- **A dieta ESTÁ na obra**, ao contrário do que a ficha dizia: com o par intacto formando a
  esfera de taiji completa, **eles se alimentam sozinhos** da conversão mútua entre qi yin e qi
  yang; quebrado o par, o sobrevivente precisa ser solto periodicamente para absorver do ar o qi
  correspondente. Um par completo é um Gu de rank 4 de manutenção zero.
- Acionamento: um Mestre Gu de **rank 1** com reserva de essência de **rank 3** gastou **quase
  toda** a reserva numa única metade.
- **Evolução**: existe versão imortal, e quem virou Imortal **não consegue mais reverter a troca
  com o exemplar mortal de rank 4** — precisa elevar o Gu a nível imortal antes. A janela para
  desfazer fecha quando o alvo sobe de patamar.

**Como ficou.** A ficha foi reescrita por inteiro com esse conteúdo, mais um bloco
`> [!note] Para o design` sobre a dependência estrutural que ela cria. Nada de enredo entrou:
nenhum personagem é nomeado.

**O que aconteceu com a nota de origem.** Enquanto esta varredura corria, o agente responsável
pela pasta `10 - Estudos de Caso Mecanicos` fez uma triagem e **excluiu** a nota `13 - O Refém que
Cura os Dois Lados`, por ela ser traço de personagem e não regra de sistema. A mecânica não se
perdeu: ela vive agora, completa e com o Gu nomeado, na ficha do `Yin Yang Rotation Gu` em
`11 - Apendices/07 - Gu de Rank 4.md`. A linha correspondente da tabela em
`11 - Apendices/10 - Catálogo de Gu - Mortais.md` foi repassada ao agente daquele arquivo com o
conteúdo verificado acima.

---

## 2. Casos corrigidos

*(seção preenchida durante a varredura; ver também os relatórios parciais
`_pipeline/vagueza-parcial-*.md`, que são arquivos de trabalho dos agentes)*

### 2.1 Apêndices `01` a `08` (glossário, tabelas e catálogos de Gu por rank)

| Arquivo | O que estava vago | O que a obra diz | Como ficou |
|---|---|---|---|
| `11/07 - Gu de Rank 4` — *Instant Success Gu* | "quem carrega **um certo Gu instável do caminho do tempo**, descrito pela obra como uma bomba-relógio, não pode usar Gu do tempo para acelerar refinos" | É o **Spring Autumn Cicada**, e a própria obra o chama de bomba-relógio porque ele se recupera dentro da abertura e a pressiona (cap. 568) | Nomeado, com o motivo mecânico, e a regra geral enunciada: carregar um Gu instável do tempo fecha a família inteira de ferramentas daquele caminho |
| `11/07 - Gu de Rank 4` — *Green Mountain Remains* | "das três garantias de refino do mundo, **a Terra de um certo Gu Imortal** é longe demais" — e a formulação era, além de vaga, errada | São a **Terra de Bu Bai** (terra sagrada dos mestres do refino, no Continente Central), o **Undefeated Hundred Battles Gu** (consumível de rank 5 que garante 100% de sucesso, hoje extinto, com aparência de disco de calcário cinzento) e este (cap. 286) | As três listadas com nome e mecanismo, mais a distinção que a mesa aproveita: as duas primeiras garantem o sucesso, esta só salva o Gu-núcleo quando o refino falha |
| `11/07 - Gu de Rank 4` — série *jin/jun* | "criada por **um dos Veneráveis do caminho da força**" — errado e vago | Não foi Venerável nenhum: foi **Chu Du, o "Imortal da Dominação"**, Gu Imortal de rank 7 das Planícies do Norte que ascendeu há trezentos anos; ele também refinou o Gu Imortal de rank 6 `Strength of a Thousand Jun` (cap. 442) | Nomeado, com o erro corrigido e as unidades (*jin*, *jun* = trinta jin) explicadas |
| `11/07 - Gu de Rank 4` — *Burning Firefly Gu* | "vive num **deserto específico**"; "o local é ponto de recurso de **um clã imortal**" | **Deserto dos Vaga-Lumes Ardentes**, no Deserto Ocidental, ponto de recurso do **clã Fang**, com formação imortal e um Gu Imortal de rank 6 de guarda; o clã usa os próprios Gu dali para manter um ambiente de caminho do fogo e criar outros Gu de fogo (cap. 1780) | Nomeados; acrescentado o mecanismo do criadouro, que é a razão de o lugar valer uma guerra |
| `11/07 - Gu de Rank 4` — *Swallow Fire Gu* | "aquisição planejada contra **uma tribo do caminho do fogo**" | A **tribo Tang**, que prioriza fogo em todo o arsenal (cap. 510) | Nomeada |
| `11/07 - Gu de Rank 4` — *Refine Essence Spirit Gu* | "Gu de transmissão secreta de **uma tribo do norte**" | A **tribo Dong Fang**, das Planícies do Norte (cap. 505) | Nomeada |
| `11/07 - Gu de Rank 4` — *Burial Soul Toad* | "as almas guardadas nele **viram um Gu diferente ao passar por uma montanha específica**" — efeito sem causa, e o parágrafo ficava circular | A montanha é a **Dang Hun Mountain**: as almas se despedaçam nela e se fundem ao terreno, formando com o tempo **gutstones**; algumas contêm um **`Guts Gu`**, que fortalece a alma. Três travas: o Guts Gu dura só um instante, as gutstones não podem ser removidas do lugar, e alma demais **infla até um desastre de morte certa** (caps. 410, 616) | A cadeia inteira explicada, virando uma logística de duas pontas |
| `11/07 - Gu de Rank 4` — *Nauseous Crying Baby Gu* | "criado para anular **um golpe combinado célebre de uma tribo do norte**" | O golpe é a **alma combinada de três corações**, da **tribo Dong Fang** (cap. 507) | Nomeados; a corrida armamentista posterior já estava descrita no campo "Como se obtém" e não foi duplicada |
| `11/07` e `11/08` — *Sky Well Gu* / *Blue Sky Well Gu* | "ocorre em um único lugar do mundo — **uma ilha específica no Mar Oriental**"; "apenas **um clã** talvez tivesse um exemplar" | **Ilha Tian Jing**, no Mar Oriental; e o clã é o **clã Yi**, da Fronteira Sul (cap. 353) | Nomeados nos dois arquivos |
| `11/07` e `11/08` — linhagem do *Heavenly Essence Treasure Lotus* | "o exemplar de rank 6 era o Gu vital de **um dos Veneráveis, o mais rico da história em essência imortal**" | **Genesis Lotus Immortal Venerable**, criador do caminho da madeira. E a obra dá a consequência prática: ele nunca precisou se preocupar com essência, enquanto os inimigos **esgotavam a própria no meio da luta** (caps. 463, 2073) | Nomeado, com a consequência de combate acrescentada — ter a fonte não é mais dano, é nunca ficar sem munição |
| `11/08 - Gu de Rank 5` — *Moving Perspective Cup Gu* | "a receita é de **um dos Veneráveis**, que a criou para enviar a taça ao **depósito do espaço**" | **Thieving Heaven Demon Venerable**, criador do caminho do roubo; o destino é o **space cave**, o depósito lendário e proibido do caminho do espaço, onde se acumulam Gu selvagens em número incontável — e ele **fracassou** no objetivo original (cap. 434) | Nomeados; o catálogo plano já trazia tudo isso, e era a versão hierárquica que estava vaga |
| `11/08 - Gu de Rank 5` — *Blood Skull Gu* r5 | "criada séculos depois por **um Venerável**" | **Giant Sun Immortal Venerable** desenvolveu a versão de rank 5, que só exige extrair sangue dos parentes em vez de massacrar o clã (cap. 2298) | Nomeado |
| `11/07` e `11/08` — família do sangue | "herança verdadeira do **fundador do caminho do sangue**" | **Ancestral do Mar de Sangue** (*Blood Sea Ancestor*), Mestre Gu de **rank 7** — não Venerável —, que espalhou **centenas de milhares de sítios de herança** pelas cinco regiões, dos quais só **nove** são heranças verdadeiras (cap. 2014) | Nomeado, com a escala das heranças, que explica por que esses Gu circulam fora do mercado |
| `11/04`, `11/07`, `11/08` — caminho yin-yang | "fruto de uma pesquisa que **o próprio criador** acabou julgando rasa demais"; "tal como **um Venerável** o concebeu" | **Giant Sun Immortal Venerable** tentou fundar o caminho, com a ambição de descrever *todos os seres do mundo* em termos de yin e yang; desistiu ao reconhecer que a própria formulação era rasa demais (cap. 2300) | Nomeado nos três catálogos, com a ambição original e o motivo do abandono |
| `11/02 - Tabelas`, seção 6 | "uma única xícara de **um certo chá** feito de materiais imortais de rank 8 rende cerca de 1.000 dao marks" | É o **chá da mente extremamente serena**, um **golpe do caminho da comida** criado pelo **Paradise Earth Immortal Venerable**: gasta material imortal de rank 8 do caminho da terra e grava marcas do Dao da terra em quem bebe. Mil marcas = tribulação celestial (750) + calamidade terrena (250), exatamente. Mas o rendimento normal é "algumas centenas", a eficiência é baixa, e quase todo chá e vinho do mundo são **receitas de Gu do caminho da comida incompletas** (cap. 2083) | Nomeado e explicado, com as três ressalvas que impedem de ler isso como dinheiro comprando poder — e mantendo o ponto estrutural, que é da obra: o método quebra o monopólio das provações como fonte de marcas |
| `11/02 - Tabelas`, seção 1.1 | tabela de mudança de aptidão citava "**um Gu de cura de rank 4 que ressuscita**" e um método demoníaco, sem nomes | O Gu é o **`Yin Yang Rotation Gu`**; a subida documentada de 43% a 90%+ é o **`Blood Skull Gu`** | Ambos nomeados, com remissão às fichas completas |
| `11/02 - Tabelas`, seção 2 | "o truque foi engolir **um Gu consumível de rank 3** que converte toda a essência da abertura numa essência especial" | **`Man-beast Life Burial Gu`**: engolido, desce como um fluxo preto-avermelhado, tinge toda a essência da abertura e a torna muito mais agressiva contra a parede. Essa essência **mata qualquer Gu** em que for injetada e **derruba a aptidão** se ficar dentro — daí o terceiro passo obrigatório, expulsá-la logo após a ruptura (cap. 152) | Nomeado, com o procedimento de três passos completo |
| `11/02 - Tabelas`, seção 5 | "as 16 contas/dia (…) o patrimônio de **uma figura histórica**" — alusão de enredo | Aqui a vagueza escondia **enredo**, não mecânica | Reescrito para não depender de identidade nenhuma: "a renda de uma abertura imortal excepcional, do tipo que aparece uma vez por era" |
| `11/02 - Tabelas`, seção 10 | "o único atalho conhecido é **um domínio lendário e praticamente inacessível**" | O **Domínio Primordial** (*Primordial Domain*), domínio recluso citado em *As Lendas de Ren Zu*; entrar nele eleva um caminho a Supremo Grão-Mestre de uma vez, e o que o torna inacessível é a localização — nona camada da Caverna do Demônio Enlouquecido (cap. 2085) | Nomeado e localizado |
| `11/02 - Tabelas`, seção 12 | "a ruptura do teto humano só é possível por **uma técnica específica**, herdada de **um único Venerável**" | A **verdadeira herança do Spectral Soul Demon Venerable**, criador do caminho da alma, que descreve a escada de alma de um milhão, dez milhões, cem milhões e alma desolada | Nomeada |
| `11/01 - Glossário` — *Longevity Heaven* (2 linhas) | "território celestial de **um dos Veneráveis**" | É a **abertura imortal do Giant Sun Immortal Venerable**, deixada como base ao morrer; hoje gruta-céu de rank 9 que suserana as Planícies do Norte, habitada pelos descendentes de sangue dele (cap. 2047) | Nomeado nas duas ocorrências |
| `11/01 - Glossário` — *Shadow Sect* (2 linhas) | "rede oculta de fragmentos de alma de **um Venerável**" | As **almas fragmentadas do Spectral Soul Demon Venerable**, criador do caminho da alma, acumulando influência por dezenas de milhares de anos (cap. 2047) | Nomeado nas duas ocorrências |
| `11/01 - Glossário` — *Zombie Alliance* (2 linhas) | "aliança mundial de zumbis imortais; **na verdade uma fachada**" — fachada de quê? efeito sem causa | É a **fachada pública da Shadow Sect**, com filiais nas cinco regiões (cap. 2047) | Completado |
| `11/01 - Glossário` — *Heavenly Court* | "a instituição de topo do mundo" — sem dizer quem a construiu | **Primordial Origin, Star Constellation e Genesis Lotus**, os três, a duras penas (cap. 2047) | Nomeados |
| `11/01 - Glossário` — *theft path* | "criado por **um único Venerável**" | **Thieving Heaven Demon Venerable** — e a mesma nota o nomeia três tabelas adiante | Nomeado |
| `11/01 - Glossário` — *Primordial Domain* | "território ligado ao **primeiro Venerável da história**" | **Primordial Origin Immortal Venerable**; e a linha não dizia onde fica nem o que se ganha entrando | Nomeado, localizado e com o efeito |
| `11/01 - Glossário` — *true inheritance* | "o corpo completo de conhecimento deixado por **um Venerável**" — definição estreita demais | Nem toda herança verdadeira é de Venerável: o Blood Sea Ancestor era rank 7 e deixou nove | Corrigido |

**Vagueza legítima nesta faixa, deixada intacta:** as ocorrências de "um certo número de marcas
do Dao", "um certo raio", "um certo limiar" e "um certo ponto" são **tradução literal da obra**,
que é ela mesma vaga ali; a nota inclusive diz isso em voz alta em `01 - Cultivo/16 - Dao Marks`.
Também ficaram como estão os "um clã", "uma tribo", "um mercador", "um praticante" que
anonimizam **pessoas** — é a política de spoiler funcionando, e o usuário aprovou explicitamente
esse uso. E ficaram os `—` e `(ded.)`, que são honestidade e não rodeio.

### 2.2 O resto do vault, por pasta

A varredura foi feita por seis frentes paralelas, cada uma lendo os arquivos do seu escopo de
ponta a ponta e verificando cada caso no texto-fonte antes de escrever. Os relatórios detalhados,
caso a caso e com capítulo, ficam em `_pipeline/vagueza-parcial-A.md` até `-F.md`. O resumo:

| Frente | Escopo | Casos corrigidos | Padrão encontrado |
|---|---|---|---|
| A | `01 - Cultivo`, `02 - Gu`, as três notas de raiz | 41 entradas, ~95 trechos, 24 de 38 arquivos | Gu e métodos anônimos onde a obra dá o nome: `Cleansing Water Gu`, `Stone Aperture Gu`, `Gather Oil Gu`, `Justice Gu`, `Sovereign Immortal Fetus Gu`, `Second Aperture Gu`, `Ten Extreme Immortal Zombie Lifeless Formation`. E uma nota que **descrevia o mesmo método duas vezes sem perceber**, justamente porque nunca o nomeava |
| B | `03 - Paths` | 33 entradas, ~60 pontos de texto, 28 de 29 arquivos | **O foco da causa editorial (4.3).** A pasta escrevia "um Venerável", "uma instituição", "um clã" para exatamente as entidades que as pastas vizinhas nomeiam duas notas adiante |
| C | `04 - Mundo`, `05 - Sociedade` | **110 casos**, 30 de 34 arquivos | Categoria à parte — ver 4.2. Lugares, construções e formações sem nome: `Crazed Demon Cave`, `crazed demon ninth void formation`, `Emperor City`, `Dark Flow Giant City`, `Formless Hand`, `divine/ghostly concealment`, `Di Zang Sheng` |
| D | `06 - Forças`, `07 - Economia`, `08 - Veneráveis` | 62 casos, 21 de 26 notas | Veneráveis e organizações anônimos onde a obra nomeia; e **três correções factuais** que só apareceram ao ir ao texto |
| E | `11 - Apendices` 09 a 16 | **~240 casos**, 8 de 8 arquivos | Categoria à parte — ver a seção 4.1. 150 dos casos estão num arquivo só (`10 - Catálogo de Gu - Mortais`), com 117 ocorrências de "o cultivador da cena". Mais `Heavenly Court` seis vezes na mesma nota, `Treasure Yellow Heaven`, `Refinement Cauldron`, `Derivation Gu`, `Space Escape Gu` |
| F | `11 - Apendices` 05 e 06 | 23 casos | **Anonimato de agente**, não de mecânica: o inventor, o clã, o dono da terra abençoada. Onze dos vinte e três |
| (esta nota) | `11 - Apendices` 01 a 04, 07 e 08 | 26 casos | Ver a tabela da seção 2.1 |

Quatro achados dessa varredura merecem destaque porque não são só "faltava um nome" — a vagueza
estava escondendo mecânica ou, pior, um erro:

1. **Uma tabela cuja coluna se chamava "Criador, quando a obra nomeia" e não nomeava ninguém.**
   Em `03 - Paths/01 - Visão Geral dos Paths`, a cronologia dos caminhos por era dizia "por um
   Venerável", "por outra Venerável", "por dois Veneráveis Demônios". A obra dá os sete nomes numa
   lista só. A tabela mais importante do domínio estava inutilizável.
2. **Duas notas afirmavam que a obra nomeia — e sonegavam o nome.** `07 - Enslavement Path` dizia
   "credita a criação a um **Venerável nomeado**" e `22 - Phantom Path` dizia "por um Gu Imortal
   **nomeado**". São Primordial Origin e Xu Wu Xie.
3. **Uma ficha declarava silêncio da obra onde a obra fala.** O `Three Stars in the Sky Gu`
   (rank 3) dizia "a obra dá o nome e o rank e **não descreve o efeito**", com cinco campos em
   `—`. A obra descreve: a escada amplifica os Gu do caminho das estrelas, equivale a um
   `Amplify Effect Gu` não convencional, com taxa de sucesso muito maior e materiais comuns.
4. **Uma nota descrevia o mesmo método duas vezes sem perceber, porque nunca o nomeava.** Em
   `01 - Cultivo/10 - As Dez Constituições Extremas`, "uma técnica de abertura extremamente rara
   que reduz tribulações pela metade" e "um método capaz de herdar a constituição a partir de um
   corpo" são **o mesmo** método da abertura imortal de vida e morte. Anonimizar custou aqui mais
   que clareza: custou a percepção de que era um item só.
5. **A vagueza carregava um erro de fato junto.** Em `11/16 - Linha do Tempo e Eras`, "o método de
   refinar um determinado Gu de fuga espacial, que fracassou nas mãos do maior refinador da
   história" estava na lista de "o que se perdeu e não volta". A obra diz o contrário: o
   `Space Escape Gu` **foi refinado com sucesso**, depois de vinte e um anos de trabalho, e o que
   falhou foi a **função** — ele simplesmente não entrava na Porta do Espaço, e ninguém nunca
   descobriu por quê. É o único fracasso registrado na carreira daquele refinador, e vira um bloco
   de design bem melhor que a versão vaga: um Gu pode ser refinado corretamente e mesmo assim não
   cumprir a função, porque a falha estava na **concepção**.

---

## 3. Onde a vagueza era legítima, e por quê

Nem tudo o que parecia rodeio era rodeio. Estes casos foram examinados e **deixados como estão**:

- **Os quatro estados de confiabilidade.** Todo `—` ("a obra não informa") e todo `(ded.)` são
  honestidade declarada, não evasão, e foram preservados sem exceção.
- **A vagueza da própria obra.** "Um certo número de marcas do Dao", "um certo raio", "acima de um
  certo limiar" são tradução literal: o texto original é vago ali, e a nota de Dao Marks inclusive
  diz isso em voz alta. Copiar a vagueza da fonte é fidelidade.
- **Pessoas.** "Um praticante de rank 3", "um mercador demoníaco", "uma candidata à ascensão" —
  o vault anonimiza personagens de propósito, e o usuário aprovou explicitamente esse uso na
  própria observação que originou este trabalho. Continua.
- **Sujeito genérico de regra.** "Um cultivador que empilha marcas de força" não é um personagem
  escondido: é a forma correta de enunciar uma regra.
- **Lacunas reais da obra**, registradas como tais: o grão-mestre de receitas que ensinou o Liquor
  Worm, o fundador de seis das dez grandes seitas, o criador do caminho do tempo, a Casa de Gu
  Imortal de Reckless Savage. Em todos, a checagem no texto confirmou que **não há nome**.
- **Um aviso editorial explícito** em `06 - Mar Oriental`, onde a nota **declara** que não vai
  contar o enredo em vez de aludir a ele. É a forma certa de resolver o caso 3 do critério.
- **Um caso não resolvido, registrado para checagem futura:** `07/08` e `07/10` falam de "clãs
  formalmente aliados a um bloco político que prega igualdade entre humanos e variantes". O grep
  no texto-fonte não localizou esse bloco; o que existe é a doutrina pessoal de Paradise Earth.
  Ficou genérico de propósito — nomear errado é pior que deixar vago.

---

## 4. Veredito: o padrão é frequente, e tem **duas causas diferentes**

**Frequente, e não pontual.** Foram **535 casos corrigidos em 114 notas** — mais da metade das 211
do vault —, espalhados por todas as pastas temáticas e pelos apêndices.

Mas a varredura terminou com um diagnóstico que ela não tinha no começo: **não é um problema só,
são dois**, com causas distintas e conserto distinto.

### 4.1 A causa que não é editorial: resíduo de uma substituição automática

Metade do volume total está concentrada nos catálogos planos de `11 - Apendices`, e ali a vagueza
**não é medo de spoiler nem hábito de redação** — é sobra de uma substituição automática de nomes
rodada em algum passo anterior do pipeline. A prova é que ela deixou frases **agramaticais**, que
ninguém escreveria por cautela editorial:

> `"de o cultivador da cena"` · `"as suas o cultivador da cena stone nests"` ·
> `"da tribo uma tribo do norte"` · `"criada pela Gu Imortal uma Gu Imortal"` ·
> `"a terra abençoada uma Gu Imortal"` · `"**a** golpe combinado"`

Só `10 - Catálogo de Gu - Mortais.md` tinha **117 ocorrências de "o cultivador da cena"**, 15
placeholders de nome e 13 erros de concordância criados pela própria substituição. E o que foi
apagado eram, em maioria esmagadora, coisas que o vault nomeia sem cerimônia noutras pastas —
Heavenly Court, Treasure Yellow Heaven, Crazed Demon Cave, clã Gu Yue, Zombie Alliance, os dez
Veneráveis, todos com nota própria.

O contraprova está no mesmo escopo: `13 - Catálogo de Golpes - Mortais.md` saiu praticamente
limpo, e usa exatamente a descrição funcional que se quer ("um praticante rank 3 auge do caminho
da força"). O estilo do vault estava certo; **o passo de processamento é que corrompeu o texto**.

> [!warning] Consequência para o projeto
> Isto não se resolve com uma regra de escrita — se resolve **não rodando de novo aquela
> substituição**. Se algum script do pipeline ainda faz troca cega de nome próprio por perífrase,
> ele precisa ser desligado ou reescrito para produzir descrição funcional (rank + caminho +
> situação), nunca uma muleta fixa. E qualquer varredura futura deve incluir uma busca por
> concordância quebrada (`de o `, `a golpe`, `da tribo uma tribo`), que é a assinatura do estrago.

### 4.2 A causa que também não é editorial: uma política errada escrita numa nota

Uma nota — `05 - Sociedade/11 - Cultura das Cinco Regiões` — **abria declarando a política ao
contrário**: *"os nomes próprios da obra estão amarrados ao enredo"*. E agia de acordo, trocando
oito organizações reais por rótulos **inventados pelo próprio vault**, entre colchetes:
`[Clã Número Um]`, `[Clã da Prisão]`, `[Linhagem Fundadora]`. A nota chegava a admitir o estrago
em voz alta — *"uma dúzia de entidades sem nome vira névoa"* — e continuava fazendo.

Isso é mais grave que uma perífrase, porque **inventa vocabulário que não existe no mundo**: a
designer que lesse `[Clã da Prisão]` procuraria esse nome na obra e não acharia nada. Os oito
rótulos foram substituídos pelos nomes reais (clãs Wu, Shang, Tie, Yi, Sacred Feather City,
linhagem Huang Jin, clã Qing, Corte dos Homens-Peixe) e o callout com a política errada foi
removido. Esse callout é a raiz das outras 109 correções daquela frente: uma nota enunciou uma
regra falsa, e as notas vizinhas a seguiram.

**Verificado ao fim da varredura:** não resta nenhum rótulo inventado entre colchetes em nenhuma
nota do vault, e a frase da política errada não aparece mais em lugar nenhum.

### 4.3 A causa editorial: de-nomear entidades por hábito

O restante — as pastas de prosa — é o problema que a observação do usuário descreve, e ali a
gramática está correta: as frases foram escritas assim de propósito. Nenhuma pasta ficou sem nenhum caso.

Mas a distribuição diz mais que o total, e ela desmonta a hipótese de que isso fosse medo de
spoiler:

- **A vagueza é de agente, não de mecânica.** O vault quase nunca esconde *como uma coisa
  funciona* — as fichas são longas, numéricas, com custo e limite. O que ele escondia era **quem
  fez, onde fica, de quem é**: o Venerável, o clã, a instituição, a montanha, a ilha.
- **O vault já nomeava essas mesmas entidades noutro lugar.** Giant Sun, Spectral Soul, Thieving
  Heaven, o Tribunal Celestial, a Zombie Alliance, a Crazed Demon Cave — todos têm nota ou linha
  própria em alguma pasta. A perífrase não protegia nada: ela só obrigava a leitora a montar
  sozinha a ligação entre duas notas que falam da mesma coisa.
- **A concentração é por pasta, não por assunto.** `03 - Paths` sozinha responde por um quarto dos
  casos; `06 - Fronteira Sul` e `26 - Dream Path` não têm nenhum. Isso é assinatura de **hábito de
  redação de uma leva de escrita**, não de uma decisão de política.
- **Quando havia enredo de verdade por trás, ele era raro** — meia dúzia de casos em todo o vault,
  e o conserto certo foi reescrever a frase para não depender dele, nunca aludir.

### O que isso recomenda para o projeto

**São três consertos, não um** — e só o terceiro é uma regra de escrita:

1. **Desligar ou reescrever a substituição automática de nomes** (causa 4.1). Se algum passo do
   pipeline ainda troca nome próprio por perífrase fixa, ele produz "o cultivador da cena" às
   centenas e quebra a concordância no caminho. Substituto correto: descrição funcional — rank,
   caminho, situação —, nunca uma muleta única repetida.
2. **Nunca inventar rótulo para substituir nome real** (causa 4.2). Um `[Clã da Prisão]` entre
   colchetes é pior que a perífrase: cria vocabulário que não existe no mundo e que a designer vai
   procurar na obra sem achar. Se um nome não pode entrar, a frase se reescreve sem ele.
3. **A regra de escrita que faltava** (causa 4.3). O `CLAUDE.md` descreve a política pelo
   **conteúdo** (mecânica sim, enredo não) e não pelo **erro típico**:

> **Nomeie sempre o objeto, o lugar, a instituição, o caminho, o material e o Venerável.** A
> política de spoiler protege **pessoas e enredo**, não substantivos do mundo. Se a frase precisar
> de um rodeio ("um certo Gu", "um dos Veneráveis", "uma ilha específica"), o rodeio está no lugar
> errado: ou o nome entra, ou a frase é reescrita para não precisar dele. **Alusão obscura é o
> pior dos dois mundos** — não informa e ainda desperta a curiosidade que a política queria
> evitar.
>
> Corolário prático, porque foi o que mais apareceu: se a nota escreve "a obra nomeia X" ou "um
> Gu Imortal nomeado", ela **tem de dar o nome** — afirmar que o nome existe e não dá-lo é o
> defeito na sua forma mais pura.

E uma verificação barata para qualquer varredura futura, que pega as três causas de uma vez:

```
# resíduo de substituição automática (assinatura: concordância quebrada)
grep -rnE "de o cultivador|da tribo uma tribo|\ba golpe |criada pela Gu Imortal uma" --include="*.md" .
# rótulo inventado
grep -rnoE "\[(Clã|Linhagem|Seita|Tribo|Cidade|Corte|Casa) [A-ZÀ-Ú][^]]{0,30}\]" --include="*.md" .
# perífrase editorial
grep -rniE "um certo Gu|um dos Veneráveis|um Venerável |uma ilha específica|o cultivador da cena" --include="*.md" .
```

---

## 5. Verificação

`python3 _pipeline/auditar-links.py`, depois de todas as edições das seis frentes:
**5.502 links, 0 quebrados; 274 âncoras, 0 quebradas.**

Verificações extras feitas ao fim, todas com resultado zero:

- nenhum resíduo de concordância quebrada da substituição automática;
- nenhum rótulo inventado entre colchetes em nenhuma nota;
- nenhuma ocorrência restante de "o cultivador da cena" no vault;
- a frase da política errada (*"os nomes próprios da obra estão amarrados ao enredo"*) não aparece
  mais em lugar nenhum.
