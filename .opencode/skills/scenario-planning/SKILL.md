---
name: scenario-planning
description: "Executa Uncertainty-to-Options para responder: quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?"
---

# Scenario Planning

## Escopo e gatilhos

Use quando a decisão real for: **quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Uncertainty-to-Options**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Uncertainty-to-Options

1. **Focal question/horizon**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Environmental scan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Forces**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Predetermineds**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Rank impact/uncertainty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Scenario logics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Narratives/quantification**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Strategy wind-tunnel**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Options**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Indicators/triggers.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **2×2 only when orthogonal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Morphological scenarios**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Causal loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consistency check**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Signposts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **No-regret/hedge/options.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Scenario is not forecast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Black swan gets contingency, not fake probability. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Contradictions trigger rewrite.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: plausibility 20, distinctness 20, causal coherence 20, strategic stress 20, indicators 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `driver_register_csv.md` ou formato nativo equivalente: materializa **`driver-register.csv`** e deve ser citado pelo artefato principal.
- `scenario_logic_yaml.md` ou formato nativo equivalente: materializa **`scenario-logic.yaml`** e deve ser citado pelo artefato principal.
- `wind_tunnel_xlsx.md` ou formato nativo equivalente: materializa **`wind-tunnel.xlsx`** e deve ser citado pelo artefato principal.
- `signpost_dashboard_md.md` ou formato nativo equivalente: materializa **`signpost-dashboard.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Art of the Long View**, Peter Schwartz (book, força: canonical). Aplicação: Driving forces, critical uncertainties and narratives. Localizador: Doubleday, 1991, ISBN 9780385267328. Consulta: 2026-08-24.
2. **Scenario Planning Guide**, UK Government Office for Science (official, força: primary). Aplicação: Futures toolkit and policy stress-testing. Localizador: https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts. Consulta: 2026-08-24.
3. **Thinking in Systems**, Donella Meadows (book, força: canonical). Aplicação: Feedback loops, delays and leverage points. Localizador: Chelsea Green, 2008, ISBN 9781603580557. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
