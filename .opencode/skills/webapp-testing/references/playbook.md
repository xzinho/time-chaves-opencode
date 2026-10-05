# Playbook operacional — Risk-Journey-Evidence Suite

## Pergunta de controle

which user-visible failures and quality risks must be prevented before release?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **scope/risk** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **role/test-id locators** responde à pergunta sem extrapolar o dado? Se não, selecione **trace/video on retry.** e declare a troca.
3. Há uma destas exceções: CAPTCHA/payment/email require approved sandbox; flaky test is quarantined with owner/date, not silently retried forever; visual diff has tolerance rationale.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **which user-visible failures and quality risks must be prevented before release?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Scope/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Critical journeys**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **States/fixtures**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Functional tests**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Error/loading/empty/responsive**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Visual/performance/security-adjacent checks**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Flaky-test controls**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Evidence/gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Role/test-id locators**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Isolated context**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deterministic seed**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Network mocking boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Screenshot diff**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keyboard/screen-reader checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Trace/video on retry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Captcha/payment/email require approved sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Flaky test is quarantined with owner/date, not silently retried forever. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Visual diff has tolerance rationale.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “critical journeys” cita evidência identificada, aplica “role/test-id locators”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Risk-Journey-Evidence Suite foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `journey_risk_map_csv.md` ou formato nativo equivalente: materializa **`journey-risk-map.csv`** e deve ser citado pelo artefato principal.
- `fixture_contract_json.md` ou formato nativo equivalente: materializa **`fixture-contract.json`** e deve ser citado pelo artefato principal.
- `playwright_project.md` ou formato nativo equivalente: materializa **Playwright project** e deve ser citado pelo artefato principal.
- `accessibility_report.md` ou formato nativo equivalente: materializa **accessibility report** e deve ser citado pelo artefato principal.
- `trace_screenshot_bundle.md` ou formato nativo equivalente: materializa **trace/screenshot bundle** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: risk coverage 25, assertion quality 20, determinism 20, state coverage 15, accessibility 10, evidence 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **WebDriver W3C Recommendation**, W3C (standard, força: primary). Aplicação: Browser automation semantics. Localizador: https://www.w3.org/TR/webdriver2/. Consulta: 2026-08-24.
2. **Playwright Best Practices**, Microsoft (official, força: primary). Aplicação: User-visible locators, isolation and resilient assertions. Localizador: https://playwright.dev/docs/best-practices. Consulta: 2026-08-24.
3. **WCAG Evaluation Methodology 1.0**, W3C (official, força: primary). Aplicação: Accessibility test scope, sampling and reporting. Localizador: https://www.w3.org/TR/WCAG-EM/. Consulta: 2026-08-24.
