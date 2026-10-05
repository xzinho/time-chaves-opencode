#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: visual-design-system
description: "Executa Token-Component-Governance para responder: what shared rules reduce inconsistency while enabling branded product expression?"
---

# Visual Design System

## Escopo e gatilhos

Use quando a decisão real for: **what shared rules reduce inconsistency while enabling branded product expression?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Token-Component-Governance**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Token-Component-Governance

1. **Product audit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Principles**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Primitive/semantic/component tokens**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Component anatomy/states**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Documentation/examples**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Versioning/contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Adoption metrics.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Token aliases**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant constraints**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contrast/focus tests**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual regression**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deprecation policy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- One-off signature component needs rationale. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Brand token never bypasses contrast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Breaking token has migration path.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: coherence 20, coverage 20, accessibility 20, implementation 20, governance/adoption 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `tokens_json.md` ou formato nativo equivalente: materializa **`tokens.json`** e deve ser citado pelo artefato principal.
- `component_contract_schema_json.md` ou formato nativo equivalente: materializa **`component-contract.schema.json`** e deve ser citado pelo artefato principal.
- `state_matrix_csv.md` ou formato nativo equivalente: materializa **`state-matrix.csv`** e deve ser citado pelo artefato principal.
- `migration_changelog_and_visual_fixtures.md` ou formato nativo equivalente: materializa **migration/changelog and visual fixtures** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Design Tokens Format Module 2025.10**, W3C Design Tokens Community Group (official, força: primary). Aplicação: Portable token names, types and references. Localizador: https://www.designtokens.org/tr/drafts/format/. Consulta: 2026-08-24.
2. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Accessible component and color constraints. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.
3. **Atomic Design**, Brad Frost (book, força: canonical). Aplicação: Component hierarchy and system governance. Localizador: https://atomicdesign.bradfrost.com/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Token-Component-Governance

## Pergunta de controle

what shared rules reduce inconsistency while enabling branded product expression?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **product audit** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **token aliases** responde à pergunta sem extrapolar o dado? Se não, selecione **deprecation policy.** e declare a troca.
3. Há uma destas exceções: one-off signature component needs rationale; brand token never bypasses contrast; breaking token has migration path.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what shared rules reduce inconsistency while enabling branded product expression?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Product audit**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Principles**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Primitive/semantic/component tokens**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Component anatomy/states**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Documentation/examples**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Versioning/contribution**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Adoption metrics.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Token aliases**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **State matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant constraints**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Contrast/focus tests**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual regression**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Deprecation policy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- One-off signature component needs rationale. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Brand token never bypasses contrast. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Breaking token has migration path.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “principles” cita evidência identificada, aplica “token aliases”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Token-Component-Governance foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `tokens_json.md` ou formato nativo equivalente: materializa **`tokens.json`** e deve ser citado pelo artefato principal.
- `component_contract_schema_json.md` ou formato nativo equivalente: materializa **`component-contract.schema.json`** e deve ser citado pelo artefato principal.
- `state_matrix_csv.md` ou formato nativo equivalente: materializa **`state-matrix.csv`** e deve ser citado pelo artefato principal.
- `migration_changelog_and_visual_fixtures.md` ou formato nativo equivalente: materializa **migration/changelog and visual fixtures** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: coherence 20, coverage 20, accessibility 20, implementation 20, governance/adoption 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Design Tokens Format Module 2025.10**, W3C Design Tokens Community Group (official, força: primary). Aplicação: Portable token names, types and references. Localizador: https://www.designtokens.org/tr/drafts/format/. Consulta: 2026-08-24.
2. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Accessible component and color constraints. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.
3. **Atomic Design**, Brad Frost (book, força: canonical). Aplicação: Component hierarchy and system governance. Localizador: https://atomicdesign.bradfrost.com/. Consulta: 2026-08-24.


# Template — Token-Component-Governance

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | what shared rules reduce inconsistency while enabling branded product expression? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Product audit

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Principles

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Primitive/semantic/component tokens

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Component anatomy/states

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Accessibility

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Documentation/examples

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Versioning/contribution

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Adoption metrics.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Token-Component-Governance

### `tokens.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `component-contract.schema.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `state-matrix.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### migration/changelog and visual fixtures

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

