#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: contract-lgpd-review
description: "Executa Data-Clause Trace para responder: cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?"
---

# Contract Lgpd Review

## Escopo e gatilhos

Use quando a decisão real for: **cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Data-Clause Trace**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Data-Clause Trace

1. **Partes/papéis**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Data-flow map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tabela cláusula-tema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Base/finalidade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Direitos/retention/security/subprocessors/incidents/transfers**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Redlines e perguntas.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Controller-processor matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Purpose compatibility**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Raci de incidentes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Clause-to-control trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Base legal depende de fatos. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Transferência internacional revisa mecanismo vigente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alto risco escala dpo/jurídico.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: cobertura 25, precisão jurídica 25, aderência ao fluxo 20, prioridade de risco 15, remediação 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `data_flow_mmd.md` ou formato nativo equivalente: materializa **`data-flow.mmd`** e deve ser citado pelo artefato principal.
- `clause_control_matrix_csv.md` ou formato nativo equivalente: materializa **`clause-control-matrix.csv`** e deve ser citado pelo artefato principal.
- `redline_log_md.md` ou formato nativo equivalente: materializa **`redline-log.md`** e deve ser citado pelo artefato principal.
- `missing_facts_md.md` ou formato nativo equivalente: materializa **`missing-facts.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Lei Geral de Proteção de Dados Pessoais**, Brasil (official, força: primary). Aplicação: Lawful bases, rights, actors and sanctions. Localizador: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Consulta: 2026-08-24.
2. **Guias e orientações**, ANPD (official, força: primary). Aplicação: Regulatory interpretation and controller-processor duties. Localizador: https://www.gov.br/anpd/pt-br/documentos-e-publicacoes. Consulta: 2026-08-24.
3. **ISO/IEC 27701 Privacy Information Management**, ISO/IEC (standard, força: primary). Aplicação: Operational privacy controls and evidence. Localizador: https://www.iso.org/standard/71670.html. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Data-Clause Trace

## Pergunta de controle

cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **partes/papéis** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **controller-processor matrix** responde à pergunta sem extrapolar o dado? Se não, selecione **clause-to-control trace.** e declare a troca.
3. Há uma destas exceções: base legal depende de fatos; transferência internacional revisa mecanismo vigente; alto risco escala DPO/jurídico.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Partes/papéis**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Data-flow map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tabela cláusula-tema**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Base/finalidade**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Direitos/retention/security/subprocessors/incidents/transfers**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gaps**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Redlines e perguntas.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Controller-processor matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Purpose compatibility**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Raci de incidentes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Clause-to-control trace.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Base legal depende de fatos. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Transferência internacional revisa mecanismo vigente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Alto risco escala dpo/jurídico.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “data-flow map” cita evidência identificada, aplica “controller-processor matrix”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Data-Clause Trace foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `data_flow_mmd.md` ou formato nativo equivalente: materializa **`data-flow.mmd`** e deve ser citado pelo artefato principal.
- `clause_control_matrix_csv.md` ou formato nativo equivalente: materializa **`clause-control-matrix.csv`** e deve ser citado pelo artefato principal.
- `redline_log_md.md` ou formato nativo equivalente: materializa **`redline-log.md`** e deve ser citado pelo artefato principal.
- `missing_facts_md.md` ou formato nativo equivalente: materializa **`missing-facts.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: cobertura 25, precisão jurídica 25, aderência ao fluxo 20, prioridade de risco 15, remediação 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Lei Geral de Proteção de Dados Pessoais**, Brasil (official, força: primary). Aplicação: Lawful bases, rights, actors and sanctions. Localizador: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Consulta: 2026-08-24.
2. **Guias e orientações**, ANPD (official, força: primary). Aplicação: Regulatory interpretation and controller-processor duties. Localizador: https://www.gov.br/anpd/pt-br/documentos-e-publicacoes. Consulta: 2026-08-24.
3. **ISO/IEC 27701 Privacy Information Management**, ISO/IEC (standard, força: primary). Aplicação: Operational privacy controls and evidence. Localizador: https://www.iso.org/standard/71670.html. Consulta: 2026-08-24.


# Template — Data-Clause Trace

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Partes/papéis

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Data-flow map

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Tabela cláusula-tema

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Base/finalidade

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Direitos/retention/security/subprocessors/incidents/transfers

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Gaps

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Redlines e perguntas.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Data-Clause Trace

### `data-flow.mmd`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `clause-control-matrix.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `redline-log.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `missing-facts.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

