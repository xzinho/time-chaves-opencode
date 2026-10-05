#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: brazilian-legal-research
description: "Executa Questão-Norma-Precedente para responder: qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?"
---

# Brazilian Legal Research

## Escopo e gatilhos

Use quando a decisão real for: **qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Questão-Norma-Precedente**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Questão-Norma-Precedente

1. **Fatos/foro/data**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Issues**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Hierarquia normativa**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Vigência/alterações**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Jurisprudência por holding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Correntes e distinções**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Conclusão condicionada**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Citator log.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Irac adaptado**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Árvore de autoridade**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cadeia de vigência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ratio vs obiter**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Tratamento de precedente contrário.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- Segredo/privacidade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Decisão monocrática não equivale a precedente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Tema repetitivo/repercussão geral muda peso. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Escalar prática jurídica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: autoridade 25, vigência 20, aderência fática 20, tratamento contrário 15, citações recuperáveis 20.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `authority_table_csv.md` ou formato nativo equivalente: materializa **`authority-table.csv`** e deve ser citado pelo artefato principal.
- `case_brief_md.md` ou formato nativo equivalente: materializa **`case-brief.md`** e deve ser citado pelo artefato principal.
- `citation_validator_py.md` ou formato nativo equivalente: materializa **`citation-validator.py`** e deve ser citado pelo artefato principal.
- `open_questions_md.md` ou formato nativo equivalente: materializa **`open-questions.md`** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Portal da Legislação**, Presidência da República do Brasil (official, força: primary). Aplicação: Authoritative consolidated federal legislation. Localizador: https://www4.planalto.gov.br/legislacao/. Consulta: 2026-08-24.
2. **Pesquisa de Jurisprudência**, STJ (official, força: primary). Aplicação: Binding context, precedent and temporal validity. Localizador: https://scon.stj.jus.br/SCON/. Consulta: 2026-08-24.
3. **Pesquisa de Jurisprudência**, STF (official, força: primary). Aplicação: Constitutional holdings and repercussão geral. Localizador: https://jurisprudencia.stf.jus.br/. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Questão-Norma-Precedente

## Pergunta de controle

qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **fatos/foro/data** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **IRAC adaptado** responde à pergunta sem extrapolar o dado? Se não, selecione **tratamento de precedente contrário.** e declare a troca.
3. Há uma destas exceções: segredo/privacidade; decisão monocrática não equivale a precedente; tema repetitivo/repercussão geral muda peso; escalar prática jurídica.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Fatos/foro/data**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Issues**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Hierarquia normativa**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Vigência/alterações**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Jurisprudência por holding**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Correntes e distinções**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Conclusão condicionada**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Citator log.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Irac adaptado**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Árvore de autoridade**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cadeia de vigência**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Ratio vs obiter**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Tratamento de precedente contrário.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Segredo/privacidade. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Decisão monocrática não equivale a precedente. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Tema repetitivo/repercussão geral muda peso. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Escalar prática jurídica.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “issues” cita evidência identificada, aplica “IRAC adaptado”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Questão-Norma-Precedente foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `authority_table_csv.md` ou formato nativo equivalente: materializa **`authority-table.csv`** e deve ser citado pelo artefato principal.
- `case_brief_md.md` ou formato nativo equivalente: materializa **`case-brief.md`** e deve ser citado pelo artefato principal.
- `citation_validator_py.md` ou formato nativo equivalente: materializa **`citation-validator.py`** e deve ser citado pelo artefato principal.
- `open_questions_md.md` ou formato nativo equivalente: materializa **`open-questions.md`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: autoridade 25, vigência 20, aderência fática 20, tratamento contrário 15, citações recuperáveis 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Portal da Legislação**, Presidência da República do Brasil (official, força: primary). Aplicação: Authoritative consolidated federal legislation. Localizador: https://www4.planalto.gov.br/legislacao/. Consulta: 2026-08-24.
2. **Pesquisa de Jurisprudência**, STJ (official, força: primary). Aplicação: Binding context, precedent and temporal validity. Localizador: https://scon.stj.jus.br/SCON/. Consulta: 2026-08-24.
3. **Pesquisa de Jurisprudência**, STF (official, força: primary). Aplicação: Constitutional holdings and repercussão geral. Localizador: https://jurisprudencia.stf.jus.br/. Consulta: 2026-08-24.


# Template — Questão-Norma-Precedente

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Fatos/foro/data

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Issues

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Hierarquia normativa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Vigência/alterações

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Jurisprudência por holding

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Correntes e distinções

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Conclusão condicionada

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Citator log.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Questão-Norma-Precedente

### `authority-table.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `case-brief.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `citation-validator.py`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `open-questions.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

