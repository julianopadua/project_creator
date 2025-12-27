# scripts/generate_tree.py
import os
from pathlib import Path
from fnmatch import fnmatch


DEFAULT_IGNORE_NAMES = {
    # VCS/IDE/OS
    ".git", ".vscode", ".idea", ".DS_Store",

    # Python
    "__pycache__", ".pytest_cache", ".mypy_cache",
    ".venv", "venv",

    # Node / Next / build artifacts
    "node_modules", ".next", ".turbo",
    "dist", "build", "out",
    ".cache", ".vercel",
    ".npm", ".yarn",
    "coverage",
}

DEFAULT_IGNORE_GLOBS = {
    # env/secrets
    ".env*",  # pega .env, .env.local, .env.production etc.

    # logs
    "*.log", "npm-debug.log*", "yarn-debug.log*", "yarn-error.log*", "pnpm-debug.log*",

    # TS/JS caches
    "*.tsbuildinfo",
}


def _should_ignore(path: Path, ignore_names: set[str], ignore_globs: set[str]) -> bool:
    name = path.name
    if name in ignore_names:
        return True
    for pat in ignore_globs:
        if fnmatch(name, pat):
            return True
    return False


def generate_project_tree(
    root_dir: Path,
    indent: str = "",
    ignore_names: set[str] | None = None,
    ignore_globs: set[str] | None = None,
    prune_dirnames: set[str] | None = None,
    prune_relpaths: set[str] | None = None,
    _project_root: Path | None = None,
) -> str:
    """
    Gera uma string representando a árvore de arquivos de forma recursiva,
    ignorando artefatos locais/gerados e colapsando diretórios irrelevantes.
    """
    root_dir = Path(root_dir)

    if _project_root is None:
        _project_root = root_dir

    if ignore_names is None:
        ignore_names = set(DEFAULT_IGNORE_NAMES)
    if ignore_globs is None:
        ignore_globs = set(DEFAULT_IGNORE_GLOBS)

    # Diretórios que aparecem na árvore, mas NÃO têm conteúdo expandido
    if prune_dirnames is None:
        prune_dirnames = {"public"}  # bom default p/ Next.js
    if prune_relpaths is None:
        prune_relpaths = {"doc/supabase"}  # opcional (ajuste se quiser expandir docs)

    try:
        items = sorted(list(root_dir.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        return ""

    # Filtra primeiro, para o "is_last" ficar correto
    filtered: list[Path] = []
    for item in items:
        if _should_ignore(item, ignore_names, ignore_globs):
            continue
        filtered.append(item)

    tree_str = ""

    for idx, item in enumerate(filtered):
        is_last = idx == (len(filtered) - 1)
        connector = "└── " if is_last else "├── "

        rel_posix = item.relative_to(_project_root).as_posix()

        if item.is_dir():
            # Decide se colapsa
            should_prune = (item.name in prune_dirnames) or (rel_posix in prune_relpaths)

            if should_prune:
                tree_str += f"{indent}{connector}{item.name}/ [conteúdo omitido]\n"
                continue

            tree_str += f"{indent}{connector}{item.name}/\n"
            extension = "    " if is_last else "│   "
            tree_str += generate_project_tree(
                item,
                indent=indent + extension,
                ignore_names=ignore_names,
                ignore_globs=ignore_globs,
                prune_dirnames=prune_dirnames,
                prune_relpaths=prune_relpaths,
                _project_root=_project_root,
            )
        else:
            tree_str += f"{indent}{connector}{item.name}\n"

    return tree_str


def save_structure_to_markdown(project_path: str, output_file: str = "projeto_estrutura.md") -> None:
    abs_path = Path(project_path).resolve()
    project_name = abs_path.name

    header = f"# Estrutura do Projeto: {project_name}\n\n"
    header += "Este documento descreve a hierarquia de pastas e arquivos para análise de contexto.\n\n"
    header += "```text\n"
    header += f"{project_name}/\n"

    tree_content = generate_project_tree(abs_path)

    footer = "```\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header + tree_content + footer)

    print(f"✅ Estrutura salva com sucesso em: {output_file}")


if __name__ == "__main__":
    caminho_do_projeto = input("Digite o caminho do projeto: ").strip()
    if os.path.exists(caminho_do_projeto):
        save_structure_to_markdown(caminho_do_projeto)
    else:
        print("❌ Caminho não encontrado.")
