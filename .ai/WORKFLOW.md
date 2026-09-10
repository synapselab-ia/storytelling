# Global Workflow

Este é o ciclo padrão para qualquer tarefa narrativa no repositório.

## 1. Selecionar projeto

Leia `START_HERE.md`, identifique `projects/<slug>/` e carregue `PROJECT.md` + `STATUS.md`.

## 2. Classificar a tarefa

Determine se a solicitação é principalmente:

- exploração de ideia;
- decisão de canon;
- planejamento estrutural;
- outline de capítulo/cena;
- escrita de prosa;
- revisão;
- auditoria;
- alteração de canon;
- manutenção técnica.

Não trate brainstorming como canon aprovado sem registro explícito.

## 3. Construir contexto mínimo suficiente

Carregue apenas o necessário para a tarefa, priorizando:

- regras editoriais aplicáveis;
- personagens presentes;
- conhecimento atual;
- timeline relevante;
- estado atual de entidades;
- revelações permitidas/proibidas;
- cenas anteriores necessárias para continuidade.

Contexto obrigatório deve ser determinístico. Busca semântica pode complementar, nunca substituir fatos críticos.

## 4. Executar

Ao escrever ou revisar, preserve as restrições carregadas. Quando uma exigência do usuário conflitar com canon existente, aponte o impacto antes de consolidar a alteração.

## 5. Validar

Quando existirem validadores para a tarefa, execute-os. Diferencie:

- ERROR: inconsistência objetiva ou regra bloqueante;
- WARNING: suspeita semântica/editorial que requer julgamento;
- INFO: observação não bloqueante.

## 6. Consolidar

Após mudança aprovada:

- atualize os arquivos-fonte adequados;
- atualize `STATUS.md` se houver mudança de estágio, decisão ou próximo passo;
- não use `generated/` para registrar decisões permanentes.

## 7. Continuidade entre chats

Ao encerrar uma etapa importante, o repositório deve conter informação suficiente para que outro agente retome o trabalho sem acesso ao chat anterior.