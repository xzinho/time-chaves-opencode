#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: market-research
description: "Executa Question-to-Evidence Protocol para responder: que desenho responde à pergunta com validade suficiente para a decisão?"
---

# Market Research

## Escopo e gatilhos

Use quando a decisão real for: **que desenho responde à pergunta com validade suficiente para a decisão?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Question-to-Evidence Protocol**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Question-to-Evidence Protocol

1. **Decision/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Constructs/hypotheses**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desk research**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Qualitative/quantitative design**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sample/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Instrument pilot**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fieldwork qa**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Analysis**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Recommendation.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Triangulation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sampling plan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive pretest**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Coding frame**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence intervals/effect sizes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Nonresponse analysis.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Convenience sample rotulada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pergunta sensível protege participante. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado secundário incompatível não é combinado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fit do desenho 25, validade 25, amostra 15, transparência 20, utilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `sampling_plan_xlsx.md` ou formato nativo equivalente: materializa **`sampling-plan.xlsx`** e deve ser citado pelo artefato principal.
- `questionnaire_md.md` ou formato nativo equivalente: materializa **`questionnaire.md`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `evidence_table.md` ou formato nativo equivalente: materializa **evidence table** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (standard, força: primary). Aplicação: Ethical research, consent and transparency. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **Marketing Research, 8th ed.**, Naresh Malhotra (book, força: canonical). Aplicação: Research design, sampling and analysis. Localizador: Pearson, 2019, ISBN 9780134734842. Consulta: 2026-08-24.
3. **Pesquisa Nacional por Amostra de Domicílios**, IBGE (official, força: primary). Aplicação: Authoritative Brazilian population and labor estimates. Localizador: https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Question-to-Evidence Protocol

## Pergunta de controle

que desenho responde à pergunta com validade suficiente para a decisão?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **decision/question** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **triangulation** responde à pergunta sem extrapolar o dado? Se não, selecione **nonresponse analysis.** e declare a troca.
3. Há uma destas exceções: convenience sample rotulada; pergunta sensível protege participante; dado secundário incompatível não é combinado.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que desenho responde à pergunta com validade suficiente para a decisão?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Decision/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Constructs/hypotheses**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desk research**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Qualitative/quantitative design**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sample/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Instrument pilot**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fieldwork qa**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Analysis**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Recommendation.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Triangulation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sampling plan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive pretest**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Coding frame**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence intervals/effect sizes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Nonresponse analysis.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Convenience sample rotulada. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pergunta sensível protege participante. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado secundário incompatível não é combinado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “constructs/hypotheses” cita evidência identificada, aplica “triangulation”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Question-to-Evidence Protocol foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `sampling_plan_xlsx.md` ou formato nativo equivalente: materializa **`sampling-plan.xlsx`** e deve ser citado pelo artefato principal.
- `questionnaire_md.md` ou formato nativo equivalente: materializa **`questionnaire.md`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `evidence_table.md` ou formato nativo equivalente: materializa **evidence table** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fit do desenho 25, validade 25, amostra 15, transparência 20, utilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (standard, força: primary). Aplicação: Ethical research, consent and transparency. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **Marketing Research, 8th ed.**, Naresh Malhotra (book, força: canonical). Aplicação: Research design, sampling and analysis. Localizador: Pearson, 2019, ISBN 9780134734842. Consulta: 2026-08-24.
3. **Pesquisa Nacional por Amostra de Domicílios**, IBGE (official, força: primary). Aplicação: Authoritative Brazilian population and labor estimates. Localizador: https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html. Consulta: 2026-08-24.


# Template — Question-to-Evidence Protocol

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | que desenho responde à pergunta com validade suficiente para a decisão? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Decision/question

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Constructs/hypotheses

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Desk research

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Qualitative/quantitative design

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Sample/frame

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Instrument pilot

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Fieldwork qa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Analysis

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Limitations

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 10. Recommendation.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Question-to-Evidence Protocol

### `research-protocol.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `sampling-plan.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `questionnaire.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `codebook.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### evidence table

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

