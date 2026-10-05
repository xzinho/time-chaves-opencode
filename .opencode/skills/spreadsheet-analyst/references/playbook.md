# Playbook operacional — Workbook Lineage Audit

## Pergunta de controle

can the workbook be trusted, what drives outputs, and where are errors/anomalies?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **file inventory** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **formula pattern clustering** responde à pergunta sem extrapolar o dado? Se não, selecione **hidden-sheet review.** e declare a troca.
3. Há uma destas exceções: formulas preserved unless asked; macros quarantined; merged cells handled explicitly; blank vs zero maintained.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **can the workbook be trusted, what drives outputs, and where are errors/anomalies?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **File inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Sheet/range map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Types/nulls/duplicates**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Formula lineage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Named ranges/external links**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Reconciliation**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Anomaly tests**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Preserve/edit**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Parse-back/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Formula pattern clustering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency graph**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Outlier rules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Unit/sign audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Hidden-sheet review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Formulas preserved unless asked. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Macros quarantined. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Merged cells handled explicitly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Blank vs zero maintained.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “sheet/range map” cita evidência identificada, aplica “formula pattern clustering”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Workbook Lineage Audit foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `workbook_profile_json.md` ou formato nativo equivalente: materializa **`workbook-profile.json`** e deve ser citado pelo artefato principal.
- `lineage_graphml.md` ou formato nativo equivalente: materializa **`lineage.graphml`** e deve ser citado pelo artefato principal.
- `anomaly_log_csv.md` ou formato nativo equivalente: materializa **`anomaly-log.csv`** e deve ser citado pelo artefato principal.
- `xlsx_with_checks_and_chart.md` ou formato nativo equivalente: materializa **XLSX with checks and chart** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: integrity 25, lineage 20, analysis 20, preservation 20, evidence 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Readable and auditable spreadsheet structure. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Microsoft Spreadsheet Inquire**, Microsoft (official, força: primary). Aplicação: Dependency, inconsistency and workbook analysis. Localizador: https://support.microsoft.com/en-us/office/what-you-can-do-with-spreadsheet-inquire-5444eb12-14a2-4d82-b527-45b9884f98cf. Consulta: 2026-08-24.
3. **Spreadsheet Check and Control**, Patrick O'Beirne (book, força: recognized). Aplicação: Error taxonomy, controls and review evidence. Localizador: Systems Publishing, 2005, ISBN 9781905404001. Consulta: 2026-08-24.
