import os
from pathlib import Path

from google import genai
from google.genai import errors

PROJECT_ROOT = Path("projects/o-futuro-onde-te-perco")

GLOBAL_CONTEXT = [
    Path("START_HERE.md"),
    Path(".ai/CONSTITUTION.md"),
    Path(".ai/PRECEDENCE.md"),
    Path(".ai/WORKFLOW.md"),
    Path("editorial/GLOBAL_WRITING_RULES.md"),
]

PROJECT_CONTEXT = [
    PROJECT_ROOT / "PROJECT.md",
    PROJECT_ROOT / "STATUS.md",
]

DEFAULT_AUDIT_MODELS = ("gemini-3.7-flash", "gemini-3.6-flash")


def existing_markdown_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(path for path in directory.glob("*.md") if path.is_file())


def read_context(paths: list[Path]) -> str:
    sections: list[str] = []
    missing: list[str] = []

    for path in paths:
        if not path.exists():
            missing.append(str(path))
            continue
        sections.append(f"\n\n===== {path} =====\n{path.read_text(encoding='utf-8')}")

    if missing:
        print("WARNING: arquivos de contexto ausentes:")
        for path in missing:
            print(f"- {path}")

    return "".join(sections)


def build_context() -> str:
    paths = list(GLOBAL_CONTEXT)
    paths.extend(PROJECT_CONTEXT)
    paths.extend(existing_markdown_files(PROJECT_ROOT / "canon"))
    paths.extend(existing_markdown_files(PROJECT_ROOT / "story"))
    paths.extend(existing_markdown_files(PROJECT_ROOT / "editorial"))
    paths.extend(existing_markdown_files(PROJECT_ROOT / "manuscript"))
    return read_context(paths)


def audit_models() -> tuple[str, ...]:
    configured = os.environ.get("GEMINI_AUDITOR_MODEL")
    if configured:
        return (configured, *DEFAULT_AUDIT_MODELS)
    return DEFAULT_AUDIT_MODELS


def generate_report(client: genai.Client, prompt: str) -> tuple[str, str]:
    last_server_error: errors.ServerError | None = None
    attempted: set[str] = set()

    for model in audit_models():
        if model in attempted:
            continue
        attempted.add(model)

        try:
            response = client.models.generate_content(model=model, contents=prompt)
            text = response.text or ""
            if not text.strip():
                raise RuntimeError(f"Modelo {model} retornou resposta vazia")
            return model, text
        except errors.ServerError as exc:
            last_server_error = exc
            print(f"WARNING: {model} indisponível no momento; tentando fallback.")

    if last_server_error is not None:
        raise last_server_error
    raise RuntimeError("Nenhum modelo de auditoria disponível")


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY não configurada")

    context = build_context()
    if not context.strip():
        raise RuntimeError("Nenhum contexto narrativo encontrado para auditoria")

    prompt = f"""Você é um auditor de continuidade de um repositório de ficção.

Analise o contexto versionado abaixo como um conjunto hierárquico de fontes de verdade.
Respeite explicitamente START_HERE.md, CONSTITUTION.md e PRECEDENCE.md.

Objetivos:
1. identificar contradições objetivas entre canon, story, STATUS e regras editoriais;
2. identificar fatos tratados como fechados em um arquivo mas ainda abertos em outro;
3. apontar violações de timeline, conhecimento, revelação, estado físico ou regras sobrenaturais;
4. distinguir decisões realmente inconsistentes de decisões simplesmente ainda abertas;
5. não inventar fatos para preencher lacunas.

Formato do relatório:
- ERROR: inconsistência objetiva e bloqueante;
- WARNING: possível problema semântico/editorial que exige julgamento;
- INFO: observação não bloqueante.

Se não houver ERROR objetivo, diga explicitamente: "NO BLOCKING ERRORS".
Não reescreva a história e não proponha canon novo como se fosse correção automática.

CONTEXTO VERSIONADO:
{context}
"""

    client = genai.Client(api_key=api_key)
    model, report = generate_report(client, prompt)

    print(f"--- RELATÓRIO DE AUDITORIA NARRATIVA ({model}) ---")
    print(report)


if __name__ == "__main__":
    main()
