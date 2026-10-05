# Playbook operacional — Creative Evidence Loop

## Pergunta de controle

qual combinação de audiência, estágio, promessa, prova e formato merece teste?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **brief verificável** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **message-market fit** responde à pergunta sem extrapolar o dado? Se não, selecione **controle de variável criativa.** e declare a troca.
3. Há uma destas exceções: segmento regulado exige aprovação; ausência de prova converte claim em hipótese; pouco orçamento reduz células, não mistura variáveis.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual combinação de audiência, estágio, promessa, prova e formato merece teste?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Brief verificável**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Matriz de tensões**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inventário de claims/provas**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **3 territórios criativos**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Variações hook/body/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gate de política**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Plano de células e hipótese.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Message-market fit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Awareness ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Angle × format matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pre-mortem de interpretação**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Controle de variável criativa.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Segmento regulado exige aprovação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de prova converte claim em hipótese. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pouco orçamento reduz células, não mistura variáveis.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “matriz de tensões” cita evidência identificada, aplica “message-market fit”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Creative Evidence Loop foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `creative_test_matrix_csv.md` ou formato nativo equivalente: materializa **`creative-test-matrix.csv`** e deve ser citado pelo artefato principal.
- `policy_gate_yaml.md` ou formato nativo equivalente: materializa **`policy-gate.yaml`** e deve ser citado pelo artefato principal.
- `storyboard_com_safe_zones.md` ou formato nativo equivalente: materializa **storyboard com safe zones** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: insight 20, especificidade 20, prova 20, distinção 15, adequação ao formato 15, compliance 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Meta Advertising Standards**, Meta (official, força: primary). Aplicação: Policy gate and prohibited-claim checklist. Localizador: https://transparency.meta.com/policies/ad-standards/. Consulta: 2026-08-24.
2. **Google Ads Creative Best Practices**, Google (official, força: primary). Aplicação: Asset variation and responsive-ad constraints. Localizador: https://support.google.com/google-ads/answer/6167122. Consulta: 2026-08-24.
3. **Ogilvy on Advertising**, David Ogilvy (book, força: canonical). Aplicação: Research-led promise, headline and proof discipline. Localizador: Vintage, 1985, ISBN 9780394729039. Consulta: 2026-08-24.
