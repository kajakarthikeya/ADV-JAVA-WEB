import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Advanced Java Programming Lab Record (24IT385) | Week 0 – Week 13</title>
  <meta name="description"
    content="Complete Week 0 to Week 13 Digital Laboratory Record for Advanced Java Programming Lab (24IT385). Authored by Venkata Sai Karthikeya Kaja (24EU08161), Department of Information Technology, Siddhartha Academy of Higher Education." />
  <link rel="icon" type="image/svg+xml"
    href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%23059669'/><g fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M9 10c0-2 1.3-2.5 1.3-4.5S9 3.5 9 1.5'/><path d='M16 9c0-2 1.3-2.5 1.3-4.5S16 2.5 16 0.5'/><path d='M23 10c0-2 1.3-2.5 1.3-4.5S23 3.5 23 1.5'/><path d='M6 14h17v8a7 7 0 0 1-7 7h-3a7 7 0 0 1-7-7v-8z' fill='white' fill-opacity='0.25'/><path d='M23 15h3a2.5 2.5 0 0 1 2.5 2.5v2a2.5 2.5 0 0 1-2.5 2.5h-3'/><path d='M3 30h26'/></g></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap"
    rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />
  <link rel="stylesheet" href="style.css" />
</head>

<body>

  <div id="scroll-progress" role="progressbar" aria-hidden="true"></div>

  <!-- LOADER -->
  <div id="loader" aria-hidden="true">
    <div class="loader-ring"></div>
    <div class="loader-logo">Advanced Java Lab Record · 24IT385</div>
  </div>

  <!-- GLASS NAVBAR -->
  <header>
    <nav class="navbar" role="navigation" aria-label="Main navigation">
      <div class="navbar-inner">
        <a href="#hero" class="nav-logo" aria-label="Back to top">
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
          <div class="nav-logo-text">
            <span class="nav-logo-title">Advanced Java Programming</span>
            <span class="nav-logo-sub">Lab Record · 24EU08161</span>
          </div>
        </a>
        <ul class="nav-links" role="list">
          <li><a href="#hero" class="nav-link active">Home</a></li>
          <li><a href="#weeks" class="nav-link">Lab Weeks (0–13)</a></li>
          <li><a href="#curriculum" class="nav-link">Architecture</a></li>
          <li><a href="#downloads" class="nav-link">Downloads</a></li>
          <li><a href="#student" class="nav-link">Student Info</a></li>
        </ul>
        <div class="nav-cta">
          <a href="#weeks" class="btn btn-primary btn-sm">🚀 Explore Weeks 0–13</a>
        </div>
        <button class="hamburger" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>
    <nav class="mobile-nav" aria-label="Mobile navigation">
      <a href="#hero" class="nav-link">🏠 Home</a>
      <a href="#weeks" class="nav-link">📚 All Weeks (0–13)</a>
      <a href="#curriculum" class="nav-link">⚙️ Curriculum &amp; Architecture</a>
      <a href="#downloads" class="nav-link">⬇️ Downloads &amp; Source Code</a>
      <a href="#student" class="nav-link">👨‍🎓 Student Profile</a>
    </nav>
  </header>

  <main>

    <!-- HERO SECTION -->
    <section id="hero"
      style="min-height:90vh;display:flex;align-items:center;padding-top:var(--navbar-h);position:relative;">
      <div class="container hero-inner"
        style="display:grid;grid-template-columns:1.15fr 0.85fr;gap:48px;align-items:center;width:100%;padding:48px 24px;">

        <!-- Left Column -->
        <div class="hero-content">
          <div class="badge badge-green" style="margin-bottom:20px;">
            <span>🎓</span> Advanced Java Programming Lab (24IT385) · Academic Year 2026–2027
          </div>

          <h1
            style="font-family:var(--font-heading);font-size:clamp(2.4rem, 5vw, 3.8rem);font-weight:900;line-height:1.1;letter-spacing:-0.03em;margin-bottom:16px;">
            Week-Wise Digital<br />
            <span
              style="background:linear-gradient(135deg, #059669, #10b981, #14b8a6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Laboratory
              Record</span>
          </h1>

          <p style="font-size:1.1rem;font-weight:700;color:var(--text-main);margin-bottom:8px;">
            Venkata Sai Karthikeya Kaja · Roll No: <span style="color:#059669;">24EU08161</span>
          </p>

          <p style="font-size:0.95rem;color:var(--text-sub);margin-bottom:18px;">
            Department of Information Technology · Siddhartha Academy of Higher Education
          </p>

          <p style="font-size:0.92rem;color:var(--text-muted);line-height:1.75;max-width:560px;margin-bottom:24px;">
            An authoritative, full-semester digital laboratory record covering Week 0 through Week 13.
            Includes complete theoretical analyses, NetBeans &amp; terminal outputs, authentic document screenshots,
            downloadable Java source code, and full Spring Boot JPA architectures.
          </p>

          <!-- Typing Effect Box -->
          <div
            style="font-family:var(--font-code);font-size:0.82rem;color:#047857;padding:12px 18px;background:#ECFDF5;border:1px solid #A7F3D0;border-radius:var(--r-md);margin-bottom:28px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;box-shadow:0 2px 8px rgba(5,150,105,0.08);">
            <span style="color:#059669;font-weight:700;">// </span>
            <span class="hero-typing-text"></span>
          </div>

          <!-- Hero Actions -->
          <div style="display:flex;flex-wrap:wrap;gap:14px;margin-bottom:36px;">
            <a href="#weeks" class="btn btn-primary btn-lg">
              <span>📚</span> Browse Weeks 0–13
            </a>
            <a href="#downloads" class="btn btn-secondary btn-lg">
              <span>⬇️</span> Download Source Files
            </a>
          </div>

          <!-- Hero Stats -->
          <div style="display:flex;gap:36px;padding-top:24px;border-top:1px solid var(--border-glass);">
            <div>
              <div style="font-family:var(--font-heading);font-size:1.8rem;font-weight:900;color:#0F172A;" data-count="14">14</div>
              <div style="font-size:0.72rem;color:var(--text-muted);text-transform:uppercase;font-weight:700;letter-spacing:0.06em;">Lab Weeks (0–13)</div>
            </div>
            <div>
              <div style="font-family:var(--font-heading);font-size:1.8rem;font-weight:900;color:#0F172A;" data-count="60" data-suffix="+">60+</div>
              <div style="font-size:0.72rem;color:var(--text-muted);text-transform:uppercase;font-weight:700;letter-spacing:0.06em;">Authentic Figures</div>
            </div>
            <div>
              <div style="font-family:var(--font-heading);font-size:1.8rem;font-weight:900;color:#0F172A;" data-count="24" data-suffix="+">24+</div>
              <div style="font-size:0.72rem;color:var(--text-muted);text-transform:uppercase;font-weight:700;letter-spacing:0.06em;">Downloadable Codes</div>
            </div>
            <div>
              <div style="font-family:var(--font-heading);font-size:1.8rem;font-weight:900;color:#059669;" data-count="100" data-suffix="%">100%</div>
              <div style="font-size:0.72rem;color:var(--text-muted);text-transform:uppercase;font-weight:700;letter-spacing:0.06em;">Verified Authentic</div>
            </div>
          </div>
        </div>

        <!-- Right Column: Technology Stack Interactive Showcase -->
        <div class="hero-visual" style="display:flex;justify-content:center;">
          <div
            style="background:#FFFFFF;border:1px solid #D1FAE5;border-radius:var(--r-xl);padding:28px;width:100%;max-width:460px;box-shadow:var(--shadow-hover);">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid #ECFDF5;">
              <span style="font-family:var(--font-heading);font-size:0.8rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;color:#059669;">
                Curriculum Progression Matrix
              </span>
              <span class="badge badge-green" style="font-size:0.7rem;">24IT385</span>
            </div>

            <!-- Tier 1 -->
            <div style="padding:10px 14px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:var(--r-md);margin-bottom:10px;display:flex;align-items:center;gap:12px;">
              <div style="width:34px;height:34px;border-radius:8px;background:#ECFDF5;color:#059669;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">0–1</div>
              <div style="flex:1;">
                <div style="font-size:0.85rem;font-weight:700;color:#0F172A;">Core Java &amp; Web Fundamentals</div>
                <div style="font-size:0.72rem;color:#64748B;">Applets, Servlets, JDBC vs ODBC, Cookies &amp; Sessions</div>
              </div>
            </div>

            <!-- Tier 2 -->
            <div style="padding:10px 14px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:var(--r-md);margin-bottom:10px;display:flex;align-items:center;gap:12px;">
              <div style="width:34px;height:34px;border-radius:8px;background:#EFF6FF;color:#2563EB;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">02</div>
              <div style="flex:1;">
                <div style="font-size:0.85rem;font-weight:700;color:#0F172A;">Linux Runtime &amp; JDK 26 Setup</div>
                <div style="font-size:0.72rem;color:#64748B;">OpenJDK SE 26, Ubuntu CLI, update-alternatives</div>
              </div>
            </div>

            <!-- Tier 3 -->
            <div style="padding:10px 14px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:var(--r-md);margin-bottom:10px;display:flex;align-items:center;gap:12px;">
              <div style="width:34px;height:34px;border-radius:8px;background:#FEF3C7;color:#D97706;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">3–6</div>
              <div style="flex:1;">
                <div style="font-size:0.85rem;font-weight:700;color:#0F172A;">Relational Database Connectivity</div>
                <div style="font-size:0.72rem;color:#64748B;">UCanAccess MS Access, Remote MySQL, Student CRUD</div>
              </div>
            </div>

            <!-- Tier 4 -->
            <div style="padding:10px 14px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:var(--r-md);margin-bottom:10px;display:flex;align-items:center;gap:12px;">
              <div style="width:34px;height:34px;border-radius:8px;background:#F3E8FF;color:#9333EA;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">7–8</div>
              <div style="flex:1;">
                <div style="font-size:0.85rem;font-weight:700;color:#0F172A;">Servlets &amp; State Management</div>
                <div style="font-size:0.72rem;color:#64748B;">GenericServlet, HttpServlet, SMS Portal, Cookies</div>
              </div>
            </div>

            <!-- Tier 5 -->
            <div style="padding:10px 14px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:var(--r-md);display:flex;align-items:center;gap:12px;">
              <div style="width:34px;height:34px;border-radius:8px;background:#ECFDF5;color:#059669;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">9–13</div>
              <div style="flex:1;">
                <div style="font-size:0.85rem;font-weight:700;color:#0F172A;">Enterprise Spring Boot &amp; JPA</div>
                <div style="font-size:0.72rem;color:#64748B;">STS Maven, JdbcTemplate, MySQL JPA, Custom Queries</div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- WEEKS 0 TO 13 BROWSER & FILTER SECTION -->
    <section id="weeks" style="padding:72px 24px;background:#F8FAFC;border-top:1px solid #D1FAE5;">
      <div class="container">

        <div style="text-align:center;max-width:760px;margin:0 auto 36px;" class="reveal">
          <div class="badge badge-green" style="margin-bottom:12px;">Complete 14-Week Digital Lab Record</div>
          <h2 style="font-family:var(--font-heading);font-size:2.3rem;font-weight:800;color:#0F172A;margin-bottom:12px;">
            Laboratory Experiments <span
              style="background:linear-gradient(135deg,#059669,#10b981);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">(Week 0 – 13)</span>
          </h2>
          <p style="font-size:0.95rem;color:var(--text-sub);">
            Browse or search all 14 laboratory weeks. Each page includes comprehensive aims, theoretical principles,
            step-by-step procedures, NetBeans &amp; terminal outputs, complete Java source codes, and authentic screenshots.
          </p>
        </div>

        <!-- SEARCH BAR & FILTER CHIPS -->
        <div style="max-width:900px;margin:0 auto 36px;" class="reveal">
          <!-- Search Box -->
          <div style="position:relative;margin-bottom:18px;">
            <input type="text" id="week-search-input" placeholder="🔍  Search by week, topic, code, or keyword (e.g. UCanAccess, CRUD, Servlet, JPA, H2)..."
              style="width:100%;padding:14px 20px 14px 44px;font-size:0.95rem;font-family:var(--font-main);background:#FFFFFF;border:1.5px solid #D1FAE5;border-radius:var(--r-lg);color:#0F172A;box-shadow:var(--shadow-sm);outline:none;transition:all var(--t-fast);" />
            <span style="position:absolute;left:16px;top:50%;transform:translateY(-50%);font-size:1.1rem;color:#059669;pointer-events:none;">⚡</span>
            <button id="search-clear-btn" style="position:absolute;right:14px;top:50%;transform:translateY(-50%);display:none;padding:4px 8px;font-size:0.8rem;background:#ECFDF5;color:#059669;border-radius:6px;font-weight:700;">Clear</button>
          </div>

          <!-- Category Chips -->
          <div class="filter-chips-wrap" style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;">
            <button class="filter-chip active" data-filter="all">All Weeks (14)</button>
            <button class="filter-chip" data-filter="core">Core &amp; Theory (0–1)</button>
            <button class="filter-chip" data-filter="env">Environment (2)</button>
            <button class="filter-chip" data-filter="jdbc">JDBC &amp; Databases (3–6)</button>
            <button class="filter-chip" data-filter="web">Servlets &amp; Web (7–8)</button>
            <button class="filter-chip" data-filter="spring">Spring Boot &amp; JPA (9–13)</button>
          </div>
        </div>

        <!-- 14 WEEK CARDS GRID -->
        <div class="week-cards-grid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:24px;">

          <!-- WEEK 0 -->
          <div class="week-card" data-category="core" data-keywords="week 0 core java advanced java applet servlet jdbc odbc cookie session spring boot standalone web">
            <div class="week-card-header">
              <span class="week-badge">Week 00</span>
              <span class="week-cat-tag">Core &amp; Theory</span>
            </div>
            <h3 class="week-title">Advanced Java Introduction &amp; Theory</h3>
            <p class="week-desc">
              Comprehensive question-and-answer study covering Core vs Advanced Java, Applets vs Servlets, JDBC vs ODBC, Cookies, Sessions, and Spring Boot architecture.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">Java SE/EE</span>
              <span class="tech-tag">Servlets</span>
              <span class="tech-tag">Cookies &amp; Sessions</span>
              <span class="tech-tag">Spring Boot</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-0.html" class="week-explore-btn">
                <span>Explore Week 0</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 1 -->
          <div class="week-card" data-category="core" data-keywords="week 1 lab task 1 comparative matrix c c++ java python javascript technology requirements">
            <div class="week-card-header">
              <span class="week-badge">Week 01</span>
              <span class="week-cat-tag">Core &amp; Theory</span>
            </div>
            <h3 class="week-title">Advanced Java Lab Task 1: Comparative Study</h3>
            <p class="week-desc">
              Multi-dimensional analysis comparing Java, C, C++, Python, and JavaScript across memory management, speed, concurrency, and enterprise readiness.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">Language Matrix</span>
              <span class="tech-tag">JVM vs Interpreters</span>
              <span class="tech-tag">App Paradigms</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-1.html" class="week-explore-btn">
                <span>Explore Week 1</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 2 -->
          <div class="week-card" data-category="env" data-keywords="week 2 java development environment setup openjdk oracle jdk 26 ubuntu tarball java_home path alternatives">
            <div class="week-card-header">
              <span class="week-badge">Week 02</span>
              <span class="week-cat-tag">Environment Setup</span>
            </div>
            <h3 class="week-title">Java Environment Setup: JDK 26 in Ubuntu</h3>
            <p class="week-desc">
              Downloading, extracting, and configuring OpenJDK &amp; Oracle JDK 26 in Ubuntu Linux. Managing update-alternatives, JAVA_HOME, and PATH. Includes original terminal screenshot.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">Ubuntu Linux</span>
              <span class="tech-tag">Oracle JDK 26</span>
              <span class="tech-tag">update-alternatives</span>
              <span class="tech-tag">Bash Scripts</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-2.html" class="week-explore-btn">
                <span>Explore Week 2</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 3 -->
          <div class="week-card" data-category="jdbc" data-keywords="week 3 ms access ucanaccess jdbc jackcess hsqldb accessdemo classpath studentdb">
            <div class="week-card-header">
              <span class="week-badge">Week 03</span>
              <span class="week-cat-tag">JDBC &amp; Databases</span>
            </div>
            <h3 class="week-title">MS Access Connectivity Using UCanAccess</h3>
            <p class="week-desc">
              Configuring pure-Java Type-4 connectivity for Microsoft Access databases using the UCanAccess driver and 5 dependency JARs without native Windows ODBC DSN bridges.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">UCanAccess 5.1.2</span>
              <span class="tech-tag">MS Access</span>
              <span class="tech-tag">Jackcess</span>
              <span class="tech-tag">Classpath</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-3.html" class="week-explore-btn">
                <span>Explore Week 3</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 4 -->
          <div class="week-card" data-category="jdbc" data-keywords="week 4 remote mysql database connectivity port 3306 drivermanager employee insert select">
            <div class="week-card-header">
              <span class="week-badge">Week 04</span>
              <span class="week-cat-tag">JDBC &amp; Databases</span>
            </div>
            <h3 class="week-title">Remote MySQL Database Connectivity</h3>
            <p class="week-desc">
              Connecting Java to a remote MySQL 8.0 server over TCP/IP port 3306 via Connector/J Type-4 driver. Record insertion, roster display, and original NetBeans output.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">MySQL Connector/J</span>
              <span class="tech-tag">Remote DB 3306</span>
              <span class="tech-tag">DriverManager</span>
              <span class="tech-tag">SQL INSERT</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-4.html" class="week-explore-btn">
                <span>Explore Week 4</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 5 -->
          <div class="week-card" data-category="jdbc" data-keywords="week 5 remote mysql database operations update delete verification connection close">
            <div class="week-card-header">
              <span class="week-badge">Week 05</span>
              <span class="week-cat-tag">JDBC &amp; Databases</span>
            </div>
            <h3 class="week-title">Remote MySQL Operations &amp; Teardown</h3>
            <p class="week-desc">
              Sequential transactional operations on remote MySQL database: updating employee records, deleting records, verification queries, and safe socket cleanup.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">SQL UPDATE</span>
              <span class="tech-tag">SQL DELETE</span>
              <span class="tech-tag">Socket Teardown</span>
              <span class="tech-tag">ResultSet</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-5.html" class="week-explore-btn">
                <span>Explore Week 5</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 6 -->
          <div class="week-card" data-category="jdbc" data-keywords="week 6 jdbc crud operations student database insert select update delete netbeans mysql">
            <div class="week-card-header">
              <span class="week-badge">Week 06</span>
              <span class="week-cat-tag">JDBC &amp; Databases</span>
            </div>
            <h3 class="week-title">JDBC CRUD Operations on Student Database</h3>
            <p class="week-desc">
              Full CRUD lifecycle (Create, Read, Update, Delete) on student table in MySQL. NetBeans execution with 8 authentic command prompt and IDE screenshot captures.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">Student CRUD</span>
              <span class="tech-tag">PreparedStatement</span>
              <span class="tech-tag">NetBeans IDE</span>
              <span class="tech-tag">MySQL CLI</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-6.html" class="week-explore-btn">
                <span>Explore Week 6</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 7 -->
          <div class="week-card" data-category="web" data-keywords="week 7 generic servlet http servlet netbeans glassfish tomcat web application html form doget dopost">
            <div class="week-card-header">
              <span class="week-badge">Week 07</span>
              <span class="week-cat-tag">Servlets &amp; Web</span>
            </div>
            <h3 class="week-title">Generic Servlet &amp; HTTP Servlet in NetBeans</h3>
            <p class="week-desc">
              Web application creation in NetBeans: comparing protocol-independent GenericServlet with protocol-specific HttpServlet, handling HTML forms, and browser dispatch.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">HttpServlet</span>
              <span class="tech-tag">GenericServlet</span>
              <span class="tech-tag">HTML5 Forms</span>
              <span class="tech-tag">GlassFish / Tomcat</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-7.html" class="week-explore-btn">
                <span>Explore Week 7</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 8 -->
          <div class="week-card" data-category="web" data-keywords="week 8 advanced java web applications student management system cookies session tracking servlets jdbc mysql">
            <div class="week-card-header">
              <span class="week-badge">Week 08</span>
              <span class="week-cat-tag">Servlets &amp; Web</span>
            </div>
            <h3 class="week-title">Advanced Java Web Apps &amp; Session Management</h3>
            <p class="week-desc">
              4 practical modules: Full Student Management System (SMS) via Servlets &amp; JDBC, client-side Cookie tracking, server-side HttpSession management, and portal integration.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">SMS CRUD Portal</span>
              <span class="tech-tag">Cookie API</span>
              <span class="tech-tag">HttpSession</span>
              <span class="tech-tag">11 Figures</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-8.html" class="week-explore-btn">
                <span>Explore Week 8</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 9 -->
          <div class="week-card" data-category="spring" data-keywords="week 9 maven spring boot development sts springmavendemo studentmanagement pom.xml clean install">
            <div class="week-card-header">
              <span class="week-badge">Week 09</span>
              <span class="week-cat-tag">Spring Boot &amp; JPA</span>
            </div>
            <h3 class="week-title">Maven &amp; Spring Boot Development in STS</h3>
            <p class="week-desc">
              3 structured activities in Spring Tool Suite (STS): creating Maven archetype projects, developing REST web applications, and comprehensive POM.xml dependency configuration.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">Spring Tool Suite</span>
              <span class="tech-tag">Maven Build</span>
              <span class="tech-tag">POM.xml</span>
              <span class="tech-tag">REST Controllers</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-9.html" class="week-explore-btn">
                <span>Explore Week 9</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 10 -->
          <div class="week-card" data-category="spring" data-keywords="week 10 spring boot jdbctemplate h2 in-memory database author author service rowmapper batch insert">
            <div class="week-card-header">
              <span class="week-badge">Week 10</span>
              <span class="week-cat-tag">Spring Boot &amp; JPA</span>
            </div>
            <h3 class="week-title">Spring Boot JdbcTemplate with In-Memory H2</h3>
            <p class="week-desc">
              Automated database connectivity via Spring's JdbcTemplate with in-memory H2 DB. Author domain entity, RowMapper row mapping, batch insert, and H2 web console testing.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">JdbcTemplate</span>
              <span class="tech-tag">H2 Database</span>
              <span class="tech-tag">RowMapper</span>
              <span class="tech-tag">@PostConstruct</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-10.html" class="week-explore-btn">
                <span>Explore Week 10</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 11 -->
          <div class="week-card" data-category="spring" data-keywords="week 11 spring boot jpa mysql thymeleaf employee repository employee controller hibernate">
            <div class="week-card-header">
              <span class="week-badge">Week 11</span>
              <span class="week-cat-tag">Spring Boot &amp; JPA</span>
            </div>
            <h3 class="week-title">Spring Boot JPA with MySQL &amp; Thymeleaf Web UI</h3>
            <p class="week-desc">
              Full-stack enterprise application with Spring Data JPA and MySQL. Employee entity, JpaRepository interface, REST API endpoints, and Thymeleaf server-side rendered HTML UI.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">Spring Data JPA</span>
              <span class="tech-tag">MySQL Server</span>
              <span class="tech-tag">Thymeleaf UI</span>
              <span class="tech-tag">Hibernate ORM</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-11.html" class="week-explore-btn">
                <span>Explore Week 11</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 12 -->
          <div class="week-card" data-category="spring" data-keywords="week 12 spring data jpa h2 student repository student controller rest requestparam jparepository">
            <div class="week-card-header">
              <span class="week-badge">Week 12</span>
              <span class="week-cat-tag">Spring Boot &amp; JPA</span>
            </div>
            <h3 class="week-title">Spring Data JPA Repository with In-Memory H2</h3>
            <p class="week-desc">
              Rapid API development utilizing JpaRepository for automated CRUD operations on Student entities. URL request parameter binding (@RequestParam) and H2 browser console.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">JpaRepository</span>
              <span class="tech-tag">H2 Console</span>
              <span class="tech-tag">@RequestParam</span>
              <span class="tech-tag">JSON Output</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-12.html" class="week-explore-btn">
                <span>Explore Week 12</span> <span>→</span>
              </a>
            </div>
          </div>

          <!-- WEEK 13 -->
          <div class="week-card" data-category="spring" data-keywords="week 13 derived custom query methods spring data jpa findby query jpql native sql">
            <div class="week-card-header">
              <span class="week-badge">Week 13</span>
              <span class="week-cat-tag">Spring Boot &amp; JPA</span>
            </div>
            <h3 class="week-title">Derived &amp; Custom Query Methods in Spring Data JPA</h3>
            <p class="week-desc">
              All 8 prescribed query derivations: findByName, findByFirstName, And/Or clauses, OrderBy, First10, and custom native SQL execution with @Query annotations.
            </p>
            <div class="week-tech-tags">
              <span class="tech-tag">Derived Queries</span>
              <span class="tech-tag">@Query Annotation</span>
              <span class="tech-tag">JPQL &amp; Native SQL</span>
              <span class="tech-tag">8 Query Patterns</span>
            </div>
            <div class="week-card-footer">
              <a href="pages/week-13.html" class="week-explore-btn">
                <span>Explore Week 13</span> <span>→</span>
              </a>
            </div>
          </div>

        </div>

        <!-- No search results fallback message -->
        <div id="no-weeks-found" style="display:none;text-align:center;padding:48px 24px;background:#FFFFFF;border:1px dashed #A7F3D0;border-radius:var(--r-xl);margin-top:24px;">
          <div style="font-size:2rem;margin-bottom:8px;">🔍</div>
          <h3 style="font-family:var(--font-heading);color:#0F172A;font-weight:700;">No matching laboratory weeks found</h3>
          <p style="font-size:0.9rem;color:#64748B;">Try searching for a different keyword or click "All Weeks".</p>
        </div>

      </div>
    </section>

    <!-- ARCHITECTURE & ROADMAP SECTION -->
    <section id="curriculum" style="padding:72px 24px;background:#FFFFFF;border-top:1px solid #D1FAE5;border-bottom:1px solid #D1FAE5;">
      <div class="container">
        <div style="text-align:center;max-width:700px;margin:0 auto 48px;" class="reveal">
          <div class="badge badge-green" style="margin-bottom:12px;">Curriculum Architecture</div>
          <h2 style="font-family:var(--font-heading);font-size:2.2rem;font-weight:800;color:#0F172A;margin-bottom:12px;">
            5 Structural Pillars of <span
              style="background:linear-gradient(135deg,#059669,#10b981);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Advanced Java</span>
          </h2>
          <p style="font-size:0.95rem;color:var(--text-sub);">
            The laboratory curriculum builds systematically from foundational JVM architectural concepts to modern cloud-ready enterprise microservices.
          </p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:24px;" class="reveal">

          <div class="pillar-card">
            <div class="pillar-icon">🏛️</div>
            <h3 class="pillar-title">1. Language Foundations</h3>
            <div class="pillar-weeks">Weeks 0 – 1</div>
            <p class="pillar-desc">
              Contrasting Core Java with Enterprise Java, examining desktop applet sunsetting, introducing servlet architectures, and multi-language comparative evaluations.
            </p>
          </div>

          <div class="pillar-card">
            <div class="pillar-icon">🐧</div>
            <h3 class="pillar-title">2. Linux Runtime Config</h3>
            <div class="pillar-weeks">Week 2</div>
            <p class="pillar-desc">
              Automated deployment of bleeding-edge OpenJDK &amp; Oracle JDK 26 in Ubuntu Linux systems, maintaining runtime alternatives, JAVA_HOME, and execution paths.
            </p>
          </div>

          <div class="pillar-card">
            <div class="pillar-icon">🔌</div>
            <h3 class="pillar-title">3. JDBC &amp; Database Engines</h3>
            <div class="pillar-weeks">Weeks 3 – 6</div>
            <p class="pillar-desc">
              Heterogeneous connectivity across MS Access (UCanAccess) and MySQL 8.0, PreparedStatement security, parameterized batching, and full CRUD implementations.
            </p>
          </div>

          <div class="pillar-card">
            <div class="pillar-icon">🌐</div>
            <h3 class="pillar-title">4. Servlets &amp; State Management</h3>
            <div class="pillar-weeks">Weeks 7 – 8</div>
            <p class="pillar-desc">
              NetBeans web application development, HTTP lifecycle dispatching, Student Management System portals, Cookie state tracking, and session security.
            </p>
          </div>

          <div class="pillar-card">
            <div class="pillar-icon">🍃</div>
            <h3 class="pillar-title">5. Enterprise Spring Boot &amp; JPA</h3>
            <div class="pillar-weeks">Weeks 9 – 13</div>
            <p class="pillar-desc">
              Spring Tool Suite Maven lifecycle, JdbcTemplate, Hibernate ORM, MySQL and in-memory H2 databases, REST controllers, and advanced JPA derived queries.
            </p>
          </div>

        </div>
      </div>
    </section>

    <!-- DOWNLOADS SECTION -->
    <section id="downloads" style="padding:72px 24px;background:#F8FAFC;">
      <div class="container">

        <div style="text-align:center;max-width:700px;margin:0 auto 48px;" class="reveal">
          <div class="badge badge-green" style="margin-bottom:12px;">Centralized Resources</div>
          <h2 style="font-family:var(--font-heading);font-size:2.2rem;font-weight:800;color:#0F172A;margin-bottom:12px;">
            Download <span
              style="background:linear-gradient(135deg,#059669,#10b981);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Source Code &amp; Documents</span>
          </h2>
          <p style="font-size:0.95rem;color:var(--text-sub);">
            Direct access to all 24+ validated Java source files, SQL database schema scripts, Maven POM files, Linux shell scripts, and original lab assignment documents.
          </p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:24px;" class="reveal">

          <!-- Java Source Files -->
          <div class="resource-card">
            <div style="font-size:2rem;margin-bottom:14px;">☕</div>
            <h3 style="font-family:var(--font-heading);font-size:1.1rem;font-weight:700;color:#0F172A;margin-bottom:8px;">
              Java Source Files (.java)
            </h3>
            <p style="font-size:0.84rem;color:#64748B;line-height:1.6;margin-bottom:18px;">
              Complete standalone Java classes, servlets, JPA entities, repositories, and controllers for all weeks.
            </p>
            <div style="display:flex;flex-direction:column;gap:8px;">
              <a href="assets/downloads/StudentCRUD.java" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>📄</span> Download StudentCRUD.java (W6)
              </a>
              <a href="assets/downloads/AccessDemo.java" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>📄</span> Download AccessDemo.java (W3)
              </a>
              <a href="assets/downloads/EmployeeController.java" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>📄</span> Download EmployeeController.java (W11)
              </a>
            </div>
          </div>

          <!-- SQL Database Scripts -->
          <div class="resource-card">
            <div style="font-size:2rem;margin-bottom:14px;">🗄️</div>
            <h3 style="font-family:var(--font-heading);font-size:1.1rem;font-weight:700;color:#0F172A;margin-bottom:8px;">
              Database Schemas (.sql)
            </h3>
            <p style="font-size:0.84rem;color:#64748B;line-height:1.6;margin-bottom:18px;">
              Production-ready DDL and DML scripts for MySQL databases, student records, employee tables, and sample data.
            </p>
            <div style="display:flex;flex-direction:column;gap:8px;">
              <a href="assets/downloads/schema_student.sql" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>💾</span> Download schema_student.sql
              </a>
              <a href="assets/downloads/studentdb_schema.sql" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>💾</span> Download studentdb_schema.sql
              </a>
              <a href="pages/week-6.html#procedure" class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>🔍</span> View Full SQL Schemas in W6
              </a>
            </div>
          </div>

          <!-- Configuration & Build Scripts -->
          <div class="resource-card">
            <div style="font-size:2rem;margin-bottom:14px;">⚙️</div>
            <h3 style="font-family:var(--font-heading);font-size:1.1rem;font-weight:700;color:#0F172A;margin-bottom:8px;">
              Build &amp; Shell Scripts
            </h3>
            <p style="font-size:0.84rem;color:#64748B;line-height:1.6;margin-bottom:18px;">
              Linux automation shell scripts for JDK 26 installation and enterprise Maven pom.xml configuration files.
            </p>
            <div style="display:flex;flex-direction:column;gap:8px;">
              <a href="assets/downloads/setup_jdk26.sh" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>🐧</span> Download setup_jdk26.sh (W2)
              </a>
              <a href="assets/downloads/pom.xml" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>📦</span> Download pom.xml (W9)
              </a>
              <a href="pages/week-9.html#activity3" class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>🔍</span> View STS POM Configuration
              </a>
            </div>
          </div>

          <!-- Original Source Documents Archive -->
          <div class="resource-card">
            <div style="font-size:2rem;margin-bottom:14px;">📑</div>
            <h3 style="font-family:var(--font-heading);font-size:1.1rem;font-weight:700;color:#0F172A;margin-bottom:8px;">
              Original Lab Documents
            </h3>
            <p style="font-size:0.84rem;color:#64748B;line-height:1.6;margin-bottom:18px;">
              Archive of all authoritative lab manual submissions, DOCX tasks, and ODT records provided for verification.
            </p>
            <div style="display:flex;flex-direction:column;gap:8px;">
              <a href="assets/documents/Week_0.odt" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>📘</span> Week_0.odt Source File
              </a>
              <a href="assets/documents/JDBC_CRUD_OPERATIONS_24EU08161.docx" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>📘</span> Week 6 CRUD Docx File
              </a>
              <a href="assets/documents/Week_13.pdf" download class="btn btn-secondary btn-sm" style="justify-content:flex-start;">
                <span>📘</span> Week 13 Derived Queries PDF
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- STUDENT CONTACT SECTION -->
    <section id="student"
      style="padding:72px 24px;background:#FFFFFF;border-top:1px solid #D1FAE5;">
      <div class="container">

        <div style="text-align:center;max-width:680px;margin:0 auto 48px;" class="reveal">
          <div class="badge badge-green" style="margin-bottom:12px;">Author &amp; Course Identity</div>
          <h2 style="font-family:var(--font-heading);font-size:2.2rem;font-weight:800;color:#0F172A;margin-bottom:12px;">
            Student <span
              style="background:linear-gradient(135deg,#059669,#10b981);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Profile
              &amp; Record Metadata</span>
          </h2>
          <p style="font-size:0.95rem;color:var(--text-sub);">
            Official candidate credentials and course registration details for Advanced Java Programming Lab (24IT385).
          </p>
        </div>

        <div class="student-card reveal">
          <div class="student-card-title">👨‍🎓 Student Laboratory Record Information</div>

          <div class="student-grid">

            <div class="student-item">
              <div class="student-icon">👤</div>
              <div>
                <div class="student-label">Student Name</div>
                <div class="student-val">VENKATA SAI KARTHIKEYA KAJA</div>
              </div>
            </div>

            <div class="student-item">
              <div class="student-icon">🆔</div>
              <div>
                <div class="student-label">Roll Number</div>
                <div class="student-val" style="color:#059669;font-weight:900;">24EU08161</div>
              </div>
            </div>

            <div class="student-item">
              <div class="student-icon">🏛️</div>
              <div>
                <div class="student-label">Department</div>
                <div class="student-val">INFORMATION TECHNOLOGY</div>
              </div>
            </div>

            <div class="student-item">
              <div class="student-icon">🏷️</div>
              <div>
                <div class="student-label">Course Code &amp; Title</div>
                <div class="student-val">24IT385 · ADVANCED JAVA PROGRAMMING LAB</div>
              </div>
            </div>

            <div class="student-item">
              <div class="student-icon">🏫</div>
              <div>
                <div class="student-label">Institution</div>
                <div class="student-val">SIDDHARTHA ACADEMY OF HIGHER EDUCATION</div>
              </div>
            </div>

            <div class="student-item">
              <div class="student-icon">📅</div>
              <div>
                <div class="student-label">Academic Year</div>
                <div class="student-val">2026 – 2027</div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer style="padding:48px 24px 32px;border-top:1px solid #D1FAE5;background:#FFFFFF;">
    <div class="container"
      style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="nav-logo-icon" aria-label="Java Logo">
          <svg class="coffee-cup-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path class="steam steam-1" d="M6 7c0-1.5 1-2 1-3.5S6 2 6 0.5"></path>
            <path class="steam steam-2" d="M12 6c0-1.5 1-2 1-3.5S12 1 12 0"></path>
            <path class="steam steam-3" d="M18 7c0-1.5 1-2 1-3.5S18 2 18 0.5"></path>
            <path d="M4 10h13v6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5v-6z" fill="#059669" fill-opacity="0.15"></path>
            <path d="M17 11h2.5a2 2 0 0 1 2 2v1.5a2 2 0 0 1-2 2H17"></path>
            <path d="M2 22h19"></path>
          </svg>
        </div>
        <div>
          <div style="font-family:var(--font-heading);font-size:0.95rem;font-weight:800;color:#0F172A;">
            Advanced Java Programming Lab Record (24IT385)
          </div>
          <div style="font-size:0.75rem;color:#64748B;">
            Venkata Sai Karthikeya Kaja · Roll No: 24EU08161 · IT Department
          </div>
        </div>
      </div>
      <div style="font-size:0.8rem;color:#64748B;">
        © 2026–2027 Siddhartha Academy of Higher Education. Digital Lab Record Submission.
      </div>
    </div>
  </footer>

  <!-- FULLSCREEN LIGHTBOX ZOOM MODAL WITH PREV / NEXT CYCLING -->
  <div id="zoom-modal" class="modal-overlay" aria-hidden="true" role="dialog">
    <div class="modal-content">
      <span class="modal-close" title="Close Modal">&times;</span>
      <button class="modal-nav-btn modal-prev" title="Previous Image">&#10094;</button>
      <button class="modal-nav-btn modal-next" title="Next Image">&#10095;</button>
      <img src="" alt="Zoomed Screenshot" class="modal-img" />
      <div class="modal-caption"></div>
    </div>
  </div>

  <button id="back-to-top" aria-label="Back to top">↑</button>

  <script src="script.js"></script>
</body>

</html>
"""

with open(r'c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print("index.html written successfully!")

