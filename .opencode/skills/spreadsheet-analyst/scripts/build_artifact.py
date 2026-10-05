#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: spreadsheet-analyst
description: "Executa Workbook Lineage Audit para responder: can the workbook be trusted, what drives outputs, and where are errors/anomalies?"
---

# Spreadsheet Analyst

## Escopo e gatilhos

Use quando a decisão real for: **can the workbook be trusted, what drives outputs, and where are errors/anomalies?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Workbook Lineage Audit**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Workbook Lineage Audit

1. **File inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Sheet/range map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Types/nulls/duplicates**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Formula lineage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Named ranges/external links**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Reconciliation**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Anomaly tests**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Preserve/edit**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Parse-back/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Formula pattern clustering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency graph**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Outlier rules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Unit/sign audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Hidden-sheet review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Formulas preserved unless asked. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Macros quarantined. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Merged cells handled explicitly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Blank vs zero maintained.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: integrity 25, lineage 20, analysis 20, preservation 20, evidence 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `workbook_profile_json.md` ou formato nativo equivalente: materializa **`workbook-profile.json`** e deve ser citado pelo artefato principal.
- `lineage_graphml.md` ou formato nativo equivalente: materializa **`lineage.graphml`** e deve ser citado pelo artefato principal.
- `anomaly_log_csv.md` ou formato nativo equivalente: materializa **`anomaly-log.csv`** e deve ser citado pelo artefato principal.
- `xlsx_with_checks_and_chart.md` ou formato nativo equivalente: materializa **XLSX with checks and chart** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Readable and auditable spreadsheet structure. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Microsoft Spreadsheet Inquire**, Microsoft (official, força: primary). Aplicação: Dependency, inconsistency and workbook analysis. Localizador: https://support.microsoft.com/en-us/office/what-you-can-do-with-spreadsheet-inquire-5444eb12-14a2-4d82-b527-45b9884f98cf. Consulta: 2026-08-24.
3. **Spreadsheet Check and Control**, Patrick O'Beirne (book, força: recognized). Aplicação: Error taxonomy, controls and review evidence. Localizador: Systems Publishing, 2005, ISBN 9781905404001. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Workbook Lineage Audit

## Pergunta de controle

can the workbook be trusted, what drives outputs, and where are errors/anomalies?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **file inventory** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **formula pattern clustering** responde à pergunta sem extrapolar o dado? Se não, selecione **hidden-sheet review.** e declare a troca.
3. Há uma destas exceções: formulas preserved unless asked; macros quarantined; merged cells handled explicitly; blank vs zero maintained.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **can the workbook be trusted, what drives outputs, and where are errors/anomalies?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **File inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Sheet/range map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Types/nulls/duplicates**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Formula lineage**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Named ranges/external links**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Reconciliation**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Anomaly tests**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Preserve/edit**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Parse-back/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Formula pattern clustering**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency graph**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Balance checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Outlier rules**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Unit/sign audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Hidden-sheet review.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Formulas preserved unless asked. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Macros quarantined. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Merged cells handled explicitly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Blank vs zero maintained.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “sheet/range map” cita evidência identificada, aplica “formula pattern clustering”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Workbook Lineage Audit foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `workbook_profile_json.md` ou formato nativo equivalente: materializa **`workbook-profile.json`** e deve ser citado pelo artefato principal.
- `lineage_graphml.md` ou formato nativo equivalente: materializa **`lineage.graphml`** e deve ser citado pelo artefato principal.
- `anomaly_log_csv.md` ou formato nativo equivalente: materializa **`anomaly-log.csv`** e deve ser citado pelo artefato principal.
- `xlsx_with_checks_and_chart.md` ou formato nativo equivalente: materializa **XLSX with checks and chart** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: integrity 25, lineage 20, analysis 20, preservation 20, evidence 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **FAST Standard**, FAST Standard Organisation (standard, força: primary). Aplicação: Readable and auditable spreadsheet structure. Localizador: https://www.fast-standard.org/the-fast-standard/. Consulta: 2026-08-24.
2. **Microsoft Spreadsheet Inquire**, Microsoft (official, força: primary). Aplicação: Dependency, inconsistency and workbook analysis. Localizador: https://support.microsoft.com/en-us/office/what-you-can-do-with-spreadsheet-inquire-5444eb12-14a2-4d82-b527-45b9884f98cf. Consulta: 2026-08-24.
3. **Spreadsheet Check and Control**, Patrick O'Beirne (book, força: recognized). Aplicação: Error taxonomy, controls and review evidence. Localizador: Systems Publishing, 2005, ISBN 9781905404001. Consulta: 2026-08-24.


