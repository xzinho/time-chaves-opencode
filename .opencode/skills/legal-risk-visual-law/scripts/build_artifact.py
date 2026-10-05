#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: legal-risk-visual-law
description: "Executa Meaning-Preserving Legal Design para responder: como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?"
---

# Legal Risk Visual Law

## Escopo e gatilhos

Use quando a decisão real for: **como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Meaning-Preserving Legal Design**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Meaning-Preserving Legal Design

1. **Legal source**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Rule/condition/exception/consequence extraction**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Audience task**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Layer architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Visual encoding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Legal fidelity review**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Comprehension test**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Revision.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Layered disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Decision tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk heatmap with criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Before/after comprehension**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic crosswalk.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Ambiguidade substantiva permanece explícita. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Cor nunca é único canal. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Documento visual não substitui original quando obrigatório.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fidelidade 30, compreensão 25, actionability 20, acessibilidade 15, rastreabilidade 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `legal_semantic_map_csv.md` ou formato nativo equivalente: materializa **`legal-semantic-map.csv`** e deve ser citado pelo artefato principal.
- `decision_tree_mmd.md` ou formato nativo equivalente: materializa **`decision-tree.mmd`** e deve ser citado pelo artefato principal.
- `comprehension_script.md` ou formato nativo equivalente: materializa **comprehension script** e deve ser citado pelo artefato principal.
- `fidelity_checklist.md` ou formato nativo equivalente: materializa **fidelity checklist** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Visual Law Library**, Legal Design Alliance (official, força: primary). Aplicação: User-centered legal information design. Localizador: https://www.legaldesignalliance.org/. Consulta: 2026-08-24.
2. **Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Layered explanation without changing legal meaning. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
3. **Legal Design: Integrating Business, Design and Legal Thinking**, Corrales, Fenwick, Haapio (book, força: canonical). Aplicação: Legal-service prototyping and usability. Localizador: Edward Elgar, 2021, ISBN 9781839102271. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Meaning-Preserving Legal Design

## Pergunta de controle

como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **legal source** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **layered disclosure** responde à pergunta sem extrapolar o dado? Se não, selecione **semantic crosswalk.** e declare a troca.
3. Há uma destas exceções: ambiguidade substantiva permanece explícita; cor nunca é único canal; documento visual não substitui original quando obrigatório.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Legal source**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Rule/condition/exception/consequence extraction**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Audience task**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Layer architecture**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Visual encoding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Legal fidelity review**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Comprehension test**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Revision.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Layered disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Decision tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk heatmap with criteria**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Before/after comprehension**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic crosswalk.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Ambiguidade substantiva permanece explícita. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Cor nunca é único canal. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Documento visual não substitui original quando obrigatório.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “rule/condition/exception/consequence extraction” cita evidência identificada, aplica “layered disclosure”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Meaning-Preserving Legal Design foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `legal_semantic_map_csv.md` ou formato nativo equivalente: materializa **`legal-semantic-map.csv`** e deve ser citado pelo artefato principal.
- `decision_tree_mmd.md` ou formato nativo equivalente: materializa **`decision-tree.mmd`** e deve ser citado pelo artefato principal.
- `comprehension_script.md` ou formato nativo equivalente: materializa **comprehension script** e deve ser citado pelo artefato principal.
- `fidelity_checklist.md` ou formato nativo equivalente: materializa **fidelity checklist** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fidelidade 30, compreensão 25, actionability 20, acessibilidade 15, rastreabilidade 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Visual Law Library**, Legal Design Alliance (official, força: primary). Aplicação: User-centered legal information design. Localizador: https://www.legaldesignalliance.org/. Consulta: 2026-08-24.
2. **Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Layered explanation without changing legal meaning. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
3. **Legal Design: Integrating Business, Design and Legal Thinking**, Corrales, Fenwick, Haapio (book, força: canonical). Aplicação: Legal-service prototyping and usability. Localizador: Edward Elgar, 2021, ISBN 9781839102271. Consulta: 2026-08-24.


# Template — Meaning-Preserving Legal Design

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Legal source

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Rule/condition/exception/consequence extraction

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Audience task

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Layer architecture

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Visual encoding

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Legal fidelity review

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Comprehension test

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Revision.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Meaning-Preserving Legal Design

### `legal-semantic-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `decision-tree.mmd`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### comprehension script

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### fidelity checklist

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

