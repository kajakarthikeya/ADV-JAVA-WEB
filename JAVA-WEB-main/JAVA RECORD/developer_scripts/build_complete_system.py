# -*- coding: utf-8 -*-
"""
Complete System Builder:
1. Generates 14 Week Pages with Centered Top Header, Left Sidebar, Week/Task Hierarchy, and Step Galleries.
2. Generates Master index.html with Centered Top Header, Left Sidebar, and Dynamic Week Switcher.
"""

import os
import re
from build_sidebar_helpers import WEEKS_META, get_header_html, get_sidebar_html, get_step_gallery_html
from step_gallery_data import STEP_GALLERY_DATA

def extract_section_content(html, section_id):
    # Regex to get inner HTML of section
    m = re.search(r'<section class="content-section" id="' + section_id + r'">([\s\S]*?)</section>', html)
    if m:
        content = m.group(1).strip()
        # Remove old section title since our task block provides the proper hierarchical heading
        content = re.sub(r'<h2 class="content-section-title.*?</h2>', '', content, count=1).strip()
        return content
    return ""

def build_single_task_week(week_num, meta, original_html):
    week_key = f"week-{week_num}"
    task_key = "task-1"
    task_title = meta["tasks"][0][1]
    
    aim_content = extract_section_content(original_html, "aim")
    req_content = extract_section_content(original_html, "requirements")
    proc_content = extract_section_content(original_html, "procedure")
    prog_content = extract_section_content(original_html, "program")
    out_content = extract_section_content(original_html, "output")
    res_an_content = extract_section_content(original_html, "result-analysis")
    conclusion_content = extract_section_content(original_html, "result")
    
    # Step gallery
    step_gallery_html = get_step_gallery_html(week_key, task_key, is_page=True)
    step_count = len(STEP_GALLERY_DATA.get(week_key, {}).get(task_key, []))
    
    html = f"""
      <div class="week-main-header">
        <div class="week-super-meta">
          <span class="week-number-badge">WEEK {week_num:02d}</span>
          <span class="week-category-tag">{meta['category']}</span>
          <span class="week-roll-tag">Roll: 24EU08161</span>
        </div>
        <h1 class="week-display-title">WEEK {week_num}: {meta['full_title'].upper()}</h1>
        <p class="week-overview-desc">{meta['desc']}</p>
      </div>

      <section class="task-section" id="{week_key}-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">WEEK {week_num} · PRACTICAL EXPERIMENT</div>
          <h2 class="task-display-title">{task_title}</h2>
        </div>

        <div class="task-sub-block" id="aim">
          <h3 class="task-sub-title"><span class="sub-icon">🎯</span> 1. Aim</h3>
          {aim_content}
        </div>

        <div class="task-sub-block" id="requirements">
          <h3 class="task-sub-title"><span class="sub-icon">⚙️</span> 2. Software Requirements</h3>
          {req_content}
        </div>

        <div class="task-sub-block" id="procedure">
          <h3 class="task-sub-title"><span class="sub-icon">🔧</span> 3. Step-by-Step Procedure</h3>
          {proc_content}
        </div>

        <div class="task-sub-block" id="program">
          <h3 class="task-sub-title"><span class="sub-icon">💻</span> 4. Program &amp; IDE Source Code Verification</h3>
          {prog_content}
        </div>

        <div class="task-sub-block" id="output">
          <h3 class="task-sub-title"><span class="sub-icon">📟</span> 5. Execution Output &amp; Verification</h3>
          {out_content}
        </div>
"""
    if step_gallery_html:
        html += f"""
        <div class="task-sub-block" id="step-gallery">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> 6. Step-by-Step Practical Screenshot Gallery ({step_count} Steps)</h3>
          <p style="font-size:0.84rem;color:#64748B;margin-bottom:14px;">Every individual setup, coding, compilation, database, and execution step documented chronologically:</p>
          {step_gallery_html}
        </div>
"""
    if res_an_content:
        html += f"""
        <div class="task-sub-block" id="result-analysis">
          <h3 class="task-sub-title"><span class="sub-icon">📊</span> 7. Result Analysis &amp; Technical Discussion</h3>
          {res_an_content}
        </div>
"""
    if conclusion_content:
        html += f"""
        <div class="task-sub-block" id="result">
          <h3 class="task-sub-title"><span class="sub-icon">🏁</span> 8. Conclusion &amp; Result</h3>
          {conclusion_content}
        </div>
"""
    html += """      </section>\n"""
    return html

