#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: document-builder
description: "Executa Semantic Document Pipeline para responder: como preservar estrutura, identidade e acessibilidade no formato nativo?"
---

# Document Builder

## Escopo e gatilhos

Use quando a decisão real for: **como preservar estrutura, identidade e acessibilidade no formato nativo?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Semantic Document Pipeline**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Semantic Document Pipeline

1. **Content model**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Style map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Page/section rules**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Components (tables/callouts)**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Links/media**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Generate**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Parse-back**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Visual/accessibility qa**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Export.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Semantic styles**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keep-with-next**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Orphan control**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Repeat headers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alt text**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metadata**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Package inspection.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Template fornecido é autoridade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pdf não substitui arquivo editável quando exigido. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Fonte ausente usa fallback explícito.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fidelidade 25, estrutura 20, acessibilidade 20, render 20, editabilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `document_schema_json.md` ou formato nativo equivalente: materializa **`document-schema.json`** e deve ser citado pelo artefato principal.
- `style_map_yaml.md` ou formato nativo equivalente: materializa **`style-map.yaml`** e deve ser citado pelo artefato principal.
- `native_builder.md` ou formato nativo equivalente: materializa **native builder** e deve ser citado pelo artefato principal.
- `parse_back_assertions.md` ou formato nativo equivalente: materializa **parse-back assertions** e deve ser citado pelo artefato principal.
- `render_snapshots.md` ou formato nativo equivalente: materializa **render snapshots** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **PDF/UA-1 ISO 14289-1**, ISO (standard, força: primary). Aplicação: Accessible document structure. Localizador: https://www.iso.org/standard/64599.html. Consulta: 2026-08-24.
2. **OOXML ECMA-376**, Ecma International (standard, força: primary). Aplicação: Native Office document packaging and semantics. Localizador: https://ecma-international.org/publications-and-standards/standards/ecma-376/. Consulta: 2026-08-24.
3. **python-docx**, python-openxml (github, força: mature). Aplicação: Reproducible DOCX generation and validation. Localizador: https://github.com/python-openxml/python-docx. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Semantic Document Pipeline

## Pergunta de controle

como preservar estrutura, identidade e acessibilidade no formato nativo?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **content model** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **semantic styles** responde à pergunta sem extrapolar o dado? Se não, selecione **package inspection.** e declare a troca.
3. Há uma destas exceções: template fornecido é autoridade; PDF não substitui arquivo editável quando exigido; fonte ausente usa fallback explícito.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **como preservar estrutura, identidade e acessibilidade no formato nativo?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Content model**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Style map**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Page/section rules**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Components (tables/callouts)**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Links/media**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Generate**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Parse-back**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Visual/accessibility qa**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Export.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Semantic styles**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Keep-with-next**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Orphan control**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Repeat headers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alt text**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Metadata**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Package inspection.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Template fornecido é autoridade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pdf não substitui arquivo editável quando exigido. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Fonte ausente usa fallback explícito.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “style map” cita evidência identificada, aplica “semantic styles”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Semantic Document Pipeline foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `document_schema_json.md` ou formato nativo equivalente: materializa **`document-schema.json`** e deve ser citado pelo artefato principal.
- `style_map_yaml.md` ou formato nativo equivalente: materializa **`style-map.yaml`** e deve ser citado pelo artefato principal.
- `native_builder.md` ou formato nativo equivalente: materializa **native builder** e deve ser citado pelo artefato principal.
- `parse_back_assertions.md` ou formato nativo equivalente: materializa **parse-back assertions** e deve ser citado pelo artefato principal.
- `render_snapshots.md` ou formato nativo equivalente: materializa **render snapshots** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fidelidade 25, estrutura 20, acessibilidade 20, render 20, editabilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **PDF/UA-1 ISO 14289-1**, ISO (standard, força: primary). Aplicação: Accessible document structure. Localizador: https://www.iso.org/standard/64599.html. Consulta: 2026-08-24.
2. **OOXML ECMA-376**, Ecma International (standard, força: primary). Aplicação: Native Office document packaging and semantics. Localizador: https://ecma-international.org/publications-and-standards/standards/ecma-376/. Consulta: 2026-08-24.
3. **python-docx**, python-openxml (github, força: mature). Aplicação: Reproducible DOCX generation and validation. Localizador: https://github.com/python-openxml/python-docx. Consulta: 2026-08-24.


# Template — Semantic Document Pipeline

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | como preservar estrutura, identidade e acessibilidade no formato nativo? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Content model

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Style map

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Page/section rules

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Components (tables/callouts)

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Links/media

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Generate

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Parse-back

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Visual/accessibility qa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Export.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Semantic Document Pipeline

### `document-schema.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `style-map.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### native builder

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### parse-back assertions

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### render snapshots

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

