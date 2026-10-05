# Playbook operacional — Intent-to-Experiment Chain

## Pergunta de controle

qual ruptura no caminho search→landing→action tem maior impacto causal provável?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **query/intent clusters** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **content decay segmentation** responde à pergunta sem extrapolar o dado? Se não, selecione **sequential guardrails.** e declare a troca.
3. Há uma destas exceções: baixo tráfego usa qualitative/pooled tests; mudança SEO não recebe causalidade instantânea; bot/internal traffic filtrado.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual ruptura no caminho search→landing→action tem maior impacto causal provável?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Query/intent clusters**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Technical/indexability**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Serp promise**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Landing continuity**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Event qa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Funnel/cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Evidence-backed hypothesis**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Experiment design**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Readout.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Content decay segmentation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query-page mapping**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Funnel leakage**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Instrumentation validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ice with evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sequential guardrails.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Baixo tráfego usa qualitative/pooled tests. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mudança seo não recebe causalidade instantânea. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/internal traffic filtrado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “technical/indexability” cita evidência identificada, aplica “content decay segmentation”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Intent-to-Experiment Chain foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `query_page_map_csv.md` ou formato nativo equivalente: materializa **`query-page-map.csv`** e deve ser citado pelo artefato principal.
- `event_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`event-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `experiment_card_md.md` ou formato nativo equivalente: materializa **`experiment-card.md`** e deve ser citado pelo artefato principal.
- `seo_cro_backlog_xlsx.md` ou formato nativo equivalente: materializa **`seo-cro-backlog.xlsx`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: integridade de dados 25, aderência à intenção 20, hipótese 20, desenho 20, impacto 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Google Search Essentials**, Google Search Central (official, força: primary). Aplicação: Search eligibility and spam-policy gate. Localizador: https://developers.google.com/search/docs/essentials. Consulta: 2026-08-24.
2. **Google Analytics 4 Developer Documentation**, Google (official, força: primary). Aplicação: Event, conversion and attribution instrumentation. Localizador: https://developers.google.com/analytics/devguides/collection/ga4. Consulta: 2026-08-24.
3. **You Should Test That!**, Chris Goward (book, força: canonical). Aplicação: Hypothesis prioritization and controlled experimentation. Localizador: Wiley, 2013, ISBN 9781118301302. Consulta: 2026-08-24.