autoridade 25, vigência 20, aderência fática 20, tratamento contrário 15, citações recuperáveis 20.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `segredo/privacidade; decisão monocrática não equivale a precedente; tema repetitivo/repercussão geral muda peso; escalar prática jurídica.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "authorities": [
    {
      "type": "lei",
      "identifier": "Lei 13.709/2018",
      "article": "art. 7º",
      "url": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm",
      "accessed": "2026-08-24"
    }
  ]
}


{
  "required": [
    "type",
    "identifier",
    "article",
    "url",
    "accessed"
  ],
  "official_hosts": [
    "planalto.gov.br",
    "stf.jus.br",
    "stj.jus.br"
  ]
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Questão-Norma-Precedente",
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
        "fatos_foro_data",
        "issues",
        "hierarquia_normativa",
        "vig_ncia_altera_es",
        "jurisprud_ncia_por_holding",
        "correntes_e_distin_es",
        "conclus_o_condicionada",
        "citator_log"
      ],
      "properties": {
        "fatos_foro_data": {
          "type": "string",
          "minLength": 3
        },
        "issues": {
          "type": "string",
          "minLength": 3
        },
        "hierarquia_normativa": {
          "type": "string",
          "minLength": 3
        },
        "vig_ncia_altera_es": {
          "type": "string",
          "minLength": 3
        },
        "jurisprud_ncia_por_holding": {
          "type": "string",
          "minLength": 3
        },
        "correntes_e_distin_es": {
          "type": "string",
          "minLength": 3
        },
        "conclus_o_condicionada": {
          "type": "string",
          "minLength": 3
        },
        "citator_log": {
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
    "behavior": "brazilian-legal-research:domain-scenario-1",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    }
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "brazilian-legal-research:domain-scenario-2:resource-variant-a",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "authorities.json",
      "path": "authorities.0.type",
      "value": "lei alternative"
    }
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "brazilian-legal-research:domain-scenario-3:resource-variant-b",
    "expect": {
      "exit": 0,
      "resources_consumed": 2
    },
    "mutate": {
      "asset": "authorities.json",
      "path": "authorities.0.identifier",
      "value": "Lei 13.709/2018 alternative"
    }
  },
  {
    "id": "negative-1",
    "fixture": "negative-1.json",
    "mutate": {
      "asset": "authorities.json",
      "path": "authorities.0.url",
      "value": "https://example.com/law"
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "brazilian-legal-research:closed-failure-1"
  },
  {
    "id": "negative-2",
    "fixture": "negative-2.json",
    "mutate": {
      "asset": "authorities.json",
      "path": "authorities.0.article",
      "value": ""
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "brazilian-legal-research:closed-failure-2"
  },
  {
    "id": "negative-3",
    "fixture": "negative-3.json",
    "mutate": {
      "asset": "authorities.json",
      "path": "authorities.0.identifier",
      "value": "Blog 1"
    },
    "expect": {
      "exit_nonzero": true,
      "no_artifact": true
    },
    "kind": "negative",
    "invariant": "brazilian-legal-research:closed-failure-3"
  }
]


{
  "objective": "Executar brazilian-legal-research com evidência verificável | rejeição 1"
}


{
  "objective": "Executar brazilian-legal-research com evidência verificável | rejeição 2"
}


{
  "objective": "Executar brazilian-legal-research com evidência verificável | rejeição 3"
}


{
  "objective": "Executar brazilian-legal-research com evidência verificável | cenário executável 1"
}


{
  "objective": "Executar brazilian-legal-research com evidência verificável | cenário executável 2"
}


{
  "objective": "Executar brazilian-legal-research com evidência verificável | cenário executável 3"
}


## 4. brazilian-legal-research — Questão-Norma-Precedente

- **Decisão:** qual resposta é sustentada pelas fontes vigentes, com qual grau de confiança e quais divergências?
- **Fluxo:** fatos/foro/data → issues → hierarquia normativa → vigência/alterações → jurisprudência por holding → correntes e distinções → conclusão condicionada → citator log.
- **Técnicas:** IRAC adaptado; árvore de autoridade; cadeia de vigência; ratio vs obiter; tratamento de precedente contrário.
- **Exceções:** segredo/privacidade; decisão monocrática não equivale a precedente; tema repetitivo/repercussão geral muda peso; escalar prática jurídica.
- **Rubrica:** autoridade 25, vigência 20, aderência fática 20, tratamento contrário 15, citações recuperáveis 20.
- **Recursos:** `authority-table.csv`, `case-brief.md`, `citation-validator.py`, `open-questions.md`.


[
  {
    "type": "official",
    "title": "Portal da Legislação",
    "author": "Presidência da República do Brasil",
    "url": "https://www4.planalto.gov.br/legislacao/",
    "strength": "primary",
    "use": "Authoritative consolidated federal legislation"
  },
  {
    "type": "official",
    "title": "Pesquisa de Jurisprudência",
    "author": "STJ",
    "url": "https://scon.stj.jus.br/SCON/",
    "strength": "primary",
    "use": "Binding context, precedent and temporal validity"
  },
  {
    "type": "official",
    "title": "Pesquisa de Jurisprudência",
    "author": "STF",
    "url": "https://jurisprudencia.stf.jus.br/",
    "strength": "primary",
    "use": "Constitutional holdings and repercussão geral"
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
 A=load("assets/authorities.json"); B=load("assets/citation-schema.json")
 from urllib.parse import urlparse
 authorities=A["authorities"]; required=B["required"]
 citations=[]
 for a in authorities:
     if any(not str(a.get(k," ")).strip() for k in required): fail("incomplete legal citation")
     host=urlparse(a["url"]).hostname or ""
     if not any(host==h or host.endswith("."+h) for h in B["official_hosts"]): fail("non-official authority")
     if not (a["identifier"].startswith(("Lei ","Decreto ","RE ","REsp "))): fail("unsupported authority identifier")
     citations.append({**a,"citation":f'{a["identifier"]}, {a["article"]} (acesso {a["accessed"]})'})
 artifact={"kind":"brazilian-legal-research","jurisdiction":"BR","authorities":citations,"propositions_supported":len(citations)}
 artifact["objective"]=request["objective"].strip(); artifact["resources"]=["assets/authorities.json","assets/citation-schema.json"]
 out=pathlib.Path(ns.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
