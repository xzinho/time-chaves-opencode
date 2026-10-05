#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: security-review
description: "Executa Asset-Threat-Control-Evidence para responder: what must block release, what can be remediated, and what residual risk is accepted by whom?"
---

# Security Review

## Escopo e gatilhos

Use quando a decisão real for: **what must block release, what can be remediated, and what residual risk is accepted by whom?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Asset-Threat-Control-Evidence**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Asset-Threat-Control-Evidence

1. **Scope/data/classification**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Architecture/trust boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Threat model**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Asvs/ssdf control mapping**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code/config/runtime evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Exploitability/impact**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Remediation/retest**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Stride-like prompts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Attack path**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Misuse case**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Secret/dependency/auth/session review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence tiers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity matrix.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Scanner finding not confirmed is tentative. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Production test needs authorization. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Risk acceptance requires named authority/date.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: scope 15, threat coverage 25, evidence 25, severity 15, remediation/retest 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `threat_model_md.md` ou formato nativo equivalente: materializa **`threat-model.md`** e deve ser citado pelo artefato principal.
- `control_evidence_csv.md` ou formato nativo equivalente: materializa **`control-evidence.csv`** e deve ser citado pelo artefato principal.
- `finding_schema_json.md` ou formato nativo equivalente: materializa **`finding-schema.json`** e deve ser citado pelo artefato principal.
- `release_gate_with_owner_due_date.md` ou formato nativo equivalente: materializa **release gate with owner/due date** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **OWASP Application Security Verification Standard 4.0.3**, OWASP (official, força: primary). Aplicação: Testable application-security control baseline. Localizador: https://owasp.org/www-project-application-security-verification-standard/. Consulta: 2026-08-24.
2. **NIST Secure Software Development Framework 1.1**, NIST (official, força: primary). Aplicação: Secure-development practices and evidence. Localizador: https://csrc.nist.gov/pubs/sp/800/218/final. Consulta: 2026-08-24.
3. **Threat Modeling Playbook**, OWASP (github, força: mature). Aplicação: Practical threat-model facilitation. Localizador: https://github.com/OWASP/threat-modeling-playbook. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Asset-Threat-Control-Evidence

## Pergunta de controle

what must block release, what can be remediated, and what residual risk is accepted by whom?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **scope/data/classification** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **STRIDE-like prompts** responde à pergunta sem extrapolar o dado? Se não, selecione **severity matrix.** e declare a troca.
3. Há uma destas exceções: scanner finding not confirmed is tentative; production test needs authorization; risk acceptance requires named authority/date.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what must block release, what can be remediated, and what residual risk is accepted by whom?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Scope/data/classification**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Architecture/trust boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Threat model**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Asvs/ssdf control mapping**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code/config/runtime evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Exploitability/impact**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Remediation/retest**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Stride-like prompts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Attack path**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Misuse case**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Secret/dependency/auth/session review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence tiers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity matrix.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Scanner finding not confirmed is tentative. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Production test needs authorization. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Risk acceptance requires named authority/date.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “architecture/trust boundaries” cita evidência identificada, aplica “STRIDE-like prompts”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Asset-Threat-Control-Evidence foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `threat_model_md.md` ou formato nativo equivalente: materializa **`threat-model.md`** e deve ser citado pelo artefato principal.
- `control_evidence_csv.md` ou formato nativo equivalente: materializa **`control-evidence.csv`** e deve ser citado pelo artefato principal.
- `finding_schema_json.md` ou formato nativo equivalente: materializa **`finding-schema.json`** e deve ser citado pelo artefato principal.
- `release_gate_with_owner_due_date.md` ou formato nativo equivalente: materializa **release gate with owner/due date** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: scope 15, threat coverage 25, evidence 25, severity 15, remediation/retest 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **OWASP Application Security Verification Standard 4.0.3**, OWASP (official, força: primary). Aplicação: Testable application-security control baseline. Localizador: https://owasp.org/www-project-application-security-verification-standard/. Consulta: 2026-08-24.
2. **NIST Secure Software Development Framework 1.1**, NIST (official, força: primary). Aplicação: Secure-development practices and evidence. Localizador: https://csrc.nist.gov/pubs/sp/800/218/final. Consulta: 2026-08-24.
3. **Threat Modeling Playbook**, OWASP (github, força: mature). Aplicação: Practical threat-model facilitation. Localizador: https://github.com/OWASP/threat-modeling-playbook. Consulta: 2026-08-24.


# Template — Asset-Threat-Control-Evidence

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | what must block release, what can be remediated, and what residual risk is accepted by whom? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Scope/data/classification

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Architecture/trust boundaries

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Threat model

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Asvs/ssdf control mapping

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Code/config/runtime evidence

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Exploitability/impact

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Findings

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Remediation/retest

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Gate.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Asset-Threat-Control-Evidence

