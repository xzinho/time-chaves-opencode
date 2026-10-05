---
name: sales-enablement
description: "Executa Behavior-Readiness System para responder: que comportamento de qual papel precisa mudar para mover qual outcome?"
---

# Sales Enablement

## Escopo e gatilhos

Use quando a decisão real for: **que comportamento de qual papel precisa mudar para mover qual outcome?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Behavior-Readiness System**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Behavior-Readiness System

1. **Business outcome**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Role/behavior map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Baseline**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Content/process/tool gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Practice/coaching**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Certification**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Field reinforcement**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Leading/lagging evaluation.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Competency matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Spaced practice**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Roleplay rubric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Manager coaching loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Kirkpatrick 1–4**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Asset usage telemetry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Content is not enablement without behavior. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Certification expires. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Poor process is not solved by training.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: outcome alignment 25, role specificity 20, practice 20, reinforcement 15, measurement 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `competency_matrix_xlsx.md` ou formato nativo equivalente: materializa **`competency-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `certification_rubric_yaml.md` ou formato nativo equivalente: materializa **`certification-rubric.yaml`** e deve ser citado pelo artefato principal.
- `asset_map_csv.md` ou formato nativo equivalente: materializa **`asset-map.csv`** e deve ser citado pelo artefato principal.
- `reinforcement_calendar.md` ou formato nativo equivalente: materializa **reinforcement calendar** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **What is Sales Enablement?**, Sales Enablement Collective (official, força: primary). Aplicação: Capability, content, coaching and measurement charter. Localizador: https://www.salesenablementcollective.com/what-is-sales-enablement/. Consulta: 2026-08-24.
2. **Sales Enablement 3.0**, Roderick Jefferson (book, força: recognized). Aplicação: Role-based readiness and behavior change. Localizador: Kogan Page, 2020, ISBN 9781789664737. Consulta: 2026-08-24.
3. **Kirkpatrick Model**, Kirkpatrick Partners (official, força: primary). Aplicação: Reaction, learning, behavior and results evaluation. Localizador: https://www.kirkpatrickpartners.com/the-kirkpatrick-model/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
