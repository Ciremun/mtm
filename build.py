#!/usr/bin/env python3

if __name__ != '__main__':
    exit(1)

# Evaluate Template
from jinja2 import Environment, FileSystemLoader

def url_for(folder: str, *, filename: str):
    return f'{folder}/{filename}'

def build_page(name: str) -> None:
    template = env.get_template(f'{name}.jinja')
    page = template.render(**globals())
    with open(f'{name}.html', 'w', encoding='utf-8') as f:
        f.write(page)

main_css = 'main.min.css'
index_js = 'index.min.js'

env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)

build_page('index')
