---
name: api-testing
description: "Executa Contract-State-Oracles para responder: que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?"
---

# Api Testing

## Escopo e gatilhos

Use quando a decisão real for: **que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Contract-State-Oracles**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Contract-State-Oracles

1. **Importar spec**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Inventariar operações/auth/estados**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Validar schema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Partitions e boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sequências stateful**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Negative/security**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Timeout/idempotency/retry**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Relatório de evidência.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Equivalence partitioning**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pairwise**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Property-based generation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metamorphic invariants**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consumer contract**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State model.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Endpoint não idempotente usa sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Eventual consistency usa polling limitado. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Api sem spec gera shadow contract marcado como inferido.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cobertura de risco 25, qualidade de oráculo 25, determinismo 15, negativos 15, estado 10, evidência 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `operation_inventory_json.md` ou formato nativo equivalente: materializa **`operation-inventory.json`** e deve ser citado pelo artefato principal.
- `state_machine_yaml.md` ou formato nativo equivalente: materializa **`state-machine.yaml`** e deve ser citado pelo artefato principal.
- `invariants_yaml.md` ou formato nativo equivalente: materializa **`invariants.yaml`** e deve ser citado pelo artefato principal.
- `corpus_de_payloads.md` ou formato nativo equivalente: materializa **corpus de payloads** e deve ser citado pelo artefato principal.
- `junit_report.md` ou formato nativo equivalente: materializa **JUnit report** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **OpenAPI Specification 3.1**, OpenAPI Initiative (standard, força: primary). Aplicação: Contract inventory and schema assertions. Localizador: https://spec.openapis.org/oas/v3.1.0. Consulta: 2026-08-24.
2. **RFC 9110 HTTP Semantics**, IETF (standard, força: primary). Aplicação: Status, method, caching and idempotency semantics. Localizador: https://www.rfc-editor.org/rfc/rfc9110. Consulta: 2026-08-24.
3. **Schemathesis**, Schemathesis (github, força: mature). Aplicação: Property-based tests from OpenAPI schemas. Localizador: https://github.com/schemathesis/schemathesis. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
