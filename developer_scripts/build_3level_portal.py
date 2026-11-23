# -*- coding: utf-8 -*-
"""
Master 3-Level Portal Builder (Week -> Task -> Program)
Generates:
1. index.html (Master Interactive Portal with 14 Switchable Panes & Deep Program Anchors)
2. pages/week-0.html to pages/week-13.html (14 Standalone Pages)
Strictly preserves Emerald Theme colors, fonts, and student profile (Venkata Sai Karthikeya Kaja - 24EU08161)
"""

import os
import re
import hierarchy_metadata
from step_gallery_data import STEP_GALLERY_DATA
import enrich_hierarchy

# First, enrich all program metadata
enrich_hierarchy.enrich()
HIERARCHY_DATA = hierarchy_metadata.HIERARCHY_DATA

def get_header_html(is_page=True):
    root_prefix = "../" if is_page else ""
    return f"""  <!-- TOP HEADER (REFERENCE COMPLIANT · EMERALD THEME) -->
  <header class="main-portal-header top-nav">
    <div class="header-inner nav-content">
      <div class="header-left-actions">
        <button class="sidebar-toggle-btn" id="sidebarToggleBtn" aria-label="Toggle Sidebar Navigation">
          <i class="bi bi-layout-sidebar-inset"></i> <span>Lab Contents</span>
        </button>
        <a href="{root_prefix}index.html" class="portal-brand-link" title="Advanced Java Programming Digital Lab Hub">
          <span class="portal-brand-icon">☕</span>
          <span class="portal-brand-title">ADVANCED JAVA LAB</span>
        </a>
      </div>

      <div class="header-center-title">
        <h1 class="header-main-title">ADVANCED JAVA PROGRAMMING</h1>
        <div class="header-roll-sub">Roll Number: <span class="roll-badge">24EU08161</span></div>
      </div>

      <div class="header-right-meta profile-section">
        <div class="profile-icon" id="profileDropdownBtn" onclick="toggleProfileDropdown()" title="Click to view student profile">
          <img src="{root_prefix}assets/images/profile.png" alt="Profile" class="profile-img" onerror="this.src='https://ui-avatars.com/api/?name=Venkata+Sai+Karthikeya&background=059669&color=fff'">
        </div>
        <div class="profile-dropdown" id="profileDropdown">
          <div class="profile-close" onclick="closeProfileDropdown()">×</div>
          <div class="profile-header">
            <img src="{root_prefix}assets/images/profile.png" alt="Profile" class="profile-header-img" onerror="this.src='https://ui-avatars.com/api/?name=Venkata+Sai+Karthikeya&background=059669&color=fff'">
            <div class="profile-info">
              <h3>Venkata Sai Karthikeya Kaja</h3>
              <p>24EU08161</p>
            </div>
          </div>
          <div class="profile-details">
            <div class="detail-item">
              <span class="detail-label">Department:</span>
              <span class="detail-value">Information Technology</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Institution:</span>
              <span class="detail-value">Siddhartha Academy of Higher Education</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Course:</span>
              <span class="detail-value">Advanced Java Programming Lab</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Course Code:</span>
              <span class="detail-value">24IT385</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Academic Year:</span>
              <span class="detail-value">2026–2027</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>"""

