# Playbook operacional — Claim-Beat-Retention Script

## Pergunta de controle

what sequence earns attention, builds belief and converts within duration/platform constraints?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **audience/awareness/offer** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **open loop** responde à pergunta sem extrapolar o dado? Se não, selecione **CTA singularity.** e declare a troca.
3. Há uma destas exceções: no fake scarcity; testimonial claims verified; short form compresses beats, not logic; spoken cadence tested aloud.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what sequence earns attention, builds belief and converts within duration/platform constraints?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Audience/awareness/offer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Core promise**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Claim-proof inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Hook variants**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Problem stakes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mechanism**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Proof/demo**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objections**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Beat/timecode**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Visual/audio directions**. Registre entrada, transformação, evidência e saída antes de avançar.
12. **Read-time/claim qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Open loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Concrete demonstration**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pattern interrupt**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof pacing**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection stack**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cta singularity.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- No fake scarcity. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Testimonial claims verified. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Short form compresses beats, not logic. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Spoken cadence tested aloud.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “core promise” cita evidência identificada, aplica “open loop”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Claim-Beat-Retention Script foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `vsl_beat_sheet_csv.md` ou formato nativo equivalente: materializa **`vsl-beat-sheet.csv`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `broll_map_md.md` ou formato nativo equivalente: materializa **`broll-map.md`** e deve ser citado pelo artefato principal.
- `timecoded_script_and_variants.md` ou formato nativo equivalente: materializa **timecoded script and variants** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: hook 20, belief progression 20, proof 20, retention pacing 15, offer/CTA 15, compliance 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Save the Cat!**, Blake Snyder (book, força: canonical). Aplicação: Beat architecture and pacing, adapted clean-room. Localizador: Michael Wiese Productions, 2005, ISBN 9781932907001. Consulta: 2026-08-24.
2. **YouTube Creator Academy**, YouTube (official, força: primary). Aplicação: Audience retention, packaging and platform constraints. Localizador: https://creatoracademy.youtube.com/. Consulta: 2026-08-24.
3. **Made to Stick**, Chip Heath and Dan Heath (book, força: canonical). Aplicação: Concrete, credible and emotionally memorable messages. Localizador: Random House, 2007, ISBN 9781400064281. Consulta: 2026-08-24.
