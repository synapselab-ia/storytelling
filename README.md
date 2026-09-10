# Storytelling

Repositório monorepo para planejamento, escrita, revisão e validação de romances assistidos por IA.

O objetivo é manter o **Git como fonte de verdade** e permitir que diferentes agentes (GPT, Gemini ou outros) trabalhem nos mesmos projetos sem depender da memória de um chat específico.

## Princípios

- Cada livro vive isolado em `projects/<slug>/`.
- Regras compartilhadas vivem na raiz e não devem ser duplicadas dentro dos projetos.
- Canon, planejamento e manuscrito são camadas diferentes.
- A IA nunca deve inventar canon para preencher lacunas.
- Mudanças relevantes de canon devem ser explícitas e versionadas.
- Conteúdo em `generated/` é derivado e nunca tem autoridade sobre a fonte de verdade.

## Entrada para agentes

Antes de trabalhar neste repositório, leia `START_HERE.md`.

Adaptadores específicos:

- GPT / Codex: `AGENTS.md`
- Gemini: `GEMINI.md`

As regras canônicas dos agentes ficam em `.ai/`, para evitar duplicação entre fornecedores.

## Estrutura prevista

```text
storytelling/
├── START_HERE.md
├── AGENTS.md
├── GEMINI.md
├── .ai/
├── editorial/
├── schemas/
├── tools/
└── projects/
    ├── _template/
    ├── livro-a/
    └── livro-b/
```

## Continuar em outro chat

Exemplo de instrução:

> Acesse meu repositório `storytelling`, leia `START_HERE.md` e continue o projeto indicado seguindo a fonte de verdade do repositório.

Nunca presuma contexto ausente de conversas anteriores: recupere-o do repositório.