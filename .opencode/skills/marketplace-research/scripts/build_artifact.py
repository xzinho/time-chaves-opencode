#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: marketplace-research
description: "Executa Multi-Signal Category Scan para responder: categoria/produto mostra oportunidade defensável após fees, competição e operação?"
---

# Marketplace Research

## Escopo e gatilhos

Use quando a decisão real for: **categoria/produto mostra oportunidade defensável após fees, competição e operação?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Multi-Signal Category Scan**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Multi-Signal Category Scan

1. **Category taxonomy**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Query set**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Demand signals**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Seller/listing census**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Review mining**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Fee/logistics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Price/rank snapshots**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Validation test.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Signal triangulation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Review jobs/pains coding**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Assortment map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Seller concentration**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Temporal snapshots.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Rank não é volume. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Scraping obedece termos. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Páginas personalizadas registram região/login. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Promoção separada de preço regular.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cobertura 20, triangulação 25, economia 20, gap 20, limitações 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `marketplace_snapshot_csv.md` ou formato nativo equivalente: materializa **`marketplace-snapshot.csv`** e deve ser citado pelo artefato principal.
- `review_codebook_yaml.md` ou formato nativo equivalente: materializa **`review-codebook.yaml`** e deve ser citado pelo artefato principal.
- `assortment_map_xlsx.md` ou formato nativo equivalente: materializa **`assortment-map.xlsx`** e deve ser citado pelo artefato principal.
- `source_log.md` ou formato nativo equivalente: materializa **source log** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Amazon Best Sellers**, Amazon (official, força: primary). Aplicação: Observable rank/category signal with timestamp caveat. Localizador: https://www.amazon.com.br/gp/bestsellers. Consulta: 2026-08-24.
2. **Google Trends Help**, Google (official, força: primary). Aplicação: Normalized demand direction and geographic comparison. Localizador: https://support.google.com/trends/. Consulta: 2026-08-24.
3. **Platform Revolution**, Parker, Van Alstyne, Choudary (book, força: canonical). Aplicação: Marketplace sides, network effects and governance. Localizador: Norton, 2016, ISBN 9780393249132. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


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


# Template — Multi-Signal Category Scan

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | categoria/produto mostra oportunidade defensável após fees, competição e operação? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Category taxonomy

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Query set

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Demand signals

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Seller/listing census

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Review mining

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Fee/logistics

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Price/rank snapshots

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Gaps

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Validation test.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Multi-Signal Category Scan

### `marketplace-snapshot.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `review-codebook.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `assortment-map.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### source log

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

cobertura 20, triangulação 25, economia 20, gap 20, limitações 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `rank não é volume; scraping obedece termos; páginas personalizadas registram região/login; promoção separada de preço regular.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Marketplace Research Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "d['search_volume']*d['median_price']*(1-d['fee_rate'])*(1+d['review_gap'])/max(d['seller_count'],1)"
}


{
  "version": "3.1.9",
  "skill": "marketplace-research",
  "required": [
    "search_volume",
    "median_price",
    "seller_count",
    "review_gap",
    "fee_rate"
  ],
  "outputs": [
    "revenue_pool_proxy",
    "competition_ratio",
    "opportunity_index"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Multi-Signal Category Scan",
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
        "category_taxonomy",
        "query_set",
        "demand_signals",
        "seller_listing_census",
        "review_mining",
        "fee_logistics",
        "price_rank_snapshots",
        "gaps",
        "validation_test"
      ],
      "properties": {
        "category_taxonomy": {
          "type": "string",
          "minLength": 3
        },
        "query_set": {
          "type": "string",
          "minLength": 3
        },
        "demand_signals": {
          "type": "string",
          "minLength": 3
        },
        "seller_listing_census": {
          "type": "string",
          "minLength": 3
        },
        "review_mining": {
          "type": "string",
          "minLength": 3
        },
        "fee_logistics": {
          "type": "string",
          "minLength": 3
        },
        "price_rank_snapshots": {
          "type": "string",
          "minLength": 3
        },
        "gaps": {
          "type": "string",
          "minLength": 3
        },
        "validation_test": {
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
  "median_price": 10,
  "seller_count": 10,
  "review_gap": 0.2,
  "fee_rate": 0.15
}


{
  "search_volume": "not-a-number",
  "median_price": 10,
  "seller_count": 10,
  "review_gap": 0.2,
  "fee_rate": 0.15
}


{
  "search_volume": -1,
  "median_price": 10,
  "seller_count": 10,
  "review_gap": 0.2,
  "fee_rate": 0.15
}


{
  "search_volume": 10,
  "median_price": 11,
  "seller_count": 10,
  "review_gap": 0.2,
  "fee_rate": 0.15
}


{
  "search_volume": 20,
  "median_price": 12,
  "seller_count": 10,
  "review_gap": 0.2,
  "fee_rate": 0.15
}


{
  "search_volume": 30,
  "median_price": 13,
  "seller_count": 10,
  "review_gap": 0.2,
  "fee_rate": 0.15
}


## 22. marketplace-research — Multi-Signal Category Scan

- **Decisão:** categoria/produto mostra oportunidade defensável após fees, competição e operação?
- **Fluxo:** category taxonomy → query set → demand signals → seller/listing census → review mining → fee/logistics → price/rank snapshots → gaps → validation test.
- **Técnicas:** signal triangulation; review jobs/pains coding; assortment map; seller concentration; temporal snapshots.
- **Exceções:** rank não é volume; scraping obedece termos; páginas personalizadas registram região/login; promoção separada de preço regular.
- **Rubrica:** cobertura 20, triangulação 25, economia 20, gap 20, limitações 15.
- **Recursos:** `marketplace-snapshot.csv`, `review-codebook.yaml`, `assortment-map.xlsx`, source log.


[
  {
    "type": "official",
    "title": "Amazon Best Sellers",
    "author": "Amazon",
    "url": "https://www.amazon.com.br/gp/bestsellers",
    "strength": "primary",
    "use": "Observable rank/category signal with timestamp caveat"
  },
  {
    "type": "official",
    "title": "Google Trends Help",
    "author": "Google",
    "url": "https://support.google.com/trends/",
    "strength": "primary",
    "use": "Normalized demand direction and geographic comparison"
  },
  {
    "type": "book",
    "title": "Platform Revolution",
    "author": "Parker, Van Alstyne, Choudary",
    "reference": "Norton, 2016, ISBN 9780393249132",
    "strength": "canonical",
    "use": "Marketplace sides, network effects and governance"
  }
]"""
import argparse, json, pathlib, sys
slug='marketplace-research'; required=['search_volume', 'median_price', 'seller_count', 'review_gap', 'fee_rate']; metric='opportunity'
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
    value=d['search_volume']*d['median_price']*(1-d['fee_rate'])*(1+d['review_gap'])/max(d['seller_count'],1)
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
