# Playbook operacional — Multi-Signal Category Scan

## Pergunta de controle

categoria/produto mostra oportunidade defensável após fees, competição e operação?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **category taxonomy** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **signal triangulation** responde à pergunta sem extrapolar o dado? Se não, selecione **temporal snapshots.** e declare a troca.
3. Há uma destas exceções: rank não é volume; scraping obedece termos; páginas personalizadas registram região/login; promoção separada de preço regular.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **categoria/produto mostra oportunidade defensável após fees, competição e operação?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Category taxonomy**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Query set**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Demand signals**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Seller/listing census**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Review mining**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Fee/logistics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Price/rank snapshots**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Validation test.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Signal triangulation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Review jobs/pains coding**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Assortment map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Seller concentration**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Temporal snapshots.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Rank não é volume. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Scraping obedece termos. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Páginas personalizadas registram região/login. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Promoção separada de preço regular.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “query set” cita evidência identificada, aplica “signal triangulation”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Multi-Signal Category Scan foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `marketplace_snapshot_csv.md` ou formato nativo equivalente: materializa **`marketplace-snapshot.csv`** e deve ser citado pelo artefato principal.
- `review_codebook_yaml.md` ou formato nativo equivalente: materializa **`review-codebook.yaml`** e deve ser citado pelo artefato principal.
- `assortment_map_xlsx.md` ou formato nativo equivalente: materializa **`assortment-map.xlsx`** e deve ser citado pelo artefato principal.
- `source_log.md` ou formato nativo equivalente: materializa **source log** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: cobertura 20, triangulação 25, economia 20, gap 20, limitações 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Amazon Best Sellers**, Amazon (official, força: primary). Aplicação: Observable rank/category signal with timestamp caveat. Localizador: https://www.amazon.com.br/gp/bestsellers. Consulta: 2026-08-24.
2. **Google Trends Help**, Google (official, força: primary). Aplicação: Normalized demand direction and geographic comparison. Localizador: https://support.google.com/trends/. Consulta: 2026-08-24.
3. **Platform Revolution**, Parker, Van Alstyne, Choudary (book, força: canonical). Aplicação: Marketplace sides, network effects and governance. Localizador: Norton, 2016, ISBN 9780393249132. Consulta: 2026-08-24.
