# Playbook operacional — Unit-Cohort-Driver Budget

## Pergunta de controle

which unit creates contribution, at what scale/payback, and how much cash can be committed?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **define unit/cohort/time** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **cohort curves** responde à pergunta sem extrapolar o dado? Se não, selecione **rolling forecast.** e declare a troca.
3. Há uma destas exceções: LTV limited by observed horizon; negative margin blocks scaling; accrual profit separated from cash; shared costs allocation disclosed.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **which unit creates contribution, at what scale/payback, and how much cash can be committed?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Define unit/cohort/time**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Revenue bridge**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Variable/step/fixed costs**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Cac/retention/ltv/payback**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Driver-based budget**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Base/downside/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cash runway/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Cohort curves**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gross/contribution margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Blended vs marginal cac**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Payback**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capacity steps**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rolling forecast.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Ltv limited by observed horizon. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Negative margin blocks scaling. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Accrual profit separated from cash. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Shared costs allocation disclosed.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “revenue bridge” cita evidência identificada, aplica “cohort curves”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Unit-Cohort-Driver Budget foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `unit_model_xlsx.md` ou formato nativo equivalente: materializa **`unit-model.xlsx`** e deve ser citado pelo artefato principal.
- `cohort_table_csv.md` ou formato nativo equivalente: materializa **`cohort-table.csv`** e deve ser citado pelo artefato principal.
- `budget_drivers_yaml.md` ou formato nativo equivalente: materializa **`budget-drivers.yaml`** e deve ser citado pelo artefato principal.
- `variance_bridge.md` ou formato nativo equivalente: materializa **variance bridge** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: unit definition 20, cost completeness 25, cohort evidence 20, scenario 20, guardrails 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Lean Analytics**, Croll and Yoskovitz (book, força: canonical). Aplicação: Business-model-specific unit metrics. Localizador: O'Reilly, 2013, ISBN 9781449335670. Consulta: 2026-08-24.
2. **Financial Intelligence for Entrepreneurs**, Berman and Knight (book, força: recognized). Aplicação: Contribution, working capital and accrual interpretation. Localizador: Harvard Business Review Press, 2008, ISBN 9781422119150. Consulta: 2026-08-24.
3. **Break-even point**, US Small Business Administration (official, força: primary). Aplicação: Cost inventory and cash need framing. Localizador: https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs. Consulta: 2026-08-24.
