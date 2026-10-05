---
name: architecture-review
description: "Executa Scenario-Tradeoff Review para responder: a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?"
---

# Architecture Review

## Escopo e gatilhos

Use quando a decisão real for: **a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Scenario-Tradeoff Review**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Scenario-Tradeoff Review

1. **Stakeholders/concerns**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Context/container/data/deployment views**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Quality-attribute scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Decision log**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Tradeoff/risk probes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Fitness functions**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Utility tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Atam-lite**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Adr review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency/critical-path map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Failure-mode walkthrough.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Brownfield começa por runtime evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama desatualizado não é fonte. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de slo bloqueia afirmações de desempenho.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: rastreabilidade 20, qualidade dos cenários 20, evidência 20, tradeoffs 20, operabilidade/reversibilidade 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `stakeholder_concern_matrix_md.md` ou formato nativo equivalente: materializa **`stakeholder-concern-matrix.md`** e deve ser citado pelo artefato principal.
- `quality_scenarios_yaml.md` ou formato nativo equivalente: materializa **`quality-scenarios.yaml`** e deve ser citado pelo artefato principal.
- `adr_index_csv.md` ou formato nativo equivalente: materializa **`adr-index.csv`** e deve ser citado pelo artefato principal.
- `fitness_functions_yaml.md` ou formato nativo equivalente: materializa **`fitness-functions.yaml`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ISO/IEC/IEEE 42010 Architecture Description**, ISO/IEC/IEEE (standard, força: primary). Aplicação: Stakeholders, concerns, viewpoints and decisions. Localizador: https://www.iso.org/standard/74393.html. Consulta: 2026-08-24.
2. **AWS Well-Architected Framework**, AWS (official, força: primary). Aplicação: Risk review across operational pillars. Localizador: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html. Consulta: 2026-08-24.
3. **Software Architecture in Practice, 4th ed.**, Bass, Clements, Kazman (book, força: canonical). Aplicação: Quality-attribute scenarios and tradeoff analysis. Localizador: Addison-Wesley, 2021, ISBN 9780136886099. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
