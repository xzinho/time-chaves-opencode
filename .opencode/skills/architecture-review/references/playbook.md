# Playbook operacional — Scenario-Tradeoff Review

## Pergunta de controle

a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?

## Preparação e contrato de evidência

Abra um ledger com `id`, afirmação, tipo (`fato|inferência|hipótese`), fonte, data, recorte, confiança e consequência. Defina a unidade de análise adequada a este domínio e a condição de parada. Nenhuma conclusão pode apontar para uma fonte que não esteja no ledger.

## Árvore de decisão específica

1. A evidência necessária para **stakeholders/concerns** existe e é vigente? Se não, suspenda a conclusão e registre coleta mínima.
2. A técnica **utility tree** responde à pergunta sem extrapolar o dado? Se não, selecione **failure-mode walkthrough.** e declare a troca.
3. Há uma destas exceções: brownfield começa por runtime evidence; diagrama desatualizado não é fonte; ausência de SLO bloqueia afirmações de desempenho.? Se sim, segmente o caso, aplique o gate e não agregue o resultado.
4. O output permite decidir **a arquitetura satisfaz atributos prioritários sob cenários concretos e riscos aceitáveis?**? Se não, volte à primeira etapa sem evidência suficiente.

## Execução passo a passo

1. **Stakeholders/concerns**. Registre entrada, transformação, evidência e saída antes de avançar.
2. **Context/container/data/deployment views**. Registre entrada, transformação, evidência e saída antes de avançar.
3. **Quality-attribute scenarios**. Registre entrada, transformação, evidência e saída antes de avançar.
4. **Decision log**. Registre entrada, transformação, evidência e saída antes de avançar.
5. **Tradeoff/risk probes**. Registre entrada, transformação, evidência e saída antes de avançar.
6. **Fitness functions**. Registre entrada, transformação, evidência e saída antes de avançar.
7. **Gate.**. Registre entrada, transformação, evidência e saída antes de avançar.

Em cada transição, anexe um `evidence_id`; registre o que foi descartado e por quê. Alternativas precisam ter condição de reversão. Recomendações devem apontar para uma observação ou hipótese testável.

## Caixa de ferramentas

- **Utility tree**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Atam-lite**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Adr review**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Dependency/critical-path map**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.
- **Failure-mode walkthrough.**: aplique somente quando responder à decisão central; documente escolha, limite e sinal de invalidação.

## Casos de borda

- Brownfield começa por runtime evidence. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Diagrama desatualizado não é fonte. Marque a condição no artefato e acione o gate indicado antes do handoff.
- Ausência de slo bloqueia afirmações de desempenho.. Marque a condição no artefato e acione o gate indicado antes do handoff.

Se dados conflitarem, não faça média cega: preserve as versões, compare autoridade/recência/aderência e escreva a divergência. Se o dado estiver ausente, use `NÃO COMPROVADO`, nunca zero silencioso. Se o risco puder causar dano irreversível, pare antes de qualquer ação externa.

## Exemplo e anti-exemplo

**Exemplo aceito:** a etapa “context/container/data/deployment views” cita evidência identificada, aplica “utility tree”, explicita limite e produz uma decisão condicionada com owner e data.

**Anti-exemplo:** “seguir melhores práticas” sem dizer qual problema foi observado, qual regra de Scenario-Tradeoff Review foi aplicada, que evidência sustenta a mudança e como medir o efeito.

## Recursos reutilizáveis obrigatórios

- `stakeholder_concern_matrix_md.md` ou formato nativo equivalente: materializa **`stakeholder-concern-matrix.md`** e deve ser citado pelo artefato principal.
- `quality_scenarios_yaml.md` ou formato nativo equivalente: materializa **`quality-scenarios.yaml`** e deve ser citado pelo artefato principal.
- `adr_index_csv.md` ou formato nativo equivalente: materializa **`adr-index.csv`** e deve ser citado pelo artefato principal.
- `fitness_functions_yaml.md` ou formato nativo equivalente: materializa **`fitness-functions.yaml`** e deve ser citado pelo artefato principal.

Cada recurso recebe versão, autor, data e link reverso no artefato. Recursos sem uso comprovado contam como ausentes.

## QA, pontuação e handoff

Pontue: rastreabilidade 20, qualidade dos cenários 20, evidência 20, tradeoffs 20, operabilidade/reversibilidade 20.. Para cada eixo, use 0 ausente, 1 parcial, 2 comprovado. Reprove eixo crítico em zero, fonte irrecuperável, placeholder, contradição não tratada ou ausência de decisão. O handoff inclui pergunta, método, ledger, recursos, achados, incertezas, decisão, owner, prazo e condição de reabertura.

## Fontes aplicadas

1. **ISO/IEC/IEEE 42010 Architecture Description**, ISO/IEC/IEEE (standard, força: primary). Aplicação: Stakeholders, concerns, viewpoints and decisions. Localizador: https://www.iso.org/standard/74393.html. Consulta: 2026-08-24.
2. **AWS Well-Architected Framework**, AWS (official, força: primary). Aplicação: Risk review across operational pillars. Localizador: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html. Consulta: 2026-08-24.
3. **Software Architecture in Practice, 4th ed.**, Bass, Clements, Kazman (book, força: canonical). Aplicação: Quality-attribute scenarios and tradeoff analysis. Localizador: Addison-Wesley, 2021, ISBN 9780136886099. Consulta: 2026-08-24.
