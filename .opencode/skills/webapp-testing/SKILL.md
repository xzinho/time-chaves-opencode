---
name: webapp-testing
description: "Executa Risk-Journey-Evidence Suite para responder: which user-visible failures and quality risks must be prevented before release?"
---

# Webapp Testing

## Escopo e gatilhos

Use quando a decisão real for: **which user-visible failures and quality risks must be prevented before release?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Risk-Journey-Evidence Suite**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Risk-Journey-Evidence Suite

1. **Scope/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Critical journeys**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **States/fixtures**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Functional tests**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Error/loading/empty/responsive**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Visual/performance/security-adjacent checks**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Flaky-test controls**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Evidence/gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Role/test-id locators**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Isolated context**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deterministic seed**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Network mocking boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Screenshot diff**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keyboard/screen-reader checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Trace/video on retry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Captcha/payment/email require approved sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Flaky test is quarantined with owner/date, not silently retried forever. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Visual diff has tolerance rationale.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: risk coverage 25, assertion quality 20, determinism 20, state coverage 15, accessibility 10, evidence 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `journey_risk_map_csv.md` ou formato nativo equivalente: materializa **`journey-risk-map.csv`** e deve ser citado pelo artefato principal.
- `fixture_contract_json.md` ou formato nativo equivalente: materializa **`fixture-contract.json`** e deve ser citado pelo artefato principal.
- `playwright_project.md` ou formato nativo equivalente: materializa **Playwright project** e deve ser citado pelo artefato principal.
- `accessibility_report.md` ou formato nativo equivalente: materializa **accessibility report** e deve ser citado pelo artefato principal.
- `trace_screenshot_bundle.md` ou formato nativo equivalente: materializa **trace/screenshot bundle** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **WebDriver W3C Recommendation**, W3C (standard, força: primary). Aplicação: Browser automation semantics. Localizador: https://www.w3.org/TR/webdriver2/. Consulta: 2026-08-24.
2. **Playwright Best Practices**, Microsoft (official, força: primary). Aplicação: User-visible locators, isolation and resilient assertions. Localizador: https://playwright.dev/docs/best-practices. Consulta: 2026-08-24.
3. **WCAG Evaluation Methodology 1.0**, W3C (official, força: primary). Aplicação: Accessibility test scope, sampling and reporting. Localizador: https://www.w3.org/TR/WCAG-EM/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
