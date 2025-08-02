import os
import datetime
import subprocess
import sys

def sanitize_path(path):
    """Remove aspas do caminho."""
    return path.strip('\'"')

def create_project_structure(base_path, project_name):
    base_path = sanitize_path(base_path)
    current_datetime = datetime.datetime.now()

    # Cria diretório principal do projeto
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

    # Cria requirements.txt
    requirements = '''requests>=2.31.0
beautifulsoup4>=4.12.2
pyyaml>=6.0.1
tqdm>=4.66.1
pandas>=2.2.2
streamlit>=1.35.0
'''
    with open(os.path.join(project_path, 'requirements.txt'), 'w') as file:
        file.write(requirements)

    # Cria config.yaml (na raiz, não dentro da src)
    config_content = '''# configuration parameters
paths:
  data_raw: ./data/raw
  data_processed: ./data/processed
  images: ./images
  report: ./report
  addons: ./addons
'''
    with open(os.path.join(project_path, 'config.yaml'), 'w') as file:
        file.write(config_content)

    # Cria script principal na src
    script_content = f'''# Made by Juliano E. S. Padua
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import yaml

script_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(script_dir, "..", "config.yaml")

# load configuration
with open(config_dir, 'r') as config_file:
    config = yaml.safe_load(config_file)

# initialize paths from config
data_raw_path = os.path.join(script_dir, config['paths']['data_raw'])
data_processed_path = os.path.join(script_dir, config['paths']['data_processed'])
images_path = os.path.join(script_dir, config['paths']['images'])
report_path = os.path.join(script_dir, config['paths']['report'])
addons_path = os.path.join(script_dir, config['paths']['addons'])

# your code starts here
current_datetime = datetime.datetime.now()
print(f"Project '{project_name}' initialized on {{current_datetime.strftime('%Y-%m-%d %H:%M:%S')}}")
'''
    script_path = os.path.join(directories['src'], f'{project_name}.py')
    with open(script_path, 'w') as file:
        file.write(script_content)

    # Cria README.md
    readme_content = f'''# {project_name}

## Introduction

*Provide an overview of the project here. Describe the purpose and scope of the project.*

## How to Use

*Explain how to set up and run the project. Include instructions on installation, configuration, and execution.*

## Conclusion

*Summarize the project and discuss any future developments or considerations.*
'''
    with open(os.path.join(project_path, 'README.md'), 'w') as file:
        file.write(readme_content)

    # Cria .gitignore
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
    with open(os.path.join(project_path, '.gitignore'), 'w') as file:
        file.write(gitignore_content)

    # Cria e ativa ambiente virtual
    print("Creating virtual environment...")
    venv_path = os.path.join(project_path, "venv")
    subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)

    # Inicializa repositório Git
    print("Initializing Git repository...")
    subprocess.run(["git", "init"], cwd=project_path, check=True)

    print(f"\n✅ Projeto '{project_name}' criado com sucesso em: {project_path}")
    print("➡️  Próximos passos:")
    print(f"   cd {project_name}")
    print("   source venv/bin/activate   # (Linux/macOS)")
    print("   .\\venv\\Scripts\\activate   # (Windows)")
    print("   pip install -r requirements.txt")

if __name__ == '__main__':
    base_path = input('Enter the base path for the project: ').strip()
    project_name = input('Enter the project name: ').strip()
    create_project_structure(base_path, project_name)
