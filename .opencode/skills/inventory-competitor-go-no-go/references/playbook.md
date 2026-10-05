# Playbook operacional — Market-Inventory Gate

## Pergunta de controle

entrar, testar condicionado ou não entrar em uma categoria/SKU?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **market boundary** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **five forces** responde à pergunta sem extrapolar o dado? Se não, selecione **weighted evidence.** e declare a troca.
3. Há uma destas exceções: rank sem vendas é proxy; sazonalidade exige cohort temporal; MOQ e lead time podem vetar margem nominal.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **entrar, testar condicionado ou não entrar em uma categoria/SKU?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Market boundary**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Substitutes/competitors**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Demand evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Supply/price/fees**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Inventory cash cycle**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Contribution scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Strategic fit**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Kill criteria**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Five forces**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Substitution test**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Landed-cost waterfall**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sell-through/stockout/markdown scenarios**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted evidence.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Rank sem vendas é proxy. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Sazonalidade exige cohort temporal. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Moq e lead time podem vetar margem nominal.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “substitutes/competitors” cita evidência identificada, aplica “five forces”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Market-Inventory Gate foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `competitor_inventory_csv.md` ou formato nativo equivalente: materializa **`competitor-inventory.csv`** e deve ser citado pelo artefato principal.
- `landed_cost_xlsx.md` ou formato nativo equivalente: materializa **`landed-cost.xlsx`** e deve ser citado pelo artefato principal.
- `kill_criteria_yaml.md` ou formato nativo equivalente: materializa **`kill-criteria.yaml`** e deve ser citado pelo artefato principal.
- `go_no_go_memo.md` ou formato nativo equivalente: materializa **go/no-go memo** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: mercado 20, economia 25, estoque/caixa 20, evidência 20, decisão 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Competitive Strategy**, Michael E. Porter (book, força: canonical). Aplicação: Industry forces and strategic positioning. Localizador: Free Press, 1980, ISBN 9780684841489. Consulta: 2026-08-24.
2. **Commission Notice on the definition of the relevant market (2024)**, European Commission (official, força: primary). Aplicação: Relevant-market and substitution boundaries. Localizador: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52024XC01645. Consulta: 2026-08-24.
3. **The Art of Profitability**, Adrian Slywotzky (book, força: recognized). Aplicação: Profit-model and inventory-risk lenses. Localizador: Warner Business, 2002, ISBN 9780446692274. Consulta: 2026-08-24.