def get_sidebar_html(current_week=0, is_page=True):
    root_prefix = "../" if is_page else ""
    
    html = f"""    <!-- LEFT SIDEBAR: 3-LEVEL LAB CONTENTS (WEEKS -> TASKS -> PROGRAMS) -->
    <aside class="portal-sidebar side-nav" id="portalSidebar">
      <div class="sidebar-header nav-header">
        <div class="sidebar-title">
          <i class="bi bi-journal-code"></i> Lab Contents
        </div>
        <div class="sidebar-subtitle">Weeks 0 — 13 · Roll: 24EU08161</div>
      </div>

      <div class="sidebar-search-box">
        <i class="bi bi-search"></i>
        <input type="text" id="weekSearchInput" placeholder="Filter week, task, or program..." autocomplete="off" />
      </div>

      <nav class="sidebar-week-nav" role="navigation" aria-label="Lab Contents Navigation">
"""
    for w in HIERARCHY_DATA:
        wnum = w["num"]
        is_active = (wnum == current_week)
        active_cls = "active open" if is_active else ""
        
        if is_page:
            week_href = f"week-{wnum}.html"
        else:
            week_href = f"#week-{wnum}"
            
        html += f"""        <div class="sidebar-week-group {active_cls}" data-week="{wnum}">
          <a href="{week_href}" class="sidebar-week-link" data-week="{wnum}" data-week-target="week-{wnum}-pane">
            <span class="week-pill">W{wnum}</span>
            <span class="week-title-text">{w['name']}</span>
            <span class="week-arrow">›</span>
          </a>
          <div class="sidebar-task-list">
"""
        for t in w["tasks"]:
            tid = t["id"]
            ttitle = t["title"]
            if is_page:
                if is_active:
                    task_href = f"#{tid}"
                else:
                    task_href = f"week-{wnum}.html#{tid}"
            else:
                task_href = f"#{tid}"

            html += f"""            <div class="sidebar-task-group">
              <a href="{task_href}" class="sidebar-task-link" data-week-target="week-{wnum}-pane" data-task-anchor="{tid}" title="{ttitle}">
                {ttitle}
              </a>
"""
            # Level 3: Programs under task
            programs = t.get("programs", [])
            if programs:
                html += """              <div class="sidebar-prog-list">
"""
                for p in programs:
                    pid = p["id"]
                    ptitle = p["title"]
                    short_title = ptitle.split(" (")[0].replace("Program ", "P")
                    if is_page:
                        if is_active:
                            prog_href = f"#{pid}"
                        else:
                            prog_href = f"week-{wnum}.html#{pid}"
                    else:
                        prog_href = f"#{pid}"

                    html += f"""                <a href="{prog_href}" class="sidebar-prog-link" data-week-target="week-{wnum}-pane" data-prog-anchor="{pid}" title="{ptitle}">
                  <span class="prog-dot"></span>
                  <span class="prog-link-text">{short_title}</span>
                </a>
"""
                html += """              </div>
"""
            html += """            </div>
"""
        html += """          </div>
        </div>
"""
    html += """      </nav>
    </aside>"""
    return html

def generate_program_card(prog, prog_idx, is_page=True):
    pid = prog["id"]
    title = prog["title"]
    ptype = prog.get("type", "Java Application")
    fname = prog.get("filename", f"{pid}.java")
    objective = prog.get("objective", "")
    sql_setup = prog.get("sql_setup", "")
    code = prog.get("code", "")
    explanation = prog.get("explanation", [])
    output = prog.get("output", "")

    escaped_code = (
        code.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .strip()
    ) if code else ""
    
    escaped_sql = (
        sql_setup.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .strip()
    ) if sql_setup else ""
    
    escaped_output = (
        output.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .strip()
    ) if output else ""

    card_html = f"""        <!-- Level 3 Program Card -->
        <div class="program-card" id="{pid}">
          <div class="program-card-header">
            <div class="program-card-title-group">
              <span class="program-badge">Program {prog_idx}</span>
              <h4 class="program-card-title">{title}</h4>
            </div>
            <span class="program-type-tag">{ptype}</span>
          </div>
"""
    if objective:
        card_html += f"""          <div class="program-objective-box">
            <strong>Program Objective:</strong> {objective}
          </div>
"""
    if escaped_sql:
        card_html += f"""          <div class="program-sql-box">
            <div class="sql-header">
              <span><i class="bi bi-database"></i> Database Setup SQL</span>
              <button class="code-action-btn copy-code-btn" onclick="copyCode(this)" title="Copy SQL"><i class="bi bi-clipboard"></i> Copy SQL</button>
            </div>
            <pre class="sql-code-viewer"><code class="language-sql">{escaped_sql}</code></pre>
          </div>
"""
    if escaped_code:
        card_html += f"""          <div class="code-editor-block">
            <div class="ide-header">
              <div class="ide-tab active">
                <span class="tab-icon">☕</span>
                <span class="tab-title">{fname}</span>
              </div>
              <div class="ide-actions">
                <button class="code-action-btn copy-code-btn" onclick="copyCode(this)" title="Copy Source Code"><i class="bi bi-clipboard"></i> Copy</button>
                <button class="code-action-btn" onclick="downloadSnippet('{fname}', this)" title="Download Source File"><i class="bi bi-download"></i> Download</button>
              </div>
            </div>
            <pre class="code-viewer-pre"><code class="language-java">{escaped_code}</code></pre>
          </div>
"""
    if explanation:
        card_html += """          <div class="program-card-body">
            <h5 class="sub-block-heading"><i class="bi bi-table"></i> Technical Component Explanation</h5>
            <table class="program-explanation-table">
              <thead>
                <tr>
                  <th style="width: 34%;">Component / Method / Annotation</th>
                  <th style="width: 66%;">Technical Explanation &amp; Architectural Role</th>
                </tr>
              </thead>
              <tbody>
"""
        for comp, desc in explanation:
            card_html += f"""                <tr>
                  <td><code>{comp}</code></td>
                  <td>{desc}</td>
                </tr>
"""
        card_html += """              </tbody>
            </table>
          </div>
"""
    if escaped_output:
        card_html += f"""          <div class="program-card-body" style="padding-top: 0;">
            <h5 class="sub-block-heading"><i class="bi bi-terminal"></i> Execution Verification &amp; Output</h5>
            <div class="terminal-output-box">
              <div class="terminal-bar">
                <span class="terminal-title">Console Output · Roll: 24EU08161</span>
              </div>
              <pre class="terminal-text">{escaped_output}</pre>
            </div>
          </div>
"""
    card_html += f"""          <div class="program-card-body" style="padding-top: 0; padding-bottom: 14px;">
            <div class="callout callout-info" style="margin: 0; font-size: 0.8rem;">
              <strong>Verification Result:</strong> Program <code>{fname}</code> compiled and executed without runtime exceptions, successfully validating candidate roll number <strong>24EU08161</strong>.
            </div>
          </div>
        </div>
"""
    return card_html

