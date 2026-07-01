import re

# ================= 1. INDEX.HTML =================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_skills_html = '''    <!-- ====== SKILLS SECTION ====== -->
    <section id="skills" class="skills">
        <div class="container">
            <h2 class="section-title" data-aos="fade-up">Skills & Expertise</h2>
            <p class="section-subtitle" data-aos="fade-up" data-aos-delay="100">A blend of technical skills, security tools, and cybersecurity knowledge that power my work.</p>
            
            <div class="carousel-wrapper skills-carousel-wrapper" data-aos="fade-up" data-aos-delay="200">
                <button class="carousel-btn prev-btn" id="prevSkill" aria-label="Previous Skill"><i class="fas fa-chevron-left"></i></button>
                <div class="carousel-container">
                    <div class="carousel-track" id="skillCarousel">
                        
                        <!-- Card 1: Programming -->
                        <div class="skill-card">
                            <div class="skill-card-icon">
                                <i class="fas fa-code"></i>
                            </div>
                            <h3>Programming</h3>
                            <p class="skill-desc">Languages and scripting skills used for automation, development, and security research.</p>
                            <div class="skill-divider"></div>
                            <div class="skill-chip-grid col-2">
                                <div class="skill-chip"><i class="fab fa-python"></i><span>Python</span></div>
                                <div class="skill-chip"><i class="fas fa-c"></i><span>C</span></div>
                                <div class="skill-chip"><i class="fab fa-js"></i><span>JavaScript</span></div>
                                <div class="skill-chip"><i class="fas fa-terminal"></i><span>Bash</span></div>
                                <div class="skill-chip"><i class="fab fa-linux"></i><span>Linux</span></div>
                                <div class="skill-chip"><i class="fab fa-git-alt"></i><span>Git</span></div>
                            </div>
                        </div>

                        <!-- Card 2: Security Tools -->
                        <div class="skill-card">
                            <div class="skill-card-icon">
                                <i class="fas fa-tools"></i>
                            </div>
                            <h3>Security Tools</h3>
                            <p class="skill-desc">Industry-standard tools used for penetration testing, monitoring, and security analysis.</p>
                            <div class="skill-divider"></div>
                            <div class="skill-chip-grid col-2">
                                <div class="skill-chip"><i class="fas fa-bolt"></i><span>Burp Suite</span></div>
                                <div class="skill-chip"><i class="fas fa-eye"></i><span>Nmap</span></div>
                                <div class="skill-chip"><i class="fas fa-shield-alt"></i><span>Metasploit</span></div>
                                <div class="skill-chip"><i class="fas fa-database"></i><span>SQLMap</span></div>
                                <div class="skill-chip"><i class="fas fa-wave-square"></i><span>Wireshark</span></div>
                                <div class="skill-chip"><i class="fas fa-key"></i><span>Hydra</span></div>
                                <div class="skill-chip"><i class="fas fa-search"></i><span>Nessus</span></div>
                                <div class="skill-chip"><i class="fas fa-paw"></i><span>Wazuh</span></div>
                                <div class="skill-chip"><i class="fas fa-chart-bar"></i><span>Splunk</span></div>
                                <div class="skill-chip"><i class="fas fa-piggy-bank"></i><span>Snort</span></div>
                            </div>
                        </div>

                        <!-- Card 3: Concepts -->
                        <div class="skill-card">
                            <div class="skill-card-icon">
                                <i class="fas fa-brain"></i>
                            </div>
                            <h3>Concepts</h3>
                            <p class="skill-desc">Core cybersecurity methodologies and defensive security practices.</p>
                            <div class="skill-divider"></div>
                            <div class="skill-chip-grid col-3">
                                <div class="skill-chip"><i class="fas fa-globe"></i><span>Web App Security</span></div>
                                <div class="skill-chip"><i class="fas fa-search-dollar"></i><span>Vulnerability Assessment</span></div>
                                <div class="skill-chip"><i class="fas fa-bolt"></i><span>Penetration Testing</span></div>
                                <div class="skill-chip"><i class="fas fa-shield-virus"></i><span>OWASP Top 10</span></div>
                                <div class="skill-chip"><i class="fas fa-chart-line"></i><span>SIEM</span></div>
                                <div class="skill-chip"><i class="fas fa-network-wired"></i><span>MITRE ATT&CK</span></div>
                                <div class="skill-chip"><i class="fas fa-search"></i><span>IOC Analysis</span></div>
                                <div class="skill-chip"><i class="fas fa-bug"></i><span>CVE Analysis</span></div>
                                <div class="skill-chip"><i class="fas fa-bullseye"></i><span>Threat Detection</span></div>
                                <div class="skill-chip" style="grid-column: 1 / -1; margin: 0 auto; width: 60%; flex-direction: row; gap: 0.5rem;"><i class="fas fa-siren-on" style="margin-right:0.5rem"></i><span>Incident Response</span></div>
                            </div>
                        </div>

                    </div>
                </div>
                <button class="carousel-btn next-btn" id="nextSkill" aria-label="Next Skill"><i class="fas fa-chevron-right"></i></button>
            </div>
            <div class="carousel-dots" id="skillDots"></div>
        </div>
    </section>'''

# Replace old skills section
html = re.sub(r'<!-- ====== SKILLS SECTION ====== -->.*?</section>', new_skills_html, html, flags=re.DOTALL)
html = html.replace('href="style.css?v=3"', 'href="style.css?v=4"')
html = html.replace('src="script.js?v=3"', 'src="script.js?v=4"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# ================= 2. STYLE.CSS =================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* ====== SKILLS REDESIGN ====== */
.section-subtitle {
    text-align: center;
    color: var(--text-muted);
    font-size: 1.1rem;
    margin-bottom: 3rem;
    margin-top: -1.5rem;
}

.skills-carousel-wrapper {
    margin-top: 1rem;
}

.skill-card {
    flex: 0 0 100%; width: 100%; max-width: 100%;
    background: linear-gradient(145deg, rgba(13, 13, 13, 0.84), rgba(5, 5, 5, 0.92));
    border: 1px solid rgba(255, 255, 255, 0.08); padding: 2.5rem 1.8rem; border-radius: 12px;
    transition: transform 0.45s ease, border-color 0.45s ease, box-shadow 0.45s ease, background 0.45s ease;
    display: flex; flex-direction: column; align-items: center; text-align: center;
    backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05), 0 16px 42px rgba(0, 0, 0, 0.22);
}

@media (min-width: 768px) {
    .skill-card { flex: 0 0 calc(50% - 1rem); width: calc(50% - 1rem); max-width: calc(50% - 1rem); }
}

@media (min-width: 1024px) {
    .skill-card { flex: 0 0 calc(33.3333% - 1.34rem); width: calc(33.3333% - 1.34rem); max-width: calc(33.3333% - 1.34rem); }
}

.skill-card:hover { border-color: rgba(0, 255, 136, 0.42); transform: translateY(-6px); box-shadow: 0 18px 48px rgba(0, 0, 0, 0.34), 0 0 22px rgba(0, 255, 136, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.07); }

.skill-card-icon {
    width: 70px; height: 70px;
    border-radius: 50%;
    border: 1px solid rgba(0, 255, 136, 0.4);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.8rem; color: var(--accent);
    margin-bottom: 1.2rem;
    box-shadow: 0 0 15px rgba(0, 255, 136, 0.15), inset 0 0 10px rgba(0, 255, 136, 0.1);
    transition: var(--transition);
}
.skill-card:hover .skill-card-icon { box-shadow: 0 0 25px rgba(0, 255, 136, 0.3), inset 0 0 15px rgba(0, 255, 136, 0.2); transform: scale(1.05); }

.skill-card h3 { font-size: 1.4rem; color: var(--accent); font-weight: 700; margin-bottom: 0.8rem; letter-spacing: 0.5px; }
.skill-desc { color: var(--text-muted); font-size: 0.9rem; line-height: 1.5; margin-bottom: 1.5rem; flex-grow: 1; }

.skill-divider {
    width: 60%; height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    margin-bottom: 1.8rem;
    opacity: 0.5;
    position: relative;
    flex-shrink: 0;
}
.skill-divider::after {
    content: ''; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 8px; height: 8px; border-radius: 50%; background: var(--accent);
    box-shadow: 0 0 10px var(--accent);
}

.skill-chip-grid {
    display: grid; gap: 0.8rem; width: 100%;
}
.skill-chip-grid.col-2 { grid-template-columns: 1fr 1fr; }
.skill-chip-grid.col-3 { grid-template-columns: repeat(3, 1fr); }
.skill-chip {
    background: rgba(0, 255, 136, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 6px; padding: 0.7rem 0.5rem;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.5rem;
    transition: var(--transition);
    cursor: default;
}
.skill-chip-grid.col-2 .skill-chip { flex-direction: row; justify-content: flex-start; padding: 0.8rem 1rem; gap: 1rem; }
.skill-chip:hover { border-color: rgba(0, 255, 136, 0.4); background: rgba(0, 255, 136, 0.08); transform: translateY(-2px); box-shadow: 0 0 15px rgba(0, 255, 136, 0.15); }
.skill-chip i { font-size: 1.2rem; color: var(--accent); transition: var(--transition); }
.skill-chip:hover i { transform: scale(1.1); filter: drop-shadow(0 0 5px var(--accent)); }
.skill-chip span { font-size: 0.75rem; font-weight: 500; color: var(--text-muted); transition: color 0.3s; text-align: center; }
.skill-chip-grid.col-2 .skill-chip span { font-size: 0.85rem; }
.skill-chip:hover span { color: var(--text); }
'''

