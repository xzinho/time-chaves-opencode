#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: executive-briefing
description: "Executa Decision-First Brief para responder: o que o executivo deve decidir, por quê agora e com qual consequência?"
---

# Executive Briefing

## Escopo e gatilhos

Use quando a decisão real for: **o que o executivo deve decidir, por quê agora e com qual consequência?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Decision-First Brief**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Decision-First Brief

1. **Decision statement**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **One-line answer**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Material facts**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Options/tradeoffs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Recommendation**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Risks/unknowns**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Explicit ask**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Owners/dates.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Pyramid logic**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Bluf**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fact/inference/assumption tags**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Option table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Red-team question.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Sem decisão vira status brief. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crise prioriza facts/time/owner. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Incerteza não é escondida por prosa.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: decisão 25, síntese 20, evidência 20, tradeoffs 15, ação 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `decision_brief_md.md` ou formato nativo equivalente: materializa **`decision-brief.md`** e deve ser citado pelo artefato principal.
- `fact_assumption_ledger_csv.md` ou formato nativo equivalente: materializa **`fact-assumption-ledger.csv`** e deve ser citado pelo artefato principal.
- `one_page_pdf.md` ou formato nativo equivalente: materializa **one-page PDF** e deve ser citado pelo artefato principal.
- `verbal_60_second_variant.md` ou formato nativo equivalente: materializa **verbal 60-second variant** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Pyramid Principle**, Barbara Minto (book, força: canonical). Aplicação: Answer-first logic and mutually exclusive support. Localizador: Financial Times Prentice Hall, 2009, ISBN 9780273710516. Consulta: 2026-08-24.
2. **Writing for GOV.UK**, UK Government Digital Service (official, força: primary). Aplicação: Concise audience-centered executive language. Localizador: https://www.gov.uk/guidance/content-design/writing-for-gov-uk. Consulta: 2026-08-24.
3. **Smart Brevity**, Jim VandeHei, Mike Allen, Roy Schwartz (book, força: recognized). Aplicação: Why-it-matters and scannable action architecture. Localizador: Workman, 2022, ISBN 9781523516971. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Decision-First Brief

## Pergunta de controle

o que o executivo deve decidir, por quê agora e com qual consequência?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **decision statement** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **pyramid logic** responde à pergunta sem extrapolar o dado? Se não, selecione **red-team question.** e declare a troca.
3. Há uma destas exceções: sem decisão vira status brief; crise prioriza facts/time/owner; incerteza não é escondida por prosa.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **o que o executivo deve decidir, por quê agora e com qual consequência?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Decision statement**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **One-line answer**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Material facts**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Options/tradeoffs**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Recommendation**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Risks/unknowns**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Explicit ask**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Owners/dates.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Pyramid logic**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Bluf**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Fact/inference/assumption tags**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Option table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Red-team question.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Sem decisão vira status brief. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crise prioriza facts/time/owner. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Incerteza não é escondida por prosa.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “one-line answer” cita evidência identificada, aplica “pyramid logic”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Decision-First Brief foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `decision_brief_md.md` ou formato nativo equivalente: materializa **`decision-brief.md`** e deve ser citado pelo artefato principal.
- `fact_assumption_ledger_csv.md` ou formato nativo equivalente: materializa **`fact-assumption-ledger.csv`** e deve ser citado pelo artefato principal.
- `one_page_pdf.md` ou formato nativo equivalente: materializa **one-page PDF** e deve ser citado pelo artefato principal.
- `verbal_60_second_variant.md` ou formato nativo equivalente: materializa **verbal 60-second variant** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: decisão 25, síntese 20, evidência 20, tradeoffs 15, ação 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Pyramid Principle**, Barbara Minto (book, força: canonical). Aplicação: Answer-first logic and mutually exclusive support. Localizador: Financial Times Prentice Hall, 2009, ISBN 9780273710516. Consulta: 2026-08-24.
2. **Writing for GOV.UK**, UK Government Digital Service (official, força: primary). Aplicação: Concise audience-centered executive language. Localizador: https://www.gov.uk/guidance/content-design/writing-for-gov-uk. Consulta: 2026-08-24.
3. **Smart Brevity**, Jim VandeHei, Mike Allen, Roy Schwartz (book, força: recognized). Aplicação: Why-it-matters and scannable action architecture. Localizador: Workman, 2022, ISBN 9781523516971. Consulta: 2026-08-24.


