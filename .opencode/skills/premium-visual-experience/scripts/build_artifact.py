#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: premium-visual-experience
description: "Executa Intentional Experience Direction para responder: que estética e interação amplificam a proposta sem sacrificar usabilidade/performance?"
---

# Premium Visual Experience

## Escopo e gatilhos

Use quando a decisão real for: **que estética e interação amplificam a proposta sem sacrificar usabilidade/performance?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Intentional Experience Direction**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Intentional Experience Direction

1. **Brand/product intent**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Mood/anti-mood**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Hierarchy/rhythm**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Signature moments**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Component/motion rules**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Prototype key journeys**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Accessibility/performance**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Perceptual review.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Contrast map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual rhythm**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Focal hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Motion grammar**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Progressive complexity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Aesthetic-usability countercheck.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Reduced motion. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Low-end device budget. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dense enterprise flows prioritize scanning. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Novelty must not hide controls.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: identidade 20, hierarquia 20, craft 20, função 20, acessibilidade/performance 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `art_direction_board_md.md` ou formato nativo equivalente: materializa **`art-direction-board.md`** e deve ser citado pelo artefato principal.
- `signature_moments_yaml.md` ou formato nativo equivalente: materializa **`signature-moments.yaml`** e deve ser citado pelo artefato principal.
- `motion_tokens.md` ou formato nativo equivalente: materializa **motion tokens** e deve ser citado pelo artefato principal.
- `visual_qa_scorecard.md` ou formato nativo equivalente: materializa **visual QA scorecard** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Material Design 3**, Google (official, força: primary). Aplicação: Interaction, motion and component behavior baseline. Localizador: https://m3.material.io/. Consulta: 2026-08-24.
2. **Human Interface Guidelines**, Apple (official, força: primary). Aplicação: Platform coherence, hierarchy and feedback. Localizador: https://developer.apple.com/design/human-interface-guidelines/. Consulta: 2026-08-24.
3. **The Laws of Simplicity**, John Maeda (book, força: canonical). Aplicação: Reduction, organization and emotional quality. Localizador: MIT Press, 2006, ISBN 9780262134729. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Intentional Experience Direction

## Pergunta de controle

que estética e interação amplificam a proposta sem sacrificar usabilidade/performance?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **brand/product intent** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **contrast map** responde à pergunta sem extrapolar o dado? Se não, selecione **aesthetic-usability countercheck.** e declare a troca.
3. Há uma destas exceções: reduced motion; low-end device budget; dense enterprise flows prioritize scanning; novelty must not hide controls.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que estética e interação amplificam a proposta sem sacrificar usabilidade/performance?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Brand/product intent**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Mood/anti-mood**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Hierarchy/rhythm**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Signature moments**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Component/motion rules**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Prototype key journeys**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Accessibility/performance**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Perceptual review.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Contrast map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual rhythm**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Focal hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Motion grammar**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Progressive complexity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Aesthetic-usability countercheck.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Reduced motion. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Low-end device budget. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Dense enterprise flows prioritize scanning. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Novelty must not hide controls.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “mood/anti-mood” cita evidência identificada, aplica “contrast map”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Intentional Experience Direction foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `art_direction_board_md.md` ou formato nativo equivalente: materializa **`art-direction-board.md`** e deve ser citado pelo artefato principal.
- `signature_moments_yaml.md` ou formato nativo equivalente: materializa **`signature-moments.yaml`** e deve ser citado pelo artefato principal.
- `motion_tokens.md` ou formato nativo equivalente: materializa **motion tokens** e deve ser citado pelo artefato principal.
- `visual_qa_scorecard.md` ou formato nativo equivalente: materializa **visual QA scorecard** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: identidade 20, hierarquia 20, craft 20, função 20, acessibilidade/performance 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Material Design 3**, Google (official, força: primary). Aplicação: Interaction, motion and component behavior baseline. Localizador: https://m3.material.io/. Consulta: 2026-08-24.
2. **Human Interface Guidelines**, Apple (official, força: primary). Aplicação: Platform coherence, hierarchy and feedback. Localizador: https://developer.apple.com/design/human-interface-guidelines/. Consulta: 2026-08-24.
3. **The Laws of Simplicity**, John Maeda (book, força: canonical). Aplicação: Reduction, organization and emotional quality. Localizador: MIT Press, 2006, ISBN 9780262134729. Consulta: 2026-08-24.


# Template — Intentional Experience Direction

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | que estética e interação amplificam a proposta sem sacrificar usabilidade/performance? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Brand/product intent

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Mood/anti-mood

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Hierarchy/rhythm

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Signature moments

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Component/motion rules

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Prototype key journeys

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Accessibility/performance

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Perceptual review.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Intentional Experience Direction

### `art-direction-board.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `signature-moments.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### motion tokens

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### visual QA scorecard

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