coherence 20, coverage 20, accessibility 20, implementation 20, governance/adoption 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `one-off signature component needs rationale; brand token never bypasses contrast; breaking token has migration path.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "states": [
    "default",
    "hover",
    "focus",
    "disabled",
    "error"
  ]
}


{
  "groups": [
    "color",
    "type",
    "space",
    "radius",
    "shadow"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Token-Component-Governance",
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
        "product_audit",
        "principles",
        "primitive_semantic_component_tokens",
        "component_anatomy_states",
        "accessibility",
        "documentation_examples",
        "versioning_contribution",
        "adoption_metrics"
      ],
      "properties": {
        "product_audit": {
          "type": "string",
          "minLength": 3
        },
        "principles": {
          "type": "string",
          "minLength": 3
        },
        "primitive_semantic_component_tokens": {
          "type": "string",
          "minLength": 3
        },
        "component_anatomy_states": {
          "type": "string",
          "minLength": 3
        },
        "accessibility": {
          "type": "string",
          "minLength": 3
        },
        "documentation_examples": {
          "type": "string",
          "minLength": 3
        },
        "versioning_contribution": {
          "type": "string",
          "minLength": 3
        },
        "adoption_metrics": {
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
    "behavior": "visual-design-system:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "visual-design-system:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "visual-design-system:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "token groups incomplete"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "component set too small"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "component states incomplete"
  }
]


{
  "tokens": {
    "type": {},
    "space": {},
    "radius": {},
    "shadow": {}
  },
  "components": [
    {
      "name": "Button",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "color"
      ]
    },
    {
      "name": "Input",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "space"
      ]
    }
  ]
}


{
  "tokens": {
    "color": {},
    "type": {},
    "space": {},
    "radius": {},
    "shadow": {}
  },
  "components": []
}


{
  "tokens": {
    "color": {},
    "type": {},
    "space": {},
    "radius": {},
    "shadow": {}
  },
  "components": [
    {
      "name": "Button",
      "states": [],
      "token_refs": [
        "color"
      ]
    },
    {
      "name": "Input",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "space"
      ]
    }
  ]
}


{
  "tokens": {
    "color": {},
    "type": {},
    "space": {},
    "radius": {},
    "shadow": {}
  },
  "components": [
    {
      "name": "Button",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "color"
      ]
    },
    {
      "name": "Input",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "space"
      ]
    }
  ]
}


{
  "tokens": {
    "color": {},
    "type": {},
    "space": {},
    "radius": {},
    "shadow": {}
  },
  "components": [
    {
      "name": "SecondaryButton",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "color"
      ]
    },
    {
      "name": "Input",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "space"
      ]
    }
  ]
}


{
  "tokens": {
    "color": {},
    "type": {},
    "space": {},
    "radius": {},
    "shadow": {}
  },
  "components": [
    {
      "name": "Button",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "color"
      ]
    },
    {
      "name": "SearchInput",
      "states": [
        "default",
        "hover",
        "focus",
        "disabled",
        "error"
      ],
      "token_refs": [
        "space"
      ]
    }
  ]
}


## 36. visual-design-system — Token-Component-Governance

- **Decisão:** what shared rules reduce inconsistency while enabling branded product expression?
- **Fluxo:** product audit → principles → primitive/semantic/component tokens → component anatomy/states → accessibility → documentation/examples → versioning/contribution → adoption metrics.
- **Técnicas:** token aliases; state matrix; variant constraints; contrast/focus tests; visual regression; deprecation policy.
- **Exceções:** one-off signature component needs rationale; brand token never bypasses contrast; breaking token has migration path.
- **Rubrica:** coherence 20, coverage 20, accessibility 20, implementation 20, governance/adoption 20.
- **Recursos:** `tokens.json`, `component-contract.schema.json`, `state-matrix.csv`, migration/changelog and visual fixtures.


[
  {
    "type": "official",
    "title": "Design Tokens Format Module 2025.10",
    "author": "W3C Design Tokens Community Group",
    "url": "https://www.designtokens.org/tr/drafts/format/",
    "strength": "primary",
    "use": "Portable token names, types and references"
  },
  {
    "type": "official",
    "title": "Web Content Accessibility Guidelines 2.2",
    "author": "W3C",
    "url": "https://www.w3.org/TR/WCAG22/",
    "strength": "primary",
    "use": "Accessible component and color constraints"
  },
  {
    "type": "book",
    "title": "Atomic Design",
    "author": "Brad Frost",
    "url": "https://atomicdesign.bradfrost.com/",
    "strength": "canonical",
    "use": "Component hierarchy and system governance"
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
    tokens=data.get('tokens'); components=data.get('components')
    if not isinstance(tokens,dict) or set(assets['token-schema']['groups'])-set(tokens): fail('token groups incomplete')
    if not isinstance(components,list) or len(components)<2: fail('component set too small')
    names=set(); audited=[]
    for c in components:
        name=req(c,'name')
        if name in names: fail('duplicate component')
        names.add(name); states=set(c.get('states',[]))
        if set(assets['component-states']['states'])-states: fail('component states incomplete')
        if any(ref not in tokens for ref in c.get('token_refs',[])): fail('unknown token reference')
        audited.append({'name':name,'states':len(states)})
    return {'token_groups':len(tokens),'components':audited,'coverage':'complete'}
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
