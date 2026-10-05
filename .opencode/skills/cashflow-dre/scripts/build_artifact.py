#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: cashflow-dre
description: "Executa Accrual-to-Cash Bridge para responder: resultado, liquidez e capital de giro contam a mesma história?"
---

# Cashflow Dre

## Escopo e gatilhos

Use quando a decisão real for: **resultado, liquidez e capital de giro contam a mesma história?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Accrual-to-Cash Bridge**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Accrual-to-Cash Bridge

1. **Importar plano/razão/extratos**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Mapear contas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Montar dre**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Classificar caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Bridge lucro**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Aging/working capital**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cenários e reconciliações.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Método direto/indireto**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Análise vertical/horizontal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ebitda-to-cash**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dso/dio/dpo**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Checks de abertura/fechamento.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Transferências internas eliminadas. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Impostos/juros classificados por política. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado incompleto conserva `unknown`, nunca zero silencioso.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: reconciliação 30, classificação 20, rastreabilidade 20, insight 15, controles 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `chart_of_accounts_map_csv.md` ou formato nativo equivalente: materializa **`chart-of-accounts-map.csv`** e deve ser citado pelo artefato principal.
- `cashflow_xlsx.md` ou formato nativo equivalente: materializa **`cashflow.xlsx`** e deve ser citado pelo artefato principal.
- `reconciliation_checks_yaml.md` ou formato nativo equivalente: materializa **`reconciliation-checks.yaml`** e deve ser citado pelo artefato principal.
- `coment_rio_de_varia_es.md` ou formato nativo equivalente: materializa **comentário de variações** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **CPC 03 (R2) Demonstração dos Fluxos de Caixa**, CPC (official, força: primary). Aplicação: Cash-flow classification and reconciliation. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=34. Consulta: 2026-08-24.
2. **CPC 26 (R1) Apresentação das Demonstrações Contábeis**, CPC (official, força: primary). Aplicação: Income-statement structure and comparatives. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=57. Consulta: 2026-08-24.
3. **IAS 7 Statement of Cash Flows**, IFRS Foundation (standard, força: primary). Aplicação: Operating, investing and financing cash taxonomy. Localizador: https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Accrual-to-Cash Bridge

## Pergunta de controle

resultado, liquidez e capital de giro contam a mesma história?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **importar plano/razão/extratos** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **método direto/indireto** responde à pergunta sem extrapolar o dado? Se não, selecione **checks de abertura/fechamento.** e declare a troca.
3. Há uma destas exceções: transferências internas eliminadas; impostos/juros classificados por política; dado incompleto conserva `unknown`, nunca zero silencioso.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **resultado, liquidez e capital de giro contam a mesma história?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Importar plano/razão/extratos**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Mapear contas**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Montar dre**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Classificar caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Bridge lucro**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Caixa**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Aging/working capital**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Cenários e reconciliações.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Método direto/indireto**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Análise vertical/horizontal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ebitda-to-cash**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dso/dio/dpo**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Checks de abertura/fechamento.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Transferências internas eliminadas. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Impostos/juros classificados por política. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dado incompleto conserva `unknown`, nunca zero silencioso.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “mapear contas” cita evidência identificada, aplica “método direto/indireto”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Accrual-to-Cash Bridge foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `chart_of_accounts_map_csv.md` ou formato nativo equivalente: materializa **`chart-of-accounts-map.csv`** e deve ser citado pelo artefato principal.
- `cashflow_xlsx.md` ou formato nativo equivalente: materializa **`cashflow.xlsx`** e deve ser citado pelo artefato principal.
- `reconciliation_checks_yaml.md` ou formato nativo equivalente: materializa **`reconciliation-checks.yaml`** e deve ser citado pelo artefato principal.
- `coment_rio_de_varia_es.md` ou formato nativo equivalente: materializa **comentário de variações** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: reconciliação 30, classificação 20, rastreabilidade 20, insight 15, controles 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **CPC 03 (R2) Demonstração dos Fluxos de Caixa**, CPC (official, força: primary). Aplicação: Cash-flow classification and reconciliation. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=34. Consulta: 2026-08-24.
2. **CPC 26 (R1) Apresentação das Demonstrações Contábeis**, CPC (official, força: primary). Aplicação: Income-statement structure and comparatives. Localizador: https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=57. Consulta: 2026-08-24.
3. **IAS 7 Statement of Cash Flows**, IFRS Foundation (standard, força: primary). Aplicação: Operating, investing and financing cash taxonomy. Localizador: https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/. Consulta: 2026-08-24.


# Template — Accrual-to-Cash Bridge

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | resultado, liquidez e capital de giro contam a mesma história? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Importar plano/razão/extratos

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Mapear contas

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Montar dre

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Classificar caixa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Bridge lucro

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Caixa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Aging/working capital

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Cenários e reconciliações.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Accrual-to-Cash Bridge

### `chart-of-accounts-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `cashflow.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `reconciliation-checks.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### comentário de variações

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

