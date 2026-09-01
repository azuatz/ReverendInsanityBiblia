# Pesquisa em wikis: lacunas deixadas pela leitura da obra

**Status:** COMPLETO — 7 de 7 perguntas trabalhadas (a nº 1 tem resultado negativo, ver seção)
**Data:** 2026-09-01
**Regra de ouro:** a OBRA é a autoridade máxima; a wiki complementa mas nunca sobrepõe.

## Fontes usadas

- **Wiki principal:** `https://reverend-insanity.fandom.com` — atenção: o domínio `reverendinsanity.fandom.com` (sem hífen) **não existe** (HTTP 404); `guzhenren.fandom.com` também **não existe** (404). Os dois wikis Fandom vivos são `reverend-insanity.fandom.com` (o grande, ~ usado aqui) e `true-reverend-insanity.fandom.com` (menor, fork).
- Nota de método: o WebFetch retornou HTTP 402 para o Fandom; as páginas foram lidas via API MediaWiki (`/api.php?action=parse&prop=text|wikitext`), que devolve o mesmo conteúdo da página pública.

Legenda de marcação:
- `[CONFIRMA texto]` — a fonte confirma o que a leitura da obra registrou
- `[COMPLEMENTA texto]` — a wiki traz o que a obra não deu explicitamente
- `[CONFLITA com texto]` — a fonte diverge do que a obra diz

---

## 1. Limiares percentuais de aptidão para romper cada rank — **PARCIALMENTE CORRIGIDO**

> [!warning] CORREÇÃO (2026-09-01, verificada no texto-fonte pelo usuário)
> A conclusão original desta seção — "a obra nunca fala em limiares percentuais" —
> estava **ERRADA**, e a wiki é que é incompleta. A obra ENUNCIA o mecanismo e dá o
> número do rank 1→2. Ver `CORRECAO-limiares-aptidao.md` nesta mesma pasta, com as
> citações exatas dos capítulos 90, 91, 105 e 10. Lição de método: a ausência de uma
> informação na wiki nunca prova ausência na obra; verificar sempre no texto-fonte
> antes de afirmar uma negativa.

### Resposta curta (revisada)

O **mecanismo existe e é explícito na obra**: romper a parede da abertura exige
projetar de uma vez uma porcentagem mínima de essência primeva, e a aptidão é o teto
de quanto se pode armazenar — logo a aptidão trava diretamente até que rank se pode
subir. O número do rank 1→2 é **55%** (cap. 90-91). O que NÃO existe é a *tabela
numérica completa* para 3→4 e 4→5: a obra passa a descrever a barreira em termos
qualitativos e de recursos. A wiki não registra nem o mecanismo nem o 55%.

### O que foi verificado, e como

| Verificação | Resultado |
|---|---|
| Busca `insource:/55%/` em `reverend-insanity.fandom.com` | **zero resultados** — a string "55%" não aparece em nenhuma página do wiki |
| Busca `insource:/55%/` em `true-reverend-insanity.fandom.com` | **zero resultados** |
| Busca `insource:/aperture walls.*%/` em ambos | **zero resultados** |
| Páginas https://reverend-insanity.fandom.com/wiki/Rank_1_Gu_Master, .../Rank_2_Gu_Master, .../Rank_3_Gu_Master, .../Rank_4_Gu_Master | **nenhuma porcentagem de qualquer tipo**; todas repetem a mesma frase genérica |
| Página https://reverend-insanity.fandom.com/wiki/Cultivation | **nenhuma porcentagem** de avanço de rank |
| Página https://reverend-insanity.fandom.com/wiki/Primeval_Essence | porcentagens existem, mas são de **condensação e regeneração**, não de limiar de avanço |
| Página https://reverend-insanity.fandom.com/wiki/Fang_Yuan/Cultivation | porcentagens existem, mas são de **capacidade da abertura** (44% → 42/43% → 90%), não de limiar |
| WebSearch (múltiplas formulações, em inglês) por fóruns, SpaceBattles, Sufficient Velocity, compilações de fãs | nenhuma fonte propõe uma progressão numérica |

`[CONFIRMA texto]` **A wiki não contradiz e não estende o dado de 55%.** Ela nem sequer registra o número.

### Por que provavelmente não existe (leitura estrutural das fontes, marcada como interpretação)

