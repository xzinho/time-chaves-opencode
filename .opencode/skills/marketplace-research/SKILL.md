---
name: marketplace-research
description: "Executa Multi-Signal Category Scan para responder: categoria/produto mostra oportunidade defensável após fees, competição e operação?"
---

# Marketplace Research

## Escopo e gatilhos

Use quando a decisão real for: **categoria/produto mostra oportunidade defensável após fees, competição e operação?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Multi-Signal Category Scan**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Multi-Signal Category Scan

1. **Category taxonomy**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Query set**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Demand signals**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Seller/listing census**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Review mining**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Fee/logistics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Price/rank snapshots**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Validation test.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Signal triangulation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Review jobs/pains coding**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Assortment map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Seller concentration**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Temporal snapshots.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Rank não é volume. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Scraping obedece termos. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Páginas personalizadas registram região/login. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Promoção separada de preço regular.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cobertura 20, triangulação 25, economia 20, gap 20, limitações 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `marketplace_snapshot_csv.md` ou formato nativo equivalente: materializa **`marketplace-snapshot.csv`** e deve ser citado pelo artefato principal.
- `review_codebook_yaml.md` ou formato nativo equivalente: materializa **`review-codebook.yaml`** e deve ser citado pelo artefato principal.
- `assortment_map_xlsx.md` ou formato nativo equivalente: materializa **`assortment-map.xlsx`** e deve ser citado pelo artefato principal.
- `source_log.md` ou formato nativo equivalente: materializa **source log** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Amazon Best Sellers**, Amazon (official, força: primary). Aplicação: Observable rank/category signal with timestamp caveat. Localizador: https://www.amazon.com.br/gp/bestsellers. Consulta: 2026-08-24.
2. **Google Trends Help**, Google (official, força: primary). Aplicação: Normalized demand direction and geographic comparison. Localizador: https://support.google.com/trends/. Consulta: 2026-08-24.
3. **Platform Revolution**, Parker, Van Alstyne, Choudary (book, força: canonical). Aplicação: Marketplace sides, network effects and governance. Localizador: Norton, 2016, ISBN 9780393249132. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
