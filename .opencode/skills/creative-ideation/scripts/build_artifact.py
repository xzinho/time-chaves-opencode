#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: creative-ideation
description: "Executa Tension-Recombination Portfolio para responder: quais ideias são simultaneamente novas, pertinentes e testáveis?"
---

# Creative Ideation

## Escopo e gatilhos

Use quando a decisão real for: **quais ideias são simultaneamente novas, pertinentes e testáveis?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Tension-Recombination Portfolio**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Tension-Recombination Portfolio

1. **Desafio/restrições**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Fatos/tensões**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Estímulos distantes**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Divergência por operadores**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Clusters**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Concepts**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Crítica diferida**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Portfólio exploit/explore**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Microteste.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Forced connections**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Inversion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Subtraction**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Analogy transfer**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Morphological box**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Silent brainwriting.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Bloqueio de repertório pede pesquisa. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Grupo hierárquico usa geração silenciosa. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ideia regulada vai a feasibility gate.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: novidade 25, pertinência 25, coerência 15, viabilidade 15, testabilidade 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `tension_bank_csv.md` ou formato nativo equivalente: materializa **`tension-bank.csv`** e deve ser citado pelo artefato principal.
- `morphological_matrix_xlsx.md` ou formato nativo equivalente: materializa **`morphological-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `concept_card_md.md` ou formato nativo equivalente: materializa **`concept-card.md`** e deve ser citado pelo artefato principal.
- `portfolio_map.md` ou formato nativo equivalente: materializa **portfolio map** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **A Technique for Producing Ideas**, James Webb Young (book, força: canonical). Aplicação: Fact gathering, incubation and recombination. Localizador: McGraw-Hill, 1965, ISBN 9780071410946. Consulta: 2026-08-24.
2. **Creative Confidence**, Tom Kelley and David Kelley (book, força: canonical). Aplicação: Divergence, experiments and confidence-building. Localizador: Crown Business, 2013, ISBN 9780385349369. Consulta: 2026-08-24.
3. **Design Kit Methods**, IDEO.org (official, força: primary). Aplicação: Human-centered ideation and field-testing methods. Localizador: https://www.designkit.org/methods. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Tension-Recombination Portfolio

## Pergunta de controle

quais ideias são simultaneamente novas, pertinentes e testáveis?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **desafio/restrições** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **forced connections** responde à pergunta sem extrapolar o dado? Se não, selecione **silent brainwriting.** e declare a troca.
3. Há uma destas exceções: bloqueio de repertório pede pesquisa; grupo hierárquico usa geração silenciosa; ideia regulada vai a feasibility gate.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **quais ideias são simultaneamente novas, pertinentes e testáveis?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Desafio/restrições**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Fatos/tensões**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Estímulos distantes**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Divergência por operadores**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Clusters**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Concepts**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Crítica diferida**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Portfólio exploit/explore**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Microteste.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Forced connections**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Inversion**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Subtraction**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Analogy transfer**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Morphological box**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Silent brainwriting.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Bloqueio de repertório pede pesquisa. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Grupo hierárquico usa geração silenciosa. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ideia regulada vai a feasibility gate.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “fatos/tensões” cita evidência identificada, aplica “forced connections”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Tension-Recombination Portfolio foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `tension_bank_csv.md` ou formato nativo equivalente: materializa **`tension-bank.csv`** e deve ser citado pelo artefato principal.
- `morphological_matrix_xlsx.md` ou formato nativo equivalente: materializa **`morphological-matrix.xlsx`** e deve ser citado pelo artefato principal.
- `concept_card_md.md` ou formato nativo equivalente: materializa **`concept-card.md`** e deve ser citado pelo artefato principal.
- `portfolio_map.md` ou formato nativo equivalente: materializa **portfolio map** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: novidade 25, pertinência 25, coerência 15, viabilidade 15, testabilidade 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **A Technique for Producing Ideas**, James Webb Young (book, força: canonical). Aplicação: Fact gathering, incubation and recombination. Localizador: McGraw-Hill, 1965, ISBN 9780071410946. Consulta: 2026-08-24.
2. **Creative Confidence**, Tom Kelley and David Kelley (book, força: canonical). Aplicação: Divergence, experiments and confidence-building. Localizador: Crown Business, 2013, ISBN 9780385349369. Consulta: 2026-08-24.
3. **Design Kit Methods**, IDEO.org (official, força: primary). Aplicação: Human-centered ideation and field-testing methods. Localizador: https://www.designkit.org/methods. Consulta: 2026-08-24.


# Template — Tension-Recombination Portfolio

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | quais ideias são simultaneamente novas, pertinentes e testáveis? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Desafio/restrições

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Fatos/tensões

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Estímulos distantes

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Divergência por operadores

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Clusters

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Concepts

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Crítica diferida

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Portfólio exploit/explore

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Microteste.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Tension-Recombination Portfolio

### `tension-bank.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `morphological-matrix.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `concept-card.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### portfolio map

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

