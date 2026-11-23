# -*- coding: utf-8 -*-
"""
Master Portal index.html Builder
Builds index.html with Centered Top Header, Left Sidebar (Weeks 0-13),
and Dynamic Tab/Pane Switching for all 14 weeks without page reloads!
"""

import os
import re
from build_sidebar_helpers import WEEKS_META, get_header_html
from build_complete_system import build_week_0, build_week_7, build_week_8, build_week_9, build_single_task_week

def get_index_sidebar_html():
    html = """    <!-- LEFT SIDEBAR: WEEK-WISE NAVIGATION -->
    <aside class="portal-sidebar" id="portalSidebar">
      <div class="sidebar-header">
        <div class="sidebar-title">
          <i class="bi bi-journal-code"></i> Digital Lab Record
        </div>
        <div class="sidebar-subtitle">Weeks 0 — 13 Navigation · 24IT385</div>
      </div>

      <div class="sidebar-search-box">
        <i class="bi bi-search"></i>
        <input type="text" id="weekSearchInput" placeholder="Filter week or task..." />
      </div>

      <nav class="sidebar-week-nav" role="navigation" aria-label="Lab Weeks Navigation">
"""
    for w in WEEKS_META:
        num = w["num"]
        active_cls = "active open" if num == 0 else ""
        html += f"""        <div class="sidebar-week-group {active_cls}" data-week="{num}">
          <a href="#week-{num}" class="sidebar-week-link" data-week-target="week-{num}-pane">
            <span class="week-pill">W{num}</span>
            <span class="week-title-text">{w['title']}</span>
            <span class="week-arrow">›</span>
          </a>
          <div class="sidebar-task-list">
"""
        for tid, ttitle in w["tasks"]:
            html += f"""            <a href="#week-{num}" class="sidebar-task-link" data-week-target="week-{num}-pane" data-task-anchor="{tid}" title="{ttitle}">{ttitle}</a>\n"""
        html += f"""          </div>
        </div>\n"""
        
    html += """      </nav>
    </aside>"""
    return html

