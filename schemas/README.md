# Schemas

Esta pasta conterá schemas estruturais compartilhados para dados narrativos, por exemplo:

- personagem;
- fato canônico;
- evento de timeline;
- aquisição de conhecimento;
- revelação;
- cena;
- mudança de estado.

Os schemas devem permanecer neutros em relação a fornecedor de IA e, quando possível, compatíveis com validação local e CI.

Não adicione campos específicos de um único livro ao schema global sem verificar se eles representam um conceito reutilizável. Extensões específicas podem viver dentro do próprio projeto.