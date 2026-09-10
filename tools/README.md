# Tools

Esta pasta será usada para scripts e validadores automáticos do sistema narrativo.

Direção prevista:

```text
tools/
├── bookctl.py
├── build_context.py
├── validate_all.py
└── validators/
    ├── schema.py
    ├── references.py
    ├── timeline.py
    ├── knowledge.py
    ├── revelations.py
    ├── pov.py
    └── continuity.py
```

Princípios:

- validadores determinísticos devem ser preferidos para regras objetivas;
- validações semânticas por IA devem produzir warnings quando houver incerteza;
- ferramentas não devem ser a única fonte de dados canônicos;
- qualquer índice ou banco gerado deve poder ser reconstruído a partir dos arquivos versionados.