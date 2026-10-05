# Playbook operacional — Notation-Semantics Pipeline

## Pergunta de controle

qual notação responde à pergunta e que regras impedem ambiguidade?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **audiência/pergunta** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **consistent direction** responde à pergunta sem extrapolar o dado? Se não, selecione **diagram lint.** e declare a troca.
3. Há uma destas exceções: misturar notações só com legenda; BPMN sem eventos não vira flowchart decorativo; informação sensível é sanitizada.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual notação responde à pergunta e que regras impedem ambiguidade?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Audiência/pergunta**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Selecionar bpmn/uml/c4/flow/er**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Definir grammar**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Modelar happy path**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Exceptions**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Lint semântico**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Render**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Legenda e source.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Consistent direction**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Crossing minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic shapes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Explicit boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Exception paths**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Diagram lint.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Misturar notações só com legenda. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bpmn sem eventos não vira flowchart decorativo. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Informação sensível é sanitizada.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “selecionar BPMN/UML/C4/flow/ER” cita evidência identificada, aplica “consistent direction”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Notation-Semantics Pipeline foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `notation_decision_tree_yaml.md` ou formato nativo equivalente: materializa **`notation-decision-tree.yaml`** e deve ser citado pelo artefato principal.
- `diagram_source.md` ou formato nativo equivalente: materializa **`diagram-source`** e deve ser citado pelo artefato principal.
- `lint_rules_yaml.md` ou formato nativo equivalente: materializa **`lint-rules.yaml`** e deve ser citado pelo artefato principal.
- `legend_md.md` ou formato nativo equivalente: materializa **`legend.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: semântica 30, completude 20, legibilidade 20, consistência 15, editabilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **BPMN 2.0.2**, Object Management Group (standard, força: primary). Aplicação: Process-event-gateway semantics. Localizador: https://www.omg.org/spec/BPMN/2.0.2/. Consulta: 2026-08-24.
2. **UML 2.5.1**, Object Management Group (standard, força: primary). Aplicação: Structural and behavioral diagram semantics. Localizador: https://www.omg.org/spec/UML/2.5.1/. Consulta: 2026-08-24.
3. **Mermaid**, Mermaid (github, força: mature). Aplicação: Text-source diagrams with deterministic rendering. Localizador: https://github.com/mermaid-js/mermaid. Consulta: 2026-08-24.
