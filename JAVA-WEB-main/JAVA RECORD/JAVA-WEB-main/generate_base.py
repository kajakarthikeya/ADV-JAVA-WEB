# -*- coding: utf-8 -*-
"""
Generator for Week 0 to Week 3 HTML Pages
Advanced Java Programming Lab (24IT385)
Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os

pages_dir = r'C:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\pages'
os.makedirs(pages_dir, exist_ok=True)

def get_page_header(week_num, title, subtitle, pills, category):
    prev_link = f'week-{week_num-1}.html' if week_num > 0 else '#'
    next_link = f'week-{week_num+1}.html' if week_num < 13 else '#'
    pills_html = "".join([f'<span class="meta-pill">{p}</span>' for p in pills])
    
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Week {week_num}: {title} | Lab Record</title>
  <meta name="description" content="{subtitle} - Advanced Java Programming Lab (24IT385) by Venkata Sai Karthikeya Kaja (24EU08161)" />
  <link rel="icon" type="image/svg+xml"
    href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%23059669'/><g fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M9 10c0-2 1.3-2.5 1.3-4.5S9 3.5 9 1.5'/><path d='M16 9c0-2 1.3-2.5 1.3-4.5S16 2.5 16 0.5'/><path d='M23 10c0-2 1.3-2.5 1.3-4.5S23 3.5 23 1.5'/><path d='M6 14h17v8a7 7 0 0 1-7 7h-3a7 7 0 0 1-7-7v-8z' fill='white' fill-opacity='0.25'/><path d='M23 15h3a2.5 2.5 0 0 1 2.5 2.5v2a2.5 2.5 0 0 1-2.5 2.5h-3'/><path d='M3 30h26'/></g></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />
  <link rel="stylesheet" href="../style.css" />
  <link rel="stylesheet" href="../assets/css/topic-page.css" />
</head>

<body>
  <div id="scroll-progress" aria-hidden="true"></div>

  <!-- NAVBAR -->
  <header>
    <nav class="navbar" role="navigation" aria-label="Main navigation">
      <div class="navbar-inner">
        <a href="../index.html" class="nav-logo" aria-label="Back to home">
          <div class="nav-logo-icon" aria-label="Java Logo">
            <svg class="coffee-cup-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22"
              fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path class="steam steam-1" d="M6 7c0-1.5 1-2 1-3.5S6 2 6 0.5"></path>
              <path class="steam steam-2" d="M12 6c0-1.5 1-2 1-3.5S12 1 12 0"></path>
              <path class="steam steam-3" d="M18 7c0-1.5 1-2 1-3.5S18 2 18 0.5"></path>
              <path d="M4 10h13v6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5v-6z" fill="currentColor" fill-opacity="0.25"></path>
              <path d="M17 11h2.5a2 2 0 0 1 2 2v1.5a2 2 0 0 1-2 2H17"></path>
              <path d="M2 22h19"></path>
            </svg>
          </div>
          <div class="nav-logo-text">
            <span class="nav-logo-title">Advanced Java Programming</span>
            <span class="nav-logo-sub">Lab Record · 24IT385</span>
          </div>
        </a>
        <ul class="nav-links" role="list">
          <li><a href="../index.html#hero" class="nav-link">Home</a></li>
          <li><a href="../index.html#weeks" class="nav-link active">All Weeks</a></li>
          <li><a href="../index.html#downloads" class="nav-link">Downloads</a></li>
          <li><a href="../index.html#contact" class="nav-link">Student Info</a></li>
        </ul>
        <div class="nav-cta">
          <a href="../index.html#weeks" class="btn btn-secondary btn-sm">← All 14 Weeks</a>
        </div>
        <button class="hamburger" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>
    <nav class="mobile-nav" aria-label="Mobile navigation">
      <a href="../index.html" class="nav-link">🏠 Home</a>
      <a href="../index.html#weeks" class="nav-link">📚 All Weeks</a>
      <a href="../index.html#downloads" class="nav-link">⬇️ Downloads</a>
      <a href="../index.html#contact" class="nav-link">👨‍🎓 Student Info</a>
    </nav>
  </header>

  <main class="topic-page">
    <!-- EXPERIMENT HERO -->
    <div class="topic-hero">
      <div class="container">
        <div class="topic-hero-breadcrumb">
          <a href="../index.html">Home</a>
          <span class="breadcrumb-sep">›</span>
          <a href="../index.html#weeks">Weeks</a>
          <span class="breadcrumb-sep">›</span>
          <span>Week {week_num}</span>
        </div>

        <div class="topic-hero-meta">
          <span class="topic-experiment-num">Week {week_num:02d}</span>
          <span class="badge badge-purple">{category}</span>
          <span class="badge badge-blue">Roll: 24EU08161</span>
        </div>

        <h1 class="topic-hero-title">
          {title}<br />
          <span class="highlight">{subtitle}</span>
        </h1>

        <div class="topic-meta-pills">
          {pills_html}
        </div>
      </div>
    </div>
"""