fit do desenho 25, validade 25, amostra 15, transparência 20, utilidade 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `convenience sample rotulada; pergunta sensível protege participante; dado secundário incompatível não é combinado.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Market Research Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "(min(d['market_size']/10000000,1)*25+d['growth_rate']*100*.25+(1-d['competition_intensity'])*25+d['evidence_quality']*25)"
}


{
  "version": "3.1.9",
  "skill": "market-research",
  "required": [
    "market_size",
    "growth_rate",
    "competition_intensity",
    "evidence_quality",
    "reachable_share"
  ],
  "outputs": [
    "attractiveness_score",
    "reachable_value",
    "confidence"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Question-to-Evidence Protocol",
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
        "decision_question",
        "constructs_hypotheses",
        "desk_research",
        "qualitative_quantitative_design",
        "sample_frame",
        "instrument_pilot",
        "fieldwork_qa",
        "analysis",
        "limitations",
        "recommendation"
      ],
      "properties": {
        "decision_question": {
          "type": "string",
          "minLength": 3
        },
        "constructs_hypotheses": {
          "type": "string",
          "minLength": 3
        },
        "desk_research": {
          "type": "string",
          "minLength": 3
        },
        "qualitative_quantitative_design": {
          "type": "string",
          "minLength": 3
        },
        "sample_frame": {
          "type": "string",
          "minLength": 3
        },
        "instrument_pilot": {
          "type": "string",
          "minLength": 3
        },
        "fieldwork_qa": {
          "type": "string",
          "minLength": 3
        },
        "analysis": {
          "type": "string",
          "minLength": 3
        },
        "limitations": {
          "type": "string",
          "minLength": 3
        },
        "recommendation": {
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
  "competition_intensity": 0.5,
  "evidence_quality": 0.8,
  "reachable_share": 0.02
}


{
  "market_size": "not-a-number",
  "growth_rate": 0.1,
  "competition_intensity": 0.5,
  "evidence_quality": 0.8,
  "reachable_share": 0.02
}


{
  "market_size": -1,
  "growth_rate": 0.1,
  "competition_intensity": 0.5,
  "evidence_quality": 0.8,
  "reachable_share": 0.02
}


{
  "market_size": 10,
  "growth_rate": 1.1,
  "competition_intensity": 0.5,
  "evidence_quality": 0.8,
  "reachable_share": 0.02
}


{
  "market_size": 20,
  "growth_rate": 2.1,
  "competition_intensity": 0.5,
  "evidence_quality": 0.8,
  "reachable_share": 0.02
}


{
  "market_size": 30,
  "growth_rate": 3.1,
  "competition_intensity": 0.5,
  "evidence_quality": 0.8,
  "reachable_share": 0.02
}


## 21. market-research — Question-to-Evidence Protocol

- **Decisão:** que desenho responde à pergunta com validade suficiente para a decisão?
- **Fluxo:** decision/question → constructs/hypotheses → desk research → qualitative/quantitative design → sample/frame → instrument pilot → fieldwork QA → analysis → limitations → recommendation.
- **Técnicas:** triangulation; sampling plan; cognitive pretest; coding frame; confidence intervals/effect sizes; nonresponse analysis.
- **Exceções:** convenience sample rotulada; pergunta sensível protege participante; dado secundário incompatível não é combinado.
- **Rubrica:** fit do desenho 25, validade 25, amostra 15, transparência 20, utilidade 15.
- **Recursos:** `research-protocol.md`, `sampling-plan.xlsx`, `questionnaire.md`, `codebook.csv`, evidence table.


[
  {
    "type": "standard",
    "title": "ICC/ESOMAR International Code",
    "author": "ICC and ESOMAR",
    "url": "https://esomar.org/code-and-guidelines/icc-esomar-code",
    "strength": "primary",
    "use": "Ethical research, consent and transparency"
  },
  {
    "type": "book",
    "title": "Marketing Research, 8th ed.",
    "author": "Naresh Malhotra",
    "reference": "Pearson, 2019, ISBN 9780134734842",
    "strength": "canonical",
    "use": "Research design, sampling and analysis"
  },
  {
    "type": "official",
    "title": "Pesquisa Nacional por Amostra de Domicílios",
    "author": "IBGE",
    "url": "https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html",
    "strength": "primary",
    "use": "Authoritative Brazilian population and labor estimates"
  }
]"""
import argparse, json, pathlib, sys
slug='market-research'; required=['market_size', 'growth_rate', 'competition_intensity', 'evidence_quality', 'reachable_share']; metric='attractiveness'
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
    value=(min(d['market_size']/10000000,1)*25+d['growth_rate']*100*.25+(1-d['competition_intensity'])*25+d['evidence_quality']*25)
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
