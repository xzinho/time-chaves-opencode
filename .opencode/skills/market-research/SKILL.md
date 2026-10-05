---
name: market-research
description: "Executa Question-to-Evidence Protocol para responder: que desenho responde à pergunta com validade suficiente para a decisão?"
---

# Market Research

## Escopo e gatilhos

Use quando a decisão real for: **que desenho responde à pergunta com validade suficiente para a decisão?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Question-to-Evidence Protocol**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Question-to-Evidence Protocol

1. **Decision/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Constructs/hypotheses**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desk research**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Qualitative/quantitative design**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sample/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Instrument pilot**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fieldwork qa**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Analysis**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Recommendation.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Triangulation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sampling plan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive pretest**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Coding frame**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence intervals/effect sizes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Nonresponse analysis.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Convenience sample rotulada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pergunta sensível protege participante. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado secundário incompatível não é combinado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fit do desenho 25, validade 25, amostra 15, transparência 20, utilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `sampling_plan_xlsx.md` ou formato nativo equivalente: materializa **`sampling-plan.xlsx`** e deve ser citado pelo artefato principal.
- `questionnaire_md.md` ou formato nativo equivalente: materializa **`questionnaire.md`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `evidence_table.md` ou formato nativo equivalente: materializa **evidence table** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (standard, força: primary). Aplicação: Ethical research, consent and transparency. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **Marketing Research, 8th ed.**, Naresh Malhotra (book, força: canonical). Aplicação: Research design, sampling and analysis. Localizador: Pearson, 2019, ISBN 9780134734842. Consulta: 2026-08-24.
3. **Pesquisa Nacional por Amostra de Domicílios**, IBGE (official, força: primary). Aplicação: Authoritative Brazilian population and labor estimates. Localizador: https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
