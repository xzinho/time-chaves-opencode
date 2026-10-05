#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: web-research-with-sources
description: "Executa Reproducible Evidence Synthesis para responder: what does the best available evidence support, contradict or leave uncertain?"
---

# Web Research With Sources

## Escopo e gatilhos

Use quando a decisão real for: **what does the best available evidence support, contradict or leave uncertain?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Reproducible Evidence Synthesis**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Reproducible Evidence Synthesis

1. **Protocol/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Search strings/sources/date**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inclusion/exclusion**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Capture metadata**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Screen**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Extract claims/quotes/context**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Assess authority/recency/directness**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Triangulate**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Synthesize with confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Bibliography/limitations.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Prisma-like log**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Primary-source preference**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Lateral reading**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contradiction table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence labels.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Inaccessible source listed, not guessed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Snippet is not evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dynamic page gets timestamp/archive. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ai summary never cited as source.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: reproducibility 25, source strength 25, claim traceability 25, contradiction/limits 15, synthesis 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `search_log_csv.md` ou formato nativo equivalente: materializa **`search-log.csv`** e deve ser citado pelo artefato principal.
- `sources_json.md` ou formato nativo equivalente: materializa **`sources.json`** e deve ser citado pelo artefato principal.
- `claim_evidence_csv.md` ou formato nativo equivalente: materializa **`claim-evidence.csv`** e deve ser citado pelo artefato principal.
- `limitations_md.md` ou formato nativo equivalente: materializa **`limitations.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **PRISMA 2020 Statement**, PRISMA (standard, força: primary). Aplicação: Transparent search, screening and inclusion trail. Localizador: https://www.prisma-statement.org/prisma-2020. Consulta: 2026-08-24.
2. **Evaluating Sources**, Library of Congress (official, força: primary). Aplicação: Authority, provenance and corroboration checks. Localizador: https://guides.loc.gov/evaluating-sources. Consulta: 2026-08-24.
3. **Web Annotation Data Model**, W3C (official, força: primary). Aplicação: Quote-level evidence anchors and provenance. Localizador: https://www.w3.org/TR/annotation-model/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Reproducible Evidence Synthesis

## Pergunta de controle

what does the best available evidence support, contradict or leave uncertain?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **protocol/question** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **PRISMA-like log** responde à pergunta sem extrapolar o dado? Se não, selecione **confidence labels.** e declare a troca.
3. Há uma destas exceções: inaccessible source listed, not guessed; snippet is not evidence; dynamic page gets timestamp/archive; AI summary never cited as source.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what does the best available evidence support, contradict or leave uncertain?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Protocol/question**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Search strings/sources/date**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inclusion/exclusion**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Capture metadata**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Screen**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Extract claims/quotes/context**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Assess authority/recency/directness**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Triangulate**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Synthesize with confidence**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Bibliography/limitations.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Prisma-like log**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Primary-source preference**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Lateral reading**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Claim-evidence matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contradiction table**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Confidence labels.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Inaccessible source listed, not guessed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Snippet is not evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dynamic page gets timestamp/archive. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ai summary never cited as source.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “search strings/sources/date” cita evidência identificada, aplica “PRISMA-like log”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Reproducible Evidence Synthesis foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `research_protocol_md.md` ou formato nativo equivalente: materializa **`research-protocol.md`** e deve ser citado pelo artefato principal.
- `search_log_csv.md` ou formato nativo equivalente: materializa **`search-log.csv`** e deve ser citado pelo artefato principal.
- `sources_json.md` ou formato nativo equivalente: materializa **`sources.json`** e deve ser citado pelo artefato principal.
- `claim_evidence_csv.md` ou formato nativo equivalente: materializa **`claim-evidence.csv`** e deve ser citado pelo artefato principal.
- `limitations_md.md` ou formato nativo equivalente: materializa **`limitations.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: reproducibility 25, source strength 25, claim traceability 25, contradiction/limits 15, synthesis 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **PRISMA 2020 Statement**, PRISMA (standard, força: primary). Aplicação: Transparent search, screening and inclusion trail. Localizador: https://www.prisma-statement.org/prisma-2020. Consulta: 2026-08-24.
2. **Evaluating Sources**, Library of Congress (official, força: primary). Aplicação: Authority, provenance and corroboration checks. Localizador: https://guides.loc.gov/evaluating-sources. Consulta: 2026-08-24.
3. **Web Annotation Data Model**, W3C (official, força: primary). Aplicação: Quote-level evidence anchors and provenance. Localizador: https://www.w3.org/TR/annotation-model/. Consulta: 2026-08-24.


# Template — Reproducible Evidence Synthesis

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | what does the best available evidence support, contradict or leave uncertain? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Protocol/question

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Search strings/sources/date

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Inclusion/exclusion

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Capture metadata

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Screen

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Extract claims/quotes/context

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Assess authority/recency/directness

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Triangulate

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Synthesize with confidence

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 10. Bibliography/limitations.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Reproducible Evidence Synthesis

### `research-protocol.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `search-log.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `sources.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `claim-evidence.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `limitations.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

