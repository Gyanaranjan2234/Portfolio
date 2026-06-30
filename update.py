import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Cache bust
content = content.replace('href="style.css"', 'href="style.css?v=3"')
content = content.replace('src="script.js"', 'src="script.js?v=3"')

# 2. Shorten ReconSentinel description
old_desc = 'Intelligent network reconnaissance platform for asset discovery, host discovery, port scanning, service detection, and CVE intelligence lookup. Maps findings to MITRE ATT&CK techniques, generates risk scores, creates PDF security reports, and includes an AI assistant for security insights.'
new_desc = 'Intelligent network reconnaissance platform for asset discovery, host discovery, port scanning, service detection, and CVE intelligence lookup. Maps findings to MITRE ATT&CK techniques, generates risk scores, and creates PDF security reports.'
content = content.replace(old_desc, new_desc)

# 3. Add certification cards
target = '''                        Comprehensive AI and machine learning fundamentals certification with practical applications.
                    </p>
                </div>
            </div>
        </div>
    </section>'''

new_cards = '''                        Comprehensive AI and machine learning fundamentals certification with practical applications.
                    </p>
                </div>

                <!-- Achievement 5 -->
                <div class="achievement-card" data-aos="flip-left" data-aos-delay="400">
                    <div class="achievement-icon">
                        <i class="fas fa-calendar-check"></i>
                    </div>
                    <h3>TryHackMe Advent of Cyber 2025</h3>
                    <p class="achievement-subtitle">Cyber Security Challenges</p>
                    <p class="achievement-date">December 2025</p>
                    <p class="achievement-details">
                        Successfully completed 24 hands-on cybersecurity challenges covering security fundamentals, threat analysis, and practical defensive concepts through TryHackMe's Advent of Cyber program.
                    </p>
                </div>

                <!-- Achievement 6 -->
                <div class="achievement-card" data-aos="flip-left" data-aos-delay="500">
                    <div class="achievement-icon">
                        <i class="fab fa-google"></i>
                    </div>
                    <h3>Google Cybersecurity</h3>
                    <p class="achievement-subtitle">Foundations of Cybersecurity</p>
                    <p class="achievement-date">June 2026</p>
                    <p class="achievement-details">
                        Completed Google's Foundations of Cybersecurity course, covering core security concepts, risk management, security operations, and industry best practices for cybersecurity professionals.
                    </p>
                </div>
            </div>
        </div>
    </section>'''

if target in content:
    content = content.replace(target, new_cards)
else:
    print("Target for cards not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
