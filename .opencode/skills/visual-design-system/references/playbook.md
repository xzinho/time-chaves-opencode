# Playbook operacional — Token-Component-Governance

## Pergunta de controle

what shared rules reduce inconsistency while enabling branded product expression?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **product audit** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **token aliases** responde à pergunta sem extrapolar o dado? Se não, selecione **deprecation policy.** e declare a troca.
3. Há uma destas exceções: one-off signature component needs rationale; brand token never bypasses contrast; breaking token has migration path.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what shared rules reduce inconsistency while enabling branded product expression?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Product audit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Principles**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Primitive/semantic/component tokens**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Component anatomy/states**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Documentation/examples**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Versioning/contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Adoption metrics.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Token aliases**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant constraints**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contrast/focus tests**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual regression**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deprecation policy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- One-off signature component needs rationale. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Brand token never bypasses contrast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Breaking token has migration path.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “principles” cita evidência identificada, aplica “token aliases”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Token-Component-Governance foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `tokens_json.md` ou formato nativo equivalente: materializa **`tokens.json`** e deve ser citado pelo artefato principal.
- `component_contract_schema_json.md` ou formato nativo equivalente: materializa **`component-contract.schema.json`** e deve ser citado pelo artefato principal.
- `state_matrix_csv.md` ou formato nativo equivalente: materializa **`state-matrix.csv`** e deve ser citado pelo artefato principal.
- `migration_changelog_and_visual_fixtures.md` ou formato nativo equivalente: materializa **migration/changelog and visual fixtures** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: coherence 20, coverage 20, accessibility 20, implementation 20, governance/adoption 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Design Tokens Format Module 2025.10**, W3C Design Tokens Community Group (official, força: primary). Aplicação: Portable token names, types and references. Localizador: https://www.designtokens.org/tr/drafts/format/. Consulta: 2026-08-24.
2. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Accessible component and color constraints. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.
3. **Atomic Design**, Brad Frost (book, força: canonical). Aplicação: Component hierarchy and system governance. Localizador: https://atomicdesign.bradfrost.com/. Consulta: 2026-08-24.
