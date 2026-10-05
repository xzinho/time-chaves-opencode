---
name: product-marketing-context
description: "Executa Positioning Evidence File para responder: para quem o produto é uniquely valuable, versus what, in what context?"
---

# Product Marketing Context

## Escopo e gatilhos

Use quando a decisão real for: **para quem o produto é uniquely valuable, versus what, in what context?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Positioning Evidence File**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Positioning Evidence File

1. **Customer evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Job/circumstance**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Alternatives**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Unique attributes**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Value/proof**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Best-fit segment**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Category/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Message boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Versioned context.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Switching interview**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternative map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Value chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Beachhead criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Aspirational feature excluded. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Multiple segments get separate contexts. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Category creation requires education cost.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: customer evidence 25, differentiation 25, clarity 20, proof 15, usability downstream 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `positioning_canvas_md.md` ou formato nativo equivalente: materializa **`positioning-canvas.md`** e deve ser citado pelo artefato principal.
- `alternative_map_csv.md` ou formato nativo equivalente: materializa **`alternative-map.csv`** e deve ser citado pelo artefato principal.
- `message_boundaries_yaml.md` ou formato nativo equivalente: materializa **`message-boundaries.yaml`** e deve ser citado pelo artefato principal.
- `proof_library.md` ou formato nativo equivalente: materializa **proof library** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Obviously Awesome**, April Dunford (book, força: canonical). Aplicação: Competitive alternatives, differentiated value and category. Localizador: Ambient Press, 2019, ISBN 9781999023003. Consulta: 2026-08-24.
2. **Crossing the Chasm, 3rd ed.**, Geoffrey Moore (book, força: canonical). Aplicação: Beachhead segment and whole-product context. Localizador: HarperBusiness, 2014, ISBN 9780062292988. Consulta: 2026-08-24.
3. **Jobs to Be Done Theory**, Christensen Institute (official, força: primary). Aplicação: Progress, circumstance and switching forces. Localizador: https://www.christenseninstitute.org/theory/jobs-to-be-done/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
