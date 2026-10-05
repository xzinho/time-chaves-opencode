# Playbook operacional — Argument-to-Slide System

## Pergunta de controle

qual sequência faz a audiência compreender, acreditar e decidir?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **audience/decision** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **assertion-evidence** responde à pergunta sem extrapolar o dado? Se não, selecione **appendix routing.** e declare a troca.
3. Há uma destas exceções: leave-behind needs more context; board deck leads with decisions; data-heavy slide gets takeaway and source, not decoration.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual sequência faz a audiência compreender, acreditar e decidir?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Audience/decision**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Storyline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Slide functions**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Wireframes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Chart selection**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Build**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Speaker notes**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Rehearsal/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Assertion-evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **One function per slide**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart integrity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Section rhythm**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Appendix routing.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Leave-behind needs more context. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Board deck leads with decisions. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Data-heavy slide gets takeaway and source, not decoration.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “storyline” cita evidência identificada, aplica “assertion-evidence”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Argument-to-Slide System foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `storyline_csv.md` ou formato nativo equivalente: materializa **`storyline.csv`** e deve ser citado pelo artefato principal.
- `slide_schema_json.md` ou formato nativo equivalente: materializa **`slide-schema.json`** e deve ser citado pelo artefato principal.
- `chart_decision_tree.md` ou formato nativo equivalente: materializa **chart decision tree** e deve ser citado pelo artefato principal.
- `native_pptx_builder_and_render_montage.md` ou formato nativo equivalente: materializa **native PPTX builder and render montage** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: storyline 25, evidence 20, visual hierarchy 20, readability 15, action 10, accessibility 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Visual Display of Quantitative Information**, Edward Tufte (book, força: canonical). Aplicação: Evidence-dense, honest quantitative graphics. Localizador: Graphics Press, 2001, ISBN 9780961392147. Consulta: 2026-08-24.
2. **Presentation Zen**, Garr Reynolds (book, força: canonical). Aplicação: Audience, story and visual restraint. Localizador: New Riders, 2019, ISBN 9780135800911. Consulta: 2026-08-24.
3. **PowerPoint Accessibility**, Microsoft (official, força: primary). Aplicação: Reading order, alt text, contrast and structure. Localizador: https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25. Consulta: 2026-08-24.