def build_week_0(original_html):
    meta = WEEKS_META[0]
    aim_content = extract_section_content(original_html, "aim")
    req_content = extract_section_content(original_html, "requirements")
    proc_content = extract_section_content(original_html, "procedure")
    prog_content = extract_section_content(original_html, "program")
    out_content = extract_section_content(original_html, "output")
    res_an_content = extract_section_content(original_html, "result-analysis")
    qa_content = extract_section_content(original_html, "qa-matrix")
    conclusion_content = extract_section_content(original_html, "result")

    return f"""
      <div class="week-main-header">
        <div class="week-super-meta">
          <span class="week-number-badge">WEEK 00</span>
          <span class="week-category-tag">{meta['category']}</span>
          <span class="week-roll-tag">Roll: 24EU08161</span>
        </div>
        <h1 class="week-display-title">WEEK 0: ADVANCED JAVA INTRODUCTION &amp; THEORY</h1>
        <p class="week-overview-desc">{meta['desc']}</p>
      </div>

      <!-- Task 1 -->
      <section class="task-section" id="week-0-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">WEEK 0 · THEORETICAL MODULE</div>
          <h2 class="task-display-title">Task 1: Introduction to Advanced Java Architecture &amp; Foundations</h2>
        </div>
        <div class="task-sub-block" id="aim">
          <h3 class="task-sub-title"><span class="sub-icon">🎯</span> 1. Aim</h3>
          {aim_content}
        </div>
        <div class="task-sub-block" id="requirements">
          <h3 class="task-sub-title"><span class="sub-icon">⚙️</span> 2. Hardware &amp; Software Specifications</h3>
          {req_content}
        </div>
      </section>

      <!-- Task 2 -->
      <section class="task-section" id="week-0-task-2">
        <div class="task-header-block">
          <div class="task-pretitle">WEEK 0 · COMPARATIVE ARCHITECTURE</div>
          <h2 class="task-display-title">Task 2: Core Java vs Advanced Java Paradigm Comparison</h2>
        </div>
        <div class="task-sub-block" id="procedure">
          <h3 class="task-sub-title"><span class="sub-icon">🔧</span> Architectural Analysis &amp; Theoretical Evaluation</h3>
          {proc_content}
        </div>
      </section>

      <!-- Task 3 -->
      <section class="task-section" id="week-0-task-3">
        <div class="task-header-block">
          <div class="task-pretitle">WEEK 0 · WEB ENGINE CONCEPTS</div>
          <h2 class="task-display-title">Task 3: Java Applets vs Java Servlets</h2>
        </div>
        <div class="task-sub-block" id="program">
          <h3 class="task-sub-title"><span class="sub-icon">💻</span> Architectural Framework &amp; Lifecycle Implementation</h3>
          {prog_content}
        </div>
      </section>

      <!-- Task 4 & 5 -->
      <section class="task-section" id="week-0-task-4">
        <div class="task-header-block">
          <div class="task-pretitle">WEEK 0 · DATABASE &amp; SESSION STATE</div>
          <h2 class="task-display-title">Task 4: JDBC vs ODBC &amp; Task 5: Cookies vs Sessions</h2>
        </div>
        <div class="task-sub-block" id="output">
          <h3 class="task-sub-title"><span class="sub-icon">📟</span> Execution Models &amp; Runtime Verification</h3>
          {out_content}
        </div>
        <div class="task-sub-block" id="result-analysis">
          <h3 class="task-sub-title"><span class="sub-icon">📊</span> Result Analysis &amp; Technical Discussion</h3>
          {res_an_content}
        </div>
        <div class="task-sub-block" id="qa-matrix">
          <h3 class="task-sub-title"><span class="sub-icon">📋</span> Comprehensive Week 0 Q&amp;A Evaluation</h3>
          {qa_content}
        </div>
        <div class="task-sub-block" id="result">
          <h3 class="task-sub-title"><span class="sub-icon">🏁</span> Conclusion</h3>
          {conclusion_content}
        </div>
      </section>
"""

