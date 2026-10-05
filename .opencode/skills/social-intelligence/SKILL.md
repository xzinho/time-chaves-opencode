---
name: social-intelligence
description: "Executa Trace-to-Narrative Observatory para responder: que narrativas/sinais importam, quão confiáveis são e que ação justificam?"
---

# Social Intelligence

## Escopo e gatilhos

Use quando a decisão real for: **que narrativas/sinais importam, quão confiáveis são e que ação justificam?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Trace-to-Narrative Observatory**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Trace-to-Narrative Observatory

1. **Decision/query book**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Platform/sample plan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Collect with timestamps**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Dedupe/entities**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code themes/stance/format**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Velocity/novelty**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Corroborate**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Narrative map**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Implications/caveats.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Purposive sampling**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query expansion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Codebook agreement**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source diversity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Anomaly detection**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Narrative lifecycle.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Engagement unavailable means no traction claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/coordination suspected is flagged. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Social trace is not population opinion.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: provenance 25, coverage 20, coding 20, corroboration 20, caveats/action 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `query_book_yaml.md` ou formato nativo equivalente: materializa **`query-book.yaml`** e deve ser citado pelo artefato principal.
- `source_ledger_jsonl.md` ou formato nativo equivalente: materializa **`source-ledger.jsonl`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `narrative_map_and_dedupe_state.md` ou formato nativo equivalente: materializa **narrative map and dedupe state** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (official, força: primary). Aplicação: Ethical observation and reporting. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **An Introduction to Social Media Research**, Matthew Salganik (book, força: canonical). Aplicação: Digital-trace validity, ethics and representativeness. Localizador: Bit by Bit, Princeton University Press, 2018, ISBN 9780691158648. Consulta: 2026-08-24.
3. **Google Trends Help**, Google (official, força: primary). Aplicação: Cross-checking normalized public interest. Localizador: https://support.google.com/trends/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