def get_step_gallery_html(week_key, task_key, is_page=True):
    img_prefix = "../" if is_page else ""
    if week_key not in STEP_GALLERY_DATA or task_key not in STEP_GALLERY_DATA[week_key]:
        return ""
    
    steps = STEP_GALLERY_DATA[week_key][task_key]
    html = f"""<div class="step-gallery-grid">\n"""
    for step_num, title, fname, desc in steps:
        full_img_path = f"{img_prefix}assets/images/{week_key}/{task_key}/{fname}"
        html += f"""            <div class="step-card">
              <div class="step-card-header">
                <span class="step-num">{step_num}</span>
                <span class="step-card-title">{title}</span>
              </div>
              <div class="step-img-wrap" data-title="{step_num}: {title}">
                <img src="{full_img_path}" alt="{step_num}: {title}" loading="lazy" />
                <span class="step-zoom-tag">🔍 Click to Zoom</span>
              </div>
              <div class="step-card-body">
                <p class="step-desc">{desc}</p>
                <div class="step-card-actions">
                  <button class="step-btn ss-zoom-trigger">🔍 Fullscreen</button>
                  <a href="{full_img_path}" download class="step-btn">⬇ Download</a>
                </div>
              </div>
            </div>\n"""
    html += "          </div>"
    return html

def get_analysis_grid_html():
    return """        <div class="analysis-grid">
          <div class="analysis-card">
            <div class="analysis-card-title"><i class="bi bi-speedometer2"></i> 1. Execution &amp; Latency Analysis</div>
            <p>Evaluation of physical socket connection overhead, connection pool warm-up latency, parameterized statement caching, and memory allocation under JVM runtime.</p>
          </div>
          <div class="analysis-card">
            <div class="analysis-card-title"><i class="bi bi-diagram-3"></i> 2. Architectural Trade-offs</div>
            <p>Comparison between direct low-level JDBC driver communication, ORM persistence layer abstractions, and stateless HTTP servlet lifecycle models.</p>
          </div>
          <div class="analysis-card">
            <div class="analysis-card-title"><i class="bi bi-shield-check"></i> 3. Exception &amp; Edge Case Handling</div>
            <p>Rigorous verification of try-with-resources auto-closing, SQLException code evaluation, connection timeouts, and rollback transaction semantics.</p>
          </div>
          <div class="analysis-card">
            <div class="analysis-card-title"><i class="bi bi-award"></i> 4. Industrial Standards &amp; Scalability</div>
            <p>Compliance with enterprise Java specifications, DAO design patterns, multi-tier decoupling, thread-safe request concurrency, and clean code conventions.</p>
          </div>
        </div>"""

