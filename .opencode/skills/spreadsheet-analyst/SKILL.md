---
name: spreadsheet-analyst
description: "Executa Workbook Lineage Audit para responder: can the workbook be trusted, what drives outputs, and where are errors/anomalies?"
---

# Spreadsheet Analyst

## Escopo e gatilhos

Use quando a decisão real for: **can the workbook be trusted, what drives outputs, and where are errors/anomalies?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Workbook Lineage Audit**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Workbook Lineage Audit

1. **File inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Sheet/range map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Types/nulls/duplicates**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Formula lineage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Named ranges/external links**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Reconciliation**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Anomaly tests**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Preserve/edit**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Parse-back/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Formula pattern clustering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency graph**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Outlier rules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Unit/sign audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Hidden-sheet review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Formulas preserved unless asked. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Macros quarantined. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Merged cells handled explicitly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Blank vs zero maintained.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: integrity 25, lineage 20, analysis 20, preservation 20, evidence 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `workbook_profile_json.md` ou formato nativo equivalente: materializa **`workbook-profile.json`** e deve ser citado pelo artefato principal.
- `lineage_graphml.md` ou formato nativo equivalente: materializa **`lineage.graphml`** e deve ser citado pelo artefato principal.
- `anomaly_log_csv.md` ou formato nativo equivalente: materializa **`anomaly-log.csv`** e deve ser citado pelo artefato principal.
- `xlsx_with_checks_and_chart.md` ou formato nativo equivalente: materializa **XLSX with checks and chart** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Readable and auditable spreadsheet structure. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Microsoft Spreadsheet Inquire**, Microsoft (official, força: primary). Aplicação: Dependency, inconsistency and workbook analysis. Localizador: https://support.microsoft.com/en-us/office/what-you-can-do-with-spreadsheet-inquire-5444eb12-14a2-4d82-b527-45b9884f98cf. Consulta: 2026-08-24.
3. **Spreadsheet Check and Control**, Patrick O'Beirne (book, força: recognized). Aplicação: Error taxonomy, controls and review evidence. Localizador: Systems Publishing, 2005, ISBN 9781905404001. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
