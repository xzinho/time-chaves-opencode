#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: presentation-builder
description: "Executa Argument-to-Slide System para responder: qual sequência faz a audiência compreender, acreditar e decidir?"
---

# Presentation Builder

## Escopo e gatilhos

Use quando a decisão real for: **qual sequência faz a audiência compreender, acreditar e decidir?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Argument-to-Slide System**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Argument-to-Slide System

1. **Audience/decision**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Storyline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Slide functions**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Wireframes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Chart selection**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Build**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Speaker notes**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Rehearsal/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Assertion-evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **One function per slide**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart integrity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Section rhythm**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Appendix routing.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Leave-behind needs more context. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Board deck leads with decisions. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Data-heavy slide gets takeaway and source, not decoration.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: storyline 25, evidence 20, visual hierarchy 20, readability 15, action 10, accessibility 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `storyline_csv.md` ou formato nativo equivalente: materializa **`storyline.csv`** e deve ser citado pelo artefato principal.
- `slide_schema_json.md` ou formato nativo equivalente: materializa **`slide-schema.json`** e deve ser citado pelo artefato principal.
- `chart_decision_tree.md` ou formato nativo equivalente: materializa **chart decision tree** e deve ser citado pelo artefato principal.
- `native_pptx_builder_and_render_montage.md` ou formato nativo equivalente: materializa **native PPTX builder and render montage** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Visual Display of Quantitative Information**, Edward Tufte (book, força: canonical). Aplicação: Evidence-dense, honest quantitative graphics. Localizador: Graphics Press, 2001, ISBN 9780961392147. Consulta: 2026-08-24.
2. **Presentation Zen**, Garr Reynolds (book, força: canonical). Aplicação: Audience, story and visual restraint. Localizador: New Riders, 2019, ISBN 9780135800911. Consulta: 2026-08-24.
3. **PowerPoint Accessibility**, Microsoft (official, força: primary). Aplicação: Reading order, alt text, contrast and structure. Localizador: https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Argument-to-Slide System

## Pergunta de controle

qual sequência faz a audiência compreender, acreditar e decidir?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **audience/decision** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **assertion-evidence** responde à pergunta sem extrapolar o dado? Se não, selecione **appendix routing.** e declare a troca.
3. Há uma destas exceções: leave-behind needs more context; board deck leads with decisions; data-heavy slide gets takeaway and source, not decoration.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual sequência faz a audiência compreender, acreditar e decidir?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Audience/decision**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Storyline**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Slide functions**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Wireframes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Chart selection**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Build**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Speaker notes**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Accessibility**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Rehearsal/render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Assertion-evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **One function per slide**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart integrity**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Section rhythm**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Appendix routing.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Leave-behind needs more context. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Board deck leads with decisions. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Data-heavy slide gets takeaway and source, not decoration.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “storyline” cita evidência identificada, aplica “assertion-evidence”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Argument-to-Slide System foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `storyline_csv.md` ou formato nativo equivalente: materializa **`storyline.csv`** e deve ser citado pelo artefato principal.
- `slide_schema_json.md` ou formato nativo equivalente: materializa **`slide-schema.json`** e deve ser citado pelo artefato principal.
- `chart_decision_tree.md` ou formato nativo equivalente: materializa **chart decision tree** e deve ser citado pelo artefato principal.
- `native_pptx_builder_and_render_montage.md` ou formato nativo equivalente: materializa **native PPTX builder and render montage** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: storyline 25, evidence 20, visual hierarchy 20, readability 15, action 10, accessibility 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Visual Display of Quantitative Information**, Edward Tufte (book, força: canonical). Aplicação: Evidence-dense, honest quantitative graphics. Localizador: Graphics Press, 2001, ISBN 9780961392147. Consulta: 2026-08-24.
2. **Presentation Zen**, Garr Reynolds (book, força: canonical). Aplicação: Audience, story and visual restraint. Localizador: New Riders, 2019, ISBN 9780135800911. Consulta: 2026-08-24.
3. **PowerPoint Accessibility**, Microsoft (official, força: primary). Aplicação: Reading order, alt text, contrast and structure. Localizador: https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25. Consulta: 2026-08-24.


# Template — Argument-to-Slide System

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual sequência faz a audiência compreender, acreditar e decidir? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Audience/decision

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Storyline

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Evidence inventory

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Slide functions

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Wireframes

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Chart selection

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Build

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Speaker notes

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Accessibility

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 10. Rehearsal/render qa.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Argument-to-Slide System

### `storyline.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `slide-schema.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### chart decision tree

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### native PPTX builder and render montage

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

