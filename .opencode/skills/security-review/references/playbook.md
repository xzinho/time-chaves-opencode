# Playbook operacional — Asset-Threat-Control-Evidence

## Pergunta de controle

what must block release, what can be remediated, and what residual risk is accepted by whom?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **scope/data/classification** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **STRIDE-like prompts** responde à pergunta sem extrapolar o dado? Se não, selecione **severity matrix.** e declare a troca.
3. Há uma destas exceções: scanner finding not confirmed is tentative; production test needs authorization; risk acceptance requires named authority/date.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **what must block release, what can be remediated, and what residual risk is accepted by whom?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Scope/data/classification**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Architecture/trust boundaries**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Threat model**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Asvs/ssdf control mapping**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Code/config/runtime evidence**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Exploitability/impact**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Findings**. Registre entrada, transformação, evidência e saída antes de avançar.
8. **Remediation/retest**. Registre entrada, transformação, evidência e saída antes de avançar.
9. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Stride-like prompts**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Attack path**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Misuse case**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Secret/dependency/auth/session review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Evidence tiers**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Severity matrix.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Scanner finding not confirmed is tentative. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Production test needs authorization. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Risk acceptance requires named authority/date.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “architecture/trust boundaries” cita evidência identificada, aplica “STRIDE-like prompts”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Asset-Threat-Control-Evidence foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `threat_model_md.md` ou formato nativo equivalente: materializa **`threat-model.md`** e deve ser citado pelo artefato principal.
- `control_evidence_csv.md` ou formato nativo equivalente: materializa **`control-evidence.csv`** e deve ser citado pelo artefato principal.
- `finding_schema_json.md` ou formato nativo equivalente: materializa **`finding-schema.json`** e deve ser citado pelo artefato principal.
- `release_gate_with_owner_due_date.md` ou formato nativo equivalente: materializa **release gate with owner/due date** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: scope 15, threat coverage 25, evidence 25, severity 15, remediation/retest 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **OWASP Application Security Verification Standard 4.0.3**, OWASP (official, força: primary). Aplicação: Testable application-security control baseline. Localizador: https://owasp.org/www-project-application-security-verification-standard/. Consulta: 2026-08-24.
2. **NIST Secure Software Development Framework 1.1**, NIST (official, força: primary). Aplicação: Secure-development practices and evidence. Localizador: https://csrc.nist.gov/pubs/sp/800/218/final. Consulta: 2026-08-24.
3. **Threat Modeling Playbook**, OWASP (github, força: mature). Aplicação: Practical threat-model facilitation. Localizador: https://github.com/OWASP/threat-modeling-playbook. Consulta: 2026-08-24.
