#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: product-marketing-context
description: "Executa Positioning Evidence File para responder: para quem o produto é uniquely valuable, versus what, in what context?"
---

# Product Marketing Context

## Escopo e gatilhos

Use quando a decisão real for: **para quem o produto é uniquely valuable, versus what, in what context?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Positioning Evidence File**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Positioning Evidence File

1. **Customer evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Job/circumstance**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Alternatives**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Unique attributes**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Value/proof**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Best-fit segment**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Category/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Message boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Versioned context.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Switching interview**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternative map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Value chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Beachhead criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Aspirational feature excluded. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Multiple segments get separate contexts. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Category creation requires education cost.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: customer evidence 25, differentiation 25, clarity 20, proof 15, usability downstream 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `positioning_canvas_md.md` ou formato nativo equivalente: materializa **`positioning-canvas.md`** e deve ser citado pelo artefato principal.
- `alternative_map_csv.md` ou formato nativo equivalente: materializa **`alternative-map.csv`** e deve ser citado pelo artefato principal.
- `message_boundaries_yaml.md` ou formato nativo equivalente: materializa **`message-boundaries.yaml`** e deve ser citado pelo artefato principal.
- `proof_library.md` ou formato nativo equivalente: materializa **proof library** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Obviously Awesome**, April Dunford (book, força: canonical). Aplicação: Competitive alternatives, differentiated value and category. Localizador: Ambient Press, 2019, ISBN 9781999023003. Consulta: 2026-08-24.
2. **Crossing the Chasm, 3rd ed.**, Geoffrey Moore (book, força: canonical). Aplicação: Beachhead segment and whole-product context. Localizador: HarperBusiness, 2014, ISBN 9780062292988. Consulta: 2026-08-24.
3. **Jobs to Be Done Theory**, Christensen Institute (official, força: primary). Aplicação: Progress, circumstance and switching forces. Localizador: https://www.christenseninstitute.org/theory/jobs-to-be-done/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Positioning Evidence File

## Pergunta de controle

para quem o produto é uniquely valuable, versus what, in what context?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **customer evidence** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **switching interview** responde à pergunta sem extrapolar o dado? Se não, selecione **claim-evidence trace.** e declare a troca.
3. Há uma destas exceções: aspirational feature excluded; multiple segments get separate contexts; category creation requires education cost.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **para quem o produto é uniquely valuable, versus what, in what context?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Customer evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Job/circumstance**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Alternatives**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Unique attributes**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Value/proof**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Best-fit segment**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Category/frame**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Message boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Versioned context.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Switching interview**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternative map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Value chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Beachhead criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Aspirational feature excluded. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Multiple segments get separate contexts. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Category creation requires education cost.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “job/circumstance” cita evidência identificada, aplica “switching interview”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Positioning Evidence File foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `positioning_canvas_md.md` ou formato nativo equivalente: materializa **`positioning-canvas.md`** e deve ser citado pelo artefato principal.
- `alternative_map_csv.md` ou formato nativo equivalente: materializa **`alternative-map.csv`** e deve ser citado pelo artefato principal.
- `message_boundaries_yaml.md` ou formato nativo equivalente: materializa **`message-boundaries.yaml`** e deve ser citado pelo artefato principal.
- `proof_library.md` ou formato nativo equivalente: materializa **proof library** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: customer evidence 25, differentiation 25, clarity 20, proof 15, usability downstream 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Obviously Awesome**, April Dunford (book, força: canonical). Aplicação: Competitive alternatives, differentiated value and category. Localizador: Ambient Press, 2019, ISBN 9781999023003. Consulta: 2026-08-24.
2. **Crossing the Chasm, 3rd ed.**, Geoffrey Moore (book, força: canonical). Aplicação: Beachhead segment and whole-product context. Localizador: HarperBusiness, 2014, ISBN 9780062292988. Consulta: 2026-08-24.
3. **Jobs to Be Done Theory**, Christensen Institute (official, força: primary). Aplicação: Progress, circumstance and switching forces. Localizador: https://www.christenseninstitute.org/theory/jobs-to-be-done/. Consulta: 2026-08-24.


# Template — Positioning Evidence File

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | para quem o produto é uniquely valuable, versus what, in what context? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Customer evidence

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Job/circumstance

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Alternatives

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Unique attributes

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Value/proof

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Best-fit segment

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Category/frame

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Message boundaries

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Versioned context.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Positioning Evidence File

### `positioning-canvas.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `alternative-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `message-boundaries.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### proof library

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