cobertura 25, precisão jurídica 25, aderência ao fluxo 20, prioridade de risco 15, remediação 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `base legal depende de fatos; transferência internacional revisa mecanismo vigente; alto risco escala DPO/jurídico.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "clauses": [
    {
      "id": "purpose",
      "required": true
    },
    {
      "id": "retention",
      "required": true
    },
    {
      "id": "incident",
      "required": true
    },
    {
      "id": "subprocessor",
      "required": true
    }
  ]
}


{
  "controls": [
    {
      "id": "LGPD-07",
      "article": "art. 7º",
      "requirement": "base legal explícita"
    },
    {
      "id": "LGPD-46",
      "article": "art. 46",
      "requirement": "medidas de segurança"
    }
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Data-Clause Trace",
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
        "partes_pap_is",
        "data_flow_map",
        "tabela_cl_usula_tema",
        "base_finalidade",
        "direitos_retention_security_subprocessors_incidents_transfers",
        "gaps",
        "redlines_e_perguntas"
      ],
      "properties": {
        "partes_pap_is": {
          "type": "string",
          "minLength": 3
        },
        "data_flow_map": {
          "type": "string",
          "minLength": 3
        },
        "tabela_cl_usula_tema": {
          "type": "string",
          "minLength": 3
        },
        "base_finalidade": {
          "type": "string",
          "minLength": 3
        },
        "direitos_retention_security_subprocessors_incidents_transfers": {
          "type": "string",
          "minLength": 3
        },
        "gaps": {
          "type": "string",
          "minLength": 3
        },
        "redlines_e_perguntas": {
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
    "behavior": "contract-lgpd-review:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "contract-lgpd-review:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "clause-catalog.json",
      "path": "clauses.0.id",
      "value": "purpose alternative"
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "contract-lgpd-review:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "clause-catalog.json",
      "path": "clauses.1.id",
      "value": "retention alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "lgpd-controls.json",
      "path": "controls.0.article",
      "value": ""
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "contract-lgpd-review:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "lgpd-controls.json",
      "path": "controls",
      "value": []
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "contract-lgpd-review:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "clause-catalog.json",
      "path": "clauses",
      "value": [
        {
          "id": "purpose",
          "required": true
        }
      ]
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "contract-lgpd-review:closed-failure-3"
  }
]


{
  "objective": "Executar contract-lgpd-review com evidência verificável | rejeição 1"
}


{
  "objective": "Executar contract-lgpd-review com evidência verificável | rejeição 2"
}


{
  "objective": "Executar contract-lgpd-review com evidência verificável | rejeição 3"
}


{
  "objective": "Executar contract-lgpd-review com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar contract-lgpd-review com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar contract-lgpd-review com evidência verificável | cenário executável 3"
}


## 8. contract-lgpd-review — Data-Clause Trace

- **Decisão:** cada fluxo de dados e responsabilidade contratual é lícito, necessário, claro e operacionalizável?
- **Fluxo:** partes/papéis → data-flow map → tabela cláusula-tema → base/finalidade → direitos/retention/security/subprocessors/incidents/transfers → gaps → redlines e perguntas.
- **Técnicas:** controller-processor matrix; purpose compatibility; minimization; RACI de incidentes; clause-to-control trace.
- **Exceções:** base legal depende de fatos; transferência internacional revisa mecanismo vigente; alto risco escala DPO/jurídico.
- **Rubrica:** cobertura 25, precisão jurídica 25, aderência ao fluxo 20, prioridade de risco 15, remediação 15.
- **Recursos:** `data-flow.mmd`, `clause-control-matrix.csv`, `redline-log.md`, `missing-facts.md`.


[
  {
    "type": "official",
    "title": "Lei Geral de Proteção de Dados Pessoais",
    "author": "Brasil",
    "url": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm",
    "strength": "primary",
    "use": "Lawful bases, rights, actors and sanctions"
  },
  {
    "type": "official",
    "title": "Guias e orientações",
    "author": "ANPD",
    "url": "https://www.gov.br/anpd/pt-br/documentos-e-publicacoes",
    "strength": "primary",
    "use": "Regulatory interpretation and controller-processor duties"
  },
  {
    "type": "standard",
    "title": "ISO/IEC 27701 Privacy Information Management",
    "author": "ISO/IEC",
    "url": "https://www.iso.org/standard/71670.html",
    "strength": "primary",
    "use": "Operational privacy controls and evidence"
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
 A=load("assets/lgpd-controls.json"); B=load("assets/clause-catalog.json")
 controls={x["id"]:x for x in A["controls"]}; clauses=B["clauses"]
 if len(controls)<2: fail("LGPD control catalog too small")
 if any(not x.get("article") for x in controls.values()): fail("LGPD control missing article citation")
 required=[c["id"] for c in clauses if c.get("required")]
 if len(required)<4: fail("clause catalog insufficient")
 findings=[{"clause":c,"severity":"high" if c in ("purpose","incident") else "medium","legal_basis":[x["article"] for x in controls.values()]} for c in required]
 artifact={"kind":"lgpd-contract-review","mandatory_clauses":required,"control_map":controls,"findings_template":findings,"disclaimer":"Revisão técnica; decisão jurídica exige profissional habilitado."}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/lgpd-controls.json","assets/clause-catalog.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
