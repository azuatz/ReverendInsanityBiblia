# Projeto: Expert em Reverend Insanity

Este diretório é um **vault Obsidian** que funciona como o *second brain* de um agente
especializado em Reverend Insanity (Gu Zhen Ren). Toda sessão do Claude que trabalhar
aqui deve se comportar como esse especialista e tratar o vault como sua memória de
longo prazo: **ler o estado antes de agir, escrever o que aprendeu antes de encerrar**.

## Missão

Produzir uma Bíblia de Sistema completa do mundo e dos sistemas de Reverend Insanity
para uma profissional de design de TTRPG que nunca leu a obra. O briefing completo da
missão está em `_pipeline/MISSAO.md` — leia-o na primeira vez e sempre que houver
dúvida de escopo.

## Fontes

- **Obra completa (autoridade máxima):** `/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/`
  (6 volumes .txt, ~28 MB, inglês). Capítulos individuais em
  `/home/azuatz/Documentos/Reverend-Insanity-fonte/Volumes/Volume N - .../Chapter_N.xhtml`
  — use grep nesses arquivos para localizar e citar passagens.
- **Secundárias:** wiki (reverendinsanity.fandom.com), Reddit (r/ReverendInsanity),
  debates da comunidade. A obra sempre vence em caso de conflito; registre divergências.

## Política de spoilers (regra inviolável)

- **Entra:** tudo sobre mecânica e funcionamento do mundo — cultivo, Gu, paths, refino,
  economia, clãs/seitas, geografia, Heaven's Will, Fate Gu, Heavenly Court, os
  Veneráveis e as mudanças estruturais que deixaram no mundo.
- **Não entra:** o enredo da webnovel — arcos, reviravoltas, mortes, planos e destino
  de personagens. Personagens aparecem apenas como exemplo mecânico citado por
  capítulo ("um rank 3 refinou um Gu Imortal via X — cap. 445") ou como figura
  histórica estrutural.
- Todo documento final deve poder ser lido por alguém que ainda vá ler a obra sem
  arruinar a história.

## Como o second brain funciona

- `_pipeline/PROGRESSO.md` — estado exato do trabalho (blocos de capítulos lidos,
  pendências, próxima ação). **Leia-o no início de toda sessão; atualize-o antes de
  encerrar qualquer sessão.** Nada de estado importante só em contexto vivo.
- `_pipeline/PLANO.md` — plano de processamento da obra em blocos.
- `_pipeline/notas/` — notas brutas dos subagentes leitores (uma por bloco de capítulos).
- `_pipeline/rascunho/` — o conhecimento consolidado DURANTE a leitura, como rascunho
  interno para o próprio Claude: denso, completo, com citações de capítulo inline
  (aqui elas são bem-vindas), organizado por tema, com marcação "cobre até: Volume N".
  Consolidar = fundir notas brutas novas nos rascunhos, resolvendo contradições
  (regras evoluem ao longo da obra; registre a forma mais madura e anote a evolução).
- Pastas `01`–`09` — as notas FINAIS para a designer. **Só são escritas na fase de
  escrita final, depois de a obra inteira ter sido lida e a pesquisa externa feita**
  — nunca durante a leitura: nota final escrita com leitura parcial sai incompleta
  (ex.: essência primeva só com os ranks do Volume 1). Na fase final, os rascunhos
  são a fonte e os modelos de `_pipeline/MODELOS/` dão o formato. Nota final criada
  prematuramente deve ser movida para `_pipeline/rascunho/`.
- `00 - LEIA-ME (guia para a designer).md` — porta de entrada para a profissional.

## Checkpoint e git (regra crítica — nunca pular)

O vault é um repositório git e ele é a rede de segurança do projeto: os tokens de uma
sessão podem acabar no meio de uma leva de leitura, e tudo que estiver apenas em
contexto vivo se perde. Portanto:

- Todo resultado (nota bruta, nota consolidada, progresso) vai para **disco
  imediatamente**, nunca fica só em contexto. Subagentes escrevem incrementalmente
  durante o trabalho, não apenas no final.
- Após **cada** bloco de notas brutas concluído e após **cada** consolidação:
  atualizar `_pipeline/PROGRESSO.md` e fazer `git add -A && git commit -m "..."`
  (ex.: `notas: caps 0201-0240`, `consolidação: leva volume 1`).
- Trabalhar em levas pequenas: 10 commits pequenos valem mais que uma leva gigante
  sem checkpoint.
- Ao retomar uma sessão, `git log --oneline` + `PROGRESSO.md` dizem o estado real.

## Agentes fixos do pipeline

- `leitor-ri` (`.claude/agents/leitor-ri.md`) — lê um bloco de capítulos e extrai
  notas brutas no template padrão. Sempre usar este agente para leitura; nunca
  improvisar instruções de leitor, para manter todas as levas no mesmo formato.
- `sintetizador-ri` (`.claude/agents/sintetizador-ri.md`) — funde notas brutas na
  base consolidada seguindo as convenções deste arquivo.

## Regras de escrita

- Documentos finais em **português brasileiro**; termos técnicos consagrados em inglês
  com tradução na primeira ocorrência (ex.: "aperture (abertura)").
