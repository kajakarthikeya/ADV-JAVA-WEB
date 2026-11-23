# -*- coding: utf-8 -*-
"""
Perfect Lab Record Portal Builder
Integrates:
1. Centered Top Header: ADVANCED JAVA PROGRAMMING · Roll Number: 24EU08161
2. Left Sidebar: All Weeks 0-13 with expandable tasks and live search
3. Visual Hierarchy: Large prominent WEEK headings, smaller TASK headings
4. Step-by-Step Practical Screenshot Galleries (12-18 steps per task)
5. Proof Screenshots in Program & Output sections (No Mac dots)
6. Comprehensive 4-card Result Analysis for each week
7. Master index.html portal with dynamic week switching without reloads
"""

import os
import re
import shutil

from step_gallery_data import STEP_GALLERY_DATA
from build_sidebar_helpers import WEEKS_META, get_header_html, get_sidebar_html, get_step_gallery_html

# Import raw authoritative bodies
import sys
sys.path.append('JAVA-WEB-main')
from build_weeks_0_to_3_v2 import w0_body, w1_body, w2_body, w3_body
from build_weeks_4_to_8_v2 import w4_body, w5_body, w6_body, w8_body
from build_weeks_9_to_13_v2 import w9_body, w10_body, w11_body, w12_body, w13_body
from update_week_7_v2 import content as w7_body

raw_bodies = {
    0: w0_body,
    1: w1_body,
    2: w2_body,
    3: w3_body,
    4: w4_body,
    5: w5_body,
    6: w6_body,
    7: w7_body,
    8: w8_body,
    9: w9_body,
    10: w10_body,
    11: w11_body,
    12: w12_body,
    13: w13_body
}

def clean_body_html(body_html):
    # Remove old <div class="topic-content-wrap container">
    cleaned = re.sub(r'<div class="topic-content-wrap container">', '', body_html)
    # Remove old <aside class="topic-sidebar"[\s\S]*?</aside>', '')
    cleaned = re.sub(r'<aside class="topic-sidebar"[\s\S]*?</aside>', '', cleaned)
    # Remove <article class="topic-main"> and closing </article>
    cleaned = re.sub(r'<article class="topic-main">', '', cleaned)
    cleaned = re.sub(r'</article>', '', cleaned)
    
    # REMOVE ALL .ss-actions (Replace, Download, Choose File input buttons)
    cleaned = re.sub(r'<div class="ss-actions">[\s\S]*?</div>', '', cleaned)
    cleaned = re.sub(r'<div class="step-card-actions">[\s\S]*?</div>', '', cleaned)
    cleaned = re.sub(r'<button class="[^"]*ss-replace-btn[^"]*">[\s\S]*?</button>', '', cleaned)
    cleaned = re.sub(r'<a class="[^"]*ss-download-btn[^"]*"[\s\S]*?</a>', '', cleaned)
    cleaned = re.sub(r'<input type="file"[^>]*>', '', cleaned)
    
    # Remove trailing </div>
    cleaned = cleaned.strip()
    if cleaned.endswith("</div>"):
        cleaned = cleaned[:-6].strip()
    return cleaned

