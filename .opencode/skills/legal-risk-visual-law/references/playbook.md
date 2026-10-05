# Playbook operacional — Meaning-Preserving Legal Design

## Pergunta de controle

como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **legal source** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **layered disclosure** responde à pergunta sem extrapolar o dado? Se não, selecione **semantic crosswalk.** e declare a troca.
3. Há uma destas exceções: ambiguidade substantiva permanece explícita; cor nunca é único canal; documento visual não substitui original quando obrigatório.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Legal source**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Rule/condition/exception/consequence extraction**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Audience task**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Layer architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Visual encoding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Legal fidelity review**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Comprehension test**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Revision.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Layered disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Decision tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk heatmap with criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Before/after comprehension**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic crosswalk.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Ambiguidade substantiva permanece explícita. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Cor nunca é único canal. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Documento visual não substitui original quando obrigatório.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “rule/condition/exception/consequence extraction” cita evidência identificada, aplica “layered disclosure”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Meaning-Preserving Legal Design foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `legal_semantic_map_csv.md` ou formato nativo equivalente: materializa **`legal-semantic-map.csv`** e deve ser citado pelo artefato principal.
- `decision_tree_mmd.md` ou formato nativo equivalente: materializa **`decision-tree.mmd`** e deve ser citado pelo artefato principal.
- `comprehension_script.md` ou formato nativo equivalente: materializa **comprehension script** e deve ser citado pelo artefato principal.
- `fidelity_checklist.md` ou formato nativo equivalente: materializa **fidelity checklist** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fidelidade 30, compreensão 25, actionability 20, acessibilidade 15, rastreabilidade 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Visual Law Library**, Legal Design Alliance (official, força: primary). Aplicação: User-centered legal information design. Localizador: https://www.legaldesignalliance.org/. Consulta: 2026-08-24.
2. **Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Layered explanation without changing legal meaning. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
3. **Legal Design: Integrating Business, Design and Legal Thinking**, Corrales, Fenwick, Haapio (book, força: canonical). Aplicação: Legal-service prototyping and usability. Localizador: Edward Elgar, 2021, ISBN 9781839102271. Consulta: 2026-08-24.