identidade 20, hierarquia 20, craft 20, função 20, acessibilidade/performance 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `reduced motion; low-end device budget; dense enterprise flows prioritize scanning; novelty must not hide controls.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "required": [
    "loading",
    "empty",
    "error",
    "success"
  ]
}


{
  "spacing": [
    4,
    8,
    12,
    16,
    24,
    32,
    48,
    64
  ],
  "radii": [
    0,
    8,
    16,
    24
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Intentional Experience Direction",
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
        "brand_product_intent",
        "mood_anti_mood",
        "hierarchy_rhythm",
        "signature_moments",
        "component_motion_rules",
        "prototype_key_journeys",
        "accessibility_performance",
        "perceptual_review"
      ],
      "properties": {
        "brand_product_intent": {
          "type": "string",
          "minLength": 3
        },
        "mood_anti_mood": {
          "type": "string",
          "minLength": 3
        },
        "hierarchy_rhythm": {
          "type": "string",
          "minLength": 3
        },
        "signature_moments": {
          "type": "string",
          "minLength": 3
        },
        "component_motion_rules": {
          "type": "string",
          "minLength": 3
        },
        "prototype_key_journeys": {
          "type": "string",
          "minLength": 3
        },
        "accessibility_performance": {
          "type": "string",
          "minLength": 3
        },
        "perceptual_review": {
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
    "behavior": "premium-visual-experience:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "premium-visual-experience:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "premium-visual-experience:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "multiple screens required"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "invalid spacing token"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "missing experience states: error,success"
  }
]


{
  "tokens": {
    "spacing": 16
  },
  "screens": []
}


{
  "tokens": {
    "spacing": 7
  },
  "screens": [
    {
      "name": "Home",
      "components": [
        "hero"
      ],
      "states": [
        "loading",
        "empty"
      ]
    },
    {
      "name": "Detail",
      "components": [
        "card"
      ],
      "states": [
        "error",
        "success"
      ]
    }
  ]
}


{
  "tokens": {
    "spacing": 16
  },
  "screens": [
    {
      "name": "Home",
      "components": [
        "hero"
      ],
      "states": [
        "loading",
        "empty"
      ]
    },
    {
      "name": "Detail",
      "components": [
        "card"
      ],
      "states": []
    }
  ]
}


{
  "tokens": {
    "spacing": 16
  },
  "screens": [
    {
      "name": "Home",
      "components": [
        "hero"
      ],
      "states": [
        "loading",
        "empty"
      ]
    },
    {
      "name": "Detail",
      "components": [
        "card"
      ],
      "states": [
        "error",
        "success"
      ]
    }
  ]
}


{
  "tokens": {
    "spacing": 8
  },
  "screens": [
    {
      "name": "Home",
      "components": [
        "hero"
      ],
      "states": [
        "loading",
        "empty"
      ]
    },
    {
      "name": "Detail",
      "components": [
        "card"
      ],
      "states": [
        "error",
        "success"
      ]
    }
  ]
}


{
  "tokens": {
    "spacing": 24
  },
  "screens": [
    {
      "name": "Home",
      "components": [
        "hero"
      ],
      "states": [
        "loading",
        "empty"
      ]
    },
    {
      "name": "Detail",
      "components": [
        "card"
      ],
      "states": [
        "error",
        "success"
      ]
    }
  ]
}


## 24. premium-visual-experience — Intentional Experience Direction

- **Decisão:** que estética e interação amplificam a proposta sem sacrificar usabilidade/performance?
- **Fluxo:** brand/product intent → mood/anti-mood → hierarchy/rhythm → signature moments → component/motion rules → prototype key journeys → accessibility/performance → perceptual review.
- **Técnicas:** contrast map; visual rhythm; focal hierarchy; motion grammar; progressive complexity; aesthetic-usability countercheck.
- **Exceções:** reduced motion; low-end device budget; dense enterprise flows prioritize scanning; novelty must not hide controls.
- **Rubrica:** identidade 20, hierarquia 20, craft 20, função 20, acessibilidade/performance 20.
- **Recursos:** `art-direction-board.md`, `signature-moments.yaml`, motion tokens, visual QA scorecard.


[
  {
    "type": "official",
    "title": "Material Design 3",
    "author": "Google",
    "url": "https://m3.material.io/",
    "strength": "primary",
    "use": "Interaction, motion and component behavior baseline"
  },
  {
    "type": "official",
    "title": "Human Interface Guidelines",
    "author": "Apple",
    "url": "https://developer.apple.com/design/human-interface-guidelines/",
    "strength": "primary",
    "use": "Platform coherence, hierarchy and feedback"
  },
  {
    "type": "book",
    "title": "The Laws of Simplicity",
    "author": "John Maeda",
    "reference": "MIT Press, 2006, ISBN 9780262134729",
    "strength": "canonical",
    "use": "Reduction, organization and emotional quality"
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
    screens=data.get('screens'); tokens=data.get('tokens',{})
    if not isinstance(screens,list) or len(screens)<2: fail('multiple screens required')
    if tokens.get('spacing') not in assets['tokens']['spacing']: fail('invalid spacing token')
    states=set(); components=0
    for screen in screens:
        req(screen,'name'); comps=screen.get('components')
        if not isinstance(comps,list) or not comps: fail('screen components required')
        components+=len(comps); states.update(screen.get('states',[]))
    missing=set(assets['states']['required'])-states
    if missing: fail('missing experience states: '+','.join(sorted(missing)))
    return {'screen_count':len(screens),'component_count':components,'tokens':tokens,'state_coverage':sorted(states),'experience_spec':screens,'quality_gate':'all required states covered'}
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
