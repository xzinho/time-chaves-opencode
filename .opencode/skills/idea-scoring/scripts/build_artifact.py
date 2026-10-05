#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: idea-scoring
description: "Executa Evidence-Calibrated Portfolio para responder: investir, experimentar, estacionar ou matar uma ideia?"
---

# Idea Scoring

## Escopo e gatilhos

Use quando a decisão real for: **investir, experimentar, estacionar ou matar uma ideia?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Evidence-Calibrated Portfolio**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Evidence-Calibrated Portfolio

1. **Define outcome/unit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Normalize ideas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Score reach/impact/confidence/effort/strategic fit/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Evidence grade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Uncertainty penalty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Rank**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Portfolio balance**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Next test.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Anchored scales**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence decay**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted score**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sensitivity to weights**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dominance check.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Scores próximos viram empate. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alta upside/baixa confiança recebe experimento. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Veto legal/security sobrepõe ranking.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: definição 15, evidência 25, calibração 20, transparência 20, ação 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `score_rubric_yaml.md` ou formato nativo equivalente: materializa **`score-rubric.yaml`** e deve ser citado pelo artefato principal.
- `idea_portfolio_xlsx.md` ou formato nativo equivalente: materializa **`idea-portfolio.xlsx`** e deve ser citado pelo artefato principal.
- `evidence_card_md.md` ou formato nativo equivalente: materializa **`evidence-card.md`** e deve ser citado pelo artefato principal.
- `sensitivity_plot.md` ou formato nativo equivalente: materializa **sensitivity plot** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Lean Startup**, Eric Ries (book, força: canonical). Aplicação: Leap-of-faith assumptions and validated learning. Localizador: Crown Business, 2011, ISBN 9780307887894. Consulta: 2026-08-24.
2. **Testing Business Ideas**, David Bland and Alexander Osterwalder (book, força: canonical). Aplicação: Assumption mapping and experiment selection. Localizador: Wiley, 2019, ISBN 9781119551447. Consulta: 2026-08-24.
3. **RICE Prioritization**, Intercom (official, força: primary). Aplicação: Reach-impact-confidence-effort normalization. Localizador: https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Evidence-Calibrated Portfolio

## Pergunta de controle

investir, experimentar, estacionar ou matar uma ideia?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **define outcome/unit** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **anchored scales** responde à pergunta sem extrapolar o dado? Se não, selecione **dominance check.** e declare a troca.
3. Há uma destas exceções: scores próximos viram empate; alta upside/baixa confiança recebe experimento; veto legal/security sobrepõe ranking.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **investir, experimentar, estacionar ou matar uma ideia?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Define outcome/unit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Normalize ideas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Score reach/impact/confidence/effort/strategic fit/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Evidence grade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Uncertainty penalty**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Rank**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Portfolio balance**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Next test.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Anchored scales**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence decay**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Weighted score**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sensitivity to weights**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dominance check.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Scores próximos viram empate. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alta upside/baixa confiança recebe experimento. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Veto legal/security sobrepõe ranking.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “normalize ideas” cita evidência identificada, aplica “anchored scales”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Evidence-Calibrated Portfolio foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `score_rubric_yaml.md` ou formato nativo equivalente: materializa **`score-rubric.yaml`** e deve ser citado pelo artefato principal.
- `idea_portfolio_xlsx.md` ou formato nativo equivalente: materializa **`idea-portfolio.xlsx`** e deve ser citado pelo artefato principal.
- `evidence_card_md.md` ou formato nativo equivalente: materializa **`evidence-card.md`** e deve ser citado pelo artefato principal.
- `sensitivity_plot.md` ou formato nativo equivalente: materializa **sensitivity plot** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: definição 15, evidência 25, calibração 20, transparência 20, ação 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Lean Startup**, Eric Ries (book, força: canonical). Aplicação: Leap-of-faith assumptions and validated learning. Localizador: Crown Business, 2011, ISBN 9780307887894. Consulta: 2026-08-24.
2. **Testing Business Ideas**, David Bland and Alexander Osterwalder (book, força: canonical). Aplicação: Assumption mapping and experiment selection. Localizador: Wiley, 2019, ISBN 9781119551447. Consulta: 2026-08-24.
3. **RICE Prioritization**, Intercom (official, força: primary). Aplicação: Reach-impact-confidence-effort normalization. Localizador: https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/. Consulta: 2026-08-24.


# Template — Evidence-Calibrated Portfolio

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | investir, experimentar, estacionar ou matar uma ideia? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Define outcome/unit

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Normalize ideas

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Score reach/impact/confidence/effort/strategic fit/risk

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Evidence grade

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Uncertainty penalty

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Rank

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Portfolio balance

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Next test.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Evidence-Calibrated Portfolio

