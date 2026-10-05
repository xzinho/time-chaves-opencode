#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: api-testing
description: "Executa Contract-State-Oracles para responder: que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?"
---

# Api Testing

## Escopo e gatilhos

Use quando a decisão real for: **que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Contract-State-Oracles**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Contract-State-Oracles

1. **Importar spec**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Inventariar operações/auth/estados**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Validar schema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Partitions e boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sequências stateful**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Negative/security**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Timeout/idempotency/retry**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Relatório de evidência.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Equivalence partitioning**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pairwise**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Property-based generation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metamorphic invariants**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consumer contract**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State model.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Endpoint não idempotente usa sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Eventual consistency usa polling limitado. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Api sem spec gera shadow contract marcado como inferido.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cobertura de risco 25, qualidade de oráculo 25, determinismo 15, negativos 15, estado 10, evidência 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `operation_inventory_json.md` ou formato nativo equivalente: materializa **`operation-inventory.json`** e deve ser citado pelo artefato principal.
- `state_machine_yaml.md` ou formato nativo equivalente: materializa **`state-machine.yaml`** e deve ser citado pelo artefato principal.
- `invariants_yaml.md` ou formato nativo equivalente: materializa **`invariants.yaml`** e deve ser citado pelo artefato principal.
- `corpus_de_payloads.md` ou formato nativo equivalente: materializa **corpus de payloads** e deve ser citado pelo artefato principal.
- `junit_report.md` ou formato nativo equivalente: materializa **JUnit report** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **OpenAPI Specification 3.1**, OpenAPI Initiative (standard, força: primary). Aplicação: Contract inventory and schema assertions. Localizador: https://spec.openapis.org/oas/v3.1.0. Consulta: 2026-08-24.
2. **RFC 9110 HTTP Semantics**, IETF (standard, força: primary). Aplicação: Status, method, caching and idempotency semantics. Localizador: https://www.rfc-editor.org/rfc/rfc9110. Consulta: 2026-08-24.
3. **Schemathesis**, Schemathesis (github, força: mature). Aplicação: Property-based tests from OpenAPI schemas. Localizador: https://github.com/schemathesis/schemathesis. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Contract-State-Oracles

## Pergunta de controle

que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **importar spec** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **equivalence partitioning** responde à pergunta sem extrapolar o dado? Se não, selecione **state model.** e declare a troca.
3. Há uma destas exceções: endpoint não idempotente usa sandbox; eventual consistency usa polling limitado; API sem spec gera shadow contract marcado como inferido.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Importar spec**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Inventariar operações/auth/estados**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Validar schema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Partitions e boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Sequências stateful**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Negative/security**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Timeout/idempotency/retry**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Relatório de evidência.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Equivalence partitioning**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pairwise**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Property-based generation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metamorphic invariants**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Consumer contract**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State model.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Endpoint não idempotente usa sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Eventual consistency usa polling limitado. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Api sem spec gera shadow contract marcado como inferido.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “inventariar operações/auth/estados” cita evidência identificada, aplica “equivalence partitioning”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Contract-State-Oracles foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `operation_inventory_json.md` ou formato nativo equivalente: materializa **`operation-inventory.json`** e deve ser citado pelo artefato principal.
- `state_machine_yaml.md` ou formato nativo equivalente: materializa **`state-machine.yaml`** e deve ser citado pelo artefato principal.
- `invariants_yaml.md` ou formato nativo equivalente: materializa **`invariants.yaml`** e deve ser citado pelo artefato principal.
- `corpus_de_payloads.md` ou formato nativo equivalente: materializa **corpus de payloads** e deve ser citado pelo artefato principal.
- `junit_report.md` ou formato nativo equivalente: materializa **JUnit report** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: cobertura de risco 25, qualidade de oráculo 25, determinismo 15, negativos 15, estado 10, evidência 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **OpenAPI Specification 3.1**, OpenAPI Initiative (standard, força: primary). Aplicação: Contract inventory and schema assertions. Localizador: https://spec.openapis.org/oas/v3.1.0. Consulta: 2026-08-24.
2. **RFC 9110 HTTP Semantics**, IETF (standard, força: primary). Aplicação: Status, method, caching and idempotency semantics. Localizador: https://www.rfc-editor.org/rfc/rfc9110. Consulta: 2026-08-24.
3. **Schemathesis**, Schemathesis (github, força: mature). Aplicação: Property-based tests from OpenAPI schemas. Localizador: https://github.com/schemathesis/schemathesis. Consulta: 2026-08-24.


# Template — Contract-State-Oracles

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Importar spec

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Inventariar operações/auth/estados

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Validar schema

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Partitions e boundaries

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Sequências stateful

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Negative/security

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Timeout/idempotency/retry

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Relatório de evidência.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Contract-State-Oracles

### `operation-inventory.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `state-machine.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `invariants.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### corpus de payloads

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### JUnit report

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

