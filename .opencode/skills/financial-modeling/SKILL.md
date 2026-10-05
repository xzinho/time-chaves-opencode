---
name: financial-modeling
description: "Executa Inputs-Logic-Outputs-Control para responder: quais drivers explicam outputs e como o modelo reage a incerteza?"
---

# Financial Modeling

## Escopo e gatilhos

Use quando a decisão real for: **quais drivers explicam outputs e como o modelo reage a incerteza?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Inputs-Logic-Outputs-Control**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Inputs-Logic-Outputs-Control

1. **Objective/granularity**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Timeline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Assumptions register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Inputs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Calculation blocks**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Statements/outputs**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Sensitivities/scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Integrity checks**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Review.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Fast conventions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Corkscrew schedules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sign/unit discipline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Scenario switches**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Data tables**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance and circularity checks.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Circularidade só se documentada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Histórico/projeção separados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Hardcode em fórmula é blocker.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: correção 30, transparência 20, estrutura 20, controle 15, decisão 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `workbook_com_estilos_sem_nticos.md` ou formato nativo equivalente: materializa **workbook com estilos semânticos** e deve ser citado pelo artefato principal.
- `assumptions_csv.md` ou formato nativo equivalente: materializa **`assumptions.csv`** e deve ser citado pelo artefato principal.
- `model_checks_yaml.md` ou formato nativo equivalente: materializa **`model-checks.yaml`** e deve ser citado pelo artefato principal.
- `scenario_summary.md` ou formato nativo equivalente: materializa **scenario summary** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Flexible, appropriate, structured and transparent models. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Principles of Financial Modelling**, Michael Rees (book, força: canonical). Aplicação: Model architecture, checks and scenarios. Localizador: Wiley, 2018, ISBN 9781118904015. Consulta: 2026-08-24.
3. **Financial Modeling, 4th ed.**, Simon Benninga (book, força: canonical). Aplicação: Spreadsheet model architecture, valuation and auditability. Localizador: MIT Press, 2014, ISBN 9780262027281. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
