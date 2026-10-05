---
name: cashflow-dre
description: "Executa Accrual-to-Cash Bridge para responder: resultado, liquidez e capital de giro contam a mesma história?"
---

# Cashflow Dre

## Escopo e gatilhos

Use quando a decisão real for: **resultado, liquidez e capital de giro contam a mesma história?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Accrual-to-Cash Bridge**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Accrual-to-Cash Bridge

1. **Importar plano/razão/extratos**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Mapear contas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Montar dre**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Classificar caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Bridge lucro**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Aging/working capital**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cenários e reconciliações.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Método direto/indireto**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Análise vertical/horizontal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ebitda-to-cash**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dso/dio/dpo**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Checks de abertura/fechamento.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Transferências internas eliminadas. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Impostos/juros classificados por política. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado incompleto conserva `unknown`, nunca zero silencioso.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: reconciliação 30, classificação 20, rastreabilidade 20, insight 15, controles 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `chart_of_accounts_map_csv.md` ou formato nativo equivalente: materializa **`chart-of-accounts-map.csv`** e deve ser citado pelo artefato principal.
- `cashflow_xlsx.md` ou formato nativo equivalente: materializa **`cashflow.xlsx`** e deve ser citado pelo artefato principal.
- `reconciliation_checks_yaml.md` ou formato nativo equivalente: materializa **`reconciliation-checks.yaml`** e deve ser citado pelo artefato principal.
- `coment_rio_de_varia_es.md` ou formato nativo equivalente: materializa **comentário de variações** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **CPC 03 (R2) Demonstração dos Fluxos de Caixa**, CPC (official, força: primary). Aplicação: Cash-flow classification and reconciliation. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=34. Consulta: 2026-08-24.
2. **CPC 26 (R1) Apresentação das Demonstrações Contábeis**, CPC (official, força: primary). Aplicação: Income-statement structure and comparatives. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=57. Consulta: 2026-08-24.
3. **IAS 7 Statement of Cash Flows**, IFRS Foundation (standard, força: primary). Aplicação: Operating, investing and financing cash taxonomy. Localizador: https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.
