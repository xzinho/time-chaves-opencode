#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: concept-visualizer
description: "Executa Relation-to-Form Compiler para responder: qual forma visual representa a relação essencial sem distorcê-la?"
---

# Concept Visualizer

## Escopo e gatilhos

Use quando a decisão real for: **qual forma visual representa a relação essencial sem distorcê-la?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Relation-to-Form Compiler**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Relation-to-Form Compiler

1. **Frase nuclear**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Entidades/relações**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tipo (hierarquia, fluxo, ciclo, mapa, matriz, causalidade)**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Nível de abstração**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Layout**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Teste de leitura**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fonte renderizável.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual grammar**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Preattentive hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Label economy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternate-text narrative.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Causalidade exige evidência. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Relações múltiplas podem pedir small multiples. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama denso divide vistas, não reduz fonte.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: fidelidade semântica 30, legibilidade 25, hierarquia 20, economia 15, acessibilidade 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `concept_graph_json.md` ou formato nativo equivalente: materializa **`concept-graph.json`** e deve ser citado pelo artefato principal.
- `diagram_mmd.md` ou formato nativo equivalente: materializa **`diagram.mmd`** e deve ser citado pelo artefato principal.
- `legend_alt_text.md` ou formato nativo equivalente: materializa **legend/alt-text** e deve ser citado pelo artefato principal.
- `card_de_escolha_de_nota_o.md` ou formato nativo equivalente: materializa **card de escolha de notação** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **The Back of the Napkin**, Dan Roam (book, força: canonical). Aplicação: Visual encoding by who/what/how/when/where/why. Localizador: Portfolio, 2008, ISBN 9781591841999. Consulta: 2026-08-24.
2. **Visual Thinking**, Rudolf Arnheim (book, força: canonical). Aplicação: Perceptual reasoning and abstraction. Localizador: University of California Press, 1969, ISBN 9780520242265. Consulta: 2026-08-24.
3. **Diagram as Code**, Mermaid (official, força: primary). Aplicação: Reproducible concept diagrams. Localizador: https://mermaid.js.org/intro/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Relation-to-Form Compiler

## Pergunta de controle

qual forma visual representa a relação essencial sem distorcê-la?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **frase nuclear** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **progressive disclosure** responde à pergunta sem extrapolar o dado? Se não, selecione **alternate-text narrative.** e declare a troca.
3. Há uma destas exceções: causalidade exige evidência; relações múltiplas podem pedir small multiples; diagrama denso divide vistas, não reduz fonte.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual forma visual representa a relação essencial sem distorcê-la?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Frase nuclear**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Entidades/relações**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Tipo (hierarquia, fluxo, ciclo, mapa, matriz, causalidade)**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Nível de abstração**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Layout**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Teste de leitura**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Fonte renderizável.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Progressive disclosure**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Visual grammar**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Preattentive hierarchy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Label economy**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Alternate-text narrative.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Causalidade exige evidência. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Relações múltiplas podem pedir small multiples. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama denso divide vistas, não reduz fonte.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “entidades/relações” cita evidência identificada, aplica “progressive disclosure”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Relation-to-Form Compiler foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `concept_graph_json.md` ou formato nativo equivalente: materializa **`concept-graph.json`** e deve ser citado pelo artefato principal.
- `diagram_mmd.md` ou formato nativo equivalente: materializa **`diagram.mmd`** e deve ser citado pelo artefato principal.
- `legend_alt_text.md` ou formato nativo equivalente: materializa **legend/alt-text** e deve ser citado pelo artefato principal.
- `card_de_escolha_de_nota_o.md` ou formato nativo equivalente: materializa **card de escolha de notação** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: fidelidade semântica 30, legibilidade 25, hierarquia 20, economia 15, acessibilidade 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **The Back of the Napkin**, Dan Roam (book, força: canonical). Aplicação: Visual encoding by who/what/how/when/where/why. Localizador: Portfolio, 2008, ISBN 9781591841999. Consulta: 2026-08-24.
2. **Visual Thinking**, Rudolf Arnheim (book, força: canonical). Aplicação: Perceptual reasoning and abstraction. Localizador: University of California Press, 1969, ISBN 9780520242265. Consulta: 2026-08-24.
3. **Diagram as Code**, Mermaid (official, força: primary). Aplicação: Reproducible concept diagrams. Localizador: https://mermaid.js.org/intro/. Consulta: 2026-08-24.


# Template — Relation-to-Form Compiler

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual forma visual representa a relação essencial sem distorcê-la? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Frase nuclear

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Entidades/relações

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Tipo (hierarquia, fluxo, ciclo, mapa, matriz, causalidade)

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Nível de abstração

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Layout

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Teste de leitura

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Fonte renderizável.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Relation-to-Form Compiler

### `concept-graph.json`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `diagram.mmd`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### legend/alt-text

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### card de escolha de notação

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

