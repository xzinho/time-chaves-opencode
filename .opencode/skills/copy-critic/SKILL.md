---
name: copy-critic
description: "Executa Layered Editorial Diagnosis para responder: qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?"
---

# Copy Critic

## Escopo e gatilhos

Use quando a decisão real for: **qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Layered Editorial Diagnosis**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Layered Editorial Diagnosis

1. **Objetivo/audiência**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Factual/claim gate**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Arquitetura**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Parágrafo**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Frase**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Palavra**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Voz/consistência**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Acessibilidade**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Revisão priorizada com antes/depois.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Reverse outline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Information-scent test**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ambiguity scan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive-load pass**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Style sheet**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity taxonomy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Texto jurídico não simplifica obrigação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Seo não justifica redundância. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crítica separa gosto de falha observável.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: diagnóstico 30, preservação de intenção 20, impacto 20, justificativa 15, acessibilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `editorial_scorecard_yaml.md` ou formato nativo equivalente: materializa **`editorial-scorecard.yaml`** e deve ser citado pelo artefato principal.
- `style_sheet_md.md` ou formato nativo equivalente: materializa **`style-sheet.md`** e deve ser citado pelo artefato principal.
- `issue_log_csv.md` ou formato nativo equivalente: materializa **`issue-log.csv`** e deve ser citado pelo artefato principal.
- `diff_anotado.md` ou formato nativo equivalente: materializa **diff anotado** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Federal Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Clarity, audience and actionable-language audit. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
2. **The Copyeditor's Handbook, 4th ed.**, Amy Einsohn and Marilyn Schwartz (book, força: canonical). Aplicação: Editorial levels and consistency checks. Localizador: University of California Press, 2019, ISBN 9780520286726. Consulta: 2026-08-24.
3. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Readable, understandable and accessible copy. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
