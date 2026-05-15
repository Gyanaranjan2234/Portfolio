# Email Service Configuration Guide

This guide helps you set up email functionality for your portfolio contact form.

## Option 1: Formspree (Recommended - Easy Setup)

### Steps:
1. Visit https://formspree.io/
2. Sign up with your email
3. Create a new form and get your form endpoint (looks like: `https://formspree.io/f/XXXXXX`)
4. Update your HTML form in `index.html`:

```html
<form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" data-aos="fade-left">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send Message</button>
</form>
```

5. That's it! Emails will be sent to your verified email address.

### Pros:
- ✅ No backend required
- ✅ Free tier available
- ✅ Easy setup
- ✅ Spam protection

### Cons:
- ⚠️ Limited customization
- ⚠️ Free tier has limits
- ⚠️ Limited branding

---

## Option 2: EmailJS (Client-Side Email Service)

### Steps:
1. Sign up at https://www.emailjs.com/
2. Create a Gmail account or connect your email service
3. Get your Service ID, Template ID, and Public Key
4. Add EmailJS library to `index.html` (in the `<head>`):

```html
<script type="text/javascript" 
    src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/index.min.js">
</script>
```

5. Update `script.js` with:

```javascript
// Initialize EmailJS
(function(){
    emailjs.init("YOUR_PUBLIC_KEY_HERE");
})();

// Update contact form submission
function sendEmail(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    emailjs.send("SERVICE_ID", "TEMPLATE_ID", {
        from_name: name,
        from_email: email,
        message: message,
        to_email: "gyana.tcr20@gmail.com"
    }).then(() => {
        showNotification('Email sent successfully!', 'success');
        document.getElementById('contactForm').reset();
    }).catch(error => {
        showNotification('Failed to send email', 'error');
        console.error('EmailJS Error:', error);
    });
}
```

### Pros:
- ✅ No backend needed
- ✅ Direct client-side sending
- ✅ Customizable templates
- ✅ Free tier available

### Cons:
- ⚠️ Public key visible in code (minimal security risk for contact forms)
- ⚠️ More setup required

---

## Option 3: Backend with Node.js/Express (Advanced)

### Steps:

1. **Create a simple backend** (e.g., using Node.js):

```javascript
// server.js
const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Configure email service
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASSWORD // Use app-specific password
    }
});

// Email endpoint
app.post('/api/send-email', async (req, res) => {
    const { name, email, message } = req.body;
    
    try {
        await transporter.sendMail({
            from: process.env.EMAIL_USER,
            to: 'gyana.tcr20@gmail.com',
            subject: `New Message from ${name}`,
            html: `
                <h2>New Contact Form Submission</h2>
                <p><strong>Name:</strong> ${name}</p>
                <p><strong>Email:</strong> ${email}</p>
                <p><strong>Message:</strong></p>
                <p>${message}</p>
            `
        });
        
        res.json({ success: true, message: 'Email sent successfully' });
    } catch (error) {
        console.error('Email error:', error);
        res.status(500).json({ success: false, error: error.message });
    }
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

2. **Update `script.js`**:

```javascript
async function sendEmailViaBackend(name, email, message) {
    try {
        const response = await fetch('/api/send-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, message })
        });
        
        const data = await response.json();
        if (data.success) {
            showNotification('Message sent successfully!', 'success');
        } else {
            showNotification('Failed to send message', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showNotification('Error sending message', 'error');
    }
}
```

3. **Create `.env` file** in your project root:

```
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-specific-password
```

4. **Deploy backend**:
   - Use services like Heroku, Railway, Render, or Vercel
   - Ensure environment variables are set in deployment

### Pros:
- ✅ Most secure (credentials not exposed)
- ✅ Full customization
- ✅ Easy email templating
- ✅ Can log emails to database

### Cons:
- ⚠️ Requires backend setup
- ⚠️ Requires hosting
- ⚠️ More complex deployment

---

## Option 4: Third-Party Services

### SendGrid
- Visit https://sendgrid.com/
- Create account and API key
- Use SendGrid's email API

### Mailgun
- Visit https://www.mailgun.com/
- Create account and API key
- Integrate with your form

### AWS SES (Simple Email Service)
- Use AWS SES for high-volume emails
- More complex setup but very reliable

---

## Quick Setup Checklist

- [ ] Choose email service option
- [ ] Create account/API credentials
- [ ] Update HTML form with correct action/method
- [ ] Test email sending
- [ ] Verify email arrives in inbox
- [ ] Add error handling
- [ ] Test with multiple emails

---

## Gmail App Password (For Gmail/Nodemailer)

If using Nodemailer with Gmail:

1. Enable 2-Factor Authentication on your Google Account
2. Go to https://myaccount.google.com/apppasswords
3. Select "Mail" and "Windows Computer" (or your device)
4. Generate app password
5. Use this password in your `.env` file (NOT your regular Gmail password)

---

## Testing the Contact Form

Before going live:

1. Test with valid email
2. Test with invalid email (should show error)
3. Test with empty fields (should show error)
4. Verify email arrives
5. Test on mobile devices
6. Check email formatting

---

## Troubleshooting

### Emails not arriving?
- Check spam/junk folder
- Verify sender email is correct
- Check service credentials
- Review service logs

### CORS errors?
- Add CORS headers to backend
- Use Formspree instead (handles CORS)

### Rate limiting?
- Implement rate limiting in backend
- Use service's built-in rate limits

---

## Security Best Practices

1. Never expose API keys in frontend code
2. Use environment variables for credentials
3. Validate email format server-side
4. Add rate limiting to prevent spam
5. Use HTTPS for form submissions
6. Implement CAPTCHA for added protection
7. Sanitize user input
8. Log email submissions for records

---

## Support

For issues:
- Check the service documentation
- Review error messages in browser console
- Test connectivity to external services
- Verify API credentials are correct

**Recommended**: Start with Formspree for simplicity, then upgrade to backend as needed.
