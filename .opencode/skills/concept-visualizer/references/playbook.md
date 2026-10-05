# Playbook operacional — Relation-to-Form Compiler

## Pergunta de controle

qual forma visual representa a relação essencial sem distorcê-la?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **frase nuclear** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **progressive disclosure** responde à pergunta sem extrapolar o dado? Se não, selecione **alternate-text narrative.** e declare a troca.
3. Há uma destas exceções: causalidade exige evidência; relações múltiplas podem pedir small multiples; diagrama denso divide vistas, não reduz fonte.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual forma visual representa a relação essencial sem distorcê-la?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Frase nuclear**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Entidades/relações**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tipo (hierarquia, fluxo, ciclo, mapa, matriz, causalidade)**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Nível de abstração**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Layout**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Teste de leitura**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fonte renderizável.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual grammar**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Preattentive hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Label economy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternate-text narrative.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Causalidade exige evidência. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Relações múltiplas podem pedir small multiples. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama denso divide vistas, não reduz fonte.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “entidades/relações” cita evidência identificada, aplica “progressive disclosure”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Relation-to-Form Compiler foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `concept_graph_json.md` ou formato nativo equivalente: materializa **`concept-graph.json`** e deve ser citado pelo artefato principal.
- `diagram_mmd.md` ou formato nativo equivalente: materializa **`diagram.mmd`** e deve ser citado pelo artefato principal.
- `legend_alt_text.md` ou formato nativo equivalente: materializa **legend/alt-text** e deve ser citado pelo artefato principal.
- `card_de_escolha_de_nota_o.md` ou formato nativo equivalente: materializa **card de escolha de notação** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fidelidade semântica 30, legibilidade 25, hierarquia 20, economia 15, acessibilidade 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Back of the Napkin**, Dan Roam (book, força: canonical). Aplicação: Visual encoding by who/what/how/when/where/why. Localizador: Portfolio, 2008, ISBN 9781591841999. Consulta: 2026-08-24.
2. **Visual Thinking**, Rudolf Arnheim (book, força: canonical). Aplicação: Perceptual reasoning and abstraction. Localizador: University of California Press, 1969, ISBN 9780520242265. Consulta: 2026-08-24.
3. **Diagram as Code**, Mermaid (official, força: primary). Aplicação: Reproducible concept diagrams. Localizador: https://mermaid.js.org/intro/. Consulta: 2026-08-24.
