---
name: concept-visualizer
description: "Executa Relation-to-Form Compiler para responder: qual forma visual representa a relação essencial sem distorcê-la?"
---

# Concept Visualizer

## Escopo e gatilhos

Use quando a decisão real for: **qual forma visual representa a relação essencial sem distorcê-la?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Relation-to-Form Compiler**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Relation-to-Form Compiler

1. **Frase nuclear**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Entidades/relações**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tipo (hierarquia, fluxo, ciclo, mapa, matriz, causalidade)**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Nível de abstração**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Layout**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Teste de leitura**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fonte renderizável.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual grammar**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Preattentive hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Label economy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternate-text narrative.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Causalidade exige evidência. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Relações múltiplas podem pedir small multiples. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama denso divide vistas, não reduz fonte.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fidelidade semântica 30, legibilidade 25, hierarquia 20, economia 15, acessibilidade 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `concept_graph_json.md` ou formato nativo equivalente: materializa **`concept-graph.json`** e deve ser citado pelo artefato principal.
- `diagram_mmd.md` ou formato nativo equivalente: materializa **`diagram.mmd`** e deve ser citado pelo artefato principal.
- `legend_alt_text.md` ou formato nativo equivalente: materializa **legend/alt-text** e deve ser citado pelo artefato principal.
- `card_de_escolha_de_nota_o.md` ou formato nativo equivalente: materializa **card de escolha de notação** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Back of the Napkin**, Dan Roam (book, força: canonical). Aplicação: Visual encoding by who/what/how/when/where/why. Localizador: Portfolio, 2008, ISBN 9781591841999. Consulta: 2026-08-24.
2. **Visual Thinking**, Rudolf Arnheim (book, força: canonical). Aplicação: Perceptual reasoning and abstraction. Localizador: University of California Press, 1969, ISBN 9780520242265. Consulta: 2026-08-24.
3. **Diagram as Code**, Mermaid (official, força: primary). Aplicação: Reproducible concept diagrams. Localizador: https://mermaid.js.org/intro/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
