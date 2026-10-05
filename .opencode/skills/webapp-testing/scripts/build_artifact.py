#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: webapp-testing
description: "Executa Risk-Journey-Evidence Suite para responder: which user-visible failures and quality risks must be prevented before release?"
---

# Webapp Testing

## Escopo e gatilhos

Use quando a decisão real for: **which user-visible failures and quality risks must be prevented before release?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Risk-Journey-Evidence Suite**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Risk-Journey-Evidence Suite

1. **Scope/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Critical journeys**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **States/fixtures**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Functional tests**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Error/loading/empty/responsive**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Visual/performance/security-adjacent checks**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Flaky-test controls**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Evidence/gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Role/test-id locators**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Isolated context**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deterministic seed**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Network mocking boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Screenshot diff**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keyboard/screen-reader checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Trace/video on retry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Captcha/payment/email require approved sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Flaky test is quarantined with owner/date, not silently retried forever. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Visual diff has tolerance rationale.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: risk coverage 25, assertion quality 20, determinism 20, state coverage 15, accessibility 10, evidence 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `journey_risk_map_csv.md` ou formato nativo equivalente: materializa **`journey-risk-map.csv`** e deve ser citado pelo artefato principal.
- `fixture_contract_json.md` ou formato nativo equivalente: materializa **`fixture-contract.json`** e deve ser citado pelo artefato principal.
- `playwright_project.md` ou formato nativo equivalente: materializa **Playwright project** e deve ser citado pelo artefato principal.
- `accessibility_report.md` ou formato nativo equivalente: materializa **accessibility report** e deve ser citado pelo artefato principal.
- `trace_screenshot_bundle.md` ou formato nativo equivalente: materializa **trace/screenshot bundle** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **WebDriver W3C Recommendation**, W3C (standard, força: primary). Aplicação: Browser automation semantics. Localizador: https://www.w3.org/TR/webdriver2/. Consulta: 2026-08-24.
2. **Playwright Best Practices**, Microsoft (official, força: primary). Aplicação: User-visible locators, isolation and resilient assertions. Localizador: https://playwright.dev/docs/best-practices. Consulta: 2026-08-24.
3. **WCAG Evaluation Methodology 1.0**, W3C (official, força: primary). Aplicação: Accessibility test scope, sampling and reporting. Localizador: https://www.w3.org/TR/WCAG-EM/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Risk-Journey-Evidence Suite

## Pergunta de controle

which user-visible failures and quality risks must be prevented before release?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **scope/risk** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **role/test-id locators** responde à pergunta sem extrapolar o dado? Se não, selecione **trace/video on retry.** e declare a troca.
3. Há uma destas exceções: CAPTCHA/payment/email require approved sandbox; flaky test is quarantined with owner/date, not silently retried forever; visual diff has tolerance rationale.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **which user-visible failures and quality risks must be prevented before release?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Scope/risk**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Critical journeys**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **States/fixtures**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Functional tests**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Error/loading/empty/responsive**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Visual/performance/security-adjacent checks**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Flaky-test controls**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Evidence/gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Role/test-id locators**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Isolated context**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deterministic seed**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Network mocking boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Screenshot diff**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keyboard/screen-reader checks**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Trace/video on retry.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Captcha/payment/email require approved sandbox. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Flaky test is quarantined with owner/date, not silently retried forever. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Visual diff has tolerance rationale.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “critical journeys” cita evidência identificada, aplica “role/test-id locators”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Risk-Journey-Evidence Suite foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `journey_risk_map_csv.md` ou formato nativo equivalente: materializa **`journey-risk-map.csv`** e deve ser citado pelo artefato principal.
- `fixture_contract_json.md` ou formato nativo equivalente: materializa **`fixture-contract.json`** e deve ser citado pelo artefato principal.
- `playwright_project.md` ou formato nativo equivalente: materializa **Playwright project** e deve ser citado pelo artefato principal.
- `accessibility_report.md` ou formato nativo equivalente: materializa **accessibility report** e deve ser citado pelo artefato principal.
- `trace_screenshot_bundle.md` ou formato nativo equivalente: materializa **trace/screenshot bundle** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: risk coverage 25, assertion quality 20, determinism 20, state coverage 15, accessibility 10, evidence 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **WebDriver W3C Recommendation**, W3C (standard, força: primary). Aplicação: Browser automation semantics. Localizador: https://www.w3.org/TR/webdriver2/. Consulta: 2026-08-24.
2. **Playwright Best Practices**, Microsoft (official, força: primary). Aplicação: User-visible locators, isolation and resilient assertions. Localizador: https://playwright.dev/docs/best-practices. Consulta: 2026-08-24.
3. **WCAG Evaluation Methodology 1.0**, W3C (official, força: primary). Aplicação: Accessibility test scope, sampling and reporting. Localizador: https://www.w3.org/TR/WCAG-EM/. Consulta: 2026-08-24.


# Template — Risk-Journey-Evidence Suite

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | which user-visible failures and quality risks must be prevented before release? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Scope/risk

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Critical journeys

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. States/fixtures

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Functional tests

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Error/loading/empty/responsive

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Accessibility

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Visual/performance/security-adjacent checks

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Flaky-test controls

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Evidence/gate.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Risk-Journey-Evidence Suite

### `journey-risk-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `fixture-contract.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### Playwright project

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### accessibility report

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### trace/screenshot bundle

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

