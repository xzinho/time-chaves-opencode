#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: unit-economics-budgeting
description: "Executa Unit-Cohort-Driver Budget para responder: which unit creates contribution, at what scale/payback, and how much cash can be committed?"
---

# Unit Economics Budgeting

## Escopo e gatilhos

Use quando a decisão real for: **which unit creates contribution, at what scale/payback, and how much cash can be committed?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Unit-Cohort-Driver Budget**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Unit-Cohort-Driver Budget

1. **Define unit/cohort/time**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Revenue bridge**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Variable/step/fixed costs**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Cac/retention/ltv/payback**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Driver-based budget**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Base/downside/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cash runway/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Cohort curves**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gross/contribution margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Blended vs marginal cac**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Payback**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capacity steps**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rolling forecast.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Ltv limited by observed horizon. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Negative margin blocks scaling. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Accrual profit separated from cash. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Shared costs allocation disclosed.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: unit definition 20, cost completeness 25, cohort evidence 20, scenario 20, guardrails 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `unit_model_xlsx.md` ou formato nativo equivalente: materializa **`unit-model.xlsx`** e deve ser citado pelo artefato principal.
- `cohort_table_csv.md` ou formato nativo equivalente: materializa **`cohort-table.csv`** e deve ser citado pelo artefato principal.
- `budget_drivers_yaml.md` ou formato nativo equivalente: materializa **`budget-drivers.yaml`** e deve ser citado pelo artefato principal.
- `variance_bridge.md` ou formato nativo equivalente: materializa **variance bridge** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Lean Analytics**, Croll and Yoskovitz (book, força: canonical). Aplicação: Business-model-specific unit metrics. Localizador: O'Reilly, 2013, ISBN 9781449335670. Consulta: 2026-08-24.
2. **Financial Intelligence for Entrepreneurs**, Berman and Knight (book, força: recognized). Aplicação: Contribution, working capital and accrual interpretation. Localizador: Harvard Business Review Press, 2008, ISBN 9781422119150. Consulta: 2026-08-24.
3. **Break-even point**, US Small Business Administration (official, força: primary). Aplicação: Cost inventory and cash need framing. Localizador: https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Unit-Cohort-Driver Budget

## Pergunta de controle

which unit creates contribution, at what scale/payback, and how much cash can be committed?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **define unit/cohort/time** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **cohort curves** responde à pergunta sem extrapolar o dado? Se não, selecione **rolling forecast.** e declare a troca.
3. Há uma destas exceções: LTV limited by observed horizon; negative margin blocks scaling; accrual profit separated from cash; shared costs allocation disclosed.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **which unit creates contribution, at what scale/payback, and how much cash can be committed?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Define unit/cohort/time**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Revenue bridge**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Variable/step/fixed costs**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Cac/retention/ltv/payback**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Driver-based budget**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Base/downside/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cash runway/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Cohort curves**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gross/contribution margin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Blended vs marginal cac**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Payback**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capacity steps**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rolling forecast.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Ltv limited by observed horizon. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Negative margin blocks scaling. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Accrual profit separated from cash. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Shared costs allocation disclosed.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “revenue bridge” cita evidência identificada, aplica “cohort curves”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Unit-Cohort-Driver Budget foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `unit_model_xlsx.md` ou formato nativo equivalente: materializa **`unit-model.xlsx`** e deve ser citado pelo artefato principal.
- `cohort_table_csv.md` ou formato nativo equivalente: materializa **`cohort-table.csv`** e deve ser citado pelo artefato principal.
- `budget_drivers_yaml.md` ou formato nativo equivalente: materializa **`budget-drivers.yaml`** e deve ser citado pelo artefato principal.
- `variance_bridge.md` ou formato nativo equivalente: materializa **variance bridge** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: unit definition 20, cost completeness 25, cohort evidence 20, scenario 20, guardrails 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Lean Analytics**, Croll and Yoskovitz (book, força: canonical). Aplicação: Business-model-specific unit metrics. Localizador: O'Reilly, 2013, ISBN 9781449335670. Consulta: 2026-08-24.
2. **Financial Intelligence for Entrepreneurs**, Berman and Knight (book, força: recognized). Aplicação: Contribution, working capital and accrual interpretation. Localizador: Harvard Business Review Press, 2008, ISBN 9781422119150. Consulta: 2026-08-24.
3. **Break-even point**, US Small Business Administration (official, força: primary). Aplicação: Cost inventory and cash need framing. Localizador: https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs. Consulta: 2026-08-24.


# Template — Unit-Cohort-Driver Budget

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | which unit creates contribution, at what scale/payback, and how much cash can be committed? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Define unit/cohort/time

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Revenue bridge

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Variable/step/fixed costs

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Contribution

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Cac/retention/ltv/payback

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Driver-based budget

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Base/downside/upside

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Cash runway/guardrails.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Unit-Cohort-Driver Budget

