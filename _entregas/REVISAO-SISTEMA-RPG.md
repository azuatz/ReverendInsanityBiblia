# Revisão externa do sistema de RPG

> Documento de trabalho de um revisor externo. Destinatário: o agente que mantém
> `/home/azuatz/Documentos/REVEREND INSANITY/`. Este revisor **não editou nada** no
> sistema — só leu.
>
> **Status: EM ESCRITA INCREMENTAL.** Blocos são gravados assim que fecham.

## Como esta revisão foi feita

**Três acervos, três papéis.**

1. **O sistema** — `/home/azuatz/Documentos/REVEREND INSANITY/` (842 arquivos, 39 MB).
   Objeto da revisão. Lido: `CLAUDE.md`, `00 — Portal/` inteiro, `01 — Fundação/`
   inteiro, `02 — Caminho do Cultivo/` inteiro, `03 — Gu/` (estrutura + notas de
   regra), `04`, `05`, `06`, e varreduras por termo em todos os 842 arquivos.
2. **A Bíblia de Sistema** — `/home/azuatz/Documentos/ReverendInsanityExpert/`
   (140+ notas escritas a partir da leitura integral da obra). Base de comparação.
3. **A obra** — `~/Documentos/Reverend-Insanity-fonte/texto/*.txt`, 6 volumes.
   **Autoridade máxima e desempate.** Toda citação de capítulo abaixo foi verificada
   por `grep -i` no texto-fonte, e o número do capítulo foi resolvido com
   `head -n <linha> <vol> | grep -oE "^## Chapter [0-9]+" | tail -1`.

**Achado de método que vale registrar para o agente executor:** a obra grafa nomes
de Gu, essências e golpes **em minúsculas** ("all-out effort Gu", "green grape
immortal essence bead"). Buscar com `grep` sensível a maiúsculas produz falsos
negativos em massa. **Use sempre `grep -i`.** E o termo canônico em inglês é
**primeval** (essence / stone / sea) — "primordial essence" **não existe na obra**,
embora "essência primordial" seja a tradução PT correta.

**O que ficou de fora, e por quê.**

- `09 — Lore de Vespéria/` — é cenário autoral do usuário, não Reverend Insanity.
  Divergência ali não é erro. Não revisado.
- `10 — Referência Canônica/` e `_Fontes/` — imutáveis por regra do próprio vault.
  Usados só como leitura, para entender de onde vieram os números do sistema.
- `_Processo/🎯 Simulação de Combate — Resultados.md` (330 KB) e
  `_Processo/🧭 Log de Decisões.md` (500 KB) — consultados por busca dirigida, não
  lidos linha a linha. **Consequência honesta:** é possível que um achado abaixo já
  tenha uma decisão registrada que o justifica. Onde suspeitei disso, avisei.
- Balanceamento numérico interno (o sistema tem simulação própria com 3.000+
  iterações). Não é o meu papel e eu não tenho os dados dela.

**O critério de corte.** O pedido do usuário foi explícito: *"há coisas que não
precisa colocar por já estar muito cheio, mas coisas que você achar que estão
incompletas e crê ser o recomendado, envie para ele adicionar."* Portanto isto
**não é uma lista do que falta** — é uma lista curada. Um achado só entrou se
passou por um destes três filtros:

1. **contradiz a obra** (erro de canonicidade),
2. **falta algo sem o qual o mestre trava na mesa** (regra sem número, recurso sem
   economia, procedimento sem passo a passo), ou
3. **o sistema já tem o assunto, mas raso, e a obra dá material que o torna muito
   melhor** — e o ganho é grande o bastante para pagar o volume que acrescenta.

Tudo que não passou nos três filtros virou a seção **"O que existe na obra e eu NÃO
recomendo acrescentar"**, no fim. Essa seção é parte do produto: ela poupa o agente
executor de reabrir discussões já fechadas por mim.
