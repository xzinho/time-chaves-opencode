---
name: idea-scoring
description: "Executa Evidence-Calibrated Portfolio para responder: investir, experimentar, estacionar ou matar uma ideia?"
---

# Idea Scoring

## Escopo e gatilhos

Use quando a decisão real for: **investir, experimentar, estacionar ou matar uma ideia?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Evidence-Calibrated Portfolio**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Evidence-Calibrated Portfolio

1. **Define outcome/unit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Normalize ideas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Score reach/impact/confidence/effort/strategic fit/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Evidence grade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Uncertainty penalty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Rank**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Portfolio balance**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Next test.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Anchored scales**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence decay**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted score**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sensitivity to weights**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dominance check.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Scores próximos viram empate. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alta upside/baixa confiança recebe experimento. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Veto legal/security sobrepõe ranking.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: definição 15, evidência 25, calibração 20, transparência 20, ação 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `score_rubric_yaml.md` ou formato nativo equivalente: materializa **`score-rubric.yaml`** e deve ser citado pelo artefato principal.
- `idea_portfolio_xlsx.md` ou formato nativo equivalente: materializa **`idea-portfolio.xlsx`** e deve ser citado pelo artefato principal.
- `evidence_card_md.md` ou formato nativo equivalente: materializa **`evidence-card.md`** e deve ser citado pelo artefato principal.
- `sensitivity_plot.md` ou formato nativo equivalente: materializa **sensitivity plot** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Lean Startup**, Eric Ries (book, força: canonical). Aplicação: Leap-of-faith assumptions and validated learning. Localizador: Crown Business, 2011, ISBN 9780307887894. Consulta: 2026-08-24.
2. **Testing Business Ideas**, David Bland and Alexander Osterwalder (book, força: canonical). Aplicação: Assumption mapping and experiment selection. Localizador: Wiley, 2019, ISBN 9781119551447. Consulta: 2026-08-24.
3. **RICE Prioritization**, Intercom (official, força: primary). Aplicação: Reach-impact-confidence-effort normalization. Localizador: https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
