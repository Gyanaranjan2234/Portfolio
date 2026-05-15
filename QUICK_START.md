# QUICK START GUIDE

Get your portfolio running in 5 minutes! ⚡

## 1. View Locally (2 minutes)

### Option A: Python (Easiest)
```bash
# Open terminal/PowerShell in Portfolio folder
# Windows: Shift + Right-click → Open PowerShell here

# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```
Then open: `http://localhost:8000`

### Option B: VS Code Live Server
1. Install "Live Server" extension
2. Right-click `index.html`
3. Select "Open with Live Server"

### Option C: Node.js
```bash
npm install -g http-server
http-server
```

## 2. Customize (3 minutes)

### Update Your Info
Edit `index.html`:
- Replace all instances of "Gyana Ranjan Behera" with your name
- Update email: `gyana.tcr20@gmail.com`
- Update GitHub link in contact section
- Add your resume to `assets/resume.pdf`

### Change Colors (Optional)
Edit top of `style.css`:
```css
:root {
    --accent: #00ff41;      /* Green - change to #ff0055 for red */
}
```

## 3. Deploy (Choose One)

### Option 1: GitHub Pages (Easiest)
```bash
# Install Git: https://git-scm.com/

git clone https://github.com/YOUR_USERNAME/your-portfolio-repo.git
cd your-portfolio-repo

# Copy all files here, then:
git add .
git commit -m "Initial commit"
git push origin main
```

Go to: https://github.com/YOUR_USERNAME/your-portfolio-repo/settings/pages

### Option 2: Netlify (No Code)
1. Go to https://netlify.com
2. Drag and drop your Portfolio folder
3. Done! You get a live URL

### Option 3: Vercel (No Code)
1. Go to https://vercel.com
2. Import your GitHub repo
3. Done! You get a live URL

## 4. Done! 🎉

Your portfolio is now live online!

---

## Important Files

```
Portfolio/
├── index.html          ← Main file - customize this
├── style.css           ← Styling - modify colors here
├── script.js           ← Interactive features
├── assets/
│   └── resume.pdf      ← Add YOUR resume here!
├── README.md           ← Full documentation
├── DEPLOYMENT_GUIDE.md ← Detailed deployment steps
└── EMAIL_SETUP_GUIDE.md← Email configuration
```

## Essential Customizations

1. **Add Your Resume**
   - Replace `assets/resume.pdf` with YOUR resume
   - The "Download Resume" button will link to it

2. **Update Name & Email**
   - `index.html`: Search and replace your info
   - `script.js`: Update email address

3. **Update GitHub & LinkedIn**
   - `index.html`: Find social links in contact section
   - Update URLs to your profiles

4. **Add GitHub Username**
   - If you have GitHub: update the link
   - If not: remove the GitHub link

## Testing Checklist

- [ ] Site loads without errors
- [ ] All sections scroll smoothly
- [ ] Hamburger menu works on mobile
- [ ] Links work
- [ ] Resume downloads
- [ ] Looks good on phone

## Common Customizations

### Change Name
Find in `index.html`:
```html
<h1 class="hero-title">Gyana Ranjan Behera</h1>
```
Replace with your name

### Change Title/Role
Find in `index.html`:
```html
<span class="typing-text">Cybersecurity Enthusiast</span>
```
Or in `script.js`:
```javascript
strings: [
    'Your Role 1',
    'Your Role 2',
    'Your Role 3'
],
```

### Update About Section
Find in `index.html` - About section
Replace the text with your bio

### Update Skills
Edit the Skills section cards in `index.html`
Add your tools and technologies

### Add Your Projects
Edit Projects section in `index.html`
Replace with your actual projects

## Need Help?

1. **Check README.md** - Full documentation
2. **Check DEPLOYMENT_GUIDE.md** - Deployment instructions
3. **Check EMAIL_SETUP_GUIDE.md** - Email form setup
4. **Browser Console** - Ctrl+Shift+I → Console tab
5. **Search code comments** - Look for "TODO" or "CUSTOMIZE"

## Next Steps

1. ✅ Get site running locally
2. ✅ Customize with your info
3. ✅ Test on phone (important!)
4. ✅ Deploy online
5. ✅ Share with others!

## One More Thing...

**Add Your Resume!**
- Download your resume as PDF
- Rename to `resume.pdf`
- Place in `assets/resume.pdf`
- The download button will work now

---

## Pro Tips

1. **Mobile Testing**: 
   - Open DevTools: F12
   - Click mobile icon
   - Test on different screen sizes

2. **Sharing Your Site**:
   - Add to LinkedIn profile
   - Share on Twitter/X
   - Email to recruiters
   - Add to applications

3. **Keep It Updated**:
   - Update resume annually
   - Add new projects when done
   - Fix any broken links
   - Keep content fresh

4. **Performance**:
   - Compress images before adding
   - Use Google PageSpeed Insights to check
   - Optimize before deploying

---

## Commands Reference

```bash
# Local server (Python)
python -m http.server 8000

# Local server (Node)
http-server

# Git commands
git clone <url>           # Download repo
git add .                 # Add all files
git commit -m "message"   # Commit changes
git push origin main      # Upload to GitHub

# Check if Python installed
python --version

# Check if Git installed
git --version
```

---

## Quick Deployment Options

| Service | Time | Cost | URL |
|---------|------|------|-----|
| GitHub Pages | 5 min | Free | yourname.github.io |
| Netlify | 2 min | Free | yourname.netlify.app |
| Vercel | 2 min | Free | yourname.vercel.app |
| Paid Host | 10 min | $2-10/mo | your-domain.com |

---

## You've Got This! 🚀

Your portfolio website is production-ready. Just personalize it and share!

Questions? Check the full documentation in:
- `README.md`
- `DEPLOYMENT_GUIDE.md`
- `EMAIL_SETUP_GUIDE.md`

---

**Happy coding and good luck with your cybersecurity journey!** 🔐
