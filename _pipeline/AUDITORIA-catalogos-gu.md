# Auditoria dos catálogos de Gu

Relatório da leva de fechamento dos catálogos de Gu (`10 - Apendices/03`, `04`, `05`, `06`).
Escrito incrementalmente durante o trabalho.

Escopo: deduplicação dos dois catálogos, varredura de Gu ausentes no texto-fonte,
reescrita das entradas vagas e conferência da nota-índice.

---

## Duplicatas fundidas

### Catálogo de mortais — dentro do próprio arquivo

Método: extração programática da primeira célula de toda linha de tabela e contagem de
frequência. Nove nomes apareciam duas vezes. Regra adotada para escolher a casa de cada
Gu: **quando a obra atribui um caminho, a ficha mora na seção daquele caminho**; as
seções que são famílias funcionais (cura e vida, Gu lendários, linhagem lunar) ficam com
os Gu que não têm caminho atribuído — com uma exceção justificada abaixo. Toda seção que
perdeu uma linha ganhou um **ponteiro em itálico** logo antes da tabela, dizendo onde a
ficha completa está.

| Gu | Estava em | Casa final | O que foi preservado da linha apagada |
|---|---|---|---|
| Therapy Light Gu | Caminho da luz + Cura e vida | **Caminho da luz** | o cardápio inventado (pétalas brancas e água de nascente `*`), somado ao ritmo canônico por rank |
| Vitality Leaf | Caminho da madeira + Cura e vida | **Caminho da madeira** | "barata e fácil de produzir porque a planta-mãe repõe as folhas; a cura mais difundida do mundo" |
| Wood Charm Gu | Caminho da madeira + Caminho da transformação | **Caminho da madeira** | a linha da transformação era um *stub* que se descrevia por referência ("ficha principal no caminho da madeira — ver acima"). Dela veio o único conteúdo real: refino reconhecidamente mais difícil que o dos outros rank 3 da época, e a rota de avanço por fusão com Lifespan Gu de cem anos (rank 4) e de mil (rank 5) |
| Blood Moon Gu | Caminho do sangue + Linhagem lunar | **Linhagem lunar** | "caso-modelo de troca de dieta por conveniência" e "janela mensal que um inimigo informado pode explorar". A exceção à regra geral está justificada abaixo |
| Moon Poison Gu | Caminho do veneno + Linhagem lunar | **Linhagem lunar** | "debilitação **progressiva**" e a mecânica de inalação enquanto o alvo continuar respirando |
| Blood Skull Gu | Caminho do sangue + Caminho do refinamento | **Caminho do sangue** | os números que faltavam: cerca de cem corpos quando são parentes próximos, **dez pontos percentuais de aptidão por carga**, e a história do exemplar (espólio selado, refinado na hora com uma injeção de essência; versão rank 5 criada séculos depois por um Venerável) |
| Guts Gu | Caminho da alma + Cura e vida | **Caminho da alma** | "o fortalecimento de alma número um do mundo, cerca de **dez vezes** os métodos comuns" e a dependência do Airsac Gu para sair do lugar |
| Hope Gu | Caminho do homem + Gu lendários | **Caminho do homem** | que a contagem de pontos de luz absorvidos **é** a medição de aptidão do rito dos quinze anos |
| Sneak Attack Gu | duas linhas seguidas, rank 2 e rank 5 | **as duas mantidas** | não era duplicata e sim duas potências reais. O erro era outro: a história de origem (refino de rank 1 fracassado, com cadáver de bebê anômalo, Sandpit, Chimney Smoke, Clear Water e sangue da ponta da língua) estava na linha do **rank 5**, quando pertence à do rank 2. Corrigido, e a linha do rank 5 passou a descrever a elevação |

**Por que a linhagem lunar é exceção.** A seção "Linhagem lunar" não é um caminho: é um
estudo de caso de uma árvore de fusões de um clã, e seu valor didático depende de as
linhas ficarem **lado a lado para comparação de colunas** (o texto da seção manda o
leitor comparar a coluna de alimentação do Golden Moon com a do Blood Moon). Tirar dois
ramos de lá para outras seções destruiria o argumento. Os dois Gu ganharam, na própria
célula de efeito, a frase que diz que pertencem também ao caminho do sangue e ao do
veneno, e essas duas seções ganharam ponteiro.

### Catálogo de imortais — dentro do próprio arquivo

Treze nomes duplicados. Nove deles eram o mesmo padrão: um Gu de **rank 9** aparecia na
seção do seu caminho **e** na seção "Os Gu de rank 9". Decisão: a seção "Os Gu de rank 9"
passa a ser a **casa única** de todo Gu daquele patamar, e as seções de caminho ficam com
ponteiro. O motivo é estrutural e está escrito na própria nota: no rank 9 as três
aptidões se dissolvem e as fichas usam uma coluna diferente das demais (✴️ Peculiaridade
em vez de refino/vantagem/desvantagem) — manter as duas cópias garantia divergência, e de
fato havia divergência em oito dos nove casos.