`[COMPLEMENTA texto]` — A mecânica descrita pela wiki (mesma frase em todas as páginas de rank, https://reverend-insanity.fandom.com/wiki/Cultivation, **sem citação de capítulo**) é qualitativa, não percentual:

> "Mestres Gu mortais cultivam refinando as paredes da abertura mortal com o auxílio de sua essência primeva. Uma vez que as paredes tenham atingido um certo ponto, não podem mais ser refinadas; nesse momento o Mestre Gu usa sua essência primeva para quebrar e destruir as paredes. As paredes quebradas dão lugar às do próximo realm menor, ou, no caso de subir de rank, às do próximo rank."

E, na página https://reverend-insanity.fandom.com/wiki/Primeval_Essence (também sem citação): "quebrar as paredes da abertura não é feito de uma vez, requer um certo tempo, dependendo do volume de essência primeva usado em cada 'ataque'; por isso é aconselhável gastar a essência primeva num ritmo levemente mais lento que o da regeneração."

Ou seja: o modelo canônico é **acumulação + nutrição + demolição repetida**, não "atingir X% e romper". As porcentagens que a obra e a wiki usam são de **capacidade da abertura** (o teto de aptidão), não de **gatilho de avanço**. Um limiar único de 55% relatado nos caps. 90-92 é, com toda a probabilidade, uma medição de caso — o quanto *aquele* Mestre Gu naquele momento tinha acumulado — e não uma constante do sistema.

**Aviso contra falsa confirmação:** se em algum momento aparecer uma tabela "55% / 65% / 75% / 85%" atribuída à obra, ela deve ser tratada como **fabricação de fã até prova em contrário**. Nenhuma das fontes consultadas nesta pesquisa a sustenta.

### Único dado percentual de avanço que EXISTE nas fontes

`[COMPLEMENTA texto]` Não é um limiar de rank, mas de **realm menor** (estágio): condensar essência primeva de um estágio para o seguinte custa **4:1** — 4% de essência de estágio inicial gera 1% de estágio médio (via Gu como o Liquor Worm). A wiki marca isso como "Based on ch. 29; **unconfirmed**". Fonte: https://reverend-insanity.fandom.com/wiki/Primeval_Essence

---

## 2. Graus de aptidão (talent grades) — faixas numéricas completas

**Fonte:** https://reverend-insanity.fandom.com/wiki/Gu_Master (seção "Grades of Aptitude/Talent")
**Cita capítulo?** NÃO. A tabela da wiki não traz nenhuma referência de capítulo. É compilação/interpretação da wiki a partir de trechos dispersos (o texto em volta cita o Clã Gu Yue e Fang Yuan, mas sem nota de rodapé).

Tabela literal da wiki:

| Talent [Grade] | Aptitude [Grade] | Capacidade máxima de essência primeva na abertura | Informação (tradução) |
|---|---|---|---|
| Extreme | N/A | **100%** | Só existe em Mestres Gu com uma das *ten extreme physiques*. |
| 1st | **A** | **80–99%** | Excepcional; alcança **rank 5** (pico da cultivação mortal) e talvez Gu Imortal com preparação suficiente. |
| 2nd | **B** | **60–79%** | Bom; realm máximo usualmente **rank 3~4**. |
| 3rd | **C** | **40–59%** | Ordinário; realm máximo usualmente **rank 2~3**. |
| 4th | **D** | **20–39%** | O mais fraco; realm máximo usualmente **rank 1~2**. |

Marcação por item:
- `[CONFIRMA texto]` C = 40–59%, B = 60–79%, A = 80–99%. Batem exatamente com o registrado na leitura.
- `[CONFLITA com texto]` **D = 20–39%**, não 20–30%. A leitura anotou "20-30%"; a wiki diz 20–39% (fecha o intervalo contíguo com C a partir de 40%). Divergência registrada, não resolvida — a obra é a autoridade; se a obra em algum capítulo disse 30%, isso prevalece e a wiki está apenas "arredondando" para uma escala contígua de dezenas.
- `[COMPLEMENTA texto]` **O "grau 10 / supremo" não existe com esse nome na wiki.** O que a wiki chama de topo é o grau **"Extreme"** (também "perfect grade" na legenda da imagem da página *Primeval Essence*), reservado às Dez Constituições Extremas, com capacidade **100%**. Não há grade numerada "10".
- `[COMPLEMENTA texto]` **Abaixo de D não existe nada.** A wiki diz explicitamente: "there are only four talent grades" (A, B, C, D). Quem tem menos que isso simplesmente **não tem talento para cultivar** e permanece mortal — não há um "grau E". A wiki dá a estatística: "não é ruim se 5 em cada 10 pessoas tiverem talento para se tornar Mestre Gu"; no Clã Gu Yue a proporção chega a 6 em 10, por causa da purificação de linhagem feita pelo ancestral do clã.
- `[COMPLEMENTA texto]` A wiki ressalva que o grau **não é um teto absoluto**: "mesmo um Mestre Gu com aptidão grau C pode potencialmente se tornar rank 5 e até Gu Imortal". Por isso as colunas usam "usually".
- `[COMPLEMENTA texto]` Aptidão é **mutável**: sobe permanentemente com Blood Skull Gu e Polished Gold Gu; cai permanentemente com ferimentos graves, impurezas prolongadas na abertura, essência primeva alheia, ou Man-Beast Life Burial Gu.
- `[COMPLEMENTA texto]` Detalhe operacional útil (página *Primeval Essence*, sem citação de capítulo): a **velocidade de regeneração** da essência primeva também depende da aptidão — "Fang Yuan, com aptidão grau C, precisa de cerca de uma hora para repor 4% de sua essência primeva; em seis horas recupera 24%".

**Fonte secundária** que replica os mesmos números com a leitura por "camadas da abertura" (D = 2–3 camadas; C = 4–5 camadas, para no rank 2 mas uma pequena porcentagem chega a rank 3 inicial; B = 6–7 camadas, chega a rank 3 e até rank 4): https://true-reverend-insanity.fandom.com/wiki/Gu_Master — também **sem citação de capítulo**.

---

## 3. Lista completa das Ten Extreme Physiques

**Fonte:** https://reverend-insanity.fandom.com/wiki/Ten_Extreme_Physiques
**Cita capítulo?** SIM, e bastante. O infobox lista o capítulo de introdução de cada constituição, e o corpo tem notas de rodapé (ch. 140, 173, 929, 939, 1796, 2113, 2141). A ligação com Ren Zu vem de ch. 131 ("The Legends of Ren Zu").

`[COMPLEMENTA texto]` — **Resultado central: só 8 das 10 têm nome canônico.** As duas restantes (9º filho e 10ª filha de Ren Zu) **nunca foram nomeadas na obra**; a wiki registra "Unknown". Ou seja, a lista "completa" pedida **não existe** — nem na obra, nem na wiki. Isso é resultado, não falha de busca.

| # (filho de Ren Zu) | Constituição | Path associado | Portador(es) | Cap. de introdução |
|---|---|---|---|---|
| 1º (filho) | **Verdant Great Sun** (Grande Sol Verdejante) | desconhecido | desconhecido | ch. 131 |
| 2º (filha) | **Desolate Ancient Moon** (Lua Antiga Desolada) | Tempo | Fairy Lian Xiang | ch. 131 |
| 3º (filho) | **Northern Dark Ice Soul** (Alma de Gelo do Norte Sombrio) | Gelo & Neve / Alma | Bai Ning Bing; o Imortal Zumbi homônimo | ch. 135 |
| 4º (filha) | **Boundless Forest Samsara** (Samsara da Floresta Sem Limites) | desconhecido | desconhecido | ch. 807 |
| 5º (filho) | **Blazing Glory Lightning Brilliance** (Glória Flamejante Brilho do Raio) | Fogo + Raio | Imortal Gu Misterioso de Vestes Negras | ch. 1229 |
| 6º (filha) | **Myriad Gold Wondrous Essence** (Miríade de Ouro Essência Maravilhosa) | desconhecido | You Chan | ch. 1473 |
| 7º (filho) | **Great Strength True Martial** (Grande Força Verdadeiro Marcial) | Força | Hei Lou Lan; Martial Duel Heavenly King; Reckless Savage Demon Venerable (*rumor*, ch. 2113) | ch. 618 |
| 8º (filha) | **Carefree Wisdom Heart** (Coração Sábio Despreocupado) | Sabedoria | Shang Gui Cai; Fairy Ming Hao | ch. 495 |
| 9º (filho) | **— sem nome —** | — | — | — |
| 10º (filha) | **— sem nome —** | — | — | — |
| *(artificial, fora dos dez)* | **Pure Dream Reality Seeker Physique** (Sonho Puro Buscador da Realidade) | Sonho | Ying Wu Xie (antes); Meng Qiu Zhen (ch. 1796) | ch. 1001 |

- `[COMPLEMENTA texto]` A **Pure Dream Reality Seeker Physique NÃO é uma das dez** — a wiki a classifica como "Artificially Created", uma constituição extrema fabricada, não descendente de um filho de Ren Zu.
- `[COMPLEMENTA texto]` Traços mecânicos (fonte cita ch. 140): aptidão **acima de grau A**, teto de 100%; produção de essência primeva muito acima do normal; **a partir do rank 3 a essência primeva nutre as paredes da abertura passivamente**, na velocidade de um Mestre Gu comum cultivando ativamente (e a velocidade passiva cresce com o rank); amplificam Gu do path complementar em +1 rank de efeito (rank 3 com Northern Dark Ice Soul usando Gu de gelo rank 2 gera efeito de rank 3); ao ascender, ganham **super grade blessed land**; **não sofrem a barreira dos grandes realms** ("every large realm had a barrier... but that's not the case with the ten extreme physiques, they can continue to advance without obstacles").
- `[COMPLEMENTA texto]` Desvantagens: a abertura mortal fica sobrecarregada e **pode explodir a qualquer momento**, matando o portador (risco cresce com o rank). Paliativos listados: baixar a aptidão (temporário, ela volta a subir), virar zumbi permanentemente (inibe a cultivação de vez), Everlasting Gu como selo temporário, Stone Aperture Gu (atrasa mas não impede a auto-detonação), Dark Limit Immortal Gu como selo. Calamidades e tribulações muito mais fortes. E precisam ascender com o Immortal Gu apropriado ao seu path (ex.: Great Strength True Martial exige um Immortal Gu de path da Força como vital Gu).
- `[COMPLEMENTA texto]` Trivia com citação (ch. 173): a constituição extrema **não precisa estar presente ao abrir a abertura** — pode surgir gradualmente. Pelos registros antigos do Clã Bai, Mestres Gu com **99% de aptidão correm risco de subir espontaneamente para 100%** conforme cultivam.
- **Atenção a um falso positivo:** a busca no wiki retorna também uma página "Righteous Virtue Physique". Ela **não** aparece na tabela das Dez Constituições Extremas e não deve ser contada entre elas (verificar caso a caso; não confirmado como constituição extrema).

---

## 4. Lista canônica dos paths e seus criadores

**Fonte:** https://reverend-insanity.fandom.com/wiki/Dao (seção "Paths"; a página `.../wiki/Path` é um redirect para cá)
**Cita capítulo?** Parcialmente. A seção tem notas de rodapé para afirmações gerais (ch. 752, 1064, 1465, 2089), mas **as descrições individuais dos paths não têm citação por linha** — são sínteses da wiki.

`[COMPLEMENTA texto]` **Advertência importante antes da lista: a obra não tem uma lista canônica fechada de paths.** A própria wiki explica por quê: "com cada geração que passa, paths velhos e obsoletos declinam e são esquecidos"; paths novos surgem (Killing path é "brand new... created in Great Era"; Pill path e Weapon path são "newly emerging"). Portanto qualquer lista é um **retrato do momento narrativo**, não um cânone fixo. A lista abaixo é a da wiki (44 paths principais + 4 sub-paths).

**44 paths principais (ordem alfabética da wiki, nomes em inglês):**

Blade · Blood · Bone · Cloud · Dark · Dream · Earth · Enslavement · Fire · Food · Formation · Heaven · Human · Ice · Illusion · Information · Killing · Light · Lightning · Luck · Metal · Moon · Painting · Pill · Poison · Qi · Refinement · Rule · Shadow · Snow · Soul · Sound · Space · Star · Strength · Sword · Theft · Time · Transformation · Water · Weapon · Wind · Wisdom · Wood

**Sub-paths declarados:**
- de **Rule**: **Phantom** (fantasmas/aparições, entre verdade e falsidade; permite atravessar objetos sólidos e ataques) e **Restriction** (regras que restringem)
- de **Wisdom**: **Emotion** (cria emoções — moral de aliados, inibição no inimigo) e **Enchantment** (afeição/encanto; cultivadores descritos como belos além do padrão)
- **Weapon** engloba **Blade** e **Sword** (a wiki lista os três como paths separados e ao mesmo tempo diz que Weapon "includes blade path and sword path" — inconsistência da própria wiki, registrada aqui)

**Hierarquias declaradas com citação de capítulo:**
- `[COMPLEMENTA texto]` (ch. 752) — "Metal, wood, water, fire, earth: esses são os cinco paths mais mainstream, mais populares até que cloud path e sound path. Strength path e qi path são bem menos."
- `[COMPLEMENTA texto]` (ch. 1064) — "Metal path, fire path, lightning path, sword path, blood path: esses cinco são publicamente reconhecidos como os paths de maior poder de combate."
- `[COMPLEMENTA texto]` A wiki distingue **major paths** (uso amplo) de **minor paths** (menos desenvolvidos/populares — cita Shadow e Sound como minor). Critério para algo ser "path": precisa ter uma direção clara (um elemento, um aspecto da realidade, um efeito específico) **e** cobrir os aspectos básicos — ataque, defesa, cura, movimento, armazenamento e investigação.
- `[COMPLEMENTA texto]` Space path e Time path são citados como **os dois primeiros paths cultivados** por Mestres Gu.

### Paths com criador nomeado

**Fontes:** as páginas individuais de cada path em `https://reverend-insanity.fandom.com/wiki/<Nome>_Path` (ex.: `.../wiki/Qi_Path`, `.../wiki/Rule_Path`). O infobox de cada uma tem um campo **"Creator"**. **Cita capítulo?** Em geral **não** para a atribuição do criador; algumas páginas têm notas de rodapé para pontos laterais (Food Path cita fonte para a fundação; Soul Path cita ch. para a origem via Black Heaven's Heavenly Spirit).

Nomenclatura das eras usada pela wiki: 1ª = *Immemorial Antiquity*; 2ª = *Remote Antiquity*; 3ª = *Olden Antiquity*; 4ª = *Medieval Antiquity*; 5ª = *Late Antiquity*; 6ª = *Current Era / Great Era*.

| Path | Criador | Era |
|---|---|---|
| **Human** | **Ren Zu** ("said to be founded by Ren Zu himself" — a wiki usa "said to be", tratar como lenda interna) | pré-histórica |
| **Time** | **nenhum nomeado** — um dos dois primeiros paths, cultivado desde a Antiguidade Imemorial (1ª era) | 1ª |
| **Space** | **nenhum nomeado** — o outro dos dois primeiros paths, desde a 1ª era | 1ª |
| **Qi** | **Primordial Origin Immortal Venerable** | 2ª |
| **Enslavement** | **Primordial Origin Immortal Venerable** | 2ª |
| **Wisdom** | **Star Constellation Immortal Venerable** | 2ª |
| **Star** | **Star Constellation Immortal Venerable** | 2ª |
| **Refinement** | **nenhum nomeado** — "fundado durante a Antiguidade Remota". Thieving Heaven fundou apenas o *aspecto* de refinar Gu falsos | 2ª |
| **Rule** | **Limitless Demon Venerable** | 3ª |
| **Strength** | **Reckless Savage Demon Venerable** | 3ª |
| **Transformation** | **Reckless Savage Demon Venerable** | 3ª |
| **Food** | **um Imortal Gu Beastman não nomeado** | 3ª |
| **Earth** | **nenhum nomeado** — "fundado e desenvolvido durante a Antiguidade Medieval" | 4ª |
| **Wood** | **Genesis Lotus Immortal Venerable** | 4ª |
| **Painting** | **Genesis Lotus Immortal Venerable** (mantido em segredo como seu path de especialidade) | 4ª |
| **Theft** | **Thieving Heaven Demon Venerable** | 4ª |
| **Luck** | **Giant Sun Immortal Venerable** (desenvolveu a partir de <<The Legends of Ren Zu>>, criando *All Living Beings Luck* e *Heaven and Earth Luck*) | 4ª |
| **Blood** | **Blood Sea Ancestor** | era não especificada |
| **Soul** | **Spectral Soul Demon Venerable** | 5ª |
| **Killing** | **Spectral Soul Demon Venerable** (já enlouquecido) | 6ª |
| **Pill** | **Ruan Dan**, uma Fera Desolada Imemorial ligada à Heavenly Court | 6ª |
| **Weapon** | **Che Wei** | 6ª |
| **Heaven** | **nenhum criador nomeado** — só se sabe que foi cultivado por Limitless Demon Venerable, Paradise Earth Immortal Venerable e depois Fang Yuan | — |
| **Dream** | **nenhum criador nomeado**; path descrito como "incompleto"/emergente | 6ª |
| todos os demais (Blade, Bone, Cloud, Dark, Fire, Formation, Ice, Illusion, Information, Light, Lightning, Metal, Moon, Poison, Shadow, Snow, Sound, Sword, Water, Wind) | **sem criador nomeado nas fontes consultadas** | — |

**Achados analíticos importantes:**

- `[COMPLEMENTA texto]` Contagem: **~16 paths têm criador nomeado**; ~28 não têm. A regra "cada Venerável criou seu path" é **aproximada, não absoluta**.
- `[CONFLITA com texto]` A trivia da página *Venerable* afirma "a maioria dos Veneráveis criou e foi pioneira em seu path principal". Cruzando com as páginas de path, isso **falha em pelo menos três casos**:
  - **Red Lotus Demon Venerable** — path principal **Tempo**, mas Time path existe **desde a 1ª era**, muito antes dele. Ele é o *Dao Lord* do tempo, **não o criador**.
  - **Paradise Earth Immortal Venerable** — path principal **Terra**, mas a wiki data a fundação do Earth path na **Antiguidade Medieval (4ª era)**, enquanto ele é da **Antiguidade Tardia (5ª)**. Também Dao Lord, não criador.
  - **Fang Yuan** (11º) — path principal **Refinamento**, fundado na **2ª era**.
  - Ou seja: **ser Dao Lord de um path ≠ ter criado o path.** Distinção estrutural que vale registrar.
- `[COMPLEMENTA texto]` A própria wiki registra um **furo de continuidade** que ela mesma aponta (nas páginas *Soul Path*, *Wisdom Path* e *Enslavement Path*): dizem que Spectral Soul "inventou" o Soul path na 5ª era, mas o Enslavement path (que depende de fundação de alma) já existia desde a 2ª era, fundado por Primordial Origin — "e é até possível que tenha sido inventado antes de Star Constellation fundar o Wisdom path". Anotado como inconsistência conhecida, **não** resolvida.
- `[COMPLEMENTA texto]` Origem do Soul path segundo a página (atribuída a Star Constellation Immortal Venerable, com nota de rodapé): Spectral Soul o fundou após captar profundidades obtidas ao devorar o Espírito Celestial de Black Heaven — **e só porque falhou em criar o Killing path** primeiro. O Killing path só veio depois, na 6ª era, quando ele já estava insano.
- `[COMPLEMENTA texto]` **Qi path está em declínio** na era atual, sendo substituído pelo Strength path — que por sua vez também já está em declínio.

---

## 5. Os 10 (11) Veneráveis

**Fonte:** https://reverend-insanity.fandom.com/wiki/Venerable
**Cita capítulo?** SIM, para as mecânicas (ch. 1844, 2085, 2209, 2240, 2260, 2267) e para o caso do Giant Sun. A tabela de paths por Venerável **não tem citação por linha**.

`[CONFIRMA texto]` **A lista dos dez históricos, confirmada, com raw chinês, path principal, especialidade, paths menores e era:**

| # | Raw | Nome | Path principal | Especialidade | Menores | Era |
|---|---|---|---|---|---|---|
| 1 | 元始仙尊 | **Primordial Origin Immortal Venerable** | Qi | Escravização (Enslavement) | Humano | Antiguidade Remota (*Remote Antiquity*, começa há ~3 milhões de anos) |
| 2 | 星宿仙尊 | **Star Constellation Immortal Venerable** | Sabedoria (Wisdom) | Estrela (Star) | Formação & Refinamento | Antiguidade Remota |
| 3 | 无极魔尊 | **Limitless Demon Venerable** | Regra (Rule) | Céu (Heaven) | — | Antiguidade Antiga (*Olden Antiquity*, começa há ~1 milhão de anos) |
| 4 | 狂蛮魔尊 | **Reckless Savage Demon Venerable** | Força (Strength) | Transformação | Sabedoria | Antiguidade Antiga |
| 5 | 红莲魔尊 | **Red Lotus Demon Venerable** | Tempo (Time) | — | — | Antiguidade Antiga |
| 6 | 元莲仙尊 | **Genesis Lotus Immortal Venerable** | Madeira (Wood) | Pintura (Painting) | Humano | Antiguidade Medieval (*Medieval Antiquity*, começa há ~300 mil anos) |
| 7 | 盗天魔尊 | **Thieving Heaven Demon Venerable** | Roubo (Theft) | Espaço | Refinamento | Antiguidade Medieval |
| 8 | 巨阳仙尊 | **Giant Sun Immortal Venerable** | Sorte (Luck) | Sangue (Blood) | Humano | Antiguidade Medieval |
| 9 | 幽魂魔尊 | **Spectral Soul Demon Venerable** | Alma (Soul) | Comida (Food) | Matança e outros | Antiguidade Tardia (*Late Antiquity*, começa há ~100 mil anos) |
| 10 | 乐土仙尊 | **Paradise Earth Immortal Venerable** | Terra (Earth) | Céu (Heaven) | Formação & Veneno | Antiguidade Tardia |

**Sobre Great Dream — `[CONFIRMA texto]`, com nuance importante:**
- 大梦仙尊 **Great Dream Immortal Venerable** (path do Sonho) aparece na tabela da wiki como **#11 previsto**, da Era Atual/Grande Era — **NÃO como um dos dez históricos**. A wiki diz literalmente: "The future eleventh Venerable was destined to be Great Dream Immortal Venerable... However, ever since the destruction of Fate Gu, the future position of the eleventh Venerable became vacant to all rank 8 Gu Immortals." E na trivia: "The destined Great Dream Immortal Venerable in Fang Yuan's first life never came into existence, as she (Feng Jin Huang) was plotted against by Shadow Sect and ultimately killed."
- Ou seja: **Great Dream é um destino não realizado**, não um Venerável histórico. Confirmação limpa da leitura.
- O 11º Venerável que **de fato** existe é **Fang Yuan** — 炼天魔尊 **Heaven Refining Demon Venerable** (título dado) / 大爱仙尊 **Great Love Immortal Venerable** (título assumido): path principal Refinamento, especialidade Céu, menores Tempo & Escravização e outros. Alcançado após atingir Supreme Grandmaster em refinamento e cruzar a Chaos Tribulation.

**Legado estrutural — `[COMPLEMENTA texto]`, o mecanismo que a obra explicita:**
- **Dao Lord:** ao virar Venerável com attainment Supreme Grandmaster, o indivíduo se torna o *senhor* daquele path — a melhora dele **é** a melhora do path, e portanto do céu e da terra. Como Dao Lord ele **sente e refina todas as dao marks naturais daquele path em toda a heaven and earth** e depois as manipula à vontade. O período em que todo Venerável "vagueia pelo mundo" após ascender é, na verdade, o refinamento dessas dao marks naturais: eles transformam o mundo inteiro em killer move pessoal. **Esse é o segredo da invencibilidade dos Veneráveis.** Por conflito de dao marks, **um Venerável só pode ser Dao Lord de um path** (ch. 2240, 2267). E precisam manter o refinamento de *todas* as dao marks naturais do mundo para sustentar o nível Supreme Grandmaster.
- **Main path + specialty path:** os Veneráveis cultivavam um path principal (que espalhavam amplamente) e um path de especialidade **mantido em segredo**, com informação lacrada, para que no futuro houvesse poucas contramedidas e os métodos continuassem eficazes. Legado estrutural direto: por isso os paths principais viraram mainstream. Trivia da wiki: "A maioria dos Veneráveis criou e foi pioneira em seu path principal, o que por sua vez o tornou um path mainstream cultivado por muitos depois."
- **Caso especial do Giant Sun:** a wiki nota (com justificativa) que ele **planejava** ter Sangue como principal e Sorte como especialidade, mas após o renascimento continuou sendo Dao Lord de **Sorte** e lutando com métodos de sorte, porque o blood path não estava avançado o suficiente e suas dao marks de sangue eram recentes/poucas. Os métodos de sangue ficaram reservados para revivificação. **Isso é uma inversão em relação à tabela** — registrar como ponto de atenção.
- **Ressalva da wiki sobre Spectral Soul:** nunca foi *completamente* confirmado se o attainment dele em Sword Path chegou a Supreme Grandmaster; o argumento é indireto (sua Split Soul Bo Qing, imortal de sword path, tentou avançar a rank 9, o que exige Supreme Grandmaster) e a wiki mesma nota que o attainment de Bo Qing é independente do corpo principal. Marcar como **inferência da wiki**, não fato da obra.

**Condições de ascensão a rank 9 — `[COMPLEMENTA texto]` (fonte cita ch. 2085):**
1. O núcleo da abertura deve produzir **essência imortal rank 8, white litchi**;
2. Possuir **pelo menos 300.000 dao marks** do path principal;
3. Atingir pelo menos **Supreme Grandmaster attainment** no path principal;
4. Cumpridos os três, **romper o bloqueio do Dao** para transformar o núcleo da abertura.

O "bloqueio do Dao" tem três partes: uma **tribulação suprema**; a **queda na produção de Lifespan Gu** durante a era de um Venerável (o Céu reduz de propósito para o Venerável não viver "demais"); e os ditames da Vontade do Céu via **Fate Gu**. Historicamente romperam por sorte enorme vinda do human path (caso do Red Lotus) ou por bênção da Vontade do Céu (caso do Primordial Origin).

**Restrições de quem pode ser Venerável — `[COMPLEMENTA texto]`:**
- Só **humanos**. Humanos variantes e feras conseguem chegar no máximo a **rank 8**. Há um "grande segredo" na ascensão a rank 9 que barra imortais humanos variantes (ch. 1844); muitos ficam presos em pico de rank 8 mesmo após passar a tribulação final de rank 8.
- Antes de Red Lotus danificar o **Fate Gu**, só quem estava *fadado* a ser Venerável podia sê-lo.
- Todo Venerável é acompanhado de um **Dao Guardian** (ch. 2085).
- Rank 9 (imortais e Immortal Gu) sofre a inveja da Vontade do Céu e **não pode viver para sempre** — por isso em toda a história humana só houve 11 Veneráveis, todos limitados por lifespan; e existem pouquíssimos Immortal Gu rank 9 (ch. 2260).
- Um Venerável enfrenta **a cada 100 anos** um desastre caótico originado de **fora da fronteira do mundo** (ch. 2209).
- **Título:** o sufixo **Immortal Venerable** vai para o justo, **Demon Venerable** para o cruel/impiedoso — atribuição que depende da opinião do povo e da Heavenly Court. O prefixo único costuma vir do path com que se alcançou rank 9, da natureza da pessoa, ou de algo singular dela.

---

## 6. Rankings de Gu supremos: "Ten Big Mystical Gu" × "Top Ten Great Immortal/Demonic Gu" × "sete Gu misteriosos"

**Fonte:** https://reverend-insanity.fandom.com/wiki/Gu (seção "Top 10 Gu"), mais as páginas individuais de cada Gu.
**Cita capítulo?** A seção "Top 10 Gu" tem **uma única** nota de rodapé (ch. 1903, para a colocação omitida do Response Gu). As três tabelas em si **não têm citação de capítulo**.

### Resposta à pergunta central

`[COMPLEMENTA texto]` — São **duas coisas diferentes**, e a terceira é provavelmente um mal-entendido:

1. **"Ten Big Mystical Gu" = "Top Ten Mystical Gu" = "List of Mystical Gu"** — **a MESMA lista**, apenas traduzida de formas diferentes (o wiki usa as três grafias em páginas distintas: a página *Qi Escape Gu* diz "top ten Big Mystical Gu rankings", a *Star Eyes* diz "Top Ten Mystical Gu rankings", a *Imitation Gu* diz "List of Mystical Gu"). Não são listas separadas.
2. **"Top Ten Great Immortal Gu" e "Top Ten Great Demonic Gu"** — a wiki as trata como **DUAS listas adicionais e distintas** da lista dos Mystical Gu, cada uma com sua própria tabela de 10 posições. Ambas estão quase inteiramente vazias ("Unknown").
3. **"Sete Gu misteriosos"** — **não encontrado como lista própria.** Nenhuma fonte consultada tem uma lista de sete. As explicações plausíveis (marcadas como **interpretação, não fato**): (a) confusão com a colocação **7ª** do Spring Autumn Cicada na lista dos Mystical Gu antes de ser reclassificado; (b) contagem parcial — só ~7 das 10 posições da lista dos Mystical Gu têm nome conhecido na obra.

### Lista 1 — Top Ten Mystical Gu (十大奇蛊 / "Ten Big Mystical Gu")

A wiki nota: "A lista dos Gu místicos mudava constantemente e o top 10 raramente era ajustado. A maioria dos 10 primeiros está relacionada aos Veneráveis de rank 9."

| # | Gu | Criado por | Colocação anterior |
|---|---|---|---|
| 1º | **Stare Pregnancy Gu** ⚠ | Giant Sun Immortal Venerable | — |
| 2º | *desconhecido* | — | — |
| 3º | **Spring Autumn Cicada** | Red Lotus Demon Venerable | era 7º |
| 4º | **Care Immortal Gu** | Limitless Demon Venerable | era 3º |
| 5º | **Qi Escape Gu** ⚠ | Kong Sheng Tian | — |
| 6º | **Combat Relocation Gu** | Paradise Earth Immortal Venerable | — |
| 7º | **Connect Mind Gu** | Star Constellation Immortal Venerable | — |
| 8º | **Imitation Gu** | Thieving Heaven Demon Venerable | — |
| 9º | *desconhecido* | — | — |
| 10º | **Star Eyes Immortal Gu** | desconhecido | — |
| *sem colocação* | **Response Gu** (está no top 10, mas a posição é omitida — ch. 1903) | desconhecido | — |

**Duas divergências que precisam ser sinalizadas:**

- `[CONFLITA com texto]` **Qi Escape Gu — 4º ou 5º?** A tabela da página *Gu* põe Qi Escape Gu em **5º**. Mas a própria página https://reverend-insanity.fandom.com/wiki/Qi_Escape_Gu diz "famoso por ser **ranqueado quatro** no top ten Big Mystical Gu" — e, decisivamente, **o título do capítulo 678 da obra é literalmente "Number Four in the List of Mystical Gu"** (verificável nos índices públicos do webnovel). Ou seja: **a obra diz 4º; a tabela da wiki diz 5º.** Como a lista muda ao longo do tempo (Care Immortal Gu explicitamente caiu de 3º para 4º), é possível que as duas estejam corretas em momentos diferentes — mas a wiki não datou nenhuma delas. **Prevalece a obra: 4º no momento do cap. 678.**
- ⚠ `[CONFLITA com texto]` **"Stare Pregnancy Gu" em 1º é suspeito.** Esse nome **não tem página no wiki**, **não aparece na página do Giant Sun Immortal Venerable** (que lista como Gu dele: Connect Luck Gu, Break Luck Gu, Divert Disaster Gu, Calamity Beckoning Gu, **Fortune Rivalling Heaven Gu** e Qi Luck Immortal Gu) e **não aparece em nenhuma outra página do wiki**. Aparece **só nessa célula de tabela, sem citação**. Fontes de fã concorrentes (compilação "Gu world encyclopedia for fanfic writers", em webnovel.com) afirmam que o **1º é Fortune Rivalling Heaven Immortal Gu** — o Gu vital tardio do Giant Sun, ápice da inheritance *All Living Beings Luck*. Nenhuma das duas versões tem citação de capítulo. **Marcar como não resolvido**; a versão "Fortune Rivalling Heaven" é a mais coerente com o resto do wiki, mas isso é inferência.

### Lista 2 — Top Ten Great Immortal Gu

Praticamente vazia na wiki. **Única entrada preenchida:**

| # | Gu | Criado por |
|---|---|---|
| 6º | **Heavenly Essence Treasure Imperial Lotus** | Genesis Lotus Immortal Venerable |
| 1º–5º, 7º–10º | *desconhecidos* | — |

(Sobre esse Gu: é a forma rank 6 do *Heavenly Essence Treasure Lotus*, um Gu de wood path que funciona como Spirit Spring portátil, produzindo ~50 Primeval Stones por dia na versão rank 3; introduzido no ch. 162. Fonte: https://reverend-insanity.fandom.com/wiki/Heavenly_Essence_Treasure_Lotus_Gu)

### Lista 3 — Top Ten Great Demonic Gu

Também praticamente vazia. **Duas entradas:**

| # | Gu | Criado por |
|---|---|---|
| 7º | **Blood Deity Immortal Gu** | Blood Sea Ancestor |
| 8º | **Imitate Gu** (imita a função dos Gu alheios) | desconhecido |
| demais | *desconhecidos* | — |

(Blood Deity: mencionado no ch. 165, "ranqueado 7º entre os 'Top Ten Great Demonic Gu' do Mundo Gu". Fonte: https://reverend-insanity.fandom.com/wiki/Blood_Deity)

`[COMPLEMENTA texto]` **Nota de cautela:** o 8º dos Great Demonic Gu, "Imitate Gu", e o 8º dos Mystical Gu, "Imitation Gu" (de Thieving Heaven), são nomes quase idênticos ocupando a mesma posição em listas diferentes. Pode ser (a) duplicação editorial no wiki, (b) dois Gu genuinamente distintos com nomes parecidos na tradução. **Não resolvido** — verificar na obra.

### Conclusão operacional para o texto

Três listas nominalmente distintas; **apenas a dos Mystical Gu está minimamente povoada** (7 de 10 nomeados, com 1 posição adicional omitida). As outras duas existem no cânone como *conceito* mas a obra revelou pouquíssimas entradas. Não há lista de sete.

---

## 7. Cores/qualidades da essência primeva e imortal por rank

**Fontes:**
- https://reverend-insanity.fandom.com/wiki/Primeval_Essence (ranks 1–5, mortal)
- https://reverend-insanity.fandom.com/wiki/Immortal_Essence (ranks 6–9, imortal)

**Cita capítulo?** A tabela de cores **não** tem citação por linha. As taxas de condensação têm citação **explicitamente marcada como não confirmada** pela própria wiki ("Based on ch. 26; unconfirmed", "Based on ch. 29; unconfirmed"). A página *Immortal Essence* cita ch. 374 (menção) e ch. 377 (aparição real). O uso de essência de estágio médio vs. inicial no Moonlight Gu cita ch. 35.

### Mortal — ranks 1 a 5, com os quatro estágios menores de cada

| Rank | Cor do grande realm | Inicial | Médio | Superior | Pico |
|---|---|---|---|---|---|
| 1 | **Green Copper** (cobre verde) | Jade Green | Pale Green | Dark Green | Black Green |
| 2 | **Red Steel** (aço vermelho / ferro vermelho) | Light Red | Scarlet Red | Crimson Red | Dark Red |
| 3 | **White Silver** (prata branca) | Light Silver | Blossom Silver | Bright Silver | Snow Silver |
| 4 | **Yellow Golden** (dourado amarelo) | Light Gold | Bright Gold | Essence Gold | True Gold |
| 5 | **Purple Crystal** (cristal púrpura) | Light Purple | Violet Purple | Deep Purple | Crystal Purple |

- `[COMPLEMENTA texto]` A wiki nota na tradução que "red steel" e "red iron" são usados **de forma intercambiável** — mesma coisa.
- `[COMPLEMENTA texto]` A essência primeva de um Mestre Gu recém-desperto é descrita como água do mar lisa como espelho, verde-azulado denso, com lustro de cobre.
- `[COMPLEMENTA texto]` No wikitext bruto da página há duas linhas soltas: "After Crystal Purple is **Bronze with Gold Glint**" e "After Bronze with Gold Glint is **Yellow as Emperors Heaven**". Elas **não aparecem na tabela renderizada** e não têm citação — são anotações de editor. Tratar como **não confirmado**; não conflitam com a lista de essência imortal porque parecem descrever outra escala (possivelmente qualidade de pedra/essência acima de rank 5). Registrar como pendência.

### Imortal — ranks 6 a 9

| Rank | Essência imortal | Cor/qualidade | Taxa de conversão |
|---|---|---|---|
| 6 | **Green Grape** (uva verde) | verde translúcido em contas, com cheiro de ferrugem | base |
| 7 | **Red Date** (tâmara vermelha) | — | 1 conta = 100 contas de uva verde |
| 8 | **White Litchi** (lichia branca) | — | 1 conta = 100 contas de tâmara vermelha |
| 9 | **Yellow Apricot** (damasco amarelo) | — | 1 conta = 100 contas de lichia branca |

- `[COMPLEMENTA texto]` Ao ascender a rank 6 a abertura mortal vira **abertura imortal** e **para de produzir essência primeva**, passando a produzir contas de essência imortal. A quantidade recebida na ascensão e a produção mensal dependem do **grau da blessed land / grotto-heaven** e da "força vital" e qualidade dos recursos dentro dela. Blessed lands "caídas" de imortais mortos **não produzem nada**.
- `[COMPLEMENTA texto]` **Só o próprio Gu Imortal que produziu a essência pode usá-la** para ativar seus Immortal Gu. Exceção: **immortal Gu Houses**, que podem ser abastecidas com essência de outro imortal.
- `[COMPLEMENTA texto]` Usar Immortal Gu de rank acima do seu funciona, mas com **gasto intensificado**: um imortal rank 6 ativando um Immortal Gu rank 7 que custa 1 conta de tâmara vermelha gasta **130** (não 100) contas de uva verde.
- `[COMPLEMENTA texto]` Uma conta de essência imortal pode ser **diluída em essência primeva quase infinita** para uso de Gu mortais. O contrário não é possível. Immortal essence stones convertem em contas (1 pedra = 1 conta de uva verde), mas contas não convertem de volta em pedras.

### Taxas de condensação entre ranks e estágios (marcadas como NÃO CONFIRMADAS pela wiki)

- **Entre grandes realms** (baseado em ch. 26, *unconfirmed*): 1 porção de essência de rank n+1 ≈ 10 porções de rank n. Ex.: 1 porção de rank 3 inicial ≈ 10 porções de rank 2 pico ≈ 10.000 porções de rank 1 pico. A própria wiki ressalva: "não está claramente afirmado que uma porção de estágio *inicial* equivale a 10 porções de estágio *pico* do rank anterior".
- **Entre estágios menores** (baseado em ch. 29, *unconfirmed*): condensar exige **4:1** por degrau — 4% de essência de estágio inicial condensa 1% de estágio médio (via Gu como o Liquor Worm). Acumulado: inicial→médio 400%; inicial→superior 1600%; inicial→pico 6400%.

---

## Apêndice — achado lateral útil: ciclo de calamidades e tribulações por rank imortal

**Fonte:** https://reverend-insanity.fandom.com/wiki/Cultivation — **sem citação de capítulo** para a tabela.

| Rank | A cada 10 anos | A cada 50 anos | A cada 100 anos | Condição de avanço |
|---|---|---|---|---|
| 6 | Calamidade Terrestre | — | Tribulação Celeste | Após 300 anos (tempo de abertura) e 3 tribulações celestes bem-sucedidas → rank 7 |
| 7 | Calamidade Terrestre | Tribulação Celeste | Grande Tribulação | Após 300 anos e 3 grandes tribulações → rank 8 |
| 8 | Tribulação Celeste | Grande Tribulação | Tribulação Miríade | Após 300 anos e 3 tribulações miríade (as 2 primeiras vencidas), antes da última → **pico de rank 8** (poder de "meio-Venerável") |
| 9 | Grande Tribulação | Tribulação Miríade | **Tribulação do Caos** | — |

- `[COMPLEMENTA texto]` Gu Imortais **não** têm mais os 4 realms menores. A potência de um imortal se mede por **quantas calamidades e tribulações** já atravessou: ex., um rank 6 que passou 2 tribulações celestes e 27 calamidades terrestres é considerado pico de rank 6.
- `[COMPLEMENTA texto]` Ao chegar a **rank 8**, a blessed land vira **grotto-heaven**, e a obsessão do imortal toma a forma de um **espírito celestial** após sua morte.
- `[COMPLEMENTA texto]` **Rank 10 não existe**: "rank nove é o limite do mundo inteiro, é o cume mais alto, este mundo não pode ter rank dez, então rank nove é o mais forte."
- `[COMPLEMENTA texto]` Média de dao marks por rank (a página *Dao* cita **ch. 2071**): rank 6 → 0 a 9.000; rank 7 → 10.000 a 30.000; rank 8 → 100.000 a 300.000. "Fora aberrações como Fang Yuan, Feng Jiu Ge e os Veneráveis passados." Cruza com a exigência de **300.000 dao marks** para rank 9 (ch. 2085): ou seja, o teto médio de rank 8 é exatamente o piso de entrada para Venerável.
- `[COMPLEMENTA texto]` Ascensão mortal→imortal (três qi): céu + terra (devem ser **iguais entre si**) + humano (soma da acumulação pessoal: força de combate, resistência do corpo, profundidade da alma, familiaridade com Gu, entendimento do céu e da terra, consciência da própria natureza, sorte, talento, aptidão, encontros fortuitos, insights). Desbalanceou, morre e a alma se dissipa. Durante a ascensão, com uma pergunta específica formulada, obtém-se a **inspiração do céu e da terra** (ch. 647) — pergunta vaga gera resposta vaga. Recomenda-se ascender só com o vital Gu já em rank 5. Qi de céu e terra excedente refina um ou mais Gu mortais rank 5 em Immortal Gu.
- `[COMPLEMENTA texto]` Graus de abertura imortal (fonte: https://true-reverend-insanity.fandom.com/wiki/Gu_Master, **sem citação**): low / medium / high / perfect, correspondendo a blessed lands small / medium / large / **super**. A super grade tem 6.700 a <13.000 km², puxa um afluente gigantesco do Rio do Tempo com fluxo temporal **1:40**, forma **mais de 50** contas de essência imortal por ano e sobra qi para refinar pelo menos dois Immortal Gu. Portadores de constituição extrema recebem sempre super grade.

---

## Resumo do que ficou EM ABERTO (para não ser reinventado depois)

1. **Limiares percentuais de rank 2→3, 3→4, 4→5:** não existem em nenhuma fonte. Tratar como inexistentes.
2. **Nomes da 9ª e da 10ª constituições extremas:** nunca revelados na obra.
3. **1ª posição da lista dos Mystical Gu:** disputada — "Stare Pregnancy Gu" (wiki, sem citação e sem página própria) vs. "Fortune Rivalling Heaven Gu" (compilação de fã, sem citação).
4. **Posição do Qi Escape Gu:** 4º (obra, título do cap. 678) vs. 5º (tabela da wiki).
5. **9 de 10 posições dos "Top Ten Great Immortal Gu" e 8 de 10 dos "Great Demonic Gu":** nunca reveladas.
6. **"Bronze with Gold Glint" e "Yellow as Emperors Heaven"** (linhas soltas no wikitext da página *Primeval Essence*): a que escala pertencem? Não confirmado.
7. **Criador do Time path, do Space path, do Refinement path, do Earth path e do Heaven path:** nunca nomeado.
8. **"Imitate Gu" vs "Imitation Gu":** mesmo Gu duplicado em duas listas, ou dois Gu distintos?
