import sys
sys.path.append('.')
sys.path.append('JAVA-WEB-main')
from build_weeks_0_to_3_v2 import w0_body
from build_sidebar_helpers import get_step_gallery_html
from step_gallery_data import STEP_GALLERY_DATA
import re

def build_week_0_tasks(is_page=True):
    # Parse individual sections from w0_body
    sec_dict = {}
    for sid, content in re.findall(r'<section[^>]*id=["\'](.*?)["\'][^>]*>([\s\S]*?)</section>', w0_body):
        sec_dict[sid] = f'<section class="content-section" id="{sid}">{content}</section>'

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

    return t1_content + t2_content + t3_content + t4_content + t5_content

print("Week 0 task builder defined successfully!")
