#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: sales-enablement
description: "Executa Behavior-Readiness System para responder: que comportamento de qual papel precisa mudar para mover qual outcome?"
---

# Sales Enablement

## Escopo e gatilhos

Use quando a decisão real for: **que comportamento de qual papel precisa mudar para mover qual outcome?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Behavior-Readiness System**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Behavior-Readiness System

1. **Business outcome**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Role/behavior map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Baseline**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Content/process/tool gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Practice/coaching**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Certification**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Field reinforcement**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Leading/lagging evaluation.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Competency matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Spaced practice**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Roleplay rubric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Manager coaching loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Kirkpatrick 1–4**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Asset usage telemetry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Content is not enablement without behavior. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Certification expires. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Poor process is not solved by training.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: outcome alignment 25, role specificity 20, practice 20, reinforcement 15, measurement 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `competency_matrix_xlsx.md` ou formato nativo equivalente: materializa **`competency-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `certification_rubric_yaml.md` ou formato nativo equivalente: materializa **`certification-rubric.yaml`** e deve ser citado pelo artefato principal.
- `asset_map_csv.md` ou formato nativo equivalente: materializa **`asset-map.csv`** e deve ser citado pelo artefato principal.
- `reinforcement_calendar.md` ou formato nativo equivalente: materializa **reinforcement calendar** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **What is Sales Enablement?**, Sales Enablement Collective (official, força: primary). Aplicação: Capability, content, coaching and measurement charter. Localizador: https://www.salesenablementcollective.com/what-is-sales-enablement/. Consulta: 2026-08-24.
2. **Sales Enablement 3.0**, Roderick Jefferson (book, força: recognized). Aplicação: Role-based readiness and behavior change. Localizador: Kogan Page, 2020, ISBN 9781789664737. Consulta: 2026-08-24.
3. **Kirkpatrick Model**, Kirkpatrick Partners (official, força: primary). Aplicação: Reaction, learning, behavior and results evaluation. Localizador: https://www.kirkpatrickpartners.com/the-kirkpatrick-model/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Behavior-Readiness System

## Pergunta de controle

que comportamento de qual papel precisa mudar para mover qual outcome?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **business outcome** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **competency matrix** responde à pergunta sem extrapolar o dado? Se não, selecione **asset usage telemetry.** e declare a troca.
3. Há uma destas exceções: content is not enablement without behavior; certification expires; poor process is not solved by training.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que comportamento de qual papel precisa mudar para mover qual outcome?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Business outcome**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Role/behavior map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Baseline**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Content/process/tool gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Practice/coaching**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Certification**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Field reinforcement**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Leading/lagging evaluation.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Competency matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Spaced practice**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Roleplay rubric**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Manager coaching loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Kirkpatrick 1–4**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Asset usage telemetry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Content is not enablement without behavior. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Certification expires. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Poor process is not solved by training.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “role/behavior map” cita evidência identificada, aplica “competency matrix”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Behavior-Readiness System foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `competency_matrix_xlsx.md` ou formato nativo equivalente: materializa **`competency-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `certification_rubric_yaml.md` ou formato nativo equivalente: materializa **`certification-rubric.yaml`** e deve ser citado pelo artefato principal.
- `asset_map_csv.md` ou formato nativo equivalente: materializa **`asset-map.csv`** e deve ser citado pelo artefato principal.
- `reinforcement_calendar.md` ou formato nativo equivalente: materializa **reinforcement calendar** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: outcome alignment 25, role specificity 20, practice 20, reinforcement 15, measurement 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **What is Sales Enablement?**, Sales Enablement Collective (official, força: primary). Aplicação: Capability, content, coaching and measurement charter. Localizador: https://www.salesenablementcollective.com/what-is-sales-enablement/. Consulta: 2026-08-24.
2. **Sales Enablement 3.0**, Roderick Jefferson (book, força: recognized). Aplicação: Role-based readiness and behavior change. Localizador: Kogan Page, 2020, ISBN 9781789664737. Consulta: 2026-08-24.
3. **Kirkpatrick Model**, Kirkpatrick Partners (official, força: primary). Aplicação: Reaction, learning, behavior and results evaluation. Localizador: https://www.kirkpatrickpartners.com/the-kirkpatrick-model/. Consulta: 2026-08-24.


# Template — Behavior-Readiness System

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | que comportamento de qual papel precisa mudar para mover qual outcome? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Business outcome

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Role/behavior map

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Baseline

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Content/process/tool gaps

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Practice/coaching

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Certification

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Field reinforcement

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Leading/lagging evaluation.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Behavior-Readiness System

### `competency-matrix.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `certification-rubric.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `asset-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### reinforcement calendar

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

