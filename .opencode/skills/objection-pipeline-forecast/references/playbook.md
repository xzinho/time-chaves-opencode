# Playbook operacional — Evidence-Stage Forecast

## Pergunta de controle

qual receita é provável e que objeção/risco impede progressão?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **define stage exit evidence** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **stage evidence checklist** responde à pergunta sem extrapolar o dado? Se não, selecione **calibration/Brier review.** e declare a troca.
3. Há uma destas exceções: founder deals separated; one-off whale scenario; missing next step downgrades; verbal enthusiasm is not stage evidence.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual receita é provável e que objeção/risco impede progressão?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Define stage exit evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Clean opportunities**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Code objections**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Aging/slippage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Base rates by cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Opportunity adjustments**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Commit/base/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Interventions.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Stage evidence checklist**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cohort conversion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted pipeline vs category**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Calibration/brier review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Founder deals separated. Marque a condição no artefato e acione o gate indicado antes do handoff.
- One-off whale scenario. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing next step downgrades. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Verbal enthusiasm is not stage evidence.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “clean opportunities” cita evidência identificada, aplica “stage evidence checklist”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Evidence-Stage Forecast foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `pipeline_schema_json.md` ou formato nativo equivalente: materializa **`pipeline-schema.json`** e deve ser citado pelo artefato principal.
- `objection_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`objection-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `forecast_xlsx.md` ou formato nativo equivalente: materializa **`forecast.xlsx`** e deve ser citado pelo artefato principal.
- `deal_inspection_card.md` ou formato nativo equivalente: materializa **deal inspection card** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: hygiene 20, stage evidence 25, calibration 20, objection diagnosis 20, action 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Need-payoff discovery and objection diagnosis. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Sales Acceleration Formula**, Mark Roberge (book, força: recognized). Aplicação: Stage definitions, data quality and forecast discipline. Localizador: Wiley, 2015, ISBN 9781119047070. Consulta: 2026-08-24.
3. **Forecast Categories**, Salesforce (official, força: primary). Aplicação: Commit/best-case/pipeline semantics. Localizador: https://help.salesforce.com/s/articleView?id=sf.forecasts3_categories.htm&type=5. Consulta: 2026-08-24.
