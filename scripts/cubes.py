import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change all "col-2" to "col-3" in the skill-chip-grid
html = html.replace('class="skill-chip-grid col-2"', 'class="skill-chip-grid col-3"')

# For the single Snort element, the user wants it to just flow or be centered?
# The user said:
# "Nessus        Wazuh        Splunk
# Snort"
# I can either let it naturally sit on the left (default for grid) or center it.
# Let's let it sit naturally first, or center it if it looks better. I'll just change the class.
# Wait, for Incident Response in concepts it is centered with inline style. Let's leave Snort as is, it will be left aligned.

html = html.replace('href="style.css?v=6"', 'href="style.css?v=7"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the specific col-2 overrides
css = re.sub(r'\.skill-chip-grid\.col-2 \.skill-chip \{.*?\}\n', '', css)
css = re.sub(r'\.skill-chip-grid\.col-2 \.skill-chip span \{.*?\}\n', '', css)

# Enforce square aspect ratio or uniform height/padding on all .skill-chip
# The current .skill-chip is:
# .skill-chip {
#     background: rgba(0, 255, 136, 0.03);
#     border: 1px solid rgba(255, 255, 255, 0.08);
#     border-radius: 6px; padding: 0.8rem 0.5rem;
#     display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.5rem;
#     transition: var(--transition);
#     cursor: default;
#     height: 100%;
# }
# To make them square cubes, we can add spect-ratio: 1 / 1; or give them a fixed min-height.
# Let's add spect-ratio: 1 / 1; and ensure text aligns nicely.
# Actually, the user says "uniform cube/grid layout similar to the Cybersecurity Concepts card."
# In Concepts, they were already vertical. Let's just add spect-ratio: 1 / 1; or min-height: 80px; to ensure they are distinct cubes.
# I'll just modify the base .skill-chip to ensure uniform height and styling.

css = css.replace('.skill-chip {\n    background:', '.skill-chip {\n    aspect-ratio: 1 / 1;\n    background:')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates applied.")