novidade 25, pertinência 25, coerência 15, viabilidade 15, testabilidade 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `bloqueio de repertório pede pesquisa; grupo hierárquico usa geração silenciosa; ideia regulada vai a feasibility gate.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "lenses": [
    "inversion",
    "analogy",
    "constraint",
    "combination",
    "extreme"
  ]
}


{
  "criteria": [
    "novelty",
    "relevance",
    "feasibility"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Tension-Recombination Portfolio",
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
        "desafio_restri_es",
        "fatos_tens_es",
        "est_mulos_distantes",
        "diverg_ncia_por_operadores",
        "clusters",
        "concepts",
        "cr_tica_diferida",
        "portf_lio_exploit_explore",
        "microteste"
      ],
      "properties": {
        "desafio_restri_es": {
          "type": "string",
          "minLength": 3
        },
        "fatos_tens_es": {
          "type": "string",
          "minLength": 3
        },
        "est_mulos_distantes": {
          "type": "string",
          "minLength": 3
        },
        "diverg_ncia_por_operadores": {
          "type": "string",
          "minLength": 3
        },
        "clusters": {
          "type": "string",
          "minLength": 3
        },
        "concepts": {
          "type": "string",
          "minLength": 3
        },
        "cr_tica_diferida": {
          "type": "string",
          "minLength": 3
        },
        "portf_lio_exploit_explore": {
          "type": "string",
          "minLength": 3
        },
        "microteste": {
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
    "behavior": "creative-ideation:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "creative-ideation:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "creative-ideation:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "missing problem"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "at least five ideas required"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "duplicate idea"
  }
]


{
  "ideas": [
    {
      "title": "Ideia 0",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 1",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 2",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 3",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 4",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    }
  ]
}


{
  "problem": "reduzir churn",
  "ideas": []
}


{
  "problem": "reduzir churn",
  "ideas": [
    {
      "title": "Ideia 0",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 0",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 2",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 3",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 4",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    }
  ]
}


{
  "problem": "reduzir churn",
  "ideas": [
    {
      "title": "Ideia 0",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 1",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 2",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 3",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 4",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    }
  ]
}


{
  "problem": "reduzir churn",
  "ideas": [
    {
      "title": "Ideia 0",
      "scores": {
        "novelty": 5,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 1",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 2",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 3",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 4",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    }
  ]
}


{
  "problem": "aumentar retenção",
  "ideas": [
    {
      "title": "Ideia 0",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 1",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 2",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 3",
      "scores": {
        "novelty": 4,
        "relevance": 4,
        "feasibility": 3
      }
    },
    {
      "title": "Ideia 4",
      "scores": {
        "novelty": 3,
        "relevance": 4,
        "feasibility": 3
      }
    }
  ]
}


## 11. creative-ideation — Tension-Recombination Portfolio

- **Decisão:** quais ideias são simultaneamente novas, pertinentes e testáveis?
- **Fluxo:** desafio/restrições → fatos/tensões → estímulos distantes → divergência por operadores → clusters → concepts → crítica diferida → portfólio exploit/explore → microteste.
- **Técnicas:** forced connections; inversion; subtraction; analogy transfer; morphological box; silent brainwriting.
- **Exceções:** bloqueio de repertório pede pesquisa; grupo hierárquico usa geração silenciosa; ideia regulada vai a feasibility gate.
- **Rubrica:** novidade 25, pertinência 25, coerência 15, viabilidade 15, testabilidade 20.
- **Recursos:** `tension-bank.csv`, `morphological-matrix.xlsx`, `concept-card.md`, portfolio map.


[
  {
    "type": "book",
    "title": "A Technique for Producing Ideas",
    "author": "James Webb Young",
    "reference": "McGraw-Hill, 1965, ISBN 9780071410946",
    "strength": "canonical",
    "use": "Fact gathering, incubation and recombination"
  },
  {
    "type": "book",
    "title": "Creative Confidence",
    "author": "Tom Kelley and David Kelley",
    "reference": "Crown Business, 2013, ISBN 9780385349369",
    "strength": "canonical",
    "use": "Divergence, experiments and confidence-building"
  },
  {
    "type": "official",
    "title": "Design Kit Methods",
    "author": "IDEO.org",
    "url": "https://www.designkit.org/methods",
    "strength": "primary",
    "use": "Human-centered ideation and field-testing methods"
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
    problem=req(data,'problem'); ideas=data.get('ideas'); lenses=assets['lenses']['lenses']
    if not isinstance(ideas,list) or len(ideas)<5: fail('at least five ideas required')
    seen=set(); ranked=[]
    for i,idea in enumerate(ideas):
        title=req(idea,'title').strip().lower()
        if title in seen: fail('duplicate idea')
        seen.add(title); scores=idea.get('scores',{})
        if set(assets['scorecard']['criteria'])-set(scores): fail('incomplete scorecard')
        total=sum(float(scores[k]) for k in assets['scorecard']['criteria'])/3
        ranked.append({'title':idea['title'],'lens':lenses[i%len(lenses)],'score':round(total,2)})
    return {'problem':problem,'portfolio':sorted(ranked,key=lambda x:x['score'],reverse=True)}
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
