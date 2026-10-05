#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: financial-modeling
description: "Executa Inputs-Logic-Outputs-Control para responder: quais drivers explicam outputs e como o modelo reage a incerteza?"
---

# Financial Modeling

## Escopo e gatilhos

Use quando a decisão real for: **quais drivers explicam outputs e como o modelo reage a incerteza?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Inputs-Logic-Outputs-Control**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Inputs-Logic-Outputs-Control

1. **Objective/granularity**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Timeline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Assumptions register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Inputs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Calculation blocks**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Statements/outputs**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Sensitivities/scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Integrity checks**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Review.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Fast conventions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Corkscrew schedules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sign/unit discipline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Scenario switches**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Data tables**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance and circularity checks.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Circularidade só se documentada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Histórico/projeção separados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Hardcode em fórmula é blocker.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: correção 30, transparência 20, estrutura 20, controle 15, decisão 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `workbook_com_estilos_sem_nticos.md` ou formato nativo equivalente: materializa **workbook com estilos semânticos** e deve ser citado pelo artefato principal.
- `assumptions_csv.md` ou formato nativo equivalente: materializa **`assumptions.csv`** e deve ser citado pelo artefato principal.
- `model_checks_yaml.md` ou formato nativo equivalente: materializa **`model-checks.yaml`** e deve ser citado pelo artefato principal.
- `scenario_summary.md` ou formato nativo equivalente: materializa **scenario summary** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Flexible, appropriate, structured and transparent models. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Principles of Financial Modelling**, Michael Rees (book, força: canonical). Aplicação: Model architecture, checks and scenarios. Localizador: Wiley, 2018, ISBN 9781118904015. Consulta: 2026-08-24.
3. **Financial Modeling, 4th ed.**, Simon Benninga (book, força: canonical). Aplicação: Spreadsheet model architecture, valuation and auditability. Localizador: MIT Press, 2014, ISBN 9780262027281. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Inputs-Logic-Outputs-Control

## Pergunta de controle

quais drivers explicam outputs e como o modelo reage a incerteza?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **objective/granularity** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **FAST conventions** responde à pergunta sem extrapolar o dado? Se não, selecione **balance and circularity checks.** e declare a troca.
3. Há uma destas exceções: circularidade só se documentada; histórico/projeção separados; hardcode em fórmula é blocker.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **quais drivers explicam outputs e como o modelo reage a incerteza?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Objective/granularity**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Timeline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Assumptions register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Inputs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Calculation blocks**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Statements/outputs**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Sensitivities/scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Integrity checks**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Review.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Fast conventions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Corkscrew schedules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sign/unit discipline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Scenario switches**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Data tables**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance and circularity checks.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Circularidade só se documentada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Histórico/projeção separados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Hardcode em fórmula é blocker.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “timeline” cita evidência identificada, aplica “FAST conventions”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Inputs-Logic-Outputs-Control foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `workbook_com_estilos_sem_nticos.md` ou formato nativo equivalente: materializa **workbook com estilos semânticos** e deve ser citado pelo artefato principal.
- `assumptions_csv.md` ou formato nativo equivalente: materializa **`assumptions.csv`** e deve ser citado pelo artefato principal.
- `model_checks_yaml.md` ou formato nativo equivalente: materializa **`model-checks.yaml`** e deve ser citado pelo artefato principal.
- `scenario_summary.md` ou formato nativo equivalente: materializa **scenario summary** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: correção 30, transparência 20, estrutura 20, controle 15, decisão 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Flexible, appropriate, structured and transparent models. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Principles of Financial Modelling**, Michael Rees (book, força: canonical). Aplicação: Model architecture, checks and scenarios. Localizador: Wiley, 2018, ISBN 9781118904015. Consulta: 2026-08-24.
3. **Financial Modeling, 4th ed.**, Simon Benninga (book, força: canonical). Aplicação: Spreadsheet model architecture, valuation and auditability. Localizador: MIT Press, 2014, ISBN 9780262027281. Consulta: 2026-08-24.


# Template — Inputs-Logic-Outputs-Control

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | quais drivers explicam outputs e como o modelo reage a incerteza? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Objective/granularity

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Timeline

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Assumptions register

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Inputs

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Calculation blocks

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Statements/outputs

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Sensitivities/scenarios

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Integrity checks

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Review.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Inputs-Logic-Outputs-Control

### workbook com estilos semânticos

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `assumptions.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `model-checks.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### scenario summary

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

