---
name: creative-ideation
description: "Executa Tension-Recombination Portfolio para responder: quais ideias são simultaneamente novas, pertinentes e testáveis?"
---

# Creative Ideation

## Escopo e gatilhos

Use quando a decisão real for: **quais ideias são simultaneamente novas, pertinentes e testáveis?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Tension-Recombination Portfolio**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Tension-Recombination Portfolio

1. **Desafio/restrições**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Fatos/tensões**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Estímulos distantes**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Divergência por operadores**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Clusters**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Concepts**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Crítica diferida**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Portfólio exploit/explore**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Microteste.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Forced connections**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Inversion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Subtraction**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Analogy transfer**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Morphological box**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Silent brainwriting.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Bloqueio de repertório pede pesquisa. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Grupo hierárquico usa geração silenciosa. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ideia regulada vai a feasibility gate.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: novidade 25, pertinência 25, coerência 15, viabilidade 15, testabilidade 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `tension_bank_csv.md` ou formato nativo equivalente: materializa **`tension-bank.csv`** e deve ser citado pelo artefato principal.
- `morphological_matrix_xlsx.md` ou formato nativo equivalente: materializa **`morphological-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `concept_card_md.md` ou formato nativo equivalente: materializa **`concept-card.md`** e deve ser citado pelo artefato principal.
- `portfolio_map.md` ou formato nativo equivalente: materializa **portfolio map** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **A Technique for Producing Ideas**, James Webb Young (book, força: canonical). Aplicação: Fact gathering, incubation and recombination. Localizador: McGraw-Hill, 1965, ISBN 9780071410946. Consulta: 2026-08-24.
2. **Creative Confidence**, Tom Kelley and David Kelley (book, força: canonical). Aplicação: Divergence, experiments and confidence-building. Localizador: Crown Business, 2013, ISBN 9780385349369. Consulta: 2026-08-24.
3. **Design Kit Methods**, IDEO.org (official, força: primary). Aplicação: Human-centered ideation and field-testing methods. Localizador: https://www.designkit.org/methods. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