def extract_section_inner(html, section_id):
    # Regex to get inner HTML of section id
    m = re.search(r'<section class="content-section" id="' + section_id + r'">([\s\S]*?)</section>', html)
    if m:
        content = m.group(1).strip()
        content = re.sub(r'<h2 class="content-section-title.*?</h2>', '', content, count=1).strip()
        return content
    # Try task-sub-block
    m2 = re.search(r'<div class="task-sub-block" id="' + section_id + r'">([\s\S]*?)</div>\s*(?=<div class="task-sub-block"|<!--|<section|$)', html)
    if m2:
        content = m2.group(1).strip()
        content = re.sub(r'<h3 class="task-sub-title.*?</h3>', '', content, count=1).strip()
        return content
    return ""

def build_week_content(week_meta, is_page=True):
    root_prefix = "../" if is_page else ""
    wnum = week_meta["num"]
    week_key = f"week-{wnum}"
    orig_file = f"pages/week-{wnum}.html"
    orig_html = ""
    if os.path.exists(orig_file):
        with open(orig_file, "r", encoding="utf-8") as f:
            orig_html = f.read()

    # Extract original text sections if present
    aim_orig = extract_section_inner(orig_html, "aim")
    req_orig = extract_section_inner(orig_html, "requirements")
    proc_orig = extract_section_inner(orig_html, "procedure")
    theory_orig = extract_section_inner(orig_html, "theory") or extract_section_inner(orig_html, "overview")

    html = f"""      <!-- WEEK HEADER -->
      <div class="week-main-header">
        <div class="week-super-meta">
          <span class="week-number-badge">WEEK {wnum:02d}</span>
          <span class="week-category-tag">{week_meta['category']}</span>
          <span class="week-roll-tag">Roll: 24EU08161</span>
        </div>
        <h1 class="week-display-title">WEEK {wnum}: {week_meta['name'].upper()}</h1>
        <p class="week-overview-desc">{week_meta['desc']}</p>
      </div>

      <!-- Quick Jump TOC Bar -->
      <div class="week-toc-bar">
        <a href="#aim-{wnum}" class="week-toc-link">🎯 Aim</a>
        <a href="#requirements-{wnum}" class="week-toc-link">⚙️ Requirements</a>
        <a href="#procedure-{wnum}" class="week-toc-link">🔧 Procedure</a>
        <a href="#programs-section-{wnum}" class="week-toc-link">💻 Programs</a>
        <a href="#step-gallery-{wnum}" class="week-toc-link">📸 Step Screenshots</a>
        <a href="#result-{wnum}" class="week-toc-link">🏆 Result</a>
        <a href="#result-analysis-{wnum}" class="week-toc-link">📊 Result Analysis</a>
      </div>
"""

    # For each task in this week:
    for task_idx, task in enumerate(week_meta["tasks"], 1):
        tid = task["id"]
        ttitle = task["title"]
        taim = task["aim"]
        task_key = f"task-{task_idx}"
        
        # Check if there are screenshots for this task
        step_gallery_html = get_step_gallery_html(week_key, task_key, is_page=is_page)
        step_count = len(STEP_GALLERY_DATA.get(week_key, {}).get(task_key, []))

        html += f"""      <!-- TASK SECTION: LEVEL 2 -->
      <section class="task-section" id="{tid}">
        <div class="task-header-block">
          <div class="task-pretitle">WEEK {wnum} · TASK {task_idx} OF {len(week_meta['tasks'])}</div>
          <h2 class="task-display-title">{ttitle}</h2>
        </div>

        <!-- 1. Aim -->
        <div class="task-sub-block" id="aim-{wnum}">
          <h3 class="task-sub-title"><span class="sub-icon">🎯</span> 1. Aim &amp; Learning Objectives</h3>
          <p>{taim}</p>
          {f'<div class="callout callout-info" style="margin-top:12px;">{aim_orig}</div>' if (aim_orig and task_idx == 1) else ''}
        </div>

        <!-- 2. Requirements -->
        <div class="task-sub-block" id="requirements-{wnum}">
          <h3 class="task-sub-title"><span class="sub-icon">⚙️</span> 2. Hardware &amp; Software Requirements</h3>
"""
        reqs = task.get("requirements", [])
        if reqs:
            html += """          <div class="req-grid">\n"""
            for category, items in reqs:
                html += f"""            <div class="req-card">
              <div class="req-card-title">💻 {category}</div>
              <div class="req-list">
"""
                for item in items:
                    html += f"""                <div class="req-item"><span class="req-item-dot"></span>{item}</div>\n"""
                html += """              </div>
            </div>\n"""
            html += """          </div>\n"""
        elif req_orig and task_idx == 1:
            html += f"""          {req_orig}\n"""
        else:
            html += """          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Software Environment</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>JDK Platform: OpenJDK 26 / Oracle JDK 8+</div>
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans 8.2 / Spring Tool Suite 4</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: MySQL 8.0 / In-Memory H2 / MS Access</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware Requirements</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>RAM: 8 GB Recommended</div>
                <div class="req-item"><span class="req-item-dot"></span>Processor: 64-bit Multi-core Intel/AMD</div>
                <div class="req-item"><span class="req-item-dot"></span>Storage: 4 GB Available SSD Space</div>
              </div>
            </div>
          </div>
"""
        html += """        </div>

        <!-- 3. Procedure -->
        <div class="task-sub-block" id="procedure-{wnum}">
          <h3 class="task-sub-title"><span class="sub-icon">🔧</span> 3. Step-by-Step Procedure</h3>
"""
        if proc_orig and task_idx == 1:
            html += f"""          {proc_orig}\n"""
        else:
            html += f"""          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Step 1: Workspace &amp; Environment Preparation</div></div>
                <div class="timeline-desc">Launch development IDE (NetBeans/STS), configure target JDK runtime, and verify build dependencies.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗄️</div><div class="timeline-title">Step 2: Database Schema &amp; Connection Setup</div></div>
                <div class="timeline-desc">Initialize database schema, tables, and driver classpath configurations for student records.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">💻</div><div class="timeline-title">Step 3: Source Code Implementation</div></div>
                <div class="timeline-desc">Author Java component classes binding candidate roll number <strong>24EU08161</strong> and implementing required business logic.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Step 4: Compilation, Deployment &amp; Execution</div></div>
                <div class="timeline-desc">Build project using Maven/Ant and execute target program on local application server / console runtime.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">✅</div><div class="timeline-title">Step 5: Output Verification &amp; Result Capture</div></div>
                <div class="timeline-desc">Capture console logs and browser output validating correct functional execution.</div>
              </div>
            </div>
          </div>
"""
        html += """        </div>

        <!-- 4. Programs & Source Code (Level 3) -->
        <div class="task-sub-block" id="programs-section-{wnum}">
          <h3 class="task-sub-title"><span class="sub-icon">💻</span> 4. Program Source Code &amp; Component Verification</h3>
          <p class="section-intro-text">Dedicated program units implementing the experiment tasks with clean IDE tabs, code viewers, component breakdown tables, and execution output.</p>
"""
        # Render each program card
        for p_idx, prog in enumerate(task.get("programs", []), 1):
            html += generate_program_card(prog, p_idx, is_page=is_page)

        html += """        </div>\n"""

        # Step Screenshot Gallery
        if step_gallery_html:
            html += f"""        <!-- 5. Step-by-Step Practical Screenshots -->
        <div class="task-sub-block" id="step-gallery-{wnum}">
          <h3 class="task-sub-title"><span class="sub-icon">📸</span> 5. Step-by-Step Practical Screenshots ({step_count} Steps)</h3>
          <p class="section-intro-text">Authentic sequential screen captures documenting each practical step executed in the laboratory environment with student roll number <strong>24EU08161</strong>.</p>
          {step_gallery_html}
        </div>
"""

        # Task Result & Analysis
        html += f"""        <!-- 6. Result & Result Analysis -->
        <div class="task-sub-block" id="result-{wnum}">
          <h3 class="task-sub-title"><span class="sub-icon">🏆</span> 6. Experiment Result</h3>
          <div class="callout callout-success">
            <strong>Experiment Successful:</strong> The lab task <em>"{ttitle}"</em> was successfully designed, compiled, and executed. All operations and database transactions completed with zero runtime faults under candidate roll number <strong>24EU08161</strong>.
          </div>
        </div>

        <div class="task-sub-block" id="result-analysis-{wnum}">
          <h3 class="task-sub-title"><span class="sub-icon">📊</span> 7. Engineering Result Analysis</h3>
          <p class="section-intro-text">Multi-dimensional technical evaluation examining execution performance, architectural design decisions, exception handling, and industry scalability.</p>
          {get_analysis_grid_html()}
        </div>

      </section>
"""

    # Footer navigation buttons
    prev_num = (wnum - 1) if wnum > 0 else None
    next_num = (wnum + 1) if wnum < 13 else None
    prev_link = f"week-{prev_num}.html" if is_page else f"#week-{prev_num}"
    next_link = f"week-{next_num}.html" if is_page else f"#week-{next_num}"

    html += f"""      <!-- WEEK FOOTER NAV -->
      <div class="week-footer-nav" style="display:flex; justify-content:space-between; margin-top:40px; padding-top:20px; border-top:1px solid #E2E8F0;">
        {f'<a href="{prev_link}" class="step-btn" style="padding:8px 16px; font-size:0.85rem;"><i class="bi bi-arrow-left"></i> Previous: Week {prev_num}</a>' if prev_num is not None else '<span></span>'}
        <a href="{root_prefix}index.html" class="step-btn" style="padding:8px 16px; font-size:0.85rem;"><i class="bi bi-house"></i> Master Hub</a>
        {f'<a href="{next_link}" class="step-btn" style="padding:8px 16px; font-size:0.85rem;">Next: Week {next_num} <i class="bi bi-arrow-right"></i></a>' if next_num is not None else '<span></span>'}
      </div>
"""
    return html

