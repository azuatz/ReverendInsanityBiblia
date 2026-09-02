#!/usr/bin/env python3
"""Numera as notas do vault na ordem de leitura e reescreve todos os wikilinks.

Rode a partir da raiz do vault:
    python3 _pipeline/numerar-notas.py --dry     # só mostra o que faria
    python3 _pipeline/numerar-notas.py           # executa

Por que existe: o Obsidian ordena a barra lateral alfabeticamente, então
"Avançar com Aptidão Baixa" aparecia antes de "Ranks e Avanço" — ordem sem
sentido para quem lê pela primeira vez. Com prefixo numérico, a barra lateral
passa a ser o currículo de leitura.

O script renomeia os arquivos e reescreve TODOS os wikilinks do vault, incluindo
os que usam texto alternativo ([[Arquivo|texto]]) e âncora de seção
([[Arquivo#Seção]]). Depois, rode _pipeline/auditar-links.py para conferir.
"""
import io, os, re, sys, glob, subprocess

# Ordem de leitura por pasta. A primeira de cada pasta é sempre a nota-porta.
ORDEM = {
    "01 - Cultivo": [
        "Visão Geral do Cultivo", "Abertura", "Aptidão", "Essência Primordial",
        "Ranks e Avanço", "Attainment", "Avançar com Aptidão Baixa",
        "As Dez Constituições Extremas", "Longevidade", "Tribulações e Calamidades",
        "Ascensão Imortal", "Dao Marks", "Tornar-se Venerável",
    ],
    "02 - Gu": [
        "Visão Geral dos Gu", "O que é um Gu", "Usar e Alimentar Gu", "Gu Vital",
        "Refino de Gu", "Fusão de Gu", "Killer Moves", "Formações de Gu",
        "A Morte dos Gu", "Espólio de Gu", "Conflito de Marcas e Compatibilidade",
        "Gu Imortais",
    ],
    # Caminhos: porta, escolha, depois os 17 na ordem de acesso do mundo
    # (camada 1 = qualquer um sabe que existe; camada 2 = estudo; depois os secretos)
    "03 - Paths": [
        "Visão Geral dos Paths", "Como se Escolhe um Caminho",
        "Blood Path", "Strength Path", "Transformation Path", "Enslavement Path",
        "Refinement Path", "Poison Path", "Sword Path", "Soul Path", "Space Path",
        "Wisdom Path", "Time Path", "Star Path", "Food Path", "Rule Path",
        "Heaven Path", "Luck Path", "Dream Path",
    ],
    "04 - Mundo": [
        "Visão Geral do Mundo", "A Filosofia do Mundo", "As Duas Eras de um Mestre Gu",
        "As Cinco Regiões", "Atlas das Cinco Regiões", "Escala, Distâncias e Viagem",
        "Bestas Gu e Reis Fera", "Lendas de Ren Zu", "Blessed Lands e Grotto-Heavens",
        "Viver Dentro da Abertura Imortal", "Vontade dos Céus", "Fate Gu",
        "Cosmologia", "Lugares Fora das Cinco Regiões", "Tribunal Celestial",
    ],
    "05 - Sociedade": [
        "Visão Geral da Sociedade", "Clãs", "Seitas e Academias",
        "Tipos de Gente e Filosofias de Vida", "Caminho Correto e Caminho Demoníaco",
        "Cultura das Cinco Regiões", "As Grandes Forças do Mundo",
        "Tribunal Celestial e Grandes Forças", "Sociedade Fora das Cinco Regiões",
    ],
    "06 - Economia e Vida": [
        "Visão Geral da Economia", "Pedras Primordiais", "Como um Mestre Gu Ganha a Vida",
        "Vida Cotidiana", "Mercados e Leilões", "Ritmo de Cultivo e Reclusão",
        "Heranças e Provações", "Eventos e Instituições Jogáveis", "Aposta de Rochas",
        "Convenção do Caminho de Refino", "Economia Imortal",
        "Produzir Gu Dentro da Abertura",
    ],
    "07 - Veneraveis e Legados": [
        "Visão Geral dos Veneráveis", "Os Criadores de Caminhos",
        "Os Arquitetos da Ordem", "Os Que Romperam as Leis",
    ],
    "09 - Estudos de Caso Mecanicos": ["Estudos de Caso Mecânicos"],
    "10 - Apendices": [
        "Glossário EN-PT", "Tabelas de Referência Rápida", "Catálogo de Gu",
        "Catálogo de Gu - Mortais", "Catálogo de Gu - Imortais",
        "Catálogo de Receitas", "Catálogo de Golpes - Mortais",
        "Catálogo de Golpes - Imortais", "Linha do Tempo e Eras",
    ],
}


