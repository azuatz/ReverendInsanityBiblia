# Diário de decisões autônomas (operação noturna)

O usuário autorizou a operação contínua durante a noite, com o Claude tomando sempre
a decisão recomendada e registrando aqui cada uma, para revisão de manhã. Formato:
decisão, motivo, e se vale a pena o usuário reconsiderar.

## Decisões

1. **Blocos de ~41 capítulos** (vs. 50+) para os volumes 2–6 — margem de segurança no
   contexto dos leitores Sonnet; blocos de 40 funcionaram bem no Volume 1.
   *Reconsiderar?* Não — custo/benefício claro.
2. **Leitura do Volume 2 lançada em paralelo à consolidação do Volume 1** — leitores
   escrevem em `_pipeline/notas/`, sintetizador em `_pipeline/rascunho/`; sem
   conflito de arquivos, e a noite rende mais.
   *Reconsiderar?* Não.
3. **Sintetizadores sempre em série** (um volume por vez, na ordem) — todos editam os
   mesmos arquivos de rascunho; paralelo causaria conflito de escrita.
   *Reconsiderar?* Não.
4. **Levas de no máximo 6 leitores simultâneos** — equilíbrio entre velocidade e
   controle; o Volume 5 (23 blocos) será feito em ~4 levas.
   *Reconsiderar?* Se quiser mais velocidade em noites futuras, dá para testar 8–10.

(novas decisões são acrescentadas abaixo conforme a noite avança)
