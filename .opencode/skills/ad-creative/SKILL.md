---
name: ad-creative
description: "Executa Creative Evidence Loop para responder: qual combinação de audiência, estágio, promessa, prova e formato merece teste?"
---

# Ad Creative

## Escopo e gatilhos

Use quando a decisão real for: **qual combinação de audiência, estágio, promessa, prova e formato merece teste?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Creative Evidence Loop**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Creative Evidence Loop

1. **Brief verificável**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Matriz de tensões**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inventário de claims/provas**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **3 territórios criativos**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Variações hook/body/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gate de política**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Plano de células e hipótese.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Message-market fit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Awareness ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Angle × format matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pre-mortem de interpretação**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Controle de variável criativa.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Segmento regulado exige aprovação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de prova converte claim em hipótese. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pouco orçamento reduz células, não mistura variáveis.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: insight 20, especificidade 20, prova 20, distinção 15, adequação ao formato 15, compliance 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `creative_test_matrix_csv.md` ou formato nativo equivalente: materializa **`creative-test-matrix.csv`** e deve ser citado pelo artefato principal.
- `policy_gate_yaml.md` ou formato nativo equivalente: materializa **`policy-gate.yaml`** e deve ser citado pelo artefato principal.
- `storyboard_com_safe_zones.md` ou formato nativo equivalente: materializa **storyboard com safe zones** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Meta Advertising Standards**, Meta (official, força: primary). Aplicação: Policy gate and prohibited-claim checklist. Localizador: https://transparency.meta.com/policies/ad-standards/. Consulta: 2026-08-24.
2. **Google Ads Creative Best Practices**, Google (official, força: primary). Aplicação: Asset variation and responsive-ad constraints. Localizador: https://support.google.com/google-ads/answer/6167122. Consulta: 2026-08-24.
3. **Ogilvy on Advertising**, David Ogilvy (book, força: canonical). Aplicação: Research-led promise, headline and proof discipline. Localizador: Vintage, 1985, ISBN 9780394729039. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
