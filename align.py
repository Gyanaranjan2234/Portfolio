import re

# Update index.html for version bump
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="style.css?v=8"', 'href="style.css?v=9"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('justify-content: space-between;', 'justify-content: flex-start;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Alignment fixed.")
