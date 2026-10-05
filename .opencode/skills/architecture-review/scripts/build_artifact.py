#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: architecture-review
description: "Executa Scenario-Tradeoff Review para responder: a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?"
---

# Architecture Review

## Escopo e gatilhos

Use quando a decisão real for: **a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Scenario-Tradeoff Review**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Scenario-Tradeoff Review

1. **Stakeholders/concerns**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Context/container/data/deployment views**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Quality-attribute scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Decision log**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Tradeoff/risk probes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Fitness functions**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Utility tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Atam-lite**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Adr review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency/critical-path map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Failure-mode walkthrough.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Brownfield começa por runtime evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama desatualizado não é fonte. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de slo bloqueia afirmações de desempenho.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: rastreabilidade 20, qualidade dos cenários 20, evidência 20, tradeoffs 20, operabilidade/reversibilidade 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `stakeholder_concern_matrix_md.md` ou formato nativo equivalente: materializa **`stakeholder-concern-matrix.md`** e deve ser citado pelo artefato principal.
- `quality_scenarios_yaml.md` ou formato nativo equivalente: materializa **`quality-scenarios.yaml`** e deve ser citado pelo artefato principal.
- `adr_index_csv.md` ou formato nativo equivalente: materializa **`adr-index.csv`** e deve ser citado pelo artefato principal.
- `fitness_functions_yaml.md` ou formato nativo equivalente: materializa **`fitness-functions.yaml`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ISO/IEC/IEEE 42010 Architecture Description**, ISO/IEC/IEEE (standard, força: primary). Aplicação: Stakeholders, concerns, viewpoints and decisions. Localizador: https://www.iso.org/standard/74393.html. Consulta: 2026-08-24.
2. **AWS Well-Architected Framework**, AWS (official, força: primary). Aplicação: Risk review across operational pillars. Localizador: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html. Consulta: 2026-08-24.
3. **Software Architecture in Practice, 4th ed.**, Bass, Clements, Kazman (book, força: canonical). Aplicação: Quality-attribute scenarios and tradeoff analysis. Localizador: Addison-Wesley, 2021, ISBN 9780136886099. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Scenario-Tradeoff Review

## Pergunta de controle

a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **stakeholders/concerns** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **utility tree** responde à pergunta sem extrapolar o dado? Se não, selecione **failure-mode walkthrough.** e declare a troca.
3. Há uma destas exceções: brownfield começa por runtime evidence; diagrama desatualizado não é fonte; ausência de SLO bloqueia afirmações de desempenho.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Stakeholders/concerns**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Context/container/data/deployment views**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Quality-attribute scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Decision log**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Tradeoff/risk probes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Fitness functions**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Utility tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Atam-lite**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Adr review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency/critical-path map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Failure-mode walkthrough.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Brownfield começa por runtime evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama desatualizado não é fonte. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de slo bloqueia afirmações de desempenho.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “context/container/data/deployment views” cita evidência identificada, aplica “utility tree”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Scenario-Tradeoff Review foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `stakeholder_concern_matrix_md.md` ou formato nativo equivalente: materializa **`stakeholder-concern-matrix.md`** e deve ser citado pelo artefato principal.
- `quality_scenarios_yaml.md` ou formato nativo equivalente: materializa **`quality-scenarios.yaml`** e deve ser citado pelo artefato principal.
- `adr_index_csv.md` ou formato nativo equivalente: materializa **`adr-index.csv`** e deve ser citado pelo artefato principal.
- `fitness_functions_yaml.md` ou formato nativo equivalente: materializa **`fitness-functions.yaml`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: rastreabilidade 20, qualidade dos cenários 20, evidência 20, tradeoffs 20, operabilidade/reversibilidade 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ISO/IEC/IEEE 42010 Architecture Description**, ISO/IEC/IEEE (standard, força: primary). Aplicação: Stakeholders, concerns, viewpoints and decisions. Localizador: https://www.iso.org/standard/74393.html. Consulta: 2026-08-24.
2. **AWS Well-Architected Framework**, AWS (official, força: primary). Aplicação: Risk review across operational pillars. Localizador: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html. Consulta: 2026-08-24.
3. **Software Architecture in Practice, 4th ed.**, Bass, Clements, Kazman (book, força: canonical). Aplicação: Quality-attribute scenarios and tradeoff analysis. Localizador: Addison-Wesley, 2021, ISBN 9780136886099. Consulta: 2026-08-24.


# Template — Scenario-Tradeoff Review

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Stakeholders/concerns

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Context/container/data/deployment views

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Quality-attribute scenarios

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Decision log

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Tradeoff/risk probes

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Fitness functions

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Gate.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Scenario-Tradeoff Review

### `stakeholder-concern-matrix.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `quality-scenarios.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `adr-index.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `fitness-functions.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

