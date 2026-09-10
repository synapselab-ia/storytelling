# START HERE

Este arquivo é o ponto de entrada obrigatório para qualquer agente ou pessoa que trabalhe neste repositório.

## 1. Leia as regras globais

Antes de editar qualquer projeto, leia:

1. `.ai/CONSTITUTION.md`
2. `.ai/PRECEDENCE.md`
3. `.ai/WORKFLOW.md`

Se estiver usando um cliente que reconheça arquivos próprios de instrução, leia também o adaptador correspondente (`AGENTS.md` ou `GEMINI.md`). Esses adaptadores não substituem as regras centrais.

## 2. Identifique o projeto

Livros ficam em `projects/<slug>/`.

Nunca misture canon, personagens, timeline ou regras específicas entre projetos.

Ao trabalhar em um livro, leia primeiro:

1. `projects/<slug>/PROJECT.md`
2. `projects/<slug>/STATUS.md`
3. somente os arquivos de canon, story e editorial necessários à tarefa atual.

## 3. Regra de continuidade entre chats

Não dependa de memória de conversas anteriores. O repositório é a fonte de verdade.

Se uma informação mencionada pelo usuário não estiver registrada no repositório, trate-a como uma proposta nova até que seja formalmente incorporada.

## 4. Antes de escrever prosa

Confirme que existem, no mínimo:

- premissa e direção estrutural suficientes;
- POV definido;
- estado atual dos personagens relevantes;
- conhecimento permitido de cada personagem;
- revelações permitidas e proibidas;
- timeline suficiente para a cena ou capítulo;
- regras editoriais aplicáveis.

Se isso não existir, desenvolva primeiro a camada de planejamento/canon em vez de improvisar silenciosamente.

## 5. Depois de uma alteração relevante

Atualize `STATUS.md` do projeto quando a alteração mudar o estado do trabalho, decisões em aberto ou próximo passo.

Mudanças de canon devem ser explícitas. Não reinterprete silenciosamente fatos anteriores para acomodar prosa nova.

## 6. Conteúdo gerado

Arquivos derivados, índices, relatórios e context packs devem ficar em `generated/` dentro do projeto quando essa camada existir. Eles podem ser reconstruídos e não são fonte de verdade.

## 7. Em caso de conflito

Siga `.ai/PRECEDENCE.md`. Se o conflito não puder ser resolvido deterministicamente, pare a alteração conflitante e registre o problema em vez de inventar uma solução.