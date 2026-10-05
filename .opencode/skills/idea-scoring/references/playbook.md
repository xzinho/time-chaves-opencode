# Playbook operacional — Evidence-Calibrated Portfolio

## Pergunta de controle

investir, experimentar, estacionar ou matar uma ideia?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **define outcome/unit** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **anchored scales** responde à pergunta sem extrapolar o dado? Se não, selecione **dominance check.** e declare a troca.
3. Há uma destas exceções: scores próximos viram empate; alta upside/baixa confiança recebe experimento; veto legal/security sobrepõe ranking.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **investir, experimentar, estacionar ou matar uma ideia?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Define outcome/unit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Normalize ideas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Score reach/impact/confidence/effort/strategic fit/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Evidence grade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Uncertainty penalty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Rank**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Portfolio balance**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Next test.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Anchored scales**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence decay**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted score**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sensitivity to weights**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dominance check.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Scores próximos viram empate. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alta upside/baixa confiança recebe experimento. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Veto legal/security sobrepõe ranking.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “normalize ideas” cita evidência identificada, aplica “anchored scales”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Evidence-Calibrated Portfolio foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `score_rubric_yaml.md` ou formato nativo equivalente: materializa **`score-rubric.yaml`** e deve ser citado pelo artefato principal.
- `idea_portfolio_xlsx.md` ou formato nativo equivalente: materializa **`idea-portfolio.xlsx`** e deve ser citado pelo artefato principal.
- `evidence_card_md.md` ou formato nativo equivalente: materializa **`evidence-card.md`** e deve ser citado pelo artefato principal.
- `sensitivity_plot.md` ou formato nativo equivalente: materializa **sensitivity plot** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: definição 15, evidência 25, calibração 20, transparência 20, ação 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Lean Startup**, Eric Ries (book, força: canonical). Aplicação: Leap-of-faith assumptions and validated learning. Localizador: Crown Business, 2011, ISBN 9780307887894. Consulta: 2026-08-24.
2. **Testing Business Ideas**, David Bland and Alexander Osterwalder (book, força: canonical). Aplicação: Assumption mapping and experiment selection. Localizador: Wiley, 2019, ISBN 9781119551447. Consulta: 2026-08-24.
3. **RICE Prioritization**, Intercom (official, força: primary). Aplicação: Reach-impact-confidence-effort normalization. Localizador: https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/. Consulta: 2026-08-24.
