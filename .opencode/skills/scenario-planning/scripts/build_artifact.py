#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: scenario-planning
description: "Executa Uncertainty-to-Options para responder: quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?"
---

# Scenario Planning

## Escopo e gatilhos

Use quando a decisão real for: **quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Uncertainty-to-Options**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Uncertainty-to-Options

1. **Focal question/horizon**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Environmental scan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Forces**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Predetermineds**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Rank impact/uncertainty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Scenario logics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Narratives/quantification**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Strategy wind-tunnel**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Options**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Indicators/triggers.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **2×2 only when orthogonal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Morphological scenarios**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Causal loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consistency check**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Signposts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **No-regret/hedge/options.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Scenario is not forecast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Black swan gets contingency, not fake probability. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Contradictions trigger rewrite.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: plausibility 20, distinctness 20, causal coherence 20, strategic stress 20, indicators 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `driver_register_csv.md` ou formato nativo equivalente: materializa **`driver-register.csv`** e deve ser citado pelo artefato principal.
- `scenario_logic_yaml.md` ou formato nativo equivalente: materializa **`scenario-logic.yaml`** e deve ser citado pelo artefato principal.
- `wind_tunnel_xlsx.md` ou formato nativo equivalente: materializa **`wind-tunnel.xlsx`** e deve ser citado pelo artefato principal.
- `signpost_dashboard_md.md` ou formato nativo equivalente: materializa **`signpost-dashboard.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Art of the Long View**, Peter Schwartz (book, força: canonical). Aplicação: Driving forces, critical uncertainties and narratives. Localizador: Doubleday, 1991, ISBN 9780385267328. Consulta: 2026-08-24.
2. **Scenario Planning Guide**, UK Government Office for Science (official, força: primary). Aplicação: Futures toolkit and policy stress-testing. Localizador: https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts. Consulta: 2026-08-24.
3. **Thinking in Systems**, Donella Meadows (book, força: canonical). Aplicação: Feedback loops, delays and leverage points. Localizador: Chelsea Green, 2008, ISBN 9781603580557. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Uncertainty-to-Options

## Pergunta de controle

quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **focal question/horizon** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **2×2 only when orthogonal** responde à pergunta sem extrapolar o dado? Se não, selecione **no-regret/hedge/options.** e declare a troca.
3. Há uma destas exceções: scenario is not forecast; black swan gets contingency, not fake probability; contradictions trigger rewrite.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Focal question/horizon**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Environmental scan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Forces**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Predetermineds**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Rank impact/uncertainty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Scenario logics**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Narratives/quantification**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Strategy wind-tunnel**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Options**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Indicators/triggers.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **2×2 only when orthogonal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Morphological scenarios**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Causal loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consistency check**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Signposts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **No-regret/hedge/options.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Scenario is not forecast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Black swan gets contingency, not fake probability. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Contradictions trigger rewrite.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “environmental scan” cita evidência identificada, aplica “2×2 only when orthogonal”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Uncertainty-to-Options foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `driver_register_csv.md` ou formato nativo equivalente: materializa **`driver-register.csv`** e deve ser citado pelo artefato principal.
- `scenario_logic_yaml.md` ou formato nativo equivalente: materializa **`scenario-logic.yaml`** e deve ser citado pelo artefato principal.
- `wind_tunnel_xlsx.md` ou formato nativo equivalente: materializa **`wind-tunnel.xlsx`** e deve ser citado pelo artefato principal.
- `signpost_dashboard_md.md` ou formato nativo equivalente: materializa **`signpost-dashboard.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: plausibility 20, distinctness 20, causal coherence 20, strategic stress 20, indicators 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Art of the Long View**, Peter Schwartz (book, força: canonical). Aplicação: Driving forces, critical uncertainties and narratives. Localizador: Doubleday, 1991, ISBN 9780385267328. Consulta: 2026-08-24.
2. **Scenario Planning Guide**, UK Government Office for Science (official, força: primary). Aplicação: Futures toolkit and policy stress-testing. Localizador: https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts. Consulta: 2026-08-24.
3. **Thinking in Systems**, Donella Meadows (book, força: canonical). Aplicação: Feedback loops, delays and leverage points. Localizador: Chelsea Green, 2008, ISBN 9781603580557. Consulta: 2026-08-24.


# Template — Uncertainty-to-Options

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | quais opções são robustas em futuros plausíveis e quais sinais acionam mudança? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Focal question/horizon

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Environmental scan

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Forces

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Predetermineds

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Rank impact/uncertainty

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Scenario logics

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Narratives/quantification

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Strategy wind-tunnel

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Options

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 10. Indicators/triggers.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Uncertainty-to-Options

### `driver-register.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `scenario-logic.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `wind-tunnel.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `signpost-dashboard.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

