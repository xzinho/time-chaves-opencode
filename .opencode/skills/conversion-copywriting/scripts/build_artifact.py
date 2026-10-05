#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: conversion-copywriting
description: "Executa Awareness-Proof Sequence para responder: que próxima crença o leitor precisa aceitar para agir?"
---

# Conversion Copywriting

## Escopo e gatilhos

Use quando a decisão real for: **que próxima crença o leitor precisa aceitar para agir?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Awareness-Proof Sequence**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Awareness-Proof Sequence

1. **Voice-of-customer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Estágio/sofisticação**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desired action**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Belief chain**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Headline/promessa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mecanismo**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Prova**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objection handling**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Substantiation/read-aloud.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Message hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Specificity ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk reversal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Friction audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant isolation.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Prova fraca reduz claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mercado saturado exige mecanismo/distinção. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Urgência deve ser factual.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: relevância 20, clareza 20, credibilidade 20, progressão 15, oferta 15, ética/compliance 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `voc_bank_csv.md` ou formato nativo equivalente: materializa **`voc-bank.csv`** e deve ser citado pelo artefato principal.
- `belief_chain_yaml.md` ou formato nativo equivalente: materializa **`belief-chain.yaml`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `variant_sheet.md` ou formato nativo equivalente: materializa **variant sheet** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Scientific Advertising**, Claude Hopkins (book, força: canonical). Aplicação: Specific claims, reason-why and measurable response. Localizador: Lord & Thomas, 1923; public domain. Consulta: 2026-08-24.
2. **Breakthrough Advertising**, Eugene Schwartz (book, força: canonical). Aplicação: Awareness stages and market sophistication. Localizador: Boardroom, 1966, ISBN 9780887232984. Consulta: 2026-08-24.
3. **Truth In Advertising**, US FTC (official, força: primary). Aplicação: Claim substantiation and deception guardrails. Localizador: https://www.ftc.gov/news-events/topics/truth-advertising. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Awareness-Proof Sequence

## Pergunta de controle

que próxima crença o leitor precisa aceitar para agir?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **voice-of-customer** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **message hierarchy** responde à pergunta sem extrapolar o dado? Se não, selecione **variant isolation.** e declare a troca.
3. Há uma destas exceções: prova fraca reduz claim; mercado saturado exige mecanismo/distinção; urgência deve ser factual.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **que próxima crença o leitor precisa aceitar para agir?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Voice-of-customer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Estágio/sofisticação**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Desired action**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Belief chain**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Headline/promessa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mecanismo**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Prova**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objection handling**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Substantiation/read-aloud.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Message hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Specificity ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof taxonomy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Risk reversal**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Friction audit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Variant isolation.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Prova fraca reduz claim. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mercado saturado exige mecanismo/distinção. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Urgência deve ser factual.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “estágio/sofisticação” cita evidência identificada, aplica “message hierarchy”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Awareness-Proof Sequence foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `voc_bank_csv.md` ou formato nativo equivalente: materializa **`voc-bank.csv`** e deve ser citado pelo artefato principal.
- `belief_chain_yaml.md` ou formato nativo equivalente: materializa **`belief-chain.yaml`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `variant_sheet.md` ou formato nativo equivalente: materializa **variant sheet** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: relevância 20, clareza 20, credibilidade 20, progressão 15, oferta 15, ética/compliance 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Scientific Advertising**, Claude Hopkins (book, força: canonical). Aplicação: Specific claims, reason-why and measurable response. Localizador: Lord & Thomas, 1923; public domain. Consulta: 2026-08-24.
2. **Breakthrough Advertising**, Eugene Schwartz (book, força: canonical). Aplicação: Awareness stages and market sophistication. Localizador: Boardroom, 1966, ISBN 9780887232984. Consulta: 2026-08-24.
3. **Truth In Advertising**, US FTC (official, força: primary). Aplicação: Claim substantiation and deception guardrails. Localizador: https://www.ftc.gov/news-events/topics/truth-advertising. Consulta: 2026-08-24.


# Template — Awareness-Proof Sequence

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | que próxima crença o leitor precisa aceitar para agir? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Voice-of-customer

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Estágio/sofisticação

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Desired action

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Belief chain

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Headline/promessa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Mecanismo

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Prova

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Objection handling

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Offer/cta

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 10. Substantiation/read-aloud.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Awareness-Proof Sequence

### `voc-bank.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `belief-chain.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `claim-proof-ledger.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### variant sheet

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

