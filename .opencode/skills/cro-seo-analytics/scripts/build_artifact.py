#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: cro-seo-analytics
description: "Executa Intent-to-Experiment Chain para responder: qual ruptura no caminho search→landing→action tem maior impacto causal provável?"
---

# Cro Seo Analytics

## Escopo e gatilhos

Use quando a decisão real for: **qual ruptura no caminho search→landing→action tem maior impacto causal provável?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Intent-to-Experiment Chain**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Intent-to-Experiment Chain

1. **Query/intent clusters**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Technical/indexability**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Serp promise**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Landing continuity**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Event qa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Funnel/cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Evidence-backed hypothesis**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Experiment design**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Readout.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Content decay segmentation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query-page mapping**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Funnel leakage**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Instrumentation validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ice with evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sequential guardrails.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Baixo tráfego usa qualitative/pooled tests. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mudança seo não recebe causalidade instantânea. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/internal traffic filtrado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: integridade de dados 25, aderência à intenção 20, hipótese 20, desenho 20, impacto 15.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `query_page_map_csv.md` ou formato nativo equivalente: materializa **`query-page-map.csv`** e deve ser citado pelo artefato principal.
- `event_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`event-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `experiment_card_md.md` ou formato nativo equivalente: materializa **`experiment-card.md`** e deve ser citado pelo artefato principal.
- `seo_cro_backlog_xlsx.md` ou formato nativo equivalente: materializa **`seo-cro-backlog.xlsx`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Google Search Essentials**, Google Search Central (official, força: primary). Aplicação: Search eligibility and spam-policy gate. Localizador: https://developers.google.com/search/docs/essentials. Consulta: 2026-08-24.
2. **Google Analytics 4 Developer Documentation**, Google (official, força: primary). Aplicação: Event, conversion and attribution instrumentation. Localizador: https://developers.google.com/analytics/devguides/collection/ga4. Consulta: 2026-08-24.
3. **You Should Test That!**, Chris Goward (book, força: canonical). Aplicação: Hypothesis prioritization and controlled experimentation. Localizador: Wiley, 2013, ISBN 9781118301302. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Intent-to-Experiment Chain

## Pergunta de controle

qual ruptura no caminho search→landing→action tem maior impacto causal provável?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **query/intent clusters** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **content decay segmentation** responde à pergunta sem extrapolar o dado? Se não, selecione **sequential guardrails.** e declare a troca.
3. Há uma destas exceções: baixo tráfego usa qualitative/pooled tests; mudança SEO não recebe causalidade instantânea; bot/internal traffic filtrado.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual ruptura no caminho search→landing→action tem maior impacto causal provável?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Query/intent clusters**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Technical/indexability**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Serp promise**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Landing continuity**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Event qa**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Funnel/cohort**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Evidence-backed hypothesis**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Experiment design**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Readout.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Content decay segmentation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Query-page mapping**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Funnel leakage**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Instrumentation validation**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ice with evidence**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Sequential guardrails.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Baixo tráfego usa qualitative/pooled tests. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Mudança seo não recebe causalidade instantânea. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Bot/internal traffic filtrado.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “technical/indexability” cita evidência identificada, aplica “content decay segmentation”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Intent-to-Experiment Chain foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `query_page_map_csv.md` ou formato nativo equivalente: materializa **`query-page-map.csv`** e deve ser citado pelo artefato principal.
- `event_taxonomy_yaml.md` ou formato nativo equivalente: materializa **`event-taxonomy.yaml`** e deve ser citado pelo artefato principal.
- `experiment_card_md.md` ou formato nativo equivalente: materializa **`experiment-card.md`** e deve ser citado pelo artefato principal.
- `seo_cro_backlog_xlsx.md` ou formato nativo equivalente: materializa **`seo-cro-backlog.xlsx`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: integridade de dados 25, aderência à intenção 20, hipótese 20, desenho 20, impacto 15.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Google Search Essentials**, Google Search Central (official, força: primary). Aplicação: Search eligibility and spam-policy gate. Localizador: https://developers.google.com/search/docs/essentials. Consulta: 2026-08-24.
2. **Google Analytics 4 Developer Documentation**, Google (official, força: primary). Aplicação: Event, conversion and attribution instrumentation. Localizador: https://developers.google.com/analytics/devguides/collection/ga4. Consulta: 2026-08-24.
3. **You Should Test That!**, Chris Goward (book, força: canonical). Aplicação: Hypothesis prioritization and controlled experimentation. Localizador: Wiley, 2013, ISBN 9781118301302. Consulta: 2026-08-24.


# Template — Intent-to-Experiment Chain

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual ruptura no caminho search→landing→action tem maior impacto causal provável? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Query/intent clusters

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Technical/indexability

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Serp promise

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Landing continuity

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Event qa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Funnel/cohort

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Evidence-backed hypothesis

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Experiment design

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 9. Readout.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Intent-to-Experiment Chain

### `query-page-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `event-taxonomy.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `experiment-card.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `seo-cro-backlog.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

