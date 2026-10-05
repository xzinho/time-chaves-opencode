---
name: professional-report-builder
description: "Executa Evidence-to-Report Architecture para responder: que report structure makes findings auditable and decisions actionable?"
---

# Professional Report Builder

## Escopo e gatilhos

Use quando a decisão real for: **que report structure makes findings auditable and decisions actionable?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Evidence-to-Report Architecture**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Evidence-to-Report Architecture

1. **Mandate/audience**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Report questions**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Outline/numbering**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Methods**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Implications**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Recommendations**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Appendices/citations**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Finding-evidence-recommendation chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source notes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart purpose**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cross-reference validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Executive/detail layering.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Sensitive appendix restricted. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing method disclosed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Recommendation separates evidence from judgment.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: traceability 25, structure 20, analysis 20, actionability 20, production quality 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `report_schema_json.md` ou formato nativo equivalente: materializa **`report-schema.json`** e deve ser citado pelo artefato principal.
- `evidence_register_csv.md` ou formato nativo equivalente: materializa **`evidence-register.csv`** e deve ser citado pelo artefato principal.
- `recommendation_trace_csv.md` ou formato nativo equivalente: materializa **`recommendation-trace.csv`** e deve ser citado pelo artefato principal.
- `docx_pdf_builders.md` ou formato nativo equivalente: materializa **DOCX/PDF builders** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ISO 2145 Documentation Numbering**, ISO (standard, força: primary). Aplicação: Stable section hierarchy. Localizador: https://www.iso.org/standard/6937.html. Consulta: 2026-08-24.
2. **GOV.UK Style Guide**, UK Government Digital Service (official, força: primary). Aplicação: Readable, consistent professional language. Localizador: https://www.gov.uk/guidance/style-guide. Consulta: 2026-08-24.
3. **Storytelling with Data**, Cole Nussbaumer Knaflic (book, força: canonical). Aplicação: Chart choice, attention and explanatory narrative. Localizador: Wiley, 2015, ISBN 9781119002253. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