reproducibility 25, source strength 25, claim traceability 25, contradiction/limits 15, synthesis 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `inaccessible source listed, not guessed; snippet is not evidence; dynamic page gets timestamp/archive; AI summary never cited as source.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "min_sources_per_claim": 1,
  "allowed_schemes": [
    "https"
  ],
  "required": [
    "url",
    "title",
    "published",
    "claim_ids",
    "quote"
  ]
}


{
  "sources": [
    {
      "url": "https://www.w3.org/TR/WCAG22/",
      "title": "WCAG 2.2",
      "published": "2023-10-05",
      "claim_ids": [
        "C1"
      ],
      "quote": "Web Content Accessibility Guidelines 2.2"
    }
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Reproducible Evidence Synthesis",
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
        "protocol_question",
        "search_strings_sources_date",
        "inclusion_exclusion",
        "capture_metadata",
        "screen",
        "extract_claims_quotes_context",
        "assess_authority_recency_directness",
        "triangulate",
        "synthesize_with_confidence",
        "bibliography_limitations"
      ],
      "properties": {
        "protocol_question": {
          "type": "string",
          "minLength": 3
        },
        "search_strings_sources_date": {
          "type": "string",
          "minLength": 3
        },
        "inclusion_exclusion": {
          "type": "string",
          "minLength": 3
        },
        "capture_metadata": {
          "type": "string",
          "minLength": 3
        },
        "screen": {
          "type": "string",
          "minLength": 3
        },
        "extract_claims_quotes_context": {
          "type": "string",
          "minLength": 3
        },
        "assess_authority_recency_directness": {
          "type": "string",
          "minLength": 3
        },
        "triangulate": {
          "type": "string",
          "minLength": 3
        },
        "synthesize_with_confidence": {
          "type": "string",
          "minLength": 3
        },
        "bibliography_limitations": {
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
    "behavior": "web-research-with-sources:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "web-research-with-sources:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "sources.json",
      "path": "sources.0.title",
      "value": "WCAG 2.2 alternative"
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "web-research-with-sources:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "sources.json",
      "path": "sources.0.published",
      "value": "2023-10-05 alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "sources.json",
      "path": "sources.0.url",
      "value": "http://example.com"
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "web-research-with-sources:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "sources.json",
      "path": "sources.0.quote",
      "value": ""
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "web-research-with-sources:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "sources.json",
      "path": "sources.0.claim_ids",
      "value": []
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "web-research-with-sources:closed-failure-3"
  }
]


{
  "objective": "Executar web-research-with-sources com evidência verificável | rejeição 1"
}


{
  "objective": "Executar web-research-with-sources com evidência verificável | rejeição 2"
}


{
  "objective": "Executar web-research-with-sources com evidência verificável | rejeição 3"
}


{
  "objective": "Executar web-research-with-sources com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar web-research-with-sources com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar web-research-with-sources com evidência verificável | cenário executável 3"
}


## 38. web-research-with-sources — Reproducible Evidence Synthesis

- **Decisão:** what does the best available evidence support, contradict or leave uncertain?
- **Fluxo:** protocol/question → search strings/sources/date → inclusion/exclusion → capture metadata → screen → extract claims/quotes/context → assess authority/recency/directness → triangulate → synthesize with confidence → bibliography/limitations.
- **Técnicas:** PRISMA-like log; primary-source preference; lateral reading; claim-evidence matrix; contradiction table; confidence labels.
- **Exceções:** inaccessible source listed, not guessed; snippet is not evidence; dynamic page gets timestamp/archive; AI summary never cited as source.
- **Rubrica:** reproducibility 25, source strength 25, claim traceability 25, contradiction/limits 15, synthesis 10.
- **Recursos:** `research-protocol.md`, `search-log.csv`, `sources.json`, `claim-evidence.csv`, `limitations.md`.


[
  {
    "type": "standard",
    "title": "PRISMA 2020 Statement",
    "author": "PRISMA",
    "url": "https://www.prisma-statement.org/prisma-2020",
    "strength": "primary",
    "use": "Transparent search, screening and inclusion trail"
  },
  {
    "type": "official",
    "title": "Evaluating Sources",
    "author": "Library of Congress",
    "url": "https://guides.loc.gov/evaluating-sources",
    "strength": "primary",
    "use": "Authority, provenance and corroboration checks"
  },
  {
    "type": "official",
    "title": "Web Annotation Data Model",
    "author": "W3C",
    "url": "https://www.w3.org/TR/annotation-model/",
    "strength": "primary",
    "use": "Quote-level evidence anchors and provenance"
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
 A=load("assets/sources.json"); B=load("assets/evidence-policy.json")
 from urllib.parse import urlparse
 sources=A["sources"]; policy=B; claims={}
 for s in sources:
     if any(not str(s.get(k,"")).strip() for k in policy["required"]): fail("source metadata/evidence incomplete")
     if urlparse(s["url"]).scheme not in policy["allowed_schemes"]: fail("insecure source URL")
     for cid in s["claim_ids"]: claims.setdefault(cid,[]).append(s["url"])
 if not claims or any(len(v)<policy["min_sources_per_claim"] for v in claims.values()): fail("unsupported claim")
 artifact={"kind":"source-grounded-research","sources":sources,"claim_evidence":claims,"citation_count":sum(map(len,claims.values()))}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/sources.json","assets/evidence-policy.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
