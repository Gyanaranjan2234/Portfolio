# DEPLOYMENT GUIDE

Complete guide to deploy your portfolio website to the internet.

## Table of Contents
1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [GitHub Pages (Free & Recommended)](#github-pages-free--recommended)
3. [Netlify (Free & Easy)](#netlify-free--easy)
4. [Vercel (Free & Fast)](#vercel-free--fast)
5. [Traditional Hosting](#traditional-hosting)
6. [Domain Setup](#domain-setup)
7. [SSL Certificate](#ssl-certificate)
8. [Performance Optimization](#performance-optimization)

---

## Pre-Deployment Checklist

Before deploying, ensure:

- [ ] All links are working (including GitHub, LinkedIn)
- [ ] Resume PDF is uploaded to `assets/resume.pdf`
- [ ] All typos are fixed
- [ ] Images are optimized and compressed
- [ ] Mobile responsiveness tested
- [ ] All sections have content
- [ ] Social links are correct
- [ ] Email contact form is configured (optional)
- [ ] Favicon is set (already included)
- [ ] Meta tags are correct
- [ ] No console errors in browser DevTools

---

## GitHub Pages (Free & Recommended)

**Best for**: Static sites, easy version control, free hosting

### Step 1: Create GitHub Account
1. Go to https://github.com/
2. Sign up with your email
3. Verify your email

### Step 2: Create Repository
1. Click "+" → "New repository"
2. Name: `gyana-portfolio` (or any name)
3. Description: `My Cybersecurity Portfolio`
4. Select "Public"
5. Check "Add a README file"
6. Click "Create repository"

### Step 3: Upload Files
#### Option A: Using Git (Recommended)

1. **Install Git** from https://git-scm.com/

2. **Clone the repository**:
```bash
cd Desktop
git clone https://github.com/YOUR_USERNAME/gyana-portfolio.git
cd gyana-portfolio
```

3. **Copy your portfolio files** into this folder

4. **Add files to Git**:
```bash
git add .
```

5. **Commit changes**:
```bash
git commit -m "Initial portfolio commit"
```

6. **Push to GitHub**:
```bash
git push origin main
```

#### Option B: Using GitHub Web Interface

1. In your repository, click "Add file" → "Upload files"
2. Drag and drop your `index.html`, `style.css`, `script.js`
3. Upload `assets` folder
4. Click "Commit changes"

### Step 4: Enable GitHub Pages
1. Go to repository → Settings
2. Scroll to "Pages" section
3. Under "Source", select "Deploy from a branch"
4. Select branch: `main`
5. Select folder: `/ (root)`
6. Click "Save"
7. Wait 1-2 minutes for deployment

### Step 5: Access Your Site
Your site will be live at:
```
https://YOUR_USERNAME.github.io/gyana-portfolio
```

Or with custom domain (see [Domain Setup](#domain-setup) section)

### Pro Tips:
- Enable branch protection
- Set up GitHub Actions for automated checks
- Use GitHub Issues to track improvements
- Star your repo to bookmark it

---

## Netlify (Free & Easy)

**Best for**: Easiest deployment, great for beginners

### Step 1: Create Netlify Account
1. Go to https://netlify.com/
2. Sign up with GitHub account
3. Authorize Netlify

### Step 2: Deploy Your Site
#### Option A: Connect Git Repository (Recommended)

1. Click "New site from Git"
2. Choose GitHub
3. Select your portfolio repository
4. Click "Deploy site"
5. Wait for automatic deployment

#### Option B: Drag and Drop

1. Click "Deploys"
2. Drag your entire project folder into the drop zone
3. Netlify will deploy automatically

### Step 3: Configure Domain (Optional)
1. Go to "Site settings" → "Domain management"
2. Click "Add domain"
3. Enter your domain name

### Your Site
```
https://your-site-name.netlify.app
```

### Pro Tips:
- Netlify provides automatic HTTPS
- Free tier includes unlimited bandwidth
- Deploy by pushing to GitHub automatically

---

## Vercel (Free & Fast)

**Best for**: Super fast CDN, optimal performance

### Step 1: Create Vercel Account
1. Go to https://vercel.com/
2. Sign up with GitHub
3. Authorize Vercel

### Step 2: Deploy
1. Click "Import Project"
2. Select "Import Git Repository"
3. Paste your GitHub repo URL
4. Click "Import"
5. Leave settings as default
6. Click "Deploy"

### Step 3: Access Site
```
https://your-portfolio.vercel.app
```

### Pro Tips:
- Vercel has the fastest global CDN
- Automatic deployments from Git
- Built-in analytics and performance monitoring
- Free tier is very generous

---

## Traditional Hosting

**Best for**: Maximum control, custom domain

### Popular Hosting Providers:
- **Bluehost** - $2.95-$9.95/month
- **Hostinger** - $1.99-$6.99/month
- **SiteGround** - $2.99-$7.99/month
- **Namecheap** - Budget-friendly
- **AWS S3 + CloudFront** - Pay-as-you-go

### Steps (General):
1. Sign up with hosting provider
2. Upload files via FTP/SFTP:
   - Use FileZilla or WinSCP
   - Connect with FTP credentials
   - Upload to `public_html` folder
3. Point domain to hosting
4. Enable SSL certificate

### Using FTP:
```
Host: ftp.yourhost.com
Username: Your FTP username
Password: Your FTP password
Remote path: /public_html
```

---

## Domain Setup

### Register Domain
1. Go to domain registrar:
   - **Namecheap**: https://www.namecheap.com/
   - **GoDaddy**: https://www.godaddy.com/
   - **Google Domains**: https://domains.google/
   - **Domain.com**: https://www.domain.com/

2. Search for available domain (e.g., `gyanaportfolio.com`)
3. Purchase domain
4. Complete registration

### Connect Domain to GitHub Pages

1. **Update DNS Settings**:
   - Go to your domain registrar dashboard
   - Find DNS settings
   - Add these A records pointing to GitHub:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```

2. **Configure in GitHub**:
   - Go to repository → Settings → Pages
   - Under "Custom domain", enter your domain
   - Check "Enforce HTTPS"
   - Save

3. **Wait for DNS propagation** (up to 48 hours)

### Connect Domain to Netlify

1. In Netlify dashboard: Site settings → Domain management
2. Click "Add domain"
3. Enter your custom domain
4. Netlify will provide nameserver addresses
5. Go to your domain registrar
6. Update nameservers to Netlify's:
   - `dns1.p06.nsone.net`
   - `dns2.p06.nsone.net`
   - `dns3.p06.nsone.net`
   - `dns4.p06.nsone.net`

### Connect Domain to Vercel

1. In Vercel dashboard: Settings → Domains
2. Add your domain
3. Update nameservers to Vercel's (provided in dashboard)
4. Or add CNAME record pointing to vercel.app

---

## SSL Certificate

### For GitHub Pages & Netlify & Vercel
- ✅ **Automatically included** with HTTPS
- No additional setup needed
- Always enabled

### For Traditional Hosting
1. Most hosts provide free Let's Encrypt SSL
2. Enable in hosting control panel
3. Or use Cloudflare (free HTTPS):
   - Go to https://www.cloudflare.com/
   - Add your site
   - Update nameservers
   - Enable SSL/TLS

---

## Performance Optimization

### Before Deployment:

1. **Compress Images**:
   - Use TinyPNG: https://tinypng.com/
   - Use ImageOptim (Mac) or OptiPNG (Windows)

2. **Minify Code** (Optional):
   - CSS: https://cssnano.co/
   - JavaScript: https://www.terser.org/
   - Use build tools like PostCSS or Webpack

3. **Optimize Assets**:
   - Remove unused CSS/JS
   - Use CDN for external libraries
   - Lazy load images

### After Deployment:

1. **Test Performance**:
   - Google PageSpeed Insights: https://pagespeed.web.dev/
   - GTmetrix: https://gtmetrix.com/
   - WebPageTest: https://www.webpagetest.org/

2. **Monitor**:
   - Set up Google Analytics
   - Use Sentry for error tracking
   - Monitor uptime

---

## Continuous Deployment Setup

### GitHub Actions (Automatic Tests)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check HTML validity
        run: |
          # Add your validation commands here
          echo "Deployment ready!"
```

---

## Post-Deployment Checklist

- [ ] Site loads correctly on all devices
- [ ] All links work
- [ ] Images load properly
- [ ] CSS and JavaScript work
- [ ] Form submissions work (if applicable)
- [ ] Mobile menu functions
- [ ] Scroll animations trigger
- [ ] Performance is acceptable
- [ ] No console errors
- [ ] Favicon displays
- [ ] Open Graph tags work

---

## Troubleshooting

### Site not appearing?
- Wait 5-10 minutes for DNS/deployment
- Clear browser cache (Ctrl+Shift+Delete)
- Check GitHub Pages settings
- Verify files are in repository

### CSS/JavaScript not loading?
- Check file paths (use relative paths)
- Verify files were uploaded
- Check browser console for errors
- Ensure HTTPS if referenced from HTTPS page

### Domain not working?
- DNS propagation takes up to 48 hours
- Verify DNS records are correct
- Check domain registrar settings
- Use DNS checker: https://mxtoolbox.com/

### Performance issues?
- Optimize images
- Minify CSS/JavaScript
- Use CDN for external resources
- Enable caching headers
- Review PageSpeed Insights report

### Form not working?
- Verify form service is configured
- Check browser console for errors
- Test with valid email
- Verify email service credentials

---

## Maintenance

### Regular Updates:
- Update resume PDF monthly
- Add new projects as completed
- Update skills and achievements
- Review and fix broken links
- Monitor analytics

### Security:
- Keep dependencies updated
- Use HTTPS everywhere
- Monitor for vulnerabilities
- Regular backups

### Backups:
- Backup to local machine regularly
- Use GitHub for version control
- Keep previous versions in branches

---

## Next Steps After Deployment

1. **Share Your Portfolio**:
   - Add to LinkedIn
   - Share on Twitter
   - Post on GitHub
   - Email to contacts

2. **Promote**:
   - Submit to portfolio websites
   - Share on Reddit/Dev communities
   - Add to job applications

3. **Monitor**:
   - Track visitors with Google Analytics
   - Monitor performance metrics
   - Gather feedback

4. **Improve**:
   - Add analytics insights
   - Optimize based on traffic patterns
   - Add new projects and content

---

## Quick Comparison

| Platform | Cost | Setup | Speed | Best For |
|----------|------|-------|-------|----------|
| GitHub Pages | Free | Easy | Fast | Git users |
| Netlify | Free | Very Easy | Very Fast | Beginners |
| Vercel | Free | Very Easy | Fastest | Performance |
| Traditional | $2-15/mo | Medium | Varies | Control |

---

## Support & Resources

- GitHub Pages Docs: https://pages.github.com/
- Netlify Docs: https://docs.netlify.com/
- Vercel Docs: https://vercel.com/docs
- DNS Help: https://www.cloudflare.com/learning/dns/
- SSL Info: https://www.ssl.com/article/ssl-tls-https-process/

---

**Your portfolio is now ready for the world! 🚀**

For questions, check the specific platform's documentation.
