# Project Initialization Script

<div align="center">
  <img src="images/default_folder_structure.png" alt="Default Folder Structure" width="500"/>
  <h4>Figure 1: Default Folder Structure</h4>
</div>

## Summary

This project provides a Python script that automates the creation of a standardized project directory structure. By running the script, users can quickly set up a new project with a consistent folder hierarchy, essential starter files, and initial code templates, streamlining the development process and ensuring uniformity across multiple projects.

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
- [Customization Guide](#customization-guide)
  - [Modifying the Directory Structure](#modifying-the-directory-structure)
  - [Updating Requirements](#updating-requirements)
  - [Customizing the Main Python Script](#customizing-the-main-python-script)
  - [Adjusting the README Template](#adjusting-the-readme-template)
- [Conclusion](#conclusion)

## Introduction

This project presents a Python-based solution designed to automate the initialization of a standardized project directory structure. By executing a single script, users can generate a comprehensive folder hierarchy along with essential starter files, facilitating a consistent and efficient workflow for data analysis, software development, or research projects.

## Features

- **Automated Directory Creation**: Generates a predefined folder structure, including:

  - `src/`: Contains source code files.
    - `config.yaml`: Configuration file with predefined paths.
    - `<project_name>.py`: Main Python script with essential imports and initial setup.
  - `data/`:
    - `raw/`: Directory for raw data.
    - `processed/`: Directory for processed data.
  - `images/`: Folder for storing images and figures.
  - `report/`: Directory for reports and documentation.
  - `addons/`: Folder for additional scripts or utilities.
  - `requirements.txt`: File listing required Python packages.
  - `README.md`: A template README file to guide project documentation.

- **Configuration Management**: Initializes a `config.yaml` file with relative paths to key directories, allowing for flexible path handling within the project.

- **Starter Code Generation**: Creates a main Python script that:

  - Imports essential libraries (`pandas`, `matplotlib`, `datetime`, `os`, `yaml`).
  - Loads configuration settings.
  - Initializes directory paths based on the configuration.
  - Prints the project initialization date and time.

- **Requirements Specification**: Provides a `requirements.txt` file to facilitate the setup of the Python environment with all necessary dependencies.

- **README Template**: Generates a `README.md` file with a structured outline, including sections for Introduction, How to Use, and Conclusion, guiding users on how to document their project effectively.

## How to Use

1. **Clone the Repository**: Download or clone the project to your local machine.

2. **Run the Initialization Script**:

   ```bash
   python project_creator.py
   ```

   - **Input Prompts**:
     - **Base Path**: Enter the directory where you want the project to be created.
     - **Project Name**: Enter the desired name for your project.

3. **Customize Your Project**:

   - Edit the `config.yaml` file in the `src/` directory to adjust configuration settings as needed.
   - Add your code to the `<project_name>.py` script in the `src/` directory.
   - Update the `README.md` with detailed information about your project.

## Code Overview

The `project_creator.py` script automates several tasks to set up your project. Below is an overview of its main components and guidance on how to manipulate them.

### Directory Structure Creation

```python
# Define subdirectories with their keys
directories = {
    'src': os.path.join(project_path, 'src'),
    'data_raw': os.path.join(project_path, 'data', 'raw'),
    'data_processed': os.path.join(project_path, 'data', 'processed'),
    'images': os.path.join(project_path, 'images'),
    'report': os.path.join(project_path, 'report'),
    'addons': os.path.join(project_path, 'addons'),
}

# Create subdirectories
for dir_path in directories.values():
    os.makedirs(dir_path, exist_ok=True)
```

- **Explanation**:
  - A dictionary named `directories` maps directory identifiers to their paths.
  - The `os.makedirs()` function creates each directory. The `exist_ok=True` parameter avoids errors if the directory already exists.
- **How to Manipulate**:
  - **Add New Directories**: Include new key-value pairs in the `directories` dictionary.
    ```python
    directories['logs'] = os.path.join(project_path, 'logs')
    ```
  - **Modify Directory Paths**: Change the paths in the dictionary to suit your project's needs.

### Requirements File Generation

```python
# Create requirements.txt
requirements = '''pandas
matplotlib
datetime
os
pyyaml
'''
with open(os.path.join(project_path, 'requirements.txt'), 'w') as file:
    file.write(requirements)
```

- **Explanation**:
  - The `requirements` string lists the Python packages required for the project.
  - The script writes this string to a `requirements.txt` file in the project root.
- **How to Manipulate**:
  - **Add Packages**: Include additional package names in the `requirements` string.
    ```python
    requirements = '''pandas
matplotlib
datetime
os
pyyaml
numpy
scipy
'''
    ```
  - **Specify Versions**: Pin packages to specific versions for consistency.
    ```python
    requirements = '''pandas==1.3.0
matplotlib==3.4.2
pyyaml==5.4.1
'''
    ```

### Main Python Script Generation

```python
# Create the main Python script
script_content = f'''# Made by Juliano E. S. Padua
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import yaml

script_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(script_dir, "config.yaml")

# Load configuration
with open(config_dir, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize paths from config
data_raw_path = os.path.join(script_dir, config['paths']['data_raw'])
data_processed_path = os.path.join(script_dir, config['paths']['data_processed'])
images_path = os.path.join(script_dir, config['paths']['images'])
report_path = os.path.join(script_dir, config['paths']['report'])
addons_path = os.path.join(script_dir, config['paths']['addons'])

# Your code starts here
current_datetime = datetime.datetime.now()
print(f"Project '{project_name}' initialized on {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
'''
script_path = os.path.join(directories['src'], f'{project_name}.py')
with open(script_path, 'w') as file:
    file.write(script_content)
```

- **Explanation**:
  - The script generates a main Python file named after your project.
  - It includes essential imports, loads configurations, initializes paths, and prints the initialization timestamp.
- **How to Manipulate**:
  - **Change Imports**: Modify the `import` statements to include or exclude libraries.
    ```python
    import numpy as np
    ```
  - **Alter Code Template**: Edit the `script_content` string to add default functions or classes.
    ```python
    script_content = f'''# Made by {your_name}
# Additional code...

  - **Update Initialization Message**: Customize the print statement as desired.

### README.md Template Creation

```python
# Create README.md with base topic construction
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
```

- **Explanation**:
  - Generates a basic `README.md` file with placeholders for key sections.
- **How to Manipulate**:
  - **Customize the Template**: Modify the `readme_content` string to include additional sections like Features, License, or Contact Information.
    ```python
    readme_content = f'''# {project_name}

## Customization Guide

### Modifying the Directory Structure

- **Add Directories**: Update the `directories` dictionary.
- **Remove Directories**: Delete entries from the `directories` dictionary.
- **Change Paths**: Adjust the paths to fit your project layout.

### Updating Requirements

- **Add Dependencies**: Include new packages in the `requirements` string.
- **Remove Dependencies**: Delete package names from the string.
- **Version Control**: Specify package versions to ensure compatibility.

### Customizing the Main Python Script

- **Default Functions**: Add function templates to `script_content`.
  ```python
  def main():
      # Your main function code here

  if __name__ == '__main__':
      main()
  ```
- **Author Information**: Update the header comment with your name or project details.
- **Additional Modules**: Import other modules as needed.

### Adjusting the README Template

- **Additional Sections**: Add new sections like FAQs, Troubleshooting, or Roadmap.
- **Placeholders**: Replace placeholder text with actual content.
- **Formatting**: Use Markdown syntax to enhance readability (e.g., tables, code blocks, images).

## Conclusion

This project serves as a foundational tool to streamline the setup of new projects by automating the creation of a standardized directory structure and initializing essential files. By understanding and manipulating the provided code, you can tailor the project initialization process to fit your specific needs, enhancing productivity and ensuring consistency across different projects.
