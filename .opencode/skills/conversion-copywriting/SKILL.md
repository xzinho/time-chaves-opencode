---
name: conversion-copywriting
description: "Executa Awareness-Proof Sequence para responder: que próxima crença o leitor precisa aceitar para agir?"
---

# Conversion Copywriting

## Escopo e gatilhos

Use quando a decisão real for: **que próxima crença o leitor precisa aceitar para agir?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Awareness-Proof Sequence**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Awareness-Proof Sequence

1. **Voice-of-customer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Estágio/sofisticação**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desired action**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Belief chain**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Headline/promessa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mecanismo**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Prova**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objection handling**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Substantiation/read-aloud.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Message hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Specificity ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk reversal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Friction audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant isolation.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Prova fraca reduz claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mercado saturado exige mecanismo/distinção. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Urgência deve ser factual.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: relevância 20, clareza 20, credibilidade 20, progressão 15, oferta 15, ética/compliance 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `voc_bank_csv.md` ou formato nativo equivalente: materializa **`voc-bank.csv`** e deve ser citado pelo artefato principal.
- `belief_chain_yaml.md` ou formato nativo equivalente: materializa **`belief-chain.yaml`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `variant_sheet.md` ou formato nativo equivalente: materializa **variant sheet** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Scientific Advertising**, Claude Hopkins (book, força: canonical). Aplicação: Specific claims, reason-why and measurable response. Localizador: Lord & Thomas, 1923; public domain. Consulta: 2026-08-24.
2. **Breakthrough Advertising**, Eugene Schwartz (book, força: canonical). Aplicação: Awareness stages and market sophistication. Localizador: Boardroom, 1966, ISBN 9780887232984. Consulta: 2026-08-24.
3. **Truth In Advertising**, US FTC (official, força: primary). Aplicação: Claim substantiation and deception guardrails. Localizador: https://www.ftc.gov/news-events/topics/truth-advertising. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
