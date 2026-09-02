# Auditoria de completude — `03 - Paths/`

**Data:** 2026-09-02 · **Escopo:** todas as notas de `03 - Paths/`.
**Pergunta de partida:** a pasta tem 17 caminhos com nota própria, mas o
`10 - Apendices/08 - Catálogo de Golpes - Imortais.md` organiza os golpes em ~35 caminhos.
Quantos caminhos a obra realmente nomeia, e quais ficaram sem cobertura?

**Método:** cruzamento de quatro fontes —
(a) varredura do texto-fonte com `grep -hioE "\b[a-z]+ path\b"` nos seis volumes, com
contagem de ocorrências e leitura de contexto para descartar falsos positivos;
(b) os cabeçalhos de caminho dos dois catálogos de golpes (`10 - Apendices/07` e `08`);
(c) `_pipeline/rascunho/paths.md`;
(d) **a enumeração canônica do cap. 1323**, que é a espinha dorsal desta auditoria (ver abaixo).

---

## O achado que reorganiza o domínio: a enumeração canônica do cap. 1323

A obra tem **uma passagem que enumera os caminhos principais por era de criação**, em forma
de aula. Ela estava citada no campo `fontes` da `01 - Visão Geral dos Paths.md`, mas o seu
conteúdo — a lista e a cronologia — **não estava aproveitado em lugar nenhum da pasta**.
Transcrição resumida (cap. 1323, um Imortal do caminho das formações ensinando o filho):

> - **Antiguidade Imemorial (era de Ren Zu):** *space path* e *time path* — "estes dois
>   caminhos pesquisaram e expuseram as profundidades do tempo e do espaço".
> - **Antiguidade Remota:** Primordial Origin criou *qi path* e *enslavement path*;
>   Star Constellation criou *wisdom path* e *star path*; *formation path* nasceu no período
>   tardio da era, com fundador não verificável; *refinement path* e *fire path* também.
> - **Antiguidade Passada (Olden Antiquity):** Limitless Demon Venerable criou *rule path*;
>   Reckless Savage criou *transformation path*; *strength path*, *wind path*, *light path*
>   e *dark path* também nasceram aqui.
> - **Antiguidade Medieval:** Genesis Lotus criou *wood path*; Thieving Heaven criou
>   *theft path*; Giant Sun criou *luck path*; e surgiram *metal path*, *water path*,
>   *ice and snow path*, *cloud path*, *earth path*, *lightning path*, *information path*
>   e *sound path* — "uma era em que todo tipo de caminho diverso apareceu".
> - **Era atual (Antiguidade Tardia em diante):** criou-se *bone path*; existem também
>   *phantom path* e *restriction path*.
> - E o encerramento decisivo: *"o que mencionei são apenas os caminhos **principais** de
>   Mestres Gu; caminhos menores como **enchantment path**, **illusion path** e outros ficam
>   omitidos por ora."*

Três consequências para o vault:

1. **A obra distingue formalmente caminhos principais de caminhos menores.** Essa distinção
   não existia em nenhuma nota da pasta e é a chave de organização correta do domínio.
2. **A lista de "mainstream" do cap. 1323 tem 25 caminhos** — e sete deles não tinham nota:
   qi, formation, wind, light, dark, wood, metal, water, ice-and-snow, cloud, earth,
   lightning, information, sound, theft, bone, phantom, restriction (dezoito, na verdade).
3. **A cronologia por era é canônica e estava perdida.** Ela responde sozinha a pergunta
   "de onde vêm os caminhos" que a `01 - Visão Geral` levanta e deixa em aberto.

---

## Inventário de caminhos da obra

`Ocorr.` = número de linhas-parágrafo distintas dos seis volumes que contêm a expressão
`<nome> path` (com `grep -i`, deduplicado). É uma medida de **massa textual disponível**,
não de importância no mundo.

*(tabela preenchida ao longo da auditoria — ver seções seguintes)*