css = re.sub(r'/\* ====== SKILLS SECTION ====== \*/.*?/\* ====== EXPERIENCE SECTION ====== \*/', '/* ====== EXPERIENCE SECTION ====== */', css, flags=re.DOTALL)

css = css.replace('/* ====== PROJECTS SECTION ====== */', new_css + '\n/* ====== PROJECTS SECTION ====== */')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# ================= 3. SCRIPT.JS =================
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_js = '''// ====== SKILL CAROUSEL ======
function initSkillCarousel() {
    const track = document.getElementById('skillCarousel');
    const prevBtn = document.getElementById('prevSkill');
    const nextBtn = document.getElementById('nextSkill');
    const dotsContainer = document.getElementById('skillDots');
    
    if (!track || !prevBtn || !nextBtn || !dotsContainer) return;
    
    const slides = Array.from(track.children);
    if (slides.length === 0) return;
    
    let currentIndex = 0;
    
    function getSlidesPerView() {
        if (window.innerWidth >= 1024) return 3;
        if (window.innerWidth >= 768) return 2;
        return 1;
    }
    
    let slidesPerView = getSlidesPerView();
    let maxIndex = Math.max(0, slides.length - slidesPerView);
    let dots = [];
    
    function createDots() {
        dotsContainer.innerHTML = '';
        if (maxIndex <= 0) return; // Hide dots if no scrolling needed
        for (let i = 0; i <= maxIndex; i++) {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (i === currentIndex) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(i));
            dotsContainer.appendChild(dot);
        }
        dots = Array.from(dotsContainer.children);
    }
    
    function updateCarousel() {
        slidesPerView = getSlidesPerView();
        const newMaxIndex = Math.max(0, slides.length - slidesPerView);
        
        if (newMaxIndex !== maxIndex) {
            maxIndex = newMaxIndex;
            if (currentIndex > maxIndex) currentIndex = maxIndex;
            createDots();
        }
        
        const slide = slides[currentIndex];
        const offset = slide.offsetLeft;
        track.style.transform = 	ranslateX(-px);
        
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
        
        if (maxIndex <= 0) {
            prevBtn.style.display = 'none';
            nextBtn.style.display = 'none';
        } else {
            prevBtn.style.display = 'flex';
            nextBtn.style.display = 'flex';
            prevBtn.disabled = currentIndex === 0;
            nextBtn.disabled = currentIndex === maxIndex;
        }
    }
    
    function goToSlide(index) {
        if (index < 0) index = 0;
        if (index > maxIndex) index = maxIndex;
        currentIndex = index;
        updateCarousel();
    }
    
    prevBtn.addEventListener('click', () => goToSlide(currentIndex - 1));
    nextBtn.addEventListener('click', () => goToSlide(currentIndex + 1));
    
    let startX = 0;
    let currentX = 0;
    let isDragging = false;
    
    track.addEventListener('touchstart', (e) => {
        if (maxIndex <= 0) return;
        startX = e.touches[0].clientX;
        isDragging = true;
        track.style.transition = 'none';
    }, { passive: true });
    
    track.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        currentX = e.touches[0].clientX;
        const diff = currentX - startX;
        const slide = slides[currentIndex];
        track.style.transform = 	ranslateX(calc(-px + px));
    }, { passive: true });
    
    track.addEventListener('touchend', (e) => {
        if (!isDragging) return;
        isDragging = false;
        track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
        const diff = currentX - startX;
        if (Math.abs(diff) > 50) {
            if (diff > 0) goToSlide(currentIndex - 1);
            else goToSlide(currentIndex + 1);
        } else {
            updateCarousel();
        }
    });
    
    window.addEventListener('resize', debounce(() => {
        track.style.transition = 'none';
        updateCarousel();
        setTimeout(() => {
            track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
        }, 50);
    }, 250));
    
    createDots();
    setTimeout(updateCarousel, 50);
}

// ====== PROJECT CAROUSEL ======'''

js = js.replace('// ====== PROJECT CAROUSEL ======', new_js)
js = js.replace('initProjectCarousel();', 'initProjectCarousel();\n    initSkillCarousel();')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Redesign complete.")
