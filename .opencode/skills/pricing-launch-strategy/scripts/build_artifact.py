#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: pricing-launch-strategy
description: "Executa Value-WTP Launch Lab para responder: quem paga quanto por qual bundle, sob quais fences e rollout risks?"
---

# Pricing Launch Strategy

## Escopo e gatilhos

Use quando a decisão real for: **quem paga quanto por qual bundle, sob quais fences e rollout risks?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Value-WTP Launch Lab**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Value-WTP Launch Lab

1. **Segment/jobs**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Alternatives/reference price**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Value drivers**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Wtp research**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Package architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Unit economics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Price scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Launch cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Instrumentation/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Value metric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Conjoint/psm limitations**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Good-better-best**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fences**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Grandfathering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Price waterfall**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rollback trigger.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Psm is exploratory. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Regulated price escalates. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Sparse sample uses ranges. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Discount never hides negative contribution.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: value linkage 25, research 20, economics 20, packaging 15, rollout 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `wtp_study_md.md` ou formato nativo equivalente: materializa **`wtp-study.md`** e deve ser citado pelo artefato principal.
- `package_matrix_xlsx.md` ou formato nativo equivalente: materializa **`package-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `price_waterfall_xlsx.md` ou formato nativo equivalente: materializa **`price-waterfall.xlsx`** e deve ser citado pelo artefato principal.
- `launch_rollback_plan.md` ou formato nativo equivalente: materializa **launch/rollback plan** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Strategy and Tactics of Pricing**, Nagle, Hogan, Zale (book, força: canonical). Aplicação: Value-based segmentation and price fences. Localizador: Routledge, 2016, ISBN 9781138737501. Consulta: 2026-08-24.
2. **Monetizing Innovation**, Madhavan Ramanujam and Georg Tacke (book, força: canonical). Aplicação: Willingness-to-pay before product launch. Localizador: Wiley, 2016, ISBN 9781119240860. Consulta: 2026-08-24.
3. **Van Westendorp Price Sensitivity Meter**, ESOMAR archive (official, força: primary). Aplicação: Exploratory acceptable-price bands with limitations. Localizador: https://ana.esomar.org/documents/price-sensitivity-meter-a-new-approach-to-consumer-perception-of-price. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Value-WTP Launch Lab

## Pergunta de controle

quem paga quanto por qual bundle, sob quais fences e rollout risks?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **segment/jobs** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **value metric** responde à pergunta sem extrapolar o dado? Se não, selecione **rollback trigger.** e declare a troca.
3. Há uma destas exceções: PSM is exploratory; regulated price escalates; sparse sample uses ranges; discount never hides negative contribution.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **quem paga quanto por qual bundle, sob quais fences e rollout risks?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Segment/jobs**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Alternatives/reference price**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Value drivers**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Wtp research**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Package architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Unit economics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Price scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Launch cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Instrumentation/guardrails.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Value metric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Conjoint/psm limitations**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Good-better-best**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fences**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Grandfathering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Price waterfall**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Rollback trigger.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Psm is exploratory. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Regulated price escalates. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Sparse sample uses ranges. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Discount never hides negative contribution.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “alternatives/reference price” cita evidência identificada, aplica “value metric”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Value-WTP Launch Lab foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `wtp_study_md.md` ou formato nativo equivalente: materializa **`wtp-study.md`** e deve ser citado pelo artefato principal.
- `package_matrix_xlsx.md` ou formato nativo equivalente: materializa **`package-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `price_waterfall_xlsx.md` ou formato nativo equivalente: materializa **`price-waterfall.xlsx`** e deve ser citado pelo artefato principal.
- `launch_rollback_plan.md` ou formato nativo equivalente: materializa **launch/rollback plan** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: value linkage 25, research 20, economics 20, packaging 15, rollout 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Strategy and Tactics of Pricing**, Nagle, Hogan, Zale (book, força: canonical). Aplicação: Value-based segmentation and price fences. Localizador: Routledge, 2016, ISBN 9781138737501. Consulta: 2026-08-24.
2. **Monetizing Innovation**, Madhavan Ramanujam and Georg Tacke (book, força: canonical). Aplicação: Willingness-to-pay before product launch. Localizador: Wiley, 2016, ISBN 9781119240860. Consulta: 2026-08-24.
3. **Van Westendorp Price Sensitivity Meter**, ESOMAR archive (official, força: primary). Aplicação: Exploratory acceptable-price bands with limitations. Localizador: https://ana.esomar.org/documents/price-sensitivity-meter-a-new-approach-to-consumer-perception-of-price. Consulta: 2026-08-24.


# Template — Value-WTP Launch Lab

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | quem paga quanto por qual bundle, sob quais fences e rollout risks? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Segment/jobs

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Alternatives/reference price

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Value drivers

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Wtp research

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Package architecture

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Unit economics

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Price scenarios

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Launch cohort

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Instrumentation/guardrails.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Value-WTP Launch Lab

