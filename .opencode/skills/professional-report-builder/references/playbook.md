# Playbook operacional — Evidence-to-Report Architecture

## Pergunta de controle

que report structure makes findings auditable and decisions actionable?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **mandate/audience** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **finding-evidence-recommendation chain** responde à pergunta sem extrapolar o dado? Se não, selecione **executive/detail layering.** e declare a troca.
3. Há uma destas exceções: sensitive appendix restricted; missing method disclosed; recommendation separates evidence from judgment.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que report structure makes findings auditable and decisions actionable?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Mandate/audience**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Report questions**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Outline/numbering**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Methods**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Implications**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Recommendations**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Appendices/citations**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Finding-evidence-recommendation chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source notes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart purpose**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cross-reference validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Executive/detail layering.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Sensitive appendix restricted. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing method disclosed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Recommendation separates evidence from judgment.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “report questions” cita evidência identificada, aplica “finding-evidence-recommendation chain”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Evidence-to-Report Architecture foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `report_schema_json.md` ou formato nativo equivalente: materializa **`report-schema.json`** e deve ser citado pelo artefato principal.
- `evidence_register_csv.md` ou formato nativo equivalente: materializa **`evidence-register.csv`** e deve ser citado pelo artefato principal.
- `recommendation_trace_csv.md` ou formato nativo equivalente: materializa **`recommendation-trace.csv`** e deve ser citado pelo artefato principal.
- `docx_pdf_builders.md` ou formato nativo equivalente: materializa **DOCX/PDF builders** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: traceability 25, structure 20, analysis 20, actionability 20, production quality 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ISO 2145 Documentation Numbering**, ISO (standard, força: primary). Aplicação: Stable section hierarchy. Localizador: https://www.iso.org/standard/6937.html. Consulta: 2026-08-24.
2. **GOV.UK Style Guide**, UK Government Digital Service (official, força: primary). Aplicação: Readable, consistent professional language. Localizador: https://www.gov.uk/guidance/style-guide. Consulta: 2026-08-24.
3. **Storytelling with Data**, Cole Nussbaumer Knaflic (book, força: canonical). Aplicação: Chart choice, attention and explanatory narrative. Localizador: Wiley, 2015, ISBN 9781119002253. Consulta: 2026-08-24.
