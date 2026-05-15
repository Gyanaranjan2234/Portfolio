/* ====================================
   CYBERSECURITY PORTFOLIO - JAVASCRIPT
   ==================================== */

// ====== NAVIGATION & SCROLLING ======

// Mobile Menu Toggle
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelectorAll('.nav-link');

navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when link is clicked
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// ====== SMOOTH SCROLLING & ACTIVE LINK ======

// Update active link based on scroll position
window.addEventListener('scroll', () => {
    let current = '';

    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });

    // Update scroll progress bar
    updateScrollProgress();
});

// Smooth scroll for navigation links
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        
        const targetId = link.getAttribute('href');
        if (targetId.startsWith('#')) {
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ====== SCROLL PROGRESS BAR ======

function updateScrollProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = docHeight ? (scrollTop / docHeight) * 100 : 0;
    
    const scrollProgress = document.getElementById('scrollProgress');
    scrollProgress.style.width = scrollPercent + '%';
}

// ====== TYPING ANIMATION ======

// Initialize Typed.js for typing animation
document.addEventListener('DOMContentLoaded', () => {
    // Only initialize if Typed library is loaded
    if (typeof Typed !== 'undefined') {
        new Typed('.typing-text', {
            strings: [
                'Cybersecurity Enthusiast',
                'VAPT Learner',
                'Web App Security Expert',
                'Bug Bounty Hunter',
                'Ethical Hacker'
            ],
            typeSpeed: 60,
            backSpeed: 40,
            backDelay: 1500,
            loop: true,
            showCursor: false
        });
    }

    // Initialize AOS (Animate On Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out-quart',
            once: true,
            offset: 100
        });
    }

    // Initialize scroll-to-top button
    initScrollToTop();

    // Initialize contact form
    initContactForm();
});

// ====== SCROLL TO TOP BUTTON ======

function initScrollToTop() {
    const scrollToTopBtn = document.getElementById('scrollToTop');

    // Show/hide scroll to top button
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollToTopBtn.classList.add('show');
        } else {
            scrollToTopBtn.classList.remove('show');
        }
    });

    // Smooth scroll to top
    scrollToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ====== CONTACT FORM HANDLING ======

function initContactForm() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Basic validation
            if (!name || !email || !message) {
                showNotification('Please fill all fields', 'error');
                return;
            }

            if (!isValidEmail(email)) {
                showNotification('Please enter a valid email', 'error');
                return;
            }

            // In a real application, you would send this to a backend
            // For now, we'll just show a success message and reset the form
            
            // Simulate sending email (you can replace this with actual backend call)
            console.log('Form Data:', {
                name,
                email,
                message
            });

            // Show success message
            showNotification('Message sent successfully! I will get back to you soon.', 'success');

            // Reset form
            contactForm.reset();

            // Optional: Actually send email via backend
            sendEmailViaBackend(name, email, message);
        });
    }
}

// Email validation function
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Show notification (toast-like message)
function showNotification(message, type) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#00ff41' : '#ff0055'};
        color: ${type === 'success' ? '#050505' : '#fff'};
        border-radius: 6px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        font-weight: 600;
        animation: slideIn 0.3s ease-out;
        max-width: 300px;
    `;

    // Add animation keyframes if not already present
    if (!document.querySelector('style[data-notification]')) {
        const style = document.createElement('style');
        style.setAttribute('data-notification', 'true');
        style.textContent = `
            @keyframes slideIn {
                from {
                    transform: translateX(400px);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            
            @keyframes slideOut {
                from {
                    transform: translateX(0);
                    opacity: 1;
                }
                to {
                    transform: translateX(400px);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(notification);

    // Remove notification after 4 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 4000);
}

// Send email via backend (placeholder function)
async function sendEmailViaBackend(name, email, message) {
    try {
        // This is a placeholder - in production, you would have a backend endpoint
        const response = await fetch('/api/send-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name,
                email,
                message,
                to: 'gyana.tcr20@gmail.com'
            })
        });

        // Note: This will fail in production without a backend
        // You can remove this or set up a backend service
    } catch (error) {
        console.log('Note: Backend email service not configured. In production, implement email service.');
    }
}

// ====== KEYBOARD NAVIGATION ======

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + K to focus on contact
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const contactSection = document.getElementById('contact');
        if (contactSection) {
            contactSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }

    // Escape to close mobile menu
    if (e.key === 'Escape') {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
    }

    // Ctrl/Cmd + . to scroll to top
    if ((e.ctrlKey || e.metaKey) && e.key === '.') {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
});

// ====== ACCESSIBILITY ENHANCEMENTS ======

// Ensure all interactive elements are keyboard accessible
function enhanceAccessibility() {
    // Add focus styles to all interactive elements
    const interactiveElements = document.querySelectorAll('a, button, input, textarea');
    
    interactiveElements.forEach(element => {
        element.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && element.tagName !== 'TEXTAREA') {
                element.click();
            }
        });
    });

    // Announce route changes for screen readers
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const title = entry.target.querySelector('h2')?.textContent;
                if (title) {
                    announceToScreenReader(`Navigated to ${title} section`);
                }
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
}

// Simple screen reader announcement
function announceToScreenReader(message) {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.className = 'sr-only';
    announcement.textContent = message;
    announcement.style.cssText = `
        position: absolute;
        left: -10000px;
        width: 1px;
        height: 1px;
        overflow: hidden;
    `;
    document.body.appendChild(announcement);

    setTimeout(() => {
        announcement.remove();
    }, 1000);
}

// ====== PERFORMANCE OPTIMIZATION ======

// Lazy load images (if any)
function lazyLoadImages() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        imageObserver.unobserve(img);
                    }
                }
            });
        });

        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(img => imageObserver.observe(img));
    }
}

// ====== INITIALIZATION ======

// Call accessibility enhancements on load
window.addEventListener('load', () => {
    enhanceAccessibility();
    lazyLoadImages();
});

// ====== UTILITY FUNCTIONS ======

// Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ====== STATS ANIMATION (Optional) ======

// Animate numbers when they come into view
function animateStats() {
    const statCards = document.querySelectorAll('.stat-card h3');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                const element = entry.target;
                element.classList.add('animated');

                // You could add number animation here if needed
                // Example: animate from 0 to the final number
            }
        });
    });

    statCards.forEach(card => observer.observe(card));
}

// Call stats animation when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', animateStats);
} else {
    animateStats();
}

// ====== TERMINAL EFFECT (Optional Enhancement) ======

// Add subtle terminal typing effect to terminal window
function initTerminalEffect() {
    const terminalLines = document.querySelectorAll('.terminal-line');
    
    terminalLines.forEach((line, index) => {
        // Add staggered animation delay
        line.style.animationDelay = `${index * 0.1}s`;
    });
}

// Call terminal effect on load
window.addEventListener('load', initTerminalEffect);

// ====== SERVICE WORKER (Optional - for offline support) ======

// Register service worker if available
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // Only register if you have a service worker file
        // navigator.serviceWorker.register('/sw.js');
    });
}

// ====== DEBUG MODE (Development only) ======

// Enable debug mode with console logging
const DEBUG = false;

function debug(...args) {
    if (DEBUG) {
        console.log('[Portfolio Debug]', ...args);
    }
}

debug('Portfolio script loaded successfully');

// ====== EXPORT FOR TESTING ======

// Make functions available for testing
window.portfolioDebug = {
    isValidEmail,
    showNotification,
    updateScrollProgress,
    animateStats
};