def build_week_7(original_html):
    meta = WEEKS_META[7]
    aim_content = extract_section_content(original_html, "aim")
    req_content = extract_section_content(original_html, "requirements")
    proc_content = extract_section_content(original_html, "procedure")
    act1 = extract_section_content(original_html, "activity-1")
    act2 = extract_section_content(original_html, "activity-2")
    act3 = extract_section_content(original_html, "activity-3")
    act4 = extract_section_content(original_html, "activity-4")
    act5 = extract_section_content(original_html, "activity-5")
    act6 = extract_section_content(original_html, "activity-6")
    res_an = extract_section_content(original_html, "result-analysis")
    gallery = extract_section_content(original_html, "screenshots")
    conclusion = extract_section_content(original_html, "result")

    return f"""
      <div class="week-main-header">
        <div class="week-super-meta">
          <span class="week-number-badge">WEEK 07</span>
          <span class="week-category-tag">{meta['category']}</span>
          <span class="week-roll-tag">Roll: 24EU08161</span>
        </div>
        <h1 class="week-display-title">WEEK 7: GENERIC SERVLET AND HTTP SERVLET</h1>
        <p class="week-overview-desc">{meta['desc']}</p>
      </div>

      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">LAB OVERVIEW &amp; SETUP</div>
          <h2 class="task-display-title">Servlet Technology Foundations &amp; NetBeans Environment</h2>
        </div>
        <div class="task-sub-block" id="aim">
          <h3 class="task-sub-title"><span class="sub-icon">🎯</span> 1. Aim</h3>
          {aim_content}
        </div>
        <div class="task-sub-block" id="requirements">
          <h3 class="task-sub-title"><span class="sub-icon">⚙️</span> 2. Software Requirements</h3>
          {req_content}
        </div>
        <div class="task-sub-block" id="procedure">
          <h3 class="task-sub-title"><span class="sub-icon">🔧</span> 3. Step-by-Step Procedure</h3>
          {proc_content}
        </div>
      </div>

      <!-- Task 1 -->
      <section class="task-section" id="week-7-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 1</div>
          <h2 class="task-display-title">Task 1: NetBeans Web Application Creation &amp; index.html</h2>
        </div>
        {act1}
      </section>

      <!-- Task 2 -->
      <section class="task-section" id="week-7-task-2">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 2 · AUTHENTIC LAB PROOF (24EU08161)</div>
          <h2 class="task-display-title">Task 2: HTTP Servlet Rendering Student Details (24EU08161)</h2>
        </div>
        {act2}
      </section>

      <!-- Task 3 -->
      <section class="task-section" id="week-7-task-3">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 3</div>
          <h2 class="task-display-title">Task 3: HTTP GET &amp; POST Servlet Handling (GetPostServlet)</h2>
        </div>
        {act3}
      </section>

      <!-- Task 4 -->
      <section class="task-section" id="week-7-task-4">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 4</div>
          <h2 class="task-display-title">Task 4: Generic Servlet Implementation (MyGenericServlet)</h2>
        </div>
        {act4}
      </section>

      <!-- Task 5 -->
      <section class="task-section" id="week-7-task-5">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 5</div>
          <h2 class="task-display-title">Task 5: Servlet Life Cycle Demonstration (LifeCycleServlet)</h2>
        </div>
        {act5}
      </section>

      <!-- Task 6 -->
      <section class="task-section" id="week-7-task-6">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 6</div>
          <h2 class="task-display-title">Task 6: Interactive Student Registration Form Processing (StudentFormServlet)</h2>
        </div>
        {act6}
      </section>

      <!-- Analysis & Gallery -->
      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">EVALUATION &amp; RESULTS</div>
          <h2 class="task-display-title">Technical Discussion &amp; Authentic 16-Figure Proof Gallery</h2>
        </div>
        <div class="task-sub-block" id="result-analysis">
          <h3 class="task-sub-title"><span class="sub-icon">📊</span> Result Analysis &amp; Technical Discussion</h3>
          {res_an}
        </div>
        <div class="task-sub-block" id="screenshots">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Authentic NetBeans &amp; Browser Screenshot Gallery (16 Figures)</h3>
          {gallery}
        </div>
        <div class="task-sub-block" id="result">
          <h3 class="task-sub-title"><span class="sub-icon">🏁</span> Conclusion</h3>
          {conclusion}
        </div>
      </div>
"""

