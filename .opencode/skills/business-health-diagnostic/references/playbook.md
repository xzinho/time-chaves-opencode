# Playbook operacional — Causal Health Map

## Pergunta de controle

qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **outcomes/tendências** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **driver tree** responde à pergunta sem extrapolar o dado? Se não, selecione **leading/lagging indicators.** e declare a troca.
3. Há uma destas exceções: sazonalidade e choque externo são segmentados; falta de baseline vira coleta; nota agregada nunca oculta falha crítica.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Outcomes/tendências**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Value model**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Drivers por mercado/cliente/operação/pessoas/finanças**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Symptom-to-cause tree**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Evidence/confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Constraints**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **30/60/90.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Driver tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Five-whys com evidência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Constraint map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capability maturity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Leading/lagging indicators.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Sazonalidade e choque externo são segmentados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Falta de baseline vira coleta. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Nota agregada nunca oculta falha crítica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “value model” cita evidência identificada, aplica “driver tree”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Causal Health Map foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `driver_tree_yaml.md` ou formato nativo equivalente: materializa **`driver-tree.yaml`** e deve ser citado pelo artefato principal.
- `health_scorecard_xlsx.md` ou formato nativo equivalente: materializa **`health-scorecard.xlsx`** e deve ser citado pelo artefato principal.
- `constraint_register_csv.md` ou formato nativo equivalente: materializa **`constraint-register.csv`** e deve ser citado pelo artefato principal.
- `plano_30_60_90.md` ou formato nativo equivalente: materializa **plano 30/60/90** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: causalidade 25, evidência 25, materialidade 20, executabilidade 20, aprendizagem 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **EFQM Model**, EFQM (standard, força: primary). Aplicação: Systemic diagnosis of direction, execution and results. Localizador: https://efqm.org/the-efqm-model/. Consulta: 2026-08-24.
2. **Business Model Canvas**, Strategyzer (official, força: primary). Aplicação: Business-model coherence map. Localizador: https://www.strategyzer.com/library/the-business-model-canvas. Consulta: 2026-08-24.
3. **Good Strategy/Bad Strategy**, Richard Rumelt (book, força: canonical). Aplicação: Diagnosis, guiding policy and coherent actions. Localizador: Crown Business, 2011, ISBN 9780307886231. Consulta: 2026-08-24.
