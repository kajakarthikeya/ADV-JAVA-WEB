# -*- coding: utf-8 -*-
"""
Generator for Weeks 0 to 3
Advanced Java Programming Lab (24IT385)
Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os
from generate_base import get_page_header, get_page_footer

pages_dir = r'C:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\pages'

# ==============================================================================
# WEEK 0: Advanced Java Introduction and Theory
# ==============================================================================
def generate_week_0():
    header = get_page_header(
        0,
        "Advanced Java Introduction & Theoretical Foundations",
        "Comprehensive Q&A Analysis of Java Enterprise Architecture, Servlets, JDBC, and Frameworks",
        ["☕ Core vs Advanced", "🌐 Servlets & Applets", "🔌 JDBC & ODBC", "🍪 Cookies & Sessions", "🌱 Spring Boot Architecture"],
        "Core & Theory"
    )

    body = """
    <!-- CONTENT WRAPPER -->
    <div class="topic-content-wrap container">

      <!-- SIDEBAR TOC -->
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 0 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview</a>
          <a href="#q1" class="toc-item">3. Core vs Advanced Java</a>
          <a href="#q2" class="toc-item">4. Applets Features</a>
          <a href="#q3" class="toc-item">5. Servlets Features</a>
          <a href="#q4" class="toc-item">6. Applets vs Servlets</a>
          <a href="#q5" class="toc-item">7. Role of JDBC & ODBC</a>
          <a href="#q6" class="toc-item">8. ODBC vs JDBC</a>
          <a href="#q7" class="toc-item">9. Cookies vs Sessions</a>
          <a href="#q8" class="toc-item">10. Spring Boot vs Spring</a>
          <a href="#q9" class="toc-item">11. Standalone vs Web Apps</a>
          <a href="#q10" class="toc-item">12. Web App Requirements</a>
          <a href="#result" class="toc-item">13. Result & Conclusion</a>
        </nav>
      </aside>

      <!-- MAIN ARTICLE -->
      <article class="topic-main">

        <!-- 1. AIM -->
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim of the Study</h2>
          <p>
            To comprehensively investigate and articulate the fundamental principles, architectural differences, and technological progressions of enterprise Java programming, establishing a rigorous theoretical foundation for web-tier development, middleware connectivity, and modern microservices.
          </p>
        </section>

        <!-- 2. OVERVIEW -->
        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Architectural Overview</h2>
          <p>
            Java technology is architecturally divided into distinct editions tailored for varying computational domains: Java Standard Edition (Java SE / Core Java) and Java Enterprise Edition (Jakarta EE / Advanced Java). While Core Java provides foundational syntax, object-oriented semantics, standard collections, and basic I/O, Advanced Java equips developers with distributed communication, transaction management, server-side dynamic content generation, database pooling, and cloud-native frameworks.
          </p>
        </section>

        <!-- 3. QUESTION 1 -->
        <section class="content-section" id="q1">
          <h2 class="content-section-title"><span class="section-icon">❓</span> 3. Core Java vs. Advanced Java</h2>
          <p>
            <strong>Core Java</strong> is used for developing standalone desktop, console, and embedded applications. It encompasses fundamental OOP concepts, exception handling, multithreading, collections, file handling, and basic input/output streams without requiring a web container or server.
          </p>
          <p>
            <strong>Advanced Java</strong> is dedicated to enterprise-level, multi-tiered, and web-based applications. It encompasses Servlets, JavaServer Pages (JSP), JDBC, Spring Framework, Hibernate, Java Persistence API (JPA), and RESTful web services executing on application servers such as Apache Tomcat, WildFly, or GlassFish.
          </p>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Aspect</th>
                  <th>Core Java (Java SE)</th>
                  <th>Advanced Java (Jakarta EE / Enterprise)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Definition</strong></td>
                  <td>Basic general-purpose computing part of Java</td>
                  <td>Specialized enterprise, web, and distributed application platform</td>
                </tr>
                <tr>
                  <td><strong>Application Scope</strong></td>
                  <td>Standalone desktop, CLI, and utility applications</td>
                  <td>Web applications, enterprise ERP, banking, cloud microservices</td>
                </tr>
                <tr>
                  <td><strong>Core Focus Areas</strong></td>
                  <td>OOP, Memory Model, Collections, Multithreading, Exceptions</td>
                  <td>Database Connectivity, Servlets, JPA, Distributed Transactions, REST</td>
                </tr>
                <tr>
                  <td><strong>Packages Used</strong></td>
                  <td><code>java.lang</code>, <code>java.util</code>, <code>java.io</code>, <code>java.math</code></td>
                  <td><code>javax.servlet</code>, <code>jakarta.persistence</code>, <code>java.sql</code>, <code>org.springframework</code></td>
                </tr>
                <tr>
                  <td><strong>Server Requirement</strong></td>
                  <td>Runs directly on local JVM; no web server required</td>
                  <td>Requires Servlet Container (Tomcat) or Enterprise Application Server</td>
                </tr>
                <tr>
                  <td><strong>Learning Sequence</strong></td>
                  <td>Prerequisite baseline for all Java development</td>
                  <td>Subsequent specialization after mastering Core Java concepts</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 4. QUESTION 2 -->
        <section class="content-section" id="q2">
          <h2 class="content-section-title"><span class="section-icon">🖼️</span> 4. Key Features of Java Applets</h2>
          <p>
            Java Applets were client-side Java programs designed to run inside web browsers via a Java plugin. Historically significant for introducing interactive multimedia to the early Web, their principal features include:
          </p>
          <ul class="feature-list" style="margin-left:20px;line-height:1.8;">
            <li><strong>Browser & Viewer Execution:</strong> Executed within web browser viewports or the standalone JDK <code>appletviewer</code> utility.</li>
            <li><strong>JVM Platform Independence:</strong> Compiled to standard bytecode (.class) and executed across Windows, Mac, and Linux JVMs.</li>
            <li><strong>Sandbox Security Model:</strong> Confined within a restrictive client security sandbox preventing arbitrary local file system access or network port scanning.</li>
            <li><strong>AWT Graphical Interface:</strong> Utilized Abstract Window Toolkit (AWT) components for buttons, canvases, and mouse/keyboard event handling.</li>
            <li><strong>Automated Network Download:</strong> Transferred over HTTP and executed instantaneously on the client runtime.</li>
            <li><strong>Strict Lifecycle Callback Architecture:</strong> Managed via 5 distinct lifecycle methods: <code>init()</code>, <code>start()</code>, <code>paint()</code>, <code>stop()</code>, and <code>destroy()</code>.</li>
            <li><strong>Modern Deprecation:</strong> Deprecated in Java 9 and fully removed due to security vulnerabilities and the rise of HTML5/CSS3/JavaScript.</li>
          </ul>
        </section>

        <!-- 5. QUESTION 3 -->
        <section class="content-section" id="q3">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 5. Key Features of Java Servlets</h2>
          <p>
            Java Servlets represent the cornerstone of server-side Java web computing. Unlike client-bound applets, servlets execute inside a web container, intercepting HTTP client requests and delivering dynamic HTML, XML, or JSON responses:
          </p>
          <ul class="feature-list" style="margin-left:20px;line-height:1.8;">
            <li><strong>Server-Side Execution:</strong> Executed in a secure, controlled server environment with direct access to enterprise databases and services.</li>
            <li><strong>Multithreaded Performance Advantage:</strong> Unlike CGI (Common Gateway Interface) which spawned a heavyweight OS process for every request, servlets allocate lightweight threads within a single persistent JVM process.</li>
            <li><strong>State & Session Management:</strong> Built-in APIs for managing conversational state across multiple requests via <code>HttpSession</code>, cookies, and URL rewriting.</li>
            <li><strong>Database Integration:</strong> Native connectivity to relational databases through JDBC connection pools.</li>
            <li><strong>Platform & Container Portability:</strong> Compliant with standard servlet specifications (Servlet API 3.x/4.x/5.x/6.x), running portably on Apache Tomcat, Jetty, or JBoss.</li>
          </ul>
        </section>

        <!-- 6. QUESTION 4 -->
        <section class="content-section" id="q4">
          <h2 class="content-section-title"><span class="section-icon">⚖️</span> 6. Differences Between Applets and Servlets</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Attribute</th>
                  <th>Java Applets</th>
                  <th>Java Servlets</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Execution Location</strong></td>
                  <td>Client-side inside web browser or AppletViewer</td>
                  <td>Server-side inside a Servlet Container (e.g., Apache Tomcat)</td>
                </tr>
                <tr>
                  <td><strong>Primary Purpose</strong></td>
                  <td>Client UI rendering and user interaction</td>
                  <td>Business logic execution and dynamic response generation</td>
                </tr>
                <tr>
                  <td><strong>Security Model</strong></td>
                  <td>Confined to restricted client-side JVM Sandbox</td>
                  <td>Trusted server execution with access to backend resources & DB</td>
                </tr>
                <tr>
                  <td><strong>User Interface</strong></td>
                  <td>Graphical user interface built using AWT / Swing</td>
                  <td>No GUI; generates HTML, XML, or JSON output payloads</td>
                </tr>
                <tr>
                  <td><strong>Lifecycle Methods</strong></td>
                  <td><code>init()</code>, <code>start()</code>, <code>paint()</code>, <code>stop()</code>, <code>destroy()</code></td>
                  <td><code>init()</code>, <code>service()</code>, <code>destroy()</code></td>
                </tr>
                <tr>
                  <td><strong>Current Status</strong></td>
                  <td>Obsolete and removed from modern Java platforms</td>
                  <td>Widely used; foundational layer for Spring MVC and Jakarta EE</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 7. QUESTION 5 -->
        <section class="content-section" id="q5">
          <h2 class="content-section-title"><span class="section-icon">🔌</span> 7. Role of JDBC and ODBC in Database Connectivity</h2>
          <p>
            Database connectivity bridges programming code with persistent Relational Database Management Systems (RDBMS).
          </p>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">☕ JDBC (Java Database Connectivity)</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                JDBC is an industry-standard Java API (under <code>java.sql</code> and <code>javax.sql</code>) providing a uniform interface for Java applications to communicate with any relational database. It enables driver loading, physical connection establishment, SQL statement compilation, parameterized batch execution, result set traversal, and transaction control.
              </p>
            </div>
            <div class="req-card">
              <div class="req-card-title">🖥️ ODBC (Open Database Connectivity)</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                ODBC is an open standard C-based API developed by Microsoft for connecting diverse programming languages (C, C++, VB) to database systems. It utilizes native OS drivers and Windows Data Source Names (DSN), making it language-independent but heavily operating-system dependent.
              </p>
            </div>
          </div>
        </section>

        <!-- 8. QUESTION 6 -->
        <section class="content-section" id="q6">
          <h2 class="content-section-title"><span class="section-icon">🔄</span> 8. Detailed Comparison: ODBC vs. JDBC</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Comparison Parameter</th>
                  <th>ODBC (Open Database Connectivity)</th>
                  <th>JDBC (Java Database Connectivity)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Language Focus</strong></td>
                  <td>Language-independent; primarily written in C/C++</td>
                  <td>Specifically architected for the Java programming language</td>
                </tr>
                <tr>
                  <td><strong>Platform Portability</strong></td>
                  <td>Platform-dependent (heavily coupled to Windows binaries)</td>
                  <td>Platform-independent (Type-4 pure Java drivers run anywhere)</td>
                </tr>
                <tr>
                  <td><strong>Driver Mechanism</strong></td>
                  <td>Relies on native OS DLLs and vendor-specific drivers</td>
                  <td>Uses JDBC Driver implementations (Type 1, 2, 3, or Type 4)</td>
                </tr>
                <tr>
                  <td><strong>Performance for Java</strong></td>
                  <td>Slower due to JNI C-to-Java translation bridge overhead</td>
                  <td>High performance; communicates directly over database sockets</td>
                </tr>
                <tr>
                  <td><strong>Configuration</strong></td>
                  <td>Requires manual Windows Administrative DSN setup</td>
                  <td>Zero OS configuration; configured purely via connection URL</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 9. QUESTION 7 -->
        <section class="content-section" id="q7">
          <h2 class="content-section-title"><span class="section-icon">🍪</span> 9. State Management: Cookies vs. Sessions</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Cookies (Client-Side)</th>
                  <th>Sessions (Server-Side)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Storage Location</strong></td>
                  <td>Stored locally on the client's web browser</td>
                  <td>Stored securely in the web server's memory / cache</td>
                </tr>
                <tr>
                  <td><strong>Capacity Limitation</strong></td>
                  <td>Restricted to approximately 4 KB per cookie</td>
                  <td>Virtually unlimited (governed by available server RAM)</td>
                </tr>
                <tr>
                  <td><strong>Security Level</strong></td>
                  <td>Vulnerable to client-side inspection, XSS, and tampering</td>
                  <td>Highly secure; only an opaque Session ID (JSESSIONID) is shared</td>
                </tr>
                <tr>
                  <td><strong>Lifecycle Duration</strong></td>
                  <td>Persists until explicit expiration date (Max-Age) or user clear</td>
                  <td>Terminates upon browser close, user logout, or inactivity timeout</td>
                </tr>
                <tr>
                  <td><strong>Primary Use Cases</strong></td>
                  <td>Remembering user preferences, tracking tokens, themes</td>
                  <td>User authentication, shopping carts, sensitive profile states</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 10. QUESTION 8 -->
        <section class="content-section" id="q8">
          <h2 class="content-section-title"><span class="section-icon">🌱</span> 10. Spring Boot vs. Traditional Spring Framework</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Dimension</th>
                  <th>Traditional Spring Framework</th>
                  <th>Spring Boot</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Configuration Overhead</strong></td>
                  <td>Requires extensive manual XML configuration or verbose JavaConfig</td>
                  <td>Provides intelligent Auto-Configuration (<code>@EnableAutoConfiguration</code>)</td>
                </tr>
                <tr>
                  <td><strong>Server Deployment</strong></td>
                  <td>Requires external web server (e.g., WAR deployed to Tomcat)</td>
                  <td>Features embedded web servers (Tomcat, Jetty) inside standalone JAR</td>
                </tr>
                <tr>
                  <td><strong>Dependency Management</strong></td>
                  <td>Manual resolution of individual compatible JAR versions</td>
                  <td>Opinionated Starter POMs (e.g., <code>spring-boot-starter-web</code>)</td>
                </tr>
                <tr>
                  <td><strong>Production Readiness</strong></td>
                  <td>Requires third-party tools for metrics and monitoring</td>
                  <td>Includes built-in Actuator for metrics, health checks, and telemetry</td>
                </tr>
                <tr>
                  <td><strong>Application Suitability</strong></td>
                  <td>Heavyweight monolithic enterprise applications</td>
                  <td>Rapid application prototyping, microservices, and cloud-native systems</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 11. QUESTION 9 -->
        <section class="content-section" id="q9">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 11. Standalone vs. Web Applications</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Criterion</th>
                  <th>Standalone Desktop Applications</th>
                  <th>Distributed Web Applications</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Execution Host</strong></td>
                  <td>Executes directly on the local client machine's OS</td>
                  <td>Executes on remote web and application servers</td>
                </tr>
                <tr>
                  <td><strong>Installation</strong></td>
                  <td>Requires per-machine installation and platform compatibility</td>
                  <td>Zero client installation; accessed instantly via any web browser</td>
                </tr>
                <tr>
                  <td><strong>Network Dependence</strong></td>
                  <td>Functions completely offline without network access</td>
                  <td>Requires active intranet or Internet network connectivity</td>
                </tr>
                <tr>
                  <td><strong>User Interface</strong></td>
                  <td>Native desktop windowing (Swing, JavaFX, Qt, WinForms)</td>
                  <td>Browser-rendered responsive markup (HTML5, CSS3, JavaScript)</td>
                </tr>
                <tr>
                  <td><strong>Update Deployment</strong></td>
                  <td>Requires individual client patches or installer re-runs</td>
                  <td>Centralized instant deployment; updates apply globally to all users</td>
                </tr>
                <tr>
                  <td><strong>Representative Examples</strong></td>
                  <td>Calculator, VLC Media Player, MS Paint, Notepad</td>
                  <td>Gmail, Amazon, GitHub, Banking Portals, ERP Systems</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 12. QUESTION 10 -->
        <section class="content-section" id="q10">
          <h2 class="content-section-title"><span class="section-icon">🛠️</span> 12. Basic Requirements for Executing Web Applications</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">☕ 1. Runtime & Build Environment</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span><strong>JDK (Java Development Kit):</strong> Compiles Java source into bytecode (.class).</div>
                <div class="req-item"><span class="req-item-dot"></span><strong>JRE / JVM:</strong> Executes compiled bytecode within runtime environment.</div>
                <div class="req-item"><span class="req-item-dot"></span><strong>Build Tools:</strong> Apache Maven or Gradle for dependency management.</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 2. Web & Database Servers</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span><strong>Web/Servlet Container:</strong> Apache Tomcat, Jetty, or Undertow.</div>
                <div class="req-item"><span class="req-item-dot"></span><strong>Database Engine:</strong> MySQL 8.0, PostgreSQL, Oracle, or In-Memory H2.</div>
                <div class="req-item"><span class="req-item-dot"></span><strong>JDBC Connector:</strong> Type-4 pure Java driver JAR (e.g., MySQL Connector/J).</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🖥️ 3. Client & Presentation Tier</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span><strong>Web Browser:</strong> Chrome, Firefox, Edge, or Safari to render HTML/CSS.</div>
                <div class="req-item"><span class="req-item-dot"></span><strong>Markup & Styling:</strong> HTML5 markup, CSS3 styling, and JavaScript logic.</div>
                <div class="req-item"><span class="req-item-dot"></span><strong>Templating:</strong> Server-side rendering engines (Thymeleaf, JSP).</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💻 4. Development IDE</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span><strong>IDE:</strong> Spring Tool Suite 4 (STS), NetBeans 8.2, or IntelliJ IDEA.</div>
                <div class="req-item"><span class="req-item-dot"></span><strong>Server Adapters:</strong> Integrated server plugins to manage deployment lifecycles.</div>
              </div>
            </div>
          </div>
        </section>

        <!-- 13. RESULT -->
        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 13. Result & Theoretical Learning Outcomes</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="margin-bottom:12px;font-weight:600;color:var(--text-main);">
              Learning Outcome Summary:
            </p>
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Through the structured investigation of Unit 0, the theoretical distinction between Core Java and Advanced Java was established. Key architectural insights into client-side applet obsolescence versus server-side servlet vitality were documented. The vital roles of JDBC Type-4 drivers, client-side Cookies, server-side Sessions, and Spring Boot auto-configuration were systematized, establishing the required framework for the subsequent 13 laboratory experiments.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(0)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-0.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_0()