def build_index_html():
    header_html = get_header_html(is_page=False)
    sidebar_html = get_index_sidebar_html()
    
    panes_html = ""
    for num in range(14):
        meta = WEEKS_META[num]
        fpath = f"pages/week-{num}.html"
        with open(fpath, "r", encoding="utf-8") as fp:
            orig = fp.read()
            
        if num == 0:
            pane_body = build_week_0(orig)
        elif num == 7:
            pane_body = build_week_7(orig)
        elif num == 8:
            pane_body = build_week_8(orig)
        elif num == 9:
            pane_body = build_week_9(orig)
        else:
            pane_body = build_single_task_week(num, meta, orig)
            
        # Adjust image paths for root index.html
        pane_body = pane_body.replace("../assets/", "assets/")
        
        # Navigation between weeks
        prev_btn = f'<button class="btn btn-secondary btn-sm switch-week-btn" data-target="week-{num-1}-pane">← Week {num-1}</button>' if num > 0 else '<span></span>'
        next_btn = f'<button class="btn btn-primary btn-sm switch-week-btn" data-target="week-{num+1}-pane">Week {num+1} →</button>' if num < 13 else '<span></span>'
        
        open_page_btn = f'<a href="pages/week-{num}.html" class="btn btn-secondary btn-sm" target="_blank" style="margin-left:auto;"><i class="bi bi-box-arrow-up-right"></i> Open Dedicated Standalone Page</a>'
        
        active_pane_cls = "active-pane" if num == 0 else ""
        display_style = "display: block;" if num == 0 else "display: none;"
        
        panes_html += f"""
      <!-- WEEK {num} PANE -->
      <div class="week-pane {active_pane_cls}" id="week-{num}-pane" style="{display_style}">
        <div style="display:flex;justify-content:flex-end;margin-bottom:14px;">
          {open_page_btn}
        </div>
        {pane_body}
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:36px;padding-top:20px;border-top:1px solid #D1FAE5;">
          {prev_btn}
          <span style="font-size:0.85rem;color:#64748B;font-weight:600;">Week {num} of 13 · Advanced Java Lab Record</span>
          {next_btn}
        </div>
      </div>
"""

    downloads_section = """
      <!-- DOWNLOADS & ARCHITECTURE SECTION -->
      <section class="task-section" id="downloads" style="margin-top:48px;">
        <div class="task-header-block">
          <div class="task-pretitle">LAB REPOSITORY RESOURCES</div>
          <h2 class="task-display-title">Authoritative Lab Source Code &amp; Documentation Downloads</h2>
          <p style="font-size:0.9rem;color:#64748B;margin-top:4px;">All source code files (.java), Maven build descriptors (pom.xml), and lab records for 24EU08161:</p>
        </div>
        
        <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:16px;">
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">☕ AccessDemo.java</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 3: Pure Java UCanAccess MS Access Connectivity.</p>
            <a href="assets/downloads/AccessDemo.java" download class="step-btn">⬇ Download .java</a>
          </div>
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">☕ StudentCRUD.java</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 6: MySQL JDBC Full CRUD Application.</p>
            <a href="assets/downloads/StudentCRUD.java" download class="step-btn">⬇ Download .java</a>
          </div>
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">☕ NewServlet.java</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 7: NetBeans HTTP Servlet with Roll 24EU08161.</p>
            <a href="assets/downloads/NewServlet.java" download class="step-btn">⬇ Download .java</a>
          </div>
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">☕ GetPostServlet.java</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 7: Servlet Handling GET and POST Methods.</p>
            <a href="assets/downloads/GetPostServlet.java" download class="step-btn">⬇ Download .java</a>
          </div>
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">☕ AuthorService.java</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 10: Spring Boot JdbcTemplate with In-Memory H2.</p>
            <a href="assets/downloads/AuthorService.java" download class="step-btn">⬇ Download .java</a>
          </div>
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">☕ EmployeeRepository.java</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 11: Spring Data JPA MySQL Repository.</p>
            <a href="assets/downloads/EmployeeRepository.java" download class="step-btn">⬇ Download .java</a>
          </div>
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">☕ StudentRepository.java</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 13: Derived &amp; Custom Native @Query Methods.</p>
            <a href="assets/downloads/StudentRepository.java" download class="step-btn">⬇ Download .java</a>
          </div>
          <div class="step-card" style="padding:16px;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:6px;">📄 ADVANCED_JAVA_SERVLET_RECORD_24EU08161.docx</div>
            <p style="font-size:0.78rem;color:#64748B;margin-bottom:12px;">Week 7: Full Authentic Servlet Record with NetBeans Screenshots.</p>
            <a href="assets/documents/ADVANCED_JAVA_SERVLET_RECORD_24EU08161.docx" download class="step-btn">⬇ Download Docx</a>
          </div>
        </div>
      </section>

      <!-- STUDENT PROFILE -->
      <section class="task-section" id="student-profile" style="margin-top:24px;">
        <div class="task-header-block">
          <div class="task-pretitle">STUDENT IDENTIFICATION</div>
          <h2 class="task-display-title">Academic &amp; Institutional Credentials</h2>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:20px;">
          <div><span style="color:#64748B;font-size:0.78rem;text-transform:uppercase;">Candidate Name:</span><div style="font-weight:700;color:#0F172A;font-size:1.05rem;">Venkata Sai Karthikeya Kaja</div></div>
          <div><span style="color:#64748B;font-size:0.78rem;text-transform:uppercase;">University Roll Number:</span><div style="font-weight:800;color:#059669;font-size:1.15rem;font-family:var(--font-code);">24EU08161</div></div>
          <div><span style="color:#64748B;font-size:0.78rem;text-transform:uppercase;">Academic Department:</span><div style="font-weight:600;color:#0F172A;">Information Technology</div></div>
          <div><span style="color:#64748B;font-size:0.78rem;text-transform:uppercase;">Course &amp; Code:</span><div style="font-weight:600;color:#0F172A;">Advanced Java Programming Lab (24IT385)</div></div>
          <div><span style="color:#64748B;font-size:0.78rem;text-transform:uppercase;">Institution:</span><div style="font-weight:600;color:#0F172A;">Siddhartha Academy of Higher Education</div></div>
          <div><span style="color:#64748B;font-size:0.78rem;text-transform:uppercase;">Academic Year:</span><div style="font-weight:600;color:#0F172A;">2026–2027</div></div>
        </div>
      </section>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Advanced Java Programming Lab Record (24IT385) | Week 0 — Week 13</title>
  <meta name="description" content="Digital Laboratory Record for Advanced Java Programming Lab (24IT385) by Venkata Sai Karthikeya Kaja (24EU08161), Department of Information Technology, Siddhartha Academy of Higher Education." />
  <link rel="icon" type="image/svg+xml"
    href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%23059669'/><g fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M9 10c0-2 1.3-2.5 1.3-4.5S9 3.5 9 1.5'/><path d='M16 9c0-2 1.3-2.5 1.3-4.5S16 2.5 16 0.5'/><path d='M23 10c0-2 1.3-2.5 1.3-4.5S23 3.5 23 1.5'/><path d='M6 14h17v8a7 7 0 0 1-7 7h-3a7 7 0 0 1-7-7v-8z' fill='white' fill-opacity='0.25'/><path d='M23 15h3a2.5 2.5 0 0 1 2.5 2.5v2a2.5 2.5 0 0 1-2.5 2.5h-3'/><path d='M3 30h26'/></g></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="assets/css/topic-page.css" />
</head>

<body>
  <div id="scroll-progress" aria-hidden="true"></div>

{header_html}

  <div class="portal-layout">
{sidebar_html}

    <main class="portal-main-content" id="portalMainContent">
{panes_html}
{downloads_section}
    </main>
  </div>

  <!-- IMAGE ZOOM MODAL -->
  <div class="ss-modal" id="ssModal" role="dialog" aria-modal="true" aria-label="Screenshot zoom view">
    <div class="ss-modal-backdrop"></div>
    <div class="ss-modal-content">
      <div class="ss-modal-header">
        <h4 class="ss-modal-title" id="ssModalTitle">Figure Preview</h4>
        <div class="ss-modal-actions">
          <a href="#" download id="ssModalDownload" class="btn btn-secondary btn-sm">⬇ Download Full-Res</a>
          <button class="ss-modal-close" aria-label="Close modal">✕</button>
        </div>
      </div>
      <div class="ss-modal-body">
        <img src="" alt="Fullscreen screenshot" id="ssModalImg" />
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="footer" style="background:#0F172A;color:#94A3B8;padding:40px 24px 28px;border-top:1px solid #1E293B;">
    <div style="max-width:1440px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px;">
      <div>
        <div style="font-family:var(--font-heading);font-weight:800;color:#F8FAFC;font-size:1.05rem;">Advanced Java Programming Lab Record (24IT385)</div>
        <div style="font-size:0.84rem;margin-top:4px;">Venkata Sai Karthikeya Kaja · Roll Number: <strong style="color:#10B981;">24EU08161</strong> · Department of Information Technology</div>
        <div style="font-size:0.78rem;color:#64748B;">Siddhartha Academy of Higher Education · Academic Year 2026–2027</div>
      </div>
      <div style="display:flex;gap:12px;">
        <a href="#week-0" class="btn btn-secondary btn-sm switch-week-btn" data-target="week-0-pane" style="color:#F8FAFC;border-color:#334155;">↑ Top of Record</a>
        <a href="#downloads" class="btn btn-secondary btn-sm" style="color:#F8FAFC;border-color:#334155;">⬇ All Downloads</a>
      </div>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as fp:
        fp.write(html)
    print("Generated master index.html portal successfully!")

if __name__ == "__main__":
    build_index_html()

