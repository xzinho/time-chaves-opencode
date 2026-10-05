#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: social-intelligence
description: "Executa Trace-to-Narrative Observatory para responder: que narrativas/sinais importam, quão confiáveis são e que ação justificam?"
---

# Social Intelligence

## Escopo e gatilhos

Use quando a decisão real for: **que narrativas/sinais importam, quão confiáveis são e que ação justificam?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Trace-to-Narrative Observatory**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Trace-to-Narrative Observatory

1. **Decision/query book**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Platform/sample plan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Collect with timestamps**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Dedupe/entities**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code themes/stance/format**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Velocity/novelty**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Corroborate**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Narrative map**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Implications/caveats.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Purposive sampling**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query expansion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Codebook agreement**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source diversity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Anomaly detection**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Narrative lifecycle.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Engagement unavailable means no traction claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/coordination suspected is flagged. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Social trace is not population opinion.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: provenance 25, coverage 20, coding 20, corroboration 20, caveats/action 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `query_book_yaml.md` ou formato nativo equivalente: materializa **`query-book.yaml`** e deve ser citado pelo artefato principal.
- `source_ledger_jsonl.md` ou formato nativo equivalente: materializa **`source-ledger.jsonl`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `narrative_map_and_dedupe_state.md` ou formato nativo equivalente: materializa **narrative map and dedupe state** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (official, força: primary). Aplicação: Ethical observation and reporting. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **An Introduction to Social Media Research**, Matthew Salganik (book, força: canonical). Aplicação: Digital-trace validity, ethics and representativeness. Localizador: Bit by Bit, Princeton University Press, 2018, ISBN 9780691158648. Consulta: 2026-08-24.
3. **Google Trends Help**, Google (official, força: primary). Aplicação: Cross-checking normalized public interest. Localizador: https://support.google.com/trends/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Trace-to-Narrative Observatory

## Pergunta de controle

que narrativas/sinais importam, quão confiáveis são e que ação justificam?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **decision/query book** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **purposive sampling** responde à pergunta sem extrapolar o dado? Se não, selecione **narrative lifecycle.** e declare a troca.
3. Há uma destas exceções: engagement unavailable means no traction claim; bot/coordination suspected is flagged; social trace is not population opinion.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que narrativas/sinais importam, quão confiáveis são e que ação justificam?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Decision/query book**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Platform/sample plan**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Collect with timestamps**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Dedupe/entities**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code themes/stance/format**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Velocity/novelty**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Corroborate**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Narrative map**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Implications/caveats.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Purposive sampling**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query expansion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Codebook agreement**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source diversity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Anomaly detection**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Narrative lifecycle.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Engagement unavailable means no traction claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/coordination suspected is flagged. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Social trace is not population opinion.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “platform/sample plan” cita evidência identificada, aplica “purposive sampling”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Trace-to-Narrative Observatory foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `query_book_yaml.md` ou formato nativo equivalente: materializa **`query-book.yaml`** e deve ser citado pelo artefato principal.
- `source_ledger_jsonl.md` ou formato nativo equivalente: materializa **`source-ledger.jsonl`** e deve ser citado pelo artefato principal.
- `codebook_csv.md` ou formato nativo equivalente: materializa **`codebook.csv`** e deve ser citado pelo artefato principal.
- `narrative_map_and_dedupe_state.md` ou formato nativo equivalente: materializa **narrative map and dedupe state** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: provenance 25, coverage 20, coding 20, corroboration 20, caveats/action 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ICC/ESOMAR International Code**, ICC and ESOMAR (official, força: primary). Aplicação: Ethical observation and reporting. Localizador: https://esomar.org/code-and-guidelines/icc-esomar-code. Consulta: 2026-08-24.
2. **An Introduction to Social Media Research**, Matthew Salganik (book, força: canonical). Aplicação: Digital-trace validity, ethics and representativeness. Localizador: Bit by Bit, Princeton University Press, 2018, ISBN 9780691158648. Consulta: 2026-08-24.
3. **Google Trends Help**, Google (official, força: primary). Aplicação: Cross-checking normalized public interest. Localizador: https://support.google.com/trends/. Consulta: 2026-08-24.


# Template — Trace-to-Narrative Observatory

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | que narrativas/sinais importam, quão confiáveis são e que ação justificam? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Decision/query book

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Platform/sample plan

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Collect with timestamps

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Dedupe/entities

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Code themes/stance/format

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Velocity/novelty

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Corroborate

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Narrative map

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Implications/caveats.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Trace-to-Narrative Observatory

### `query-book.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `source-ledger.jsonl`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `codebook.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### narrative map and dedupe state

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