# ==============================================================================
# WEEK 1: Programming Language Comparative Analysis
# ==============================================================================
def generate_week_1():
    header = get_page_header(
        1,
        "Advanced Java Lab Task 1: Programming Language Comparative Analysis",
        "20-Parameter Architectural Matrix & Domain Suitability of Java, C, C++, Python & JavaScript",
        ["📊 20-Parameter Matrix", "⚡ 5 Major Languages", "🎯 Domain Suitability", "🏆 Architectural Synthesis"],
        "Core & Theory"
    )

    body = """
    <!-- CONTENT WRAPPER -->
    <div class="topic-content-wrap container">

      <!-- SIDEBAR TOC -->
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 1 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview</a>
          <a href="#matrix" class="toc-item">3. 20-Parameter Matrix</a>
          <a href="#unique" class="toc-item">4. Unique Features</a>
          <a href="#suitability" class="toc-item">5. Domain Suitability</a>
          <a href="#conclusion" class="toc-item">6. Evaluative Conclusion</a>
          <a href="#result" class="toc-item">7. Result</a>
        </nav>
      </aside>

      <!-- MAIN ARTICLE -->
      <article class="topic-main">

        <!-- 1. AIM -->
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To evaluate, compare, and synthesize the architectural paradigms, compiler/runtime mechanics, memory management models, and operational attributes of five predominant programming languages (Java, C, C++, Python, and JavaScript) across 20 standardized parameters, determining empirical domain suitability for contemporary software engineering.
          </p>
        </section>

        <!-- 2. OVERVIEW -->
        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Architectural Overview</h2>
          <p>
            Modern software engineering encompasses vastly diverse operating requirements: hard real-time kernel programming, high-throughput financial transactions, distributed cloud microservices, exploratory machine learning pipelines, and interactive client-side web rendering. Selecting an optimal software platform demands an objective understanding of runtime trade-offs: manual memory control versus garbage collection, Ahead-Of-Time (AOT) machine compilation versus Just-In-Time (JIT) bytecode interpretation, and static versus dynamic type systems.
          </p>
        </section>

        <!-- 3. 20-PARAMETER MATRIX -->
        <section class="content-section" id="matrix">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 3. 20-Parameter Comprehensive Comparative Matrix</h2>
          <p>Based on official ISO standards, OpenJDK specifications, ECMAScript releases, and current language documentation (2026):</p>
          
          <div class="table-wrap">
            <table style="font-size:0.8rem;">
              <thead>
                <tr>
                  <th style="min-width:140px;">Parameter</th>
                  <th style="min-width:140px;">Java</th>
                  <th style="min-width:130px;">C</th>
                  <th style="min-width:130px;">C++</th>
                  <th style="min-width:140px;">Python</th>
                  <th style="min-width:140px;">JavaScript</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>1. Open Source / Commercial</strong></td>
                  <td>Open Source (OpenJDK) & Commercial (Oracle JDK)</td>
                  <td>Open Standard (ISO/IEC 9899)</td>
                  <td>Open Standard (ISO/IEC 14882)</td>
                  <td>Open Source (PSF License)</td>
                  <td>Open Standard (ECMA-262 / W3C)</td>
                </tr>
                <tr>
                  <td><strong>2. Compiler / Interpreter</strong></td>
                  <td>Both (Compiled to bytecode, JIT executed by JVM)</td>
                  <td>Pure Compiler (Direct machine code)</td>
                  <td>Pure Compiler (Direct machine code)</td>
                  <td>Interpreter (Bytecode compiled & interpreted)</td>
                  <td>Both (JIT Compiled & Interpreted by V8/SpiderMonkey)</td>
                </tr>
                <tr>
                  <td><strong>3. OOP Support</strong></td>
                  <td>Yes (Pure class-based object-oriented)</td>
                  <td>No (Procedural / Structured paradigm)</td>
                  <td>Yes (Multi-paradigm: OOP, Procedural, Generic)</td>
                  <td>Yes (Multi-paradigm: OOP, Functional, Scripting)</td>
                  <td>Yes (Prototype-based & Class syntax OOP)</td>
                </tr>
                <tr>
                  <td><strong>4. Developer Organization</strong></td>
                  <td>Oracle Corporation (originally Sun Microsystems)</td>
                  <td>ANSI / ISO Standardization Committees</td>
                  <td>ISO / IEC JTC1/SC22/WG21 Committee</td>
                  <td>Python Software Foundation (PSF)</td>
                  <td>Ecma International / TC39</td>
                </tr>
                <tr>
                  <td><strong>5. Original Developer</strong></td>
                  <td>James Gosling</td>
                  <td>Dennis Ritchie</td>
                  <td>Bjarne Stroustrup</td>
                  <td>Guido van Rossum</td>
                  <td>Brendan Eich</td>
                </tr>
                <tr>
                  <td><strong>6. Major Version (2026)</strong></td>
                  <td>Java 25 (LTS) / Java 26</td>
                  <td>C23</td>
                  <td>C++26</td>
                  <td>Python 3.14</td>
                  <td>ECMAScript 2026 (ES17)</td>
                </tr>
                <tr>
                  <td><strong>7. Primary Purpose</strong></td>
                  <td>Enterprise software & distributed backend systems</td>
                  <td>Operating systems & low-level hardware control</td>
                  <td>High-performance systems, engines & simulations</td>
                  <td>AI, Data Science, automation & rapid scripting</td>
                  <td>Interactive web frontend & full-stack development</td>
                </tr>
                <tr>
                  <td><strong>8. Common Applications</strong></td>
                  <td>Banking portals, Android apps, microservices, big data</td>
                  <td>Linux kernel, device drivers, embedded microcontrollers</td>
                  <td>Game engines (Unreal), browsers, trading systems</td>
                  <td>Machine learning (TensorFlow), computer vision, scripts</td>
                  <td>Single Page Apps (React/Angular), Node.js backends</td>
                </tr>
                <tr>
                  <td><strong>9. Database Support</strong></td>
                  <td>Outstanding native support via JDBC & JPA/Hibernate</td>
                  <td>External client libraries (libmysqlclient, sqlite3)</td>
                  <td>External libraries (ODBC, MySQL Connector/C++, ODB)</td>
                  <td>Excellent via DB-API (psycopg2, SQLAlchemy, PyMySQL)</td>
                  <td>Exceptional via NPM drivers & ORMs (Prisma, Mongoose)</td>
                </tr>
                <tr>
                  <td><strong>10. Memory Management</strong></td>
                  <td>Automatic Garbage Collection (G1, ZGC, Shenandoah)</td>
                  <td>Manual memory allocation (malloc, calloc, free)</td>
                  <td>Manual memory & RAII / Smart Pointers (unique_ptr)</td>
                  <td>Automatic Reference Counting & Cyclic GC</td>
                  <td>Automatic Generational Mark-and-Sweep GC</td>
                </tr>
                <tr>
                  <td><strong>11. Security Features</strong></td>
                  <td>Bytecode verification, SecurityManager, JVM sandbox</td>
                  <td>Minimal built-in; prone to buffer overflows & leaks</td>
                  <td>Modern smart pointers; vulnerable if raw pointers misused</td>
                  <td>Secure runtime environment; dynamic execution risks (eval)</td>
                  <td>Browser Same-Origin Policy, Sandboxed Execution</td>
                </tr>
                <tr>
                  <td><strong>12. Execution Performance</strong></td>
                  <td>High (Near-native speed with HotSpot JIT)</td>
                  <td>Extremely High (Bare-metal execution efficiency)</td>
                  <td>Extremely High (Zero-overhead abstractions)</td>
                  <td>Moderate to Low (Interpreted overhead; C-extensions)</td>
                  <td>High (Optimized JIT engines like Google V8)</td>
                </tr>
                <tr>
                  <td><strong>13. Platform Independence</strong></td>
                  <td>Yes (Write Once, Run Anywhere via JVM)</td>
                  <td>No (Requires per-platform recompilation)</td>
                  <td>No (Source portable; requires platform compilation)</td>
                  <td>Yes (Interpreted across any OS with Python runtime)</td>
                  <td>Yes (Universal browser and cross-platform Node.js)</td>
                </tr>
                <tr>
                  <td><strong>14. Other Features</strong></td>
                  <td>Virtual threads (Project Loom), strong type safety</td>
                  <td>Direct pointer arithmetic, tiny runtime footprint</td>
                  <td>Standard Template Library (STL), templates, move semantics</td>
                  <td>Massive scientific library ecosystem, clean syntax</td>
                  <td>Event loop, asynchronous I/O (async/await), dynamic typing</td>
                </tr>
                <tr>
                  <td><strong>15. Ease of Learning</strong></td>
                  <td>Moderate (Strict OOP and verbose syntax)</td>
                  <td>Moderate (Pointers and manual memory challenge beginners)</td>
                  <td>Difficult (Complex syntax, template metaprogramming)</td>
                  <td>Easy (Highly readable English-like syntax)</td>
                  <td>Easy to Moderate (Forgiving syntax, async complexity)</td>
                </tr>
                <tr>
                  <td><strong>16. Popular IDEs</strong></td>
                  <td>IntelliJ IDEA, Eclipse, Spring Tool Suite, NetBeans</td>
                  <td>VS Code, CLion, Code::Blocks, Vim</td>
                  <td>Visual Studio, CLion, VS Code, Qt Creator</td>
                  <td>PyCharm, VS Code, Jupyter Notebook</td>
                  <td>VS Code, WebStorm, Sublime Text</td>
                </tr>
                <tr>
                  <td><strong>17. Compilation Output</strong></td>
                  <td>Platform-independent bytecode (.class files)</td>
                  <td>Native platform machine binary (.exe / ELF)</td>
                  <td>Native platform machine binary (.exe / ELF)</td>
                  <td>Bytecode cache (.pyc) executed by interpreter</td>
                  <td>JIT optimized native machine code in memory</td>
                </tr>
                <tr>
                  <td><strong>18. Ecosystem Packages</strong></td>
                  <td>Maven Central Repository (billions of artifacts)</td>
                  <td>OS Package Managers (apt, vcpkg, conan)</td>
                  <td>Conan, vcpkg, CMake modules</td>
                  <td>PyPI (Python Package Index - 450,000+ packages)</td>
                  <td>NPM (Node Package Manager - 2M+ packages)</td>
                </tr>
                <tr>
                  <td><strong>19. Advantages</strong></td>
                  <td>Rock-solid stability, WORA, immense enterprise tooling</td>
                  <td>Absolute hardware control, predictable execution time</td>
                  <td>Unrivaled speed, memory efficiency, multi-paradigm</td>
                  <td>Fast prototyping, unparalleled AI/ML dominance</td>
                  <td>Ubiquitous browser integration, single-language stack</td>
                </tr>
                <tr>
                  <td><strong>20. Limitations</strong></td>
                  <td>Higher heap memory footprint, initial startup latency</td>
                  <td>Lack of OOP, no automatic garbage collection, crash-prone</td>
                  <td>Extremely steep learning curve, complex build pipelines</td>
                  <td>Slow execution loops, Global Interpreter Lock (GIL)</td>
                  <td>Loose typing quirks, browser compatibility variances</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 4. UNIQUE FEATURES -->
        <section class="content-section" id="unique">
          <h2 class="content-section-title"><span class="section-icon">🌟</span> 4. Unique Features of Each Language</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">☕ Java</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <strong>Write Once, Run Anywhere (WORA):</strong> Bytecode architecture decouples source code from underlying processor architectures. With the advent of Project Loom (Virtual Threads), Java achieves unprecedented millions of concurrent lightweight threads for cloud-scale throughput without OS thread overhead.
              </p>
            </div>
            <div class="req-card">
              <div class="req-card-title">💻 C</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <strong>Direct Hardware Mapping:</strong> C maps directly to CPU assembly instructions, offering raw pointer arithmetic and direct memory manipulation. It remains the universal lingua franca for kernels, embedded firmware, and microcontroller firmware.
              </p>
            </div>
            <div class="req-card">
              <div class="req-card-title">⚡ C++</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <strong>Zero-Cost Abstractions & RAII:</strong> Resource Acquisition Is Initialization (RAII) guarantees deterministic resource cleanup without garbage collection. High-level abstractions (templates, ranges, lambda expressions) compile down to optimal machine instructions with zero runtime cost.
              </p>
            </div>
            <div class="req-card">
              <div class="req-card-title">🐍 Python</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <strong>Rich Mathematical Ecosystem & Expressiveness:</strong> Unmatched developer velocity enabled by clean, indentation-delimited syntax. Dominates modern Artificial Intelligence, Machine Learning, and scientific computing through seamless bindings to highly optimized C/Fortran math libraries.
              </p>
            </div>
            <div class="req-card" style="grid-column:1/-1;">
              <div class="req-card-title">🌐 JavaScript</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <strong>Universal Browser Execution & Event-Driven Asynchrony:</strong> The sole programming language native to all web browsers. Utilizing an event loop and non-blocking I/O model (Promises, async/await), JavaScript enables unified full-stack engineering where the same language powers the client UI and the Node.js API backend.
              </p>
            </div>
          </div>
        </section>

        <!-- 5. DOMAIN SUITABILITY -->
        <section class="content-section" id="suitability">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 5. Domain Suitability Analysis</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Computing Domain</th>
                  <th>Recommended Language</th>
                  <th>Technical Justification</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>System Programming</strong></td>
                  <td><strong>C / C++</strong></td>
                  <td>Direct memory addressing, deterministic latency, zero garbage collector pause times, and direct hardware register access make C and C++ indispensable for OS kernels (Linux, Windows), hypervisors, and embedded automotive microcontrollers.</td>
                </tr>
                <tr>
                  <td><strong>Enterprise Applications</strong></td>
                  <td><strong>Java</strong></td>
                  <td>Java's robust type safety, rock-solid multithreading, enterprise Spring Boot ecosystem, automated garbage collection, and mature database integration (JDBC/JPA) deliver the unmatched reliability and transaction integrity required by global banking and e-commerce backends.</td>
                </tr>
                <tr>
                  <td><strong>Web Development</strong></td>
                  <td><strong>JavaScript (Frontend) / Java (Backend)</strong></td>
                  <td>JavaScript is the universal standard for client-side responsive interfaces, while Java (Spring Boot) provides high-performance, fault-tolerant, horizontally scalable REST API backends.</td>
                </tr>
                <tr>
                  <td><strong>Artificial Intelligence & Data Science</strong></td>
                  <td><strong>Python</strong></td>
                  <td>PyTorch, TensorFlow, NumPy, and Pandas make Python the undisputed champion for neural network training, data manipulation, computer vision, and LLM development.</td>
                </tr>
                <tr>
                  <td><strong>Mobile Application Development</strong></td>
                  <td><strong>Java / Kotlin (Android)</strong></td>
                  <td>Android OS natively operates on Java bytecode and ART (Android Runtime), providing direct access to native mobile hardware APIs, sensor telemetry, and background services.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 6. CONCLUSION -->
        <section class="content-section" id="conclusion">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 6. Evaluative Conclusion (Synthesis)</h2>
          <div style="background:var(--bg-secondary);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;line-height:1.8;">
            <p style="color:var(--text-main);font-weight:600;margin-bottom:10px;">
              Academic Evaluation Synthesis (140 Words):
            </p>
            <p style="font-size:0.92rem;color:var(--text-sub);">
              The comprehensive 20-parameter comparative analysis establishes that modern programming languages have evolved into specialized, non-competing computational domains. C and C++ maintain an uncontested monopoly over bare-metal systems, game engines, and low-latency financial systems due to deterministic memory control and zero-overhead abstractions. In contrast, Java remains the global backbone of enterprise cloud computing and distributed transactional systems, powered by its robust JVM bytecode portability, type safety, and the Spring ecosystem. Python dominates artificial intelligence, data science, and algorithmic research through unparalleled library abstraction, while JavaScript continues its universal reign over the modern interactive web tier. Therefore, modern enterprise architectures typically adopt a polyglot paradigm, orchestrating Java backends, Python AI inference pipelines, and JavaScript client interfaces to achieve optimal software performance and scalability.
            </p>
          </div>
        </section>

        <!-- 7. RESULT -->
        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 7. Result</h2>
          <p>
            The comparative study of Java, C, C++, Python, and JavaScript was successfully conducted across all twenty academic parameters. Unique language features and explicit domain suitability matrices were synthesized and documented in accordance with the Task-1 syllabus requirements.
          </p>
        </section>
    """

    footer = get_page_footer(1)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-1.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_1()

