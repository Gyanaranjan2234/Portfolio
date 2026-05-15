# Gyana Ranjan Behera - Cybersecurity Portfolio Website

A modern, professional cybersecurity portfolio website built with HTML5, CSS3, and Vanilla JavaScript. Features a dark hacker aesthetic with neon green accents, smooth animations, and fully responsive design.

## Features

✅ **Modern Design**
- Dark cybersecurity theme (#050505 background)
- Neon green (#00ff41) accent color
- Professional glassmorphism effects
- Subtle matrix grid animation in hero section

✅ **Interactive Elements**
- Smooth scroll animations (AOS.js)
- Typing animation for role titles (Typed.js)
- Active navigation highlighting
- Scroll progress bar
- Scroll-to-top button
- Terminal-style window display

✅ **Fully Responsive**
- Mobile-first design
- Hamburger menu for mobile
- Optimized for all screen sizes (desktop, tablet, mobile)
- Touch-friendly interface

✅ **Accessibility**
- Semantic HTML5
- ARIA labels
- Keyboard navigation
- Screen reader support
- High contrast ratios
- Keyboard shortcuts (Ctrl+K for contact, Ctrl+. for top)

✅ **Performance**
- Lightweight (no heavy dependencies)
- CDN-based external libraries
- Optimized CSS and JavaScript
- CSS variables for easy customization
- Lazy loading ready

## Tech Stack

- **HTML5** - Semantic structure
- **CSS3** - Modern styling with Flexbox & Grid
- **Vanilla JavaScript** - No jQuery or frameworks
- **AOS.js** - Scroll animations
- **Typed.js** - Typing effect
- **Font Awesome** - Icons
- **Google Fonts** - Typography

## Folder Structure

```
Portfolio/
├── index.html              # Main HTML file
├── style.css               # Stylesheet
├── script.js               # JavaScript functionality
├── assets/
│   ├── images/            # Placeholder for images
│   ├── icons/             # Placeholder for icons
│   └── resume.pdf         # Your resume (add your file here)
└── README.md              # This file
```

## Setup Instructions

### 1. Clone or Download
Download this project to your desired location.

### 2. Add Your Resume
- Add your resume PDF to `assets/resume.pdf`
- The download button in the hero section will link to it

### 3. Update GitHub URL
In `index.html`, find the GitHub link in the contact section and update it:
```html
<a href="https://your-github-profile-url" target="_blank" aria-label="GitHub">
```

### 4. Customize Content (Optional)

#### Change Accent Color
In `style.css`, modify the CSS variables:
```css
:root {
    --accent: #00ff41;      /* Change to #ff0055 for crimson or any other color */
    --accent-alt: #ff0055;  /* Secondary accent */
}
```

#### Update Profile Information
Edit the following in `index.html`:
- Name, title, and bio in hero section
- About section content
- Skills categories
- Projects
- Achievements
- Contact information

#### Modify Typing Animation
In `script.js`, update the strings array:
```javascript
new Typed('.typing-text', {
    strings: [
        'Your custom title 1',
        'Your custom title 2',
        'Your custom title 3'
    ],
    // ... other options
});
```

## Running Locally

1. **Using Live Server (VS Code)**
   - Install the "Live Server" extension
   - Right-click on `index.html`
   - Select "Open with Live Server"

2. **Using Python**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Python 2
   python -m SimpleHTTPServer 8000
   ```
   Then open `http://localhost:8000` in your browser

3. **Using Node.js (http-server)**
   ```bash
   npm install -g http-server
   http-server
   ```

4. **Direct File Opening**
   Simply open `index.html` in your web browser (limited functionality with some features)

## Features Explained

### Navbar
- Fixed transparent navigation with glassmorphism
- Active link highlighting based on scroll position
- Hamburger menu for mobile devices
- Keyboard navigation support

### Hero Section
- Large name heading with gradient
- Typing animation cycling through role titles
- Call-to-action buttons
- Stats cards showing achievements
- Terminal window with animated text
- Subtle scanline grid effect

### About Section
- Professional bio
- Education highlights
- Learning badges for current skills
- Hover animations on cards

### Skills Section
- Organized by categories (Programming, Tools, Concepts)
- Icon-based display
- Hover effects with elevation
- Responsive grid layout

### Experience Section
- Timeline-style layout
- Left/right alternating cards
- Responsibility lists with checkmarks
- Hover animations

### Projects Section
- Modern project cards
- Project descriptions and tags
- Links to demo and repository
- "Coming Soon" placeholder
- Glow effects on hover

### Achievements Section
- Achievement cards with icons
- Flip animation on scroll
- TryHackMe stats display
- Certifications highlight

### Contact Section
- Contact form with validation
- Email validation
- Form submission handling (requires backend)
- Contact information cards
- Social media links

## Customization Guide

### Colors
Edit CSS variables in `style.css`:
```css
:root {
    --bg: #050505;              /* Background */
    --bg-secondary: #0a0a0a;    /* Secondary bg */
    --accent: #00ff41;          /* Primary accent */
    --accent-alt: #ff0055;      /* Accent alt */
    --text: #e8e8e8;            /* Main text */
    --text-muted: #b0b0b0;      /* Muted text */
    --card: #1a1a1a;            /* Card bg */
    --border: #2a2a2a;          /* Border color */
}
```

### Fonts
The site uses:
- **Poppins** - Main font (Google Fonts)
- **JetBrains Mono** - Code/terminal font (Google Fonts)

Change in `index.html` head and `style.css`.

### Animations
- Scroll animations: Configured in `script.js` with AOS settings
- Typing speed: Modify `typeSpeed` and `backSpeed` in Typed.js config
- Transition duration: Change `--transition` variable in CSS

## Contact Form Setup (Optional)

The contact form is functional client-side with validation. To actually send emails, you have options:

### Option 1: Using Formspree (Free)
1. Go to https://formspree.io/
2. Create a new form endpoint
3. Update the form `action` attribute in `index.html`

### Option 2: Using EmailJS (Free Tier)
1. Sign up at https://www.emailjs.com/
2. Include EmailJS library in `index.html`
3. Initialize in `script.js`

### Option 3: Backend Service
Implement your own backend API endpoint and uncomment the fetch call in `sendEmailViaBackend()` in `script.js`.

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Tips

1. **Optimize Images**: Compress images before adding to `assets/images/`
2. **Minify Code**: Use tools like Terser for JS and CSSNano for CSS in production
3. **Enable GZIP**: Compress assets on server
4. **Use CDN**: Host static assets on CDN for faster delivery
5. **Lazy Loading**: Images use data-src for lazy loading

## Accessibility Notes

- All interactive elements are keyboard accessible
- ARIA labels provided for icon buttons
- High contrast ratios for readability
- Semantic HTML structure
- Screen reader support
- Keyboard shortcuts:
  - `Ctrl/Cmd + K` → Jump to contact section
  - `Ctrl/Cmd + .` → Jump to top
  - `Escape` → Close mobile menu
  - `Tab` → Navigate through elements

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Navigate through elements |
| `Enter` | Activate buttons/links |
| `Escape` | Close mobile menu |
| `Ctrl/Cmd + K` | Jump to contact section |
| `Ctrl/Cmd + .` | Jump to top of page |

## Deployment

### GitHub Pages
1. Create a GitHub repository
2. Push your code
3. Go to Settings → Pages
4. Select main branch as source
5. Your site will be live at `yourusername.github.io/repo-name`

### Netlify
1. Connect your GitHub repository
2. Set build command: (leave empty for static site)
3. Set publish directory: `/`
4. Deploy!

### Vercel
1. Import your GitHub repository
2. Configure project settings
3. Deploy!

### Traditional Hosting
1. Upload files via FTP/SFTP
2. Ensure `index.html` is in the root directory
3. Access your domain

## Troubleshooting

### Typing animation not working
- Ensure Typed.js CDN link is correct
- Check browser console for errors
- Verify `.typing-text` element exists

### Animations not triggering
- Check AOS.js CDN link
- Ensure AOS is initialized in `script.js`
- Check `data-aos` attributes in HTML

### Mobile menu not closing
- Verify hamburger toggle JavaScript is loaded
- Check if navToggle element exists
- Clear browser cache

### Scroll not smooth
- Check if `scroll-behavior: smooth` is supported
- Use JavaScript fallback (already implemented)

### Form not submitting
- Verify form validation is working
- Check browser console for errors
- Implement backend email service

## Best Practices

1. **Keep Content Updated**: Regularly update projects and achievements
2. **Proofread Everything**: Check for typos and grammar
3. **Use High-Quality Content**: Clear descriptions and accurate info
4. **Optimize Images**: Use appropriate formats and sizes
5. **Test Responsiveness**: Test on multiple devices
6. **Monitor Analytics**: Track visitor engagement
7. **Update Resume**: Keep `resume.pdf` current
8. **Maintain Links**: Ensure all external links are valid

## Credits

- **AOS.js** - Michał Sajnóg (https://github.com/michalsnik/aos)
- **Typed.js** - Matteo Mezzanotte (https://github.com/matteobruni/tsparticles)
- **Font Awesome** - Fonticons, Inc (https://fontawesome.com)
- **Google Fonts** - Google (https://fonts.google.com)

## License

This portfolio template is free to use and modify for personal projects. Feel free to customize it as needed.

## Support & Questions

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check browser console for errors
4. Verify all external CDN links are working

---

**Built with ❤️ for cybersecurity professionals**

Last Updated: May 2026
