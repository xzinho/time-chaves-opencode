# Template — Accrual-to-Cash Bridge

## Controle

| Campo | Valor obrigatório |
|---|---|
| Pergunta de decisão | resultado, liquidez e capital de giro contam a mesma história? |
| Escopo, unidade e período | |
| Owner / prazo / versão | |
| Condição de parada | |

## Ledger de evidência

| ID | Fato, inferência ou hipótese | Fonte/data/recorte | Confiança | Consequência |
|---|---|---|---:|---|

## Pipeline preenchível

### 1. Importar plano/razão/extratos

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 2. Mapear contas

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 3. Montar dre

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 4. Classificar caixa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 5. Bridge lucro

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 6. Caixa

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 7. Aging/working capital

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

### 8. Cenários e reconciliações.

- Entrada:
- Técnica aplicada:
- Evidência IDs:
- Saída verificável:
- Exceção/limite:

## Instrumentos de Accrual-to-Cash Bridge

### `chart-of-accounts-map.csv`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `cashflow.xlsx`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### `reconciliation-checks.yaml`

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

### comentário de variações

- Arquivo/aba:
- Campos ou cálculo próprios:
- Versão e link reverso:
- Como foi usado na decisão:

## Matriz de decisão

| Alternativa | Evidência a favor | Evidência contrária | Trade-off | Condição de reversão |
|---|---|---|---|---|

## Rubrica

reconciliação 30, classificação 20, rastreabilidade 20, insight 15, controles 15.

## QA e handoff

- [ ] Toda afirmação aponta para um evidence ID.
- [ ] As exceções `transferências internas eliminadas; impostos/juros classificados por política; dado incompleto conserva `unknown`, nunca zero silencioso.` foram avaliadas.
- [ ] Recursos anexos aparecem no corpo e têm versão.
- [ ] Decisão, owner, prazo, risco residual e próximo teste estão explícitos.
