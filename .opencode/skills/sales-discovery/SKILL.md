---
name: sales-discovery
description: "Executa Behavior-to-Gap Conversation para responder: existe problema material, processo de decisão e próximo passo mútuo?"
---

# Sales Discovery

## Escopo e gatilhos

Use quando a decisão real for: **existe problema material, processo de decisão e próximo passo mútuo?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Behavior-to-Gap Conversation**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Behavior-to-Gap Conversation

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

## Técnicas de campo

- **Spin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mom test behavior questions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gap quantification**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Silence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mirroring**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence recap.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Early exploratory call avoids interrogation. Marque a condição no artefato e acione o gate indicado antes do handoff.
- No pain/priority exits cleanly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Procurement details follow value discovery.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: evidence quality 25, depth 20, listening 20, qualification 15, mutual action 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `discovery_plan_md.md` ou formato nativo equivalente: materializa **`discovery-plan.md`** e deve ser citado pelo artefato principal.
- `question_bank_yaml.md` ou formato nativo equivalente: materializa **`question-bank.yaml`** e deve ser citado pelo artefato principal.
- `gap_map_csv.md` ou formato nativo equivalente: materializa **`gap-map.csv`** e deve ser citado pelo artefato principal.
- `call_evidence_next_step_note.md` ou formato nativo equivalente: materializa **call evidence/next-step note** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Situation-problem-implication-need payoff sequencing. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Mom Test**, Rob Fitzpatrick (book, força: canonical). Aplicação: Behavioral evidence and avoidance of leading questions. Localizador: CreateSpace, 2013, ISBN 9781492180746. Consulta: 2026-08-24.
3. **Sales Rep Training**, Salesforce Trailhead (official, força: primary). Aplicação: Observable discovery preparation, questioning and confirmation. Localizador: https://trailhead.salesforce.com/content/learn/modules/sales-rep-training. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