def build_week_8(original_html):
    meta = WEEKS_META[8]
    aim_content = extract_section_content(original_html, "aim")
    req_content = extract_section_content(original_html, "requirements")
    proc_content = extract_section_content(original_html, "procedure")
    prog_content = extract_section_content(original_html, "program")
    out_content = extract_section_content(original_html, "output")
    res_an = extract_section_content(original_html, "result-analysis")
    conclusion = extract_section_content(original_html, "result")
    
    t1_gallery = get_step_gallery_html("week-8", "task-1", is_page=True)
    t2_gallery = get_step_gallery_html("week-8", "task-2", is_page=True)

    return f"""
      <div class="week-main-header">
        <div class="week-super-meta">
          <span class="week-number-badge">WEEK 08</span>
          <span class="week-category-tag">{meta['category']}</span>
          <span class="week-roll-tag">Roll: 24EU08161</span>
        </div>
        <h1 class="week-display-title">WEEK 8: ADVANCED JAVA WEB APPLICATIONS</h1>
        <p class="week-overview-desc">{meta['desc']}</p>
      </div>

      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">LAB OVERVIEW</div>
          <h2 class="task-display-title">Advanced Web Application Architecture</h2>
        </div>
        <div class="task-sub-block" id="aim">
          <h3 class="task-sub-title"><span class="sub-icon">🎯</span> 1. Aim</h3>
          {aim_content}
        </div>
        <div class="task-sub-block" id="requirements">
          <h3 class="task-sub-title"><span class="sub-icon">⚙️</span> 2. Software Requirements</h3>
          {req_content}
        </div>
        <div class="task-sub-block" id="procedure">
          <h3 class="task-sub-title"><span class="sub-icon">🔧</span> 3. Step-by-Step Procedure</h3>
          {proc_content}
        </div>
      </div>

      <!-- Task 1 -->
      <section class="task-section" id="week-8-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 1 · MULTI-TIER WEB APP</div>
          <h2 class="task-display-title">Task 1: Student Management System using Servlets, JDBC and MySQL</h2>
        </div>
        <div class="task-sub-block" id="program">
          <h3 class="task-sub-title"><span class="sub-icon">💻</span> Source Code &amp; Servlet Architecture</h3>
          {prog_content}
        </div>
        <div class="task-sub-block" id="step-gallery-1">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Student Management System (16 Steps)</h3>
          {t1_gallery}
        </div>
      </section>

      <!-- Task 2 -->
      <section class="task-section" id="week-8-task-2">
        <div class="task-header-block">
          <div class="task-pretitle">TASK 2 · STATE MANAGEMENT</div>
          <h2 class="task-display-title">Task 2: Cookies Demonstration Using Java Servlets</h2>
        </div>
        <div class="task-sub-block" id="output">
          <h3 class="task-sub-title"><span class="sub-icon">📟</span> Execution Output &amp; Cookie State Proof</h3>
          {out_content}
        </div>
        <div class="task-sub-block" id="step-gallery-2">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Cookie State Tracking (12 Steps)</h3>
          {t2_gallery}
        </div>
      </section>

      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">EVALUATION &amp; RESULTS</div>
          <h2 class="task-display-title">Result Analysis &amp; Academic Conclusion</h2>
        </div>
        <div class="task-sub-block" id="result-analysis">
          <h3 class="task-sub-title"><span class="sub-icon">📊</span> Result Analysis &amp; Technical Discussion</h3>
          {res_an}
        </div>
        <div class="task-sub-block" id="result">
          <h3 class="task-sub-title"><span class="sub-icon">🏁</span> Conclusion</h3>
          {conclusion}
        </div>
      </div>
"""

