# Playbook operacional — Positioning Evidence File

## Pergunta de controle

para quem o produto é uniquely valuable, versus what, in what context?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **customer evidence** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **switching interview** responde à pergunta sem extrapolar o dado? Se não, selecione **claim-evidence trace.** e declare a troca.
3. Há uma destas exceções: aspirational feature excluded; multiple segments get separate contexts; category creation requires education cost.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **para quem o produto é uniquely valuable, versus what, in what context?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Customer evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Job/circumstance**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Alternatives**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Unique attributes**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Value/proof**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Best-fit segment**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Category/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Message boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Versioned context.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Switching interview**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternative map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Value chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Beachhead criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Aspirational feature excluded. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Multiple segments get separate contexts. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Category creation requires education cost.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “job/circumstance” cita evidência identificada, aplica “switching interview”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Positioning Evidence File foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `positioning_canvas_md.md` ou formato nativo equivalente: materializa **`positioning-canvas.md`** e deve ser citado pelo artefato principal.
- `alternative_map_csv.md` ou formato nativo equivalente: materializa **`alternative-map.csv`** e deve ser citado pelo artefato principal.
- `message_boundaries_yaml.md` ou formato nativo equivalente: materializa **`message-boundaries.yaml`** e deve ser citado pelo artefato principal.
- `proof_library.md` ou formato nativo equivalente: materializa **proof library** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: customer evidence 25, differentiation 25, clarity 20, proof 15, usability downstream 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Obviously Awesome**, April Dunford (book, força: canonical). Aplicação: Competitive alternatives, differentiated value and category. Localizador: Ambient Press, 2019, ISBN 9781999023003. Consulta: 2026-08-24.
2. **Crossing the Chasm, 3rd ed.**, Geoffrey Moore (book, força: canonical). Aplicação: Beachhead segment and whole-product context. Localizador: HarperBusiness, 2014, ISBN 9780062292988. Consulta: 2026-08-24.
3. **Jobs to Be Done Theory**, Christensen Institute (official, força: primary). Aplicação: Progress, circumstance and switching forces. Localizador: https://www.christenseninstitute.org/theory/jobs-to-be-done/. Consulta: 2026-08-24.
