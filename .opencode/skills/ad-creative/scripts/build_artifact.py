#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: ad-creative
description: "Executa Creative Evidence Loop para responder: qual combinação de audiência, estágio, promessa, prova e formato merece teste?"
---

# Ad Creative

## Escopo e gatilhos

Use quando a decisão real for: **qual combinação de audiência, estágio, promessa, prova e formato merece teste?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Creative Evidence Loop**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Creative Evidence Loop

1. **Brief verificável**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Matriz de tensões**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inventário de claims/provas**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **3 territórios criativos**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Variações hook/body/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gate de política**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Plano de células e hipótese.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Message-market fit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Awareness ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Angle × format matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pre-mortem de interpretação**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Controle de variável criativa.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Segmento regulado exige aprovação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de prova converte claim em hipótese. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pouco orçamento reduz células, não mistura variáveis.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: insight 20, especificidade 20, prova 20, distinção 15, adequação ao formato 15, compliance 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `creative_test_matrix_csv.md` ou formato nativo equivalente: materializa **`creative-test-matrix.csv`** e deve ser citado pelo artefato principal.
- `policy_gate_yaml.md` ou formato nativo equivalente: materializa **`policy-gate.yaml`** e deve ser citado pelo artefato principal.
- `storyboard_com_safe_zones.md` ou formato nativo equivalente: materializa **storyboard com safe zones** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Meta Advertising Standards**, Meta (official, força: primary). Aplicação: Policy gate and prohibited-claim checklist. Localizador: https://transparency.meta.com/policies/ad-standards/. Consulta: 2026-08-24.
2. **Google Ads Creative Best Practices**, Google (official, força: primary). Aplicação: Asset variation and responsive-ad constraints. Localizador: https://support.google.com/google-ads/answer/6167122. Consulta: 2026-08-24.
3. **Ogilvy on Advertising**, David Ogilvy (book, força: canonical). Aplicação: Research-led promise, headline and proof discipline. Localizador: Vintage, 1985, ISBN 9780394729039. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Creative Evidence Loop

## Pergunta de controle

qual combinação de audiência, estágio, promessa, prova e formato merece teste?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **brief verificável** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **message-market fit** responde à pergunta sem extrapolar o dado? Se não, selecione **controle de variável criativa.** e declare a troca.
3. Há uma destas exceções: segmento regulado exige aprovação; ausência de prova converte claim em hipótese; pouco orçamento reduz células, não mistura variáveis.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual combinação de audiência, estágio, promessa, prova e formato merece teste?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Brief verificável**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Matriz de tensões**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Inventário de claims/provas**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **3 territórios criativos**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Variações hook/body/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Gate de política**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Plano de células e hipótese.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Message-market fit**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Awareness ladder**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Angle × format matrix**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pre-mortem de interpretação**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Controle de variável criativa.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Segmento regulado exige aprovação. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de prova converte claim em hipótese. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Pouco orçamento reduz células, não mistura variáveis.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “matriz de tensões” cita evidência identificada, aplica “message-market fit”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Creative Evidence Loop foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `creative_test_matrix_csv.md` ou formato nativo equivalente: materializa **`creative-test-matrix.csv`** e deve ser citado pelo artefato principal.
- `policy_gate_yaml.md` ou formato nativo equivalente: materializa **`policy-gate.yaml`** e deve ser citado pelo artefato principal.
- `storyboard_com_safe_zones.md` ou formato nativo equivalente: materializa **storyboard com safe zones** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: insight 20, especificidade 20, prova 20, distinção 15, adequação ao formato 15, compliance 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Meta Advertising Standards**, Meta (official, força: primary). Aplicação: Policy gate and prohibited-claim checklist. Localizador: https://transparency.meta.com/policies/ad-standards/. Consulta: 2026-08-24.
2. **Google Ads Creative Best Practices**, Google (official, força: primary). Aplicação: Asset variation and responsive-ad constraints. Localizador: https://support.google.com/google-ads/answer/6167122. Consulta: 2026-08-24.
3. **Ogilvy on Advertising**, David Ogilvy (book, força: canonical). Aplicação: Research-led promise, headline and proof discipline. Localizador: Vintage, 1985, ISBN 9780394729039. Consulta: 2026-08-24.


# Template — Creative Evidence Loop

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual combinação de audiência, estágio, promessa, prova e formato merece teste? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Brief verificável

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Matriz de tensões

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Inventário de claims/provas

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. 3 territórios criativos

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Variações hook/body/cta

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Gate de política

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Plano de células e hipótese.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Creative Evidence Loop

### `claim-proof-ledger.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `creative-test-matrix.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `policy-gate.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### storyboard com safe zones

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

