---
name: "team-bundle-installer"
description: "Instala e reconfigura pacotes Time Chaves com preflight, onboarding opcional, smoke e rollback."
---

# Instalador Time Chaves

Use quando o humano enviar um arquivo `.openclaw-team` e pedir instalação.

1. Um pedido mínimo como “Instale este time de agentes de IA” é suficiente. Confirme chat privado, leia `README-ALUNO.md` e execute o preflight no OPENCLAW_HOME real. Não peça chave, fingerprint, SHA-256 nem texto longo.
2. A primeira pergunta ao aluno deve ser: “Você quer personalizar o Chaves com os dados da sua empresa agora ou prefere fazer isso depois?”.
3. Se escolher **agora**, faça no máximo duas mensagens de perguntas, aceitando texto ou áudio. Colete nome/papel, empresa/oferta/mercado, cliente/problema, resultados de 90 dias e objetivo de 12 meses; mostre o resumo e aguarde confirmação explícita.
4. Se escolher **depois**, explique que o time será instalado completo com contexto neutro e que nenhum dado empresarial será inventado. Mostre esse resumo e aguarde confirmação explícita.
5. Execute `install --personalization now|later --confirmed` somente após a confirmação. Preserve integralmente Telegram, modelos, bindings, segredos e conteúdo local.
6. No caminho adiado, confirme `personalization_pending=true`, não bloqueie tarefas e ofereça a configuração apenas em conversa relevante ou em uma lembrança periódica controlada.
7. Quando o humano disser “personalizar/reconfigurar o Time Chaves”, use `reconfigure --personalization now`: colete dados, mostre resumo, confirme e atualize o contexto dos nove agentes idempotentemente.
8. Valide integridade automática, backup, configuração, memória, skills, restart e smokes; preserve `tools.profile: full`, `tools.sessions.visibility: all`, A2A e `sessions_send` todos-com-todos.
9. Nunca exponha segredo, stack trace ou configuração no Telegram. Mensagens devem ser positivas e verdadeiras. Só use “100%” quando o receipt tiver gate APROVADO.
