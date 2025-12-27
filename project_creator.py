import os
import datetime
import subprocess
import sys

def sanitize_path(path):
    """Remove aspas do caminho."""
    return path.strip('\'"')

def run(cmd, cwd=None, check=True):
    """Executa um comando (lista) com subprocess.run, exibindo erros legíveis."""
    try:
        return subprocess.run(cmd, cwd=cwd, check=check)
    except FileNotFoundError:
        raise FileNotFoundError(f"Comando não encontrado: {cmd[0]}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Falha ao executar: {' '.join(cmd)} (código {e.returncode})")

def have_git():
    """Verifica se o Git está disponível."""
    try:
        subprocess.run(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def prompt_bool(msg, default=False):
    """
    Pergunta sim/não no stdin.
    default=False => resposta vazia conta como 'não'
    default=True  => resposta vazia conta como 'sim'
    """
    sufixo = "[S/n]" if default else "[s/N]"
    ans = input(f"{msg} {sufixo} ").strip().lower()
    if ans == "":
        return default
    return ans in ("s", "sim", "y", "yes")

def init_git_repo(project_path, do_initial_commit=True, remote_url=None):
    """Inicializa repositório Git, cria commit inicial/branch main e adiciona remote origin, se pedido."""
    print("Inicializando repositório Git...")
    run(["git", "init"], cwd=project_path)

    if do_initial_commit:
        # Adiciona tudo e faz commit inicial
        run(["git", "add", "."], cwd=project_path)
        run(["git", "commit", "-m", "Initial commit"], cwd=project_path)
        # Força branch principal como 'main'
        run(["git", "branch", "-M", "main"], cwd=project_path)

    if remote_url:
        print(f"Adicionando remote 'origin' -> {remote_url}")
        run(["git", "remote", "add", "origin", remote_url], cwd=project_path)

def create_project_structure(base_path, project_name, ask_git=True):
    base_path = sanitize_path(base_path)
    current_datetime = datetime.datetime.now()

    # Diretório principal do projeto
    project_path = os.path.join(base_path, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Subdiretórios
    directories = {
        'src': os.path.join(project_path, 'src'),
        'data_raw': os.path.join(project_path, 'data', 'raw'),
        'data_processed': os.path.join(project_path, 'data', 'processed'),
        'images': os.path.join(project_path, 'images'),
        'report': os.path.join(project_path, 'report'),
        'addons': os.path.join(project_path, 'addons'),
    }
    for path in directories.values():
        os.makedirs(path, exist_ok=True)

    # requirements.txt
    requirements = '''requests>=2.31.0
beautifulsoup4>=4.12.2
pyyaml>=6.0.1
tqdm>=4.66.1
pandas>=2.2.2
streamlit>=1.35.0
'''
    with open(os.path.join(project_path, 'requirements.txt'), 'w', encoding='utf-8') as file:
        file.write(requirements)

    # config.yaml (na raiz)
    config_content = '''# configuration parameters
paths:
  data_raw: ./data/raw
  data_processed: ./data/processed
  images: ./images
  report: ./report
  addons: ./addons
'''
    with open(os.path.join(project_path, 'config.yaml'), 'w', encoding='utf-8') as file:
        file.write(config_content)

    # Script principal em src
    script_content = f'''# Made by Juliano E. S. Padua
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from utils import load_config

paths, config = load_config()

# initialize paths from config
data_raw_path = paths["data_raw"]
data_processed_path = paths["data_processed"]
images_path = paths["images"]
report_path = paths["report"]
addons_path = paths["addons"]

# your code starts here
current_datetime = datetime.datetime.now()

# Project '{project_name}' initialized on {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}
'''
    script_path = os.path.join(directories['src'], f'{project_name}.py')
    with open(script_path, 'w', encoding='utf-8') as file:
        file.write(script_content)

    # utils.py em src (resolve caminhos a partir da RAIZ do projeto)
    utils_content = '''import os
import yaml

def load_config():
    """Carrega config.yaml do diretório raiz e resolve caminhos relativos."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))
    config_path = os.path.join(project_root, "config.yaml")

    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    def _p(rel):
        # remove prefixo ./ se existir e junta com a raiz do projeto
        rel = rel.lstrip("./")
        return os.path.join(project_root, rel)

    paths = {
        "project_root": project_root,
        "data_raw": _p(config["paths"]["data_raw"]),
        "data_processed": _p(config["paths"]["data_processed"]),
        "images": _p(config["paths"]["images"]),
        "report": _p(config["paths"]["report"]),
        "addons": _p(config["paths"]["addons"]),
    }

    return paths, config
'''
    utils_path = os.path.join(directories['src'], 'utils.py')
    with open(utils_path, 'w', encoding='utf-8') as file:
        file.write(utils_content)

    # README.md
    readme_content = f'''# {project_name}

## Introduction

Provide an overview of the project here. Describe the purpose and scope of the project.

## How to Use

Explain how to set up and run the project. Include instructions on installation, configuration, and execution.

## Conclusion

Summarize the project and discuss any future developments or considerations.
'''
    with open(os.path.join(project_path, 'README.md'), 'w', encoding='utf-8') as file:
        file.write(readme_content)

    # .gitignore
    gitignore_content = '''# venv
venv/
__pycache__/
*.pyc
*.pyo
*.zip
*.log
.env
.DS_Store
.ipynb_checkpoints/
'''
    with open(os.path.join(project_path, '.gitignore'), 'w', encoding='utf-8') as file:
        file.write(gitignore_content)

    # venv
    print("Criando virtualenv...")
    venv_path = os.path.join(project_path, "venv")
    run([sys.executable, "-m", "venv", venv_path])

    # Perguntas sobre Git
    if ask_git:
        init_git = prompt_bool("Deseja inicializar um repositório Git agora?", default=True)
    else:
        init_git = True

    if init_git:
        if not have_git():
            print("Aviso: Git não encontrado no PATH. Pulei a inicialização do repositório.")
        else:
            do_commit = prompt_bool("Criar commit inicial e definir branch principal como 'main'?", default=True)
            remote_url = None
            if prompt_bool("Adicionar um remote 'origin' agora?", default=False):
                remote_url = input("Informe a URL do remote (HTTPS ou SSH). Deixe vazio para cancelar: ").strip() or None

            try:
                init_git_repo(project_path, do_initial_commit=do_commit, remote_url=remote_url)
            except Exception as e:
                print(f"Falha ao configurar Git: {e}")

    print(f"\nProjeto '{project_name}' criado em: {project_path}")
    print("Próximos passos:")
    print(f"   cd {project_name}")
    print("   # Ativar venv")
    print("   # Linux/macOS:")
    print("   source venv/bin/activate")
    print("   # Windows (PowerShell):")
    print("   .\\venv\\Scripts\\Activate.ps1")
    print("   pip install -r requirements.txt")
    if init_git and have_git():
        print("\nSe você adicionou remote e quer enviar agora:")
        print("   git push -u origin main")

if __name__ == '__main__':
    base_path = input('Enter the base path for the project: ').strip()
    project_name = input('Enter the project name: ').strip()
    create_project_structure(base_path, project_name, ask_git=True)
