#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: professional-report-builder
description: "Executa Evidence-to-Report Architecture para responder: que report structure makes findings auditable and decisions actionable?"
---

# Professional Report Builder

## Escopo e gatilhos

Use quando a decisão real for: **que report structure makes findings auditable and decisions actionable?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Evidence-to-Report Architecture**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Evidence-to-Report Architecture

1. **Mandate/audience**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Report questions**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Outline/numbering**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Methods**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Implications**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Recommendations**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Appendices/citations**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Finding-evidence-recommendation chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source notes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart purpose**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cross-reference validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Executive/detail layering.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Sensitive appendix restricted. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing method disclosed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Recommendation separates evidence from judgment.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: traceability 25, structure 20, analysis 20, actionability 20, production quality 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `report_schema_json.md` ou formato nativo equivalente: materializa **`report-schema.json`** e deve ser citado pelo artefato principal.
- `evidence_register_csv.md` ou formato nativo equivalente: materializa **`evidence-register.csv`** e deve ser citado pelo artefato principal.
- `recommendation_trace_csv.md` ou formato nativo equivalente: materializa **`recommendation-trace.csv`** e deve ser citado pelo artefato principal.
- `docx_pdf_builders.md` ou formato nativo equivalente: materializa **DOCX/PDF builders** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **ISO 2145 Documentation Numbering**, ISO (standard, força: primary). Aplicação: Stable section hierarchy. Localizador: https://www.iso.org/standard/6937.html. Consulta: 2026-08-24.
2. **GOV.UK Style Guide**, UK Government Digital Service (official, força: primary). Aplicação: Readable, consistent professional language. Localizador: https://www.gov.uk/guidance/style-guide. Consulta: 2026-08-24.
3. **Storytelling with Data**, Cole Nussbaumer Knaflic (book, força: canonical). Aplicação: Chart choice, attention and explanatory narrative. Localizador: Wiley, 2015, ISBN 9781119002253. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Evidence-to-Report Architecture

## Pergunta de controle

que report structure makes findings auditable and decisions actionable?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **mandate/audience** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **finding-evidence-recommendation chain** responde à pergunta sem extrapolar o dado? Se não, selecione **executive/detail layering.** e declare a troca.
3. Há uma destas exceções: sensitive appendix restricted; missing method disclosed; recommendation separates evidence from judgment.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que report structure makes findings auditable and decisions actionable?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Mandate/audience**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Report questions**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Evidence register**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Outline/numbering**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Methods**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Implications**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Recommendations**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Limitations**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Appendices/citations**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Render qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Finding-evidence-recommendation chain**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Source notes**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Chart purpose**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cross-reference validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Executive/detail layering.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Sensitive appendix restricted. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Missing method disclosed. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Recommendation separates evidence from judgment.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “report questions” cita evidência identificada, aplica “finding-evidence-recommendation chain”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Evidence-to-Report Architecture foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `report_schema_json.md` ou formato nativo equivalente: materializa **`report-schema.json`** e deve ser citado pelo artefato principal.
- `evidence_register_csv.md` ou formato nativo equivalente: materializa **`evidence-register.csv`** e deve ser citado pelo artefato principal.
- `recommendation_trace_csv.md` ou formato nativo equivalente: materializa **`recommendation-trace.csv`** e deve ser citado pelo artefato principal.
- `docx_pdf_builders.md` ou formato nativo equivalente: materializa **DOCX/PDF builders** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: traceability 25, structure 20, analysis 20, actionability 20, production quality 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ISO 2145 Documentation Numbering**, ISO (standard, força: primary). Aplicação: Stable section hierarchy. Localizador: https://www.iso.org/standard/6937.html. Consulta: 2026-08-24.
2. **GOV.UK Style Guide**, UK Government Digital Service (official, força: primary). Aplicação: Readable, consistent professional language. Localizador: https://www.gov.uk/guidance/style-guide. Consulta: 2026-08-24.
3. **Storytelling with Data**, Cole Nussbaumer Knaflic (book, força: canonical). Aplicação: Chart choice, attention and explanatory narrative. Localizador: Wiley, 2015, ISBN 9781119002253. Consulta: 2026-08-24.


# Template — Evidence-to-Report Architecture

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | que report structure makes findings auditable and decisions actionable? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Mandate/audience

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Report questions

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Evidence register

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Outline/numbering

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Methods

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Findings

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Implications

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Recommendations

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Limitations

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 10. Appendices/citations

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 11. Render qa.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Evidence-to-Report Architecture

### `report-schema.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `evidence-register.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `recommendation-trace.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### DOCX/PDF builders

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

