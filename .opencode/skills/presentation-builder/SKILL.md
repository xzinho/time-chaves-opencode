---
name: presentation-builder
description: "Executa Argument-to-Slide System para responder: qual sequência faz a audiência compreender, acreditar e decidir?"
---

# Presentation Builder

## Escopo e gatilhos

Use quando a decisão real for: **qual sequência faz a audiência compreender, acreditar e decidir?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Argument-to-Slide System**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Argument-to-Slide System

1. **Audience/decision**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Storyline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Slide functions**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Wireframes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Chart selection**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Build**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Speaker notes**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Rehearsal/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Assertion-evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **One function per slide**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart integrity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Section rhythm**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Appendix routing.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Leave-behind needs more context. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Board deck leads with decisions. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Data-heavy slide gets takeaway and source, not decoration.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: storyline 25, evidence 20, visual hierarchy 20, readability 15, action 10, accessibility 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `storyline_csv.md` ou formato nativo equivalente: materializa **`storyline.csv`** e deve ser citado pelo artefato principal.
- `slide_schema_json.md` ou formato nativo equivalente: materializa **`slide-schema.json`** e deve ser citado pelo artefato principal.
- `chart_decision_tree.md` ou formato nativo equivalente: materializa **chart decision tree** e deve ser citado pelo artefato principal.
- `native_pptx_builder_and_render_montage.md` ou formato nativo equivalente: materializa **native PPTX builder and render montage** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Visual Display of Quantitative Information**, Edward Tufte (book, força: canonical). Aplicação: Evidence-dense, honest quantitative graphics. Localizador: Graphics Press, 2001, ISBN 9780961392147. Consulta: 2026-08-24.
2. **Presentation Zen**, Garr Reynolds (book, força: canonical). Aplicação: Audience, story and visual restraint. Localizador: New Riders, 2019, ISBN 9780135800911. Consulta: 2026-08-24.
3. **PowerPoint Accessibility**, Microsoft (official, força: primary). Aplicação: Reading order, alt text, contrast and structure. Localizador: https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