storyline 25, evidence 20, visual hierarchy 20, readability 15, action 10, accessibility 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `leave-behind needs more context; board deck leads with decisions; data-heavy slide gets takeaway and source, not decoration.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "max_words": 45,
  "max_points": 5
}


{
  "beats": [
    "context",
    "tension",
    "insight",
    "proof",
    "decision"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Argument-to-Slide System",
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
        "audience_decision",
        "storyline",
        "evidence_inventory",
        "slide_functions",
        "wireframes",
        "chart_selection",
        "build",
        "speaker_notes",
        "accessibility",
        "rehearsal_render_qa"
      ],
      "properties": {
        "audience_decision": {
          "type": "string",
          "minLength": 3
        },
        "storyline": {
          "type": "string",
          "minLength": 3
        },
        "evidence_inventory": {
          "type": "string",
          "minLength": 3
        },
        "slide_functions": {
          "type": "string",
          "minLength": 3
        },
        "wireframes": {
          "type": "string",
          "minLength": 3
        },
        "chart_selection": {
          "type": "string",
          "minLength": 3
        },
        "build": {
          "type": "string",
          "minLength": 3
        },
        "speaker_notes": {
          "type": "string",
          "minLength": 3
        },
        "accessibility": {
          "type": "string",
          "minLength": 3
        },
        "rehearsal_render_qa": {
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
    "behavior": "presentation-builder:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "presentation-builder:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "presentation-builder:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "at least five slides required"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "invalid story beat"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "too many points"
  }
]


{
  "slides": []
}


{
  "slides": [
    {
      "beat": "bad",
      "title": "Context",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "tension",
      "title": "Tension",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "insight",
      "title": "Insight",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "proof",
      "title": "Proof",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "decision",
      "title": "Decision",
      "points": [
        "Mensagem objetiva"
      ]
    }
  ]
}


{
  "slides": [
    {
      "beat": "context",
      "title": "Context",
      "points": [
        "ponto",
        "ponto",
        "ponto",
        "ponto",
        "ponto",
        "ponto"
      ]
    },
    {
      "beat": "tension",
      "title": "Tension",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "insight",
      "title": "Insight",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "proof",
      "title": "Proof",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "decision",
      "title": "Decision",
      "points": [
        "Mensagem objetiva"
      ]
    }
  ]
}


{
  "slides": [
    {
      "beat": "context",
      "title": "Context",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "tension",
      "title": "Tension",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "insight",
      "title": "Insight",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "proof",
      "title": "Proof",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "decision",
      "title": "Decision",
      "points": [
        "Mensagem objetiva"
      ]
    }
  ]
}


{
  "slides": [
    {
      "beat": "context",
      "title": "Context",
      "points": [
        "Contexto novo"
      ]
    },
    {
      "beat": "tension",
      "title": "Tension",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "insight",
      "title": "Insight",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "proof",
      "title": "Proof",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "decision",
      "title": "Decision",
      "points": [
        "Mensagem objetiva"
      ]
    }
  ]
}


{
  "slides": [
    {
      "beat": "context",
      "title": "Context",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "tension",
      "title": "Tension",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "insight",
      "title": "Insight",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "proof",
      "title": "Proof",
      "points": [
        "Mensagem objetiva"
      ]
    },
    {
      "beat": "decision",
      "title": "Decisão final",
      "points": [
        "Mensagem objetiva"
      ]
    }
  ]
}


## 25. presentation-builder — Argument-to-Slide System

- **Decisão:** qual sequência faz a audiência compreender, acreditar e decidir?
- **Fluxo:** audience/decision → storyline → evidence inventory → slide functions → wireframes → chart selection → build → speaker notes → accessibility → rehearsal/render QA.
- **Técnicas:** assertion-evidence; one function per slide; chart integrity; progressive disclosure; section rhythm; appendix routing.
- **Exceções:** leave-behind needs more context; board deck leads with decisions; data-heavy slide gets takeaway and source, not decoration.
- **Rubrica:** storyline 25, evidence 20, visual hierarchy 20, readability 15, action 10, accessibility 10.
- **Recursos:** `storyline.csv`, `slide-schema.json`, chart decision tree, native PPTX builder and render montage.


[
  {
    "type": "book",
    "title": "The Visual Display of Quantitative Information",
    "author": "Edward Tufte",
    "reference": "Graphics Press, 2001, ISBN 9780961392147",
    "strength": "canonical",
    "use": "Evidence-dense, honest quantitative graphics"
  },
  {
    "type": "book",
    "title": "Presentation Zen",
    "author": "Garr Reynolds",
    "reference": "New Riders, 2019, ISBN 9780135800911",
    "strength": "canonical",
    "use": "Audience, story and visual restraint"
  },
  {
    "type": "official",
    "title": "PowerPoint Accessibility",
    "author": "Microsoft",
    "url": "https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25",
    "strength": "primary",
    "use": "Reading order, alt text, contrast and structure"
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
    slides=data.get('slides');
    if not isinstance(slides,list) or len(slides)<5: fail('at least five slides required')
    beats=set(); result=[]
    for n,slide in enumerate(slides,1):
        beat=req(slide,'beat'); title=req(slide,'title'); points=slide.get('points',[])
        if beat not in assets['story']['beats']: fail('invalid story beat')
        if len(points)>assets['slide-rules']['max_points']: fail('too many points')
        words=len((' '.join(points)+' '+title).split())
        if words>assets['slide-rules']['max_words']: fail('slide too dense')
        beats.add(beat); result.append({'number':n,'beat':beat,'title':title,'points':points})
    if set(assets['story']['beats'])-beats: fail('incomplete narrative arc')
    return {'slides':result,'arc_complete':True}
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