def get_page_footer(week_num):
    prev_num = week_num - 1
    next_num = week_num + 1
    prev_btn = f'<a href="week-{prev_num}.html" class="btn btn-secondary btn-md">← Previous: Week {prev_num}</a>' if week_num > 0 else '<span></span>'
    next_btn = f'<a href="week-{next_num}.html" class="btn btn-primary btn-md">Next: Week {next_num} →</a>' if week_num < 13 else '<span></span>'
    
    return f"""
        <!-- WEEK PAGINATION NAVIGATION -->
        <nav class="week-pagination-nav" aria-label="Week navigation" style="display:flex;justify-content:space-between;align-items:center;margin-top:48px;padding-top:24px;border-top:1px solid var(--border-glass);">
          {prev_btn}
          <a href="../index.html#weeks" class="btn btn-outline btn-sm">📚 All Weeks Index</a>
          {next_btn}
        </nav>

      </article>
    </div>
  </main>

  <!-- FOOTER -->
  <footer style="padding:48px 24px 32px;border-top:1px solid var(--border-glass);background:var(--bg-card);margin-top:60px;">
    <div class="container" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
      <div style="display:flex;align-items:center;gap:10px;">
        <div class="nav-logo-icon" aria-label="Java Logo">
          <svg class="coffee-cup-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path class="steam steam-1" d="M6 7c0-1.5 1-2 1-3.5S6 2 6 0.5"></path>
            <path class="steam steam-2" d="M12 6c0-1.5 1-2 1-3.5S12 1 12 0"></path>
            <path class="steam steam-3" d="M18 7c0-1.5 1-2 1-3.5S18 2 18 0.5"></path>
            <path d="M4 10h13v6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5v-6z" fill="currentColor" fill-opacity="0.25"></path>
            <path d="M17 11h2.5a2 2 0 0 1 2 2v1.5a2 2 0 0 1-2 2H17"></path>
            <path d="M2 22h19"></path>
          </svg>
        </div>
        <div>
          <div style="font-family:var(--font-heading);font-size:0.9rem;font-weight:800;color:var(--text-main);">Advanced Java Programming Lab Record</div>
          <div style="font-size:0.75rem;color:var(--text-muted);">Venkata Sai Karthikeya Kaja · Roll No: 24EU08161 · Course: 24IT385</div>
        </div>
      </div>
      <div style="font-size:0.8rem;color:var(--text-muted);">
        © 2026–2027 Siddhartha Academy of Higher Education. Department of Information Technology.
      </div>
    </div>
  </footer>

  <!-- FULLSCREEN ZOOM MODAL -->
  <div id="zoom-modal" class="modal-overlay" aria-hidden="true" role="dialog">
    <div class="modal-content">
      <span class="modal-close" title="Close Modal">&times;</span>
      <button class="modal-nav modal-prev" title="Previous Image" aria-label="Previous Image">&#10094;</button>
      <img src="" alt="Zoomed Screenshot" class="modal-img" />
      <button class="modal-nav modal-next" title="Next Image" aria-label="Next Image">&#10095;</button>
      <div class="modal-caption"></div>
    </div>
  </div>

  <button id="back-to-top" aria-label="Back to top">↑</button>

  <script src="../script.js"></script>
</body>
</html>
"""

print("Base helper functions ready.")