plausibility 20, distinctness 20, causal coherence 20, strategic stress 20, indicators 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `scenario is not forecast; black swan gets contingency, not fake probability; contradictions trigger rewrite.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Scenario Planning Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "d['downside']*d['p_downside']+d['base']*d['p_base']+d['upside']*d['p_upside']"
}


{
  "version": "3.1.9",
  "skill": "scenario-planning",
  "required": [
    "downside",
    "base",
    "upside",
    "p_downside",
    "p_base",
    "p_upside"
  ],
  "outputs": [
    "expected_value",
    "range",
    "probability_sum"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Uncertainty-to-Options",
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
        "focal_question_horizon",
        "environmental_scan",
        "forces",
        "predetermineds",
        "rank_impact_uncertainty",
        "scenario_logics",
        "narratives_quantification",
        "strategy_wind_tunnel",
        "options",
        "indicators_triggers"
      ],
      "properties": {
        "focal_question_horizon": {
          "type": "string",
          "minLength": 3
        },
        "environmental_scan": {
          "type": "string",
          "minLength": 3
        },
        "forces": {
          "type": "string",
          "minLength": 3
        },
        "predetermineds": {
          "type": "string",
          "minLength": 3
        },
        "rank_impact_uncertainty": {
          "type": "string",
          "minLength": 3
        },
        "scenario_logics": {
          "type": "string",
          "minLength": 3
        },
        "narratives_quantification": {
          "type": "string",
          "minLength": 3
        },
        "strategy_wind_tunnel": {
          "type": "string",
          "minLength": 3
        },
        "options": {
          "type": "string",
          "minLength": 3
        },
        "indicators_triggers": {
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
  "base": 10,
  "upside": 10,
  "p_downside": 0.2,
  "p_base": 0.5,
  "p_upside": 0.3
}


{
  "downside": "not-a-number",
  "base": 10,
  "upside": 10,
  "p_downside": 0.2,
  "p_base": 0.5,
  "p_upside": 0.3
}


{
  "downside": 10,
  "base": 10,
  "upside": 10,
  "p_downside": 0.5,
  "p_base": 0.5,
  "p_upside": 0.5
}


{
  "downside": 10,
  "base": 11,
  "upside": 10,
  "p_downside": 0.2,
  "p_base": 0.5,
  "p_upside": 0.3
}


{
  "downside": 20,
  "base": 12,
  "upside": 10,
  "p_downside": 0.2,
  "p_base": 0.5,
  "p_upside": 0.3
}


{
  "downside": 30,
  "base": 13,
  "upside": 10,
  "p_downside": 0.2,
  "p_base": 0.5,
  "p_upside": 0.3
}


## 31. scenario-planning — Uncertainty-to-Options

- **Decisão:** quais opções são robustas em futuros plausíveis e quais sinais acionam mudança?
- **Fluxo:** focal question/horizon → environmental scan → forces → predetermineds → rank impact/uncertainty → scenario logics → narratives/quantification → strategy wind-tunnel → options → indicators/triggers.
- **Técnicas:** 2×2 only when orthogonal; morphological scenarios; causal loop; consistency check; signposts; no-regret/hedge/options.
- **Exceções:** scenario is not forecast; black swan gets contingency, not fake probability; contradictions trigger rewrite.
- **Rubrica:** plausibility 20, distinctness 20, causal coherence 20, strategic stress 20, indicators 20.
- **Recursos:** `driver-register.csv`, `scenario-logic.yaml`, `wind-tunnel.xlsx`, `signpost-dashboard.md`.


[
  {
    "type": "book",
    "title": "The Art of the Long View",
    "author": "Peter Schwartz",
    "reference": "Doubleday, 1991, ISBN 9780385267328",
    "strength": "canonical",
    "use": "Driving forces, critical uncertainties and narratives"
  },
  {
    "type": "official",
    "title": "Scenario Planning Guide",
    "author": "UK Government Office for Science",
    "url": "https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts",
    "strength": "primary",
    "use": "Futures toolkit and policy stress-testing"
  },
  {
    "type": "book",
    "title": "Thinking in Systems",
    "author": "Donella Meadows",
    "reference": "Chelsea Green, 2008, ISBN 9781603580557",
    "strength": "canonical",
    "use": "Feedback loops, delays and leverage points"
  }
]"""
import argparse, json, pathlib, sys
slug='scenario-planning'; required=['downside', 'base', 'upside', 'p_downside', 'p_base', 'p_upside']; metric='expected_value'
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
    value=d['downside']*d['p_downside']+d['base']*d['p_base']+d['upside']*d['p_upside']
    result={'expected_value': value, 'range': d['upside']-d['downside'], 'probability_sum': d['p_downside']+d['p_base']+d['p_upside']}
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