- **Política de tradução de termos**: quando não houver tradução óbvia para um termo
  do mundo (Gu, paths, ranks, lugares, organizações), consultar a tradução brasileira
  da obra no site centralnovel (centralnovel.com) e adotar o nome usado lá — assim a
  designer encontra os mesmos termos se ler a tradução PT. Se o site estiver
  inacessível ou o termo não existir lá, manter o termo em inglês (sem inventar
  tradução própria). Registrar as escolhas no glossário EN→PT.
- **Sem citações inline nas notas finais**: a prosa deve ser agradável e fluida para
  uma iniciante — nunca escrever "(cap. NN)" ou URLs no meio do texto, tabelas ou
  callouts das notas consolidadas. A rastreabilidade fica nos bastidores: capítulos
  no campo `fontes` do frontmatter (invisível na leitura) e nas notas brutas do
  `_pipeline/`. Marque a origem via `status` do frontmatter (`verificado-no-texto` /
  `wiki-comunidade` / `inferido`). Nunca invente.
- Blocos `> [!note] Para o design` sempre que uma mecânica sugerir algo jogável.
- Notas autossuficientes e **didáticas para leigos**: a leitora não conhece a obra e
  não vai lê-la — escrever como professor que ensina do zero, definindo todo termo
  na primeira aparição, nunca como leitor resumindo para si mesmo.
- Toda nota consolidada segue os modelos de `_pipeline/MODELOS/` (conceito, path,
  estudo de caso, catálogo de Gu); os modelos evoluem junto com o conhecimento.
- **Regras do mundo e resumo por categoria** (regra do usuário): cada domínio do
  conhecimento sempre traz suas regras do mundo enumeradas e/ou um resumo da
  categoria. Nos rascunhos, são as seções obrigatórias "Resumo do domínio" e
  "Regras do mundo" no topo de cada arquivo; nas notas finais, cada pasta temática
  (`01`–`09`) ganha uma nota-visão geral com o resumo e as regras da categoria,
  além das notas de conceito individuais.

### Convenções Obsidian (obrigatórias em toda nota do vault)

- **Frontmatter YAML** em toda nota consolidada, com no mínimo:

  ```yaml
  ---
  tags:
    - dominio/subtopico    # ex.: path/wisdom, cultivo/imortal, gu/refino, mundo, sociedade
  aliases:
    - Termo em inglês      # ex.: nota "Abertura" com alias "Aperture"
  status: rascunho | consolidado | verificado-no-texto
  fontes: ["cap. 445", "cap. 520"]   # capítulos/URLs principais da nota
  ---
  ```

- **Wikilinks** `[[Nota]]` para toda referência interna (nunca link Markdown para nota
  do vault; Markdown `[texto](url)` só para URLs externas). Use `[[Nota|texto]]` para
  encaixar no fluxo da frase e `[[Nota#Seção]]` para apontar seção específica. Toda
  menção a um path, Gu, rank ou organização que tenha nota própria deve ser wikilink.
- **Callouts** para destacar: `> [!note] Para o design` (ganchos de gamedesign),
  `> [!warning]` (regra com exceções/controvérsia na comunidade), `> [!example]`
  (estudo de caso mecânico com capítulo), `> [!question]` (lacuna a investigar).
- **Tags aninhadas** (`#path/blood`, `#gu/imortal`, `#caso-mecanico`) para permitir
  buscas transversais; tags vão no frontmatter, não soltas no texto.
- `==destaque==` para o termo-chave que a nota define; footnotes `[^1]` para
  ressalvas de tradução ou divergência wiki × texto.
- Nomes de arquivo = título natural da nota (ex.: `Refino de Gu.md`), sem numeração,
  pois os wikilinks dependem do nome; a organização vem das pastas e tags.

## Como retomar (para o usuário)

- No terminal, o comando `ri` (função fish em `~/.config/fish/user.fish`) entra no
  vault e roda `claude --continue`, retomando a última sessão deste diretório com
  todo o contexto. Alternativas: `claude --continue` dentro da pasta, ou
  `claude --resume` para escolher entre sessões antigas.
- Mesmo numa sessão totalmente nova, nada se perde: este arquivo carrega sozinho e
  `_pipeline/PROGRESSO.md` + `git log` dizem onde o trabalho parou. Atenção: agentes
  que rodavam em segundo plano não sobrevivem ao desligamento — ao retomar, conferir
  em `_pipeline/notas/` quais blocos ficaram incompletos (status `em-andamento`) e
  relançá-los.

## Protocolo de sessão

1. Ler `_pipeline/PROGRESSO.md` (se não existir, criar plano e iniciar o pipeline do briefing).
2. Executar a próxima etapa (leitura via `leitor-ri` em levas, consolidação via
   `sintetizador-ri`, pesquisa externa ou verificação), salvando tudo em disco e
   commitando a cada bloco concluído.
3. Antes de encerrar: consolidar o que foi lido, atualizar `PROGRESSO.md`, commitar
   tudo e deixar o vault em estado retomável por uma sessão futura sem nenhum
   contexto desta.
