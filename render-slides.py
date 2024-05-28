
#    new_file_path = new_file_path.replace("templates", "rendered")

import os
import json
import re

os.system("clear")

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
    new_file_path = new_file_path.replace("slides", "rendered")
    with open(new_file_path, 'w') as file:
        file.write(content)
    
    return new_file_path

def process_directory(directory, variables):
    rendered_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                rendered_file_path = replace_variables_in_file(file_path, variables)
                rendered_files.append(rendered_file_path)
    return rendered_files

def merge_files(file_list):
    merged_content = ""
    for file_path in file_list:
        with open("rendered/"+file_path, 'r') as file:
            merged_content += '<section data-markdown '
            merged_content += 'data-separator="---" data-separator-vertical="--"'
            merged_content += 'data-background-image="img/bg.png" data-background-size="1200px"'
            merged_content += 'data-separator-notes="!Note:"'
            merged_content += '>'
            merged_content += "\n" + file.read() +  "\n" + "</section>" + "\n"
    return merged_content

def replace_sections_in_slides(merged_content, slides_file):
    # Create the "rendered" directory if it doesn't exist
    if not os.path.exists('rendered'):
        os.makedirs('rendered')
    
    # Read the content of the original slides file
    with open(slides_file, 'r') as file:
        content = file.read()
    
    # Replace the sections placeholder with the merged content
    content = re.sub(r"\{\{sections\}\}", merged_content, content)
    
    # Define the path for the new file in the "rendered" folder
    new_file_path = os.path.join('rendered', os.path.basename(slides_file))
    
    # Write the updated content to the new file
    with open(new_file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    json_file = 'variables.json'
    directory_to_process = 'slides'
    sections_file = 'sections.json'
    slides_file = 'slides.htm'

    # Load variables
    variables = load_variables(json_file)
    # Process directory and get list of rendered files
    rendered_files = process_directory(directory_to_process, variables)
    # Load sections
    with open(sections_file, 'r') as f:
        sections_list = json.load(f)
    # Map sections to rendered file paths
    rendered_sections_list = [os.path.splitext(file)[0] + '_rendered.md' for file in sections_list]
    # Merge rendered files
    merged_content = merge_files(rendered_sections_list)
    # Replace sections in slides.htm
    replace_sections_in_slides(merged_content, slides_file)
    print("Slide deck has been successfully rendered.")