traceability 25, structure 20, analysis 20, actionability 20, production quality 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `sensitive appendix restricted; missing method disclosed; recommendation separates evidence from judgment.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "levels": [
    "primary",
    "secondary",
    "inference"
  ]
}


{
  "checks": [
    "scope",
    "method",
    "findings",
    "limitations",
    "recommendations"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Evidence-to-Report Architecture",
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
        "mandate_audience",
        "report_questions",
        "evidence_register",
        "outline_numbering",
        "methods",
        "findings",
        "implications",
        "recommendations",
        "limitations",
        "appendices_citations",
        "render_qa"
      ],
      "properties": {
        "mandate_audience": {
          "type": "string",
          "minLength": 3
        },
        "report_questions": {
          "type": "string",
          "minLength": 3
        },
        "evidence_register": {
          "type": "string",
          "minLength": 3
        },
        "outline_numbering": {
          "type": "string",
          "minLength": 3
        },
        "methods": {
          "type": "string",
          "minLength": 3
        },
        "findings": {
          "type": "string",
          "minLength": 3
        },
        "implications": {
          "type": "string",
          "minLength": 3
        },
        "recommendations": {
          "type": "string",
          "minLength": 3
        },
        "limitations": {
          "type": "string",
          "minLength": 3
        },
        "appendices_citations": {
          "type": "string",
          "minLength": 3
        },
        "render_qa": {
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
    "behavior": "professional-report-builder:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "professional-report-builder:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "professional-report-builder:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "weak report section scope"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "citations required"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "citation URL invalid"
  }
]


{
  "report": {
    "scope": "curto",
    "method": "Evidência verificável com fonte primária e contexto suficiente",
    "findings": "Evidência verificável com fonte primária e contexto suficiente",
    "limitations": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendations": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "citations": [
    {
      "level": "primary",
      "url": "https://example.org/a"
    },
    {
      "level": "secondary",
      "url": "https://example.org/b"
    }
  ]
}


{
  "report": {
    "scope": "Evidência verificável com fonte primária e contexto suficiente",
    "method": "Evidência verificável com fonte primária e contexto suficiente",
    "findings": "Evidência verificável com fonte primária e contexto suficiente",
    "limitations": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendations": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "citations": []
}


{
  "report": {
    "scope": "Evidência verificável com fonte primária e contexto suficiente",
    "method": "Evidência verificável com fonte primária e contexto suficiente",
    "findings": "Evidência verificável com fonte primária e contexto suficiente",
    "limitations": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendations": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "citations": [
    {
      "level": "primary",
      "url": "invalid"
    },
    {
      "level": "secondary",
      "url": "https://example.org/b"
    }
  ]
}


{
  "report": {
    "scope": "Evidência verificável com fonte primária e contexto suficiente",
    "method": "Evidência verificável com fonte primária e contexto suficiente",
    "findings": "Evidência verificável com fonte primária e contexto suficiente",
    "limitations": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendations": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "citations": [
    {
      "level": "primary",
      "url": "https://example.org/a"
    },
    {
      "level": "secondary",
      "url": "https://example.org/b"
    }
  ]
}


{
  "report": {
    "scope": "Evidência verificável com fonte primária e contexto suficiente",
    "method": "Evidência verificável com fonte primária e contexto suficiente",
    "findings": "Evidência verificável com fonte primária e contexto suficiente",
    "limitations": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendations": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "citations": [
    {
      "level": "inference",
      "url": "https://example.org/a"
    },
    {
      "level": "secondary",
      "url": "https://example.org/b"
    }
  ]
}


{
  "report": {
    "scope": "Evidência verificável com fonte primária e contexto suficiente",
    "method": "Evidência verificável com fonte primária e contexto suficiente",
    "findings": "Evidência verificável com fonte primária e contexto suficiente Evidência verificável com fonte primária e contexto suficiente",
    "limitations": "Evidência verificável com fonte primária e contexto suficiente",
    "recommendations": "Evidência verificável com fonte primária e contexto suficiente"
  },
  "citations": [
    {
      "level": "primary",
      "url": "https://example.org/a"
    },
    {
      "level": "secondary",
      "url": "https://example.org/b"
    }
  ]
}


## 28. professional-report-builder — Evidence-to-Report Architecture

- **Decisão:** que report structure makes findings auditable and decisions actionable?
- **Fluxo:** mandate/audience → report questions → evidence register → outline/numbering → methods → findings → implications → recommendations → limitations → appendices/citations → render QA.
- **Técnicas:** finding-evidence-recommendation chain; source notes; chart purpose; cross-reference validation; executive/detail layering.
- **Exceções:** sensitive appendix restricted; missing method disclosed; recommendation separates evidence from judgment.
- **Rubrica:** traceability 25, structure 20, analysis 20, actionability 20, production quality 15.
- **Recursos:** `report-schema.json`, `evidence-register.csv`, `recommendation-trace.csv`, DOCX/PDF builders.


[
  {
    "type": "standard",
    "title": "ISO 2145 Documentation Numbering",
    "author": "ISO",
    "url": "https://www.iso.org/standard/6937.html",
    "strength": "primary",
    "use": "Stable section hierarchy"
  },
  {
    "type": "official",
    "title": "GOV.UK Style Guide",
    "author": "UK Government Digital Service",
    "url": "https://www.gov.uk/guidance/style-guide",
    "strength": "primary",
    "use": "Readable, consistent professional language"
  },
  {
    "type": "book",
    "title": "Storytelling with Data",
    "author": "Cole Nussbaumer Knaflic",
    "reference": "Wiley, 2015, ISBN 9781119002253",
    "strength": "canonical",
    "use": "Chart choice, attention and explanatory narrative"
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
    report=data.get('report',{}); citations=data.get('citations')
    for section in assets['review']['checks']:
        if len(str(report.get(section,'')).strip())<12: fail('weak report section '+section)
    if not isinstance(citations,list) or len(citations)<2: fail('citations required')
    valid=set(assets['evidence']['levels']); seen=set()
    for c in citations:
        if req(c,'level') not in valid: fail('invalid evidence level')
        url=req(c,'url')
        if not url.startswith(('http://','https://')): fail('citation URL invalid')
        if url in seen: fail('duplicate citation')
        seen.add(url)
    return {'report':report,'citation_count':len(citations),'evidence_mix':{x:sum(c['level']==x for c in citations) for x in valid}}
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
