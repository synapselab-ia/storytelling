# AI Constitution

Estas regras valem para todos os projetos deste repositório.

## Fonte de verdade

1. O repositório é a fonte de verdade persistente.
2. Conversas anteriores, memória do modelo e inferências não substituem arquivos versionados.
3. Manuscrito não altera canon implicitamente.
4. Conteúdo em `generated/` é derivado e nunca prevalece sobre canon ou planejamento versionado.

## Canon e consistência

5. Nunca invente fatos para preencher lacunas sem marcá-los como proposta.
6. Nunca corrija uma contradição silenciosamente.
7. Se houver conflito, identifique os arquivos envolvidos e aplique `.ai/PRECEDENCE.md`.
8. Mudanças de canon devem ser explícitas, rastreáveis e acompanhadas de análise de impacto quando afetarem material existente.
9. Não permita que um personagem use conhecimento que ainda não adquiriu.
10. Não revele ao leitor informação marcada como restrita antes do ponto autorizado.
11. Respeite timeline, estado físico, localização, inventário, relações e demais estados persistentes.

## Projetos

12. Cada livro é isolado em `projects/<slug>/`.
13. Nunca importe canon de um livro para outro por similaridade, memória ou conveniência.
14. Regras globais devem permanecer genéricas; regras específicas de um livro pertencem ao próprio projeto.

## Escrita

15. Não comece prosa definitiva quando faltarem informações estruturais indispensáveis à cena.
16. O outline orienta a função narrativa; o manuscrito executa essa função, mas não ganha autoridade sobre canon por existir.
17. Preserve POV, voz, conhecimento, continuidade emocional e restrições de revelação aplicáveis.
18. Não force personagens a agir fora de caráter apenas para cumprir um beat; sinalize o conflito entre character logic e plot logic.
19. Evite exposição usada apenas para informar o leitor quando os personagens já conhecem a informação.

## Alterações

20. Antes de mudar fatos centrais, avalie impacto em timeline, personagens, revelações, capítulos e relações.
21. Ao concluir uma etapa relevante, atualize `STATUS.md` do projeto.
22. Se uma decisão ainda estiver aberta, registre-a como aberta; não a trate como decidida.

## Validação

23. Validadores determinísticos têm prioridade sobre julgamentos estilísticos de LLM.
24. Alertas semânticos devem ser tratados como hipóteses a revisar, não como fatos automáticos.
25. Um agente não deve declarar que o projeto está consistente sem verificar os arquivos relevantes à afirmação.