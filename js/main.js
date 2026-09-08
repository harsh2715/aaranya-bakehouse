/* ============================================
   AARANYA BAKEHOUSE - Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initContactForm();
  initActiveNavLinks();
  initCakeEstimator();
  initFAQAccordion();
  initNewsletter();
});

/* ----- Mobile Menu ----- */
function initMobileMenu() {
  const toggle = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav__list');
  const navLinks = document.querySelectorAll('.nav__link');

  if (!toggle || !navList) return;

  toggle.addEventListener('click', () => {
    const isOpen = navList.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen);
  });

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navList.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });

  document.addEventListener('click', (e) => {
    if (!toggle.contains(e.target) && !navList.contains(e.target)) {
      navList.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
}

/* ----- Interactive Custom Cake Estimator ----- */
function initCakeEstimator() {
  const sizeSelect = document.getElementById('calcSize');
  const flavorSelect = document.getElementById('calcFlavor');
  const tiersSelect = document.getElementById('calcTiers');
  const priceDisplay = document.getElementById('calcPrice');
  const bookBtn = document.getElementById('calcBookBtn');

  if (!sizeSelect || !priceDisplay) return;

  function calculateEstimate() {
    const basePrices = {
      '0.5kg': 750,
      '1.0kg': 1350,
      '1.5kg': 1950,
      '2.0kg': 2550,
      '3.0kg+': 3800
    };

    const flavorMultipliers = {
      'classic': 1.0,
      'belgian': 1.15,
      'red-velvet': 1.10,
      'fruit': 1.20,
      'pistachio': 1.25
    };

    const tierAddons = {
      '1': 0,
      '2': 450,
      '3': 900
    };

    const size = sizeSelect.value || '1.0kg';
    const flavor = flavorSelect ? flavorSelect.value : 'classic';
    const tiers = tiersSelect ? tiersSelect.value : '1';

    const base = basePrices[size] || 1350;
    const mult = flavorMultipliers[flavor] || 1.0;
    const addon = tierAddons[tiers] || 0;

    const total = Math.round((base * mult) + addon);
    priceDisplay.textContent = `₹${total.toLocaleString('en-IN')}`;

    if (bookBtn) {
      const msg = `Hi Aaranya Bakehouse, I want to enquire about a custom cake: Size ${size}, Flavor ${flavor}, ${tiers} Tier(s). Estimated price: ₹${total}.`;
      bookBtn.href = `contact.html?service=custom-cakes&size=${encodeURIComponent(size)}&note=${encodeURIComponent(msg)}`;
    }
  }

  [sizeSelect, flavorSelect, tiersSelect].forEach(el => {
    if (el) el.addEventListener('change', calculateEstimate);
  });

  calculateEstimate();
}

/* ----- FAQ Accordion ----- */
function initFAQAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  if (!faqItems.length) return;

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      // Close other accordions
      faqItems.forEach(other => {
        if (other !== item) other.classList.remove('active');
      });

      // Toggle current
      item.classList.toggle('active', !isActive);
    });
  });
}

/* ----- Contact Form Validation & Submission ----- */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  // Pre-fill from URL params if available
  const urlParams = new URLSearchParams(window.location.search);
  const serviceParam = urlParams.get('service');
  const noteParam = urlParams.get('note');

  if (serviceParam) {
    const serviceSelect = document.getElementById('service');
    if (serviceSelect) serviceSelect.value = serviceParam;
  }
  if (noteParam) {
    const messageInput = document.getElementById('message');
    if (messageInput) messageInput.value = noteParam;
  }

  const fields = [
    { id: 'name', required: true, label: 'Full Name' },
    { id: 'email', required: true, type: 'email', label: 'Email' },
    { id: 'phone', required: true, label: 'Phone Number' },
    { id: 'service', required: true, label: 'Product Required' },
    { id: 'date', required: false, label: 'Event Date' },
    { id: 'message', required: true, label: 'Enquiry Details' }
  ];

  fields.forEach(field => {
    const input = document.getElementById(field.id);
    if (!input) return;

    const errorEl = input.parentElement.querySelector('.form-error');

    input.addEventListener('blur', () => validateField(input, field, errorEl));
    input.addEventListener('input', () => {
      if (input.classList.contains('error')) {
        validateField(input, field, errorEl);
      }
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;

    fields.forEach(field => {
      const input = document.getElementById(field.id);
      const errorEl = input ? input.parentElement.querySelector('.form-error') : null;
      if (!validateField(input, field, errorEl)) {
        isValid = false;
      }
    });

    if (isValid) {
      const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        service: document.getElementById('service').value,
        date: document.getElementById('date') ? document.getElementById('date').value : '',
        message: document.getElementById('message').value,
        submittedAt: new Date().toISOString()
      };

      // Save enquiry locally for mock persistence
      try {
        const pastEnquiries = JSON.parse(localStorage.getItem('aaranya_enquiries') || '[]');
        pastEnquiries.push(formData);
        localStorage.setItem('aaranya_enquiries', JSON.stringify(pastEnquiries));
      } catch (err) {
        console.warn('Storage error', err);
      }

      form.reset();
      form.querySelectorAll('.form-control').forEach(el => el.classList.remove('error'));
      form.querySelectorAll('.form-error').forEach(el => el.classList.remove('visible'));
      
      const successEl = document.getElementById('formSuccess');
      if (successEl) {
        successEl.innerHTML = `
          <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">🎉</div>
          <h3 style="color: #2E7D32; margin-bottom: 0.4rem;">Thank you, ${formData.name.split(' ')[0]}!</h3>
          <p style="margin-bottom: 0.8rem; color: #2E7D32;">We have received your enquiry for <strong>${formData.service}</strong>. Our baker will get in touch with you at <strong>${formData.phone}</strong> within 2 business hours!</p>
          <a href="https://wa.me/919876543210?text=${encodeURIComponent('Hi Aaranya Bakehouse! I just submitted an enquiry for ' + formData.service)}" target="_blank" class="btn btn--primary btn--sm" style="background:#25D366; box-shadow:none;">Quick Chat on WhatsApp</a>
        `;
        successEl.classList.add('visible');
        successEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  });
}

function validateField(input, field, errorEl) {
  if (!input) return false;

  let valid = true;
  let message = '';

  if (field.required && !input.value.trim()) {
    valid = false;
    message = `${field.label} is required.`;
  } else if (field.type === 'email' && input.value.trim()) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(input.value.trim())) {
      valid = false;
      message = 'Please enter a valid email address.';
    }
  }

  if (!valid) {
    input.classList.add('error');
    if (errorEl) {
      errorEl.textContent = message;
      errorEl.classList.add('visible');
    }
  } else {
    input.classList.remove('error');
    if (errorEl) {
      errorEl.classList.remove('visible');
    }
  }

  return valid;
}

/* ----- Active Navigation Links ----- */
function initActiveNavLinks() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const links = document.querySelectorAll('.nav__link');
  
  links.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

/* ----- Newsletter Subscription ----- */
function initNewsletter() {
  const form = document.getElementById('newsletterForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = form.querySelector('input[type="email"]');
    if (input && input.value.includes('@')) {
      form.innerHTML = `<p style="color: #A5D6A7; font-weight:600; margin:0;">✨ Welcome to the Aaranya Circle! Your 10% discount code: <strong>CELEBRATE10</strong> has been noted.</p>`;
    }
  });
}
