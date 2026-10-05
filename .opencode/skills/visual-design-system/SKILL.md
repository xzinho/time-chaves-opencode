---
name: visual-design-system
description: "Executa Token-Component-Governance para responder: what shared rules reduce inconsistency while enabling branded product expression?"
---

# Visual Design System

## Escopo e gatilhos

Use quando a decisão real for: **what shared rules reduce inconsistency while enabling branded product expression?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Token-Component-Governance**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Token-Component-Governance

1. **Product audit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Principles**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Primitive/semantic/component tokens**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Component anatomy/states**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Documentation/examples**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Versioning/contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Adoption metrics.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Token aliases**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant constraints**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contrast/focus tests**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual regression**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deprecation policy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- One-off signature component needs rationale. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Brand token never bypasses contrast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Breaking token has migration path.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: coherence 20, coverage 20, accessibility 20, implementation 20, governance/adoption 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `tokens_json.md` ou formato nativo equivalente: materializa **`tokens.json`** e deve ser citado pelo artefato principal.
- `component_contract_schema_json.md` ou formato nativo equivalente: materializa **`component-contract.schema.json`** e deve ser citado pelo artefato principal.
- `state_matrix_csv.md` ou formato nativo equivalente: materializa **`state-matrix.csv`** e deve ser citado pelo artefato principal.
- `migration_changelog_and_visual_fixtures.md` ou formato nativo equivalente: materializa **migration/changelog and visual fixtures** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Design Tokens Format Module 2025.10**, W3C Design Tokens Community Group (official, força: primary). Aplicação: Portable token names, types and references. Localizador: https://www.designtokens.org/tr/drafts/format/. Consulta: 2026-08-24.
2. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Accessible component and color constraints. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.
3. **Atomic Design**, Brad Frost (book, força: canonical). Aplicação: Component hierarchy and system governance. Localizador: https://atomicdesign.bradfrost.com/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