# ==============================================================================
# WEEK 2: Java Development Environment Setup
# ==============================================================================
def generate_week_2():
    header = get_page_header(
        2,
        "Java Development Environment Setup in Ubuntu",
        "Downloading, Installing, and Configuring OpenJDK & Oracle JDK SE 26 on Linux",
        ["🐧 Ubuntu Linux", "☕ OpenJDK / Oracle JDK 26", "⚙️ update-alternatives", "💻 ~/.bashrc & JAVA_HOME"],
        "Environment & Setup"
    )

    body = """
    <!-- CONTENT WRAPPER -->
    <div class="topic-content-wrap container">

      <!-- SIDEBAR TOC -->
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 2 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview</a>
          <a href="#requirements" class="toc-item">3. Requirements</a>
          <a href="#procedure" class="toc-item">4. Step-by-Step Procedure</a>
          <a href="#script" class="toc-item">5. Shell Automation Script</a>
          <a href="#explanation" class="toc-item">6. Command Breakdown</a>
          <a href="#output" class="toc-item">7. Terminal Verification Output</a>
          <a href="#screenshots" class="toc-item">8. Screenshot Gallery</a>
          <a href="#result" class="toc-item">9. Result & Observation</a>
        </nav>
      </aside>

      <!-- MAIN ARTICLE -->
      <article class="topic-main">

        <!-- 1. AIM -->
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To download, extract, register, and configure the OpenJDK / Oracle JDK SE 26 development environment on an Ubuntu Linux system, establishing system-wide binary alternative symlinks via <code>update-alternatives</code>, configuring <code>JAVA_HOME</code> and <code>PATH</code> environment variables in <code>~/.bashrc</code>, and verifying the runtime version.
          </p>
        </section>

        <!-- 2. OVERVIEW -->
        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Overview</h2>
          <p>
            Enterprise Linux servers commonly run headless instances of production software without package manager restrictions. Deploying a JDK distribution into the standard system directory <code>/opt/</code> preserves operating system cleanliness while granting multi-user access. The Debian/Ubuntu <code>update-alternatives</code> system maintains symbolic links determining default commands (<code>/usr/bin/java</code> and <code>/usr/bin/javac</code>) across concurrent JDK versions. Establishing <code>JAVA_HOME</code> ensures build tools like Maven, Gradle, and Tomcat locate the JDK root directory.
          </p>
        </section>

        <!-- 3. REQUIREMENTS -->
        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 3. System Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware Requirements</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Architecture: x86_64 (64-bit) Intel/AMD CPU</div>
                <div class="req-item"><span class="req-item-dot"></span>RAM: 4 GB minimum</div>
                <div class="req-item"><span class="req-item-dot"></span>Storage: 2 GB free disk space</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Software Requirements</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>OS: Ubuntu 22.04 LTS / Linux Mint</div>
                <div class="req-item"><span class="req-item-dot"></span>Archive: openjdk-26*_bin.tar.gz</div>
                <div class="req-item"><span class="req-item-dot"></span>Shell: GNU Bash shell with sudo privileges</div>
              </div>
            </div>
          </div>
        </section>

        <!-- 4. PROCEDURE -->
        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Procedure</h2>

          <div class="timeline-procedure">
            <!-- Step 1 -->
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header">
                  <div class="timeline-icon">📦</div>
                  <div class="timeline-title">Extract the Tarball into /opt/</div>
                </div>
                <div class="timeline-desc">
                  Download the JDK 26 Linux x64 tarball and extract it into the system-wide <code>/opt/</code> directory using superuser privileges:
                  <pre class="timeline-code"><code>sudo tar -xvf ~/Downloads/openjdk-26*_bin.tar.gz -C /opt/</code></pre>
                </div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header">
                  <div class="timeline-icon">⚙️</div>
                  <div class="timeline-title">Register Java & Javac Binaries</div>
                </div>
                <div class="timeline-desc">
                  Configure Debian binary alternatives for the Java runtime engine and compiler, setting priority to 1:
                  <pre class="timeline-code"><code>sudo update-alternatives --install /usr/bin/java java /opt/jdk-26/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /opt/jdk-26/bin/javac 1</code></pre>
                </div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header">
                  <div class="timeline-icon">📝</div>
                  <div class="timeline-title">Establish Environment Variables</div>
                </div>
                <div class="timeline-desc">
                  Export <code>JAVA_HOME</code> and prepend the JDK <code>bin</code> folder to the system <code>PATH</code> inside the user's bash configuration file:
                  <pre class="timeline-code"><code>echo 'export JAVA_HOME=/opt/jdk-26' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc</code></pre>
                </div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header">
                  <div class="timeline-icon">✅</div>
                  <div class="timeline-title">Verify Runtime & Compiler Versions</div>
                </div>
                <div class="timeline-desc">
                  Verify the active Java version and ensure the 64-Bit Server VM is active:
                  <pre class="timeline-code"><code>java --version
javac --version</code></pre>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. SHELL SCRIPT -->
        <section class="content-section" id="script">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 5. Shell Automation Script (setup_jdk26.sh)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">setup_jdk26.sh</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="setup_jdk26.sh">⬇ Download .sh</button>
              </div>
            </div>
            <div class="code-editor-body">
              <div class="line-numbers" aria-hidden="true">1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21</div>
              <pre><code><span class="co">#!/bin/bash</span>
<span class="co"># Week 2: OpenJDK & Oracle JDK SE 26 Installation Script</span>
<span class="co"># Student: Venkata Sai Karthikeya Kaja (24EU08161)</span>
<span class="kw">set</span> -e

<span class="kw">echo</span> <span class="str">"Step 1: Extracting JDK tarball to /opt/"</span>
sudo tar -xvf ~/Downloads/openjdk-26*_bin.tar.gz -C /opt/

<span class="kw">echo</span> <span class="str">"Step 2: Registering Java binaries with update-alternatives"</span>
sudo update-alternatives --install /usr/bin/java java /opt/jdk-26/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /opt/jdk-26/bin/javac 1

<span class="kw">echo</span> <span class="str">"Step 3: Setting environment variables in ~/.bashrc"</span>
<span class="kw">echo</span> <span class="str">'export JAVA_HOME=/opt/jdk-26'</span> &gt;&gt; ~/.bashrc
<span class="kw">echo</span> <span class="str">'export PATH=$JAVA_HOME/bin:$PATH'</span> &gt;&gt; ~/.bashrc
<span class="kw">source</span> ~/.bashrc

<span class="kw">echo</span> <span class="str">"Step 4: Verifying Java version"</span>
java --version
javac --version
<span class="kw">echo</span> <span class="str">"Installation and Configuration Complete!"</span></code></pre>
            </div>
          </div>
        </section>

        <!-- 6. EXPLANATION -->
        <section class="content-section" id="explanation">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 6. Command Breakdown</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Command / Directive</th>
                  <th>Target Parameter</th>
                  <th>Technical Function</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>tar -xvf ... -C /opt/</code></td>
                  <td>Archive Extraction</td>
                  <td>Decompresses the tarball preserving file ownership and directories inside <code>/opt/</code>.</td>
                </tr>
                <tr>
                  <td><code>update-alternatives --install</code></td>
                  <td>Symlink Management</td>
                  <td>Creates master alternative links under <code>/usr/bin/</code> pointing to <code>/opt/jdk-26/bin/</code>.</td>
                </tr>
                <tr>
                  <td><code>export JAVA_HOME=/opt/jdk-26</code></td>
                  <td>Root Environment Variable</td>
                  <td>Informs external tools (Maven, STS, Tomcat) where Java libraries and header files reside.</td>
                </tr>
                <tr>
                  <td><code>source ~/.bashrc</code></td>
                  <td>Shell Session Reload</td>
                  <td>Applies newly appended environment exports to the active shell without logging out.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 7. OUTPUT CONSOLE -->
        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 7. Terminal Verification Output</h2>
          <div class="netbeans-output" style="background:#2c001e;">
            <div class="netbeans-header" style="background:#1e0014;">
              <div class="netbeans-tabs">
                <div class="netbeans-tab" style="background:#2c001e;color:#fff;">
                  <span class="netbeans-tab-icon">🐧</span> student@ITLAB3-1: ~ (Ubuntu Bash)
                </div>
              </div>
              <div class="netbeans-actions"><span class="nb-status-badge">SUCCESS</span></div>
            </div>
            <div class="netbeans-body" style="font-family:var(--font-code);color:#dedede;line-height:1.7;">
              <span style="color:#5cbf26;">student@ITLAB3-1:~$</span> <span style="color:#ffffff;">java --version</span><br />
              <span style="color:#38bdf8;">java 26.0.1 2026-04-21</span><br />
              <span>Java(TM) SE Runtime Environment (build 26.0.1+8-34)</span><br />
              <span>Java HotSpot(TM) 64-Bit Server VM (build 26.0.1+8-34, mixed mode, sharing)</span><br />
              <span style="color:#5cbf26;">student@ITLAB3-1:~$</span> <span style="color:#ffffff;">javac --version</span><br />
              <span style="color:#38bdf8;">javac 26.0.1</span><br />
              <span style="color:#5cbf26;">student@ITLAB3-1:~$</span> <span style="color:#ffffff;">echo $JAVA_HOME</span><br />
              <span>/opt/jdk-26</span>
            </div>
          </div>
        </section>

        <!-- 8. SCREENSHOT GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Original Screenshot Gallery
            </h2>
            <span class="badge badge-purple">Original Terminal Verification</span>
          </div>
          <p>Extracted authentic terminal verification screenshot from student lab session (adv java 2.odt):</p>

          <div class="gallery-grid">
            <!-- Card 1 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Execution Proof</span><span class="ss-counter-badge">[1 / 1]</span></div>
              <div class="ss-img-wrap" data-title="Ubuntu Terminal: Java 26 Version Verification Output">
                <img src="../assets/images/week-2/week2_terminal_verify.png" alt="Ubuntu Terminal Output Java 26 Version Verification" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Java 26 Terminal Verification</div>
                <div class="ss-subcaption">Authentic Ubuntu terminal output verifying Java SE 26 runtime & HotSpot 64-Bit Server VM build.</div>
                <div class="ss-actions">
                  <button class="ss-btn ss-replace-btn">📷 Replace Image</button>
                  <a href="../assets/images/week-2/week2_terminal_verify.png" download class="ss-btn ss-download-btn">⬇ Download</a>
                  <input type="file" class="ss-file-input" accept="image/*" />
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 9. RESULT -->
        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result & Observation</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, OpenJDK / Oracle JDK SE 26 was successfully extracted and configured on the Ubuntu Linux operating system. Symbolic binary alternatives were registered under <code>/usr/bin/java</code> and <code>/usr/bin/javac</code>, and environment paths were verified via terminal telemetry.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(2)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-2.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_2()

# ==============================================================================
# WEEK 3: Java MS Access Database Connectivity
# ==============================================================================
def generate_week_3():
    header = get_page_header(
        3,
        "Java MS Access Connectivity Using UCanAccess",
        "Pure Java JDBC Driver Setup, Classpath Configuration, and Database Traversal",
        ["🗂️ MS Access (.accdb)", "🔌 UCanAccess 5.1.3", "☕ AccessDemo.java", "🐧 Terminal Execution"],
        "JDBC & Databases"
    )

    body = """
    <!-- CONTENT WRAPPER -->
    <div class="topic-content-wrap container">

      <!-- SIDEBAR TOC -->
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 3 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview</a>
          <a href="#requirements" class="toc-item">3. Requirements</a>
          <a href="#procedure" class="toc-item">4. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">5. Java Program</a>
          <a href="#explanation" class="toc-item">6. Program Explanation</a>
          <a href="#output" class="toc-item">7. Terminal Output</a>
          <a href="#screenshots" class="toc-item">8. Screenshot Gallery (9)</a>
          <a href="#result" class="toc-item">9. Result & Observation</a>
        </nav>
      </aside>

      <!-- MAIN ARTICLE -->
      <article class="topic-main">

        <!-- 1. AIM -->
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To write, compile, and execute a Java program (<code>AccessDemo.java</code>) to connect to a Microsoft Access database (<code>StudentDB.accdb</code>) on Ubuntu Linux using the pure Java UCanAccess JDBC driver architecture without Windows ODBC DSN configuration.
          </p>
        </section>

        <!-- 2. OVERVIEW -->
        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Overview</h2>
          <p>
            The legacy Type-1 JDBC-ODBC Bridge was officially deprecated in Java 8 and completely removed in modern JDKs, breaking direct native MS Access connectivity on non-Windows platforms. <strong>UCanAccess</strong> is an open-source, pure Java JDBC driver implementation that allows Java programs to read and write Microsoft Access database formats (.mdb and .accdb) on Linux, macOS, and Windows. Under the hood, UCanAccess utilizes <strong>Jackcess</strong> for file parsing and <strong>HSQLDB</strong> as an embedded memory engine to execute SQL queries.
          </p>
        </section>

        <!-- 3. REQUIREMENTS -->
        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 3. System Requirements & Dependencies</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware & OS</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>OS: Ubuntu Linux / Windows</div>
                <div class="req-item"><span class="req-item-dot"></span>RAM: 4 GB minimum</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE 8+ / OpenJDK 21</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">📦 Driver JAR Dependencies</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span><code>ucanaccess-5.1.3.jar</code> (Core Driver)</div>
                <div class="req-item"><span class="req-item-dot"></span><code>jackcess-4.0.8.jar</code> (MS Access Parser)</div>
                <div class="req-item"><span class="req-item-dot"></span><code>hsqldb-2.7.4.jar</code> (Embedded SQL Engine)</div>
                <div class="req-item"><span class="req-item-dot"></span><code>commons-lang3-3.17.0.jar</code> &amp; <code>commons-logging-1.3.5.jar</code></div>
              </div>
            </div>
          </div>
        </section>

        <!-- 4. PROCEDURE -->
        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Procedure (Preserved from Lab Document)</h2>

          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📁</div><div class="timeline-title">Step 1: Create ucanaccess Directory</div></div>
                <div class="timeline-desc"><code>mkdir ~/Downloads/ucanaccess</code></div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📂</div><div class="timeline-title">Step 2: Navigate to Directory</div></div>
                <div class="timeline-desc"><code>cd ~/Downloads/ucanaccess</code></div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⬇️</div><div class="timeline-title">Step 3: Download Core Driver JAR</div></div>
                <div class="timeline-desc"><code>wget https://repo1.maven.org/maven2/io/github/spannm/ucanaccess/5.1.3/ucanaccess-5.1.3.jar</code></div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📦</div><div class="timeline-title">Step 4: Download Dependency JARs</div></div>
                <div class="timeline-desc">
                  Download Jackcess, Commons-Lang3, Commons-Logging, and HSQLDB dependencies via <code>wget</code>.
                </div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📝</div><div class="timeline-title">Step 5: Create Source File</div></div>
                <div class="timeline-desc"><code>nano AccessDemo.java</code></div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">6</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">✍️</div><div class="timeline-title">Step 6: Edit & Save Program</div></div>
                <div class="timeline-desc">Paste Java program, change database link to <code>StudentDB.accdb</code>, press <code>Ctrl+O (Enter)</code> and <code>Ctrl+X</code> to save.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">7</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Step 7: Compile Java Source</div></div>
                <div class="timeline-desc"><code>javac AccessDemo.java</code></div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">8</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗄️</div><div class="timeline-title">Step 8: Place Database Dataset</div></div>
                <div class="timeline-desc">Place the <code>StudentDB.accdb</code> database file inside the <code>~/Downloads/ucanaccess</code> folder.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">9</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔗</div><div class="timeline-title">Step 9: Configure CLASSPATH</div></div>
                <div class="timeline-desc"><code>export CLASSPATH=.:/home/student/Downloads/ucanaccess/ucanaccess-5.1.2-uber.jar</code></div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">10</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Step 10: Execute Java Program</div></div>
                <div class="timeline-desc"><code>java -cp ".:ucanaccess-5.1.2-uber.jar" AccessDemo</code></div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">11</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">✅</div><div class="timeline-title">Step 11: Verify Terminal Output</div></div>
                <div class="timeline-desc">Verify printed output records: <code>Connected Successfully</code>, <code>1 RAMESH 10</code>, <code>2 MAHESH 20</code>, <code>3 SURESH 30</code>, <code>4 RAJESH 40</code>.</div>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. JAVA PROGRAM -->
        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 5. Java Program (AccessDemo.java)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">AccessDemo.java</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="AccessDemo.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <div class="line-numbers" aria-hidden="true">1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24</div>
              <pre><code><span class="kw">import</span> <span class="pk">java.sql.*</span>;

