#!/usr/bin/env python3
EMBEDDED_DOMAIN_GUIDE = """---
name: vsl-video-script
description: "Executa Claim-Beat-Retention Script para responder: what sequence earns attention, builds belief and converts within duration/platform constraints?"
---

# Vsl Video Script

## Escopo e gatilhos

Use quando a decisão real for: **what sequence earns attention, builds belief and converts within duration/platform constraints?** A entrega não é um texto genérico: é um pacote auditável produzido pelo método **Claim-Beat-Retention Script**, com evidência, incerteza e próximo passo.

Não use para aconselhamento casual, execução externa automática, nem quando os fatos mínimos do domínio estiverem ausentes. Nos casos regulados, jurídicos, financeiros, privacidade ou segurança, trate o resultado como apoio técnico e preserve o gate humano competente.

## Inputs e outputs

Entradas mínimas: `objective`, `context`, `evidence[]`, `constraints[]`, `owner`, `due_date`. Entradas específicas são derivadas das etapas do fluxo e declaradas em `references/contract.schema.json`. Saídas: artefato principal, recursos reutilizáveis, source map, decision log, QA e handoff.

## Método Claim-Beat-Retention Script

1. **Audience/awareness/offer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Core promise**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Claim-proof inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Hook variants**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Problem stakes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mechanism**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Proof/demo**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objections**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Beat/timecode**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Visual/audio directions**. Registre entrada, transformação, evidência e saída antes de avançar.
12. **Read-time/claim qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

## Técnicas de campo

- **Open loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Concrete demonstration**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pattern interrupt**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof pacing**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection stack**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cta singularity.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Exceções e escalonamento

- No fake scarcity. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Testimonial claims verified. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Short form compresses beats, not logic. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Spoken cadence tested aloud.. Marque a condição no artefato e acione o gate indicado antes do handoff.

## Rubrica e falhas comuns

Rubrica: hook 20, belief progression 20, proof 20, retention pacing 15, offer/CTA 15, compliance 10.. Reprove evidência sem origem, inferência apresentada como fato, cálculo sem unidade/período, decisão sem alternativa, recurso listado mas não usado, owner/prazo ausente ou placeholder. Uma dimensão crítica zerada bloqueia a entrega mesmo com nota total alta.

## Recursos relacionados

- `vsl_beat_sheet_csv.md` ou formato nativo equivalente: materializa **`vsl-beat-sheet.csv`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `broll_map_md.md` ou formato nativo equivalente: materializa **`broll-map.md`** e deve ser citado pelo artefato principal.
- `timecoded_script_and_variants.md` ou formato nativo equivalente: materializa **timecoded script and variants** e deve ser citado pelo artefato principal.

Leia `references/playbook.md`, valide `references/contract.schema.json`, preencha `assets/output-template.md` e, quando desejar geração determinística, execute `scripts/build_artifact.py`.

## Source map clean-room

1. **Save the Cat!**, Blake Snyder (book, força: canonical). Aplicação: Beat architecture and pacing, adapted clean-room. Localizador: Michael Wiese Productions, 2005, ISBN 9781932907001. Consulta: 2026-08-24.
2. **YouTube Creator Academy**, YouTube (official, força: primary). Aplicação: Audience retention, packaging and platform constraints. Localizador: https://creatoracademy.youtube.com/. Consulta: 2026-08-24.
3. **Made to Stick**, Chip Heath and Dan Heath (book, força: canonical). Aplicação: Concrete, credible and emotionally memorable messages. Localizador: Random House, 2007, ISBN 9781400064281. Consulta: 2026-08-24.

Síntese original. Nenhuma fonte paga ou framework proprietário foi reproduzido extensamente.


# Playbook operacional — Claim-Beat-Retention Script

## Pergunta de controle

what sequence earns attention, builds belief and converts within duration/platform constraints?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **audience/awareness/offer** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **open loop** responde à pergunta sem extrapolar o dado? Se não, selecione **CTA singularity.** e declare a troca.
3. Há uma destas exceções: no fake scarcity; testimonial claims verified; short form compresses beats, not logic; spoken cadence tested aloud.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what sequence earns attention, builds belief and converts within duration/platform constraints?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Audience/awareness/offer**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Core promise**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Claim-proof inventory**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Hook variants**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Problem stakes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Mechanism**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Proof/demo**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Objections**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Offer/cta**. Registre entrada, transformação, evidência e saída antes de avançar.
10. **Beat/timecode**. Registre entrada, transformação, evidência e saída antes de avançar.
11. **Visual/audio directions**. Registre entrada, transformação, evidência e saída antes de avançar.
12. **Read-time/claim qa.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Open loop**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Concrete demonstration**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Pattern interrupt**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Proof pacing**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Objection stack**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Cta singularity.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- No fake scarcity. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Testimonial claims verified. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Short form compresses beats, not logic. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Spoken cadence tested aloud.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “core promise” cita evidência identificada, aplica “open loop”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Claim-Beat-Retention Script foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `vsl_beat_sheet_csv.md` ou formato nativo equivalente: materializa **`vsl-beat-sheet.csv`** e deve ser citado pelo artefato principal.
- `claim_proof_ledger_csv.md` ou formato nativo equivalente: materializa **`claim-proof-ledger.csv`** e deve ser citado pelo artefato principal.
- `broll_map_md.md` ou formato nativo equivalente: materializa **`broll-map.md`** e deve ser citado pelo artefato principal.
- `timecoded_script_and_variants.md` ou formato nativo equivalente: materializa **timecoded script and variants** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: hook 20, belief progression 20, proof 20, retention pacing 15, offer/CTA 15, compliance 10.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **Save the Cat!**, Blake Snyder (book, força: canonical). Aplicação: Beat architecture and pacing, adapted clean-room. Localizador: Michael Wiese Productions, 2005, ISBN 9781932907001. Consulta: 2026-08-24.
2. **YouTube Creator Academy**, YouTube (official, força: primary). Aplicação: Audience retention, packaging and platform constraints. Localizador: https://creatoracademy.youtube.com/. Consulta: 2026-08-24.
3. **Made to Stick**, Chip Heath and Dan Heath (book, força: canonical). Aplicação: Concrete, credible and emotionally memorable messages. Localizador: Random House, 2007, ISBN 9781400064281. Consulta: 2026-08-24.


# Template — Claim-Beat-Retention Script

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | what sequence earns attention, builds belief and converts within duration/platform constraints? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Audience/awareness/offer

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Core promise

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Claim-proof inventory

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Hook variants

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Problem stakes

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Mechanism

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Proof/demo

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Objections

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

### 10. Beat/timecode

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 11. Visual/audio directions

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 12. Read-time/claim qa.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Claim-Beat-Retention Script

### `vsl-beat-sheet.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `claim-proof-ledger.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `broll-map.md`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### timecoded script and variants

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

hook 20, belief progression 20, proof 20, retention pacing 15, offer/CTA 15, compliance 10.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `no fake scarcity; testimonial claims verified; short form compresses beats, not logic; spoken cadence tested aloud.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.


{
  "beats": [
    "hook",
    "problem",
    "stakes",
    "mechanism",
    "proof",
    "offer",
    "cta"
  ]
}


{
  "wpm": 150,
  "max_seconds": 180
}


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claim-Beat-Retention Script",
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
        "audience_awareness_offer",
        "core_promise",
        "claim_proof_inventory",
        "hook_variants",
        "problem_stakes",
        "mechanism",
        "proof_demo",
        "objections",
        "offer_cta",
        "beat_timecode",
        "visual_audio_directions",
        "read_time_claim_qa"
      ],
      "properties": {
        "audience_awareness_offer": {
          "type": "string",
          "minLength": 3
        },
        "core_promise": {
          "type": "string",
          "minLength": 3
        },
        "claim_proof_inventory": {
          "type": "string",
          "minLength": 3
        },
        "hook_variants": {
          "type": "string",
          "minLength": 3
        },
        "problem_stakes": {
          "type": "string",
          "minLength": 3
        },
        "mechanism": {
          "type": "string",
          "minLength": 3
        },
        "proof_demo": {
          "type": "string",
          "minLength": 3
        },
        "objections": {
          "type": "string",
          "minLength": 3
        },
        "offer_cta": {
          "type": "string",
          "minLength": 3
        },
        "beat_timecode": {
          "type": "string",
          "minLength": 3
        },
        "visual_audio_directions": {
          "type": "string",
          "minLength": 3
        },
        "read_time_claim_qa": {
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
    "behavior": "vsl-video-script:positive-branch-1"
  },
  {
    "id": "positive-2",
    "kind": "positive",
    "fixture": "positive-2.json",
    "behavior": "vsl-video-script:positive-branch-2"
  },
  {
    "id": "positive-3",
    "kind": "positive",
    "fixture": "positive-3.json",
    "behavior": "vsl-video-script:positive-branch-3"
  },
  {
    "id": "negative-1",
    "kind": "negative",
    "fixture": "negative-1.json",
    "invariant": "seven-beat VSL required"
  },
  {
    "id": "negative-2",
    "kind": "negative",
    "fixture": "negative-2.json",
    "invariant": "invalid or duplicate beat"
  },
  {
    "id": "negative-3",
    "kind": "negative",
    "fixture": "negative-3.json",
    "invariant": "script exceeds duration"
  }
]


{
  "scenes": []
}


{
  "scenes": [
    {
      "beat": "hook",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "hook",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "stakes",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "mechanism",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "proof",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "offer",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "cta",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    }
  ]
}


{
  "scenes": [
    {
      "beat": "hook",
      "narration": "palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra palavra ",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "problem",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "stakes",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "mechanism",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "proof",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "offer",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "cta",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    }
  ]
}


{
  "scenes": [
    {
      "beat": "hook",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "problem",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "stakes",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "mechanism",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "proof",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "offer",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "cta",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    }
  ]
}


{
  "scenes": [
    {
      "beat": "hook",
      "narration": "Gancho curto e específico",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "problem",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "stakes",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "mechanism",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "proof",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "offer",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "cta",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    }
  ]
}


{
  "scenes": [
    {
      "beat": "hook",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "problem",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "stakes",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "mechanism",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Demonstração em tela"
    },
    {
      "beat": "proof",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "offer",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    },
    {
      "beat": "cta",
      "narration": "Mensagem objetiva baseada em evidência",
      "visual": "Cena demonstrativa"
    }
  ]
}


## 37. vsl-video-script — Claim-Beat-Retention Script

- **Decisão:** what sequence earns attention, builds belief and converts within duration/platform constraints?
- **Fluxo:** audience/awareness/offer → core promise → claim-proof inventory → hook variants → problem stakes → mechanism → proof/demo → objections → offer/CTA → beat/timecode → visual/audio directions → read-time/claim QA.
- **Técnicas:** open loop; concrete demonstration; pattern interrupt; proof pacing; objection stack; CTA singularity.
- **Exceções:** no fake scarcity; testimonial claims verified; short form compresses beats, not logic; spoken cadence tested aloud.
- **Rubrica:** hook 20, belief progression 20, proof 20, retention pacing 15, offer/CTA 15, compliance 10.
- **Recursos:** `vsl-beat-sheet.csv`, `claim-proof-ledger.csv`, `broll-map.md`, timecoded script and variants.


[
  {
    "type": "book",
    "title": "Save the Cat!",
    "author": "Blake Snyder",
    "reference": "Michael Wiese Productions, 2005, ISBN 9781932907001",
    "strength": "canonical",
    "use": "Beat architecture and pacing, adapted clean-room"
  },
  {
    "type": "official",
    "title": "YouTube Creator Academy",
    "author": "YouTube",
    "url": "https://creatoracademy.youtube.com/",
    "strength": "primary",
    "use": "Audience retention, packaging and platform constraints"
  },
  {
    "type": "book",
    "title": "Made to Stick",
    "author": "Chip Heath and Dan Heath",
    "reference": "Random House, 2007, ISBN 9781400064281",
    "strength": "canonical",
    "use": "Concrete, credible and emotionally memorable messages"
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
    scenes=data.get('scenes');
    if not isinstance(scenes,list) or len(scenes)<7: fail('seven-beat VSL required')
    beats=assets['beats']['beats']; by={}
    for s in scenes:
        beat=req(s,'beat'); narration=req(s,'narration'); visual=req(s,'visual')
        if beat not in beats or beat in by: fail('invalid or duplicate beat')
        by[beat]={'narration':narration,'visual':visual,'words':len(narration.split())}
    if set(beats)-set(by): fail('missing VSL beat')
    seconds=round(sum(x['words'] for x in by.values())/assets['timing']['wpm']*60,1)
    if seconds>assets['timing']['max_seconds']: fail('script exceeds duration')
    return {'sequence':[{'beat':b,**by[b]} for b in beats],'estimated_seconds':seconds}
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