fidelidade 25, estrutura 20, acessibilidade 20, render 20, editabilidade 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `template fornecido é autoridade; PDF não substitui arquivo editável quando exigido; fonte ausente usa fallback explícito.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "required": [
    "purpose",
    "audience",
    "sections",
    "sources"
  ]
}


{
  "roles": [
    "title",
    "heading1",
    "heading2",
    "body",
    "caption"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Semantic Document Pipeline",
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
        "content_model",
        "style_map",
        "page_section_rules",
        "components_tables_callouts",
        "links_media",
        "generate",
        "parse_back",
        "visual_accessibility_qa",
        "export"
      ],
      "properties": {
        "content_model": {
          "type": "string",
          "minLength": 3
        },
        "style_map": {
          "type": "string",
          "minLength": 3
        },
        "page_section_rules": {
          "type": "string",
          "minLength": 3
        },
        "components_tables_callouts": {
          "type": "string",
          "minLength": 3
        },
        "links_media": {
          "type": "string",
          "minLength": 3
        },
        "generate": {
          "type": "string",
          "minLength": 3
        },
        "parse_back": {
          "type": "string",
          "minLength": 3
        },
        "visual_accessibility_qa": {
          "type": "string",
          "minLength": 3
        },
        "export": {
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
    "behavior": "document-builder:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "document-builder:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "document-builder:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "missing purpose"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "sections must be list"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "duplicate section anchor"
  }
]


{
  "audience": "diretoria",
  "sections": [
    {
      "title": "Diagnóstico",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    },
    {
      "title": "Plano",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    }
  ],
  "sources": [
    "https://example.org/a"
  ],
  "metadata": {
    "version": "1"
  }
}


{
  "purpose": "decidir",
  "audience": "diretoria",
  "sections": "bad",
  "sources": [
    "https://example.org/a"
  ],
  "metadata": {
    "version": "1"
  }
}


{
  "purpose": "decidir",
  "audience": "diretoria",
  "sections": [
    {
      "title": "Diagnóstico",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    },
    {
      "title": "Diagnóstico",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    }
  ],
  "sources": [
    "https://example.org/a"
  ],
  "metadata": {
    "version": "1"
  }
}


{
  "purpose": "decidir",
  "audience": "diretoria",
  "sections": [
    {
      "title": "Diagnóstico",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    },
    {
      "title": "Plano",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    }
  ],
  "sources": [
    "https://example.org/a"
  ],
  "metadata": {
    "version": "1"
  }
}


{
  "purpose": "decidir",
  "audience": "diretoria",
  "sections": [
    {
      "title": "Diagnóstico",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    },
    {
      "title": "Plano",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    }
  ],
  "sources": [
    "https://example.org/a"
  ],
  "metadata": {
    "version": "2"
  }
}


{
  "purpose": "decidir",
  "audience": "diretoria",
  "sections": [
    {
      "title": "Diagnóstico",
      "body": "Evidência verificável com fonte primária e contexto suficiente"
    },
    {
      "title": "Plano",
      "body": "Evidência verificável com fonte primária e contexto suficiente Evidência verificável com fonte primária e contexto suficiente"
    }
  ],
  "sources": [
    "https://example.org/a"
  ],
  "metadata": {
    "version": "1"
  }
}


## 14. document-builder — Semantic Document Pipeline

- **Decisão:** como preservar estrutura, identidade e acessibilidade no formato nativo?
- **Fluxo:** content model → style map → page/section rules → components (tables/callouts) → links/media → generate → parse-back → visual/accessibility QA → export.
- **Técnicas:** semantic styles; keep-with-next; orphan control; repeat headers; alt text; metadata; package inspection.
- **Exceções:** template fornecido é autoridade; PDF não substitui arquivo editável quando exigido; fonte ausente usa fallback explícito.
- **Rubrica:** fidelidade 25, estrutura 20, acessibilidade 20, render 20, editabilidade 15.
- **Recursos:** `document-schema.json`, `style-map.yaml`, native builder, parse-back assertions e render snapshots.


[
  {
    "type": "standard",
    "title": "PDF/UA-1 ISO 14289-1",
    "author": "ISO",
    "url": "https://www.iso.org/standard/64599.html",
    "strength": "primary",
    "use": "Accessible document structure"
  },
  {
    "type": "standard",
    "title": "OOXML ECMA-376",
    "author": "Ecma International",
    "url": "https://ecma-international.org/publications-and-standards/standards/ecma-376/",
    "strength": "primary",
    "use": "Native Office document packaging and semantics"
  },
  {
    "type": "github",
    "title": "python-docx",
    "author": "python-openxml",
    "url": "https://github.com/python-openxml/python-docx",
    "strength": "mature",
    "use": "Reproducible DOCX generation and validation"
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
    meta=data.get('metadata',{}); sections=data.get('sections')
    for k in assets['qa']['required']:
        if k not in data or data[k] in ('',None,[]): fail('missing '+k)
    if not isinstance(sections,list): fail('sections must be list')
    outline=[]; anchor=set()
    for sec in sections:
        title=req(sec,'title'); body=req(sec,'body')
        a='-'.join(title.lower().split())
        if a in anchor: fail('duplicate section anchor')
        anchor.add(a); outline.append({'anchor':a,'title':title,'words':len(body.split())})
    if not isinstance(data['sources'],list) or not data['sources']: fail('sources required')
    return {'metadata':meta,'style_roles':assets['styles']['roles'],'outline':outline,'total_words':sum(x['words'] for x in outline)}
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
