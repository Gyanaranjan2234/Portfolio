import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix .carousel-wrapper
css = css.replace('.carousel-wrapper { display: flex; align-items: center; justify-content: flex-start; gap: 1rem; position: relative; width: 100%; }', '.carousel-wrapper { display: flex; align-items: center; justify-content: space-between; gap: 1rem; position: relative; width: 100%; }')

# Fix .timeline-header
css = css.replace('.timeline-header { display: flex; justify-content: flex-start; align-items: flex-start; margin-bottom: 1rem; \nflex-wrap: wrap; gap: 1rem; }', '.timeline-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; flex-wrap: wrap; gap: 1rem; }')
css = css.replace('.timeline-header { display: flex; justify-content: flex-start; align-items: flex-start; margin-bottom: 1rem; flex-wrap: wrap; gap: 1rem; }', '.timeline-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; flex-wrap: wrap; gap: 1rem; }')

# Navbar might also have been space-between?
# Let's check navbar
# usually navbar has space-between
css = css.replace('.nav-container {\n    display: flex;\n    justify-content: flex-start;\n    align-items: center;\n    height: 100%;\n}', '.nav-container {\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n    height: 100%;\n}')

# Check header container
css = css.replace('.header-container { display: flex; justify-content: flex-start; align-items: center; height: 100%; max-width: 1200px; margin: 0 auto; padding: 0 2rem; }', '.header-container { display: flex; justify-content: space-between; align-items: center; height: 100%; max-width: 1200px; margin: 0 auto; padding: 0 2rem; }')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored justify-content for other elements.")
