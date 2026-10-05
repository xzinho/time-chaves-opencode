# Playbook operacional — Semantic Document Pipeline

## Pergunta de controle

como preservar estrutura, identidade e acessibilidade no formato nativo?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **content model** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **semantic styles** responde à pergunta sem extrapolar o dado? Se não, selecione **package inspection.** e declare a troca.
3. Há uma destas exceções: template fornecido é autoridade; PDF não substitui arquivo editável quando exigido; fonte ausente usa fallback explícito.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **como preservar estrutura, identidade e acessibilidade no formato nativo?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Content model**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Style map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Page/section rules**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Components (tables/callouts)**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Links/media**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Generate**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Parse-back**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Visual/accessibility qa**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Export.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Semantic styles**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keep-with-next**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Orphan control**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Repeat headers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alt text**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metadata**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Package inspection.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Template fornecido é autoridade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pdf não substitui arquivo editável quando exigido. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Fonte ausente usa fallback explícito.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “style map” cita evidência identificada, aplica “semantic styles”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Semantic Document Pipeline foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `document_schema_json.md` ou formato nativo equivalente: materializa **`document-schema.json`** e deve ser citado pelo artefato principal.
- `style_map_yaml.md` ou formato nativo equivalente: materializa **`style-map.yaml`** e deve ser citado pelo artefato principal.
- `native_builder.md` ou formato nativo equivalente: materializa **native builder** e deve ser citado pelo artefato principal.
- `parse_back_assertions.md` ou formato nativo equivalente: materializa **parse-back assertions** e deve ser citado pelo artefato principal.
- `render_snapshots.md` ou formato nativo equivalente: materializa **render snapshots** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fidelidade 25, estrutura 20, acessibilidade 20, render 20, editabilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **PDF/UA-1 ISO 14289-1**, ISO (standard, força: primary). Aplicação: Accessible document structure. Localizador: https://www.iso.org/standard/64599.html. Consulta: 2026-08-24.
2. **OOXML ECMA-376**, Ecma International (standard, força: primary). Aplicação: Native Office document packaging and semantics. Localizador: https://ecma-international.org/publications-and-standards/standards/ecma-376/. Consulta: 2026-08-24.
3. **python-docx**, python-openxml (github, força: mature). Aplicação: Reproducible DOCX generation and validation. Localizador: https://github.com/python-openxml/python-docx. Consulta: 2026-08-24.
