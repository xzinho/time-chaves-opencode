---
name: objection-pipeline-forecast
description: "Executa Evidence-Stage Forecast para responder: qual receita é provável e que objeção/risco impede progressão?"
---

# Objection Pipeline Forecast

## Escopo e gatilhos

Use quando a decisão real for: **qual receita é provável e que objeção/risco impede progressão?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Evidence-Stage Forecast**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Evidence-Stage Forecast

1. **Define stage exit evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Clean opportunities**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Code objections**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Aging/slippage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Base rates by cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Opportunity adjustments**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Commit/base/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Interventions.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Stage evidence checklist**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cohort conversion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted pipeline vs category**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Calibration/brier review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Founder deals separated. Marque a condição no artefato e acione o gate indicado antes do handoff.
- One-off whale scenario. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing next step downgrades. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Verbal enthusiasm is not stage evidence.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: hygiene 20, stage evidence 25, calibration 20, objection diagnosis 20, action 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `pipeline_schema_json.md` ou formato nativo equivalente: materializa **`pipeline-schema.json`** e deve ser citado pelo artefato principal.
- `objection_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`objection-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `forecast_xlsx.md` ou formato nativo equivalente: materializa **`forecast.xlsx`** e deve ser citado pelo artefato principal.
- `deal_inspection_card.md` ou formato nativo equivalente: materializa **deal inspection card** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Need-payoff discovery and objection diagnosis. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Sales Acceleration Formula**, Mark Roberge (book, força: recognized). Aplicação: Stage definitions, data quality and forecast discipline. Localizador: Wiley, 2015, ISBN 9781119047070. Consulta: 2026-08-24.
3. **Forecast Categories**, Salesforce (official, força: primary). Aplicação: Commit/best-case/pipeline semantics. Localizador: https://help.salesforce.com/s/articleView?id=sf.forecasts3_categories.htm&type=5. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
