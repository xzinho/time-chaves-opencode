# Playbook operacional — Intentional Experience Direction

## Pergunta de controle

que estética e interação amplificam a proposta sem sacrificar usabilidade/performance?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **brand/product intent** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **contrast map** responde à pergunta sem extrapolar o dado? Se não, selecione **aesthetic-usability countercheck.** e declare a troca.
3. Há uma destas exceções: reduced motion; low-end device budget; dense enterprise flows prioritize scanning; novelty must not hide controls.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que estética e interação amplificam a proposta sem sacrificar usabilidade/performance?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Brand/product intent**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Mood/anti-mood**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Hierarchy/rhythm**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Signature moments**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Component/motion rules**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Prototype key journeys**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Accessibility/performance**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Perceptual review.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Contrast map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual rhythm**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Focal hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Motion grammar**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Progressive complexity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Aesthetic-usability countercheck.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Reduced motion. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Low-end device budget. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dense enterprise flows prioritize scanning. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Novelty must not hide controls.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “mood/anti-mood” cita evidência identificada, aplica “contrast map”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Intentional Experience Direction foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `art_direction_board_md.md` ou formato nativo equivalente: materializa **`art-direction-board.md`** e deve ser citado pelo artefato principal.
- `signature_moments_yaml.md` ou formato nativo equivalente: materializa **`signature-moments.yaml`** e deve ser citado pelo artefato principal.
- `motion_tokens.md` ou formato nativo equivalente: materializa **motion tokens** e deve ser citado pelo artefato principal.
- `visual_qa_scorecard.md` ou formato nativo equivalente: materializa **visual QA scorecard** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: identidade 20, hierarquia 20, craft 20, função 20, acessibilidade/performance 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Material Design 3**, Google (official, força: primary). Aplicação: Interaction, motion and component behavior baseline. Localizador: https://m3.material.io/. Consulta: 2026-08-24.
2. **Human Interface Guidelines**, Apple (official, força: primary). Aplicação: Platform coherence, hierarchy and feedback. Localizador: https://developer.apple.com/design/human-interface-guidelines/. Consulta: 2026-08-24.
3. **The Laws of Simplicity**, John Maeda (book, força: canonical). Aplicação: Reduction, organization and emotional quality. Localizador: MIT Press, 2006, ISBN 9780262134729. Consulta: 2026-08-24.