customer evidence 25, differentiation 25, clarity 20, proof 15, usability downstream 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `aspirational feature excluded; multiple segments get separate contexts; category creation requires education cost.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "required": [
    "name",
    "job",
    "pain",
    "alternative",
    "evidence"
  ],
  "min_evidence_chars": 5
}


{
  "segments": [
    {
      "name": "SMB ops",
      "job": "reduce manual work",
      "pain": "tool fragmentation",
      "alternative": "spreadsheets",
      "evidence": "12 interviews"
    }
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Positioning Evidence File",
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
        "customer_evidence",
        "job_circumstance",
        "alternatives",
        "unique_attributes",
        "value_proof",
        "best_fit_segment",
        "category_frame",
        "message_boundaries",
        "versioned_context"
      ],
      "properties": {
        "customer_evidence": {
          "type": "string",
          "minLength": 3
        },
        "job_circumstance": {
          "type": "string",
          "minLength": 3
        },
        "alternatives": {
          "type": "string",
          "minLength": 3
        },
        "unique_attributes": {
          "type": "string",
          "minLength": 3
        },
        "value_proof": {
          "type": "string",
          "minLength": 3
        },
        "best_fit_segment": {
          "type": "string",
          "minLength": 3
        },
        "category_frame": {
          "type": "string",
          "minLength": 3
        },
        "message_boundaries": {
          "type": "string",
          "minLength": 3
        },
        "versioned_context": {
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
    "behavior": "product-marketing-context:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "product-marketing-context:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "positioning-rules.json",
      "path": "min_evidence_chars",
      "value": 6
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "product-marketing-context:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "segments.json",
      "path": "segments.0.name",
      "value": "SMB ops alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "segments.json",
      "path": "segments.0.evidence",
      "value": ""
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "product-marketing-context:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "segments.json",
      "path": "segments.0.pain",
      "value": ""
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "product-marketing-context:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "segments.json",
      "path": "segments.0.job",
      "value": ""
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "product-marketing-context:closed-failure-3"
  }
]


{
  "objective": "Executar product-marketing-context com evidência verificável | rejeição 1"
}


{
  "objective": "Executar product-marketing-context com evidência verificável | rejeição 2"
}


{
  "objective": "Executar product-marketing-context com evidência verificável | rejeição 3"
}


{
  "objective": "Executar product-marketing-context com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar product-marketing-context com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar product-marketing-context com evidência verificável | cenário executável 3"
}


## 27. product-marketing-context — Positioning Evidence File

- **Decisão:** para quem o produto é uniquely valuable, versus what, in what context?
- **Fluxo:** customer evidence → job/circumstance → alternatives → unique attributes → value/proof → best-fit segment → category/frame → message boundaries → versioned context.
- **Técnicas:** switching interview; alternative map; value chain; beachhead criteria; claim-evidence trace.
- **Exceções:** aspirational feature excluded; multiple segments get separate contexts; category creation requires education cost.
- **Rubrica:** customer evidence 25, differentiation 25, clarity 20, proof 15, usability downstream 15.
- **Recursos:** `positioning-canvas.md`, `alternative-map.csv`, `message-boundaries.yaml`, proof library.


[
  {
    "type": "book",
    "title": "Obviously Awesome",
    "author": "April Dunford",
    "reference": "Ambient Press, 2019, ISBN 9781999023003",
    "strength": "canonical",
    "use": "Competitive alternatives, differentiated value and category"
  },
  {
    "type": "book",
    "title": "Crossing the Chasm, 3rd ed.",
    "author": "Geoffrey Moore",
    "reference": "HarperBusiness, 2014, ISBN 9780062292988",
    "strength": "canonical",
    "use": "Beachhead segment and whole-product context"
  },
  {
    "type": "official",
    "title": "Jobs to Be Done Theory",
    "author": "Christensen Institute",
    "url": "https://www.christenseninstitute.org/theory/jobs-to-be-done/",
    "strength": "primary",
    "use": "Progress, circumstance and switching forces"
  }
]"""
import argparse,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(name):
 p=ROOT/name
 try: return json.loads(p.read_text())
 except Exception as e: raise SystemExit(f"resource error {name}: {e}")
def fail(message): raise SystemExit(message)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True); ns=ap.parse_args()
 try: request=json.loads(pathlib.Path(ns.input).read_text())
 except Exception as e: fail(f"invalid input: {e}")
 if not isinstance(request,dict) or not request.get("objective") or not str(request["objective"]).strip(): fail("objective required")
 A=load("assets/segments.json"); B=load("assets/positioning-rules.json")
 segments=A["segments"]; rules=B; cards=[]
 for s in segments:
     missing=[k for k in rules["required"] if not str(s.get(k,"")).strip()]
     if missing: fail("segment missing required field: "+missing[0])
     if len(s["evidence"].strip())<rules["min_evidence_chars"]: fail("segment evidence too weak")
     cards.append({"segment":s["name"],"when":s["job"],"problem":s["pain"],"instead_of":s["alternative"],"proof":s["evidence"],"message":f'Para {s["name"]}: {s["job"]} sem {s["pain"]}.'})
 artifact={"kind":"product-marketing-context","positioning_cards":cards,"evidence_coverage":len(cards)}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/segments.json","assets/positioning-rules.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
