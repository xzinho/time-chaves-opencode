#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: diagram-maker
description: "Executa Notation-Semantics Pipeline para responder: qual notação responde à pergunta e que regras impedem ambiguidade?"
---

# Diagram Maker

## Escopo e gatilhos

Use quando a decisão real for: **qual notação responde à pergunta e que regras impedem ambiguidade?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Notation-Semantics Pipeline**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Notation-Semantics Pipeline

1. **Audiência/pergunta**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Selecionar bpmn/uml/c4/flow/er**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Definir grammar**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Modelar happy path**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Exceptions**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Lint semântico**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Render**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Legenda e source.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Consistent direction**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Crossing minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic shapes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Explicit boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Exception paths**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Diagram lint.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Misturar notações só com legenda. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bpmn sem eventos não vira flowchart decorativo. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Informação sensível é sanitizada.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: semântica 30, completude 20, legibilidade 20, consistência 15, editabilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `notation_decision_tree_yaml.md` ou formato nativo equivalente: materializa **`notation-decision-tree.yaml`** e deve ser citado pelo artefato principal.
- `diagram_source.md` ou formato nativo equivalente: materializa **`diagram-source`** e deve ser citado pelo artefato principal.
- `lint_rules_yaml.md` ou formato nativo equivalente: materializa **`lint-rules.yaml`** e deve ser citado pelo artefato principal.
- `legend_md.md` ou formato nativo equivalente: materializa **`legend.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **BPMN 2.0.2**, Object Management Group (standard, força: primary). Aplicação: Process-event-gateway semantics. Localizador: https://www.omg.org/spec/BPMN/2.0.2/. Consulta: 2026-08-24.
2. **UML 2.5.1**, Object Management Group (standard, força: primary). Aplicação: Structural and behavioral diagram semantics. Localizador: https://www.omg.org/spec/UML/2.5.1/. Consulta: 2026-08-24.
3. **Mermaid**, Mermaid (github, força: mature). Aplicação: Text-source diagrams with deterministic rendering. Localizador: https://github.com/mermaid-js/mermaid. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Notation-Semantics Pipeline

## Pergunta de controle

qual notação responde à pergunta e que regras impedem ambiguidade?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **audiência/pergunta** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **consistent direction** responde à pergunta sem extrapolar o dado? Se não, selecione **diagram lint.** e declare a troca.
3. Há uma destas exceções: misturar notações só com legenda; BPMN sem eventos não vira flowchart decorativo; informação sensível é sanitizada.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual notação responde à pergunta e que regras impedem ambiguidade?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Audiência/pergunta**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Selecionar bpmn/uml/c4/flow/er**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Definir grammar**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Modelar happy path**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Exceptions**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Lint semântico**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Render**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Legenda e source.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Consistent direction**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Crossing minimization**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Semantic shapes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Explicit boundaries**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Exception paths**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Diagram lint.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Misturar notações só com legenda. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bpmn sem eventos não vira flowchart decorativo. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Informação sensível é sanitizada.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “selecionar BPMN/UML/C4/flow/ER” cita evidência identificada, aplica “consistent direction”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Notation-Semantics Pipeline foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `notation_decision_tree_yaml.md` ou formato nativo equivalente: materializa **`notation-decision-tree.yaml`** e deve ser citado pelo artefato principal.
- `diagram_source.md` ou formato nativo equivalente: materializa **`diagram-source`** e deve ser citado pelo artefato principal.
- `lint_rules_yaml.md` ou formato nativo equivalente: materializa **`lint-rules.yaml`** e deve ser citado pelo artefato principal.
- `legend_md.md` ou formato nativo equivalente: materializa **`legend.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: semântica 30, completude 20, legibilidade 20, consistência 15, editabilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **BPMN 2.0.2**, Object Management Group (standard, força: primary). Aplicação: Process-event-gateway semantics. Localizador: https://www.omg.org/spec/BPMN/2.0.2/. Consulta: 2026-08-24.
2. **UML 2.5.1**, Object Management Group (standard, força: primary). Aplicação: Structural and behavioral diagram semantics. Localizador: https://www.omg.org/spec/UML/2.5.1/. Consulta: 2026-08-24.
3. **Mermaid**, Mermaid (github, força: mature). Aplicação: Text-source diagrams with deterministic rendering. Localizador: https://github.com/mermaid-js/mermaid. Consulta: 2026-08-24.


# Template — Notation-Semantics Pipeline

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual notação responde à pergunta e que regras impedem ambiguidade? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Audiência/pergunta

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Selecionar bpmn/uml/c4/flow/er

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Definir grammar

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Modelar happy path

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Exceptions

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Lint semântico

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Render

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Legenda e source.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Notation-Semantics Pipeline

### `notation-decision-tree.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `diagram-source`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `lint-rules.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `legend.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

