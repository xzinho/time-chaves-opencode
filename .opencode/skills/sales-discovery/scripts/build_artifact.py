#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: sales-discovery
description: "Executa Behavior-to-Gap Conversation para responder: existe problema material, processo de decisão e próximo passo mútuo?"
---

# Sales Discovery

## Escopo e gatilhos

Use quando a decisão real for: **existe problema material, processo de decisão e próximo passo mútuo?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Behavior-to-Gap Conversation**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Behavior-to-Gap Conversation

1. **Account hypothesis**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Agenda/permission**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Current behavior**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Problem/impact**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Desired state**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Past attempts**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Stakeholders/process**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Priority/timing**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Summarize/confirm**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Mutual next step.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Spin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mom test behavior questions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gap quantification**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Silence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mirroring**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence recap.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Early exploratory call avoids interrogation. Marque a condição no artefato e acione o gate indicado antes do handoff.
- No pain/priority exits cleanly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Procurement details follow value discovery.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: evidence quality 25, depth 20, listening 20, qualification 15, mutual action 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `discovery_plan_md.md` ou formato nativo equivalente: materializa **`discovery-plan.md`** e deve ser citado pelo artefato principal.
- `question_bank_yaml.md` ou formato nativo equivalente: materializa **`question-bank.yaml`** e deve ser citado pelo artefato principal.
- `gap_map_csv.md` ou formato nativo equivalente: materializa **`gap-map.csv`** e deve ser citado pelo artefato principal.
- `call_evidence_next_step_note.md` ou formato nativo equivalente: materializa **call evidence/next-step note** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Situation-problem-implication-need payoff sequencing. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Mom Test**, Rob Fitzpatrick (book, força: canonical). Aplicação: Behavioral evidence and avoidance of leading questions. Localizador: CreateSpace, 2013, ISBN 9781492180746. Consulta: 2026-08-24.
3. **Sales Rep Training**, Salesforce Trailhead (official, força: primary). Aplicação: Observable discovery preparation, questioning and confirmation. Localizador: https://trailhead.salesforce.com/content/learn/modules/sales-rep-training. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Behavior-to-Gap Conversation

## Pergunta de controle

existe problema material, processo de decisão e próximo passo mútuo?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **account hypothesis** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **SPIN** responde à pergunta sem extrapolar o dado? Se não, selecione **evidence recap.** e declare a troca.
3. Há uma destas exceções: early exploratory call avoids interrogation; no pain/priority exits cleanly; procurement details follow value discovery.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **existe problema material, processo de decisão e próximo passo mútuo?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Account hypothesis**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Agenda/permission**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Current behavior**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Problem/impact**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Desired state**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Past attempts**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Stakeholders/process**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Priority/timing**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Summarize/confirm**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Mutual next step.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Spin**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mom test behavior questions**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Gap quantification**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Silence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Mirroring**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence recap.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Early exploratory call avoids interrogation. Marque a condição no artefato e acione o gate indicado antes do handoff.
- No pain/priority exits cleanly. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Procurement details follow value discovery.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “agenda/permission” cita evidência identificada, aplica “SPIN”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Behavior-to-Gap Conversation foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `discovery_plan_md.md` ou formato nativo equivalente: materializa **`discovery-plan.md`** e deve ser citado pelo artefato principal.
- `question_bank_yaml.md` ou formato nativo equivalente: materializa **`question-bank.yaml`** e deve ser citado pelo artefato principal.
- `gap_map_csv.md` ou formato nativo equivalente: materializa **`gap-map.csv`** e deve ser citado pelo artefato principal.
- `call_evidence_next_step_note.md` ou formato nativo equivalente: materializa **call evidence/next-step note** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: evidence quality 25, depth 20, listening 20, qualification 15, mutual action 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **SPIN Selling**, Neil Rackham (book, força: canonical). Aplicação: Situation-problem-implication-need payoff sequencing. Localizador: McGraw-Hill, 1988, ISBN 9780070511132. Consulta: 2026-08-24.
2. **The Mom Test**, Rob Fitzpatrick (book, força: canonical). Aplicação: Behavioral evidence and avoidance of leading questions. Localizador: CreateSpace, 2013, ISBN 9781492180746. Consulta: 2026-08-24.
3. **Sales Rep Training**, Salesforce Trailhead (official, força: primary). Aplicação: Observable discovery preparation, questioning and confirmation. Localizador: https://trailhead.salesforce.com/content/learn/modules/sales-rep-training. Consulta: 2026-08-24.


# Template — Behavior-to-Gap Conversation

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | existe problema material, processo de decisão e próximo passo mútuo? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Account hypothesis

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Agenda/permission

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Current behavior

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Problem/impact

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Desired state

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Past attempts

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Stakeholders/process

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Priority/timing

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Summarize/confirm

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 10. Mutual next step.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Behavior-to-Gap Conversation

### `discovery-plan.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `question-bank.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `gap-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### call evidence/next-step note

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

