# Playbook operacional — Layered Editorial Diagnosis

## Pergunta de controle

qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **objetivo/audiência** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **reverse outline** responde à pergunta sem extrapolar o dado? Se não, selecione **severity taxonomy.** e declare a troca.
3. Há uma destas exceções: texto jurídico não simplifica obrigação; SEO não justifica redundância; crítica separa gosto de falha observável.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Objetivo/audiência**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Factual/claim gate**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Arquitetura**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Parágrafo**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Frase**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Palavra**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Voz/consistência**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Acessibilidade**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Revisão priorizada com antes/depois.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Reverse outline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Information-scent test**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ambiguity scan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive-load pass**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Style sheet**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity taxonomy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Texto jurídico não simplifica obrigação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Seo não justifica redundância. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crítica separa gosto de falha observável.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “factual/claim gate” cita evidência identificada, aplica “reverse outline”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Layered Editorial Diagnosis foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `editorial_scorecard_yaml.md` ou formato nativo equivalente: materializa **`editorial-scorecard.yaml`** e deve ser citado pelo artefato principal.
- `style_sheet_md.md` ou formato nativo equivalente: materializa **`style-sheet.md`** e deve ser citado pelo artefato principal.
- `issue_log_csv.md` ou formato nativo equivalente: materializa **`issue-log.csv`** e deve ser citado pelo artefato principal.
- `diff_anotado.md` ou formato nativo equivalente: materializa **diff anotado** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: diagnóstico 30, preservação de intenção 20, impacto 20, justificativa 15, acessibilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Federal Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Clarity, audience and actionable-language audit. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
2. **The Copyeditor's Handbook, 4th ed.**, Amy Einsohn and Marilyn Schwartz (book, força: canonical). Aplicação: Editorial levels and consistency checks. Localizador: University of California Press, 2019, ISBN 9780520286726. Consulta: 2026-08-24.
3. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Readable, understandable and accessible copy. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.
