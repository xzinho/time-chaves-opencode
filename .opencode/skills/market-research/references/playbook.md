# Playbook operacional — Question-to-Evidence Protocol

## Pergunta de controle

que desenho responde à pergunta com validade suficiente para a decisão?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **decision/question** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **triangulation** responde à pergunta sem extrapolar o dado? Se não, selecione **nonresponse analysis.** e declare a troca.
3. Há uma destas exceções: convenience sample rotulada; pergunta sensível protege participante; dado secundário incompatível não é combinado.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que desenho responde à pergunta com validade suficiente para a decisão?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Decision/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Constructs/hypotheses**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desk research**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Qualitative/quantitative design**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sample/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Instrument pilot**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fieldwork qa**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Analysis**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Recommendation.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Triangulation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sampling plan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive pretest**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Coding frame**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence intervals/effect sizes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Nonresponse analysis.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Convenience sample rotulada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pergunta sensível protege participante. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado secundário incompatível não é combinado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “constructs/hypotheses” cita evidência identificada, aplica “triangulation”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Question-to-Evidence Protocol foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `sampling_plan_xlsx.md` ou formato nativo equivalente: materializa **`sampling-plan.xlsx`** e deve ser citado pelo artefato principal.
- `questionnaire_md.md` ou formato nativo equivalente: materializa **`questionnaire.md`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `evidence_table.md` ou formato nativo equivalente: materializa **evidence table** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fit do desenho 25, validade 25, amostra 15, transparência 20, utilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (standard, força: primary). Aplicação: Ethical research, consent and transparency. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **Marketing Research, 8th ed.**, Naresh Malhotra (book, força: canonical). Aplicação: Research design, sampling and analysis. Localizador: Pearson, 2019, ISBN 9780134734842. Consulta: 2026-08-24.
3. **Pesquisa Nacional por Amostra de Domicílios**, IBGE (official, força: primary). Aplicação: Authoritative Brazilian population and labor estimates. Localizador: https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html. Consulta: 2026-08-24.
