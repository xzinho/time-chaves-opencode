#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: business-health-diagnostic
description: "Executa Causal Health Map para responder: qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?"
---

# Business Health Diagnostic

## Escopo e gatilhos

Use quando a decisão real for: **qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Causal Health Map**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Causal Health Map

1. **Outcomes/tendências**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Value model**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Drivers por mercado/cliente/operação/pessoas/finanças**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Symptom-to-cause tree**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Evidence/confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Constraints**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **30/60/90.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Driver tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Five-whys com evidência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Constraint map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capability maturity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Leading/lagging indicators.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Sazonalidade e choque externo são segmentados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Falta de baseline vira coleta. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Nota agregada nunca oculta falha crítica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: causalidade 25, evidência 25, materialidade 20, executabilidade 20, aprendizagem 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `driver_tree_yaml.md` ou formato nativo equivalente: materializa **`driver-tree.yaml`** e deve ser citado pelo artefato principal.
- `health_scorecard_xlsx.md` ou formato nativo equivalente: materializa **`health-scorecard.xlsx`** e deve ser citado pelo artefato principal.
- `constraint_register_csv.md` ou formato nativo equivalente: materializa **`constraint-register.csv`** e deve ser citado pelo artefato principal.
- `plano_30_60_90.md` ou formato nativo equivalente: materializa **plano 30/60/90** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **EFQM Model**, EFQM (standard, força: primary). Aplicação: Systemic diagnosis of direction, execution and results. Localizador: https://efqm.org/the-efqm-model/. Consulta: 2026-08-24.
2. **Business Model Canvas**, Strategyzer (official, força: primary). Aplicação: Business-model coherence map. Localizador: https://www.strategyzer.com/library/the-business-model-canvas. Consulta: 2026-08-24.
3. **Good Strategy/Bad Strategy**, Richard Rumelt (book, força: canonical). Aplicação: Diagnosis, guiding policy and coherent actions. Localizador: Crown Business, 2011, ISBN 9780307886231. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Causal Health Map

## Pergunta de controle

qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **outcomes/tendências** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **driver tree** responde à pergunta sem extrapolar o dado? Se não, selecione **leading/lagging indicators.** e declare a troca.
3. Há uma destas exceções: sazonalidade e choque externo são segmentados; falta de baseline vira coleta; nota agregada nunca oculta falha crítica.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Outcomes/tendências**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Value model**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Drivers por mercado/cliente/operação/pessoas/finanças**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Symptom-to-cause tree**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Evidence/confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Constraints**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **30/60/90.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Driver tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Five-whys com evidência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Constraint map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Capability maturity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Leading/lagging indicators.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Sazonalidade e choque externo são segmentados. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Falta de baseline vira coleta. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Nota agregada nunca oculta falha crítica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “value model” cita evidência identificada, aplica “driver tree”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Causal Health Map foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `driver_tree_yaml.md` ou formato nativo equivalente: materializa **`driver-tree.yaml`** e deve ser citado pelo artefato principal.
- `health_scorecard_xlsx.md` ou formato nativo equivalente: materializa **`health-scorecard.xlsx`** e deve ser citado pelo artefato principal.
- `constraint_register_csv.md` ou formato nativo equivalente: materializa **`constraint-register.csv`** e deve ser citado pelo artefato principal.
- `plano_30_60_90.md` ou formato nativo equivalente: materializa **plano 30/60/90** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: causalidade 25, evidência 25, materialidade 20, executabilidade 20, aprendizagem 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **EFQM Model**, EFQM (standard, força: primary). Aplicação: Systemic diagnosis of direction, execution and results. Localizador: https://efqm.org/the-efqm-model/. Consulta: 2026-08-24.
2. **Business Model Canvas**, Strategyzer (official, força: primary). Aplicação: Business-model coherence map. Localizador: https://www.strategyzer.com/library/the-business-model-canvas. Consulta: 2026-08-24.
3. **Good Strategy/Bad Strategy**, Richard Rumelt (book, força: canonical). Aplicação: Diagnosis, guiding policy and coherent actions. Localizador: Crown Business, 2011, ISBN 9780307886231. Consulta: 2026-08-24.


# Template — Causal Health Map

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Outcomes/tendências

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Value model

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Drivers por mercado/cliente/operação/pessoas/finanças

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Symptom-to-cause tree

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Evidence/confidence

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Constraints

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. 30/60/90.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Causal Health Map