reconciliação 30, classificação 20, rastreabilidade 20, insight 15, controles 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `transferências internas eliminadas; impostos/juros classificados por política; dado incompleto conserva `unknown`, nunca zero silencioso.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "name": "Cashflow Dre Evidence Model",
  "threshold": 60,
  "principles": [
    "trace every result to supplied inputs",
    "fail closed on missing or malformed evidence",
    "separate computed facts from assumptions"
  ],
  "formula": "d['opening_cash']+d['cash_receipts']-d['cash_payments']"
}


{
  "version": "3.1.9",
  "skill": "cashflow-dre",
  "required": [
    "opening_cash",
    "cash_receipts",
    "cash_payments",
    "revenue",
    "cogs",
    "opex"
  ],
  "outputs": [
    "closing_cash",
    "gross_profit",
    "operating_profit"
  ],
  "additionalProperties": true
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Accrual-to-Cash Bridge",
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
        "importar_plano_raz_o_extratos",
        "mapear_contas",
        "montar_dre",
        "classificar_caixa",
        "bridge_lucro",
        "caixa",
        "aging_working_capital",
        "cen_rios_e_reconcilia_es"
      ],
      "properties": {
        "importar_plano_raz_o_extratos": {
          "type": "string",
          "minLength": 3
        },
        "mapear_contas": {
          "type": "string",
          "minLength": 3
        },
        "montar_dre": {
          "type": "string",
          "minLength": 3
        },
        "classificar_caixa": {
          "type": "string",
          "minLength": 3
        },
        "bridge_lucro": {
          "type": "string",
          "minLength": 3
        },
        "caixa": {
          "type": "string",
          "minLength": 3
        },
        "aging_working_capital": {
          "type": "string",
          "minLength": 3
        },
        "cen_rios_e_reconcilia_es": {
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
  "cash_receipts": 10,
  "cash_payments": 10,
  "revenue": 10,
  "cogs": 10,
  "opex": 10
}


{
  "opening_cash": "not-a-number",
  "cash_receipts": 10,
  "cash_payments": 10,
  "revenue": 10,
  "cogs": 10,
  "opex": 10
}


{
  "opening_cash": -1,
  "cash_receipts": 10,
  "cash_payments": 10,
  "revenue": 10,
  "cogs": 10,
  "opex": 10
}


{
  "opening_cash": 10,
  "cash_receipts": 11,
  "cash_payments": 10,
  "revenue": 10,
  "cogs": 10,
  "opex": 10
}


{
  "opening_cash": 20,
  "cash_receipts": 12,
  "cash_payments": 10,
  "revenue": 10,
  "cogs": 10,
  "opex": 10
}


{
  "opening_cash": 30,
  "cash_receipts": 13,
  "cash_payments": 10,
  "revenue": 10,
  "cogs": 10,
  "opex": 10
}


## 6. cashflow-dre — Accrual-to-Cash Bridge

- **Decisão:** resultado, liquidez e capital de giro contam a mesma história?
- **Fluxo:** importar plano/razão/extratos → mapear contas → montar DRE → classificar caixa → bridge lucro→caixa → aging/working capital → cenários e reconciliações.
- **Técnicas:** método direto/indireto; análise vertical/horizontal; EBITDA-to-cash; DSO/DIO/DPO; checks de abertura/fechamento.
- **Exceções:** transferências internas eliminadas; impostos/juros classificados por política; dado incompleto conserva `unknown`, nunca zero silencioso.
- **Rubrica:** reconciliação 30, classificação 20, rastreabilidade 20, insight 15, controles 15.
- **Recursos:** `chart-of-accounts-map.csv`, `cashflow.xlsx`, `reconciliation-checks.yaml`, comentário de variações.


[
  {
    "type": "official",
    "title": "CPC 03 (R2) Demonstração dos Fluxos de Caixa",
    "author": "CPC",
    "url": "https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=34",
    "strength": "primary",
    "use": "Cash-flow classification and reconciliation"
  },
  {
    "type": "official",
    "title": "CPC 26 (R1) Apresentação das Demonstrações Contábeis",
    "author": "CPC",
    "url": "https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=57",
    "strength": "primary",
    "use": "Income-statement structure and comparatives"
  },
  {
    "type": "standard",
    "title": "IAS 7 Statement of Cash Flows",
    "author": "IFRS Foundation",
    "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/",
    "strength": "primary",
    "use": "Operating, investing and financing cash taxonomy"
  }
]"""
import argparse, json, pathlib, sys
slug='cashflow-dre'; required=['opening_cash', 'cash_receipts', 'cash_payments', 'revenue', 'cogs', 'opex']; metric='net_cash'
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
    value=d['opening_cash']+d['cash_receipts']-d['cash_payments']
    result={'closing_cash': value, 'gross_profit': d['revenue']-d['cogs'], 'operating_profit': d['revenue']-d['cogs']-d['opex']}
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
