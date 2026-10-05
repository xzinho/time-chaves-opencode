# Time Chaves — OpenCode

Time de agentes adaptado do pacote **time-chaves-v3.2.0-openclaw** para **OpenCode V2**.
Você aciona o **Chaves** (orquestrador) e ele direciona as tarefas aos especialistas, confere as evidências e entrega o consolidado.

## Estrutura
```
.
├── opencode.jsonc          # default_agent: chaves
├── AGENTS.md               # contexto do time
├── sync.ps1                # sincroniza repo -> global + Drive + git push
└── .opencode
    ├── agents/             # 9 agentes
    ├── skills/             # 41 skills
    ├── commands/           # /chaves e /time
    └── context/            # personalização + templates de empresa
```

## Uso
Com o time instalado **globalmente** (`~/.config/opencode`), em **qualquer projeto**:

- `/chaves <seu pedido>` — Chaves enquadra, delega aos especialistas, confere e entrega.
- `/time <agente> <pedido>` — chama um especialista direto (ex.: `/time kiko plano de canais`).

## Sincronização (fonte da verdade)
O **repositório** é a fonte da verdade. Depois de editar agentes/skills/commands, rode:

```powershell
powershell -ExecutionPolicy Bypass -File .\sync.ps1
```

O `sync.ps1` faz, em ordem:
1. Copia `.opencode/{agents,skills,commands}` para `~/.config/opencode` (o que roda em qualquer projeto).
2. Espelha o repositório na cópia do Google Drive.
3. `git add/commit/push` no GitHub.

Opções: `-SkipGlobal`, `-SkipDrive`, `-NoGit`, `-Message "texto"`.

## Locais
| Local | Papel |
|---|---|
| `C:\Users\mgara\repos\time-chaves-opencode` | Repo oficial (fonte da verdade) |
| `~/.config/opencode` | Instalação global (o que executa) |
| `G:\Meu Drive\Time do Chaves\Time do Chaves Open code` | Cópia/espelho no Drive |
| `github.com/xzinho/time-chaves-opencode` | Remoto |

> [!NOTE]
> A cópia no Google Drive pode receber `desktop.ini` automaticamente; eles são ignorados pelo Git e pelo sync.

## Personalização
Edite `.opencode/context/` com os dados da empresa. Enquanto `personalization_pending` for `true`, os agentes operam com contexto neutro e não inventam fatos.

## Origem
Pacote original: `C:\Users\mgara\OneDrive\Desktop\time-chaves-v3.2.0-openclaw-2026.9` (mantido intacto).
