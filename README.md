# Project Initialization Script

<div align="center">
  <img src="images/default_folder_structure.png" alt="Default Folder Structure" width="500"/>
  <h4>Figure 1 – Default Folder Structure</h4>
</div>

## Summary
This project contains a Python script that **automatically scaffolds a complete, production-ready project**.  
In a single run it:

1. Creates a clean folder hierarchy.  
2. Generates essential starter files (`config.yaml`, `requirements.txt`, `README.md`, etc.).  
3. Sets up a Python **virtual environment** (`venv/`).  
4. Creates a sensible **.gitignore** and **initialises a Git repository**.  

The goal is to eliminate boilerplate and guarantee consistency across all your data-science, research, or software projects.

---

## Table of Contents
- [Summary](#summary)
- [Introduction](#introduction)
- [Features](#features)
- [How to Use](#how-to-use)
- [Code Overview](#code-overview)
  - [Directory Structure Creation](#directory-structure-creation)
  - [Requirements File Generation](#requirements-file-generation)
  - [Main Python Script Generation](#main-python-script-generation)
  - [README.md Template Creation](#readmemd-template-creation)
  - [Git & Virtual Environment Setup](#git--virtual-environment-setup)
- [Customization Guide](#customization-guide)
- [Conclusion](#conclusion)

---

## Introduction
Manually wiring every new project is tedious and error-prone.  
`project_creator.py` automates this routine, giving you a ready-to-code workspace with:

- Logical folder layout
- Pre-filled configuration
- Isolated dependency management (virtual env)
- Version-control baseline (Git)

Open the project and start building—no yak-shaving required.

---

## Features
| Category | Details |
|----------|---------|
| **Folder structure** | `src/`, `data/raw/`, `data/processed/`, `images/`, `report/`, `addons/` |
| **Config** | `config.yaml` now lives at the project root (not inside `src/`) |
| **Utils file** | `src/utils.py` loads the config and resolves all key paths |
| **Starter code** | `src/<project_name>.py` initialize the main project code |
| **Dependency file** | `requirements.txt` populated with common libs using `>=` specifiers |
| **Virtual env** | Automatically runs `python -m venv venv` in the project root |
| **Git** | Executes `git init` and writes a Python-centric `.gitignore` |
| **Docs** | Auto-generated `README.md` ready for editing, plus the architecture diagram placeholder |
| **Cross-platform** | Works on Windows, Linux and macOS (PowerShell / bash) |

---

## How to Use


### 1 – Run the script
```bash
python project_creator.py
````
### You will be asked for:
   • Base path   →  Where to create the project

   • Project name → Folder & module name

### 2 – Enter the project
```bash
cd <project_name>
````

### 3 – Activate the virtual environment
#### Windows
```bash
.\venv\Scripts\activate
````
#### macOS / Linux
```bash
source venv/bin/activate
````

### 4 – Install dependencies
```bash
pip install -r requirements.txt
````

You are now ready to add notebooks, source code, data, etc.

---

## Code Overview

### Directory Structure Creation

```python
def load_config():
    """Carrega config.yaml do diretório raiz e resolve caminhos relativos."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "..", "config.yaml")

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    paths = {
        "script_dir": script_dir,
        "data_raw": os.path.join(script_dir, config["paths"]["data_raw"]),
        "data_processed": os.path.join(script_dir, config["paths"]["data_processed"]),
        "images": os.path.join(script_dir, config["paths"]["images"]),
        "report": os.path.join(script_dir, config["paths"]["report"]),
        "addons": os.path.join(script_dir, config["paths"]["addons"]),
    }

    return paths, config
```

*Add, remove, or rename keys in `load_config` inside `utils.py` to customise your layout.*

### Requirements File Generation

The script writes:

```txt
requests>=2.31.0
beautifulsoup4>=4.12.2
pyyaml>=6.0.1
tqdm>=4.66.1
pandas>=2.2.2
streamlit>=1.35.0
```

Add or pin packages here as needed.

### Main Python Script Generation

```python
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
...
```

Use this template as the entry point for your application or analysis.

### README.md Template Creation

A skeleton README is placed at the root, containing **Introduction, How to Use, and Conclusion** sections.
Replace placeholders and add badges, screenshots, or extra sections as you wish.

### Git & Virtual Environment Setup

```python
subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
subprocess.run(["git", "init"], cwd=project_path, check=True)
```

A standard Python `.gitignore` (ignores `venv/`, `__pycache__/`, etc.) is added automatically.

---

## Customization Guide

| Task                     | Where to change                  |
| ------------------------ | -------------------------------- |
| **Add new folders**      | Edit the `directories` dict      |
| **Change default deps**  | Modify the `requirements` string |
| **Alter starter script** | Update `script_content`          |
| **Update `.gitignore`**  | Adjust `gitignore_content`       |
| **Add README sections**  | Edit `readme_content`            |

---

## Conclusion

`project_creator.py` turns project kickoff into a 30-second command-line task.
Focus on code and research, not boilerplate.

