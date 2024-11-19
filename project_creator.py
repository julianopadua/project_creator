import os
import datetime  # Added import for datetime

def sanitize_path(path):
    # remove any enclosing quotes from the path
    return path.strip('\'"')

def create_project_structure(base_path, project_name):
    # sanitize the base path
    base_path = sanitize_path(base_path)
        # print date and time when the project was initialized
    current_datetime = datetime.datetime.now()

    # create the main project directory
    project_path = os.path.join(base_path, project_name)
    os.makedirs(project_path, exist_ok=True)
    
    # define subdirectories with their keys
    directories = {
        'src': os.path.join(project_path, 'src'),
        'data_raw': os.path.join(project_path, 'data', 'raw'),
        'data_processed': os.path.join(project_path, 'data', 'processed'),
        'images': os.path.join(project_path, 'images'),
        'report': os.path.join(project_path, 'report'),
        'addons': os.path.join(project_path, 'addons'),
    }
    
    # create subdirectories
    for dir_path in directories.values():
        os.makedirs(dir_path, exist_ok=True)
    
    # create requirements.txt
    requirements = '''pandas
matplotlib
datetime
os
pyyaml
'''
    with open(os.path.join(project_path, 'requirements.txt'), 'w') as file:
        file.write(requirements)
    
    # initialize config.yaml with path variables
    config_content = '''# configuration parameters
paths:
  data_raw: ../data/raw
  data_processed: ../data/processed
  images: ../images
  report: ../report
  addons: ../addons
'''
    with open(os.path.join(directories['src'], 'config.yaml'), 'w') as file:
        file.write(config_content)
    
    # create the main Python script
    script_content = f'''# Made by Juliano E. S. Padua
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import yaml

script_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(script_dir, "config.yaml")

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
print(f"Project '{project_name}' initialized on {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
'''
    script_path = os.path.join(directories['src'], f'{project_name}.py')
    with open(script_path, 'w') as file:
        file.write(script_content)
    
    # create README.md with base topic construction
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
    
    
if __name__ == '__main__':
    base_path = input('Enter the base path for the project: ').strip()
    project_name = input('Enter the project name: ').strip()
    create_project_structure(base_path, project_name)
