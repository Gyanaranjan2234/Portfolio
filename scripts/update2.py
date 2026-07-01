import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# CSS Modification
css_old = '.achievements-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.6rem; }'
css_new = '''.achievements-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 1.6rem; }
.achievement-card { flex: 1 1 260px; max-width: 100%; }
@media (min-width: 768px) { .achievements-grid .achievement-card { max-width: calc(50% - 0.8rem); } }
@media (min-width: 1024px) { .achievements-grid .achievement-card { max-width: calc(25% - 1.2rem); } }'''
css = css.replace(css_old, css_new)

# HTML Reordering
card_bput = '''                <div class="achievement-card" data-aos="flip-left" data-aos-delay="0">
                    <div class="achievement-icon">
                        <i class="fas fa-trophy"></i>
                    </div>
                    <h3>BPUT Hackathon Winner</h3>
                    <p class="achievement-subtitle">3rd Place</p>
                    <p class="achievement-date">November 2025</p>
                    <p class="achievement-details">
                        <strong>AI Resume Builder for Blue-Collar Workers</strong><br>
                        Innovative solution leveraging AI to create personalized resumes for underrepresented workforce segments.
                    </p>
                </div>'''

card_ibm = '''                <div class="achievement-card" data-aos="flip-left" data-aos-delay="100">
                    <div class="achievement-icon achievement-icon-blue">
                        <i class="fas fa-shield-halved"></i>
                    </div>
                    <h3>IBM SkillsBuild</h3>
                    <p class="achievement-subtitle">Advanced IT Skills</p>
                    <p class="achievement-date">January 2026</p>
                    <p class="achievement-details">
                        <strong>Cyber Security Certificate of Recognition</strong><br>
                        IBM SkillsBuild Program with ICT Academy. Successfully completed the Cyber Security certification program under IBM SkillsBuild in Advanced IT Skills.
                    </p>
                </div>'''

card_google = '''                <div class="achievement-card" data-aos="flip-left" data-aos-delay="200">
                    <div class="achievement-icon">
                        <i class="fab fa-google"></i>
                    </div>
                    <h3>Google Cybersecurity</h3>
                    <p class="achievement-subtitle">Foundations of Cybersecurity</p>
                    <p class="achievement-date">June 2026</p>
                    <p class="achievement-details">
                        Completed Google's Foundations of Cybersecurity course, covering core security concepts, risk management, security operations, and industry best practices for cybersecurity professionals.
                    </p>
                </div>'''

card_deloitte = '''                <div class="achievement-card" data-aos="flip-left" data-aos-delay="300">
                    <div class="achievement-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <h3>Deloitte Forage</h3>
                    <p class="achievement-subtitle">Cybersecurity Job Simulation</p>
                    <p class="achievement-date">Completed</p>
                    <p class="achievement-details">
                        Comprehensive cybersecurity job simulation covering real-world security challenges and industry practices.
                    </p>
                </div>'''

card_tryhackme = '''                <div class="achievement-card" data-aos="flip-left" data-aos-delay="400">
                    <div class="achievement-icon">
                        <i class="fas fa-calendar-check"></i>
                    </div>
                    <h3>TryHackMe Advent of Cyber 2025</h3>
                    <p class="achievement-subtitle">Cyber Security Challenges</p>
                    <p class="achievement-date">December 2025</p>
                    <p class="achievement-details">
                        Successfully completed 24 hands-on cybersecurity challenges covering security fundamentals, threat analysis, and practical defensive concepts through TryHackMe's Advent of Cyber program.
                    </p>
                </div>'''

card_ai = '''                <div class="achievement-card" data-aos="flip-left" data-aos-delay="500">
                    <div class="achievement-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3>AI Certificate</h3>
                    <p class="achievement-subtitle">YHills Edutech Pvt. Ltd.</p>
                    <p class="achievement-date">Completed</p>
                    <p class="achievement-details">
                        Comprehensive AI and machine learning fundamentals certification with practical applications.
                    </p>
                </div>'''

new_grid = f'''            <div class="achievements-grid">
{card_bput}

{card_ibm}

{card_google}

{card_deloitte}

{card_tryhackme}

{card_ai}
            </div>'''

# Extract the existing grid content to replace it.
pattern = r'            <div class="achievements-grid">.*?</div>\s*</div>\s*</section>'
match = re.search(pattern, html, re.DOTALL)
if match:
    # Need to keep the closing tags
    full_new = new_grid + '\n        </div>\n    </section>'
    html = html[:match.start()] + full_new + html[match.end():]
else:
    print("Could not match the achievements grid in HTML.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates applied.")
