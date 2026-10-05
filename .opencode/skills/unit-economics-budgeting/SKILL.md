---
name: unit-economics-budgeting
description: "Executa Unit-Cohort-Driver Budget para responder: which unit creates contribution, at what scale/payback, and how much cash can be committed?"
---

# Unit Economics Budgeting

## Escopo e gatilhos

Use quando a decisão real for: **which unit creates contribution, at what scale/payback, and how much cash can be committed?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Unit-Cohort-Driver Budget**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Unit-Cohort-Driver Budget

1. **Define unit/cohort/time**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Revenue bridge**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Variable/step/fixed costs**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Cac/retention/ltv/payback**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Driver-based budget**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Base/downside/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cash runway/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Cohort curves**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gross/contribution margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Blended vs marginal cac**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Payback**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capacity steps**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rolling forecast.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Ltv limited by observed horizon. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Negative margin blocks scaling. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Accrual profit separated from cash. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Shared costs allocation disclosed.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: unit definition 20, cost completeness 25, cohort evidence 20, scenario 20, guardrails 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `unit_model_xlsx.md` ou formato nativo equivalente: materializa **`unit-model.xlsx`** e deve ser citado pelo artefato principal.
- `cohort_table_csv.md` ou formato nativo equivalente: materializa **`cohort-table.csv`** e deve ser citado pelo artefato principal.
- `budget_drivers_yaml.md` ou formato nativo equivalente: materializa **`budget-drivers.yaml`** e deve ser citado pelo artefato principal.
- `variance_bridge.md` ou formato nativo equivalente: materializa **variance bridge** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Lean Analytics**, Croll and Yoskovitz (book, força: canonical). Aplicação: Business-model-specific unit metrics. Localizador: O'Reilly, 2013, ISBN 9781449335670. Consulta: 2026-08-24.
2. **Financial Intelligence for Entrepreneurs**, Berman and Knight (book, força: recognized). Aplicação: Contribution, working capital and accrual interpretation. Localizador: Harvard Business Review Press, 2008, ISBN 9781422119150. Consulta: 2026-08-24.
3. **Break-even point**, US Small Business Administration (official, força: primary). Aplicação: Cost inventory and cash need framing. Localizador: https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