def transform_week_content(num, is_page=True):
    meta = WEEKS_META[num]
    raw = raw_bodies[num]
    cleaned = clean_body_html(raw)
    
    # Adjust image paths if for index.html (is_page=False)
    if not is_page:
        cleaned = cleaned.replace("../assets/", "assets/")
        
    week_key = f"week-{num}"
    
    # Large prominent Week Heading
    week_header_html = f"""
      <div class="week-main-header">
        <div class="week-super-meta">
          <span class="week-number-badge">WEEK {num:02d}</span>
          <span class="week-category-tag">{meta['category']}</span>
          <span class="week-roll-tag">Roll: 24EU08161</span>
        </div>
        <h1 class="week-display-title">WEEK {num}: {meta['full_title'].upper()}</h1>
        <p class="week-overview-desc">{meta['desc']}</p>
      </div>
"""
    
    # For single task weeks (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    if num in [1, 2, 3, 4, 5, 6, 10, 11, 12, 13]:
        task_id = f"{week_key}-task-1"
        task_title = meta["tasks"][0][1]
        step_gallery = get_step_gallery_html(week_key, "task-1", is_page=is_page)
        step_count = len(STEP_GALLERY_DATA.get(week_key, {}).get("task-1", []))
        
        gallery_block = ""
        if step_gallery:
            gallery_block = f"""
        <section class="content-section" id="step-gallery" style="margin-top:24px;">
          <h2 class="content-section-title"><span class="section-icon">📷</span> Step-by-Step Practical Screenshot Gallery ({step_count} Steps)</h2>
          <p style="font-size:0.84rem;color:#64748B;margin-bottom:14px;">Every individual setup, coding, compilation, database, and execution step documented chronologically:</p>
          {step_gallery}
        </section>
"""
        # Inject step gallery right before result analysis
        if '<section class="content-section" id="result-analysis">' in cleaned:
            parts = cleaned.split('<section class="content-section" id="result-analysis">')
            cleaned = parts[0] + gallery_block + '<section class="content-section" id="result-analysis">' + parts[1]
        else:
            cleaned += gallery_block

        content = f"""{week_header_html}
      <section class="task-section" id="{task_id}">
        <div class="task-header-block">
          <div class="task-pretitle">WEEK {num} · PRACTICAL EXPERIMENT</div>
          <h2 class="task-display-title">{task_title}</h2>
        </div>
        {cleaned}
      </section>
"""
        return content

    elif num == 0:
        # Multi-task Week 0 split into 5 distinct task sections
        sec_dict = {}
        for sid, sec_content in re.findall(r'<section[^>]*id=["\'](.*?)["\'][^>]*>([\s\S]*?)</section>', cleaned):
            sec_dict[sid] = f'<section class="content-section" id="{sid}">{sec_content}</section>'

        step_gal = get_step_gallery_html("week-0", "task-1", is_page=is_page)
        gal_block = f"""
        <section class="content-section" id="step-gallery" style="margin-top:24px;">
          <h2 class="content-section-title"><span class="section-icon">📷</span> Step-by-Step Practical Screenshot Gallery (10 Steps)</h2>
          <p style="font-size:0.84rem;color:#64748B;margin-bottom:14px;">Every individual setup, coding, compilation, database, and execution step documented chronologically:</p>
          {step_gal}
        </section>
"""

        t1_content = f"""
      <section class="task-section" id="week-0-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 1 · THEORETICAL FOUNDATION</div>
          <h2 class="task-display-title">Task 1: Introduction to Advanced Java &amp; Architecture</h2>
        </div>
        {sec_dict.get('aim', '')}
        {sec_dict.get('requirements', '')}
        {gal_block}
      </section>
"""

        t2_content = f"""
      <section class="task-section" id="week-0-task-2">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 2 · ARCHITECTURAL PARADIGM</div>
          <h2 class="task-display-title">Task 2: Core Java vs Advanced Java</h2>
        </div>
        <div class="content-section">
          <h3 class="task-sub-title"><span class="sub-icon">🏛️</span> Architectural Comparison: Java SE Desktop vs Jakarta EE Multi-tier</h3>
          <p>Core Java (Java SE) runtime is physically bounded by the single local client JVM memory space. In contrast, Advanced Java (Jakarta EE) leverages distributed, container-managed execution contexts where thread pooling, transactions, and resource lifecycles are abstracted by enterprise servers such as Apache Tomcat.</p>
        </div>
        {sec_dict.get('program', '')}
        {sec_dict.get('output', '')}
      </section>
"""

        t3_content = f"""
      <section class="task-section" id="week-0-task-3">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 3 · CLIENT VS SERVER-SIDE EVOLUTION</div>
          <h2 class="task-display-title">Task 3: Java Applets and Servlets</h2>
        </div>
        <div class="content-section">
          <h3 class="task-sub-title"><span class="sub-icon">🌐</span> Applet Sunsetting &amp; Servlet Emergence</h3>
          <p>Browser security restrictions and the deprecation of NPAPI (Netscape Plugin Application Programming Interface) eliminated client-side Java Applets. Server-side Java Servlets emerged as the standard, running within high-throughput web containers to serve dynamic HTTP content securely and scalably.</p>
          <div class="table-wrap" style="margin-top:16px;">
            <table>
              <thead>
                <tr>
                  <th>Dimension</th>
                  <th>Java Applets (Client-Side - Deprecated)</th>
                  <th>Java Servlets (Server-Side - Industry Standard)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Execution Environment</strong></td>
                  <td>User browser JVM sandbox (requires browser plugin)</td>
                  <td>Server-side Servlet Container (Tomcat, Jetty, GlassFish)</td>
                </tr>
                <tr>
                  <td><strong>Security Model</strong></td>
                  <td>Strict client sandbox, highly vulnerable to exploits</td>
                  <td>Enterprise firewall protection, protected server memory</td>
                </tr>
                <tr>
                  <td><strong>Resource Access</strong></td>
                  <td>Restricted client filesystem/network access</td>
                  <td>Full access to enterprise databases, microservices, caches</td>
                </tr>
                <tr>
                  <td><strong>Concurrency Model</strong></td>
                  <td>Single client execution instance</td>
                  <td>Multithreaded request dispatching with shared connection pool</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
"""

        t4_content = f"""
      <section class="task-section" id="week-0-task-4">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 4 · DATABASE CONNECTIVITY ARCHITECTURE</div>
          <h2 class="task-display-title">Task 4: JDBC and ODBC</h2>
        </div>
        <div class="content-section">
          <h3 class="task-sub-title"><span class="sub-icon">🔌</span> Database Connectivity: Type-4 Pure Java vs Type-1 ODBC Bridge</h3>
          <p>Open Database Connectivity (ODBC) requires native C/C++ libraries installed on each client machine. Java Database Connectivity (JDBC) Type-4 direct-socket network protocol drivers communicate directly with MySQL and Oracle databases over TCP/IP (port 3306), achieving cross-platform portability and zero native dependency overhead.</p>
          <div class="table-wrap" style="margin-top:16px;">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>ODBC (Open Database Connectivity)</th>
                  <th>JDBC (Java Database Connectivity)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Origin Language</strong></td>
                  <td>C / C++ Native Binary API</td>
                  <td>Pure Java Object-Oriented API (java.sql.*)</td>
                </tr>
                <tr>
                  <td><strong>Platform Portability</strong></td>
                  <td>Platform dependent (Windows/Linux ODBC managers)</td>
                  <td>100% Platform independent (WORA: Write Once, Run Anywhere)</td>
                </tr>
                <tr>
                  <td><strong>Driver Architecture</strong></td>
                  <td>Native DLLs and client OS middleware</td>
                  <td>Type-4 Direct Network Socket Driver (mysql-connector-j)</td>
                </tr>
                <tr>
                  <td><strong>Connection Pooling</strong></td>
                  <td>Managed via OS ODBC Administrator</td>
                  <td>Integrated via HikariCP, Tomcat DBCP, and DataSource APIs</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
"""

        t5_content = f"""
      <section class="task-section" id="week-0-task-5">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 5 · STATE MANAGEMENT STRATEGIES</div>
          <h2 class="task-display-title">Task 5: Cookies and Sessions</h2>
        </div>
        <div class="content-section">
          <h3 class="task-sub-title"><span class="sub-icon">🍪</span> HTTP State Tracking: Cookies vs Server-Side HttpSession</h3>
          <p>Because the HTTP protocol is inherently stateless, enterprise applications track user identity and state using either client-side HTTP Cookies or server-side <code>HttpSession</code> objects referenced by <code>JSESSIONID</code> tokens.</p>
          <div class="table-wrap" style="margin-top:16px;">
            <table>
              <thead>
                <tr>
                  <th>Criterion</th>
                  <th>HTTP Cookies</th>
                  <th>HttpSession</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Storage Location</strong></td>
                  <td>Client browser text store (&lt; 4 KB per cookie)</td>
                  <td>Server heap memory (unlimited object graph size)</td>
                </tr>
                <tr>
                  <td><strong>Data Type</strong></td>
                  <td>String / Text only (requires URL encoding)</td>
                  <td>Any Serializable Java Object (java.lang.Object)</td>
                </tr>
                <tr>
                  <td><strong>Security Context</strong></td>
                  <td>Vulnerable to client inspection &amp; XSS without HttpOnly</td>
                  <td>Secure: Client receives only transient opaque session ID</td>
                </tr>
                <tr>
                  <td><strong>Lifecycle Management</strong></td>
                  <td>MaxAge attribute (persistent or session-scoped)</td>
                  <td>session.setMaxInactiveInterval() or session.invalidate()</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        {sec_dict.get('result-analysis', '')}
        {sec_dict.get('qa-matrix', '')}
        {sec_dict.get('result', '')}
      </section>
"""
        content = f"""{week_header_html}
        {t1_content}
        {t2_content}
        {t3_content}
        {t4_content}
        {t5_content}
"""
        return content

    elif num == 7:
        # Multi-task Week 7 with 16 authentic NetBeans & IE screenshots
        for i in range(1, 7):
            cleaned = cleaned.replace(f'id="activity-{i}"', f'id="week-7-task-{i}" class="task-section content-section"')
        content = f"""{week_header_html}
        {cleaned}
"""
        return content

    elif num == 8:
        # Multi-task Week 8
        t1_gal = get_step_gallery_html("week-8", "task-1", is_page=is_page)
        t2_gal = get_step_gallery_html("week-8", "task-2", is_page=is_page)
        
        # Inject galleries into week 8
        content = f"""{week_header_html}
      <section class="task-section" id="week-8-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 1 · MULTI-TIER WEB APPLICATION</div>
          <h2 class="task-display-title">Task 1: Student Management System using Servlets, JDBC and MySQL</h2>
        </div>
        <div style="margin-bottom:20px;">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Student Management System (16 Steps)</h3>
          {t1_gal}
        </div>
      </section>

      <section class="task-section" id="week-8-task-2">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 2 · STATE MANAGEMENT</div>
          <h2 class="task-display-title">Task 2: Cookies Demonstration Using Java Servlets</h2>
        </div>
        <div style="margin-bottom:20px;">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Cookie State Tracking (12 Steps)</h3>
          {t2_gal}
        </div>
      </section>

      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">SOURCE CODE, EXECUTION &amp; RESULT ANALYSIS</div>
          <h2 class="task-display-title">Comprehensive Technical Walkthrough &amp; Results</h2>
        </div>
        {cleaned}
      </div>
"""
        return content

    elif num == 9:
        # Multi-task Week 9
        t1_gal = get_step_gallery_html("week-9", "task-1", is_page=is_page)
        t2_gal = get_step_gallery_html("week-9", "task-2", is_page=is_page)
        t3_gal = get_step_gallery_html("week-9", "task-3", is_page=is_page)

        content = f"""{week_header_html}
      <section class="task-section" id="week-9-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">ACTIVITY 1</div>
          <h2 class="task-display-title">Task 1: Steps to Build Maven + Spring Boot Application in STS</h2>
        </div>
        <div style="margin-bottom:20px;">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Maven + Spring Boot Setup (15 Steps)</h3>
          {t1_gal}
        </div>
      </section>

      <section class="task-section" id="week-9-task-2">
        <div class="task-header-block">
          <div class="task-pretitle">ACTIVITY 2</div>
          <h2 class="task-display-title">Task 2: Develop a Simple Spring Boot Web Application in STS</h2>
        </div>
        <div style="margin-bottom:20px;">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Web Controller Ingestion (12 Steps)</h3>
          {t2_gal}
        </div>
      </section>

      <section class="task-section" id="week-9-task-3">
        <div class="task-header-block">
          <div class="task-pretitle">ACTIVITY 3</div>
          <h2 class="task-display-title">Task 3: POM.xml Configuration and Dependency Management</h2>
        </div>
        <div style="margin-bottom:20px;">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: POM.xml Configuration (12 Steps)</h3>
          {t3_gal}
        </div>
      </section>

      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">COMPLETE IMPLEMENTATION &amp; RESULT ANALYSIS</div>
          <h2 class="task-display-title">STS Setup, Build Success &amp; Evaluation</h2>
        </div>
        {cleaned}
      </div>
"""
        return content