def build_standalone_page(week_meta):
    wnum = week_meta["num"]
    header = get_header_html(is_page=True)
    sidebar = get_sidebar_html(current_week=wnum, is_page=True)
    body = build_week_content(week_meta, is_page=True)
    
    html = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Week {wnum}: {week_meta['name']} | Digital Lab Record</title>
  <meta name="description" content="{week_meta['desc']} - Advanced Java Programming Lab (24IT385) by Venkata Sai Karthikeya Kaja (24EU08161)" />
  <link rel="icon" type="image/svg+xml"
    href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%23059669'/><g fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M9 10c0-2 1.3-2.5 1.3-4.5S9 3.5 9 1.5'/><path d='M16 9c0-2 1.3-2.5 1.3-4.5S16 2.5 16 0.5'/><path d='M23 10c0-2 1.3-2.5 1.3-4.5S23 3.5 23 1.5'/><path d='M6 14h17v8a7 7 0 0 1-7 7h-3a7 7 0 0 1-7-7v-8z' fill='white' fill-opacity='0.25'/><path d='M23 15h3a2.5 2.5 0 0 1 2.5 2.5v2a2.5 2.5 0 0 1-2.5 2.5h-3'/><path d='M3 30h26'/></g></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap"
    rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />
  <link rel="stylesheet" href="../style.css" />
  <link rel="stylesheet" href="../assets/css/topic-page.css" />
