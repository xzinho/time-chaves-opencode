---
name: business-health-diagnostic
description: "Executa Causal Health Map para responder: qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?"
---

# Business Health Diagnostic

## Escopo e gatilhos

Use quando a decisão real for: **qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Causal Health Map**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Causal Health Map

1. **Outcomes/tendências**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Value model**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Drivers por mercado/cliente/operação/pessoas/finanças**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Symptom-to-cause tree**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Evidence/confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Constraints**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **30/60/90.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Driver tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Five-whys com evidência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Constraint map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capability maturity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Leading/lagging indicators.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Sazonalidade e choque externo são segmentados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Falta de baseline vira coleta. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Nota agregada nunca oculta falha crítica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: causalidade 25, evidência 25, materialidade 20, executabilidade 20, aprendizagem 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `driver_tree_yaml.md` ou formato nativo equivalente: materializa **`driver-tree.yaml`** e deve ser citado pelo artefato principal.
- `health_scorecard_xlsx.md` ou formato nativo equivalente: materializa **`health-scorecard.xlsx`** e deve ser citado pelo artefato principal.
- `constraint_register_csv.md` ou formato nativo equivalente: materializa **`constraint-register.csv`** e deve ser citado pelo artefato principal.
- `plano_30_60_90.md` ou formato nativo equivalente: materializa **plano 30/60/90** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **EFQM Model**, EFQM (standard, força: primary). Aplicação: Systemic diagnosis of direction, execution and results. Localizador: https://efqm.org/the-efqm-model/. Consulta: 2026-08-24.
2. **Business Model Canvas**, Strategyzer (official, força: primary). Aplicação: Business-model coherence map. Localizador: https://www.strategyzer.com/library/the-business-model-canvas. Consulta: 2026-08-24.
3. **Good Strategy/Bad Strategy**, Richard Rumelt (book, força: canonical). Aplicação: Diagnosis, guiding policy and coherent actions. Localizador: Crown Business, 2011, ISBN 9780307886231. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