def build_week_9(original_html):
    meta = WEEKS_META[9]
    aim_content = extract_section_content(original_html, "aim")
    req_content = extract_section_content(original_html, "requirements")
    proc_content = extract_section_content(original_html, "procedure")
    act1 = extract_section_content(original_html, "activity-1")
    act2 = extract_section_content(original_html, "activity-2")
    act3 = extract_section_content(original_html, "activity-3")
    res_an = extract_section_content(original_html, "result-analysis")
    conclusion = extract_section_content(original_html, "result")
    
    t1_gallery = get_step_gallery_html("week-9", "task-1", is_page=True)
    t2_gallery = get_step_gallery_html("week-9", "task-2", is_page=True)
    t3_gallery = get_step_gallery_html("week-9", "task-3", is_page=True)

    return f"""
      <div class="week-main-header">
        <div class="week-super-meta">
          <span class="week-number-badge">WEEK 09</span>
          <span class="week-category-tag">{meta['category']}</span>
          <span class="week-roll-tag">Roll: 24EU08161</span>
        </div>
        <h1 class="week-display-title">WEEK 9: MAVEN AND SPRING BOOT DEVELOPMENT</h1>
        <p class="week-overview-desc">{meta['desc']}</p>
      </div>

      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">LAB OVERVIEW</div>
          <h2 class="task-display-title">Spring Boot &amp; Maven Foundations</h2>
        </div>
        <div class="task-sub-block" id="aim">
          <h3 class="task-sub-title"><span class="sub-icon">🎯</span> 1. Aim</h3>
          {aim_content}
        </div>
        <div class="task-sub-block" id="requirements">
          <h3 class="task-sub-title"><span class="sub-icon">⚙️</span> 2. Software Requirements</h3>
          {req_content}
        </div>
        <div class="task-sub-block" id="procedure">
          <h3 class="task-sub-title"><span class="sub-icon">🔧</span> 3. Step-by-Step Procedure</h3>
          {proc_content}
        </div>
      </div>

      <!-- Task 1 -->
      <section class="task-section" id="week-9-task-1">
        <div class="task-header-block">
          <div class="task-pretitle">ACTIVITY 1</div>
          <h2 class="task-display-title">Task 1: Steps to Build Maven + Spring Boot Application in STS</h2>
        </div>
        {act1}
        <div class="task-sub-block" id="step-gallery-1">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Maven + Spring Boot Setup (15 Steps)</h3>
          {t1_gallery}
        </div>
      </section>

      <!-- Task 2 -->
      <section class="task-section" id="week-9-task-2">
        <div class="task-header-block">
          <div class="task-pretitle">ACTIVITY 2</div>
          <h2 class="task-display-title">Task 2: Develop a Simple Spring Boot Web Application in STS</h2>
        </div>
        {act2}
        <div class="task-sub-block" id="step-gallery-2">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: Web Controller Development (12 Steps)</h3>
          {t2_gallery}
        </div>
      </section>

      <!-- Task 3 -->
      <section class="task-section" id="week-9-task-3">
        <div class="task-header-block">
          <div class="task-pretitle">ACTIVITY 3</div>
          <h2 class="task-display-title">Task 3: POM.xml Configuration and Dependency Management</h2>
        </div>
        {act3}
        <div class="task-sub-block" id="step-gallery-3">
          <h3 class="task-sub-title"><span class="sub-icon">📷</span> Step-by-Step Practical Gallery: POM.xml Configuration (12 Steps)</h3>
          {t3_gallery}
        </div>
      </section>

      <div class="task-section">
        <div class="task-header-block">
          <div class="task-pretitle">EVALUATION &amp; RESULTS</div>
          <h2 class="task-display-title">Result Analysis &amp; Academic Conclusion</h2>
        </div>
        <div class="task-sub-block" id="result-analysis">
          <h3 class="task-sub-title"><span class="sub-icon">📊</span> Result Analysis &amp; Technical Discussion</h3>
          {res_an}
        </div>
        <div class="task-sub-block" id="result">
          <h3 class="task-sub-title"><span class="sub-icon">🏁</span> Conclusion</h3>
          {conclusion}
        </div>
      </div>
"""

def assemble_page(week_num, body_content):
    meta = WEEKS_META[week_num]
    header_html = get_header_html(is_page=True)
    sidebar_html = get_sidebar_html(week_num, is_page=True)
    
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Week {week_num}: {meta['full_title']} | Lab Record</title>
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

{header_html}

  <div class="portal-layout">
{sidebar_html}

    <main class="portal-main-content" id="portalMainContent">
{body_content}
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
        <a href="../index.html" class="btn btn-secondary btn-sm" style="color:#F8FAFC;border-color:#334155;">🏠 Home Hub</a>
        <a href="../index.html#downloads" class="btn btn-secondary btn-sm" style="color:#F8FAFC;border-color:#334155;">⬇ All Downloads</a>
      </div>
    </div>
  </footer>

  <script src="../script.js"></script>
</body>
</html>
"""

print("Generating all 14 updated week pages...")

for num in range(14):
    fpath = f"pages/week-{num}.html"
    with open(fpath, "r", encoding="utf-8") as fp:
        orig = fp.read()
    
    meta = WEEKS_META[num]
    if num == 0:
        body = build_week_0(orig)
    elif num == 7:
        body = build_week_7(orig)
    elif num == 8:
        body = build_week_8(orig)
    elif num == 9:
        body = build_week_9(orig)
    else:
        body = build_single_task_week(num, meta, orig)
        
    full_html = assemble_page(num, body)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(full_html)
    print(f"Updated {fpath} with sidebar layout and step galleries!")

print("All 14 week pages rebuilt successfully!")