<span class="kw">public class</span> <span class="ty">AccessDemo</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="ty">String</span>[] args) {
        <span class="kw">try</span> {
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"net.ucanaccess.jdbc.UcanaccessDriver"</span>);
            <span class="ty">String</span> url = <span class="str">"jdbc:ucanaccess://StudentDB.accdb"</span>;
            <span class="ty">Connection</span> con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(url);

            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Connected Successfully"</span>);

            <span class="ty">Statement</span> st = con.<span class="fn">createStatement</span>();
            <span class="ty">ResultSet</span> rs = st.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM Student"</span>);

            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(rs.<span class="fn">getInt</span>(1) + <span class="str">" "</span> + rs.<span class="fn">getString</span>(2) + <span class="str">" "</span> + rs.<span class="fn">getInt</span>(3));
            }
            rs.<span class="fn">close</span>();
            st.<span class="fn">close</span>();
            con.<span class="fn">close</span>();
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            <span class="ty">System</span>.out.<span class="fn">println</span>(e);
        }
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- 6. EXPLANATION -->
        <section class="content-section" id="explanation">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 6. Program Explanation</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Code Segment</th>
                  <th>API Class / Method</th>
                  <th>Functional Description</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>Class.forName("net.ucanaccess.jdbc.UcanaccessDriver")</code></td>
                  <td>Class Loader</td>
                  <td>Dynamically loads and registers the pure Java UCanAccess JDBC driver with the DriverManager.</td>
                </tr>
                <tr>
                  <td><code>jdbc:ucanaccess://StudentDB.accdb</code></td>
                  <td>Connection URL</td>
                  <td>Direct JDBC URL pointing to the local MS Access database file path.</td>
                </tr>
                <tr>
                  <td><code>con.createStatement()</code></td>
                  <td>Statement Factory</td>
                  <td>Allocates a SQL statement object for executing static SQL queries against the Access database.</td>
                </tr>
                <tr>
                  <td><code>st.executeQuery("SELECT * FROM Student")</code></td>
                  <td>Query Execution</td>
                  <td>Sends the SQL query to the HSQLDB embedded engine, returning a scrollable ResultSet.</td>
                </tr>
                <tr>
                  <td><code>rs.getInt(1) + " " + rs.getString(2)</code></td>
                  <td>Cursor Traversal</td>
                  <td>Retrieves column index 1 (ID), column index 2 (Name), and column index 3 (Marks).</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 7. OUTPUT CONSOLE -->
        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 7. Terminal Execution Output</h2>
          <div class="netbeans-output" style="background:#2c001e;">
            <div class="netbeans-header" style="background:#1e0014;">
              <div class="netbeans-tabs">
                <div class="netbeans-tab" style="background:#2c001e;color:#fff;">
                  <span class="netbeans-tab-icon">🐧</span> student@ITLAB3-1: ~/Downloads/ucanaccess
                </div>
              </div>
              <div class="netbeans-actions"><span class="nb-status-badge">SUCCESS</span></div>
            </div>
            <div class="netbeans-body" style="font-family:var(--font-code);color:#dedede;line-height:1.7;">
              <span style="color:#5cbf26;">student@ITLAB3-1:~/Downloads/ucanaccess$</span> <span style="color:#ffffff;">java -cp ".:ucanaccess-5.1.2-uber.jar" AccessDemo</span><br />
              <span style="color:#4ade80;font-weight:bold;">Connected Successfully</span><br />
              <span>1 RAMESH 10</span><br />
              <span>2 MAHESH 20</span><br />
              <span>3 SURESH 30</span><br />
              <span>4 RAJESH 40</span><br />
              <span style="color:#5cbf26;">student@ITLAB3-1:~/Downloads/ucanaccess$</span>
            </div>
          </div>
        </section>

        <!-- 8. SCREENSHOT GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Original Lab Execution Screenshots (All 9 Steps)
            </h2>
            <span class="badge badge-purple">9 Authentic Screenshots</span>
          </div>
          <p>Extracted directly from student lab report (ADVANCED JAVA PROGRAMMING LAB WEEK 3 24EU08161.docx):</p>

          <div class="gallery-grid">
            <!-- Step 1 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 01</span><span class="ss-counter-badge">[1 / 9]</span></div>
              <div class="ss-img-wrap" data-title="mkdir ~/Downloads/ucanaccess">
                <img src="../assets/images/week-3/week3_step_1.png" alt="mkdir ~/Downloads/ucanaccess" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 1: Directory Creation</div>
                <div class="ss-subcaption">Creating working directory <code>mkdir ~/Downloads/ucanaccess</code>.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 02</span><span class="ss-counter-badge">[2 / 9]</span></div>
              <div class="ss-img-wrap" data-title="cd ~/Downloads/ucanaccess">
                <img src="../assets/images/week-3/week3_step_2.png" alt="cd ~/Downloads/ucanaccess" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 2: Directory Navigation</div>
                <div class="ss-subcaption">Navigating into <code>cd ~/Downloads/ucanaccess</code>.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 03</span><span class="ss-counter-badge">[3 / 9]</span></div>
              <div class="ss-img-wrap" data-title="wget ucanaccess-5.1.3.jar">
                <img src="../assets/images/week-3/week3_step_3.png" alt="wget ucanaccess-5.1.3.jar" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 3: Download Core Driver</div>
                <div class="ss-subcaption">Downloading <code>ucanaccess-5.1.3.jar</code> via wget (432K).</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 04</span><span class="ss-counter-badge">[4 / 9]</span></div>
              <div class="ss-img-wrap" data-title="wget dependencies">
                <img src="../assets/images/week-3/week3_step_4.png" alt="wget dependencies" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 4: Download Dependencies</div>
                <div class="ss-subcaption">Downloading jackcess, commons-lang3, commons-logging, and hsqldb.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_4.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 5 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 05</span><span class="ss-counter-badge">[5 / 9]</span></div>
              <div class="ss-img-wrap" data-title="nano AccessDemo.java">
                <img src="../assets/images/week-3/week3_step_5.png" alt="nano AccessDemo.java" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 5: nano Text Editor</div>
                <div class="ss-subcaption">Creating source code file via <code>nano AccessDemo.java</code>.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 6 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 07</span><span class="ss-counter-badge">[6 / 9]</span></div>
              <div class="ss-img-wrap" data-title="javac AccessDemo.java">
                <img src="../assets/images/week-3/week3_step_6.png" alt="javac AccessDemo.java" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 7: Java Compilation</div>
                <div class="ss-subcaption">Compiling Java code with zero compilation errors.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_6.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 7 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 09</span><span class="ss-counter-badge">[7 / 9]</span></div>
              <div class="ss-img-wrap" data-title="export CLASSPATH">
                <img src="../assets/images/week-3/week3_step_7.png" alt="export CLASSPATH" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 9: Classpath Export</div>
                <div class="ss-subcaption">Exporting CLASSPATH to include UCanAccess uber JAR.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_7.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 8 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 10</span><span class="ss-counter-badge">[8 / 9]</span></div>
              <div class="ss-img-wrap" data-title="java execution">
                <img src="../assets/images/week-3/week3_step_8.png" alt="java execution" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 10: Program Execution</div>
                <div class="ss-subcaption">Executing <code>java -cp ".:ucanaccess-5.1.2-uber.jar" AccessDemo</code>.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_8.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Step 9 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 11</span><span class="ss-counter-badge">[9 / 9]</span></div>
              <div class="ss-img-wrap" data-title="output records">
                <img src="../assets/images/week-3/week3_step_9.png" alt="output records" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 11: Database Output</div>
                <div class="ss-subcaption">Output records: Connected Successfully; 1 RAMESH 10; 2 MAHESH 20...</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-3/week3_step_9.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <!-- 9. RESULT -->
        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result & Observation</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, connectivity between Java and Microsoft Access (.accdb) was successfully implemented on Ubuntu Linux using the pure Java UCanAccess driver. The database records were queried and printed to the terminal without requiring Microsoft ODBC DSN configuration.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(3)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-3.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_3()
print("Weeks 0 to 3 successfully generated!")