rastreabilidade 20, qualidade dos cenários 20, evidência 20, tradeoffs 20, operabilidade/reversibilidade 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `brownfield começa por runtime evidence; diagrama desatualizado não é fonte; ausência de SLO bloqueia afirmações de desempenho.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "forbidden_edges": [
    "domain->ui",
    "domain->infrastructure"
  ],
  "required_boundaries": [
    "domain",
    "application",
    "infrastructure"
  ]
}


{
  "attributes": {
    "availability": 99.9,
    "latency_p95_ms": 300,
    "rpo_minutes": 15
  }
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Scenario-Tradeoff Review",
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
        "stakeholders_concerns",
        "context_container_data_deployment_views",
        "quality_attribute_scenarios",
        "decision_log",
        "tradeoff_risk_probes",
        "fitness_functions",
        "gate"
      ],
      "properties": {
        "stakeholders_concerns": {
          "type": "string",
          "minLength": 3
        },
        "context_container_data_deployment_views": {
          "type": "string",
          "minLength": 3
        },
        "quality_attribute_scenarios": {
          "type": "string",
          "minLength": 3
        },
        "decision_log": {
          "type": "string",
          "minLength": 3
        },
        "tradeoff_risk_probes": {
          "type": "string",
          "minLength": 3
        },
        "fitness_functions": {
          "type": "string",
          "minLength": 3
        },
        "gate": {
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
    "behavior": "architecture-review:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "architecture-review:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "dependency-rules.json",
      "path": "forbidden_edges.0",
      "value": "domain->ui alternative"
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "architecture-review:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "dependency-rules.json",
      "path": "forbidden_edges.1",
      "value": "domain->infrastructure alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "quality-attributes.json",
      "path": "attributes.availability",
      "value": 101
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "architecture-review:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "quality-attributes.json",
      "path": "attributes.latency_p95_ms",
      "value": 0
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "architecture-review:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "dependency-rules.json",
      "path": "required_boundaries",
      "value": [
        "application"
      ]
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "architecture-review:closed-failure-3"
  }
]


{
  "objective": "Executar architecture-review com evidência verificável | rejeição 1"
}


{
  "objective": "Executar architecture-review com evidência verificável | rejeição 2"
}


{
  "objective": "Executar architecture-review com evidência verificável | rejeição 3"
}


{
  "objective": "Executar architecture-review com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar architecture-review com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar architecture-review com evidência verificável | cenário executável 3"
}


## 3. architecture-review — Scenario-Tradeoff Review

- **Decisão:** a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?
- **Fluxo:** stakeholders/concerns → context/container/data/deployment views → quality-attribute scenarios → decision log → tradeoff/risk probes → fitness functions → gate.
- **Técnicas:** utility tree; ATAM-lite; ADR review; dependency/critical-path map; failure-mode walkthrough.
- **Exceções:** brownfield começa por runtime evidence; diagrama desatualizado não é fonte; ausência de SLO bloqueia afirmações de desempenho.
- **Rubrica:** rastreabilidade 20, qualidade dos cenários 20, evidência 20, tradeoffs 20, operabilidade/reversibilidade 20.
- **Recursos:** `stakeholder-concern-matrix.md`, `quality-scenarios.yaml`, `adr-index.csv`, `fitness-functions.yaml`.


[
  {
    "type": "standard",
    "title": "ISO/IEC/IEEE 42010 Architecture Description",
    "author": "ISO/IEC/IEEE",
    "url": "https://www.iso.org/standard/74393.html",
    "strength": "primary",
    "use": "Stakeholders, concerns, viewpoints and decisions"
  },
  {
    "type": "official",
    "title": "AWS Well-Architected Framework",
    "author": "AWS",
    "url": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
    "strength": "primary",
    "use": "Risk review across operational pillars"
  },
  {
    "type": "book",
    "title": "Software Architecture in Practice, 4th ed.",
    "author": "Bass, Clements, Kazman",
    "reference": "Addison-Wesley, 2021, ISBN 9780136886099",
    "strength": "canonical",
    "use": "Quality-attribute scenarios and tradeoff analysis"
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
 A=load("assets/quality-attributes.json"); B=load("assets/dependency-rules.json")
 attrs=A["attributes"]; rules=B
 for k in ("availability","latency_p95_ms","rpo_minutes"):
     if k not in attrs or not isinstance(attrs[k],(int,float)): fail("missing measurable quality attribute")
 if not 0<attrs["availability"]<=100: fail("availability SLO outside percentage range")
 if attrs["latency_p95_ms"]<=0: fail("latency SLO must be positive")
 boundaries=rules["required_boundaries"]
 if len(set(boundaries))!=len(boundaries) or "domain" not in boundaries: fail("invalid boundaries")
 artifact={"kind":"architecture-decision-review","fitness_functions":[{"metric":k,"threshold":v} for k,v in attrs.items()],"dependency_guard":{"forbidden":rules["forbidden_edges"],"boundaries":boundaries},"risk_score":round((100-attrs["availability"])*10+attrs["latency_p95_ms"]/100+attrs["rpo_minutes"]/30,2)}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/quality-attributes.json","assets/dependency-rules.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
