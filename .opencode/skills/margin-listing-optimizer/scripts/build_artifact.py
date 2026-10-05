#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: margin-listing-optimizer
description: "Executa SKU Contribution Engine para responder: qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails?"
---

# Margin Listing Optimizer

## Escopo e gatilhos

Use quando a decisão real for: **qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **SKU Contribution Engine**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método SKU Contribution Engine

1. **Sku/canal**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Fee/tax/shipping/returns/ads waterfall**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Current margin**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Competitor/content audit**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Price scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Listing experiments**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Guardrails**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Monitor.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Contribution margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Break-even roas**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Return-adjusted margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Price ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Content completeness**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sensitivity grid.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Fee muda por categoria. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Imposto depende do regime. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Buy-box/rank são proxies. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Estoque escasso altera objetivo.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cálculo 30, completude de custo 20, oportunidade do listing 15, cenário 20, guardrails 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `sku_waterfall_xlsx.md` ou formato nativo equivalente: materializa **`sku-waterfall.xlsx`** e deve ser citado pelo artefato principal.
- `fee_table_csv.md` ou formato nativo equivalente: materializa **`fee-table.csv`** e deve ser citado pelo artefato principal.
- `listing_scorecard_yaml.md` ou formato nativo equivalente: materializa **`listing-scorecard.yaml`** e deve ser citado pelo artefato principal.
- `experiment_backlog.md` ou formato nativo equivalente: materializa **experiment backlog** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Amazon Seller Fees**, Amazon (official, força: primary). Aplicação: Marketplace fee and fulfillment-cost inventory. Localizador: https://sell.amazon.com/pricing. Consulta: 2026-08-24.
2. **Mercado Livre Custos de Venda**, Mercado Livre (official, força: primary). Aplicação: Brazilian marketplace commission and shipping constraints. Localizador: https://www.mercadolivre.com.br/ajuda/Custos-de-vender-um-produto_870. Consulta: 2026-08-24.
3. **Pricing and Revenue Optimization**, Robert Phillips (book, força: canonical). Aplicação: Price-response, contribution and constrained optimization. Localizador: Stanford University Press, 2005, ISBN 9780804746984. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


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


# Template — SKU Contribution Engine

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Sku/canal

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Fee/tax/shipping/returns/ads waterfall

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Current margin

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Competitor/content audit

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Price scenarios

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Listing experiments

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Guardrails

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Monitor.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de SKU Contribution Engine

### `sku-waterfall.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `fee-table.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `listing-scorecard.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### experiment backlog

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