relevância 20, clareza 20, credibilidade 20, progressão 15, oferta 15, ética/compliance 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `prova fraca reduz claim; mercado saturado exige mecanismo/distinção; urgência deve ser factual.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "forbidden": [
    "garantido",
    "sem risco",
    "resultado certo"
  ]
}


{
  "formulas": [
    "PAS",
    "AIDA",
    "BAB"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Awareness-Proof Sequence",
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
        "voice_of_customer",
        "est_gio_sofistica_o",
        "desired_action",
        "belief_chain",
        "headline_promessa",
        "mecanismo",
        "prova",
        "objection_handling",
        "offer_cta",
        "substantiation_read_aloud"
      ],
      "properties": {
        "voice_of_customer": {
          "type": "string",
          "minLength": 3
        },
        "est_gio_sofistica_o": {
          "type": "string",
          "minLength": 3
        },
        "desired_action": {
          "type": "string",
          "minLength": 3
        },
        "belief_chain": {
          "type": "string",
          "minLength": 3
        },
        "headline_promessa": {
          "type": "string",
          "minLength": 3
        },
        "mecanismo": {
          "type": "string",
          "minLength": 3
        },
        "prova": {
          "type": "string",
          "minLength": 3
        },
        "objection_handling": {
          "type": "string",
          "minLength": 3
        },
        "offer_cta": {
          "type": "string",
          "minLength": 3
        },
        "substantiation_read_aloud": {
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
    "behavior": "conversion-copywriting:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "conversion-copywriting:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "conversion-copywriting:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "unsupported formula"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "missing conversion section"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "proof too weak"
  }
]


{
  "formula": "BAD",
  "sections": {
    "headline": "Pare de perder margem",
    "problem": "Custos crescem sem visibilidade",
    "mechanism": "Reconciliação semanal por canal",
    "proof": "Evidência verificável com fonte primária e contexto suficiente",
    "cta": "Solicite o diagnóstico"
  }
}


{
  "formula": "PAS",
  "sections": {}
}


{
  "formula": "PAS",
  "sections": {
    "headline": "Pare de perder margem",
    "problem": "Custos crescem sem visibilidade",
    "mechanism": "Reconciliação semanal por canal",
    "proof": "curta",
    "cta": "Solicite o diagnóstico"
  }
}


{
  "formula": "PAS",
  "sections": {
    "headline": "Pare de perder margem",
    "problem": "Custos crescem sem visibilidade",
    "mechanism": "Reconciliação semanal por canal",
    "proof": "Evidência verificável com fonte primária e contexto suficiente",
    "cta": "Solicite o diagnóstico"
  }
}


{
  "formula": "AIDA",
  "sections": {
    "headline": "Pare de perder margem",
    "problem": "Custos crescem sem visibilidade",
    "mechanism": "Reconciliação semanal por canal",
    "proof": "Evidência verificável com fonte primária e contexto suficiente",
    "cta": "Solicite o diagnóstico"
  }
}


{
  "formula": "BAB",
  "sections": {
    "headline": "Pare de perder margem",
    "problem": "Custos crescem sem visibilidade",
    "mechanism": "Reconciliação semanal por canal",
    "proof": "Evidência verificável com fonte primária e contexto suficiente",
    "cta": "Solicite o diagnóstico"
  }
}


## 9. conversion-copywriting — Awareness-Proof Sequence

- **Decisão:** que próxima crença o leitor precisa aceitar para agir?
- **Fluxo:** voice-of-customer → estágio/sofisticação → desired action → belief chain → headline/promessa → mecanismo → prova → objection handling → offer/CTA → substantiation/read-aloud.
- **Técnicas:** message hierarchy; specificity ladder; proof taxonomy; risk reversal; friction audit; variant isolation.
- **Exceções:** prova fraca reduz claim; mercado saturado exige mecanismo/distinção; urgência deve ser factual.
- **Rubrica:** relevância 20, clareza 20, credibilidade 20, progressão 15, oferta 15, ética/compliance 10.
- **Recursos:** `voc-bank.csv`, `belief-chain.yaml`, `claim-proof-ledger.csv`, variant sheet.


[
  {
    "type": "book",
    "title": "Scientific Advertising",
    "author": "Claude Hopkins",
    "reference": "Lord & Thomas, 1923; public domain",
    "strength": "canonical",
    "use": "Specific claims, reason-why and measurable response"
  },
  {
    "type": "book",
    "title": "Breakthrough Advertising",
    "author": "Eugene Schwartz",
    "reference": "Boardroom, 1966, ISBN 9780887232984",
    "strength": "canonical",
    "use": "Awareness stages and market sophistication"
  },
  {
    "type": "official",
    "title": "Truth In Advertising",
    "author": "US FTC",
    "url": "https://www.ftc.gov/news-events/topics/truth-advertising",
    "strength": "primary",
    "use": "Claim substantiation and deception guardrails"
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
    sections=data.get('sections'); formula=req(data,'formula')
    if formula not in assets['formulas']['formulas']: fail('unsupported formula')
    if not isinstance(sections,dict): fail('sections object required')
    needed={'headline','problem','mechanism','proof','cta'}
    if needed-set(sections): fail('missing conversion section')
    joined=' '.join(str(v) for v in sections.values()).lower()
    if any(x in joined for x in assets['claims']['forbidden']): fail('unsubstantiated absolute claim')
    if len(sections['proof'].strip())<12: fail('proof too weak')
    return {'formula':formula,'word_count':len(joined.split()),'sections':sections,'claim_check':'passed'}
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