### `score-rubric.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `idea-portfolio.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `evidence-card.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### sensitivity plot

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

definição 15, evidência 25, calibração 20, transparência 20, ação 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `scores próximos viram empate; alta upside/baixa confiança recebe experimento; veto legal/security sobrepõe ranking.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Idea Scoring Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "(d['impact']*0.35+d['confidence']*0.25+d['ease']*0.15+d['strategic_fit']*0.25)*(1 if d['evidence_count']>=2 else .6)"
}


{
  "version": "3.1.9",
  "skill": "idea-scoring",
  "required": [
    "impact",
    "confidence",
    "ease",
    "strategic_fit",
    "evidence_count"
  ],
  "outputs": [
    "weighted_score",
    "evidence_penalty",
    "decision"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Evidence-Calibrated Portfolio",
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
        "define_outcome_unit",
        "normalize_ideas",
        "score_reach_impact_confidence_effort_strategic_fit_risk",
        "evidence_grade",
        "uncertainty_penalty",
        "rank",
        "portfolio_balance",
        "next_test"
      ],
      "properties": {
        "define_outcome_unit": {
          "type": "string",
          "minLength": 3
        },
        "normalize_ideas": {
          "type": "string",
          "minLength": 3
        },
        "score_reach_impact_confidence_effort_strategic_fit_risk": {
          "type": "string",
          "minLength": 3
        },
        "evidence_grade": {
          "type": "string",
          "minLength": 3
        },
        "uncertainty_penalty": {
          "type": "string",
          "minLength": 3
        },
        "rank": {
          "type": "string",
          "minLength": 3
        },
        "portfolio_balance": {
          "type": "string",
          "minLength": 3
        },
        "next_test": {
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
  "confidence": 10,
  "ease": 10,
  "strategic_fit": 10,
  "evidence_count": 10
}


{
  "impact": "not-a-number",
  "confidence": 10,
  "ease": 10,
  "strategic_fit": 10,
  "evidence_count": 10
}


{
  "impact": -1,
  "confidence": 10,
  "ease": 10,
  "strategic_fit": 10,
  "evidence_count": 10
}


{
  "impact": 10,
  "confidence": 11,
  "ease": 10,
  "strategic_fit": 10,
  "evidence_count": 10
}


{
  "impact": 20,
  "confidence": 12,
  "ease": 10,
  "strategic_fit": 10,
  "evidence_count": 10
}


{
  "impact": 30,
  "confidence": 13,
  "ease": 10,
  "strategic_fit": 10,
  "evidence_count": 10
}


## 17. idea-scoring — Evidence-Calibrated Portfolio

- **Decisão:** investir, experimentar, estacionar ou matar uma ideia?
- **Fluxo:** define outcome/unit → normalize ideas → score reach/impact/confidence/effort/strategic fit/risk → evidence grade → uncertainty penalty → rank → portfolio balance → next test.
- **Técnicas:** anchored scales; confidence decay; weighted score; sensitivity to weights; dominance check.
- **Exceções:** scores próximos viram empate; alta upside/baixa confiança recebe experimento; veto legal/security sobrepõe ranking.
- **Rubrica:** definição 15, evidência 25, calibração 20, transparência 20, ação 20.
- **Recursos:** `score-rubric.yaml`, `idea-portfolio.xlsx`, `evidence-card.md`, sensitivity plot.


[
  {
    "type": "book",
    "title": "The Lean Startup",
    "author": "Eric Ries",
    "reference": "Crown Business, 2011, ISBN 9780307887894",
    "strength": "canonical",
    "use": "Leap-of-faith assumptions and validated learning"
  },
  {
    "type": "book",
    "title": "Testing Business Ideas",
    "author": "David Bland and Alexander Osterwalder",
    "reference": "Wiley, 2019, ISBN 9781119551447",
    "strength": "canonical",
    "use": "Assumption mapping and experiment selection"
  },
  {
    "type": "official",
    "title": "RICE Prioritization",
    "author": "Intercom",
    "url": "https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/",
    "strength": "primary",
    "use": "Reach-impact-confidence-effort normalization"
  }
]"""
import argparse, json, pathlib, sys
slug='idea-scoring'; required=['impact', 'confidence', 'ease', 'strategic_fit', 'evidence_count']; metric='weighted_score'
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
    value=(d['impact']*0.35+d['confidence']*0.25+d['ease']*0.15+d['strategic_fit']*0.25)*(1 if d['evidence_count']>=2 else .6)
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