correção 30, transparência 20, estrutura 20, controle 15, decisão 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `circularidade só se documentada; histórico/projeção separados; hardcode em fórmula é blocker.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Financial Modeling Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "d['base_revenue']*((1+d['growth_rate'])**int(d['years']))*d['ebitda_margin']*d['multiple']"
}


{
  "version": "3.1.9",
  "skill": "financial-modeling",
  "required": [
    "base_revenue",
    "growth_rate",
    "ebitda_margin",
    "multiple",
    "years"
  ],
  "outputs": [
    "projected_revenue",
    "projected_ebitda",
    "enterprise_value"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Inputs-Logic-Outputs-Control",
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
        "objective_granularity",
        "timeline",
        "assumptions_register",
        "inputs",
        "calculation_blocks",
        "statements_outputs",
        "sensitivities_scenarios",
        "integrity_checks",
        "review"
      ],
      "properties": {
        "objective_granularity": {
          "type": "string",
          "minLength": 3
        },
        "timeline": {
          "type": "string",
          "minLength": 3
        },
        "assumptions_register": {
          "type": "string",
          "minLength": 3
        },
        "inputs": {
          "type": "string",
          "minLength": 3
        },
        "calculation_blocks": {
          "type": "string",
          "minLength": 3
        },
        "statements_outputs": {
          "type": "string",
          "minLength": 3
        },
        "sensitivities_scenarios": {
          "type": "string",
          "minLength": 3
        },
        "integrity_checks": {
          "type": "string",
          "minLength": 3
        },
        "review": {
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
  "growth_rate": 0.1,
  "ebitda_margin": 10,
  "multiple": 10,
  "years": 10
}


{
  "base_revenue": "not-a-number",
  "growth_rate": 0.1,
  "ebitda_margin": 10,
  "multiple": 10,
  "years": 10
}


{
  "base_revenue": -1,
  "growth_rate": 0.1,
  "ebitda_margin": 10,
  "multiple": 10,
  "years": 10
}


{
  "base_revenue": 10,
  "growth_rate": 1.1,
  "ebitda_margin": 10,
  "multiple": 10,
  "years": 10
}


{
  "base_revenue": 20,
  "growth_rate": 2.1,
  "ebitda_margin": 10,
  "multiple": 10,
  "years": 10
}


{
  "base_revenue": 30,
  "growth_rate": 3.1,
  "ebitda_margin": 10,
  "multiple": 10,
  "years": 10
}


## 16. financial-modeling — Inputs-Logic-Outputs-Control

- **Decisão:** quais drivers explicam outputs e como o modelo reage a incerteza?
- **Fluxo:** objective/granularity → timeline → assumptions register → inputs → calculation blocks → statements/outputs → sensitivities/scenarios → integrity checks → review.
- **Técnicas:** FAST conventions; corkscrew schedules; sign/unit discipline; scenario switches; data tables; balance and circularity checks.
- **Exceções:** circularidade só se documentada; histórico/projeção separados; hardcode em fórmula é blocker.
- **Rubrica:** correção 30, transparência 20, estrutura 20, controle 15, decisão 15.
- **Recursos:** workbook com estilos semânticos, `assumptions.csv`, `model-checks.yaml`, scenario summary.


[
  {
    "type": "standard",
    "title": "FAST Standard",
    "author": "FAST Standard Organisation",
    "url": "https://www.fast-standard.org/the-fast-standard/",
    "strength": "primary",
    "use": "Flexible, appropriate, structured and transparent models"
  },
  {
    "type": "book",
    "title": "Principles of Financial Modelling",
    "author": "Michael Rees",
    "reference": "Wiley, 2018, ISBN 9781118904015",
    "strength": "canonical",
    "use": "Model architecture, checks and scenarios"
  },
  {
    "type": "book",
    "title": "Financial Modeling, 4th ed.",
    "author": "Simon Benninga",
    "reference": "MIT Press, 2014, ISBN 9780262027281",
    "strength": "canonical",
    "use": "Spreadsheet model architecture, valuation and auditability"
  }
]"""
import argparse, json, pathlib, sys
slug='financial-modeling'; required=['base_revenue', 'growth_rate', 'ebitda_margin', 'multiple', 'years']; metric='enterprise_value'
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
    value=d['base_revenue']*((1+d['growth_rate'])**int(d['years']))*d['ebitda_margin']*d['multiple']
    result={'projected_revenue': d['base_revenue']*((1+d['growth_rate'])**int(d['years'])), 'projected_ebitda': d['base_revenue']*((1+d['growth_rate'])**int(d['years']))*d['ebitda_margin'], 'enterprise_value': value}
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
