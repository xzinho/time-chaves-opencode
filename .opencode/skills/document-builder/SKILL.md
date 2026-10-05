---
name: document-builder
description: "Executa Semantic Document Pipeline para responder: como preservar estrutura, identidade e acessibilidade no formato nativo?"
---

# Document Builder

## Escopo e gatilhos

Use quando a decisão real for: **como preservar estrutura, identidade e acessibilidade no formato nativo?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Semantic Document Pipeline**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Semantic Document Pipeline

1. **Content model**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Style map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Page/section rules**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Components (tables/callouts)**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Links/media**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Generate**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Parse-back**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Visual/accessibility qa**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Export.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Semantic styles**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keep-with-next**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Orphan control**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Repeat headers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alt text**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metadata**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Package inspection.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Template fornecido é autoridade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pdf não substitui arquivo editável quando exigido. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Fonte ausente usa fallback explícito.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fidelidade 25, estrutura 20, acessibilidade 20, render 20, editabilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `document_schema_json.md` ou formato nativo equivalente: materializa **`document-schema.json`** e deve ser citado pelo artefato principal.
- `style_map_yaml.md` ou formato nativo equivalente: materializa **`style-map.yaml`** e deve ser citado pelo artefato principal.
- `native_builder.md` ou formato nativo equivalente: materializa **native builder** e deve ser citado pelo artefato principal.
- `parse_back_assertions.md` ou formato nativo equivalente: materializa **parse-back assertions** e deve ser citado pelo artefato principal.
- `render_snapshots.md` ou formato nativo equivalente: materializa **render snapshots** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **PDF/UA-1 ISO 14289-1**, ISO (standard, força: primary). Aplicação: Accessible document structure. Localizador: https://www.iso.org/standard/64599.html. Consulta: 2026-08-24.
2. **OOXML ECMA-376**, Ecma International (standard, força: primary). Aplicação: Native Office document packaging and semantics. Localizador: https://ecma-international.org/publications-and-standards/standards/ecma-376/. Consulta: 2026-08-24.
3. **python-docx**, python-openxml (github, força: mature). Aplicação: Reproducible DOCX generation and validation. Localizador: https://github.com/python-openxml/python-docx. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