outcome alignment 25, role specificity 20, practice 20, reinforcement 15, measurement 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `content is not enablement without behavior; certification expires; poor process is not solved by training.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "requires_proof": [
    "roi",
    "benchmark",
    "customer_result"
  ]
}


{
  "stages": [
    "discovery",
    "evaluation",
    "validation",
    "negotiation"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Behavior-Readiness System",
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
        "business_outcome",
        "role_behavior_map",
        "baseline",
        "content_process_tool_gaps",
        "practice_coaching",
        "certification",
        "field_reinforcement",
        "leading_lagging_evaluation"
      ],
      "properties": {
        "business_outcome": {
          "type": "string",
          "minLength": 3
        },
        "role_behavior_map": {
          "type": "string",
          "minLength": 3
        },
        "baseline": {
          "type": "string",
          "minLength": 3
        },
        "content_process_tool_gaps": {
          "type": "string",
          "minLength": 3
        },
        "practice_coaching": {
          "type": "string",
          "minLength": 3
        },
        "certification": {
          "type": "string",
          "minLength": 3
        },
        "field_reinforcement": {
          "type": "string",
          "minLength": 3
        },
        "leading_lagging_evaluation": {
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
    "behavior": "sales-enablement:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "sales-enablement:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "sales-enablement:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "materials required"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "invalid sales stage"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "stage coverage incomplete"
  }
]


{
  "materials": []
}


{
  "materials": [
    {
      "stage": "bad",
      "title": "Discovery",
      "claims": []
    },
    {
      "stage": "evaluation",
      "title": "Evaluation",
      "claims": []
    },
    {
      "stage": "validation",
      "title": "Validation",
      "claims": []
    },
    {
      "stage": "negotiation",
      "title": "Negotiation",
      "claims": []
    }
  ]
}


{
  "materials": [
    {
      "stage": "discovery",
      "title": "Só um",
      "claims": []
    }
  ]
}


{
  "materials": [
    {
      "stage": "discovery",
      "title": "Discovery",
      "claims": []
    },
    {
      "stage": "evaluation",
      "title": "Evaluation",
      "claims": []
    },
    {
      "stage": "validation",
      "title": "Validation",
      "claims": []
    },
    {
      "stage": "negotiation",
      "title": "Negotiation",
      "claims": []
    }
  ]
}


{
  "materials": [
    {
      "stage": "discovery",
      "title": "Mapa de descoberta",
      "claims": []
    },
    {
      "stage": "evaluation",
      "title": "Evaluation",
      "claims": []
    },
    {
      "stage": "validation",
      "title": "Validation",
      "claims": []
    },
    {
      "stage": "negotiation",
      "title": "Negotiation",
      "claims": []
    }
  ]
}


{
  "materials": [
    {
      "stage": "discovery",
      "title": "Discovery",
      "claims": []
    },
    {
      "stage": "evaluation",
      "title": "Evaluation",
      "claims": []
    },
    {
      "stage": "validation",
      "title": "Validation",
      "claims": [
        {
          "type": "roi",
          "source": "https://example.org/proof"
        }
      ]
    },
    {
      "stage": "negotiation",
      "title": "Negotiation",
      "claims": []
    }
  ]
}


## 30. sales-enablement — Behavior-Readiness System

- **Decisão:** que comportamento de qual papel precisa mudar para mover qual outcome?
- **Fluxo:** business outcome → role/behavior map → baseline → content/process/tool gaps → practice/coaching → certification → field reinforcement → leading/lagging evaluation.
- **Técnicas:** competency matrix; spaced practice; roleplay rubric; manager coaching loop; Kirkpatrick 1–4; asset usage telemetry.
- **Exceções:** content is not enablement without behavior; certification expires; poor process is not solved by training.
- **Rubrica:** outcome alignment 25, role specificity 20, practice 20, reinforcement 15, measurement 20.
- **Recursos:** `competency-matrix.xlsx`, `certification-rubric.yaml`, `asset-map.csv`, reinforcement calendar.


[
  {
    "type": "official",
    "title": "What is Sales Enablement?",
    "author": "Sales Enablement Collective",
    "url": "https://www.salesenablementcollective.com/what-is-sales-enablement/",
    "strength": "primary",
    "use": "Capability, content, coaching and measurement charter"
  },
  {
    "type": "book",
    "title": "Sales Enablement 3.0",
    "author": "Roderick Jefferson",
    "reference": "Kogan Page, 2020, ISBN 9781789664737",
    "strength": "recognized",
    "use": "Role-based readiness and behavior change"
  },
  {
    "type": "official",
    "title": "Kirkpatrick Model",
    "author": "Kirkpatrick Partners",
    "url": "https://www.kirkpatrickpartners.com/the-kirkpatrick-model/",
    "strength": "primary",
    "use": "Reaction, learning, behavior and results evaluation"
  }
]"""
import json,sys
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
def fail(msg): raise ValueError(msg)
def req(obj,key):
    v=obj.get(key) if isinstance(obj,dict) else None
    if v is None or (isinstance(v,str) and not v.strip()): fail("missing "+key)
    return v
def build(data):
    assets={p.stem:json.loads(p.read_text()) for p in (BASE/"assets").glob("*.json")}
    materials=data.get('materials');
    if not isinstance(materials,list) or not materials: fail('materials required')
    coverage={s:0 for s in assets['stages']['stages']}; claims=[]
    for m in materials:
        stage=req(m,'stage')
        if stage not in coverage: fail('invalid sales stage')
        req(m,'title'); coverage[stage]+=1
        for claim in m.get('claims',[]):
            if claim.get('type') in assets['claims-policy']['requires_proof'] and not claim.get('source'): fail('claim lacks proof')
            claims.append(claim)
    if any(v==0 for v in coverage.values()): fail('stage coverage incomplete')
    return {'coverage':coverage,'materials':materials,'validated_claims':len(claims)}
def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("input_pos",nargs="?"); ap.add_argument("--input",dest="input_opt"); ap.add_argument("-o","--output")
    a=ap.parse_args(); source=a.input_opt or a.input_pos
    try:
        data=json.loads(Path(source).read_text()) if source else json.load(sys.stdin)
        rendered=json.dumps(build(data),ensure_ascii=False,indent=2)+"\n"
        Path(a.output).write_text(rendered) if a.output else print(rendered,end="")
    except Exception as e:
        print(json.dumps({"error":str(e)}),file=sys.stderr); raise SystemExit(2)
if __name__=="__main__": main()
