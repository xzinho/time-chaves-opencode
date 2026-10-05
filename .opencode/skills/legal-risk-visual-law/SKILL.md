---
name: legal-risk-visual-law
description: "Executa Meaning-Preserving Legal Design para responder: como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?"
---

# Legal Risk Visual Law

## Escopo e gatilhos

Use quando a decisão real for: **como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Meaning-Preserving Legal Design**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Meaning-Preserving Legal Design

1. **Legal source**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Rule/condition/exception/consequence extraction**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Audience task**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Layer architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Visual encoding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Legal fidelity review**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Comprehension test**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Revision.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Layered disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Decision tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk heatmap with criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Before/after comprehension**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic crosswalk.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Ambiguidade substantiva permanece explícita. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Cor nunca é único canal. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Documento visual não substitui original quando obrigatório.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fidelidade 30, compreensão 25, actionability 20, acessibilidade 15, rastreabilidade 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `legal_semantic_map_csv.md` ou formato nativo equivalente: materializa **`legal-semantic-map.csv`** e deve ser citado pelo artefato principal.
- `decision_tree_mmd.md` ou formato nativo equivalente: materializa **`decision-tree.mmd`** e deve ser citado pelo artefato principal.
- `comprehension_script.md` ou formato nativo equivalente: materializa **comprehension script** e deve ser citado pelo artefato principal.
- `fidelity_checklist.md` ou formato nativo equivalente: materializa **fidelity checklist** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Visual Law Library**, Legal Design Alliance (official, força: primary). Aplicação: User-centered legal information design. Localizador: https://www.legaldesignalliance.org/. Consulta: 2026-08-24.
2. **Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Layered explanation without changing legal meaning. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
3. **Legal Design: Integrating Business, Design and Legal Thinking**, Corrales, Fenwick, Haapio (book, força: canonical). Aplicação: Legal-service prototyping and usability. Localizador: Edward Elgar, 2021, ISBN 9781839102271. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