integridade de dados 25, aderência à intenção 20, hipótese 20, desenho 20, impacto 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `baixo tráfego usa qualitative/pooled tests; mudança SEO não recebe causalidade instantânea; bot/internal traffic filtrado.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "stages": [
    {
      "name": "sessions",
      "value": 1000
    },
    {
      "name": "leads",
      "value": 120
    },
    {
      "name": "sales",
      "value": 18
    }
  ]
}


{
  "metrics": {
    "impressions": 5000,
    "clicks": 300,
    "conversions": 18
  },
  "required": [
    "impressions",
    "clicks",
    "conversions"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Intent-to-Experiment Chain",
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
        "query_intent_clusters",
        "technical_indexability",
        "serp_promise",
        "landing_continuity",
        "event_qa",
        "funnel_cohort",
        "evidence_backed_hypothesis",
        "experiment_design",
        "readout"
      ],
      "properties": {
        "query_intent_clusters": {
          "type": "string",
          "minLength": 3
        },
        "technical_indexability": {
          "type": "string",
          "minLength": 3
        },
        "serp_promise": {
          "type": "string",
          "minLength": 3
        },
        "landing_continuity": {
          "type": "string",
          "minLength": 3
        },
        "event_qa": {
          "type": "string",
          "minLength": 3
        },
        "funnel_cohort": {
          "type": "string",
          "minLength": 3
        },
        "evidence_backed_hypothesis": {
          "type": "string",
          "minLength": 3
        },
        "experiment_design": {
          "type": "string",
          "minLength": 3
        },
        "readout": {
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
    "behavior": "cro-seo-analytics:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "cro-seo-analytics:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "funnel.json",
      "path": "stages.0.name",
      "value": "sessions alternative"
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "cro-seo-analytics:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "funnel.json",
      "path": "stages.0.value",
      "value": 1001
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "funnel.json",
      "path": "stages.1.value",
      "value": 1200
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "cro-seo-analytics:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "seo-metrics.json",
      "path": "metrics.clicks",
      "value": 6000
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "cro-seo-analytics:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "seo-metrics.json",
      "path": "metrics.conversions",
      "value": 400
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "cro-seo-analytics:closed-failure-3"
  }
]


{
  "objective": "Executar cro-seo-analytics com evidência verificável | rejeição 1"
}


{
  "objective": "Executar cro-seo-analytics com evidência verificável | rejeição 2"
}


{
  "objective": "Executar cro-seo-analytics com evidência verificável | rejeição 3"
}


{
  "objective": "Executar cro-seo-analytics com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar cro-seo-analytics com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar cro-seo-analytics com evidência verificável | cenário executável 3"
}


## 12. cro-seo-analytics — Intent-to-Experiment Chain

- **Decisão:** qual ruptura no caminho search→landing→action tem maior impacto causal provável?
- **Fluxo:** query/intent clusters → technical/indexability → SERP promise → landing continuity → event QA → funnel/cohort → evidence-backed hypothesis → experiment design → readout.
- **Técnicas:** content decay segmentation; query-page mapping; funnel leakage; instrumentation validation; ICE with evidence; sequential guardrails.
- **Exceções:** baixo tráfego usa qualitative/pooled tests; mudança SEO não recebe causalidade instantânea; bot/internal traffic filtrado.
- **Rubrica:** integridade de dados 25, aderência à intenção 20, hipótese 20, desenho 20, impacto 15.
- **Recursos:** `query-page-map.csv`, `event-taxonomy.yaml`, `experiment-card.md`, `seo-cro-backlog.xlsx`.


[
  {
    "type": "official",
    "title": "Google Search Essentials",
    "author": "Google Search Central",
    "url": "https://developers.google.com/search/docs/essentials",
    "strength": "primary",
    "use": "Search eligibility and spam-policy gate"
  },
  {
    "type": "official",
    "title": "Google Analytics 4 Developer Documentation",
    "author": "Google",
    "url": "https://developers.google.com/analytics/devguides/collection/ga4",
    "strength": "primary",
    "use": "Event, conversion and attribution instrumentation"
  },
  {
    "type": "book",
    "title": "You Should Test That!",
    "author": "Chris Goward",
    "reference": "Wiley, 2013, ISBN 9781118301302",
    "strength": "canonical",
    "use": "Hypothesis prioritization and controlled experimentation"
  }
]"""
import argparse,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(name):
 p=ROOT/name
 try: return json.loads(p.read_text())
 except Exception as e: raise SystemExit(f"resource error {name}: {e}")
def fail(message): raise SystemExit(message)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True); ns=ap.parse_args()
 try: request=json.loads(pathlib.Path(ns.input).read_text())
 except Exception as e: fail(f"invalid input: {e}")
 if not isinstance(request,dict) or not request.get("objective") or not str(request["objective"]).strip(): fail("objective required")
 A=load("assets/funnel.json"); B=load("assets/seo-metrics.json")
 stages=A["stages"]; metrics=B["metrics"]
 values=[x["value"] for x in stages]
 if any(not isinstance(v,(int,float)) or v<0 for v in values) or any(values[i+1]>values[i] for i in range(len(values)-1)): fail("invalid funnel monotonicity")
 if any(k not in metrics or metrics[k]<0 for k in B["required"]): fail("missing SEO metric")
 if metrics["clicks"]>metrics["impressions"]: fail("clicks exceed impressions")
 if metrics["conversions"]>metrics["clicks"]: fail("conversions exceed clicks")
 rates=[{"from":stages[i]["name"],"to":stages[i+1]["name"],"rate":round(values[i+1]/values[i],4) if values[i] else 0} for i in range(len(stages)-1)]
 artifact={"kind":"cro-seo-scorecard","funnel_rates":rates,"ctr":round(metrics["clicks"]/metrics["impressions"],4),"conversion_rate":round(metrics["conversions"]/metrics["clicks"],4),"data_quality":"validated"}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/funnel.json","assets/seo-metrics.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