### `unit-model.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `cohort-table.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `budget-drivers.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### variance bridge

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

unit definition 20, cost completeness 25, cohort evidence 20, scenario 20, guardrails 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `LTV limited by observed horizon; negative margin blocks scaling; accrual profit separated from cash; shared costs allocation disclosed.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Unit Economics Budgeting Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "(d['arpu']*d['gross_margin']/d['monthly_churn'])/d['cac']"
}


{
  "version": "3.1.9",
  "skill": "unit-economics-budgeting",
  "required": [
    "arpu",
    "gross_margin",
    "monthly_churn",
    "cac",
    "budget"
  ],
  "outputs": [
    "ltv",
    "ltv_cac",
    "customers_affordable"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Unit-Cohort-Driver Budget",
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
        "define_unit_cohort_time",
        "revenue_bridge",
        "variable_step_fixed_costs",
        "contribution",
        "cac_retention_ltv_payback",
        "driver_based_budget",
        "base_downside_upside",
        "cash_runway_guardrails"
      ],
      "properties": {
        "define_unit_cohort_time": {
          "type": "string",
          "minLength": 3
        },
        "revenue_bridge": {
          "type": "string",
          "minLength": 3
        },
        "variable_step_fixed_costs": {
          "type": "string",
          "minLength": 3
        },
        "contribution": {
          "type": "string",
          "minLength": 3
        },
        "cac_retention_ltv_payback": {
          "type": "string",
          "minLength": 3
        },
        "driver_based_budget": {
          "type": "string",
          "minLength": 3
        },
        "base_downside_upside": {
          "type": "string",
          "minLength": 3
        },
        "cash_runway_guardrails": {
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
  "gross_margin": 0.4,
  "monthly_churn": 0.05,
  "cac": 10,
  "budget": 10
}


{
  "arpu": "not-a-number",
  "gross_margin": 0.4,
  "monthly_churn": 0.05,
  "cac": 10,
  "budget": 10
}


{
  "arpu": 10,
  "gross_margin": 0.4,
  "monthly_churn": 0,
  "cac": 10,
  "budget": 10
}


{
  "arpu": 10,
  "gross_margin": 1.4,
  "monthly_churn": 0.05,
  "cac": 10,
  "budget": 10
}


{
  "arpu": 20,
  "gross_margin": 2.4,
  "monthly_churn": 0.05,
  "cac": 10,
  "budget": 10
}


{
  "arpu": 30,
  "gross_margin": 3.4,
  "monthly_churn": 0.05,
  "cac": 10,
  "budget": 10
}


## 35. unit-economics-budgeting — Unit-Cohort-Driver Budget

- **Decisão:** which unit creates contribution, at what scale/payback, and how much cash can be committed?
- **Fluxo:** define unit/cohort/time → revenue bridge → variable/step/fixed costs → contribution → CAC/retention/LTV/payback → driver-based budget → base/downside/upside → cash runway/guardrails.
- **Técnicas:** cohort curves; gross/contribution margin; blended vs marginal CAC; payback; capacity steps; rolling forecast.
- **Exceções:** LTV limited by observed horizon; negative margin blocks scaling; accrual profit separated from cash; shared costs allocation disclosed.
- **Rubrica:** unit definition 20, cost completeness 25, cohort evidence 20, scenario 20, guardrails 15.
- **Recursos:** `unit-model.xlsx`, `cohort-table.csv`, `budget-drivers.yaml`, variance bridge.


[
  {
    "type": "book",
    "title": "Lean Analytics",
    "author": "Croll and Yoskovitz",
    "reference": "O'Reilly, 2013, ISBN 9781449335670",
    "strength": "canonical",
    "use": "Business-model-specific unit metrics"
  },
  {
    "type": "book",
    "title": "Financial Intelligence for Entrepreneurs",
    "author": "Berman and Knight",
    "reference": "Harvard Business Review Press, 2008, ISBN 9781422119150",
    "strength": "recognized",
    "use": "Contribution, working capital and accrual interpretation"
  },
  {
    "type": "official",
    "title": "Break-even point",
    "author": "US Small Business Administration",
    "url": "https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs",
    "strength": "primary",
    "use": "Cost inventory and cash need framing"
  }
]"""
import argparse, json, pathlib, sys
slug='unit-economics-budgeting'; required=['arpu', 'gross_margin', 'monthly_churn', 'cac', 'budget']; metric='ltv_cac'
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
    value=(d['arpu']*d['gross_margin']/d['monthly_churn'])/d['cac']
    result={'ltv': d['arpu']*d['gross_margin']/d['monthly_churn'], 'ltv_cac': value, 'customers_affordable': int(d['budget']//d['cac'])}
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