# Template — Decision-First Brief

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | o que o executivo deve decidir, por quê agora e com qual consequência? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Decision statement

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. One-line answer

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Material facts

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Options/tradeoffs

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Recommendation

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Risks/unknowns

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Explicit ask

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Owners/dates.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Decision-First Brief

### `decision-brief.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `fact-assumption-ledger.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### one-page PDF

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### verbal 60-second variant

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

decisão 25, síntese 20, evidência 20, tradeoffs 15, ação 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `sem decisão vira status brief; crise prioriza facts/time/owner; incerteza não é escondida por prosa.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "required": [
    "owner",
    "deadline",
    "metric"
  ]
}


{
  "order": [
    "decision",
    "why_now",
    "evidence",
    "options",
    "recommendation",
    "next_step"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Decision-First Brief",
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
        "decision_statement",
        "one_line_answer",
        "material_facts",
        "options_tradeoffs",
        "recommendation",
        "risks_unknowns",
        "explicit_ask",
        "owners_dates"
      ],
      "properties": {
        "decision_statement": {
          "type": "string",
          "minLength": 3
        },
        "one_line_answer": {
          "type": "string",
          "minLength": 3
        },
        "material_facts": {
          "type": "string",
          "minLength": 3
        },
        "options_tradeoffs": {
          "type": "string",
          "minLength": 3
        },
        "recommendation": {
          "type": "string",
          "minLength": 3
        },
        "risks_unknowns": {
          "type": "string",
          "minLength": 3
        },
        "explicit_ask": {
          "type": "string",
          "minLength": 3
        },
        "owners_dates": {
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
    "behavior": "executive-briefing:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "executive-briefing:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "executive-briefing:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "empty executive section decision"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "incomplete action contract"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "options need tradeoffs"
  }
]


{
  "brief": {},
  "action": {
    "owner": "Ana",
    "deadline": "2026-09-01",
    "metric": "Receita"
  },
  "options": [
    {
      "name": "A",
      "tradeoff": "velocidade"
    },
    {
      "name": "B",
      "tradeoff": "custo"
    }
  ]
}


{
  "brief": {
    "decision": "Evidência verificável com fonte primária e contexto suficiente",
    "why_now": "Evidência verificável com fonte primária e contexto suficiente",
    "evidence": "Evidência verificável com fonte primária e contexto suficiente",
    "options": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendation": "Evidência verificável com fonte primária e contexto suficiente",
    "next_step": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "action": {},
  "options": [
    {
      "name": "A",
      "tradeoff": "velocidade"
    },
    {
      "name": "B",
      "tradeoff": "custo"
    }
  ]
}


{
  "brief": {
    "decision": "Evidência verificável com fonte primária e contexto suficiente",
    "why_now": "Evidência verificável com fonte primária e contexto suficiente",
    "evidence": "Evidência verificável com fonte primária e contexto suficiente",
    "options": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendation": "Evidência verificável com fonte primária e contexto suficiente",
    "next_step": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "action": {
    "owner": "Ana",
    "deadline": "2026-09-01",
    "metric": "Receita"
  },
  "options": []
}


{
  "brief": {
    "decision": "Evidência verificável com fonte primária e contexto suficiente",
    "why_now": "Evidência verificável com fonte primária e contexto suficiente",
    "evidence": "Evidência verificável com fonte primária e contexto suficiente",
    "options": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendation": "Evidência verificável com fonte primária e contexto suficiente",
    "next_step": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "action": {
    "owner": "Ana",
    "deadline": "2026-09-01",
    "metric": "Receita"
  },
  "options": [
    {
      "name": "A",
      "tradeoff": "velocidade"
    },
    {
      "name": "B",
      "tradeoff": "custo"
    }
  ]
}


{
  "brief": {
    "decision": "Evidência verificável com fonte primária e contexto suficiente",
    "why_now": "Evidência verificável com fonte primária e contexto suficiente",
    "evidence": "Evidência verificável com fonte primária e contexto suficiente",
    "options": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendation": "Evidência verificável com fonte primária e contexto suficiente",
    "next_step": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "action": {
    "owner": "Bruno",
    "deadline": "2026-09-01",
    "metric": "Receita"
  },
  "options": [
    {
      "name": "A",
      "tradeoff": "velocidade"
    },
    {
      "name": "B",
      "tradeoff": "custo"
    }
  ]
}


{
  "brief": {
    "decision": "Evidência verificável com fonte primária e contexto suficiente",
    "why_now": "Evidência verificável com fonte primária e contexto suficiente",
    "evidence": "Evidência verificável com fonte primária e contexto suficiente",
    "options": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendation": "Evidência verificável com fonte primária e contexto suficiente",
    "next_step": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "action": {
    "owner": "Ana",
    "deadline": "2026-09-01",
    "metric": "Receita"
  },
  "options": [
    {
      "name": "A",
      "tradeoff": "risco operacional"
    },
    {
      "name": "B",
      "tradeoff": "custo"
    }
  ]
}


## 15. executive-briefing — Decision-First Brief

- **Decisão:** o que o executivo deve decidir, por quê agora e com qual consequência?
- **Fluxo:** decision statement → one-line answer → material facts → options/tradeoffs → recommendation → risks/unknowns → explicit ask → owners/dates.
- **Técnicas:** pyramid logic; BLUF; fact/inference/assumption tags; option table; red-team question.
- **Exceções:** sem decisão vira status brief; crise prioriza facts/time/owner; incerteza não é escondida por prosa.
- **Rubrica:** decisão 25, síntese 20, evidência 20, tradeoffs 15, ação 20.
- **Recursos:** `decision-brief.md`, `fact-assumption-ledger.csv`, one-page PDF, verbal 60-second variant.


[
  {
    "type": "book",
    "title": "The Pyramid Principle",
    "author": "Barbara Minto",
    "reference": "Financial Times Prentice Hall, 2009, ISBN 9780273710516",
    "strength": "canonical",
    "use": "Answer-first logic and mutually exclusive support"
  },
  {
    "type": "official",
    "title": "Writing for GOV.UK",
    "author": "UK Government Digital Service",
    "url": "https://www.gov.uk/guidance/content-design/writing-for-gov-uk",
    "strength": "primary",
    "use": "Concise audience-centered executive language"
  },
  {
    "type": "book",
    "title": "Smart Brevity",
    "author": "Jim VandeHei, Mike Allen, Roy Schwartz",
    "reference": "Workman, 2022, ISBN 9781523516971",
    "strength": "recognized",
    "use": "Why-it-matters and scannable action architecture"
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
    brief=data.get('brief')
    if not isinstance(brief,dict): fail('brief object required')
    for key in assets['pyramid']['order']:
        if not str(brief.get(key,'')).strip(): fail('empty executive section '+key)
    action=data.get('action',{})
    for key in assets['decision']['required']:
        if not str(action.get(key,'')).strip(): fail('incomplete action contract')
    options=data.get('options',[])
    if len(options)<2 or any('tradeoff' not in o for o in options): fail('options need tradeoffs')
    return {'headline':brief['decision'],'narrative':[brief[k] for k in assets['pyramid']['order']],'options':options,'action':action}
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
