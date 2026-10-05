---
name: security-review
description: "Executa Asset-Threat-Control-Evidence para responder: what must block release, what can be remediated, and what residual risk is accepted by whom?"
---

# Security Review

## Escopo e gatilhos

Use quando a decisão real for: **what must block release, what can be remediated, and what residual risk is accepted by whom?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Asset-Threat-Control-Evidence**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Asset-Threat-Control-Evidence

1. **Scope/data/classification**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Architecture/trust boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Threat model**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Asvs/ssdf control mapping**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code/config/runtime evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Exploitability/impact**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Remediation/retest**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Stride-like prompts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Attack path**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Misuse case**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Secret/dependency/auth/session review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence tiers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity matrix.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Scanner finding not confirmed is tentative. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Production test needs authorization. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Risk acceptance requires named authority/date.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: scope 15, threat coverage 25, evidence 25, severity 15, remediation/retest 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `threat_model_md.md` ou formato nativo equivalente: materializa **`threat-model.md`** e deve ser citado pelo artefato principal.
- `control_evidence_csv.md` ou formato nativo equivalente: materializa **`control-evidence.csv`** e deve ser citado pelo artefato principal.
- `finding_schema_json.md` ou formato nativo equivalente: materializa **`finding-schema.json`** e deve ser citado pelo artefato principal.
- `release_gate_with_owner_due_date.md` ou formato nativo equivalente: materializa **release gate with owner/due date** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **OWASP Application Security Verification Standard 4.0.3**, OWASP (official, força: primary). Aplicação: Testable application-security control baseline. Localizador: https://owasp.org/www-project-application-security-verification-standard/. Consulta: 2026-08-24.
2. **NIST Secure Software Development Framework 1.1**, NIST (official, força: primary). Aplicação: Secure-development practices and evidence. Localizador: https://csrc.nist.gov/pubs/sp/800/218/final. Consulta: 2026-08-24.
3. **Threat Modeling Playbook**, OWASP (github, força: mature). Aplicação: Practical threat-model facilitation. Localizador: https://github.com/OWASP/threat-modeling-playbook. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
