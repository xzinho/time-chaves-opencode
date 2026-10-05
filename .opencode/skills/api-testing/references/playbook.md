# Playbook operacional — Contract-State-Oracles

## Pergunta de controle

que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **importar spec** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **equivalence partitioning** responde à pergunta sem extrapolar o dado? Se não, selecione **state model.** e declare a troca.
3. Há uma destas exceções: endpoint não idempotente usa sandbox; eventual consistency usa polling limitado; API sem spec gera shadow contract marcado como inferido.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Importar spec**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Inventariar operações/auth/estados**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Validar schema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Partitions e boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sequências stateful**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Negative/security**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Timeout/idempotency/retry**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Relatório de evidência.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Equivalence partitioning**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pairwise**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Property-based generation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metamorphic invariants**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consumer contract**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State model.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Endpoint não idempotente usa sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Eventual consistency usa polling limitado. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Api sem spec gera shadow contract marcado como inferido.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “inventariar operações/auth/estados” cita evidência identificada, aplica “equivalence partitioning”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Contract-State-Oracles foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `operation_inventory_json.md` ou formato nativo equivalente: materializa **`operation-inventory.json`** e deve ser citado pelo artefato principal.
- `state_machine_yaml.md` ou formato nativo equivalente: materializa **`state-machine.yaml`** e deve ser citado pelo artefato principal.
- `invariants_yaml.md` ou formato nativo equivalente: materializa **`invariants.yaml`** e deve ser citado pelo artefato principal.
- `corpus_de_payloads.md` ou formato nativo equivalente: materializa **corpus de payloads** e deve ser citado pelo artefato principal.
- `junit_report.md` ou formato nativo equivalente: materializa **JUnit report** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: cobertura de risco 25, qualidade de oráculo 25, determinismo 15, negativos 15, estado 10, evidência 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **OpenAPI Specification 3.1**, OpenAPI Initiative (standard, força: primary). Aplicação: Contract inventory and schema assertions. Localizador: https://spec.openapis.org/oas/v3.1.0. Consulta: 2026-08-24.
2. **RFC 9110 HTTP Semantics**, IETF (standard, força: primary). Aplicação: Status, method, caching and idempotency semantics. Localizador: https://www.rfc-editor.org/rfc/rfc9110. Consulta: 2026-08-24.
3. **Schemathesis**, Schemathesis (github, força: mature). Aplicação: Property-based tests from OpenAPI schemas. Localizador: https://github.com/schemathesis/schemathesis. Consulta: 2026-08-24.