insight 20, especificidade 20, prova 20, distinção 15, adequação ao formato 15, compliance 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `segmento regulado exige aprovação; ausência de prova converte claim em hipótese; pouco orçamento reduz células, não mistura variáveis.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "hooks": [
    "contraste",
    "demonstração",
    "prova",
    "curiosidade"
  ]
}


{
  "weights": {
    "clarity": 0.25,
    "specificity": 0.3,
    "credibility": 0.25,
    "cta_strength": 0.2
  }
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Creative Evidence Loop",
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
        "brief_verific_vel",
        "matriz_de_tens_es",
        "invent_rio_de_claims_provas",
        "3_territ_rios_criativos",
        "varia_es_hook_body_cta",
        "gate_de_pol_tica",
        "plano_de_c_lulas_e_hip_tese"
      ],
      "properties": {
        "brief_verific_vel": {
          "type": "string",
          "minLength": 3
        },
        "matriz_de_tens_es": {
          "type": "string",
          "minLength": 3
        },
        "invent_rio_de_claims_provas": {
          "type": "string",
          "minLength": 3
        },
        "3_territ_rios_criativos": {
          "type": "string",
          "minLength": 3
        },
        "varia_es_hook_body_cta": {
          "type": "string",
          "minLength": 3
        },
        "gate_de_pol_tica": {
          "type": "string",
          "minLength": 3
        },
        "plano_de_c_lulas_e_hip_tese": {
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
    "behavior": "ad-creative:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "ad-creative:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "ad-creative:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "missing audience"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "variants must contain at least 3 ads"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "invalid proof"
  }
]


{
  "offer": "audit",
  "variants": [
    {
      "copy": "Diagnóstico específico 0 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 1 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 2 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    }
  ]
}


{
  "audience": "founders",
  "offer": "audit",
  "variants": []
}


{
  "audience": "founders",
  "offer": "audit",
  "variants": [
    {
      "copy": "Diagnóstico específico 0 para reduzir desperdício",
      "proof": "tbd",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 1 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 2 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    }
  ]
}


{
  "audience": "founders",
  "offer": "audit",
  "variants": [
    {
      "copy": "Diagnóstico específico 0 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 1 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 2 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    }
  ]
}


{
  "audience": "founders",
  "offer": "auditoria premium",
  "variants": [
    {
      "copy": "Diagnóstico específico 0 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 1 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 2 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    }
  ]
}


{
  "audience": "founders",
  "offer": "audit",
  "variants": [
    {
      "copy": "Diagnóstico específico 0 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 1,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 1 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    },
    {
      "copy": "Diagnóstico específico 2 para reduzir desperdício",
      "proof": "Evidência verificável com fonte primária e contexto suficiente",
      "cta": "Agende",
      "clarity": 4,
      "specificity": 5,
      "credibility": 4,
      "cta_strength": 5
    }
  ]
}


## 1. ad-creative — Creative Evidence Loop

- **Decisão:** qual combinação de audiência, estágio, promessa, prova e formato merece teste?
- **Fluxo:** brief verificável → matriz de tensões → inventário de claims/provas → 3 territórios criativos → variações hook/body/CTA → gate de política → plano de células e hipótese.
- **Técnicas:** message-market fit; awareness ladder; angle × format matrix; pre-mortem de interpretação; controle de variável criativa.
- **Exceções:** segmento regulado exige aprovação; ausência de prova converte claim em hipótese; pouco orçamento reduz células, não mistura variáveis.
- **Rubrica:** insight 20, especificidade 20, prova 20, distinção 15, adequação ao formato 15, compliance 10.
- **Recursos:** `claim-proof-ledger.csv`, `creative-test-matrix.csv`, `policy-gate.yaml`, storyboard com safe zones.


[
  {
    "type": "official",
    "title": "Meta Advertising Standards",
    "author": "Meta",
    "url": "https://transparency.meta.com/policies/ad-standards/",
    "strength": "primary",
    "use": "Policy gate and prohibited-claim checklist"
  },
  {
    "type": "official",
    "title": "Google Ads Creative Best Practices",
    "author": "Google",
    "url": "https://support.google.com/google-ads/answer/6167122",
    "strength": "primary",
    "use": "Asset variation and responsive-ad constraints"
  },
  {
    "type": "book",
    "title": "Ogilvy on Advertising",
    "author": "David Ogilvy",
    "reference": "Vintage, 1985, ISBN 9780394729039",
    "strength": "canonical",
    "use": "Research-led promise, headline and proof discipline"
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
    hooks=assets['hooks']['hooks']; w=assets['rubric']['weights']
    variants=data.get('variants'); audience=req(data,'audience'); offer=req(data,'offer')
    if not isinstance(variants,list) or len(variants)<3: fail('variants must contain at least 3 ads')
    out=[]
    for i,v in enumerate(variants):
        copy=req(v,'copy'); proof=req(v,'proof'); cta=req(v,'cta')
        if proof.lower() in {'tbd','none','a desenvolver'}: fail('invalid proof')
        score=round(w['clarity']*float(v.get('clarity',0))+w['specificity']*float(v.get('specificity',0))+w['credibility']*float(v.get('credibility',0))+w['cta_strength']*float(v.get('cta_strength',0)),3)
        out.append({'id':i+1,'hook':hooks[i%len(hooks)],'copy':copy,'proof':proof,'cta':cta,'score':score})
    return {'audience':audience,'offer':offer,'ranked':sorted(out,key=lambda x:x['score'],reverse=True)}
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