fidelidade 30, compreensão 25, actionability 20, acessibilidade 15, rastreabilidade 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `ambiguidade substantiva permanece explícita; cor nunca é único canal; documento visual não substitui original quando obrigatório.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "likelihood": [
    1,
    2,
    3,
    4,
    5
  ],
  "impact": [
    1,
    2,
    3,
    4,
    5
  ],
  "bands": {
    "low": [
      1,
      4
    ],
    "medium": [
      5,
      9
    ],
    "high": [
      10,
      16
    ],
    "critical": [
      17,
      25
    ]
  }
}


{
  "patterns": [
    "timeline",
    "decision-tree",
    "responsibility-map"
  ],
  "accessibility": {
    "contrast_min": 4.5,
    "plain_language": true
  }
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Meaning-Preserving Legal Design",
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
        "legal_source",
        "rule_condition_exception_consequence_extraction",
        "audience_task",
        "layer_architecture",
        "visual_encoding",
        "legal_fidelity_review",
        "comprehension_test",
        "revision"
      ],
      "properties": {
        "legal_source": {
          "type": "string",
          "minLength": 3
        },
        "rule_condition_exception_consequence_extraction": {
          "type": "string",
          "minLength": 3
        },
        "audience_task": {
          "type": "string",
          "minLength": 3
        },
        "layer_architecture": {
          "type": "string",
          "minLength": 3
        },
        "visual_encoding": {
          "type": "string",
          "minLength": 3
        },
        "legal_fidelity_review": {
          "type": "string",
          "minLength": 3
        },
        "comprehension_test": {
          "type": "string",
          "minLength": 3
        },
        "revision": {
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
    "behavior": "legal-risk-visual-law:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "legal-risk-visual-law:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "risk-matrix.json",
      "path": "likelihood.0",
      "value": 2
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "legal-risk-visual-law:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "risk-matrix.json",
      "path": "likelihood.1",
      "value": 3
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "risk-matrix.json",
      "path": "bands.low",
      "value": [
        1,
        5
      ]
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "legal-risk-visual-law:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "risk-matrix.json",
      "path": "bands.critical",
      "value": [
        18,
        25
      ]
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "legal-risk-visual-law:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "visual-patterns.json",
      "path": "accessibility.contrast_min",
      "value": 3
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "legal-risk-visual-law:closed-failure-3"
  }
]


{
  "objective": "Executar legal-risk-visual-law com evidência verificável | rejeição 1"
}


{
  "objective": "Executar legal-risk-visual-law com evidência verificável | rejeição 2"
}


{
  "objective": "Executar legal-risk-visual-law com evidência verificável | rejeição 3"
}


{
  "objective": "Executar legal-risk-visual-law com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar legal-risk-visual-law com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar legal-risk-visual-law com evidência verificável | cenário executável 3"
}


## 19. legal-risk-visual-law — Meaning-Preserving Legal Design

- **Decisão:** como tornar obrigação/risco compreensível sem simplificação juridicamente enganosa?
- **Fluxo:** legal source → rule/condition/exception/consequence extraction → audience task → layer architecture → visual encoding → legal fidelity review → comprehension test → revision.
- **Técnicas:** layered disclosure; decision tree; risk heatmap with criteria; before/after comprehension; semantic crosswalk.
- **Exceções:** ambiguidade substantiva permanece explícita; cor nunca é único canal; documento visual não substitui original quando obrigatório.
- **Rubrica:** fidelidade 30, compreensão 25, actionability 20, acessibilidade 15, rastreabilidade 10.
- **Recursos:** `legal-semantic-map.csv`, `decision-tree.mmd`, comprehension script, fidelity checklist.


[
  {
    "type": "official",
    "title": "Visual Law Library",
    "author": "Legal Design Alliance",
    "url": "https://www.legaldesignalliance.org/",
    "strength": "primary",
    "use": "User-centered legal information design"
  },
  {
    "type": "official",
    "title": "Plain Language Guidelines",
    "author": "PlainLanguage.gov",
    "url": "https://www.plainlanguage.gov/guidelines/",
    "strength": "primary",
    "use": "Layered explanation without changing legal meaning"
  },
  {
    "type": "book",
    "title": "Legal Design: Integrating Business, Design and Legal Thinking",
    "author": "Corrales, Fenwick, Haapio",
    "reference": "Edward Elgar, 2021, ISBN 9781839102271",
    "strength": "canonical",
    "use": "Legal-service prototyping and usability"
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
 A=load("assets/risk-matrix.json"); B=load("assets/visual-patterns.json")
 matrix=A; patterns=B
 scores={}
 for band,limits in matrix["bands"].items():
     lo,hi=limits
     if lo>hi or lo<1 or hi>25: fail("invalid risk band")
     for s in range(lo,hi+1):
         if s in scores: fail("overlapping risk bands")
         scores[s]=band
 if set(scores)!=set(range(1,26)): fail("risk bands have gaps")
 if patterns["accessibility"]["contrast_min"]<4.5 or not patterns["accessibility"]["plain_language"]: fail("visual law accessibility missing")
 artifact={"kind":"visual-law-risk-system","risk_grid":[{"likelihood":l,"impact":i,"score":l*i,"band":scores[l*i]} for l in matrix["likelihood"] for i in matrix["impact"]],"patterns":patterns["patterns"],"accessibility":patterns["accessibility"]}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/risk-matrix.json","assets/visual-patterns.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
