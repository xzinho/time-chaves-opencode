# Time Chaves — OpenCode

Adaptação do pacote **time-chaves-v3.2.0-openclaw** para o **OpenCode V2**.
Aqui você aciona o **Chaves** (orquestrador) e ele direciona as tarefas para os especialistas, confere as evidências e entrega o consolidado.

## Como usar
1. Abra o OpenCode **nesta pasta** como working directory.
2. O agente padrão já é o **Chaves** (definido em `opencode.jsonc`).
3. Faça seu pedido normalmente, por exemplo:
   > Quero lançar um novo produto. Faça um plano completo.
4. O Chaves enquadra a demanda, escolhe um owner por tarefa, dispara os especialistas (Florinda, Kiko, Barriga, Madruga…) em paralelo quando possível, cobra evidência, arbitra e entrega.

Para falar direto com um especialista, peça explicitamente:
> Use o subagente chiquinha para revisar este código.

## Estrutura
```
.
├── opencode.jsonc                 # default_agent: chaves
├── AGENTS.md                      # contexto do time (lido por todos)
└── .opencode
    ├── agents/                    # 9 agentes
    │   ├── chaves.md              # primary (orquestrador)
    │   ├── chiquinha.md           # subagent
    │   ├── dona-florinda.md
    │   ├── kiko.md
    │   ├── senhor-barriga.md
    │   ├── professor-girafales.md
    │   ├── seu-madruga.md
    │   ├── bruxa-do-71.md
    │   └── chapolin.md
    ├── skills/                    # 41 skills (copy das originais)
    └── context/                   # personalização + templates de empresa
```

## Como o roteamento funciona
O OpenCode é hub-and-spoke: o Chaves é o hub. Ele chama os especialistas com a ferramenta `subagent` passando um contrato de tarefa. Os especialistas devolvem resultado + evidência; não conversam entre si e não lançam outros subagentes.

## Personalização
Edite `.opencode/context/` com os dados da empresa (nome, oferta, mercado, cliente, metas). Enquanto `personalization_pending` for `true`, os agentes operam com contexto neutro e não inventam fatos.

## Origem
Pacote original: `C:\Users\mgara\OneDrive\Desktop\time-chaves-v3.2.0-openclaw-2026.9` (mantido intacto).
