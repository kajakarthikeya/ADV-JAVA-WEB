import os

SCRIPT_CONTENT = """/* ============================================================
   ADVANCED JAVA PROGRAMMING LAB RECORD — SCRIPT ENGINE
   Course: 24IT385 · Academic Year: 2026–2027
   Student: Venkata Sai Karthikeya Kaja (Roll: 24EU08161)
   Department of Information Technology · Siddhartha Academy of Higher Education
   ============================================================ */

'use strict';

document.addEventListener('DOMContentLoaded', () => {
  initLoader();
  initNavbar();
  initMobileNav();
  initScrollProgress();
  initBackToTop();
  initRevealAnimations();
  initTypingEffect();
  initButtonRipple();
  initSmoothScroll();
  initCodeEditors();
  generateCardGraphics();
  initScreenshotGallery();
  initZoomModal();
  initStatCounters();
  initWeekSearchAndFilter();
});

/* ─────────────────────────────────────────
   1. LOADER
──────────────────────────────────────────── */
function initLoader() {
  const loader = document.getElementById('loader');
  if (!loader) return;

  const hide = () => {
    loader.classList.add('hidden');
    document.body.style.overflow = '';
  };

  window.addEventListener('load', () => setTimeout(hide, 350));
  setTimeout(hide, 1200); // Fallback
}

/* ─────────────────────────────────────────
   2. NAVBAR & MOBILE NAV
──────────────────────────────────────────── */
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;

  const check = () => navbar.classList.toggle('scrolled', window.scrollY > 15);
  check();
  window.addEventListener('scroll', check, { passive: true });
}

function initMobileNav() {
  const hamburger = document.querySelector('.hamburger');
  const mobileNav = document.querySelector('.mobile-nav');
  if (!hamburger || !mobileNav) return;

  hamburger.addEventListener('click', () => {
    const isOpen = mobileNav.classList.toggle('open');
    hamburger.classList.toggle('active', isOpen);
    hamburger.setAttribute('aria-expanded', isOpen);
  });

  mobileNav.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      hamburger.classList.remove('active');
    });
  });
}

/* ─────────────────────────────────────────
   3. SCROLL PROGRESS BAR
──────────────────────────────────────────── */
function initScrollProgress() {
  const bar = document.getElementById('scroll-progress');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    const progress = total > 0 ? (window.scrollY / total) * 100 : 0;
    bar.style.width = `${Math.min(progress, 100)}%`;
  }, { passive: true });
}

/* ─────────────────────────────────────────
   4. BACK TO TOP
──────────────────────────────────────────── */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 350);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ─────────────────────────────────────────
   5. REVEAL ANIMATIONS
──────────────────────────────────────────── */
function initRevealAnimations() {
  const elements = document.querySelectorAll('.reveal, .stagger-children');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  elements.forEach(el => observer.observe(el));
}

/* ─────────────────────────────────────────
   6. TYPING EFFECT (Curriculum-wide Code Snippets)
──────────────────────────────────────────── */
function initTypingEffect() {
  const target = document.querySelector('.hero-typing-text');
  if (!target) return;

  const phrases = [
    'Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/studentdb", "root", "");',
    'PreparedStatement ps = con.prepareStatement("INSERT INTO student VALUES (?, ?, ?, ?)");',
    '@RestController @RequestMapping("/api/students") public class StudentController { ... }',
    'List<Student> findByLastNameOrderByFirstNameAsc(String lastName);',
    'JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);',
    'Cookie cookie = new Cookie("username", username); response.addCookie(cookie);'
  ];

  let pIndex = 0, cIndex = 0, isDeleting = false;

  function loop() {
    const current = phrases[pIndex];
    if (!isDeleting) {
      target.textContent = current.slice(0, cIndex + 1);
      cIndex++;
      if (cIndex === current.length) {
        isDeleting = true;
        setTimeout(loop, 2200);
        return;
      }
    } else {
      target.textContent = current.slice(0, cIndex - 1);
      cIndex--;
      if (cIndex === 0) {
        isDeleting = false;
        pIndex = (pIndex + 1) % phrases.length;
        setTimeout(loop, 400);
        return;
      }
    }
    setTimeout(loop, isDeleting ? 25 : 55);
  }
  setTimeout(loop, 600);
}

/* ─────────────────────────────────────────
   7. BUTTON RIPPLE EFFECT
──────────────────────────────────────────── */
function initButtonRipple() {
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      const rect = this.getBoundingClientRect();
      const ripple = document.createElement('span');
      ripple.style.cssText = `
        position: absolute;
        width: 10px; height: 10px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 50%;
        left: ${e.clientX - rect.left}px;
        top: ${e.clientY - rect.top}px;
        transform: translate(-50%, -50%) scale(0);
        animation: rippleAnim 0.6s ease-out forwards;
        pointer-events: none;
      `;
      this.style.position = 'relative';
      this.style.overflow = 'hidden';
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 650);
    });
  });

  if (!document.getElementById('ripple-style')) {
    const style = document.createElement('style');
    style.id = 'ripple-style';
    style.textContent = `@keyframes rippleAnim { to { transform: translate(-50%, -50%) scale(35); opacity: 0; } }`;
    document.head.appendChild(style);
  }
}

/* ─────────────────────────────────────────
   8. SMOOTH SCROLL
──────────────────────────────────────────── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const offsetTop = target.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top: offsetTop, behavior: 'smooth' });
    });
  });
}

/* ─────────────────────────────────────────
   9. CODE EDITORS (COPY, COLLAPSE, DOWNLOAD .JAVA/.SQL/.XML/.SH)
──────────────────────────────────────────── */
function initCodeEditors() {
  // Copy Code
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', async () => {
      const editor = btn.closest('.code-editor');
      const code = editor ? editor.querySelector('code') : null;
      if (!code) return;
      try {
        await navigator.clipboard.writeText(code.textContent);
        const prev = btn.textContent;
        btn.textContent = '✅ Copied!';
        btn.style.color = '#4ade80';
        setTimeout(() => {
          btn.textContent = prev;
          btn.style.color = '';
        }, 2000);
      } catch (err) {
        btn.textContent = 'Error';
      }
    });
  });

  // Collapse Code
  document.querySelectorAll('.collapse-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const editor = btn.closest('.code-editor');
      const body = editor ? editor.querySelector('.code-editor-body') : null;
      if (!body) return;
      body.classList.toggle('collapsed');
      btn.textContent = body.classList.contains('collapsed') ? '⬇ Expand' : '⬆ Collapse';
    });
  });

  // Download Code file (any language / filetype)
  document.querySelectorAll('.dl-java-btn, .dl-code-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const editor = btn.closest('.code-editor');
      const code = editor ? editor.querySelector('code') : null;
      const filename = btn.getAttribute('data-filename') || (editor ? editor.querySelector('.editor-filename')?.textContent.trim() : null) || 'Program.java';
      if (!code) return;

      const blob = new Blob([code.textContent], { type: 'text/plain;charset=utf-8' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = filename;
      link.click();
      URL.revokeObjectURL(link.href);
    });
  });
}

/* ─────────────────────────────────────────
   10. FALLBACK REALISTIC SVG GRAPHIC GENERATOR
   (Only applies if an imgWrap does NOT already contain an authentic extracted image)
──────────────────────────────────────────── */
function generateCardGraphics() {
  const targetWrappers = document.querySelectorAll('.ss-img-wrap, .timeline-step-img');

  targetWrappers.forEach((imgWrap, index) => {
    // If an authentic <img> is already present, do NOT overwrite it
    if (imgWrap.querySelector('img')) return;

    const card = imgWrap.closest('.ss-card, .timeline-card');
    const title = imgWrap.dataset.title || (card ? (card.querySelector('.ss-caption') || card.querySelector('.timeline-title'))?.textContent.trim() : `Step ${index + 1}`);
    const subcaption = card ? (card.querySelector('.ss-subcaption') || card.querySelector('.timeline-desc'))?.textContent.trim() : '';
    const badgeText = (card ? card.querySelector('.ss-step-badge')?.textContent.trim() : null) || `Step 0${(index % 5) + 1}`;

    const svgString = buildRealisticLabSVG(title, subcaption, badgeText);
    const encodedSvg = 'data:image/svg+xml;utf8,' + encodeURIComponent(svgString);

    imgWrap.innerHTML = `
      <img src="${encodedSvg}" alt="${escapeXml(title)}" />
      <div class="ss-zoom-overlay">
        <span>🔍 Click to Zoom</span>
      </div>
    `;
  });
}

function buildRealisticLabSVG(title, subcaption, badgeText) {
  const t = (title + ' ' + subcaption).toLowerCase();
  let fill = '#000000';
  let lines = [
    'NetBeans IDE 8.2 / STS Build Window',
    `Execution target: ${title}`,
    'run:',
    'BUILD SUCCESSFUL (total time: 1 second)'
  ];

  if (t.includes('terminal') || t.includes('ubuntu') || t.includes('jdk')) {
    return `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="337" viewBox="0 0 600 337">
      <rect width="600" height="337" rx="6" fill="#2c001e"/>
      <text x="20" y="32" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">
        <tspan fill="#5cbf26">student@ITLAB3-1:</tspan>
        <tspan fill="#729fcf">~</tspan>
        <tspan fill="#ffffff">$ java --version</tspan>
      </text>
      <text x="20" y="60" font-family="'JetBrains Mono', monospace" font-size="12" fill="#dedede">java 26.0.1 2026-04-21</text>
      <text x="20" y="82" font-family="'JetBrains Mono', monospace" font-size="12" fill="#dedede">Java(TM) SE Runtime Environment (build 26.0.1+8-34)</text>
      <text x="20" y="104" font-family="'JetBrains Mono', monospace" font-size="12" fill="#dedede">Java HotSpot(TM) 64-Bit Server VM (build 26.0.1+8-34, mixed mode)</text>
    </svg>`;
  }

  const linesHtml = lines.map((l, i) =>
    `<text x="25" y="${36 + i * 24}" font-family="'Courier New', Consolas, monospace" font-size="13" fill="${i === 3 ? '#008000' : '#333333'}" font-weight="${i === 3 ? 'bold' : 'normal'}">${escapeXml(l)}</text>`
  ).join('');

  return `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="337" viewBox="0 0 600 337">
    <rect width="600" height="337" fill="#ffffff" stroke="#a0a0a0" stroke-width="2"/>
    ${linesHtml}
  </svg>`;
}

function escapeXml(str) {
  return String(str).replace(/[&<>"']/g, m => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&apos;'
  })[m]);
}

/* ─────────────────────────────────────────
   11. SCREENSHOT GALLERY & FILEREADER REPLACEMENT
──────────────────────────────────────────── */
function initScreenshotGallery() {
  // Replace Image Button Trigger (FileReader API)
  document.querySelectorAll('.ss-replace-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const card = btn.closest('.ss-card');
      const fileInput = card ? card.querySelector('.ss-file-input') : null;
      if (fileInput) fileInput.click();
    });
  });

  // Handle File Upload Change
  document.querySelectorAll('.ss-file-input').forEach(input => {
    input.addEventListener('change', function() {
      const file = this.files[0];
      if (!file) return;
      const card = this.closest('.ss-card');
      const imgWrap = card ? card.querySelector('.ss-img-wrap') : null;
      if (!imgWrap) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        imgWrap.innerHTML = `
          <img src="${e.target.result}" alt="Lab Screenshot" />
          <div class="ss-zoom-overlay">
            <span>🔍 Click to Zoom</span>
          </div>
        `;
      };
      reader.readAsDataURL(file);
    });
  });

  // Download Image Button
  document.querySelectorAll('.ss-download-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const card = btn.closest('.ss-card');
      const img = card ? card.querySelector('.ss-img-wrap img') : null;
      const caption = card ? (card.querySelector('.ss-caption')?.textContent.trim() || 'screenshot') : 'screenshot';
      const cleanName = caption.toLowerCase().replace(/[^a-z0-9]/g, '_') + '.png';

      if (img && img.src) {
        const link = document.createElement('a');
        link.href = img.src;
        link.download = cleanName;
        link.click();
      }
    });
  });
}

/* ─────────────────────────────────────────
   12. CLICK TO ZOOM LIGHTBOX WITH PREV / NEXT & KEYBOARD CYCLING
──────────────────────────────────────────── */
function initZoomModal() {
  const modal = document.getElementById('zoom-modal');
  if (!modal) return;

  const modalImg = modal.querySelector('.modal-img');
  const modalCap = modal.querySelector('.modal-caption');
  const closeBtn = modal.querySelector('.modal-close');
  const prevBtn = modal.querySelector('.modal-prev');
  const nextBtn = modal.querySelector('.modal-next');

  let imagesList = [];
  let currentIndex = 0;

  function updateModalImage(index) {
    if (imagesList.length === 0) return;
    if (index < 0) index = imagesList.length - 1;
    if (index >= imagesList.length) index = 0;
    currentIndex = index;

    const item = imagesList[currentIndex];
    modalImg.src = item.src;
    modalCap.textContent = `${item.caption} (${currentIndex + 1} of ${imagesList.length})`;
  }

  // Find all zoomable images on the page
  function refreshImagesList() {
    imagesList = [];
    document.querySelectorAll('.ss-img-wrap img, .timeline-step-img img').forEach((img, idx) => {
      const card = img.closest('.ss-card, .timeline-card');
      const caption = card ? (card.querySelector('.ss-caption') || card.querySelector('.timeline-title'))?.textContent.trim() : `Figure ${idx + 1}`;
      imagesList.push({ src: img.src, caption: caption || `Figure ${idx + 1}` });
    });
  }

  // Open modal on click
  document.addEventListener('click', (e) => {
    const imgWrap = e.target.closest('.ss-img-wrap, .timeline-step-img');
    if (!imgWrap) return;

    const clickedImg = imgWrap.querySelector('img');
    if (!clickedImg || !clickedImg.src) return;

    refreshImagesList();
    const foundIdx = imagesList.findIndex(item => item.src === clickedImg.src);
    currentIndex = foundIdx !== -1 ? foundIdx : 0;

    updateModalImage(currentIndex);
    modal.classList.add('open');
  });

  const closeModal = () => modal.classList.remove('open');

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (prevBtn) prevBtn.addEventListener('click', (e) => { e.stopPropagation(); updateModalImage(currentIndex - 1); });
  if (nextBtn) nextBtn.addEventListener('click', (e) => { e.stopPropagation(); updateModalImage(currentIndex + 1); });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('open')) return;
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowLeft') updateModalImage(currentIndex - 1);
    if (e.key === 'ArrowRight') updateModalImage(currentIndex + 1);
  });
}

/* ─────────────────────────────────────────
   13. STAT COUNTERS
──────────────────────────────────────────── */
function initStatCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.count, 10);
      const suffix = el.dataset.suffix || '';
      const duration = 1200;
      const start = performance.now();

      function update(now) {
        const elapsed = now - start;
        const progress = Math.min(elapsed / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(ease * target) + suffix;
        if (progress < 1) requestAnimationFrame(update);
      }

      requestAnimationFrame(update);
      observer.unobserve(el);
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
}

/* ─────────────────────────────────────────
   14. WEEK SEARCH & CATEGORY FILTER
──────────────────────────────────────────── */
function initWeekSearchAndFilter() {
  const searchInput = document.getElementById('week-search-input');
  const clearBtn = document.getElementById('search-clear-btn');
  const filterChips = document.querySelectorAll('.filter-chip');
  const weekCards = document.querySelectorAll('.week-card');
  const noWeeksMsg = document.getElementById('no-weeks-found');

  if (!weekCards.length) return;

  let activeCategory = 'all';
  let searchTerm = '';

  function applyFilters() {
    let visibleCount = 0;

    weekCards.forEach(card => {
      const category = card.getAttribute('data-category');
      const keywords = (card.getAttribute('data-keywords') || '') + ' ' + card.textContent.toLowerCase();
      
      const matchesCategory = (activeCategory === 'all') || (category === activeCategory);
      const matchesSearch = !searchTerm || keywords.includes(searchTerm);

      if (matchesCategory && matchesSearch) {
        card.classList.remove('is-hidden');
        visibleCount++;
      } else {
        card.classList.add('is-hidden');
      }
    });

    if (noWeeksMsg) {
      noWeeksMsg.style.display = visibleCount === 0 ? 'block' : 'none';
    }

    if (clearBtn) {
      clearBtn.style.display = searchTerm.length > 0 ? 'block' : 'none';
    }
  }

  // Filter chips click handler
  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeCategory = chip.getAttribute('data-filter') || 'all';
      applyFilters();
    });
  });

  // Search input handler
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  // Clear button handler
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      if (searchInput) searchInput.value = '';
      searchTerm = '';
      applyFilters();
      if (searchInput) searchInput.focus();
    });
  }
}
"""

with open(r'c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\script.js', 'w', encoding='utf-8') as f:
    f.write(SCRIPT_CONTENT)

print("script.js written successfully!")

