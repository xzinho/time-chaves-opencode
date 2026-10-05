# Playbook operacional — Reproducible Evidence Synthesis

## Pergunta de controle

what does the best available evidence support, contradict or leave uncertain?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **protocol/question** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **PRISMA-like log** responde à pergunta sem extrapolar o dado? Se não, selecione **confidence labels.** e declare a troca.
3. Há uma destas exceções: inaccessible source listed, not guessed; snippet is not evidence; dynamic page gets timestamp/archive; AI summary never cited as source.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what does the best available evidence support, contradict or leave uncertain?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Protocol/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Search strings/sources/date**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inclusion/exclusion**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Capture metadata**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Screen**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Extract claims/quotes/context**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Assess authority/recency/directness**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Triangulate**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Synthesize with confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Bibliography/limitations.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Prisma-like log**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Primary-source preference**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Lateral reading**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contradiction table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence labels.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Inaccessible source listed, not guessed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Snippet is not evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dynamic page gets timestamp/archive. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ai summary never cited as source.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “search strings/sources/date” cita evidência identificada, aplica “PRISMA-like log”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Reproducible Evidence Synthesis foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `search_log_csv.md` ou formato nativo equivalente: materializa **`search-log.csv`** e deve ser citado pelo artefato principal.
- `sources_json.md` ou formato nativo equivalente: materializa **`sources.json`** e deve ser citado pelo artefato principal.
- `claim_evidence_csv.md` ou formato nativo equivalente: materializa **`claim-evidence.csv`** e deve ser citado pelo artefato principal.
- `limitations_md.md` ou formato nativo equivalente: materializa **`limitations.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: reproducibility 25, source strength 25, claim traceability 25, contradiction/limits 15, synthesis 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **PRISMA 2020 Statement**, PRISMA (standard, força: primary). Aplicação: Transparent search, screening and inclusion trail. Localizador: https://www.prisma-statement.org/prisma-2020. Consulta: 2026-08-24.
2. **Evaluating Sources**, Library of Congress (official, força: primary). Aplicação: Authority, provenance and corroboration checks. Localizador: https://guides.loc.gov/evaluating-sources. Consulta: 2026-08-24.
3. **Web Annotation Data Model**, W3C (official, força: primary). Aplicação: Quote-level evidence anchors and provenance. Localizador: https://www.w3.org/TR/annotation-model/. Consulta: 2026-08-24.
