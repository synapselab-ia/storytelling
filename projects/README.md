# Projects

Cada subdiretório representa um livro independente.

## Regras

- Use um slug estável e curto para cada projeto.
- Nunca reutilize IDs, canon ou timeline entre livros sem uma decisão explícita de universo compartilhado.
- Cada projeto deve conter pelo menos `PROJECT.md` e `STATUS.md`.
- Use `projects/_template/` como referência ao iniciar um novo livro.

## Estrutura recomendada

```text
projects/<slug>/
├── PROJECT.md
├── STATUS.md
├── canon/
├── story/
├── editorial/
├── manuscript/
├── generated/
└── tests/
```

`canon/`, `story/` e `manuscript/` são conceitualmente diferentes. Não use manuscrito como banco de canon.