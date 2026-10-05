# Playbook operacional — Inputs-Logic-Outputs-Control

## Pergunta de controle

quais drivers explicam outputs e como o modelo reage a incerteza?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **objective/granularity** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **FAST conventions** responde à pergunta sem extrapolar o dado? Se não, selecione **balance and circularity checks.** e declare a troca.
3. Há uma destas exceções: circularidade só se documentada; histórico/projeção separados; hardcode em fórmula é blocker.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **quais drivers explicam outputs e como o modelo reage a incerteza?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Objective/granularity**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Timeline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Assumptions register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Inputs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Calculation blocks**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Statements/outputs**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Sensitivities/scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Integrity checks**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Review.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Fast conventions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Corkscrew schedules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sign/unit discipline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Scenario switches**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Data tables**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance and circularity checks.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Circularidade só se documentada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Histórico/projeção separados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Hardcode em fórmula é blocker.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “timeline” cita evidência identificada, aplica “FAST conventions”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Inputs-Logic-Outputs-Control foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `workbook_com_estilos_sem_nticos.md` ou formato nativo equivalente: materializa **workbook com estilos semânticos** e deve ser citado pelo artefato principal.
- `assumptions_csv.md` ou formato nativo equivalente: materializa **`assumptions.csv`** e deve ser citado pelo artefato principal.
- `model_checks_yaml.md` ou formato nativo equivalente: materializa **`model-checks.yaml`** e deve ser citado pelo artefato principal.
- `scenario_summary.md` ou formato nativo equivalente: materializa **scenario summary** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: correção 30, transparência 20, estrutura 20, controle 15, decisão 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Flexible, appropriate, structured and transparent models. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Principles of Financial Modelling**, Michael Rees (book, força: canonical). Aplicação: Model architecture, checks and scenarios. Localizador: Wiley, 2018, ISBN 9781118904015. Consulta: 2026-08-24.
3. **Financial Modeling, 4th ed.**, Simon Benninga (book, força: canonical). Aplicação: Spreadsheet model architecture, valuation and auditability. Localizador: MIT Press, 2014, ISBN 9780262027281. Consulta: 2026-08-24.