# Template — Workbook Lineage Audit

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | can the workbook be trusted, what drives outputs, and where are errors/anomalies? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. File inventory

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Sheet/range map

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Types/nulls/duplicates

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Formula lineage

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Named ranges/external links

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Reconciliation

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Anomaly tests

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Preserve/edit

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Parse-back/render qa.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Workbook Lineage Audit

### `workbook-profile.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `lineage.graphml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `anomaly-log.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### XLSX with checks and chart

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

integrity 25, lineage 20, analysis 20, preservation 20, evidence 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `formulas preserved unless asked; macros quarantined; merged cells handled explicitly; blank vs zero maintained.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Spreadsheet Analyst Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "sum(float(r[d['value_field']]) for r in d['rows'])"
}


{
  "version": "3.1.9",
  "skill": "spreadsheet-analyst",
  "required": [
    "rows",
    "value_field",
    "group_field"
  ],
  "outputs": [
    "total",
    "average",
    "group_totals"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Workbook Lineage Audit",
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
        "file_inventory",
        "sheet_range_map",
        "types_nulls_duplicates",
        "formula_lineage",
        "named_ranges_external_links",
        "reconciliation",
        "anomaly_tests",
        "preserve_edit",
        "parse_back_render_qa"
      ],
      "properties": {
        "file_inventory": {
          "type": "string",
          "minLength": 3
        },
        "sheet_range_map": {
          "type": "string",
          "minLength": 3
        },
        "types_nulls_duplicates": {
          "type": "string",
          "minLength": 3
        },
        "formula_lineage": {
          "type": "string",
          "minLength": 3
        },
        "named_ranges_external_links": {
          "type": "string",
          "minLength": 3
        },
        "reconciliation": {
          "type": "string",
          "minLength": 3
        },
        "anomaly_tests": {
          "type": "string",
          "minLength": 3
        },
        "preserve_edit": {
          "type": "string",
          "minLength": 3
        },
        "parse_back_render_qa": {
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
  "value_field": "amount",
  "group_field": "category"
}


{
  "rows": "not-a-list",
  "value_field": "amount",
  "group_field": "category"
}


{
  "rows": [
    {
      "category": "A"
    }
  ],
  "value_field": "amount",
  "group_field": "category"
}


{
  "rows": [
    {
      "category": "A",
      "amount": 100
    },
    {
      "category": "B",
      "amount": 50
    }
  ],
  "value_field": "amount",
  "group_field": "category"
}


{
  "rows": [
    {
      "category": "A",
      "amount": 200
    },
    {
      "category": "C",
      "amount": 75
    }
  ],
  "value_field": "amount",
  "group_field": "category"
}


{
  "rows": [
    {
      "category": "A",
      "amount": 300
    },
    {
      "category": "D",
      "amount": 100
    }
  ],
  "value_field": "amount",
  "group_field": "category"
}


## 34. spreadsheet-analyst — Workbook Lineage Audit

- **Decisão:** can the workbook be trusted, what drives outputs, and where are errors/anomalies?
- **Fluxo:** file inventory → sheet/range map → types/nulls/duplicates → formula lineage → named ranges/external links → reconciliation → anomaly tests → preserve/edit → parse-back/render QA.
- **Técnicas:** formula pattern clustering; dependency graph; balance checks; outlier rules; unit/sign audit; hidden-sheet review.
- **Exceções:** formulas preserved unless asked; macros quarantined; merged cells handled explicitly; blank vs zero maintained.
- **Rubrica:** integrity 25, lineage 20, analysis 20, preservation 20, evidence 15.
- **Recursos:** `workbook-profile.json`, `lineage.graphml`, `anomaly-log.csv`, XLSX with checks and chart.


[
  {
    "type": "standard",
    "title": "FAST Standard",
    "author": "FAST Standard Organisation",
    "url": "https://www.fast-standard.org/the-fast-standard/",
    "strength": "primary",
    "use": "Readable and auditable spreadsheet structure"
  },
  {
    "type": "official",
    "title": "Microsoft Spreadsheet Inquire",
    "author": "Microsoft",
    "url": "https://support.microsoft.com/en-us/office/what-you-can-do-with-spreadsheet-inquire-5444eb12-14a2-4d82-b527-45b9884f98cf",
    "strength": "primary",
    "use": "Dependency, inconsistency and workbook analysis"
  },
  {
    "type": "book",
    "title": "Spreadsheet Check and Control",
    "author": "Patrick O'Beirne",
    "reference": "Systems Publishing, 2005, ISBN 9781905404001",
    "strength": "recognized",
    "use": "Error taxonomy, controls and review evidence"
  }
]"""
import argparse, json, pathlib, sys
slug='spreadsheet-analyst'; required=['rows', 'value_field', 'group_field']; metric='summary'
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
    value=sum(float(r[d['value_field']]) for r in d['rows'])
    result={'total': value, 'average': value/len(d['rows']), 'group_totals': group_totals(d)}
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
