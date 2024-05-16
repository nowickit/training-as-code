import os
import json
import re

def load_variables(json_file):
    with open(json_file, 'r') as f:
        variables = json.load(f)
    return variables

def replace_variables_in_file(file_path, variables):
    with open(file_path, 'r') as file:
        content = file.read()
    
    for key, value in variables.items():
        content = re.sub(r"\{\{" + re.escape(key) + r"\}\}", value, content)
    
    new_file_path = os.path.splitext(file_path)[0] + '_rendered.md'
    new_file_path = new_file_path.replace("templates", "rendered")

    with open(new_file_path, 'w') as file:
        file.write(content)

def process_directory(directory, variables):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                replace_variables_in_file(file_path, variables)

if __name__ == "__main__":
    json_file = 'variables.json'
    directory_to_process = 'templates'

    variables = load_variables(json_file)
    process_directory(directory_to_process, variables)