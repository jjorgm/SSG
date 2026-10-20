import os

from extractmarkdown import extract_title
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as md_file:
        md_contents = md_file.read()

    with open(template_path) as template_file:
        template_contents = template_file.read()

    html_string = markdown_to_html_node(md_contents).to_html()
    page_title = extract_title(md_contents)
    full_html = template_contents.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, mode='w') as html_file:
        html_file.write(full_html)