def assemble_standalone_page(num):
    meta = WEEKS_META[num]
    header = get_header_html(is_page=True)
    sidebar = get_sidebar_html(num, is_page=True)
    content = transform_week_content(num, is_page=True)
    
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Week {num}: {meta['full_title']} | Lab Record</title>
  <meta name="description" content="{meta['desc']} - Advanced Java Programming Lab (24IT385) by Venkata Sai Karthikeya Kaja (24EU08161)" />
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

{header}

  <div class="portal-layout">
{sidebar}

    <main class="portal-main-content" id="portalMainContent">
{content}
    </main>
  </div>

  <!-- IMAGE ZOOM LIGHTBOX MODAL -->
  <div id="zoom-modal" class="modal-overlay" aria-hidden="true" role="dialog" aria-label="Screenshot Preview">
    <div class="modal-content">
      <button class="modal-close" aria-label="Close Preview" title="Close (Esc)">&times;</button>
      <img src="" alt="Screenshot Preview" class="modal-img" />
      <div class="modal-caption" id="modalCaption"></div>
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
        <a href="../index.html" class="btn btn-secondary btn-sm" style="color:#F8FAFC;border-color:#334155;">🏠 Home Hub</a>
      </div>
    </div>
  </footer>

  <script src="../script.js"></script>