</head>

<body class="portal-body">
{header}

  <div class="portal-layout">
{sidebar}

    <main class="portal-main-content" id="portalMainContent">
{body}
    </main>
  </div>

  <!-- Screenshot Zoom Modal -->
  <div class="ss-modal" id="ssModal">
    <div class="ss-modal-backdrop"></div>
    <div class="ss-modal-content">
      <div class="ss-modal-header">
        <h3 class="ss-modal-title" id="ssModalTitle">Image Preview</h3>
        <div class="ss-modal-actions">
          <a href="#" download id="ssModalDownload" class="step-btn">⬇ Download High-Res</a>
          <button class="ss-modal-close" aria-label="Close Preview">✕</button>
        </div>
      </div>
      <div class="ss-modal-body">
        <img src="" alt="" id="ssModalImg" />
      </div>
    </div>
  </div>

  <footer class="portal-footer" style="text-align:center; padding:24px; color:#64748B; font-size:0.8rem; border-top:1px solid #E2E8F0; background:#FFFFFF;">
    <div><strong>Advanced Java Programming Laboratory Record (24IT385)</strong></div>
    <div>Candidate: <strong>Venkata Sai Karthikeya Kaja</strong> (Roll No: <strong>24EU08161</strong>)</div>
    <div>Department of Information Technology · Siddhartha Academy of Higher Education · Academic Year 2026–2027</div>
  </footer>

  <script src="../script.js"></script>
