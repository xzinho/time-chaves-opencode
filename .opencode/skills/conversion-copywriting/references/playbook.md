# Playbook operacional — Awareness-Proof Sequence

## Pergunta de controle

que próxima crença o leitor precisa aceitar para agir?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **voice-of-customer** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **message hierarchy** responde à pergunta sem extrapolar o dado? Se não, selecione **variant isolation.** e declare a troca.
3. Há uma destas exceções: prova fraca reduz claim; mercado saturado exige mecanismo/distinção; urgência deve ser factual.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que próxima crença o leitor precisa aceitar para agir?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Voice-of-customer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Estágio/sofisticação**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desired action**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Belief chain**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Headline/promessa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mecanismo**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Prova**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objection handling**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Substantiation/read-aloud.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Message hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Specificity ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk reversal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Friction audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant isolation.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Prova fraca reduz claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mercado saturado exige mecanismo/distinção. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Urgência deve ser factual.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “estágio/sofisticação” cita evidência identificada, aplica “message hierarchy”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Awareness-Proof Sequence foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `voc_bank_csv.md` ou formato nativo equivalente: materializa **`voc-bank.csv`** e deve ser citado pelo artefato principal.
- `belief_chain_yaml.md` ou formato nativo equivalente: materializa **`belief-chain.yaml`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `variant_sheet.md` ou formato nativo equivalente: materializa **variant sheet** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: relevância 20, clareza 20, credibilidade 20, progressão 15, oferta 15, ética/compliance 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Scientific Advertising**, Claude Hopkins (book, força: canonical). Aplicação: Specific claims, reason-why and measurable response. Localizador: Lord & Thomas, 1923; public domain. Consulta: 2026-08-24.
2. **Breakthrough Advertising**, Eugene Schwartz (book, força: canonical). Aplicação: Awareness stages and market sophistication. Localizador: Boardroom, 1966, ISBN 9780887232984. Consulta: 2026-08-24.
3. **Truth In Advertising**, US FTC (official, força: primary). Aplicação: Claim substantiation and deception guardrails. Localizador: https://www.ftc.gov/news-events/topics/truth-advertising. Consulta: 2026-08-24.
