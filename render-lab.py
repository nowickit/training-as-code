import os
import json
import re
os.system("clear")

# Load variables from variables.json
with open('variables.json', 'r') as json_file:
    variables = json.load(json_file)

# Function to replace variables in the format {{example}} with their values from variables.json
def replace_variables(content, variables):
    for key, value in variables.items():
        content = re.sub(r'\{\{' + re.escape(key) + r'\}\}', str(value), content)
    return content

# Process the lab.md file
md_path = 'lab/lab.md'
if os.path.exists(md_path):
    with open(md_path, 'r') as md_file:
        md_content = md_file.read()
    md_content = replace_variables(md_content, variables)
    with open('lab/lab_rendered.md', 'w') as rendered_md_file:
        rendered_md_file.write(md_content)
    print("File has been successfully rendered and saved as lab/lab_rendered.md.")
else:
    print(f"{md_path} does not exist.")

# Process the lab.htm file
html_path = 'lab/lab.htm'
if os.path.exists(html_path):
    with open(html_path, 'r') as html_file:
        html_content = html_file.read()
    html_content = replace_variables(html_content, variables)
    
    # Update the HTML title tag if {{title}} exists in variables.json
    if 'title' in variables:
        html_content = re.sub(r'<title>.*?</title>', f'<title>{variables["title"]}</title>', html_content)
    
    with open('lab/lab_rendered.htm', 'w') as rendered_html_file:
        rendered_html_file.write(html_content)
    print("File has been successfully rendered and saved as lab/lab_rendered.htm.")
else:
    print(f"{html_path} does not exist.")