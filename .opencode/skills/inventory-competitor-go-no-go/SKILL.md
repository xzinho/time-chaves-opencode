---
name: inventory-competitor-go-no-go
description: "Executa Market-Inventory Gate para responder: entrar, testar condicionado ou não entrar em uma categoria/SKU?"
---

# Inventory Competitor Go No Go

## Escopo e gatilhos

Use quando a decisão real for: **entrar, testar condicionado ou não entrar em uma categoria/SKU?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Market-Inventory Gate**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Market-Inventory Gate

1. **Market boundary**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Substitutes/competitors**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Demand evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Supply/price/fees**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Inventory cash cycle**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Contribution scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Strategic fit**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Kill criteria**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Five forces**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Substitution test**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Landed-cost waterfall**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sell-through/stockout/markdown scenarios**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted evidence.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Rank sem vendas é proxy. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Sazonalidade exige cohort temporal. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Moq e lead time podem vetar margem nominal.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: mercado 20, economia 25, estoque/caixa 20, evidência 20, decisão 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `competitor_inventory_csv.md` ou formato nativo equivalente: materializa **`competitor-inventory.csv`** e deve ser citado pelo artefato principal.
- `landed_cost_xlsx.md` ou formato nativo equivalente: materializa **`landed-cost.xlsx`** e deve ser citado pelo artefato principal.
- `kill_criteria_yaml.md` ou formato nativo equivalente: materializa **`kill-criteria.yaml`** e deve ser citado pelo artefato principal.
- `go_no_go_memo.md` ou formato nativo equivalente: materializa **go/no-go memo** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Competitive Strategy**, Michael E. Porter (book, força: canonical). Aplicação: Industry forces and strategic positioning. Localizador: Free Press, 1980, ISBN 9780684841489. Consulta: 2026-08-24.
2. **Commission Notice on the definition of the relevant market (2024)**, European Commission (official, força: primary). Aplicação: Relevant-market and substitution boundaries. Localizador: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52024XC01645. Consulta: 2026-08-24.
3. **The Art of Profitability**, Adrian Slywotzky (book, força: recognized). Aplicação: Profit-model and inventory-risk lenses. Localizador: Warner Business, 2002, ISBN 9780446692274. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
