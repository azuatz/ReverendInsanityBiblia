# Modelo — nota de Grande Evento (pasta `08 - Eventos e Cenarios/`)

Uso: cada nota descreve **um grande acontecimento do mundo** de Reverend Insanity como
*cenário jogável*, não como capítulo de enredo.

## A regra que governa esta pasta

O evento entra como **situação**, nunca como história. A designer precisa saber o que
acontece no mundo, por que acontece, como é estar lá dentro e o que um grupo de
personagens pode fazer ali — e **não** quem venceu, quem morreu ou o que o protagonista
fez. Os jogadores estarão no evento pelo ambiente e pelo contexto, com o mundo
funcionando exatamente como funciona na obra, mas **a história dentro dele é deles**.

Na prática:

- **Entra:** a causa estrutural, a mecânica, a geografia, os perigos, as regras especiais
  que valem no local, as forças presentes descritas como *tipos e facções*, os prêmios,
  o relógio do evento, os desfechos possíveis.
- **Não entra:** o encadeamento narrativo do romance, o papel de personagens nomeados,
  reviravoltas, traições, mortes e o desfecho específico que a obra registrou.
- Um personagem histórico só aparece como **função** ("o fundador da herança", "a força
  que convocou a assembleia") quando sem ele o evento não se explica.

## Estrutura da nota

```markdown
---
tags:
  - evento/<tipo>          # evento/calamidade, evento/guerra, evento/herança, evento/torneio…
  - regiao/<regiao>
aliases:
  - Nome em inglês
status: verificado-no-texto | consolidado
fontes: ["cap. NNN", "cap. NNN"]
conhecimento: comum | especializado | segredo
ranks: "faixa de rank dos personagens que cabem aqui"
---

# Nome do Evento

**Uma frase** que diz o que é, para quem só vai bater o olho.

> [!abstract] Ficha rápida
> | | |
> |---|---|
> | **Tipo** | calamidade natural / guerra / abertura de herança / assembleia / torneio / … |
> | **Onde** | região e terreno |
> | **Quando** | único, cíclico (de quantos em quantos anos), ou desencadeado por gatilho |
> | **Duração** | quanto dura de ponta a ponta |
> | **Escala de poder** | ranks que participam; rank mínimo para sobreviver |
> | **Quem pode entrar** | restrições de acesso |

## Por que acontece

A causa **mecânica** dentro das regras do mundo. Um evento deste cenário nunca acontece
"porque a trama pediu": ele sai de alguma regra que a designer já conhece (marés de qi,
saturação de dao marks, uma herança com relógio, uma fronteira que enfraquece…).

## Como é por dentro

O ambiente sensorial e físico: o que se vê, o que se ouve, o que mata quem se distrai.
Esta seção é o que o mestre vai ler em voz alta.

## As regras especiais que valem aqui

O que muda em relação ao mundo normal — supressões de rank, bloqueios de caminho,
formações ativas, restrições impostas por quem organiza, terreno que altera custo de
essência. Uma lista numerada, porque é isso que vira regra de mesa.

## O relógio do evento

As fases, em ordem, com a duração de cada uma e o que muda de uma para a outra.

## O que está em jogo

Prêmios, recursos, oportunidades — e o preço. Sempre em números quando a obra der.

## O que um grupo de personagens faz aqui

Por faixa de rank, o papel realista. Um rank 2 não decide uma guerra de imortais, mas
tem muito o que fazer dentro dela; diga o quê.

## Desfechos possíveis

O leque estrutural de finais, como opções para a mesa — **não** o desfecho do romance.

> [!note] Para o design
> O gancho jogável: que tipo de sessão, que tensão, que recompensa.

## O que a obra não diz

As lacunas, honestamente declaradas — é onde a designer pode inventar sem contradizer
o cânone.
```

## Convenções obrigatórias (as mesmas do resto do vault)

- Quatro estados de confiabilidade: texto simples = canônico; `(ded.)` = dedução segura;
  `*` = invenção nossa; `—` = a obra não informa. O cabeçalho de cada nota declara a
  convenção e afirma que apagar tudo marcado com `*` devolve o documento a 100% canônico.
- Sem citação de capítulo no corpo; rastreabilidade só no campo `fontes`.
- Wikilinks pelo nome exato do arquivo, com texto alternativo: `[[05 - Ranks e Avanço|ranks]]`.
- Português brasileiro, didático para quem nunca leu a obra: todo termo definido na
  primeira aparição.
