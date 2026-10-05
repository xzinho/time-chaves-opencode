# Playbook operacional — Accrual-to-Cash Bridge

## Pergunta de controle

resultado, liquidez e capital de giro contam a mesma história?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **importar plano/razão/extratos** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **método direto/indireto** responde à pergunta sem extrapolar o dado? Se não, selecione **checks de abertura/fechamento.** e declare a troca.
3. Há uma destas exceções: transferências internas eliminadas; impostos/juros classificados por política; dado incompleto conserva `unknown`, nunca zero silencioso.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **resultado, liquidez e capital de giro contam a mesma história?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Importar plano/razão/extratos**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Mapear contas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Montar dre**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Classificar caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Bridge lucro**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Aging/working capital**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cenários e reconciliações.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Método direto/indireto**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Análise vertical/horizontal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ebitda-to-cash**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dso/dio/dpo**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Checks de abertura/fechamento.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Transferências internas eliminadas. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Impostos/juros classificados por política. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado incompleto conserva `unknown`, nunca zero silencioso.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “mapear contas” cita evidência identificada, aplica “método direto/indireto”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Accrual-to-Cash Bridge foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `chart_of_accounts_map_csv.md` ou formato nativo equivalente: materializa **`chart-of-accounts-map.csv`** e deve ser citado pelo artefato principal.
- `cashflow_xlsx.md` ou formato nativo equivalente: materializa **`cashflow.xlsx`** e deve ser citado pelo artefato principal.
- `reconciliation_checks_yaml.md` ou formato nativo equivalente: materializa **`reconciliation-checks.yaml`** e deve ser citado pelo artefato principal.
- `coment_rio_de_varia_es.md` ou formato nativo equivalente: materializa **comentário de variações** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: reconciliação 30, classificação 20, rastreabilidade 20, insight 15, controles 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **CPC 03 (R2) Demonstração dos Fluxos de Caixa**, CPC (official, força: primary). Aplicação: Cash-flow classification and reconciliation. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=34. Consulta: 2026-08-24.
2. **CPC 26 (R1) Apresentação das Demonstrações Contábeis**, CPC (official, força: primary). Aplicação: Income-statement structure and comparatives. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=57. Consulta: 2026-08-24.
3. **IAS 7 Statement of Cash Flows**, IFRS Foundation (standard, força: primary). Aplicação: Operating, investing and financing cash taxonomy. Localizador: https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/. Consulta: 2026-08-24.
