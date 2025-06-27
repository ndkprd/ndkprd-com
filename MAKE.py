import os
import shutil
import yaml
from jinja2 import Environment, FileSystemLoader

# Paths
SRC_DIR = 'src'
OUTPUT_DIR = 'output'
ASSETS_DIR = os.path.join(SRC_DIR, 'assets')
OUTPUT_ASSETS_DIR = os.path.join(OUTPUT_DIR, 'assets')
CONFIG_FILE = 'config.yaml'
TEMPLATE_FILE = 'index.html.j2'
STYLE_FILE = 'style.css'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load config.yaml
def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Render Jinja2 template
def render_template(context):
    env = Environment(loader=FileSystemLoader(SRC_DIR))
    template = env.get_template(TEMPLATE_FILE)
    rendered = template.render(**context)
    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(rendered)

# Copy style.css
def copy_style():
    shutil.copy(os.path.join(SRC_DIR, STYLE_FILE), os.path.join(OUTPUT_DIR, STYLE_FILE))

# Copy assets directory
def copy_assets():
    if os.path.exists(OUTPUT_ASSETS_DIR):
        shutil.rmtree(OUTPUT_ASSETS_DIR)
    shutil.copytree(ASSETS_DIR, OUTPUT_ASSETS_DIR)

if __name__ == '__main__':
    config = load_config()
    render_template(config)
    copy_style()
    copy_assets()
    print('Site generated in output/')
