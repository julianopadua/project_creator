import os
from pathlib import Path
from datetime import datetime

def generate_project_tree(root_dir, indent="", ignore_list=None):
    """
    Gera uma string representando a árvore de arquivos de forma recursiva.
    """
    if ignore_list is None:
        ignore_list = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', '.env', '.DS_Store', '.vscode', '.next', 'dist', 'build', 'out', 'coverage'}

    tree_str = ""
    root_path = Path(root_dir)
    
    # Lista e ordena itens (pastas primeiro, depois arquivos)
    try:
        items = sorted(list(root_path.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        return ""

    for i, item in enumerate(items):
        if item.name in ignore_list:
            continue

        # Define se é o último item do nível para usar o caractere correto
        is_last = i == (len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        tree_str += f"{indent}{connector}{item.name}\n"

        if item.is_dir():
            # Aumenta o recuo para a próxima recursão
            extension = "    " if is_last else "│   "
            tree_str += generate_project_tree(item, indent + extension, ignore_list)
            
    return tree_str

def save_structure_to_markdown(project_path):
    # 1. Preparar caminhos e nomes
    abs_path = Path(project_path).resolve()
    project_name = abs_path.name  # Pega o nome da última pasta (ex: forest-portal)
    
    # 2. Criar a pasta 'estruturas' se não existir
    output_folder = Path("estruturas")
    output_folder.mkdir(exist_ok=True)
    
    # 3. Gerar o nome do arquivo: YYYY-MM-DD_Nome-do-Projeto.md
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}_{project_name}.md"
    output_file = output_folder / filename
    
    # 4. Montar o conteúdo
    header = f"# Estrutura do Projeto: {project_name}\n\n"
    header += f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
    header += "Este documento descreve a hierarquia de pastas e arquivos.\n\n"
    header += "```text\n"
    header += f"{project_name}/\n"
    
    tree_content = generate_project_tree(abs_path)
    
    footer = "```\n"
    
    # 5. Salvar o arquivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header + tree_content + footer)
    
    print(f"✅ Estrutura salva com sucesso em: {output_file}")

# --- Execução ---
if __name__ == "__main__":
    caminho_do_projeto = input("Digite o caminho do projeto: ").strip()
    
    # Remove aspas caso o usuário tenha colado o caminho com elas
    caminho_do_projeto = caminho_do_projeto.replace('"', '').replace("'", "")
    
    if os.path.exists(caminho_do_projeto):
        save_structure_to_markdown(caminho_do_projeto)
    else:
        print(f"❌ Caminho não encontrado: {caminho_do_projeto}")