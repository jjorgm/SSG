import os

from extractmarkdown import extract_title
from markdown_blocks import markdown_to_html_node


def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as md_file:
        md_contents = md_file.read()

    with open(template_path) as template_file:
        template_contents = template_file.read()

    html_string = markdown_to_html_node(md_contents).to_html()
    page_title = extract_title(md_contents)
    full_html = template_contents.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, mode='w') as html_file:
        html_file.write(full_html)

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    content_paths = os.listdir(dir_path_content)
    for content_path in content_paths:
        content = os.path.join(dir_path_content, content_path)
        if os.path.isfile(content):
            html_page = os.path.join(dest_dir_path, "index.html")
            generate_page(basepath, content, template_path, html_page)
        else:
            updated_dest_dir_path = os.path.join(dest_dir_path, content_path)
            generate_pages_recursive(basepath, content, template_path, updated_dest_dir_path)
