# Playbook operacional — Behavior-Readiness System

## Pergunta de controle

que comportamento de qual papel precisa mudar para mover qual outcome?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **business outcome** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **competency matrix** responde à pergunta sem extrapolar o dado? Se não, selecione **asset usage telemetry.** e declare a troca.
3. Há uma destas exceções: content is not enablement without behavior; certification expires; poor process is not solved by training.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que comportamento de qual papel precisa mudar para mover qual outcome?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Business outcome**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Role/behavior map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Baseline**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Content/process/tool gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Practice/coaching**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Certification**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Field reinforcement**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Leading/lagging evaluation.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Competency matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Spaced practice**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Roleplay rubric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Manager coaching loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Kirkpatrick 1–4**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Asset usage telemetry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Content is not enablement without behavior. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Certification expires. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Poor process is not solved by training.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “role/behavior map” cita evidência identificada, aplica “competency matrix”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Behavior-Readiness System foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `competency_matrix_xlsx.md` ou formato nativo equivalente: materializa **`competency-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `certification_rubric_yaml.md` ou formato nativo equivalente: materializa **`certification-rubric.yaml`** e deve ser citado pelo artefato principal.
- `asset_map_csv.md` ou formato nativo equivalente: materializa **`asset-map.csv`** e deve ser citado pelo artefato principal.
- `reinforcement_calendar.md` ou formato nativo equivalente: materializa **reinforcement calendar** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: outcome alignment 25, role specificity 20, practice 20, reinforcement 15, measurement 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **What is Sales Enablement?**, Sales Enablement Collective (official, força: primary). Aplicação: Capability, content, coaching and measurement charter. Localizador: https://www.salesenablementcollective.com/what-is-sales-enablement/. Consulta: 2026-08-24.
2. **Sales Enablement 3.0**, Roderick Jefferson (book, força: recognized). Aplicação: Role-based readiness and behavior change. Localizador: Kogan Page, 2020, ISBN 9781789664737. Consulta: 2026-08-24.
3. **Kirkpatrick Model**, Kirkpatrick Partners (official, força: primary). Aplicação: Reaction, learning, behavior and results evaluation. Localizador: https://www.kirkpatrickpartners.com/the-kirkpatrick-model/. Consulta: 2026-08-24.
