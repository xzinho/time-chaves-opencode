#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: objection-pipeline-forecast
description: "Executa Evidence-Stage Forecast para responder: qual receita é provável e que objeção/risco impede progressão?"
---

# Objection Pipeline Forecast

## Escopo e gatilhos

Use quando a decisão real for: **qual receita é provável e que objeção/risco impede progressão?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Evidence-Stage Forecast**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Evidence-Stage Forecast

1. **Define stage exit evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Clean opportunities**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Code objections**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Aging/slippage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Base rates by cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Opportunity adjustments**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Commit/base/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Interventions.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Stage evidence checklist**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cohort conversion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted pipeline vs category**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Calibration/brier review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Founder deals separated. Marque a condição no artefato e acione o gate indicado antes do handoff.
- One-off whale scenario. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing next step downgrades. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Verbal enthusiasm is not stage evidence.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: hygiene 20, stage evidence 25, calibration 20, objection diagnosis 20, action 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `pipeline_schema_json.md` ou formato nativo equivalente: materializa **`pipeline-schema.json`** e deve ser citado pelo artefato principal.
- `objection_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`objection-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `forecast_xlsx.md` ou formato nativo equivalente: materializa **`forecast.xlsx`** e deve ser citado pelo artefato principal.
- `deal_inspection_card.md` ou formato nativo equivalente: materializa **deal inspection card** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Need-payoff discovery and objection diagnosis. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Sales Acceleration Formula**, Mark Roberge (book, força: recognized). Aplicação: Stage definitions, data quality and forecast discipline. Localizador: Wiley, 2015, ISBN 9781119047070. Consulta: 2026-08-24.
3. **Forecast Categories**, Salesforce (official, força: primary). Aplicação: Commit/best-case/pipeline semantics. Localizador: https://help.salesforce.com/s/articleView?id=sf.forecasts3_categories.htm&type=5. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Evidence-Stage Forecast

## Pergunta de controle

qual receita é provável e que objeção/risco impede progressão?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **define stage exit evidence** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **stage evidence checklist** responde à pergunta sem extrapolar o dado? Se não, selecione **calibration/Brier review.** e declare a troca.
3. Há uma destas exceções: founder deals separated; one-off whale scenario; missing next step downgrades; verbal enthusiasm is not stage evidence.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual receita é provável e que objeção/risco impede progressão?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Define stage exit evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Clean opportunities**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Code objections**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Aging/slippage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Base rates by cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Opportunity adjustments**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Commit/base/upside**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Interventions.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Stage evidence checklist**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cohort conversion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted pipeline vs category**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Calibration/brier review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Founder deals separated. Marque a condição no artefato e acione o gate indicado antes do handoff.
- One-off whale scenario. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing next step downgrades. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Verbal enthusiasm is not stage evidence.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “clean opportunities” cita evidência identificada, aplica “stage evidence checklist”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Evidence-Stage Forecast foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `pipeline_schema_json.md` ou formato nativo equivalente: materializa **`pipeline-schema.json`** e deve ser citado pelo artefato principal.
- `objection_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`objection-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `forecast_xlsx.md` ou formato nativo equivalente: materializa **`forecast.xlsx`** e deve ser citado pelo artefato principal.
- `deal_inspection_card.md` ou formato nativo equivalente: materializa **deal inspection card** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: hygiene 20, stage evidence 25, calibration 20, objection diagnosis 20, action 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Need-payoff discovery and objection diagnosis. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Sales Acceleration Formula**, Mark Roberge (book, força: recognized). Aplicação: Stage definitions, data quality and forecast discipline. Localizador: Wiley, 2015, ISBN 9781119047070. Consulta: 2026-08-24.
3. **Forecast Categories**, Salesforce (official, força: primary). Aplicação: Commit/best-case/pipeline semantics. Localizador: https://help.salesforce.com/s/articleView?id=sf.forecasts3_categories.htm&type=5. Consulta: 2026-08-24.


# Template — Evidence-Stage Forecast

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual receita é provável e que objeção/risco impede progressão? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Define stage exit evidence

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Clean opportunities

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Code objections

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Aging/slippage

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Base rates by cohort

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Opportunity adjustments

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Commit/base/upside

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Interventions.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Evidence-Stage Forecast

### `pipeline-schema.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `objection-taxonomy.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `forecast.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### deal inspection card

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