provenance 25, coverage 20, coding 20, corroboration 20, caveats/action 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `engagement unavailable means no traction claim; bot/coordination suspected is flagged; social trace is not population opinion.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "weights": {
    "mentions": 0.3,
    "engagement": 0.5,
    "authors": 0.2
  },
  "max_age_hours": 24,
  "required_sources": [
    "x"
  ]
}


{
  "signals": [
    {
      "id": "S1",
      "topic": "AI agents",
      "mentions": 120,
      "engagement": 450,
      "authors": 80,
      "source": "x",
      "observed_at": "2026-08-24T10:00:00-03:00"
    }
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Trace-to-Narrative Observatory",
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
        "decision_query_book",
        "platform_sample_plan",
        "collect_with_timestamps",
        "dedupe_entities",
        "code_themes_stance_format",
        "velocity_novelty",
        "corroborate",
        "narrative_map",
        "implications_caveats"
      ],
      "properties": {
        "decision_query_book": {
          "type": "string",
          "minLength": 3
        },
        "platform_sample_plan": {
          "type": "string",
          "minLength": 3
        },
        "collect_with_timestamps": {
          "type": "string",
          "minLength": 3
        },
        "dedupe_entities": {
          "type": "string",
          "minLength": 3
        },
        "code_themes_stance_format": {
          "type": "string",
          "minLength": 3
        },
        "velocity_novelty": {
          "type": "string",
          "minLength": 3
        },
        "corroborate": {
          "type": "string",
          "minLength": 3
        },
        "narrative_map": {
          "type": "string",
          "minLength": 3
        },
        "implications_caveats": {
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
    "behavior": "social-intelligence:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "social-intelligence:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "scoring-model.json",
      "path": "max_age_hours",
      "value": 25
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "social-intelligence:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "signals.json",
      "path": "signals.0.id",
      "value": "S1 alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "scoring-model.json",
      "path": "weights",
      "value": {
        "mentions": 0.9,
        "engagement": 0.5,
        "authors": 0.2
      }
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "social-intelligence:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "signals.json",
      "path": "signals.0.source",
      "value": "unknown"
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "social-intelligence:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "signals.json",
      "path": "signals.0.observed_at",
      "value": "yesterday"
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "social-intelligence:closed-failure-3"
  }
]


{
  "objective": "Executar social-intelligence com evidência verificável | rejeição 1"
}


{
  "objective": "Executar social-intelligence com evidência verificável | rejeição 2"
}


{
  "objective": "Executar social-intelligence com evidência verificável | rejeição 3"
}


{
  "objective": "Executar social-intelligence com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar social-intelligence com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar social-intelligence com evidência verificável | cenário executável 3"
}


## 33. social-intelligence — Trace-to-Narrative Observatory

- **Decisão:** que narrativas/sinais importam, quão confiáveis são e que ação justificam?
- **Fluxo:** decision/query book → platform/sample plan → collect with timestamps → dedupe/entities → code themes/stance/format → velocity/novelty → corroborate → narrative map → implications/caveats.
- **Técnicas:** purposive sampling; query expansion; codebook agreement; source diversity; anomaly detection; narrative lifecycle.
- **Exceções:** engagement unavailable means no traction claim; bot/coordination suspected is flagged; social trace is not population opinion.
- **Rubrica:** provenance 25, coverage 20, coding 20, corroboration 20, caveats/action 15.
- **Recursos:** `query-book.yaml`, `source-ledger.jsonl`, `codebook.csv`, narrative map and dedupe state.


[
  {
    "type": "official",
    "title": "ICC/ESOMAR International Code",
    "author": "ICC and ESOMAR",
    "url": "https://esomar.org/code-and-guidelines/icc-esomar-code",
    "strength": "primary",
    "use": "Ethical observation and reporting"
  },
  {
    "type": "book",
    "title": "An Introduction to Social Media Research",
    "author": "Matthew Salganik",
    "reference": "Bit by Bit, Princeton University Press, 2018, ISBN 9780691158648",
    "strength": "canonical",
    "use": "Digital-trace validity, ethics and representativeness"
  },
  {
    "type": "official",
    "title": "Google Trends Help",
    "author": "Google",
    "url": "https://support.google.com/trends/",
    "strength": "primary",
    "use": "Cross-checking normalized public interest"
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
 A=load("assets/signals.json"); B=load("assets/scoring-model.json")
 import datetime
 signals=A["signals"]; model=B; weights=model["weights"]
 if abs(sum(weights.values())-1)>1e-9: fail("scoring weights must sum to one")
 ranked=[]
 for s in signals:
     if s.get("source") not in model["required_sources"] or any(s.get(k,0)<0 for k in weights): fail("invalid signal")
     try: datetime.datetime.fromisoformat(s["observed_at"])
     except Exception: fail("invalid observation timestamp")
     score=sum(s[k]*weights[k] for k in weights)
     ranked.append({**s,"score":round(score,2),"confidence":round(min(1,s["authors"]/50),2)})
 ranked.sort(key=lambda x:x["score"],reverse=True)
 artifact={"kind":"social-intelligence","ranked_signals":ranked,"method":"weighted-observed-signal","source_coverage":sorted(set(x["source"] for x in signals))}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/signals.json","assets/scoring-model.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
