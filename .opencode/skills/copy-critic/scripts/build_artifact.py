#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: copy-critic
description: "Executa Layered Editorial Diagnosis para responder: qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?"
---

# Copy Critic

## Escopo e gatilhos

Use quando a decisão real for: **qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Layered Editorial Diagnosis**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Layered Editorial Diagnosis

1. **Objetivo/audiência**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Factual/claim gate**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Arquitetura**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Parágrafo**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Frase**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Palavra**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Voz/consistência**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Acessibilidade**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Revisão priorizada com antes/depois.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Reverse outline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Information-scent test**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ambiguity scan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive-load pass**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Style sheet**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity taxonomy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Texto jurídico não simplifica obrigação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Seo não justifica redundância. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crítica separa gosto de falha observável.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: diagnóstico 30, preservação de intenção 20, impacto 20, justificativa 15, acessibilidade 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `editorial_scorecard_yaml.md` ou formato nativo equivalente: materializa **`editorial-scorecard.yaml`** e deve ser citado pelo artefato principal.
- `style_sheet_md.md` ou formato nativo equivalente: materializa **`style-sheet.md`** e deve ser citado pelo artefato principal.
- `issue_log_csv.md` ou formato nativo equivalente: materializa **`issue-log.csv`** e deve ser citado pelo artefato principal.
- `diff_anotado.md` ou formato nativo equivalente: materializa **diff anotado** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Federal Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Clarity, audience and actionable-language audit. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
2. **The Copyeditor's Handbook, 4th ed.**, Amy Einsohn and Marilyn Schwartz (book, força: canonical). Aplicação: Editorial levels and consistency checks. Localizador: University of California Press, 2019, ISBN 9780520286726. Consulta: 2026-08-24.
3. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Readable, understandable and accessible copy. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Layered Editorial Diagnosis

## Pergunta de controle

qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **objetivo/audiência** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **reverse outline** responde à pergunta sem extrapolar o dado? Se não, selecione **severity taxonomy.** e declare a troca.
3. Há uma destas exceções: texto jurídico não simplifica obrigação; SEO não justifica redundância; crítica separa gosto de falha observável.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Objetivo/audiência**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Factual/claim gate**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Arquitetura**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Parágrafo**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Frase**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Palavra**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Voz/consistência**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Acessibilidade**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Revisão priorizada com antes/depois.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Reverse outline**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Information-scent test**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ambiguity scan**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cognitive-load pass**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Style sheet**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity taxonomy.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Texto jurídico não simplifica obrigação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Seo não justifica redundância. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Crítica separa gosto de falha observável.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “factual/claim gate” cita evidência identificada, aplica “reverse outline”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Layered Editorial Diagnosis foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `editorial_scorecard_yaml.md` ou formato nativo equivalente: materializa **`editorial-scorecard.yaml`** e deve ser citado pelo artefato principal.
- `style_sheet_md.md` ou formato nativo equivalente: materializa **`style-sheet.md`** e deve ser citado pelo artefato principal.
- `issue_log_csv.md` ou formato nativo equivalente: materializa **`issue-log.csv`** e deve ser citado pelo artefato principal.
- `diff_anotado.md` ou formato nativo equivalente: materializa **diff anotado** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: diagnóstico 30, preservação de intenção 20, impacto 20, justificativa 15, acessibilidade 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Federal Plain Language Guidelines**, PlainLanguage.gov (official, força: primary). Aplicação: Clarity, audience and actionable-language audit. Localizador: https://www.plainlanguage.gov/guidelines/. Consulta: 2026-08-24.
2. **The Copyeditor's Handbook, 4th ed.**, Amy Einsohn and Marilyn Schwartz (book, força: canonical). Aplicação: Editorial levels and consistency checks. Localizador: University of California Press, 2019, ISBN 9780520286726. Consulta: 2026-08-24.
3. **Web Content Accessibility Guidelines 2.2**, W3C (official, força: primary). Aplicação: Readable, understandable and accessible copy. Localizador: https://www.w3.org/TR/WCAG22/. Consulta: 2026-08-24.


# Template — Layered Editorial Diagnosis

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Objetivo/audiência

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Factual/claim gate

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Arquitetura

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Parágrafo

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Frase

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Palavra

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Voz/consistência

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Acessibilidade

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Revisão priorizada com antes/depois.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Layered Editorial Diagnosis

### `editorial-scorecard.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `style-sheet.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `issue-log.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### diff anotado

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