evidence quality 25, depth 20, listening 20, qualification 15, mutual action 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `early exploratory call avoids interrogation; no pain/priority exits cleanly; procurement details follow value discovery.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "weights": {
    "impact": 3,
    "urgency": 2,
    "authority": 2,
    "fit": 3
  }
}


{
  "themes": [
    "situation",
    "impact",
    "urgency",
    "authority",
    "success"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Behavior-to-Gap Conversation",
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
        "account_hypothesis",
        "agenda_permission",
        "current_behavior",
        "problem_impact",
        "desired_state",
        "past_attempts",
        "stakeholders_process",
        "priority_timing",
        "summarize_confirm",
        "mutual_next_step"
      ],
      "properties": {
        "account_hypothesis": {
          "type": "string",
          "minLength": 3
        },
        "agenda_permission": {
          "type": "string",
          "minLength": 3
        },
        "current_behavior": {
          "type": "string",
          "minLength": 3
        },
        "problem_impact": {
          "type": "string",
          "minLength": 3
        },
        "desired_state": {
          "type": "string",
          "minLength": 3
        },
        "past_attempts": {
          "type": "string",
          "minLength": 3
        },
        "stakeholders_process": {
          "type": "string",
          "minLength": 3
        },
        "priority_timing": {
          "type": "string",
          "minLength": 3
        },
        "summarize_confirm": {
          "type": "string",
          "minLength": 3
        },
        "mutual_next_step": {
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
    "behavior": "sales-discovery:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "sales-discovery:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "sales-discovery:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "answers object required"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "discovery themes missing"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "superficial discovery answer"
  }
]


{
  "signals": {
    "impact": true,
    "urgency": true,
    "authority": true,
    "fit": true
  }
}


{
  "answers": {
    "situation": "Evidência verificável com fonte primária e contexto suficiente",
    "urgency": "Evidência verificável com fonte primária e contexto suficiente",
    "authority": "Evidência verificável com fonte primária e contexto suficiente",
    "success": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "signals": {
    "impact": true,
    "urgency": true,
    "authority": true,
    "fit": true
  }
}


{
  "answers": {
    "situation": "Evidência verificável com fonte primária e contexto suficiente",
    "impact": "x",
    "urgency": "Evidência verificável com fonte primária e contexto suficiente",
    "authority": "Evidência verificável com fonte primária e contexto suficiente",
    "success": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "signals": {
    "impact": true,
    "urgency": true,
    "authority": true,
    "fit": true
  }
}


{
  "answers": {
    "situation": "Evidência verificável com fonte primária e contexto suficiente",
    "impact": "Evidência verificável com fonte primária e contexto suficiente",
    "urgency": "Evidência verificável com fonte primária e contexto suficiente",
    "authority": "Evidência verificável com fonte primária e contexto suficiente",
    "success": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "signals": {
    "impact": true,
    "urgency": true,
    "authority": true,
    "fit": true
  }
}


{
  "answers": {
    "situation": "Evidência verificável com fonte primária e contexto suficiente",
    "impact": "Evidência verificável com fonte primária e contexto suficiente",
    "urgency": "Evidência verificável com fonte primária e contexto suficiente",
    "authority": "Evidência verificável com fonte primária e contexto suficiente",
    "success": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "signals": {
    "impact": true,
    "urgency": true,
    "authority": false,
    "fit": true
  }
}


{
  "answers": {
    "situation": "Evidência verificável com fonte primária e contexto suficiente",
    "impact": "Evidência verificável com fonte primária e contexto suficiente",
    "urgency": "Evidência verificável com fonte primária e contexto suficiente",
    "authority": "Evidência verificável com fonte primária e contexto suficiente",
    "success": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "signals": {
    "impact": true,
    "urgency": true,
    "authority": true,
    "fit": false
  }
}


## 29. sales-discovery — Behavior-to-Gap Conversation

- **Decisão:** existe problema material, processo de decisão e próximo passo mútuo?
- **Fluxo:** account hypothesis → agenda/permission → current behavior → problem/impact → desired state → past attempts → stakeholders/process → priority/timing → summarize/confirm → mutual next step.
- **Técnicas:** SPIN; Mom Test behavior questions; gap quantification; silence; mirroring; evidence recap.
- **Exceções:** early exploratory call avoids interrogation; no pain/priority exits cleanly; procurement details follow value discovery.
- **Rubrica:** evidence quality 25, depth 20, listening 20, qualification 15, mutual action 20.
- **Recursos:** `discovery-plan.md`, `question-bank.yaml`, `gap-map.csv`, call evidence/next-step note.


[
  {
    "type": "book",
    "title": "SPIN Selling",
    "author": "Neil Rackham",
    "reference": "McGraw-Hill, 1988, ISBN 9780070511132",
    "strength": "canonical",
    "use": "Situation-problem-implication-need payoff sequencing"
  },
  {
    "type": "book",
    "title": "The Mom Test",
    "author": "Rob Fitzpatrick",
    "reference": "CreateSpace, 2013, ISBN 9781492180746",
    "strength": "canonical",
    "use": "Behavioral evidence and avoidance of leading questions"
  },
  {
    "type": "official",
    "title": "Sales Rep Training",
    "author": "Salesforce Trailhead",
    "url": "https://trailhead.salesforce.com/content/learn/modules/sales-rep-training",
    "strength": "primary",
    "use": "Observable discovery preparation, questioning and confirmation"
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
    answers=data.get('answers');
    if not isinstance(answers,dict): fail('answers object required')
    missing=set(assets['questions']['themes'])-set(answers)
    if missing: fail('discovery themes missing')
    if any(len(str(answers[x]).strip())<5 for x in assets['questions']['themes']): fail('superficial discovery answer')
    signals=data.get('signals',{}); weights=assets['qualification']['weights']
    if set(weights)-set(signals): fail('qualification signals missing')
    score=sum(weights[k]*int(bool(signals[k])) for k in weights)
    return {'themes':answers,'qualification_score':score,'max_score':sum(weights.values()),'next_step':'advance' if score>=7 else 'nurture'}
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
