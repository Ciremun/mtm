#!/usr/bin/env python3

if __name__ != '__main__':
    exit(1)

# Minify CSS
# from source.util import *

# def minify(css_path: str, min_css_path: str) -> None:
#     min_css = minify_css(css_path)
#     if min_css:
#         with open(min_css_path, 'w') as f:
#             f.write(min_css)

# minify('docs/static/main.css', 'docs/static/main.min.css')
# minify('docs/static/fixed_footer.css', 'docs/static/fixed_footer.min.css')

# Evaluate Template
from jinja2 import Environment, FileSystemLoader

def url_for(folder: str, *, filename: str):
    return f'/{folder}/{filename}'

def build_page(name: str) -> None:
    template = env.get_template(f'{name}.jinja')
    page = template.render(**globals())
    with open(f'{name}.html', 'w', encoding='utf-8') as f:
        f.write(page)

main_css = 'main.css'

env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)

build_page('index')