diagnóstico 30, preservação de intenção 20, impacto 20, justificativa 15, acessibilidade 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `texto jurídico não simplifica obrigação; SEO não justifica redundância; crítica separa gosto de falha observável.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "dimensions": [
    "clarity",
    "specificity",
    "credibility",
    "voice",
    "action"
  ]
}


{
  "thresholds": {
    "blocker": 2,
    "warning": 3
  }
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Layered Editorial Diagnosis",
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
        "objetivo_audi_ncia",
        "factual_claim_gate",
        "arquitetura",
        "par_grafo",
        "frase",
        "palavra",
        "voz_consist_ncia",
        "acessibilidade",
        "revis_o_priorizada_com_antes_depois"
      ],
      "properties": {
        "objetivo_audi_ncia": {
          "type": "string",
          "minLength": 3
        },
        "factual_claim_gate": {
          "type": "string",
          "minLength": 3
        },
        "arquitetura": {
          "type": "string",
          "minLength": 3
        },
        "par_grafo": {
          "type": "string",
          "minLength": 3
        },
        "frase": {
          "type": "string",
          "minLength": 3
        },
        "palavra": {
          "type": "string",
          "minLength": 3
        },
        "voz_consist_ncia": {
          "type": "string",
          "minLength": 3
        },
        "acessibilidade": {
          "type": "string",
          "minLength": 3
        },
        "revis_o_priorizada_com_antes_depois": {
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
    "behavior": "copy-critic:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "copy-critic:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "copy-critic:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "copy too short for critique"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "all ratings required"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "rating outside 1..5"
  }
]


{
  "text": "curto",
  "ratings": {
    "clarity": 4,
    "specificity": 3,
    "credibility": 4,
    "voice": 5,
    "action": 3
  }
}


{
  "text": "uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta",
  "ratings": {}
}


{
  "text": "uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta",
  "ratings": {
    "clarity": 9,
    "specificity": 3,
    "credibility": 4,
    "voice": 5,
    "action": 3
  }
}


{
  "text": "uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta",
  "ratings": {
    "clarity": 4,
    "specificity": 3,
    "credibility": 4,
    "voice": 5,
    "action": 3
  }
}


{
  "text": "uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta",
  "ratings": {
    "clarity": 1,
    "specificity": 3,
    "credibility": 4,
    "voice": 5,
    "action": 3
  }
}


{
  "text": "uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta uma mensagem clara específica confiável orientada para ação e escrita na voz correta",
  "ratings": {
    "clarity": 4,
    "specificity": 3,
    "credibility": 4,
    "voice": 5,
    "action": 5
  }
}


## 10. copy-critic — Layered Editorial Diagnosis

- **Decisão:** qual mudança aumenta eficácia sem descaracterizar voz, fatos ou restrições?
- **Fluxo:** objetivo/audiência → factual/claim gate → arquitetura → parágrafo → frase → palavra → voz/consistência → acessibilidade → revisão priorizada com antes/depois.
- **Técnicas:** reverse outline; information-scent test; ambiguity scan; cognitive-load pass; style sheet; severity taxonomy.
- **Exceções:** texto jurídico não simplifica obrigação; SEO não justifica redundância; crítica separa gosto de falha observável.
- **Rubrica:** diagnóstico 30, preservação de intenção 20, impacto 20, justificativa 15, acessibilidade 15.
- **Recursos:** `editorial-scorecard.yaml`, `style-sheet.md`, `issue-log.csv`, diff anotado.


[
  {
    "type": "official",
    "title": "Federal Plain Language Guidelines",
    "author": "PlainLanguage.gov",
    "url": "https://www.plainlanguage.gov/guidelines/",
    "strength": "primary",
    "use": "Clarity, audience and actionable-language audit"
  },
  {
    "type": "book",
    "title": "The Copyeditor's Handbook, 4th ed.",
    "author": "Amy Einsohn and Marilyn Schwartz",
    "reference": "University of California Press, 2019, ISBN 9780520286726",
    "strength": "canonical",
    "use": "Editorial levels and consistency checks"
  },
  {
    "type": "official",
    "title": "Web Content Accessibility Guidelines 2.2",
    "author": "W3C",
    "url": "https://www.w3.org/TR/WCAG22/",
    "strength": "primary",
    "use": "Readable, understandable and accessible copy"
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
    text=req(data,'text'); ratings=data.get('ratings')
    if len(text.split())<20: fail('copy too short for critique')
    dims=assets['dimensions']['dimensions']
    if not isinstance(ratings,dict) or set(dims)-set(ratings): fail('all ratings required')
    findings=[]
    for d in dims:
        n=int(ratings[d]);
        if not 1<=n<=5: fail('rating outside 1..5')
        if n<=assets['severity']['thresholds']['blocker']: findings.append({'dimension':d,'severity':'blocker'})
        elif n<=assets['severity']['thresholds']['warning']: findings.append({'dimension':d,'severity':'warning'})
    return {'average':round(sum(int(ratings[d]) for d in dims)/len(dims),2),'findings':findings,'rewrite_required':any(f['severity']=='blocker' for f in findings)}
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
