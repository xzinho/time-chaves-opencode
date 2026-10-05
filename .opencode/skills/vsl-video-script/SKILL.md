---
name: vsl-video-script
description: "Executa Claim-Beat-Retention Script para responder: what sequence earns attention, builds belief and converts within duration/platform constraints?"
---

# Vsl Video Script

## Escopo e gatilhos

Use quando a decisão real for: **what sequence earns attention, builds belief and converts within duration/platform constraints?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Claim-Beat-Retention Script**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Claim-Beat-Retention Script

1. **Audience/awareness/offer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Core promise**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Claim-proof inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Hook variants**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Problem stakes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mechanism**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Proof/demo**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objections**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Beat/timecode**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Visual/audio directions**. Registre entrada, transformação, evidência e saída antes de avançar.
12. **Read-time/claim qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Open loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Concrete demonstration**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pattern interrupt**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof pacing**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection stack**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cta singularity.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- No fake scarcity. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Testimonial claims verified. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Short form compresses beats, not logic. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Spoken cadence tested aloud.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: hook 20, belief progression 20, proof 20, retention pacing 15, offer/CTA 15, compliance 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `vsl_beat_sheet_csv.md` ou formato nativo equivalente: materializa **`vsl-beat-sheet.csv`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `broll_map_md.md` ou formato nativo equivalente: materializa **`broll-map.md`** e deve ser citado pelo artefato principal.
- `timecoded_script_and_variants.md` ou formato nativo equivalente: materializa **timecoded script and variants** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Save the Cat!**, Blake Snyder (book, força: canonical). Aplicação: Beat architecture and pacing, adapted clean-room. Localizador: Michael Wiese Productions, 2005, ISBN 9781932907001. Consulta: 2026-08-24.
2. **YouTube Creator Academy**, YouTube (official, força: primary). Aplicação: Audience retention, packaging and platform constraints. Localizador: https://creatoracademy.youtube.com/. Consulta: 2026-08-24.
3. **Made to Stick**, Chip Heath and Dan Heath (book, força: canonical). Aplicação: Concrete, credible and emotionally memorable messages. Localizador: Random House, 2007, ISBN 9781400064281. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