| Gu | Estava também em | O que a fusão preservou |
|---|---|---|
| Fate Gu | Caminho do céu | "impõe caminhos de vida fixos" e "foi usado apenas pela vontade do céu" |
| Wisdom Gu | Caminho da sabedoria | o uso **como material de refino** (reduz drasticamente o gasto de pensamentos e eleva muito o de essência) e que o portador mais famoso nunca chegou a refiná-lo |
| Heavenly Secret Gu | Caminho da sabedoria (7 → 9) **e** Caminho do céu (9) | as três eram o mesmo Gu. Rank corrigido para **7 → 8 → 9** (a obra registra as três potências e a elevação); dieta unificada (materiais imortais de céu; nuvens esplêndidas no rank 9); e a frase que explica por que 80% de falha ainda vale a pena |
| Derivation Gu | Caminho da regra | "deriva mundos novos" e "cria marcas de lei inteiramente novas" |
| Sovereign Immortal Fetus Gu | Caminho do homem | "corpo **compatível** com a alma já existente" |
| Fire Gu · Light Gu | Caminhos elementais e menores | a atribuição explícita de caminho (fogo e luz), que a seção de rank 9 não trazia |
| Heavenly Essence Treasure Imperial Lotus | Caminhos elementais e menores | quase tudo: a faixa **6 → 9**, a linhagem mortal que produz pedras primordiais, o consumo de nascentes na fase de fusão, e a condição de um dos Dez Grandes Gu Imortais |
| Kill | Caminhos elementais e menores | nada de novo; a fusão apenas eliminou a divergência de rank (8 contra 8 → 9) |

As outras quatro duplicatas não eram de rank 9:

| Gu | Estava em | Casa final | O que foi preservado |
|---|---|---|---|
| Regret Gu | Caminho do tempo + Caminho do refinamento | **Caminho do tempo** | as duas linhas descreviam **funções diferentes do mesmo Gu** e nenhuma das duas mencionava a outra: arma de arrependimento por contato, e refazer um Gu Imortal destruído a partir da insígnia do refino original. A ficha fundida traz as duas, e diz que a segunda é a única exceção conhecida à irreversibilidade |
| Blood Asset Gu | Caminho do sangue + Caminho do refinamento | **Caminho do sangue** | as duas eram redação diferente do mesmo conteúdo; ficou a mais explícita, com a ressalva de que ele não aumenta a chance de sucesso, só reduz a perda |
| Second Aperture Gu | Caminho do céu + Gu de utilidade e estrutura de abertura | **Gu de utilidade e estrutura de abertura** | os números da linha do céu (capacidade somada: 90% + 90% = 180%; dobro da recuperação; segundo conjunto completo de Gu) e a classificação no caminho do céu, que virou nota dentro da célula |
| Human Qi Gu | Caminho do homem + Caminho do qi | **Caminho do qi** | rank corrigido para **7 → 8** (a linha do qi dizia só 8) e a explicação de por que só serve a quem ainda não ascendeu |

### Entre os dois catálogos (mortal × imortal)

Vinte e nove nomes apareciam nos dois arquivos. **Vinte e um são versões mortal e imortal
de verdade** — o caso que a obra explicita com o par mortal/imortal do Pulling Water Gu, em
que o Gu Imortal continua precisando do mortal porque um Gu Imortal é único e não serve a
dois golpes ao mesmo tempo. Foram mantidos os dois lados: Accumulate Virtue, Blood
Handprint, Blood Skull, Bone Spike, Day, Expend Strength, Extreme Light, Grass Puppet,
Gruel Mud, Justice, Luck Inspection, Man As Before, Month, Slavery, Sneak Attack, Soul
Search, Star Shoot, Strength Qi, Territory, Wealth e Year Gu (mais o Pulling Water Gu, que
o catálogo mortal já trazia com a explicação completa do par).

A conferência descobriu um defeito silencioso nesse conjunto: **dezesseis dessas linhas não
diziam que a outra versão existe**. Quem lesse só o catálogo mortal do Day Gu não teria como
saber que há um Day Gu imortal, e vice-versa — o que, num catálogo de mesa, é o mesmo que a
informação não existir. Todas as dezenove pontas faltantes (dezesseis no mortal, três no
imortal) receberam a frase que declara a outra versão, com o rank dela e o wikilink para o
outro arquivo.

**Oito estavam no catálogo mortal indevidamente**, porque a obra só lhes dá rank imortal —
em vários casos a própria célula do catálogo mortal admitia isso ("o exemplar registrado é
de rank 6, portanto imortal"). Removidos do mortal, com ponteiro na seção de origem:

| Gu | Rank canônico | Onde estava | Como se resolveu |
|---|---|---|---|
| Derivation Gu | 9 | Gu lendários e conceituais | ficha só no imortal; ponteiro na seção lendária |
| Ability Gu | 8 | Gu lendários e conceituais | idem |
| Strong Gu | 7 | Gu lendários e conceituais | idem |
| Pride Gu | — (Gu Imortal) | Gu lendários e conceituais | a linha mortal era **muito mais rica** que a imortal; o conteúdo dela foi transplantado para a ficha imortal antes da remoção (ocupa área enorme na mente, recusa-se a sair, só o Humility o expulsa, e o expulso voa para outra mente) |
| Humility Gu | — (Gu Imortal) | Gu lendários e conceituais | idem (é o único meio de expulsar o Pride Gu, e expande a capacidade da abertura já desperta) |
| Master-Servant Gu | 7 | Caminho da escravização | ficha só no imortal; ponteiro |
| Formation Plate Gu | 6 | Caminho da formação | ficha só no imortal; ponteiro |
| Musician Gu | 6 | Caminho do homem | ficha só no imortal; e a seção do caminho do homem ganhou a divisão canônica da série das profissões (ver "Entradas reescritas") |

Dois ranks estavam vazios e foram preenchidos com o texto: **Justice Gu → rank 5** na
versão mortal (a própria célula dizia "o exemplar descrito é de rank 5") e **Expend
Strength Gu → rank 4** (o texto lista "rank four bitter strength, expend strength Gu and
charging crash Gu").
