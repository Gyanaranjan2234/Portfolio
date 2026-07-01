import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add OpenVAS and Nikto to Security Tools
# Look for Splunk and Snort in Security Tools
security_tools_addition = '''<div class="skill-chip"><i class="fas fa-piggy-bank"></i><span>Snort</span></div>
                        <div class="skill-chip"><i class="fas fa-search"></i><span>OpenVAS</span></div>
                        <div class="skill-chip"><i class="fas fa-spider"></i><span>Nikto</span></div>'''

html = html.replace('<div class="skill-chip"><i class="fas fa-piggy-bank"></i><span>Snort</span></div>', security_tools_addition)

# 2. Cybersecurity Concepts inline style removal and additions
# Replace the Incident Response inline styling with a normal chip
incident_response_styled = '<div class="skill-chip" style="grid-column: 1 / -1; margin: 0 auto; width: 60%; flex-direction: row; gap: 0.5rem;"><i class="fas fa-siren-on" style="margin-right:0.5rem"></i><span>Incident Response</span></div>'
incident_response_clean = '<div class="skill-chip"><i class="fas fa-siren-on"></i><span>Incident Response</span></div>'

html = html.replace(incident_response_styled, incident_response_clean)

# Add Threat Hunting and Digital Forensics
concepts_addition = '''<div class="skill-chip"><i class="fas fa-siren-on"></i><span>Incident Response</span></div>
                        <div class="skill-chip"><i class="fas fa-crosshairs"></i><span>Threat Hunting</span></div>
                        <div class="skill-chip"><i class="fas fa-microscope"></i><span>Digital Forensics</span></div>'''

html = html.replace(incident_response_clean, concepts_addition)

# Bump version
html = html.replace('href="style.css?v=7"', 'href="style.css?v=8"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Additions made.")