risk coverage 25, assertion quality 20, determinism 20, state coverage 15, accessibility 10, evidence 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `CAPTCHA/payment/email require approved sandbox; flaky test is quarantined with owner/date, not silently retried forever; visual diff has tolerance rationale.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "journeys": [
    {
      "name": "login",
      "steps": [
        "open /login",
        "fill email",
        "fill password",
        "submit"
      ],
      "assertions": [
        "url=/dashboard",
        "session_cookie_secure"
      ]
    }
  ]
}


{
  "required_assertion_prefixes": [
    "url=",
    "text=",
    "status=",
    "session_"
  ],
  "forbidden_steps": [
    "wait arbitrary",
    "ignore error"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Risk-Journey-Evidence Suite",
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
        "scope_risk",
        "critical_journeys",
        "states_fixtures",
        "functional_tests",
        "error_loading_empty_responsive",
        "accessibility",
        "visual_performance_security_adjacent_checks",
        "flaky_test_controls",
        "evidence_gate"
      ],
      "properties": {
        "scope_risk": {
          "type": "string",
          "minLength": 3
        },
        "critical_journeys": {
          "type": "string",
          "minLength": 3
        },
        "states_fixtures": {
          "type": "string",
          "minLength": 3
        },
        "functional_tests": {
          "type": "string",
          "minLength": 3
        },
        "error_loading_empty_responsive": {
          "type": "string",
          "minLength": 3
        },
        "accessibility": {
          "type": "string",
          "minLength": 3
        },
        "visual_performance_security_adjacent_checks": {
          "type": "string",
          "minLength": 3
        },
        "flaky_test_controls": {
          "type": "string",
          "minLength": 3
        },
        "evidence_gate": {
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
    "behavior": "webapp-testing:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "webapp-testing:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "journeys.json",
      "path": "journeys.0.name",
      "value": "login alternative"
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "webapp-testing:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "journeys.json",
      "path": "journeys.0.steps.0",
      "value": "open /login alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "journeys.json",
      "path": "journeys.0.steps",
      "value": [
        "open /login"
      ]
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "webapp-testing:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "journeys.json",
      "path": "journeys.0.assertions",
      "value": []
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "webapp-testing:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "journeys.json",
      "path": "journeys.0.steps",
      "value": [
        "wait arbitrary",
        "submit"
      ]
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "webapp-testing:closed-failure-3"
  }
]


{
  "objective": "Executar webapp-testing com evidência verificável | rejeição 1"
}


{
  "objective": "Executar webapp-testing com evidência verificável | rejeição 2"
}


{
  "objective": "Executar webapp-testing com evidência verificável | rejeição 3"
}


{
  "objective": "Executar webapp-testing com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar webapp-testing com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar webapp-testing com evidência verificável | cenário executável 3"
}


## 39. webapp-testing — Risk-Journey-Evidence Suite

- **Decisão:** which user-visible failures and quality risks must be prevented before release?
- **Fluxo:** scope/risk → critical journeys → states/fixtures → functional tests → error/loading/empty/responsive → accessibility → visual/performance/security-adjacent checks → flaky-test controls → evidence/gate.
- **Técnicas:** role/test-id locators; isolated context; deterministic seed; network mocking boundaries; screenshot diff; keyboard/screen-reader checks; trace/video on retry.
- **Exceções:** CAPTCHA/payment/email require approved sandbox; flaky test is quarantined with owner/date, not silently retried forever; visual diff has tolerance rationale.
- **Rubrica:** risk coverage 25, assertion quality 20, determinism 20, state coverage 15, accessibility 10, evidence 10.
- **Recursos:** `journey-risk-map.csv`, `fixture-contract.json`, Playwright project, accessibility report, trace/screenshot bundle.


[
  {
    "type": "standard",
    "title": "WebDriver W3C Recommendation",
    "author": "W3C",
    "url": "https://www.w3.org/TR/webdriver2/",
    "strength": "primary",
    "use": "Browser automation semantics"
  },
  {
    "type": "official",
    "title": "Playwright Best Practices",
    "author": "Microsoft",
    "url": "https://playwright.dev/docs/best-practices",
    "strength": "primary",
    "use": "User-visible locators, isolation and resilient assertions"
  },
  {
    "type": "official",
    "title": "WCAG Evaluation Methodology 1.0",
    "author": "W3C",
    "url": "https://www.w3.org/TR/WCAG-EM/",
    "strength": "primary",
    "use": "Accessibility test scope, sampling and reporting"
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
 A=load("assets/journeys.json"); B=load("assets/oracle-rules.json")
 journeys=A["journeys"]; oracle=B
 plans=[]
 for j in journeys:
     steps=j.get("steps",[]); assertions=j.get("assertions",[])
     if len(steps)<2: fail("journey requires at least two executable steps")
     if not assertions: fail("journey lacks test oracle assertions")
     if any(s in oracle["forbidden_steps"] for s in steps): fail("flaky/unsafe step")
     if any(not any(a.startswith(p) for p in oracle["required_assertion_prefixes"]) for a in assertions): fail("non-observable assertion")
     plans.append({"name":j["name"],"actions":steps,"oracles":assertions,"trace":True,"screenshot_on_failure":True})
 artifact={"kind":"webapp-e2e-plan","journeys":plans,"oracle_count":sum(len(x["oracles"]) for x in plans)}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/journeys.json","assets/oracle-rules.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
