---
name: contract-lgpd-review
description: "Executa Data-Clause Trace para responder: cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?"
---

# Contract Lgpd Review

## Escopo e gatilhos

Use quando a decisão real for: **cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Data-Clause Trace**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Data-Clause Trace

1. **Partes/papéis**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Data-flow map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tabela cláusula-tema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Base/finalidade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Direitos/retention/security/subprocessors/incidents/transfers**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Redlines e perguntas.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Controller-processor matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Purpose compatibility**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Raci de incidentes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Clause-to-control trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Base legal depende de fatos. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Transferência internacional revisa mecanismo vigente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alto risco escala dpo/jurídico.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cobertura 25, precisão jurídica 25, aderência ao fluxo 20, prioridade de risco 15, remediação 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `data_flow_mmd.md` ou formato nativo equivalente: materializa **`data-flow.mmd`** e deve ser citado pelo artefato principal.
- `clause_control_matrix_csv.md` ou formato nativo equivalente: materializa **`clause-control-matrix.csv`** e deve ser citado pelo artefato principal.
- `redline_log_md.md` ou formato nativo equivalente: materializa **`redline-log.md`** e deve ser citado pelo artefato principal.
- `missing_facts_md.md` ou formato nativo equivalente: materializa **`missing-facts.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Lei Geral de Proteção de Dados Pessoais**, Brasil (official, força: primary). Aplicação: Lawful bases, rights, actors and sanctions. Localizador: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Consulta: 2026-08-24.
2. **Guias e orientações**, ANPD (official, força: primary). Aplicação: Regulatory interpretation and controller-processor duties. Localizador: https://www.gov.br/anpd/pt-br/documentos-e-publicacoes. Consulta: 2026-08-24.
3. **ISO/IEC 27701 Privacy Information Management**, ISO/IEC (standard, força: primary). Aplicação: Operational privacy controls and evidence. Localizador: https://www.iso.org/standard/71670.html. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
