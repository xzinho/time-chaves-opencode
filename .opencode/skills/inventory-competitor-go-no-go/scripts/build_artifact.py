#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: inventory-competitor-go-no-go
description: "Executa Market-Inventory Gate para responder: entrar, testar condicionado ou não entrar em uma categoria/SKU?"
---

# Inventory Competitor Go No Go

## Escopo e gatilhos

Use quando a decisão real for: **entrar, testar condicionado ou não entrar em uma categoria/SKU?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Market-Inventory Gate**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Market-Inventory Gate

1. **Market boundary**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Substitutes/competitors**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Demand evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Supply/price/fees**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Inventory cash cycle**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Contribution scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Strategic fit**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Kill criteria**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Five forces**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Substitution test**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Landed-cost waterfall**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sell-through/stockout/markdown scenarios**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted evidence.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Rank sem vendas é proxy. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Sazonalidade exige cohort temporal. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Moq e lead time podem vetar margem nominal.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: mercado 20, economia 25, estoque/caixa 20, evidência 20, decisão 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `competitor_inventory_csv.md` ou formato nativo equivalente: materializa **`competitor-inventory.csv`** e deve ser citado pelo artefato principal.
- `landed_cost_xlsx.md` ou formato nativo equivalente: materializa **`landed-cost.xlsx`** e deve ser citado pelo artefato principal.
- `kill_criteria_yaml.md` ou formato nativo equivalente: materializa **`kill-criteria.yaml`** e deve ser citado pelo artefato principal.
- `go_no_go_memo.md` ou formato nativo equivalente: materializa **go/no-go memo** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Competitive Strategy**, Michael E. Porter (book, força: canonical). Aplicação: Industry forces and strategic positioning. Localizador: Free Press, 1980, ISBN 9780684841489. Consulta: 2026-08-24.
2. **Commission Notice on the definition of the relevant market (2024)**, European Commission (official, força: primary). Aplicação: Relevant-market and substitution boundaries. Localizador: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52024XC01645. Consulta: 2026-08-24.
3. **The Art of Profitability**, Adrian Slywotzky (book, força: recognized). Aplicação: Profit-model and inventory-risk lenses. Localizador: Warner Business, 2002, ISBN 9780446692274. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


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


# Template — Market-Inventory Gate

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | entrar, testar condicionado ou não entrar em uma categoria/SKU? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Market boundary

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Substitutes/competitors

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Demand evidence

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Supply/price/fees

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Inventory cash cycle

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Contribution scenarios

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Strategic fit

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Kill criteria

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Gate.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Market-Inventory Gate

### `competitor-inventory.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `landed-cost.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `kill-criteria.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### go/no-go memo

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

mercado 20, economia 25, estoque/caixa 20, evidência 20, decisão 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `rank sem vendas é proxy; sazonalidade exige cohort temporal; MOQ e lead time podem vetar margem nominal.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Inventory Competitor Go No Go Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "(min(d['stock_units']/d['demand_units'],1)*30 + max(0,1-d['lead_time_days']/90)*20 + min(d['competitor_price']/d['our_price'],1.5)*20 + d['gross_margin']*30)"
}


{
  "version": "3.1.9",
  "skill": "inventory-competitor-go-no-go",
  "required": [
    "demand_units",
    "stock_units",
    "lead_time_days",
    "competitor_price",
    "our_price",
    "gross_margin"
  ],
  "outputs": [
    "coverage_ratio",
    "price_index",
    "go_score"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Market-Inventory Gate",
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
        "market_boundary",
        "substitutes_competitors",
        "demand_evidence",
        "supply_price_fees",
        "inventory_cash_cycle",
        "contribution_scenarios",
        "strategic_fit",
        "kill_criteria",
        "gate"
      ],
      "properties": {
        "market_boundary": {
          "type": "string",
          "minLength": 3
        },
        "substitutes_competitors": {
          "type": "string",
          "minLength": 3
        },
        "demand_evidence": {
          "type": "string",
          "minLength": 3
        },
        "supply_price_fees": {
          "type": "string",
          "minLength": 3
        },
        "inventory_cash_cycle": {
          "type": "string",
          "minLength": 3
        },
        "contribution_scenarios": {
          "type": "string",
          "minLength": 3
        },
        "strategic_fit": {
          "type": "string",
          "minLength": 3
        },
        "kill_criteria": {
          "type": "string",
          "minLength": 3
        },
        "gate": {
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
  "stock_units": 10,
  "lead_time_days": 10,
  "competitor_price": 10,
  "our_price": 10,
  "gross_margin": 0.4
}


{
  "demand_units": "not-a-number",
  "stock_units": 10,
  "lead_time_days": 10,
  "competitor_price": 10,
  "our_price": 10,
  "gross_margin": 0.4
}


{
  "demand_units": -1,
  "stock_units": 10,
  "lead_time_days": 10,
  "competitor_price": 10,
  "our_price": 10,
  "gross_margin": 0.4
}


{
  "demand_units": 10,
  "stock_units": 11,
  "lead_time_days": 10,
  "competitor_price": 10,
  "our_price": 10,
  "gross_margin": 0.4
}


{
  "demand_units": 20,
  "stock_units": 12,
  "lead_time_days": 10,
  "competitor_price": 10,
  "our_price": 10,
  "gross_margin": 0.4
}


{
  "demand_units": 30,
  "stock_units": 13,
  "lead_time_days": 10,
  "competitor_price": 10,
  "our_price": 10,
  "gross_margin": 0.4
}


## 18. inventory-competitor-go-no-go — Market-Inventory Gate

- **Decisão:** entrar, testar condicionado ou não entrar em uma categoria/SKU?
- **Fluxo:** market boundary → substitutes/competitors → demand evidence → supply/price/fees → inventory cash cycle → contribution scenarios → strategic fit → kill criteria → gate.
- **Técnicas:** five forces; substitution test; landed-cost waterfall; sell-through/stockout/markdown scenarios; weighted evidence.
- **Exceções:** rank sem vendas é proxy; sazonalidade exige cohort temporal; MOQ e lead time podem vetar margem nominal.
- **Rubrica:** mercado 20, economia 25, estoque/caixa 20, evidência 20, decisão 15.
- **Recursos:** `competitor-inventory.csv`, `landed-cost.xlsx`, `kill-criteria.yaml`, go/no-go memo.


[
  {
    "type": "book",
    "title": "Competitive Strategy",
    "author": "Michael E. Porter",
    "reference": "Free Press, 1980, ISBN 9780684841489",
    "strength": "canonical",
    "use": "Industry forces and strategic positioning"
  },
  {
    "type": "official",
    "title": "Commission Notice on the definition of the relevant market (2024)",
    "author": "European Commission",
    "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52024XC01645",
    "strength": "primary",
    "use": "Relevant-market and substitution boundaries"
  },
  {
    "type": "book",
    "title": "The Art of Profitability",
    "author": "Adrian Slywotzky",
    "reference": "Warner Business, 2002, ISBN 9780446692274",
    "strength": "recognized",
    "use": "Profit-model and inventory-risk lenses"
  }
]"""
import argparse, json, pathlib, sys
slug='inventory-competitor-go-no-go'; required=['demand_units', 'stock_units', 'lead_time_days', 'competitor_price', 'our_price', 'gross_margin']; metric='go_score'
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
    value=(min(d['stock_units']/d['demand_units'],1)*30 + max(0,1-d['lead_time_days']/90)*20 + min(d['competitor_price']/d['our_price'],1.5)*20 + d['gross_margin']*30)
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
