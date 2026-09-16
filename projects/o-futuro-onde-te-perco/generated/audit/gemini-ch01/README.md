# Pacote de auditoria Gemini Pro

Este diretório contém o material de apoio para auditar o Capítulo 1 de `O Futuro Onde Te Perco` fora do workflow automático.

## Uso recomendado

1. Baixe o Word do Capítulo 1 enviado no chat para leitura e comentários humanos.
2. Para o Gemini Pro, anexe `PROMPT_AUDITORIA_GEMINI.txt` e `CONTEXTO_AUDITORIA.md`.
3. Anexe também o manuscrito atual do Capítulo 1. A fonte versionada está em `../../../manuscript/ch-001.md`.
4. Cole o conteúdo de `PROMPT_AUDITORIA_GEMINI.txt` como instrução principal.
5. Peça ao Gemini para classificar achados em `ERROR`, `WARNING` e `INFO` e declarar `NO BLOCKING ERRORS` quando não houver inconsistência objetiva.

## Fontes canônicas de referência

A auditoria deve respeitar a hierarquia formal do repositório. O arquivo `PRECEDENCIA_E_CONFLITOS.md` reproduz essa ordem para uso externo.

O contexto consolidado não substitui as fontes canônicas. Ele existe para facilitar upload e leitura por outro modelo.

## Estado do capítulo

O Capítulo 1 está em revisão no PR #22 e ainda não foi mergeado como prosa aprovada.
