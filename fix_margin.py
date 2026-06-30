import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the margin-top: auto; from .skill-chip-grid
css = css.replace('.skill-chip-grid {\n    display: grid; gap: 0.8rem; width: 100%; margin-top: auto;\n}', '.skill-chip-grid {\n    display: grid; gap: 0.8rem; width: 100%;\n}')

# To be safe, also replace if it's on one line
css = css.replace('margin-top: auto;', '') # this might be dangerous if there are other auto margins, let's just do it cleanly

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS Fixed.")