semântica 30, completude 20, legibilidade 20, consistência 15, editabilidade 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `misturar notações só com legenda; BPMN sem eventos não vira flowchart decorativo; informação sensível é sanitizada.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "max_label": 60,
  "min_contrast": 4.5
}


{
  "types": {
    "flow": [
      "start",
      "process",
      "decision",
      "end"
    ],
    "sequence": [
      "actor",
      "message"
    ]
  }
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Notation-Semantics Pipeline",
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
        "audi_ncia_pergunta",
        "selecionar_bpmn_uml_c4_flow_er",
        "definir_grammar",
        "modelar_happy_path",
        "exceptions",
        "lint_sem_ntico",
        "render",
        "legenda_e_source"
      ],
      "properties": {
        "audi_ncia_pergunta": {
          "type": "string",
          "minLength": 3
        },
        "selecionar_bpmn_uml_c4_flow_er": {
          "type": "string",
          "minLength": 3
        },
        "definir_grammar": {
          "type": "string",
          "minLength": 3
        },
        "modelar_happy_path": {
          "type": "string",
          "minLength": 3
        },
        "exceptions": {
          "type": "string",
          "minLength": 3
        },
        "lint_sem_ntico": {
          "type": "string",
          "minLength": 3
        },
        "render": {
          "type": "string",
          "minLength": 3
        },
        "legenda_e_source": {
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
    "behavior": "diagram-maker:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "diagram-maker:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "diagram-maker:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "unsupported diagram type"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "elements required"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "dangling link"
  }
]


{
  "type": "bad",
  "elements": [
    {
      "kind": "start",
      "id": "a",
      "label": "Início"
    },
    {
      "kind": "process",
      "id": "b",
      "label": "Validar"
    },
    {
      "kind": "end",
      "id": "c",
      "label": "Fim"
    }
  ],
  "links": [
    {
      "from": "a",
      "to": "b"
    },
    {
      "from": "b",
      "to": "c"
    }
  ]
}


{
  "type": "flow",
  "elements": [],
  "links": [
    {
      "from": "a",
      "to": "b"
    },
    {
      "from": "b",
      "to": "c"
    }
  ]
}


{
  "type": "flow",
  "elements": [
    {
      "kind": "start",
      "id": "a",
      "label": "Início"
    },
    {
      "kind": "process",
      "id": "b",
      "label": "Validar"
    },
    {
      "kind": "end",
      "id": "c",
      "label": "Fim"
    }
  ],
  "links": [
    {
      "from": "a",
      "to": "missing"
    },
    {
      "from": "b",
      "to": "c"
    }
  ]
}


{
  "type": "flow",
  "elements": [
    {
      "kind": "start",
      "id": "a",
      "label": "Início"
    },
    {
      "kind": "process",
      "id": "b",
      "label": "Validar"
    },
    {
      "kind": "end",
      "id": "c",
      "label": "Fim"
    }
  ],
  "links": [
    {
      "from": "a",
      "to": "b"
    },
    {
      "from": "b",
      "to": "c"
    }
  ]
}


{
  "type": "flow",
  "elements": [
    {
      "kind": "start",
      "id": "a",
      "label": "Início"
    },
    {
      "kind": "process",
      "id": "b",
      "label": "Executar controle"
    },
    {
      "kind": "end",
      "id": "c",
      "label": "Fim"
    }
  ],
  "links": [
    {
      "from": "a",
      "to": "b"
    },
    {
      "from": "b",
      "to": "c"
    }
  ]
}


{
  "type": "flow",
  "elements": [
    {
      "kind": "start",
      "id": "a",
      "label": "Início"
    },
    {
      "kind": "process",
      "id": "b",
      "label": "Validar"
    },
    {
      "kind": "end",
      "id": "c",
      "label": "Fim"
    }
  ],
  "links": [
    {
      "from": "a",
      "to": "c"
    }
  ]
}


## 13. diagram-maker — Notation-Semantics Pipeline

- **Decisão:** qual notação responde à pergunta e que regras impedem ambiguidade?
- **Fluxo:** audiência/pergunta → selecionar BPMN/UML/C4/flow/ER → definir grammar → modelar happy path → exceptions → lint semântico → render → legenda e source.
- **Técnicas:** consistent direction; crossing minimization; semantic shapes; explicit boundaries; exception paths; diagram lint.
- **Exceções:** misturar notações só com legenda; BPMN sem eventos não vira flowchart decorativo; informação sensível é sanitizada.
- **Rubrica:** semântica 30, completude 20, legibilidade 20, consistência 15, editabilidade 15.
- **Recursos:** `notation-decision-tree.yaml`, `diagram-source`, `lint-rules.yaml`, `legend.md`.


[
  {
    "type": "standard",
    "title": "BPMN 2.0.2",
    "author": "Object Management Group",
    "url": "https://www.omg.org/spec/BPMN/2.0.2/",
    "strength": "primary",
    "use": "Process-event-gateway semantics"
  },
  {
    "type": "standard",
    "title": "UML 2.5.1",
    "author": "Object Management Group",
    "url": "https://www.omg.org/spec/UML/2.5.1/",
    "strength": "primary",
    "use": "Structural and behavioral diagram semantics"
  },
  {
    "type": "github",
    "title": "Mermaid",
    "author": "Mermaid",
    "url": "https://github.com/mermaid-js/mermaid",
    "strength": "mature",
    "use": "Text-source diagrams with deterministic rendering"
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
    kind=req(data,'type'); grammar=assets['grammar']['types']
    if kind not in grammar: fail('unsupported diagram type')
    elements=data.get('elements');
    if not isinstance(elements,list) or not elements: fail('elements required')
    valid=set(grammar[kind]); ids=set()
    for el in elements:
        if req(el,'kind') not in valid: fail('invalid element for diagram')
        if len(req(el,'label'))>assets['accessibility']['max_label']: fail('label too long')
        if req(el,'id') in ids: fail('duplicate element id')
        ids.add(el['id'])
    links=data.get('links',[])
    if any(l.get('from') not in ids or l.get('to') not in ids for l in links): fail('dangling link')
    return {'type':kind,'element_count':len(elements),'link_count':len(links),'render_spec':{'elements':elements,'links':links}}
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
