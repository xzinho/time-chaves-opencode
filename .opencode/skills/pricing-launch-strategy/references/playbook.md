# Playbook operacional — Value-WTP Launch Lab

## Pergunta de controle

quem paga quanto por qual bundle, sob quais fences e rollout risks?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **segment/jobs** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **value metric** responde à pergunta sem extrapolar o dado? Se não, selecione **rollback trigger.** e declare a troca.
3. Há uma destas exceções: PSM is exploratory; regulated price escalates; sparse sample uses ranges; discount never hides negative contribution.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **quem paga quanto por qual bundle, sob quais fences e rollout risks?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Segment/jobs**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Alternatives/reference price**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Value drivers**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Wtp research**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Package architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Unit economics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Price scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Launch cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Instrumentation/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Value metric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Conjoint/psm limitations**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Good-better-best**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fences**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Grandfathering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Price waterfall**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rollback trigger.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Psm is exploratory. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Regulated price escalates. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Sparse sample uses ranges. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Discount never hides negative contribution.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “alternatives/reference price” cita evidência identificada, aplica “value metric”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Value-WTP Launch Lab foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `wtp_study_md.md` ou formato nativo equivalente: materializa **`wtp-study.md`** e deve ser citado pelo artefato principal.
- `package_matrix_xlsx.md` ou formato nativo equivalente: materializa **`package-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `price_waterfall_xlsx.md` ou formato nativo equivalente: materializa **`price-waterfall.xlsx`** e deve ser citado pelo artefato principal.
- `launch_rollback_plan.md` ou formato nativo equivalente: materializa **launch/rollback plan** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: value linkage 25, research 20, economics 20, packaging 15, rollout 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Strategy and Tactics of Pricing**, Nagle, Hogan, Zale (book, força: canonical). Aplicação: Value-based segmentation and price fences. Localizador: Routledge, 2016, ISBN 9781138737501. Consulta: 2026-08-24.
2. **Monetizing Innovation**, Madhavan Ramanujam and Georg Tacke (book, força: canonical). Aplicação: Willingness-to-pay before product launch. Localizador: Wiley, 2016, ISBN 9781119240860. Consulta: 2026-08-24.
3. **Van Westendorp Price Sensitivity Meter**, ESOMAR archive (official, força: primary). Aplicação: Exploratory acceptable-price bands with limitations. Localizador: https://ana.esomar.org/documents/price-sensitivity-meter-a-new-approach-to-consumer-perception-of-price. Consulta: 2026-08-24.
