---
name: pricing-launch-strategy
description: "Executa Value-WTP Launch Lab para responder: quem paga quanto por qual bundle, sob quais fences e rollout risks?"
---

# Pricing Launch Strategy

## Escopo e gatilhos

Use quando a decisão real for: **quem paga quanto por qual bundle, sob quais fences e rollout risks?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Value-WTP Launch Lab**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Value-WTP Launch Lab

1. **Segment/jobs**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Alternatives/reference price**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Value drivers**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Wtp research**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Package architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Unit economics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Price scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Launch cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Instrumentation/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Value metric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Conjoint/psm limitations**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Good-better-best**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fences**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Grandfathering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Price waterfall**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rollback trigger.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Psm is exploratory. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Regulated price escalates. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Sparse sample uses ranges. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Discount never hides negative contribution.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: value linkage 25, research 20, economics 20, packaging 15, rollout 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `wtp_study_md.md` ou formato nativo equivalente: materializa **`wtp-study.md`** e deve ser citado pelo artefato principal.
- `package_matrix_xlsx.md` ou formato nativo equivalente: materializa **`package-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `price_waterfall_xlsx.md` ou formato nativo equivalente: materializa **`price-waterfall.xlsx`** e deve ser citado pelo artefato principal.
- `launch_rollback_plan.md` ou formato nativo equivalente: materializa **launch/rollback plan** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Strategy and Tactics of Pricing**, Nagle, Hogan, Zale (book, força: canonical). Aplicação: Value-based segmentation and price fences. Localizador: Routledge, 2016, ISBN 9781138737501. Consulta: 2026-08-24.
2. **Monetizing Innovation**, Madhavan Ramanujam and Georg Tacke (book, força: canonical). Aplicação: Willingness-to-pay before product launch. Localizador: Wiley, 2016, ISBN 9781119240860. Consulta: 2026-08-24.
3. **Van Westendorp Price Sensitivity Meter**, ESOMAR archive (official, força: primary). Aplicação: Exploratory acceptable-price bands with limitations. Localizador: https://ana.esomar.org/documents/price-sensitivity-meter-a-new-approach-to-consumer-perception-of-price. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