</body>
</html>
"""

def assemble_master_index():
    header = get_header_html(is_page=False)
    
    # Custom index sidebar with dynamic pane data attributes
    sidebar = """    <!-- LEFT SIDEBAR: WEEK-WISE NAVIGATION -->
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
        sidebar += f"""        <div class="sidebar-week-group {active_cls}" data-week="{num}">
          <a href="#week-{num}" class="sidebar-week-link" data-week="{num}" data-week-target="week-{num}-pane">
            <span class="week-pill">W{num}</span>
            <span class="week-title-text">{w['title']}</span>
            <span class="week-arrow">›</span>
          </a>
          <div class="sidebar-task-list">
"""
        for tid, ttitle in w["tasks"]:
            sidebar += f"""            <a href="#{tid}" class="sidebar-task-link" data-week="{num}" data-week-target="week-{num}-pane" data-task-anchor="{tid}" title="{ttitle}">{ttitle}</a>\n"""
        sidebar += f"""          </div>
        </div>\n"""
    sidebar += """      </nav>
    </aside>"""

    panes_html = ""
    for num in range(14):
        meta = WEEKS_META[num]
        content = transform_week_content(num, is_page=False)
        
        prev_btn = f'<button class="btn btn-secondary btn-sm switch-week-btn" data-target="week-{num-1}-pane">← Week {num-1}</button>' if num > 0 else '<span></span>'
        next_btn = f'<button class="btn btn-primary btn-sm switch-week-btn" data-target="week-{num+1}-pane">Week {num+1} →</button>' if num < 13 else '<span></span>'
        open_page_btn = f'<a href="pages/week-{num}.html" class="btn btn-secondary btn-sm" target="_blank" style="margin-left:auto;"><i class="bi bi-box-arrow-up-right"></i> Open Dedicated Standalone Page ↗</a>'
        
        active_pane_cls = "active-pane" if num == 0 else ""
        display_style = "display: block;" if num == 0 else "display: none;"
        
        panes_html += f"""
      <!-- WEEK {num} PANE -->
      <div class="week-pane {active_pane_cls}" id="week-{num}-pane" style="{display_style}">
        <div style="display:flex;justify-content:flex-end;margin-bottom:14px;">
          {open_page_btn}
        </div>
        {content}
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:36px;padding-top:20px;border-top:1px solid #D1FAE5;">
          {prev_btn}
          <span style="font-size:0.85rem;color:#64748B;font-weight:600;">Week {num} of 13 · Advanced Java Lab Record</span>
          {next_btn}
        </div>
      </div>
"""

    downloads_section = """
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

    return f"""<!DOCTYPE html>
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

{header}

  <div class="portal-layout">
{sidebar}

    <main class="portal-main-content" id="portalMainContent">
{panes_html}
{downloads_section}
    </main>
  </div>

  <!-- IMAGE ZOOM LIGHTBOX MODAL -->
  <div id="zoom-modal" class="modal-overlay" aria-hidden="true" role="dialog" aria-label="Screenshot Preview">
    <div class="modal-content">
      <button class="modal-close" aria-label="Close Preview" title="Close (Esc)">&times;</button>
      <img src="" alt="Screenshot Preview" class="modal-img" />
      <div class="modal-caption" id="modalCaption"></div>
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
      </div>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
"""

if __name__ == "__main__":
    print("Building all 14 standalone week pages with perfect layout and galleries...")
    for w in range(14):
        html = assemble_standalone_page(w)
        p = f"pages/week-{w}.html"
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {p} ({len(html):,} bytes)")

    print("Building master index.html portal...")
    idx_html = assemble_master_index()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_html)
    print(f"Generated index.html ({len(idx_html):,} bytes)")

    print("Build complete!")