### `driver-tree.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `health-scorecard.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `constraint-register.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### plano 30/60/90

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

causalidade 25, evidência 25, materialidade 20, executabilidade 20, aprendizagem 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `sazonalidade e choque externo são segmentados; falta de baseline vira coleta; nota agregada nunca oculta falha crítica.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Business Health Diagnostic Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "max(0,min(100, 25 + d['revenue_growth']*100 + d['gross_margin']*40 + min(d['cash_months'],12)*2 - d['customer_concentration']*30))"
}


{
  "version": "3.1.9",
  "skill": "business-health-diagnostic",
  "required": [
    "revenue_growth",
    "gross_margin",
    "cash_months",
    "customer_concentration"
  ],
  "outputs": [
    "score",
    "risk_band",
    "drivers"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Causal Health Map",
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
        "outcomes_tend_ncias",
        "value_model",
        "drivers_por_mercado_cliente_opera_o_pessoas_finan_as",
        "symptom_to_cause_tree",
        "evidence_confidence",
        "constraints",
        "30_60_90"
      ],
      "properties": {
        "outcomes_tend_ncias": {
          "type": "string",
          "minLength": 3
        },
        "value_model": {
          "type": "string",
          "minLength": 3
        },
        "drivers_por_mercado_cliente_opera_o_pessoas_finan_as": {
          "type": "string",
          "minLength": 3
        },
        "symptom_to_cause_tree": {
          "type": "string",
          "minLength": 3
        },
        "evidence_confidence": {
          "type": "string",
          "minLength": 3
        },
        "constraints": {
          "type": "string",
          "minLength": 3
        },
        "30_60_90": {
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
  "cash_months": 6,
  "customer_concentration": 0.2
}


{
  "revenue_growth": "not-a-number",
  "gross_margin": 0.4,
  "cash_months": 6,
  "customer_concentration": 0.2
}


{
  "revenue_growth": -1,
  "gross_margin": 0.4,
  "cash_months": 6,
  "customer_concentration": 0.2
}


{
  "revenue_growth": 0.05,
  "gross_margin": 0.4,
  "cash_months": 6,
  "customer_concentration": 0.2
}


{
  "revenue_growth": 0.1,
  "gross_margin": 0.45,
  "cash_months": 6,
  "customer_concentration": 0.2
}


{
  "revenue_growth": 0.15000000000000002,
  "gross_margin": 0.5,
  "cash_months": 6,
  "customer_concentration": 0.2
}


## 5. business-health-diagnostic — Causal Health Map

- **Decisão:** qual gargalo sistêmico explica mais resultados e deve ser atacado primeiro?
- **Fluxo:** outcomes/tendências → value model → drivers por mercado/cliente/operação/pessoas/finanças → symptom-to-cause tree → evidence/confidence → constraints → 30/60/90.
- **Técnicas:** driver tree; five-whys com evidência; constraint map; capability maturity; leading/lagging indicators.
- **Exceções:** sazonalidade e choque externo são segmentados; falta de baseline vira coleta; nota agregada nunca oculta falha crítica.
- **Rubrica:** causalidade 25, evidência 25, materialidade 20, executabilidade 20, aprendizagem 10.
- **Recursos:** `driver-tree.yaml`, `health-scorecard.xlsx`, `constraint-register.csv`, plano 30/60/90.


[
  {
    "type": "standard",
    "title": "EFQM Model",
    "author": "EFQM",
    "url": "https://efqm.org/the-efqm-model/",
    "strength": "primary",
    "use": "Systemic diagnosis of direction, execution and results"
  },
  {
    "type": "official",
    "title": "Business Model Canvas",
    "author": "Strategyzer",
    "url": "https://www.strategyzer.com/library/the-business-model-canvas",
    "strength": "primary",
    "use": "Business-model coherence map"
  },
  {
    "type": "book",
    "title": "Good Strategy/Bad Strategy",
    "author": "Richard Rumelt",
    "reference": "Crown Business, 2011, ISBN 9780307886231",
    "strength": "canonical",
    "use": "Diagnosis, guiding policy and coherent actions"
  }
]"""
import argparse, json, pathlib, sys
slug='business-health-diagnostic'; required=['revenue_growth', 'gross_margin', 'cash_months', 'customer_concentration']; metric='health_score'
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
    value=max(0,min(100, 25 + d['revenue_growth']*100 + d['gross_margin']*40 + min(d['cash_months'],12)*2 - d['customer_concentration']*30))
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