cálculo 30, completude de custo 20, oportunidade do listing 15, cenário 20, guardrails 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `fee muda por categoria; imposto depende do regime; buy-box/rank são proxies; estoque escasso altera objetivo.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Margin Listing Optimizer Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "d['sale_price']-d['product_cost']-d['sale_price']*d['marketplace_fee_rate']-d['shipping']-d['ad_cost']"
}


{
  "version": "3.1.9",
  "skill": "margin-listing-optimizer",
  "required": [
    "sale_price",
    "product_cost",
    "marketplace_fee_rate",
    "shipping",
    "ad_cost",
    "conversion_rate"
  ],
  "outputs": [
    "net_margin",
    "margin_rate",
    "profit_per_100_visits"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "SKU Contribution Engine",
  "type": "object",
  "required": [
    "objective",
    "context",
    "owner",
    "due_date",
    "evidence",
    "steps"
  ],
  "properties": {
    "objective": {
      "type": "string",
      "minLength": 8
    },
    "context": {
      "type": "string",
      "minLength": 8
    },
    "owner": {
      "type": "string",
      "minLength": 2
    },
    "due_date": {
      "type": "string",
      "format": "date"
    },
    "evidence": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": [
          "id",
          "claim",
          "source",
          "kind"
        ],
        "properties": {
          "id": {
            "type": "string"
          },
          "claim": {
            "type": "string"
          },
          "source": {
            "type": "string"
          },
          "kind": {
            "enum": [
              "fact",
              "inference",
              "hypothesis"
            ]
          }
        }
      }
    },
    "steps": {
      "type": "object",
      "required": [
        "sku_canal",
        "fee_tax_shipping_returns_ads_waterfall",
        "current_margin",
        "competitor_content_audit",
        "price_scenarios",
        "listing_experiments",
        "guardrails",
        "monitor"
      ],
      "properties": {
        "sku_canal": {
          "type": "string",
          "minLength": 3
        },
        "fee_tax_shipping_returns_ads_waterfall": {
          "type": "string",
          "minLength": 3
        },
        "current_margin": {
          "type": "string",
          "minLength": 3
        },
        "competitor_content_audit": {
          "type": "string",
          "minLength": 3
        },
        "price_scenarios": {
          "type": "string",
          "minLength": 3
        },
        "listing_experiments": {
          "type": "string",
          "minLength": 3
        },
        "guardrails": {
          "type": "string",
          "minLength": 3
        },
        "monitor": {
          "type": "string",
          "minLength": 3
        }
      }
    },
    "decision": {
      "type": "string"
    },
    "risks": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}


[
  {
    "id": "positive-1",
    "kind": "positive",
    "fixture": "positive-1.json",
    "invariants": [
      "exit=0",
      "assets_consumed",
      "skill_matches",
      "result_nonempty",
      "output_distinct"
    ]
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "invariants": [
      "exit=0",
      "assets_consumed",
      "skill_matches",
      "result_nonempty",
      "output_distinct"
    ]
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "invariants": [
      "exit=0",
      "assets_consumed",
      "skill_matches",
      "result_nonempty",
      "output_distinct"
    ]
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "failure_class": "missing_required",
    "invariants": [
      "exit!=0",
      "no_artifact",
      "distinct_error"
    ]
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "failure_class": "wrong_type",
    "invariants": [
      "exit!=0",
      "no_artifact",
      "distinct_error"
    ]
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "failure_class": "domain_violation",
    "invariants": [
      "exit!=0",
      "no_artifact",
      "distinct_error"
    ]
  }
]


{
  "product_cost": 10,
  "marketplace_fee_rate": 0.15,
  "shipping": 10,
  "ad_cost": 10,
  "conversion_rate": 0.03
}


{
  "sale_price": "not-a-number",
  "product_cost": 10,
  "marketplace_fee_rate": 0.15,
  "shipping": 10,
  "ad_cost": 10,
  "conversion_rate": 0.03
}


{
  "sale_price": -1,
  "product_cost": 10,
  "marketplace_fee_rate": 0.15,
  "shipping": 10,
  "ad_cost": 10,
  "conversion_rate": 0.03
}


{
  "sale_price": 10,
  "product_cost": 11,
  "marketplace_fee_rate": 0.15,
  "shipping": 10,
  "ad_cost": 10,
  "conversion_rate": 0.03
}


{
  "sale_price": 20,
  "product_cost": 12,
  "marketplace_fee_rate": 0.15,
  "shipping": 10,
  "ad_cost": 10,
  "conversion_rate": 0.03
}


{
  "sale_price": 30,
  "product_cost": 13,
  "marketplace_fee_rate": 0.15,
  "shipping": 10,
  "ad_cost": 10,
  "conversion_rate": 0.03
}


## 20. margin-listing-optimizer — SKU Contribution Engine

- **Decisão:** qual preço/listing/fulfillment maximiza contribuição respeitando demanda e guardrails?
- **Fluxo:** SKU/canal → fee/tax/shipping/returns/ads waterfall → current margin → competitor/content audit → price scenarios → listing experiments → guardrails → monitor.
- **Técnicas:** contribution margin; break-even ROAS; return-adjusted margin; price ladder; content completeness; sensitivity grid.
- **Exceções:** fee muda por categoria; imposto depende do regime; buy-box/rank são proxies; estoque escasso altera objetivo.
- **Rubrica:** cálculo 30, completude de custo 20, oportunidade do listing 15, cenário 20, guardrails 15.
- **Recursos:** `sku-waterfall.xlsx`, `fee-table.csv`, `listing-scorecard.yaml`, experiment backlog.


[
  {
    "type": "official",
    "title": "Amazon Seller Fees",
    "author": "Amazon",
    "url": "https://sell.amazon.com/pricing",
    "strength": "primary",
    "use": "Marketplace fee and fulfillment-cost inventory"
  },
  {
    "type": "official",
    "title": "Mercado Livre Custos de Venda",
    "author": "Mercado Livre",
    "url": "https://www.mercadolivre.com.br/ajuda/Custos-de-vender-um-produto_870",
    "strength": "primary",
    "use": "Brazilian marketplace commission and shipping constraints"
  },
  {
    "type": "book",
    "title": "Pricing and Revenue Optimization",
    "author": "Robert Phillips",
    "reference": "Stanford University Press, 2005, ISBN 9780804746984",
    "strength": "canonical",
    "use": "Price-response, contribution and constrained optimization"
  }
]"""
import argparse, json, pathlib, sys
slug='margin-listing-optimizer'; required=['sale_price', 'product_cost', 'marketplace_fee_rate', 'shipping', 'ad_cost', 'conversion_rate']; metric='net_margin'
def load_asset(name):
    p=pathlib.Path(__file__).resolve().parents[1]/'assets'/name
    return json.loads(p.read_text())
def group_totals(d):
    out={}
    for row in d.get('rows',[]):
        key=str(row[d['group_field']]); out[key]=out.get(key,0)+float(row[d['value_field']])
    return out

def analyze(d):
    schema=load_asset('schema.json'); methodology=load_asset('methodology.json')
    missing=[k for k in required if k not in d]
    if missing: raise ValueError('missing required: '+','.join(missing))
    if slug == 'spreadsheet-analyst' and not isinstance(d['rows'],list): raise TypeError('rows must be a list')
    if slug == 'scenario-planning' and abs(d['p_downside']+d['p_base']+d['p_upside']-1)>1e-9: raise ValueError('probabilities must sum to 1')
    if slug == 'unit-economics-budgeting' and (d['monthly_churn']<=0 or d['cac']<=0): raise ValueError('churn and CAC must be positive')
    if slug == 'spreadsheet-analyst' and (not d['rows'] or any(d['value_field'] not in r or d['group_field'] not in r for r in d['rows'])): raise ValueError('row fields missing')
    if slug != 'spreadsheet-analyst' and any(not isinstance(d[k],(int,float)) or isinstance(d[k],bool) for k in required): raise TypeError('numeric fields required')
    if slug != 'spreadsheet-analyst' and any(d[k] < 0 for k in required): raise ValueError('non-negative domain required')
    value=d['sale_price']-d['product_cost']-d['sale_price']*d['marketplace_fee_rate']-d['shipping']-d['ad_cost']
    result={metric: value, 'inputs_used': len(required), 'decision': ('GO' if value >= methodology['threshold'] else 'REVIEW')}
    return {'skill':slug,'methodology':methodology['name'],'asset_version':schema['version'],'result':result,'assumptions':d.get('assumptions',[])}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('-o','--output'); a=ap.parse_args()
    try:
        data=json.loads(pathlib.Path(a.input).read_text()); out=analyze(data)
    except (OSError,json.JSONDecodeError,ValueError,TypeError,ZeroDivisionError) as e:
        print('ERROR: '+str(e),file=sys.stderr); return 2
    text=json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)
    if a.output: pathlib.Path(a.output).write_text(text+'\n')
    else: print(text)
    return 0
if __name__=='__main__': raise SystemExit(main())
