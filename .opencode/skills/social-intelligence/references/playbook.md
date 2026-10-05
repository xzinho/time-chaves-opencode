# Playbook operacional — Trace-to-Narrative Observatory

## Pergunta de controle

que narrativas/sinais importam, quão confiáveis são e que ação justificam?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **decision/query book** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **purposive sampling** responde à pergunta sem extrapolar o dado? Se não, selecione **narrative lifecycle.** e declare a troca.
3. Há uma destas exceções: engagement unavailable means no traction claim; bot/coordination suspected is flagged; social trace is not population opinion.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que narrativas/sinais importam, quão confiáveis são e que ação justificam?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Decision/query book**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Platform/sample plan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Collect with timestamps**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Dedupe/entities**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code themes/stance/format**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Velocity/novelty**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Corroborate**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Narrative map**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Implications/caveats.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Purposive sampling**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query expansion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Codebook agreement**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source diversity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Anomaly detection**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Narrative lifecycle.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Engagement unavailable means no traction claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/coordination suspected is flagged. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Social trace is not population opinion.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “platform/sample plan” cita evidência identificada, aplica “purposive sampling”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Trace-to-Narrative Observatory foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `query_book_yaml.md` ou formato nativo equivalente: materializa **`query-book.yaml`** e deve ser citado pelo artefato principal.
- `source_ledger_jsonl.md` ou formato nativo equivalente: materializa **`source-ledger.jsonl`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `narrative_map_and_dedupe_state.md` ou formato nativo equivalente: materializa **narrative map and dedupe state** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: provenance 25, coverage 20, coding 20, corroboration 20, caveats/action 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (official, força: primary). Aplicação: Ethical observation and reporting. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **An Introduction to Social Media Research**, Matthew Salganik (book, força: canonical). Aplicação: Digital-trace validity, ethics and representativeness. Localizador: Bit by Bit, Princeton University Press, 2018, ISBN 9780691158648. Consulta: 2026-08-24.
3. **Google Trends Help**, Google (official, força: primary). Aplicação: Cross-checking normalized public interest. Localizador: https://support.google.com/trends/. Consulta: 2026-08-24.