cobertura de risco 25, qualidade de oráculo 25, determinismo 15, negativos 15, estado 10, evidência 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `endpoint não idempotente usa sandbox; eventual consistency usa polling limitado; API sem spec gera shadow contract marcado como inferido.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "endpoints": [
    {
      "method": "GET",
      "path": "/users/{id}",
      "expected_status": 200,
      "required_response": [
        "id",
        "email"
      ]
    }
  ]
}


{
  "allowed_methods": [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE"
  ],
  "success_status": [
    200,
    201,
    204
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Contract-State-Oracles",
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
        "importar_spec",
        "inventariar_opera_es_auth_estados",
        "validar_schema",
        "partitions_e_boundaries",
        "sequ_ncias_stateful",
        "negative_security",
        "timeout_idempotency_retry",
        "relat_rio_de_evid_ncia"
      ],
      "properties": {
        "importar_spec": {
          "type": "string",
          "minLength": 3
        },
        "inventariar_opera_es_auth_estados": {
          "type": "string",
          "minLength": 3
        },
        "validar_schema": {
          "type": "string",
          "minLength": 3
        },
        "partitions_e_boundaries": {
          "type": "string",
          "minLength": 3
        },
        "sequ_ncias_stateful": {
          "type": "string",
          "minLength": 3
        },
        "negative_security": {
          "type": "string",
          "minLength": 3
        },
        "timeout_idempotency_retry": {
          "type": "string",
          "minLength": 3
        },
        "relat_rio_de_evid_ncia": {
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
    "behavior": "api-testing:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "api-testing:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "endpoint-contracts.json",
      "path": "endpoints.0.expected_status",
      "value": 201
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "api-testing:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "endpoint-contracts.json",
      "path": "endpoints.0.required_response.0",
      "value": "id alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "endpoint-contracts.json",
      "path": "endpoints.0.method",
      "value": "TRACE"
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "api-testing:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "endpoint-contracts.json",
      "path": "endpoints.0.path",
      "value": "users"
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "api-testing:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "endpoint-contracts.json",
      "path": "endpoints.0.expected_status",
      "value": 500
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "api-testing:closed-failure-3"
  }
]


{
  "objective": "Executar api-testing com evidência verificável | rejeição 1"
}


{
  "objective": "Executar api-testing com evidência verificável | rejeição 2"
}


{
  "objective": "Executar api-testing com evidência verificável | rejeição 3"
}


{
  "objective": "Executar api-testing com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar api-testing com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar api-testing com evidência verificável | cenário executável 3"
}


## 2. api-testing — Contract-State-Oracles

- **Decisão:** que riscos de contrato, semântica, estado, segurança e resiliência precisam de oráculo?
- **Fluxo:** importar spec → inventariar operações/auth/estados → validar schema → partitions e boundaries → sequências stateful → negative/security → timeout/idempotency/retry → relatório de evidência.
- **Técnicas:** equivalence partitioning; pairwise; property-based generation; metamorphic invariants; consumer contract; state model.
- **Exceções:** endpoint não idempotente usa sandbox; eventual consistency usa polling limitado; API sem spec gera shadow contract marcado como inferido.
- **Rubrica:** cobertura de risco 25, qualidade de oráculo 25, determinismo 15, negativos 15, estado 10, evidência 10.
- **Recursos:** `operation-inventory.json`, `state-machine.yaml`, `invariants.yaml`, corpus de payloads e JUnit report.


[
  {
    "type": "standard",
    "title": "OpenAPI Specification 3.1",
    "author": "OpenAPI Initiative",
    "url": "https://spec.openapis.org/oas/v3.1.0",
    "strength": "primary",
    "use": "Contract inventory and schema assertions"
  },
  {
    "type": "standard",
    "title": "RFC 9110 HTTP Semantics",
    "author": "IETF",
    "url": "https://www.rfc-editor.org/rfc/rfc9110",
    "strength": "primary",
    "use": "Status, method, caching and idempotency semantics"
  },
  {
    "type": "github",
    "title": "Schemathesis",
    "author": "Schemathesis",
    "url": "https://github.com/schemathesis/schemathesis",
    "strength": "mature",
    "use": "Property-based tests from OpenAPI schemas"
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
 A=load("assets/endpoint-contracts.json"); B=load("assets/status-policy.json")
 contracts=A["endpoints"]; policy=B
 results=[]
 for e in contracts:
     method=e.get("method"); path=e.get("path"); status=e.get("expected_status")
     if method not in policy["allowed_methods"]: fail("HTTP method not allowed")
     if not isinstance(path,str) or not path.startswith("/"): fail("endpoint path must be absolute")
     if "{" in path and "}" not in path: fail("unbalanced path parameter")
     if status not in policy["success_status"]: fail("unexpected success status")
     required=e.get("required_response",[])
     if not required or len(required)!=len(set(required)): fail("response fields required and unique")
     results.append({"request":method+" "+path,"assert":{"status":status,"required_fields":required}})
 artifact={"kind":"api-test-plan","cases":results,"coverage":{"endpoints":len(results),"methods":len(set(x["method"] for x in contracts))}}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/endpoint-contracts.json","assets/status-policy.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
