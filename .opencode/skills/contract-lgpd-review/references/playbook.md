# Playbook operacional — Data-Clause Trace

## Pergunta de controle

cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **partes/papéis** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **controller-processor matrix** responde à pergunta sem extrapolar o dado? Se não, selecione **clause-to-control trace.** e declare a troca.
3. Há uma destas exceções: base legal depende de fatos; transferência internacional revisa mecanismo vigente; alto risco escala DPO/jurídico.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Partes/papéis**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Data-flow map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tabela cláusula-tema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Base/finalidade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Direitos/retention/security/subprocessors/incidents/transfers**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Redlines e perguntas.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Controller-processor matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Purpose compatibility**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Raci de incidentes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Clause-to-control trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Base legal depende de fatos. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Transferência internacional revisa mecanismo vigente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alto risco escala dpo/jurídico.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “data-flow map” cita evidência identificada, aplica “controller-processor matrix”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Data-Clause Trace foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `data_flow_mmd.md` ou formato nativo equivalente: materializa **`data-flow.mmd`** e deve ser citado pelo artefato principal.
- `clause_control_matrix_csv.md` ou formato nativo equivalente: materializa **`clause-control-matrix.csv`** e deve ser citado pelo artefato principal.
- `redline_log_md.md` ou formato nativo equivalente: materializa **`redline-log.md`** e deve ser citado pelo artefato principal.
- `missing_facts_md.md` ou formato nativo equivalente: materializa **`missing-facts.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: cobertura 25, precisão jurídica 25, aderência ao fluxo 20, prioridade de risco 15, remediação 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Lei Geral de Proteção de Dados Pessoais**, Brasil (official, força: primary). Aplicação: Lawful bases, rights, actors and sanctions. Localizador: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Consulta: 2026-08-24.
2. **Guias e orientações**, ANPD (official, força: primary). Aplicação: Regulatory interpretation and controller-processor duties. Localizador: https://www.gov.br/anpd/pt-br/documentos-e-publicacoes. Consulta: 2026-08-24.
3. **ISO/IEC 27701 Privacy Information Management**, ISO/IEC (standard, força: primary). Aplicação: Operational privacy controls and evidence. Localizador: https://www.iso.org/standard/71670.html. Consulta: 2026-08-24.