fidelidade semântica 30, legibilidade 25, hierarquia 20, economia 15, acessibilidade 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `causalidade exige evidência; relações múltiplas podem pedir small multiples; diagrama denso divide vistas, não reduz fonte.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "semantic": {
    "risk": "#ef4444",
    "decision": "#f59e0b",
    "evidence": "#22c55e"
  }
}


{
  "allowed": [
    "node",
    "edge",
    "group",
    "annotation"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Relation-to-Form Compiler",
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
        "frase_nuclear",
        "entidades_rela_es",
        "tipo_hierarquia_fluxo_ciclo_mapa_matriz_causalidade",
        "n_vel_de_abstra_o",
        "layout",
        "teste_de_leitura",
        "fonte_renderiz_vel"
      ],
      "properties": {
        "frase_nuclear": {
          "type": "string",
          "minLength": 3
        },
        "entidades_rela_es": {
          "type": "string",
          "minLength": 3
        },
        "tipo_hierarquia_fluxo_ciclo_mapa_matriz_causalidade": {
          "type": "string",
          "minLength": 3
        },
        "n_vel_de_abstra_o": {
          "type": "string",
          "minLength": 3
        },
        "layout": {
          "type": "string",
          "minLength": 3
        },
        "teste_de_leitura": {
          "type": "string",
          "minLength": 3
        },
        "fonte_renderiz_vel": {
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
    "behavior": "concept-visualizer:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "concept-visualizer:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "concept-visualizer:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "items required"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "duplicate id"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "dangling edge"
  }
]


{
  "canvas": "decision map",
  "items": []
}


{
  "canvas": "decision map",
  "items": [
    {
      "kind": "node",
      "id": "a",
      "label": "Entrada"
    },
    {
      "kind": "node",
      "id": "a",
      "label": "Decisão"
    },
    {
      "kind": "edge",
      "id": "e",
      "from": "a",
      "to": "b"
    }
  ]
}


{
  "canvas": "decision map",
  "items": [
    {
      "kind": "node",
      "id": "a",
      "label": "Entrada"
    },
    {
      "kind": "node",
      "id": "b",
      "label": "Decisão"
    },
    {
      "kind": "edge",
      "id": "e",
      "from": "a",
      "to": "missing"
    }
  ]
}


{
  "canvas": "decision map",
  "items": [
    {
      "kind": "node",
      "id": "a",
      "label": "Entrada"
    },
    {
      "kind": "node",
      "id": "b",
      "label": "Decisão"
    },
    {
      "kind": "edge",
      "id": "e",
      "from": "a",
      "to": "b"
    }
  ]
}


{
  "canvas": "risk map",
  "items": [
    {
      "kind": "node",
      "id": "a",
      "label": "Entrada"
    },
    {
      "kind": "node",
      "id": "b",
      "label": "Decisão"
    },
    {
      "kind": "edge",
      "id": "e",
      "from": "a",
      "to": "b"
    }
  ]
}


{
  "canvas": "decision map",
  "items": [
    {
      "kind": "node",
      "id": "a",
      "label": "Entrada"
    },
    {
      "kind": "node",
      "id": "b",
      "label": "Escolha crítica"
    },
    {
      "kind": "edge",
      "id": "e",
      "from": "a",
      "to": "b"
    }
  ]
}


## 7. concept-visualizer — Relation-to-Form Compiler

- **Decisão:** qual forma visual representa a relação essencial sem distorcê-la?
- **Fluxo:** frase nuclear → entidades/relações → tipo (hierarquia, fluxo, ciclo, mapa, matriz, causalidade) → nível de abstração → layout → teste de leitura → fonte renderizável.
- **Técnicas:** progressive disclosure; visual grammar; preattentive hierarchy; label economy; alternate-text narrative.
- **Exceções:** causalidade exige evidência; relações múltiplas podem pedir small multiples; diagrama denso divide vistas, não reduz fonte.
- **Rubrica:** fidelidade semântica 30, legibilidade 25, hierarquia 20, economia 15, acessibilidade 10.
- **Recursos:** `concept-graph.json`, `diagram.mmd`, legend/alt-text, card de escolha de notação.


[
  {
    "type": "book",
    "title": "The Back of the Napkin",
    "author": "Dan Roam",
    "reference": "Portfolio, 2008, ISBN 9781591841999",
    "strength": "canonical",
    "use": "Visual encoding by who/what/how/when/where/why"
  },
  {
    "type": "book",
    "title": "Visual Thinking",
    "author": "Rudolf Arnheim",
    "reference": "University of California Press, 1969, ISBN 9780520242265",
    "strength": "canonical",
    "use": "Perceptual reasoning and abstraction"
  },
  {
    "type": "official",
    "title": "Diagram as Code",
    "author": "Mermaid",
    "url": "https://mermaid.js.org/intro/",
    "strength": "primary",
    "use": "Reproducible concept diagrams"
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
    allowed=set(assets['shapes']['allowed']); items=data.get('items')
    if not isinstance(items,list) or len(items)<2: fail('items required')
    ids=set(); nodes=[]; edges=[]
    for item in items:
        kind=req(item,'kind'); ident=req(item,'id')
        if kind not in allowed: fail('unknown visual primitive')
        if ident in ids: fail('duplicate id')
        ids.add(ident); (edges if kind=='edge' else nodes).append(item)
    for e in edges:
        if e.get('from') not in ids or e.get('to') not in ids: fail('dangling edge')
    return {'canvas':req(data,'canvas'),'nodes':nodes,'edges':edges,'palette':assets['palette']['semantic']}
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