PREFIXO = re.compile(r"^\d{2} - ")


def base(nome):
    """Nome da nota sem o prefixo numerico — o script precisa ser idempotente,
    porque roda de novo toda vez que uma nota nova entra na ordem."""
    return PREFIXO.sub("", nome)


def plano():
    """Devolve (renomeios, erros). renomeios = lista de (pasta, arquivo atual, novo)."""
    ren, err = [], []
    for pasta, ordem in ORDEM.items():
        if not os.path.isdir(pasta):
            err.append(f"pasta inexistente: {pasta}")
            continue
        # base sem prefixo -> nome do arquivo como esta no disco agora
        no_disco = {base(f[:-3]): f[:-3] for f in os.listdir(pasta) if f.endswith(".md")}
        listadas = set(ordem)
        for falta in sorted(set(no_disco) - listadas):
            err.append(f"{pasta}: nota no disco e fora da ordem -> {falta}")
        for sobra in sorted(listadas - set(no_disco)):
            err.append(f"{pasta}: na ordem mas nao existe no disco -> {sobra}")
        for i, nome in enumerate(ordem, 1):
            if nome in no_disco:
                atual, alvo = no_disco[nome], f"{i:02d} - {nome}"
                if atual != alvo:
                    ren.append((pasta, atual, alvo))
    return ren, err


def reescrever_links(mapa, arquivos, dry):
    """mapa: nome antigo -> nome novo. Reescreve [[antigo]], [[antigo|txt]], [[antigo#sec]]."""
    total = 0
    for p in arquivos:
        t = io.open(p, encoding="utf-8").read()
        orig = t

        def sub(m):
            alvo = m.group(1).strip().rstrip("\\").strip()
            resto = m.group(2) or ""
            if alvo in mapa:
                # o link nu ganha texto alternativo para a prosa não exibir o número
                if not resto:
                    resto = "|" + alvo
                return "[[" + mapa[alvo] + resto + "]]"
            return m.group(0)

        # Três armadilhas que custaram uma rodada de conserto e precisam continuar cobertas:
        #   1. dentro de tabela o pipe vem escapado — [[Nota\|texto]];
        #   2. o texto alternativo pode quebrar linha, daí o re.S e o [^\]] no lugar de [^\]\n];
        #   3. o alvo pode trazer âncora de seção — [[Nota#Seção|texto]].
        t = re.sub(r"\[\[([^\]|#\n]+?)\\?((?:[|#][^\]]*?)?)\]\]", sub, t, flags=re.S)
        if t != orig:
            n = sum(1 for _ in re.finditer(r"\[\[", orig))
            total += 1
            if not dry:
                io.open(p, "w", encoding="utf-8").write(t)
    return total


def main():
    dry = "--dry" in sys.argv
    ren, err = plano()
    if err:
        print("PROBLEMAS NO PLANO (corrija a ORDEM antes de executar):")
        for e in err:
            print("   !", e)
        print()
        if not dry:
            print("abortado por seguranca.")
            return 1
    print(f"renomeios planejados: {len(ren)}")
    for pasta, a, b in ren[:6]:
        print(f"   {pasta}/{a}.md  ->  {b}.md")
    if len(ren) > 6:
        print(f"   ... mais {len(ren)-6}")

    mapa = {a: b for _, a, b in ren}
    # Reescreve links nas notas E nos bastidores: os modelos de `_pipeline/MODELOS/` e os
    # relatórios de revisão também usam wikilinks, e ficariam quebrados dentro do Obsidian
    # se só as pastas numeradas fossem tratadas.
    arquivos = sorted(
        glob.glob("[0-9]*/*.md")
        + glob.glob("*.md")
        + glob.glob("_pipeline/**/*.md", recursive=True)
        + glob.glob("_entregas/**/*.md", recursive=True)
    )
    n = reescrever_links(mapa, arquivos, dry)
    print(f"arquivos com wikilinks a reescrever: {n}")

    if dry:
        print("\n(modo seco: nada foi alterado)")
        return 0

    for pasta, a, b in ren:
        subprocess.run(["git", "mv", f"{pasta}/{a}.md", f"{pasta}/{b}.md"], check=True)
    print("renomeios aplicados com git mv (preserva historico).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