### `threat-model.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `control-evidence.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `finding-schema.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### release gate with owner/due date

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

scope 15, threat coverage 25, evidence 25, severity 15, remediation/retest 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `scanner finding not confirmed is tentative; production test needs authorization; risk acceptance requires named authority/date.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "controls": [
    {
      "id": "C01",
      "threats": [
        "T01"
      ],
      "type": "prevent",
      "evidence": "token rotation test"
    }
  ]
}


{
  "threats": [
    {
      "id": "T01",
      "asset": "session",
      "vector": "stolen token",
      "impact": 5,
      "likelihood": 4
    }
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Asset-Threat-Control-Evidence",
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
        "scope_data_classification",
        "architecture_trust_boundaries",
        "threat_model",
        "asvs_ssdf_control_mapping",
        "code_config_runtime_evidence",
        "exploitability_impact",
        "findings",
        "remediation_retest",
        "gate"
      ],
      "properties": {
        "scope_data_classification": {
          "type": "string",
          "minLength": 3
        },
        "architecture_trust_boundaries": {
          "type": "string",
          "minLength": 3
        },
        "threat_model": {
          "type": "string",
          "minLength": 3
        },
        "asvs_ssdf_control_mapping": {
          "type": "string",
          "minLength": 3
        },
        "code_config_runtime_evidence": {
          "type": "string",
          "minLength": 3
        },
        "exploitability_impact": {
          "type": "string",
          "minLength": 3
        },
        "findings": {
          "type": "string",
          "minLength": 3
        },
        "remediation_retest": {
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
    "behavior": "security-review:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "security-review:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "controls.json",
      "path": "controls.0.id",
      "value": "C01 alternative"
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "security-review:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "controls.json",
      "path": "controls.0.evidence",
      "value": "token rotation test alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "controls.json",
      "path": "controls.0.evidence",
      "value": ""
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "security-review:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "controls.json",
      "path": "controls.0.threats",
      "value": [
        "T99"
      ]
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "security-review:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "controls.json",
      "path": "controls",
      "value": []
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "security-review:closed-failure-3"
  }
]


{
  "objective": "Executar security-review com evidência verificável | rejeição 1"
}


{
  "objective": "Executar security-review com evidência verificável | rejeição 2"
}


{
  "objective": "Executar security-review com evidência verificável | rejeição 3"
}


{
  "objective": "Executar security-review com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar security-review com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar security-review com evidência verificável | cenário executável 3"
}


## 32. security-review — Asset-Threat-Control-Evidence

- **Decisão:** what must block release, what can be remediated, and what residual risk is accepted by whom?
- **Fluxo:** scope/data/classification → architecture/trust boundaries → threat model → ASVS/SSDF control mapping → code/config/runtime evidence → exploitability/impact → findings → remediation/retest → gate.
- **Técnicas:** STRIDE-like prompts; attack path; misuse case; secret/dependency/auth/session review; evidence tiers; severity matrix.
- **Exceções:** scanner finding not confirmed is tentative; production test needs authorization; risk acceptance requires named authority/date.
- **Rubrica:** scope 15, threat coverage 25, evidence 25, severity 15, remediation/retest 20.
- **Recursos:** `threat-model.md`, `control-evidence.csv`, `finding-schema.json`, release gate with owner/due date.


[
  {
    "type": "official",
    "title": "OWASP Application Security Verification Standard 4.0.3",
    "author": "OWASP",
    "url": "https://owasp.org/www-project-application-security-verification-standard/",
    "strength": "primary",
    "use": "Testable application-security control baseline"
  },
  {
    "type": "official",
    "title": "NIST Secure Software Development Framework 1.1",
    "author": "NIST",
    "url": "https://csrc.nist.gov/pubs/sp/800/218/final",
    "strength": "primary",
    "use": "Secure-development practices and evidence"
  },
  {
    "type": "github",
    "title": "Threat Modeling Playbook",
    "author": "OWASP",
    "url": "https://github.com/OWASP/threat-modeling-playbook",
    "strength": "mature",
    "use": "Practical threat-model facilitation"
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
 A=load("assets/threats.json"); B=load("assets/controls.json")
 threats={t["id"]:t for t in A["threats"]}; controls=B["controls"]
 if not threats: fail("threat model empty")
 mapped=set()
 for c in controls:
     if c.get("type") not in ("prevent","detect","respond","recover") or not str(c.get("evidence","")).strip(): fail("control lacks type or evidence")
     unknown=set(c.get("threats",[]))-set(threats)
     if unknown: fail("control maps unknown threat")
     mapped.update(c["threats"])
 if mapped!=set(threats): fail("unmitigated threats")
 artifact={"kind":"security-review","risks":[{**t,"score":t["impact"]*t["likelihood"]} for t in threats.values()],"control_mapping":controls,"residual_unmapped":[]}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/threats.json","assets/controls.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
