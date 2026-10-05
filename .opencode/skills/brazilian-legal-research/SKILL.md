---
name: brazilian-legal-research
description: "Executa Questão-Norma-Precedente para responder: qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?"
---

# Brazilian Legal Research

## Escopo e gatilhos

Use quando a decisão real for: **qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Questão-Norma-Precedente**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Questão-Norma-Precedente

1. **Fatos/foro/data**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Issues**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Hierarquia normativa**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Vigência/alterações**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Jurisprudência por holding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Correntes e distinções**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Conclusão condicionada**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Citator log.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Irac adaptado**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Árvore de autoridade**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cadeia de vigência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ratio vs obiter**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Tratamento de precedente contrário.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Segredo/privacidade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Decisão monocrática não equivale a precedente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Tema repetitivo/repercussão geral muda peso. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Escalar prática jurídica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: autoridade 25, vigência 20, aderência fática 20, tratamento contrário 15, citações recuperáveis 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `authority_table_csv.md` ou formato nativo equivalente: materializa **`authority-table.csv`** e deve ser citado pelo artefato principal.
- `case_brief_md.md` ou formato nativo equivalente: materializa **`case-brief.md`** e deve ser citado pelo artefato principal.
- `citation_validator_py.md` ou formato nativo equivalente: materializa **`citation-validator.py`** e deve ser citado pelo artefato principal.
- `open_questions_md.md` ou formato nativo equivalente: materializa **`open-questions.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Portal da Legislação**, Presidência da República do Brasil (official, força: primary). Aplicação: Authoritative consolidated federal legislation. Localizador: https://www4.planalto.gov.br/legislacao/. Consulta: 2026-08-24.
2. **Pesquisa de Jurisprudência**, STJ (official, força: primary). Aplicação: Binding context, precedent and temporal validity. Localizador: https://scon.stj.jus.br/SCON/. Consulta: 2026-08-24.
3. **Pesquisa de Jurisprudência**, STF (official, força: primary). Aplicação: Constitutional holdings and repercussão geral. Localizador: https://jurisprudencia.stf.jus.br/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
