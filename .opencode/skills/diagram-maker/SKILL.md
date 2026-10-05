---
name: diagram-maker
description: "Executa Notation-Semantics Pipeline para responder: qual notação responde à pergunta e que regras impedem ambiguidade?"
---

# Diagram Maker

## Escopo e gatilhos

Use quando a decisão real for: **qual notação responde à pergunta e que regras impedem ambiguidade?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Notation-Semantics Pipeline**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Notation-Semantics Pipeline

1. **Audiência/pergunta**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Selecionar bpmn/uml/c4/flow/er**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Definir grammar**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Modelar happy path**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Exceptions**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Lint semântico**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Render**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Legenda e source.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Consistent direction**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Crossing minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic shapes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Explicit boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Exception paths**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Diagram lint.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Misturar notações só com legenda. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bpmn sem eventos não vira flowchart decorativo. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Informação sensível é sanitizada.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: semântica 30, completude 20, legibilidade 20, consistência 15, editabilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `notation_decision_tree_yaml.md` ou formato nativo equivalente: materializa **`notation-decision-tree.yaml`** e deve ser citado pelo artefato principal.
- `diagram_source.md` ou formato nativo equivalente: materializa **`diagram-source`** e deve ser citado pelo artefato principal.
- `lint_rules_yaml.md` ou formato nativo equivalente: materializa **`lint-rules.yaml`** e deve ser citado pelo artefato principal.
- `legend_md.md` ou formato nativo equivalente: materializa **`legend.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **BPMN 2.0.2**, Object Management Group (standard, força: primary). Aplicação: Process-event-gateway semantics. Localizador: https://www.omg.org/spec/BPMN/2.0.2/. Consulta: 2026-08-24.
2. **UML 2.5.1**, Object Management Group (standard, força: primary). Aplicação: Structural and behavioral diagram semantics. Localizador: https://www.omg.org/spec/UML/2.5.1/. Consulta: 2026-08-24.
3. **Mermaid**, Mermaid (github, força: mature). Aplicação: Text-source diagrams with deterministic rendering. Localizador: https://github.com/mermaid-js/mermaid. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
