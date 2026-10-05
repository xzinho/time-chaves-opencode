---
name: executive-briefing
description: "Executa Decision-First Brief para responder: o que o executivo deve decidir, por quê agora e com qual consequência?"
---

# Executive Briefing

## Escopo e gatilhos

Use quando a decisão real for: **o que o executivo deve decidir, por quê agora e com qual consequência?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Decision-First Brief**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Decision-First Brief

1. **Decision statement**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **One-line answer**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Material facts**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Options/tradeoffs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Recommendation**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Risks/unknowns**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Explicit ask**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Owners/dates.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Pyramid logic**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Bluf**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fact/inference/assumption tags**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Option table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Red-team question.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Sem decisão vira status brief. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crise prioriza facts/time/owner. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Incerteza não é escondida por prosa.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: decisão 25, síntese 20, evidência 20, tradeoffs 15, ação 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `decision_brief_md.md` ou formato nativo equivalente: materializa **`decision-brief.md`** e deve ser citado pelo artefato principal.
- `fact_assumption_ledger_csv.md` ou formato nativo equivalente: materializa **`fact-assumption-ledger.csv`** e deve ser citado pelo artefato principal.
- `one_page_pdf.md` ou formato nativo equivalente: materializa **one-page PDF** e deve ser citado pelo artefato principal.
- `verbal_60_second_variant.md` ou formato nativo equivalente: materializa **verbal 60-second variant** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Pyramid Principle**, Barbara Minto (book, força: canonical). Aplicação: Answer-first logic and mutually exclusive support. Localizador: Financial Times Prentice Hall, 2009, ISBN 9780273710516. Consulta: 2026-08-24.
2. **Writing for GOV.UK**, UK Government Digital Service (official, força: primary). Aplicação: Concise audience-centered executive language. Localizador: https://www.gov.uk/guidance/content-design/writing-for-gov-uk. Consulta: 2026-08-24.
3. **Smart Brevity**, Jim VandeHei, Mike Allen, Roy Schwartz (book, força: recognized). Aplicação: Why-it-matters and scannable action architecture. Localizador: Workman, 2022, ISBN 9781523516971. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
