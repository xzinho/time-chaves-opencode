---
name: web-research-with-sources
description: "Executa Reproducible Evidence Synthesis para responder: what does the best available evidence support, contradict or leave uncertain?"
---

# Web Research With Sources

## Escopo e gatilhos

Use quando a decisão real for: **what does the best available evidence support, contradict or leave uncertain?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Reproducible Evidence Synthesis**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Reproducible Evidence Synthesis

1. **Protocol/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Search strings/sources/date**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inclusion/exclusion**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Capture metadata**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Screen**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Extract claims/quotes/context**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Assess authority/recency/directness**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Triangulate**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Synthesize with confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Bibliography/limitations.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Prisma-like log**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Primary-source preference**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Lateral reading**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contradiction table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence labels.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Inaccessible source listed, not guessed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Snippet is not evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dynamic page gets timestamp/archive. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ai summary never cited as source.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: reproducibility 25, source strength 25, claim traceability 25, contradiction/limits 15, synthesis 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `search_log_csv.md` ou formato nativo equivalente: materializa **`search-log.csv`** e deve ser citado pelo artefato principal.
- `sources_json.md` ou formato nativo equivalente: materializa **`sources.json`** e deve ser citado pelo artefato principal.
- `claim_evidence_csv.md` ou formato nativo equivalente: materializa **`claim-evidence.csv`** e deve ser citado pelo artefato principal.
- `limitations_md.md` ou formato nativo equivalente: materializa **`limitations.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **PRISMA 2020 Statement**, PRISMA (standard, força: primary). Aplicação: Transparent search, screening and inclusion trail. Localizador: https://www.prisma-statement.org/prisma-2020. Consulta: 2026-08-24.
2. **Evaluating Sources**, Library of Congress (official, força: primary). Aplicação: Authority, provenance and corroboration checks. Localizador: https://guides.loc.gov/evaluating-sources. Consulta: 2026-08-24.
3. **Web Annotation Data Model**, W3C (official, força: primary). Aplicação: Quote-level evidence anchors and provenance. Localizador: https://www.w3.org/TR/annotation-model/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
