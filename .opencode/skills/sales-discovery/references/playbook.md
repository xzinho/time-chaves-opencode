# Playbook operacional — Behavior-to-Gap Conversation

## Pergunta de controle

existe problema material, processo de decisão e próximo passo mútuo?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **account hypothesis** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **SPIN** responde à pergunta sem extrapolar o dado? Se não, selecione **evidence recap.** e declare a troca.
3. Há uma destas exceções: early exploratory call avoids interrogation; no pain/priority exits cleanly; procurement details follow value discovery.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **existe problema material, processo de decisão e próximo passo mútuo?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Account hypothesis**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Agenda/permission**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Current behavior**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Problem/impact**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Desired state**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Past attempts**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Stakeholders/process**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Priority/timing**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Summarize/confirm**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Mutual next step.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Spin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mom test behavior questions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gap quantification**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Silence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mirroring**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence recap.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Early exploratory call avoids interrogation. Marque a condição no artefato e acione o gate indicado antes do handoff.
- No pain/priority exits cleanly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Procurement details follow value discovery.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “agenda/permission” cita evidência identificada, aplica “SPIN”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Behavior-to-Gap Conversation foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `discovery_plan_md.md` ou formato nativo equivalente: materializa **`discovery-plan.md`** e deve ser citado pelo artefato principal.
- `question_bank_yaml.md` ou formato nativo equivalente: materializa **`question-bank.yaml`** e deve ser citado pelo artefato principal.
- `gap_map_csv.md` ou formato nativo equivalente: materializa **`gap-map.csv`** e deve ser citado pelo artefato principal.
- `call_evidence_next_step_note.md` ou formato nativo equivalente: materializa **call evidence/next-step note** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: evidence quality 25, depth 20, listening 20, qualification 15, mutual action 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Situation-problem-implication-need payoff sequencing. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Mom Test**, Rob Fitzpatrick (book, força: canonical). Aplicação: Behavioral evidence and avoidance of leading questions. Localizador: CreateSpace, 2013, ISBN 9781492180746. Consulta: 2026-08-24.
3. **Sales Rep Training**, Salesforce Trailhead (official, força: primary). Aplicação: Observable discovery preparation, questioning and confirmation. Localizador: https://trailhead.salesforce.com/content/learn/modules/sales-rep-training. Consulta: 2026-08-24.
