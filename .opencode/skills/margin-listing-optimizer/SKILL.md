---
name: margin-listing-optimizer
description: "Executa SKU Contribution Engine para responder: qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails?"
---

# Margin Listing Optimizer

## Escopo e gatilhos

Use quando a decisão real for: **qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **SKU Contribution Engine**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método SKU Contribution Engine

1. **Sku/canal**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Fee/tax/shipping/returns/ads waterfall**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Current margin**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Competitor/content audit**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Price scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Listing experiments**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Guardrails**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Monitor.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Contribution margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Break-even roas**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Return-adjusted margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Price ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Content completeness**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sensitivity grid.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Fee muda por categoria. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Imposto depende do regime. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Buy-box/rank são proxies. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Estoque escasso altera objetivo.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cálculo 30, completude de custo 20, oportunidade do listing 15, cenário 20, guardrails 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `sku_waterfall_xlsx.md` ou formato nativo equivalente: materializa **`sku-waterfall.xlsx`** e deve ser citado pelo artefato principal.
- `fee_table_csv.md` ou formato nativo equivalente: materializa **`fee-table.csv`** e deve ser citado pelo artefato principal.
- `listing_scorecard_yaml.md` ou formato nativo equivalente: materializa **`listing-scorecard.yaml`** e deve ser citado pelo artefato principal.
- `experiment_backlog.md` ou formato nativo equivalente: materializa **experiment backlog** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Amazon Seller Fees**, Amazon (official, força: primary). Aplicação: Marketplace fee and fulfillment-cost inventory. Localizador: https://sell.amazon.com/pricing. Consulta: 2026-08-24.
2. **Mercado Livre Custos de Venda**, Mercado Livre (official, força: primary). Aplicação: Brazilian marketplace commission and shipping constraints. Localizador: https://www.mercadolivre.com.br/ajuda/Custos-de-vender-um-produto_870. Consulta: 2026-08-24.
3. **Pricing and Revenue Optimization**, Robert Phillips (book, força: canonical). Aplicação: Price-response, contribution and constrained optimization. Localizador: Stanford University Press, 2005, ISBN 9780804746984. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
