# Playbook operacional — Questão-Norma-Precedente

## Pergunta de controle

qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **fatos/foro/data** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **IRAC adaptado** responde à pergunta sem extrapolar o dado? Se não, selecione **tratamento de precedente contrário.** e declare a troca.
3. Há uma destas exceções: segredo/privacidade; decisão monocrática não equivale a precedente; tema repetitivo/repercussão geral muda peso; escalar prática jurídica.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Fatos/foro/data**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Issues**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Hierarquia normativa**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Vigência/alterações**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Jurisprudência por holding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Correntes e distinções**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Conclusão condicionada**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Citator log.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Irac adaptado**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Árvore de autoridade**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cadeia de vigência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ratio vs obiter**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Tratamento de precedente contrário.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Segredo/privacidade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Decisão monocrática não equivale a precedente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Tema repetitivo/repercussão geral muda peso. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Escalar prática jurídica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “issues” cita evidência identificada, aplica “IRAC adaptado”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Questão-Norma-Precedente foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `authority_table_csv.md` ou formato nativo equivalente: materializa **`authority-table.csv`** e deve ser citado pelo artefato principal.
- `case_brief_md.md` ou formato nativo equivalente: materializa **`case-brief.md`** e deve ser citado pelo artefato principal.
- `citation_validator_py.md` ou formato nativo equivalente: materializa **`citation-validator.py`** e deve ser citado pelo artefato principal.
- `open_questions_md.md` ou formato nativo equivalente: materializa **`open-questions.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: autoridade 25, vigência 20, aderência fática 20, tratamento contrário 15, citações recuperáveis 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Portal da Legislação**, Presidência da República do Brasil (official, força: primary). Aplicação: Authoritative consolidated federal legislation. Localizador: https://www4.planalto.gov.br/legislacao/. Consulta: 2026-08-24.
2. **Pesquisa de Jurisprudência**, STJ (official, força: primary). Aplicação: Binding context, precedent and temporal validity. Localizador: https://scon.stj.jus.br/SCON/. Consulta: 2026-08-24.
3. **Pesquisa de Jurisprudência**, STF (official, força: primary). Aplicação: Constitutional holdings and repercussão geral. Localizador: https://jurisprudencia.stf.jus.br/. Consulta: 2026-08-24.
