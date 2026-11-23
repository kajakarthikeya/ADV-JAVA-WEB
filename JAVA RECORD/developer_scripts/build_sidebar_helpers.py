# -*- coding: utf-8 -*-
"""
Master Builder for Week-Wise Sidebar Navigation & Step-by-Step Galleries
Course: 24IT385 · Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os
import re
from step_gallery_data import STEP_GALLERY_DATA

WEEKS_META = [
    {
        "num": 0,
        "title": "Intro & Theory",
        "full_title": "Advanced Java Introduction and Theory",
        "category": "Core & Theory",
        "desc": "JVM Architecture, Core vs Enterprise Java, Applets vs Servlets, JDBC vs ODBC, Cookies & Sessions, Spring Boot vs Spring Framework.",
        "tasks": [
            ("week-0-task-1", "Task 1: Introduction to Advanced Java"),
            ("week-0-task-2", "Task 2: Core Java vs Advanced Java"),
            ("week-0-task-3", "Task 3: Java Applets and Servlets"),
            ("week-0-task-4", "Task 4: JDBC and ODBC"),
            ("week-0-task-5", "Task 5: Cookies and Sessions")
        ]
    },
    {
        "num": 1,
        "title": "Language Paradigms",
        "full_title": "Comparative Evaluation of Java, C, C++, Python & JS",
        "category": "Paradigms & Lab 1",
        "desc": "Comparative benchmark matrices evaluating type systems, compilation models, concurrency paradigms, and runtime environments.",
        "tasks": [
            ("week-1-task-1", "Task 1: Advanced Java Lab Assignment")
        ]
    },
    {
        "num": 2,
        "title": "Environment Setup",
        "full_title": "Downloading & Installing OpenJDK SE 26 in Ubuntu",
        "category": "Linux & JDK Setup",
        "desc": "Installation, compilation, and environment variable configuration (JAVA_HOME, PATH, update-alternatives) on Ubuntu Linux.",
        "tasks": [
            ("week-2-task-1", "Task 1: Downloading, Installing and Configuring OpenJDK and Oracle JDK 26 in Ubuntu")
        ]
    },
    {
        "num": 3,
        "title": "MS Access JDBC",
        "full_title": "Java MS Access Database Connectivity via UCanAccess",
        "category": "Type 4 Bridge",
        "desc": "Pure-Java Type 4 bridge architecture connecting Java to Microsoft Access (.accdb) using UCanAccess and Jackcess libraries.",
        "tasks": [
            ("week-3-task-1", "Task 1: Java MS Access Connectivity Using UCanAccess")
        ]
    },
    {
        "num": 4,
        "title": "Remote MySQL",
        "full_title": "Remote MySQL Database Connectivity & CRUD",
        "category": "Client-Server JDBC",
        "desc": "Client-server database communication across remote subnets executing parameterized DDL and DML operations.",
        "tasks": [
            ("week-4-task-1", "Task 1: Remote MySQL Database Connectivity")
        ]
    },
    {
        "num": 5,
        "title": "MySQL Operations",
        "full_title": "Remote MySQL Database Operations & Transactions",
        "category": "Remote Database",
        "desc": "PreparedStatement batch operations, parameter binding, connection pooling, and transactional commit semantics.",
        "tasks": [
            ("week-5-task-1", "Task 1: Remote MySQL Database Operations")
        ]
    },
    {
        "num": 6,
        "title": "JDBC CRUD",
        "full_title": "JDBC Program to Perform CRUD Operations on Student Database",
        "category": "Full CRUD",
        "desc": "Comprehensive Create, Read, Update, and Delete operations on MySQL student database with roll number 24EU08161.",
        "tasks": [
            ("week-6-task-1", "Task 1: JDBC CRUD Operations on Student Database")
        ]
    },
    {
        "num": 7,
        "title": "Servlets & NetBeans",
        "full_title": "Generic Servlet and HTTP Servlet in NetBeans",
        "category": "Servlets & Web",
        "desc": "Modular Java Web Applications on Apache Tomcat implementing GenericServlet, HttpServlet, GET/POST handlers, and dynamic forms.",
        "tasks": [
            ("week-7-task-1", "Task 1: NetBeans Web Application Creation & index.html"),
            ("week-7-task-2", "Task 2: HTTP Servlet Rendering Student Details (24EU08161)"),
            ("week-7-task-3", "Task 3: HTTP GET & POST Servlet Handling"),
            ("week-7-task-4", "Task 4: Generic Servlet Implementation"),
            ("week-7-task-5", "Task 5: Servlet Life Cycle Demonstration"),
            ("week-7-task-6", "Task 6: Interactive Student Registration Form")
        ]
    },
    {
        "num": 8,
        "title": "Web Apps & Cookies",
        "full_title": "Advanced Java Web Applications & Cookie Tracking",
        "category": "Multi-tier Web",
        "desc": "Multi-tier Student Management System using Servlets, JDBC, and MySQL, alongside client-side HTTP Cookie session state management.",
        "tasks": [
            ("week-8-task-1", "Task 1: Student Management System using Servlets, JDBC and MySQL"),
            ("week-8-task-2", "Task 2: Cookies Demonstration Using Java Servlets")
        ]
    },
    {
        "num": 9,
        "title": "Maven & Spring Boot",
        "full_title": "Maven & Spring Boot Application Development in STS",
        "category": "Spring Boot & STS",
        "desc": "Spring Starter Project wizard, dependency resolution via POM.xml, embedded Tomcat orchestration, and Maven lifecycle management.",
        "tasks": [
            ("week-9-task-1", "Task 1: Steps to Build Maven & Spring Boot in STS"),
            ("week-9-task-2", "Task 2: Develop Simple Spring Boot Web App"),
            ("week-9-task-3", "Task 3: POM.xml Configuration")
        ]
    },
    {
        "num": 10,
        "title": "JdbcTemplate & H2",
        "full_title": "Spring Boot Database Connectivity with JdbcTemplate & H2",
        "category": "In-Memory JDBC",
        "desc": "Spring JdbcTemplate architecture with embedded H2 database, @PostConstruct initialization, batch updates, and H2 Web Console.",
        "tasks": [
            ("week-10-task-1", "Task 1: Spring Boot JdbcTemplate with In-Memory H2")
        ]
    },
    {
        "num": 11,
        "title": "JPA with MySQL",
        "full_title": "Spring Boot JPA Application with MySQL & Thymeleaf UI",
        "category": "ORM & MySQL",
        "desc": "Spring Data JPA entity mapping, Hibernate ORM DDL automation, MySQL database persistence, RESTful API, and Thymeleaf web presentation.",
        "tasks": [
            ("week-11-task-1", "Task 1: Spring Boot JPA with MySQL & Web Interface")
        ]
    },
    {
        "num": 12,
        "title": "Spring Data JPA & H2",
        "full_title": "Spring Data JPA Repository Operations with In-Memory H2",
        "category": "Spring Data JPA",
        "desc": "JpaRepository CRUD abstraction with in-memory H2 database, REST controller endpoint ingestion, and web console validation.",
        "tasks": [
            ("week-12-task-1", "Task 1: Spring Data JPA Repository Operations with H2")
        ]
    },
    {
        "num": 13,
        "title": "Derived & Custom Queries",
        "full_title": "Derived and Custom Query Methods in Spring Data JPA",
        "category": "JPA Query Methods",
        "desc": "Automated query derivation from method signatures, compound AND/OR expressions, OrderBy clauses, and custom native SQL @Query.",
        "tasks": [
            ("week-13-task-1", "Task 1: Derived and Custom Query Methods in Spring Data JPA")
        ]
    }
]

def get_header_html(is_page=True):
    root_prefix = "../" if is_page else ""
    return f"""  <!-- TOP HEADER -->
  <header class="main-portal-header">
    <div class="header-top-bar">
      <div class="header-student-pill">
        <span class="student-avatar">👨‍🎓</span>
        <div class="student-pill-info">
          <span class="student-name">Venkata Sai Karthikeya Kaja</span>
          <span class="student-dept">IT · Siddhartha Academy of Higher Education</span>
        </div>
      </div>
      <div class="header-center-branding">
        <h1 class="header-main-title">ADVANCED JAVA PROGRAMMING</h1>
        <div class="header-roll-sub">Roll Number: <span class="roll-badge">24EU08161</span></div>
      </div>
      <div class="header-right-tools">
        <a href="{root_prefix}index.html" class="header-tool-btn">🏠 Home Hub</a>
        <button class="sidebar-toggle-btn" id="sidebarToggleBtn" aria-label="Toggle Week Navigation">
          <i class="bi bi-layout-sidebar-inset"></i> <span>Weeks</span>
        </button>
      </div>
    </div>
  </header>"""

def get_sidebar_html(current_week=0, is_page=True):
    root_prefix = "../" if is_page else ""
    pages_prefix = "" if is_page else "pages/"
    
    html = f"""    <!-- LEFT SIDEBAR: WEEK-WISE NAVIGATION -->
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
        is_active = (num == current_week)
        active_cls = "active open" if is_active else ""
        if not is_page:
            pane_link = f"#week-{num}"
            link_attrs = f'href="{pane_link}" class="sidebar-week-link" data-week="{num}" data-week-target="week-{num}-pane"'
        else:
            pane_link = f"week-{num}.html"
            link_attrs = f'href="{pane_link}" class="sidebar-week-link" data-week="{num}"'

        html += f"""        <div class="sidebar-week-group {active_cls}" data-week="{num}">
          <a {link_attrs}>
            <span class="week-pill">W{num}</span>
            <span class="week-title-text">{w['title']}</span>
            <span class="week-arrow">›</span>
          </a>
          <div class="sidebar-task-list">
"""
        for tid, ttitle in w["tasks"]:
            if not is_page:
                html += f"""            <a href="#{tid}" class="sidebar-task-link" data-week="{num}" data-week-target="week-{num}-pane" data-task-anchor="{tid}" title="{ttitle}">{ttitle}</a>\n"""
            else:
                task_href = f"#{tid}" if is_active else f"week-{num}.html#{tid}"
                html += f"""            <a href="{task_href}" class="sidebar-task-link" data-week="{num}" data-task-anchor="{tid}" title="{ttitle}">{ttitle}</a>\n"""
        html += f"""          </div>
        </div>\n"""
        
    html += """      </nav>
    </aside>"""
    return html

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
              </div>
            </div>\n"""
    html += "          </div>"
    return html

print("Helper templates and gallery generators ready.")