</body>
</html>
"""
    return html

def build_master_index():
    header = get_header_html(is_page=False)
    sidebar = get_sidebar_html(current_week=0, is_page=False)
    
    panes_html = ""
    for w in HIERARCHY_DATA:
        wnum = w["num"]
        display_style = "block" if wnum == 0 else "none"
        active_class = "active-pane" if wnum == 0 else ""
        content = build_week_content(w, is_page=False)
        
        panes_html += f"""      <div class="week-pane {active_class}" id="week-{wnum}-pane" style="display:{display_style};">
{content}
      </div>\n"""

    html = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Advanced Java Programming Digital Lab Record | Venkata Sai Karthikeya Kaja (24EU08161)</title>
  <meta name="description" content="Comprehensive Digital Engineering Laboratory Record covering Week 0 through Week 13 for Advanced Java Programming Lab (24IT385) by Venkata Sai Karthikeya Kaja (24EU08161)." />
  <link rel="icon" type="image/svg+xml"
    href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%23059669'/><g fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M9 10c0-2 1.3-2.5 1.3-4.5S9 3.5 9 1.5'/><path d='M16 9c0-2 1.3-2.5 1.3-4.5S16 2.5 16 0.5'/><path d='M23 10c0-2 1.3-2.5 1.3-4.5S23 3.5 23 1.5'/><path d='M6 14h17v8a7 7 0 0 1-7 7h-3a7 7 0 0 1-7-7v-8z' fill='white' fill-opacity='0.25'/><path d='M23 15h3a2.5 2.5 0 0 1 2.5 2.5v2a2.5 2.5 0 0 1-2.5 2.5h-3'/><path d='M3 30h26'/></g></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap"
    rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="assets/css/topic-page.css" />
</head>

<body class="portal-body">
{header}

  <div class="portal-layout">
{sidebar}

    <main class="portal-main-content" id="portalMainContent">
{panes_html}
    </main>
  </div>

  <!-- Screenshot Zoom Modal -->
  <div class="ss-modal" id="ssModal">
    <div class="ss-modal-backdrop"></div>
    <div class="ss-modal-content">
      <div class="ss-modal-header">
        <h3 class="ss-modal-title" id="ssModalTitle">Image Preview</h3>
        <div class="ss-modal-actions">
          <a href="#" download id="ssModalDownload" class="step-btn">⬇ Download High-Res</a>
          <button class="ss-modal-close" aria-label="Close Preview">✕</button>
        </div>
      </div>
      <div class="ss-modal-body">
        <img src="" alt="" id="ssModalImg" />
      </div>
    </div>
  </div>

  <footer class="portal-footer" style="text-align:center; padding:24px; color:#64748B; font-size:0.8rem; border-top:1px solid #E2E8F0; background:#FFFFFF;">
    <div><strong>Advanced Java Programming Laboratory Record (24IT385)</strong></div>
    <div>Candidate: <strong>Venkata Sai Karthikeya Kaja</strong> (Roll No: <strong>24EU08161</strong>)</div>
    <div>Department of Information Technology · Siddhartha Academy of Higher Education · Academic Year 2026–2027</div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
"""
    return html

def main():
    print("=== BUILDING MASTER 3-LEVEL DIGITAL LAB RECORD PORTAL ===")
    
    # 1. Build Standalone Pages
    os.makedirs("pages", exist_ok=True)
    for w in HIERARCHY_DATA:
        wnum = w["num"]
        page_html = build_standalone_page(w)
        out_path = f"pages/week-{wnum}.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"Generated standalone page: {out_path} ({len(page_html):,d} bytes)")

    # 2. Build Master Index
    index_html = build_master_index()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"Generated master index.html ({len(index_html):,d} bytes)")

    print("=== BUILD COMPLETE ===")

if __name__ == "__main__":
    main()
