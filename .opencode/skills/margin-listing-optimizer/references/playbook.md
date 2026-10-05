# Playbook operacional — SKU Contribution Engine

## Pergunta de controle

qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **SKU/canal** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **contribution margin** responde à pergunta sem extrapolar o dado? Se não, selecione **sensitivity grid.** e declare a troca.
3. Há uma destas exceções: fee muda por categoria; imposto depende do regime; buy-box/rank são proxies; estoque escasso altera objetivo.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Sku/canal**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Fee/tax/shipping/returns/ads waterfall**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Current margin**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Competitor/content audit**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Price scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Listing experiments**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Guardrails**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Monitor.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Contribution margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Break-even roas**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Return-adjusted margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Price ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Content completeness**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sensitivity grid.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Fee muda por categoria. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Imposto depende do regime. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Buy-box/rank são proxies. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Estoque escasso altera objetivo.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “fee/tax/shipping/returns/ads waterfall” cita evidência identificada, aplica “contribution margin”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de SKU Contribution Engine foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `sku_waterfall_xlsx.md` ou formato nativo equivalente: materializa **`sku-waterfall.xlsx`** e deve ser citado pelo artefato principal.
- `fee_table_csv.md` ou formato nativo equivalente: materializa **`fee-table.csv`** e deve ser citado pelo artefato principal.
- `listing_scorecard_yaml.md` ou formato nativo equivalente: materializa **`listing-scorecard.yaml`** e deve ser citado pelo artefato principal.
- `experiment_backlog.md` ou formato nativo equivalente: materializa **experiment backlog** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: cálculo 30, completude de custo 20, oportunidade do listing 15, cenário 20, guardrails 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Amazon Seller Fees**, Amazon (official, força: primary). Aplicação: Marketplace fee and fulfillment-cost inventory. Localizador: https://sell.amazon.com/pricing. Consulta: 2026-08-24.
2. **Mercado Livre Custos de Venda**, Mercado Livre (official, força: primary). Aplicação: Brazilian marketplace commission and shipping constraints. Localizador: https://www.mercadolivre.com.br/ajuda/Custos-de-vender-um-produto_870. Consulta: 2026-08-24.
3. **Pricing and Revenue Optimization**, Robert Phillips (book, força: canonical). Aplicação: Price-response, contribution and constrained optimization. Localizador: Stanford University Press, 2005, ISBN 9780804746984. Consulta: 2026-08-24.
