---
name: cro-seo-analytics
description: "Executa Intent-to-Experiment Chain para responder: qual ruptura no caminho search→landing→action tem maior impacto causal provável?"
---

# Cro Seo Analytics

## Escopo e gatilhos

Use quando a decisão real for: **qual ruptura no caminho search→landing→action tem maior impacto causal provável?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Intent-to-Experiment Chain**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Intent-to-Experiment Chain

1. **Query/intent clusters**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Technical/indexability**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Serp promise**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Landing continuity**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Event qa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Funnel/cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Evidence-backed hypothesis**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Experiment design**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Readout.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Content decay segmentation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query-page mapping**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Funnel leakage**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Instrumentation validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ice with evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sequential guardrails.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Baixo tráfego usa qualitative/pooled tests. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mudança seo não recebe causalidade instantânea. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/internal traffic filtrado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: integridade de dados 25, aderência à intenção 20, hipótese 20, desenho 20, impacto 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `query_page_map_csv.md` ou formato nativo equivalente: materializa **`query-page-map.csv`** e deve ser citado pelo artefato principal.
- `event_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`event-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `experiment_card_md.md` ou formato nativo equivalente: materializa **`experiment-card.md`** e deve ser citado pelo artefato principal.
- `seo_cro_backlog_xlsx.md` ou formato nativo equivalente: materializa **`seo-cro-backlog.xlsx`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Google Search Essentials**, Google Search Central (official, força: primary). Aplicação: Search eligibility and spam-policy gate. Localizador: https://developers.google.com/search/docs/essentials. Consulta: 2026-08-24.
2. **Google Analytics 4 Developer Documentation**, Google (official, força: primary). Aplicação: Event, conversion and attribution instrumentation. Localizador: https://developers.google.com/analytics/devguides/collection/ga4. Consulta: 2026-08-24.
3. **You Should Test That!**, Chris Goward (book, força: canonical). Aplicação: Hypothesis prioritization and controlled experimentation. Localizador: Wiley, 2013, ISBN 9781118301302. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