hygiene 20, stage evidence 25, calibration 20, objection diagnosis 20, action 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `founder deals separated; one-off whale scenario; missing next step downgrades; verbal enthusiasm is not stage evidence.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Objection Pipeline Forecast Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "d['deals']*d['average_ticket']*d['stage_probability']*(1-d['objection_penalty'])"
}


{
  "version": "3.1.9",
  "skill": "objection-pipeline-forecast",
  "required": [
    "deals",
    "average_ticket",
    "stage_probability",
    "objection_penalty",
    "sales_cycle_days"
  ],
  "outputs": [
    "weighted_pipeline",
    "daily_velocity",
    "forecast_30d"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Evidence-Stage Forecast",
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
        "define_stage_exit_evidence",
        "clean_opportunities",
        "code_objections",
        "aging_slippage",
        "base_rates_by_cohort",
        "opportunity_adjustments",
        "commit_base_upside",
        "interventions"
      ],
      "properties": {
        "define_stage_exit_evidence": {
          "type": "string",
          "minLength": 3
        },
        "clean_opportunities": {
          "type": "string",
          "minLength": 3
        },
        "code_objections": {
          "type": "string",
          "minLength": 3
        },
        "aging_slippage": {
          "type": "string",
          "minLength": 3
        },
        "base_rates_by_cohort": {
          "type": "string",
          "minLength": 3
        },
        "opportunity_adjustments": {
          "type": "string",
          "minLength": 3
        },
        "commit_base_upside": {
          "type": "string",
          "minLength": 3
        },
        "interventions": {
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
  "average_ticket": 10,
  "stage_probability": 0.5,
  "objection_penalty": 0.1,
  "sales_cycle_days": 10
}


{
  "deals": "not-a-number",
  "average_ticket": 10,
  "stage_probability": 0.5,
  "objection_penalty": 0.1,
  "sales_cycle_days": 10
}


{
  "deals": -1,
  "average_ticket": 10,
  "stage_probability": 0.5,
  "objection_penalty": 0.1,
  "sales_cycle_days": 10
}


{
  "deals": 10,
  "average_ticket": 11,
  "stage_probability": 0.5,
  "objection_penalty": 0.1,
  "sales_cycle_days": 10
}


{
  "deals": 20,
  "average_ticket": 12,
  "stage_probability": 0.5,
  "objection_penalty": 0.1,
  "sales_cycle_days": 10
}


{
  "deals": 30,
  "average_ticket": 13,
  "stage_probability": 0.5,
  "objection_penalty": 0.1,
  "sales_cycle_days": 10
}


## 23. objection-pipeline-forecast — Evidence-Stage Forecast

- **Decisão:** qual receita é provável e que objeção/risco impede progressão?
- **Fluxo:** define stage exit evidence → clean opportunities → code objections → aging/slippage → base rates by cohort → opportunity adjustments → commit/base/upside → interventions.
- **Técnicas:** stage evidence checklist; objection taxonomy; cohort conversion; weighted pipeline vs category; calibration/Brier review.
- **Exceções:** founder deals separated; one-off whale scenario; missing next step downgrades; verbal enthusiasm is not stage evidence.
- **Rubrica:** hygiene 20, stage evidence 25, calibration 20, objection diagnosis 20, action 15.
- **Recursos:** `pipeline-schema.json`, `objection-taxonomy.yaml`, `forecast.xlsx`, deal inspection card.


[
  {
    "type": "book",
    "title": "SPIN Selling",
    "author": "Neil Rackham",
    "reference": "McGraw-Hill, 1988, ISBN 9780070511132",
    "strength": "canonical",
    "use": "Need-payoff discovery and objection diagnosis"
  },
  {
    "type": "book",
    "title": "The Sales Acceleration Formula",
    "author": "Mark Roberge",
    "reference": "Wiley, 2015, ISBN 9781119047070",
    "strength": "recognized",
    "use": "Stage definitions, data quality and forecast discipline"
  },
  {
    "type": "official",
    "title": "Forecast Categories",
    "author": "Salesforce",
    "url": "https://help.salesforce.com/s/articleView?id=sf.forecasts3_categories.htm&type=5",
    "strength": "primary",
    "use": "Commit/best-case/pipeline semantics"
  }
]"""
import argparse, json, pathlib, sys
slug='objection-pipeline-forecast'; required=['deals', 'average_ticket', 'stage_probability', 'objection_penalty', 'sales_cycle_days']; metric='weighted_pipeline'
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
    value=d['deals']*d['average_ticket']*d['stage_probability']*(1-d['objection_penalty'])
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
