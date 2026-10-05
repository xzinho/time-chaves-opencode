# Playbook operacional — Uncertainty-to-Options

## Pergunta de controle

quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **focal question/horizon** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **2×2 only when orthogonal** responde à pergunta sem extrapolar o dado? Se não, selecione **no-regret/hedge/options.** e declare a troca.
3. Há uma destas exceções: scenario is not forecast; black swan gets contingency, not fake probability; contradictions trigger rewrite.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Focal question/horizon**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Environmental scan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Forces**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Predetermineds**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Rank impact/uncertainty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Scenario logics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Narratives/quantification**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Strategy wind-tunnel**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Options**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Indicators/triggers.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **2×2 only when orthogonal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Morphological scenarios**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Causal loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consistency check**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Signposts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **No-regret/hedge/options.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Scenario is not forecast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Black swan gets contingency, not fake probability. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Contradictions trigger rewrite.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “environmental scan” cita evidência identificada, aplica “2×2 only when orthogonal”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Uncertainty-to-Options foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `driver_register_csv.md` ou formato nativo equivalente: materializa **`driver-register.csv`** e deve ser citado pelo artefato principal.
- `scenario_logic_yaml.md` ou formato nativo equivalente: materializa **`scenario-logic.yaml`** e deve ser citado pelo artefato principal.
- `wind_tunnel_xlsx.md` ou formato nativo equivalente: materializa **`wind-tunnel.xlsx`** e deve ser citado pelo artefato principal.
- `signpost_dashboard_md.md` ou formato nativo equivalente: materializa **`signpost-dashboard.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: plausibility 20, distinctness 20, causal coherence 20, strategic stress 20, indicators 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Art of the Long View**, Peter Schwartz (book, força: canonical). Aplicação: Driving forces, critical uncertainties and narratives. Localizador: Doubleday, 1991, ISBN 9780385267328. Consulta: 2026-08-24.
2. **Scenario Planning Guide**, UK Government Office for Science (official, força: primary). Aplicação: Futures toolkit and policy stress-testing. Localizador: https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts. Consulta: 2026-08-24.
3. **Thinking in Systems**, Donella Meadows (book, força: canonical). Aplicação: Feedback loops, delays and leverage points. Localizador: Chelsea Green, 2008, ISBN 9781603580557. Consulta: 2026-08-24.