### `wtp-study.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `package-matrix.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `price-waterfall.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### launch/rollback plan

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

value linkage 25, research 20, economics 20, packaging 15, rollout 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `PSM is exploratory; regulated price escalates; sparse sample uses ranges; discount never hides negative contribution.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Pricing Launch Strategy Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "(min(d['price'],d['willingness_to_pay'])-d['variable_cost'])*d['expected_units']-d['launch_cost']"
}


{
  "version": "3.1.9",
  "skill": "pricing-launch-strategy",
  "required": [
    "price",
    "variable_cost",
    "expected_units",
    "launch_cost",
    "willingness_to_pay"
  ],
  "outputs": [
    "unit_margin",
    "break_even_units",
    "launch_contribution"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Value-WTP Launch Lab",
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
        "segment_jobs",
        "alternatives_reference_price",
        "value_drivers",
        "wtp_research",
        "package_architecture",
        "unit_economics",
        "price_scenarios",
        "launch_cohort",
        "instrumentation_guardrails"
      ],
      "properties": {
        "segment_jobs": {
          "type": "string",
          "minLength": 3
        },
        "alternatives_reference_price": {
          "type": "string",
          "minLength": 3
        },
        "value_drivers": {
          "type": "string",
          "minLength": 3
        },
        "wtp_research": {
          "type": "string",
          "minLength": 3
        },
        "package_architecture": {
          "type": "string",
          "minLength": 3
        },
        "unit_economics": {
          "type": "string",
          "minLength": 3
        },
        "price_scenarios": {
          "type": "string",
          "minLength": 3
        },
        "launch_cohort": {
          "type": "string",
          "minLength": 3
        },
        "instrumentation_guardrails": {
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
  "variable_cost": 10,
  "expected_units": 10,
  "launch_cost": 10,
  "willingness_to_pay": 10
}


{
  "price": "not-a-number",
  "variable_cost": 10,
  "expected_units": 10,
  "launch_cost": 10,
  "willingness_to_pay": 10
}


{
  "price": -1,
  "variable_cost": 10,
  "expected_units": 10,
  "launch_cost": 10,
  "willingness_to_pay": 10
}


{
  "price": 10,
  "variable_cost": 11,
  "expected_units": 10,
  "launch_cost": 10,
  "willingness_to_pay": 10
}


{
  "price": 20,
  "variable_cost": 12,
  "expected_units": 10,
  "launch_cost": 10,
  "willingness_to_pay": 10
}


{
  "price": 30,
  "variable_cost": 13,
  "expected_units": 10,
  "launch_cost": 10,
  "willingness_to_pay": 10
}


## 26. pricing-launch-strategy — Value-WTP Launch Lab

- **Decisão:** quem paga quanto por qual bundle, sob quais fences e rollout risks?
- **Fluxo:** segment/jobs → alternatives/reference price → value drivers → WTP research → package architecture → unit economics → price scenarios → launch cohort → instrumentation/guardrails.
- **Técnicas:** value metric; conjoint/PSM limitations; good-better-best; fences; grandfathering; price waterfall; rollback trigger.
- **Exceções:** PSM is exploratory; regulated price escalates; sparse sample uses ranges; discount never hides negative contribution.
- **Rubrica:** value linkage 25, research 20, economics 20, packaging 15, rollout 20.
- **Recursos:** `wtp-study.md`, `package-matrix.xlsx`, `price-waterfall.xlsx`, launch/rollback plan.


[
  {
    "type": "book",
    "title": "The Strategy and Tactics of Pricing",
    "author": "Nagle, Hogan, Zale",
    "reference": "Routledge, 2016, ISBN 9781138737501",
    "strength": "canonical",
    "use": "Value-based segmentation and price fences"
  },
  {
    "type": "book",
    "title": "Monetizing Innovation",
    "author": "Madhavan Ramanujam and Georg Tacke",
    "reference": "Wiley, 2016, ISBN 9781119240860",
    "strength": "canonical",
    "use": "Willingness-to-pay before product launch"
  },
  {
    "type": "official",
    "title": "Van Westendorp Price Sensitivity Meter",
    "author": "ESOMAR archive",
    "url": "https://ana.esomar.org/documents/price-sensitivity-meter-a-new-approach-to-consumer-perception-of-price",
    "strength": "primary",
    "use": "Exploratory acceptable-price bands with limitations"
  }
]"""
import argparse, json, pathlib, sys
slug='pricing-launch-strategy'; required=['price', 'variable_cost', 'expected_units', 'launch_cost', 'willingness_to_pay']; metric='contribution'
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
    value=(min(d['price'],d['willingness_to_pay'])-d['variable_cost'])*d['expected_units']-d['launch_cost']
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
