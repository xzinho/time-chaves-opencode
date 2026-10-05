# Playbook operacional — Decision-First Brief

## Pergunta de controle

o que o executivo deve decidir, por quê agora e com qual consequência?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **decision statement** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **pyramid logic** responde à pergunta sem extrapolar o dado? Se não, selecione **red-team question.** e declare a troca.
3. Há uma destas exceções: sem decisão vira status brief; crise prioriza facts/time/owner; incerteza não é escondida por prosa.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **o que o executivo deve decidir, por quê agora e com qual consequência?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Decision statement**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **One-line answer**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Material facts**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Options/tradeoffs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Recommendation**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Risks/unknowns**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Explicit ask**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Owners/dates.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Pyramid logic**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Bluf**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fact/inference/assumption tags**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Option table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Red-team question.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Sem decisão vira status brief. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crise prioriza facts/time/owner. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Incerteza não é escondida por prosa.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “one-line answer” cita evidência identificada, aplica “pyramid logic”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Decision-First Brief foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `decision_brief_md.md` ou formato nativo equivalente: materializa **`decision-brief.md`** e deve ser citado pelo artefato principal.
- `fact_assumption_ledger_csv.md` ou formato nativo equivalente: materializa **`fact-assumption-ledger.csv`** e deve ser citado pelo artefato principal.
- `one_page_pdf.md` ou formato nativo equivalente: materializa **one-page PDF** e deve ser citado pelo artefato principal.
- `verbal_60_second_variant.md` ou formato nativo equivalente: materializa **verbal 60-second variant** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: decisão 25, síntese 20, evidência 20, tradeoffs 15, ação 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Pyramid Principle**, Barbara Minto (book, força: canonical). Aplicação: Answer-first logic and mutually exclusive support. Localizador: Financial Times Prentice Hall, 2009, ISBN 9780273710516. Consulta: 2026-08-24.
2. **Writing for GOV.UK**, UK Government Digital Service (official, força: primary). Aplicação: Concise audience-centered executive language. Localizador: https://www.gov.uk/guidance/content-design/writing-for-gov-uk. Consulta: 2026-08-24.
3. **Smart Brevity**, Jim VandeHei, Mike Allen, Roy Schwartz (book, força: recognized). Aplicação: Why-it-matters and scannable action architecture. Localizador: Workman, 2022, ISBN 9781523516971. Consulta: 2026-08-24.
