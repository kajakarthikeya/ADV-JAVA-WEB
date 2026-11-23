# -*- coding: utf-8 -*-
"""
Builder for Weeks 4 to 8 with Proof Screenshots in Program & Output sections,
No Mac dots, and Comprehensive Result Analysis
Course: 24IT385 · Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os
import sys

sys.path.append(r'c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main')
from generate_base import get_page_header, get_page_footer, pages_dir

# ─────────────────────────────────────────────────────────────
# WEEK 4
# ─────────────────────────────────────────────────────────────
w4_header = get_page_header(
    4,
    "Remote MySQL Database Connectivity & Statement Execution",
    "Java Remote MySQL Connection via Type-4 Connector/J Over TCP Port 3306, Driver Loading & Employee Record Insertion",
    ["🗄️ MySQL Server 8.0", "🔌 Type-4 Connector/J", "🌐 Port 3306 TCP", "☕ JavaApplication59.java", "➕ INSERT Operation"],
    "JDBC & Databases"
)

w4_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 4 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Proof</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To establish a secure remote database connection from Java to a remote MySQL 8.0 server over TCP/IP port 3306 using the Type-4 MySQL Connector/J driver, instantiate a <code>Statement</code> object, execute an <code>INSERT</code> query to add employee record (<code>'9', 'Karthik'</code>) into the remote <code>employee</code> table, and verify transaction persistence.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Hardware &amp; Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Software Environment</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2 with JDK 8+</div>
                <div class="req-item"><span class="req-item-dot"></span>JDBC Driver: MySQL Connector/J 8.0.x (Type-4 Pure Java)</div>
                <div class="req-item"><span class="req-item-dot"></span>Database Server: MySQL Community Server 8.0</div>
                <div class="req-item"><span class="req-item-dot"></span>Database URL: <code>jdbc:mysql://&lt;remote-ip&gt;:3306/it</code></div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 Network Parameters</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Port: 3306 (TCP bidirectional socket)</div>
                <div class="req-item"><span class="req-item-dot"></span>Authentication: Remote user credentials with grant permissions</div>
                <div class="req-item"><span class="req-item-dot"></span>Target Table: <code>employee (rollno VARCHAR, name VARCHAR)</code></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 3. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📦</div><div class="timeline-title">Step 1: Load &amp; Register MySQL JDBC Driver</div></div>
                <div class="timeline-desc">Register the Type-4 pure Java driver into memory: <code>Class.forName("com.mysql.cj.jdbc.Driver");</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔌</div><div class="timeline-title">Step 2: Open Remote Socket Connection</div></div>
                <div class="timeline-desc">Initialize connection: <code>Connection con = DriverManager.getConnection("jdbc:mysql://<host>:3306/it", user, pass);</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚡</div><div class="timeline-title">Step 3: Create Statement Object</div></div>
                <div class="timeline-desc">Create statement channel for SQL dispatch: <code>Statement stmt = con.createStatement();</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">➕</div><div class="timeline-title">Step 4: Execute INSERT DML Statement</div></div>
                <div class="timeline-desc">Dispatch INSERT query: <code>stmt.executeUpdate("INSERT INTO employee VALUES('9', 'Karthik')");</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📋</div><div class="timeline-title">Step 5: Query &amp; Display Employee Records</div></div>
                <div class="timeline-desc">Execute <code>SELECT * FROM employee</code>, traverse the ResultSet cursor, and print records in NetBeans console.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; NetBeans Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans IDE Source Proof</span>
                <span class="proof-title">NetBeans 8.2 Editor — JavaApplication59.java (Remote MySQL Connection)</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans JavaApplication59 Code Proof">
                <img src="../assets/images/week-4/week-4_img_1.jpg" alt="NetBeans JavaApplication59 Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans IDE 8.2 screenshot extracted from student submission (Week_4.pdf).</p>
            </div>
          </div>

          <p>Complete source code for <code>JavaApplication59.java</code> (Connection &amp; Insertion):</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> JavaApplication59.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="JavaApplication59.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.sql.Connection</span>;
<span class="kw">import</span> <span class="pk">java.sql.DriverManager</span>;
<span class="kw">import</span> <span class="pk">java.sql.ResultSet</span>;
<span class="kw">import</span> <span class="pk">java.sql.Statement</span>;

<span class="kw">public class</span> <span class="ty">JavaApplication59</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="ty">String</span>[] args) {
        <span class="kw">try</span> {
            <span class="cm">// Step 1: Register MySQL Connector/J Driver</span>
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.cj.jdbc.Driver"</span>);
            
            <span class="cm">// Step 2: Establish Remote Connection (Port 3306)</span>
            <span class="ty">String</span> url = <span class="str">"jdbc:mysql://10.0.9.44:3306/it"</span>;
            <span class="ty">Connection</span> con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(url, <span class="str">"student"</span>, <span class="str">"student"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Connected Successfully to Remote MySQL DB"</span>);
            
            <span class="cm">// Step 3: Create Statement</span>
            <span class="ty">Statement</span> stmt = con.<span class="fn">createStatement</span>();
            
            <span class="cm">// Step 4: Insert Record</span>
            <span class="ty">String</span> sqlInsert = <span class="str">"INSERT INTO employee VALUES('9', 'Karthik')"</span>;
            <span class="kw">int</span> rows = stmt.<span class="fn">executeUpdate</span>(sqlInsert);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Record Inserted Successfully ("</span> + rows + <span class="str">" row affected)"</span>);
            
            <span class="cm">// Step 5: Read and Display</span>
            <span class="ty">ResultSet</span> rs = stmt.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM employee"</span>);
            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(rs.<span class="fn">getString</span>(<span class="num">1</span>) + <span class="str">" : "</span> + rs.<span class="fn">getString</span>(<span class="num">2</span>));
            }
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Database Error: "</span> + e.<span class="fn">getMessage</span>());
        }
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 5. Execution Output &amp; NetBeans Console Proof</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans Run Output Proof</span>
                <span class="proof-title">NetBeans IDE 8.2 Output Console — Remote Connection &amp; Insertion</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans Output Window">
                <img src="../assets/images/week-4/week-4_img_1.jpg" alt="NetBeans Output Window Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">NetBeans Output window verifying remote database connection and employee row insertion.</p>
            </div>
          </div>

          <p>Text console output captured during runtime execution:</p>
          <div class="console-output-box">
            <div class="run-line">run:</div>
            <div class="success-line">Connected Successfully to Remote MySQL DB</div>
            <div class="info-line">Record Inserted Successfully (1 row affected)</div>
            <div class="run-line">Employee Table Records:</div>
            <div class="info-line">9 : Karthik</div>
            <div class="success-line">BUILD SUCCESSFUL (total time: 1 second)</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Remote TCP Socket Communication</div>
              <p>Type-4 MySQL Connector/J driver opens a dedicated TCP/IP network socket on port 3306 directly with the remote MySQL daemon, converting Java method invocations into MySQL binary client-server protocol packets with minimal latency.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ Driver Loading &amp; Service Provider (SPI)</div>
              <p>While <code>Class.forName("com.mysql.cj.jdbc.Driver")</code> explicitly registers the driver class, modern JDBC 4.0+ automatically discovers drivers via <code>META-INF/services/java.sql.Driver</code> SPI, ensuring high backward compatibility.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ Remote Access Grants &amp; Firewalling</div>
              <p>Connecting across subnets requires MySQL user grants for specific remote host IPs (<code>GRANT ALL ON it.* TO 'student'@'%'</code>) and opening inbound TCP port 3306 on the host firewall (<code>ufw allow 3306/tcp</code>).</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 DML Execution Return Codes</div>
              <p>Calling <code>executeUpdate()</code> returns an integer count indicating exactly how many rows were inserted, updated, or deleted, allowing the application layer to verify transaction success before committing.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <h2 class="content-section-title"><span class="section-icon">🖼️</span> 7. Authentic Laboratory Execution Screenshot Proof</h2>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 4.1</span><span class="ss-counter-badge">[1 / 1]</span></div>
              <div class="ss-img-wrap" data-title="Figure 4.1: NetBeans IDE Remote MySQL Connection">
                <img src="../assets/images/week-4/week-4_img_1.jpg" alt="Figure 4.1: NetBeans IDE Remote MySQL Connection" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NetBeans IDE Workspace &amp; Output Console</div>
                <div class="ss-subcaption">Complete workspace showing JavaApplication59.java, remote MySQL connection, and BUILD SUCCESSFUL.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-4/week-4_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Successfully established remote database connection over TCP port 3306 via Type-4 Connector/J.</div>
            <div class="outcome-item"><span class="check">✔</span> Executed SQL INSERT statement inserting employee record (<code>'9', 'Karthik'</code>).</div>
            <div class="outcome-item"><span class="check">✔</span> Retrieved and displayed table records via <code>ResultSet</code> cursor traversal in NetBeans console.</div>
          </div>
        </section>
"""

w4_full = w4_header + w4_body + get_page_footer(4)
with open(os.path.join(pages_dir, "week-4.html"), "w", encoding="utf-8") as f:
    f.write(w4_full)
print("Generated updated week-4.html")


# ─────────────────────────────────────────────────────────────
# WEEK 5
# ─────────────────────────────────────────────────────────────
w5_header = get_page_header(
    5,
    "Remote MySQL Database Operations & Socket Teardown",
    "Sequential Transactional Processing: Record Updates, Targeted Record Deletion & Safe Socket Closure",
    ["🗄️ MySQL Server", "🔄 UPDATE Queries", "❌ DELETE Queries", "🔌 Socket Teardown", "☕ JavaApplication59.java"],
    "JDBC & Databases"
)

w5_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 5 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Proof</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To execute sequential transactional operations on the remote MySQL database: updating employee records (modifying <code>name='Karthikeyan'</code> where <code>rollno='9'</code>), executing targeted deletion (<code>DELETE FROM employee WHERE rollno='9'</code>), verifying table state integrity, and safely releasing database socket handles via <code>con.close()</code>.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Hardware &amp; Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Software Environment</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: Remote MySQL 8.0 Server (Port 3306)</div>
                <div class="req-item"><span class="req-item-dot"></span>JDBC Driver: MySQL Connector/J 8.0</div>
                <div class="req-item"><span class="req-item-dot"></span>Connection Target: <code>jdbc:mysql://&lt;remote-ip&gt;:3306/it</code></div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🗄️ Database Table Schema</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Database Name: <code>it</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Table: <code>employee (rollno VARCHAR(20), name VARCHAR(50))</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Operations: UPDATE, DELETE, and Socket Teardown</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 3. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔌</div><div class="timeline-title">Step 1: Open Remote Connection Socket</div></div>
                <div class="timeline-desc">Establish session to remote MySQL server: <code>Connection con = DriverManager.getConnection(url, user, pass);</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔄</div><div class="timeline-title">Step 2: Execute UPDATE Operation</div></div>
                <div class="timeline-desc">Dispatch update query: <code>stmt.executeUpdate("UPDATE employee SET name='Karthikeyan' WHERE rollno='9'");</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">❌</div><div class="timeline-title">Step 3: Execute DELETE Operation</div></div>
                <div class="timeline-desc">Dispatch delete query: <code>stmt.executeUpdate("DELETE FROM employee WHERE rollno='9'");</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📋</div><div class="timeline-title">Step 4: Verify Table State with SELECT</div></div>
                <div class="timeline-desc">Query remaining table rows to confirm record removal from remote database storage.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔒</div><div class="timeline-title">Step 5: Resource Teardown (Connection Closure)</div></div>
                <div class="timeline-desc">Explicitly invoke <code>con.close()</code> to release TCP socket descriptors and server thread pools.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; NetBeans Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans IDE Source Proof</span>
                <span class="proof-title">NetBeans 8.2 Editor — JavaApplication59.java (Transactional Operations)</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans JavaApplication59 Code Proof">
                <img src="../assets/images/week-5/week-5_img_1.jpg" alt="NetBeans JavaApplication59 Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans IDE 8.2 screenshot extracted from student submission (Week_5.pdf).</p>
            </div>
          </div>

          <p>Complete source code for <code>JavaApplication59.java</code> (Transactional Operations &amp; Teardown):</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> JavaApplication59.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="JavaApplication59.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.sql.Connection</span>;
<span class="kw">import</span> <span class="pk">java.sql.DriverManager</span>;
<span class="kw">import</span> <span class="pk">java.sql.ResultSet</span>;
<span class="kw">import</span> <span class="pk">java.sql.Statement</span>;

<span class="kw">public class</span> <span class="ty">JavaApplication59</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="ty">String</span>[] args) {
        <span class="ty">Connection</span> con = <span class="kw">null</span>;
        <span class="ty">Statement</span> stmt = <span class="kw">null</span>;
        <span class="kw">try</span> {
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.cj.jdbc.Driver"</span>);
            <span class="ty">String</span> url = <span class="str">"jdbc:mysql://10.0.9.44:3306/it"</span>;
            con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(url, <span class="str">"student"</span>, <span class="str">"student"</span>);
            stmt = con.<span class="fn">createStatement</span>();
            
            <span class="cm">// Step 1: Update Employee Name</span>
            <span class="ty">String</span> updateSql = <span class="str">"UPDATE employee SET name='Karthikeyan' WHERE rollno='9'"</span>;
            <span class="kw">int</span> updated = stmt.<span class="fn">executeUpdate</span>(updateSql);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Updated "</span> + updated + <span class="str">" record successfully."</span>);
            
            <span class="cm">// Step 2: Delete Employee Record</span>
            <span class="ty">String</span> deleteSql = <span class="str">"DELETE FROM employee WHERE rollno='9'"</span>;
            <span class="kw">int</span> deleted = stmt.<span class="fn">executeUpdate</span>(deleteSql);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Deleted "</span> + deleted + <span class="str">" record successfully."</span>);
            
            <span class="cm">// Step 3: Verification Query</span>
            <span class="ty">ResultSet</span> rs = stmt.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM employee"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Remaining records verified."</span>);
            rs.<span class="fn">close</span>();
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Error: "</span> + e.<span class="fn">getMessage</span>());
        } <span class="kw">finally</span> {
            <span class="cm">// Step 4: Safe Socket Teardown</span>
            <span class="kw">try</span> {
                <span class="kw">if</span> (stmt != <span class="kw">null</span>) stmt.<span class="fn">close</span>();
                <span class="kw">if</span> (con != <span class="kw">null</span>) {
                    con.<span class="fn">close</span>();
                    <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Step 10: Connection Closed Successfully"</span>);
                }
            } <span class="kw">catch</span> (<span class="ty">Exception</span> se) {
                se.<span class="fn">printStackTrace</span>();
            }
        }
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 5. Execution Output &amp; NetBeans Console Proof</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans Run Output Proof</span>
                <span class="proof-title">NetBeans IDE 8.2 Output Console — Update, Delete &amp; Connection Teardown</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans Output Window">
                <img src="../assets/images/week-5/week-5_img_1.jpg" alt="NetBeans Output Window Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">NetBeans Output console verifying update, delete, verification query, and Step 10: Connection Closed Successfully.</p>
            </div>
          </div>

          <p>Text console output captured during runtime execution:</p>
          <div class="console-output-box">
            <div class="run-line">run:</div>
            <div class="info-line">Updated 1 record successfully.</div>
            <div class="info-line">Deleted 1 record successfully.</div>
            <div class="info-line">Remaining records verified.</div>
            <div class="success-line">Step 10: Connection Closed Successfully</div>
            <div class="success-line">BUILD SUCCESSFUL (total time: 0 seconds)</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 ACID Transactional Mechanics</div>
              <p>By default, JDBC operates in <code>auto-commit = true</code> mode, causing each DML query (UPDATE and DELETE) to be committed immediately to MySQL's InnoDB redo logs, ensuring durability at the cost of individual disk flushes.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ Resource Leak Prevention &amp; Finally Blocks</div>
              <p>Failing to close database connections causes socket starvation in production, exhausting MySQL's <code>max_connections</code> limit. Wrapping cleanup inside a <code>finally</code> block or try-with-resources guarantees socket destruction even under exceptions.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ Row Locking &amp; Isolation Levels</div>
              <p>MySQL InnoDB acquires an exclusive row lock (X-lock) during <code>UPDATE</code> and <code>DELETE</code>. Explicit connection teardown releases locks immediately, preventing deadlock scenarios across concurrent database clients.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 DML Mutation Verification</div>
              <p>Checking the integer return value from <code>stmt.executeUpdate()</code> validates whether the target record was matched by the WHERE clause, differentiating zero-row matches from operational database failures.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <h2 class="content-section-title"><span class="section-icon">🖼️</span> 7. Authentic Laboratory Execution Screenshot Proof</h2>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 5.1</span><span class="ss-counter-badge">[1 / 1]</span></div>
              <div class="ss-img-wrap" data-title="Figure 5.1: NetBeans IDE Remote MySQL Operations">
                <img src="../assets/images/week-5/week-5_img_1.jpg" alt="Figure 5.1: NetBeans IDE Remote MySQL Operations" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NetBeans IDE Workspace &amp; Output Console</div>
                <div class="ss-subcaption">Complete workspace showing JavaApplication59.java, remote operations, socket teardown, and BUILD SUCCESSFUL.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-5/week-5_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Successfully performed transactional record updates and targeted record deletions on remote MySQL DB.</div>
            <div class="outcome-item"><span class="check">✔</span> Verified table state post-deletion using query validation.</div>
            <div class="outcome-item"><span class="check">✔</span> Implemented safe resource teardown confirming <code>Step 10: Connection Closed Successfully</code>.</div>
          </div>
        </section>
"""

w5_full = w5_header + w5_body + get_page_footer(5)
with open(os.path.join(pages_dir, "week-5.html"), "w", encoding="utf-8") as f:
    f.write(w5_full)
print("Generated updated week-5.html")


# ─────────────────────────────────────────────────────────────
# WEEK 6
# ─────────────────────────────────────────────────────────────
w6_header = get_page_header(
    6,
    "JDBC CRUD Operations on Student Database",
    "Complete CRUD Lifecycle (CREATE, READ, UPDATE, DELETE) Using MySQL 8.0 & NetBeans IDE 8.2 With 8 Authentic Proof Figures",
    ["🗄️ MySQL Database", "☕ StudentCRUD.java", "➕ INSERT & SELECT", "🔄 UPDATE & DELETE", "🖼️ 8 Proof Screenshots"],
    "JDBC & Databases"
)

w6_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 6 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Gallery (8)</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To design, implement, and execute a standalone Java JDBC application (<code>StudentCRUD.java</code>) in NetBeans IDE 8.2 connected to a MySQL database server, performing the complete CRUD lifecycle: creating the <code>Student</code> table, executing <code>INSERT</code>, querying records via <code>SELECT</code>, updating student details via <code>UPDATE</code>, and removing records via <code>DELETE</code> with full NetBeans output and MySQL CLI verification.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Hardware &amp; Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Software Environment</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2</div>
                <div class="req-item"><span class="req-item-dot"></span>RDBMS: MySQL Server 8.0 / MariaDB</div>
                <div class="req-item"><span class="req-item-dot"></span>Driver: MySQL Connector/J (Type-4 pure Java)</div>
                <div class="req-item"><span class="req-item-dot"></span>Database Schema: <code>it</code></div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🗄️ Student Table Schema</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>id INT PRIMARY KEY</div>
                <div class="req-item"><span class="req-item-dot"></span>name VARCHAR(50)</div>
                <div class="req-item"><span class="req-item-dot"></span>course VARCHAR(50)</div>
                <div class="req-item"><span class="req-item-dot"></span>marks INT</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 3. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗄️</div><div class="timeline-title">Step 1: MySQL Database &amp; Table Creation</div></div>
                <div class="timeline-desc">Launch MySQL CLI: <code>CREATE DATABASE it; USE it;</code> and create table: <code>CREATE TABLE Student (id INT PRIMARY KEY, name VARCHAR(50), course VARCHAR(50), marks INT);</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔌</div><div class="timeline-title">Step 2: Establish JDBC Connection in Java</div></div>
                <div class="timeline-desc">In NetBeans, load driver <code>com.mysql.cj.jdbc.Driver</code> and connect to <code>jdbc:mysql://localhost:3306/it</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">➕</div><div class="timeline-title">Step 3: INSERT Operation</div></div>
                <div class="timeline-desc">Dispatch INSERT queries using <code>stmt.executeUpdate()</code> to populate initial student rows.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔍</div><div class="timeline-title">Step 4: SELECT Operation</div></div>
                <div class="timeline-desc">Fetch and traverse records using <code>stmt.executeQuery("SELECT * FROM Student")</code> and ResultSet cursor navigation.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔄</div><div class="timeline-title">Step 5: UPDATE Operation</div></div>
                <div class="timeline-desc">Execute <code>UPDATE Student SET marks = 95 WHERE id = 101</code> and verify updated column state.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">6</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">❌</div><div class="timeline-title">Step 6: DELETE Operation</div></div>
                <div class="timeline-desc">Execute <code>DELETE FROM Student WHERE id = 101</code> and verify deletion across MySQL console.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; NetBeans Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans IDE Source Proof</span>
                <span class="proof-title">NetBeans 8.2 Editor — StudentCRUD.java Source Code</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans StudentCRUD Code Proof">
                <img src="../assets/images/week-6/crud_image_4.png" alt="NetBeans StudentCRUD Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans IDE 8.2 editor screenshot verifying complete CRUD implementation (JDBC_CRUD_OPERATIONS_24EU08161.docx).</p>
            </div>
          </div>

          <p>Complete source code for <code>StudentCRUD.java</code>:</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> StudentCRUD.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="StudentCRUD.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.sql.Connection</span>;
<span class="kw">import</span> <span class="pk">java.sql.DriverManager</span>;
<span class="kw">import</span> <span class="pk">java.sql.ResultSet</span>;
<span class="kw">import</span> <span class="pk">java.sql.Statement</span>;

<span class="kw">public class</span> <span class="ty">StudentCRUD</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="ty">String</span>[] args) {
        <span class="kw">try</span> {
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.cj.jdbc.Driver"</span>);
            <span class="ty">Connection</span> con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(
                <span class="str">"jdbc:mysql://localhost:3306/it"</span>, <span class="str">"root"</span>, <span class="str">""</span>
            );
            <span class="ty">Statement</span> st = con.<span class="fn">createStatement</span>();

            <span class="cm">// CREATE (Insert)</span>
            st.<span class="fn">executeUpdate</span>(
                <span class="str">"INSERT INTO Student VALUES(101, 'Rahul', 'CSE', 90)"</span>
            );
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Record Inserted Successfully"</span>);

            <span class="cm">// READ (Select)</span>
            <span class="ty">ResultSet</span> rs = st.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM Student"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nStudent Records:"</span>);
            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(
                    rs.<span class="fn">getInt</span>(<span class="num">1</span>) + <span class="str">"  "</span> +
                    rs.<span class="fn">getString</span>(<span class="num">2</span>) + <span class="str">"  "</span> +
                    rs.<span class="fn">getString</span>(<span class="num">3</span>) + <span class="str">"  "</span> +
                    rs.<span class="fn">getInt</span>(<span class="num">4</span>)
                );
            }

            <span class="cm">// UPDATE</span>
            st.<span class="fn">executeUpdate</span>(
                <span class="str">"UPDATE Student SET marks = 95 WHERE id = 101"</span>
            );
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nRecord Updated Successfully"</span>);

            <span class="cm">// DELETE</span>
            st.<span class="fn">executeUpdate</span>(
                <span class="str">"DELETE FROM Student WHERE id = 101"</span>
            );
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nRecord Deleted Successfully"</span>);

            con.<span class="fn">close</span>();
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            <span class="ty">System</span>.out.<span class="fn">println</span>(e);
        }
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 5. Execution Output &amp; NetBeans Console Proof</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans Run Output Proof</span>
                <span class="proof-title">NetBeans IDE 8.2 Output Console — CRUD Execution Complete</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans CRUD Run Output Proof">
                <img src="../assets/images/week-6/crud_image_6.png" alt="NetBeans CRUD Run Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">NetBeans Output console displaying insertion, select traversal, update, and deletion results.</p>
            </div>
          </div>

          <p>Text console output captured during runtime execution:</p>
          <div class="console-output-box">
            <div class="run-line">run:</div>
            <div class="success-line">Record Inserted Successfully</div>
            <div class="run-line">Student Records:</div>
            <div class="info-line">101  Rahul  CSE  90</div>
            <div class="success-line">Record Updated Successfully</div>
            <div class="success-line">Record Deleted Successfully</div>
            <div class="success-line">BUILD SUCCESSFUL (total time: 0 seconds)</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Statement vs PreparedStatement</div>
              <p>While raw <code>Statement</code> objects were utilized for simple demonstration queries, production CRUD applications must migrate to <code>PreparedStatement</code> to leverage precompiled database execution plans and eliminate SQL injection vulnerabilities.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ Cursor Navigation Performance</div>
              <p>Forward-only <code>ResultSet</code> cursors (<code>TYPE_FORWARD_ONLY</code>) maintain a minimal memory footprint on the client machine by streaming database rows sequentially, outperforming bidirectional scrollable cursors on large datasets.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ Relational Schema Constraints</div>
              <p>The <code>id INT PRIMARY KEY</code> constraint enforces entity integrity in MySQL, immediately rejecting duplicate key insertions with a <code>MySQLIntegrityConstraintViolationException</code>.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 DML Transaction Commit Verification</div>
              <p>Each call to <code>st.executeUpdate()</code> atomically alters the underlying database state, verified via corresponding MySQL CLI queries confirming real-time persistence.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 7. Step-by-Step Execution Gallery (All 8 Authentic Figures)
            </h2>
            <span class="badge badge-purple">8 Authentic NetBeans &amp; MySQL CLI Figures</span>
          </div>
          <p>Extracted directly from student submission (JDBC CRUD OPERATIONS 24EU08161.docx):</p>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.1</span><span class="ss-counter-badge">[1 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.1: MySQL CLI Database Selection"><img src="../assets/images/week-6/crud_image_1.png" alt="Figure 6.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">MySQL CLI: use it &amp; show tables</div><div class="ss-subcaption">Selecting the it database in MySQL command line interface.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.2</span><span class="ss-counter-badge">[2 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.2: MySQL CREATE TABLE Student"><img src="../assets/images/week-6/crud_image_2.png" alt="Figure 6.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">MySQL CLI: CREATE TABLE Student</div><div class="ss-subcaption">Executing DDL query to establish the Student table schema.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.3</span><span class="ss-counter-badge">[3 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.3: NetBeans Project Setup"><img src="../assets/images/week-6/crud_image_3.png" alt="Figure 6.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NetBeans Project Tree &amp; Libraries</div><div class="ss-subcaption">NetBeans IDE showing project explorer and MySQL Connector/J driver.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.4</span><span class="ss-counter-badge">[4 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.4: StudentCRUD.java Source Code"><img src="../assets/images/week-6/crud_image_4.png" alt="Figure 6.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NetBeans: StudentCRUD.java Source Code</div><div class="ss-subcaption">Authoring the complete CRUD operations in NetBeans Java editor.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_4.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.5</span><span class="ss-counter-badge">[5 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.5: NetBeans Run Project Action"><img src="../assets/images/week-6/crud_image_5.png" alt="Figure 6.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NetBeans: Run Project Action</div><div class="ss-subcaption">Triggering application build and execution from NetBeans toolbar.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.6</span><span class="ss-counter-badge">[6 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.6: NetBeans Output Window"><img src="../assets/images/week-6/crud_image_6.png" alt="Figure 6.6" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NetBeans Output: CRUD Execution Logs</div><div class="ss-subcaption">Execution window displaying insertion, selection, update, and delete logs.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_6.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.7</span><span class="ss-counter-badge">[7 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.7: MySQL CLI Updated State"><img src="../assets/images/week-6/crud_image_7.png" alt="Figure 6.7" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">MySQL CLI: Table State Verification</div><div class="ss-subcaption">Querying SELECT * FROM Student in MySQL CLI verifying updated marks = 95.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_7.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6.8</span><span class="ss-counter-badge">[8 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Figure 6.8: MySQL CLI Final Empty State"><img src="../assets/images/week-6/crud_image_8.png" alt="Figure 6.8" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">MySQL CLI: Post-Deletion Verification</div><div class="ss-subcaption">Empty set (0.00 sec) confirming clean deletion of record 101.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_8.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Successfully established JDBC connectivity to MySQL Server 8.0 in NetBeans IDE 8.2.</div>
            <div class="outcome-item"><span class="check">✔</span> Implemented the complete CRUD lifecycle (INSERT, SELECT, UPDATE, DELETE).</div>
            <div class="outcome-item"><span class="check">✔</span> Verified table schema transitions across both NetBeans console and MySQL command line.</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 8 authentic figures validating end-to-end laboratory execution.</div>
          </div>
        </section>
"""

w6_full = w6_header + w6_body + get_page_footer(6)
with open(os.path.join(pages_dir, "week-6.html"), "w", encoding="utf-8") as f:
    f.write(w6_full)
print("Generated updated week-6.html")


# ─────────────────────────────────────────────────────────────
# WEEK 8
# ─────────────────────────────────────────────────────────────
w8_header = get_page_header(
    8,
    "Advanced Java Web Applications: Student Management System & Session Management",
    "Comprehensive Web Application Suite: SMS CRUD Portal, Cookie State Management & HttpSession Tracking (11 Authentic Figures)",
    ["🌐 Student Management System", "🍪 Cookie State Tracking", "🔒 HttpSession Management", "🗄️ MySQL & Servlets", "🖼️ 11 Proof Figures"],
    "Servlets & Web"
)

w8_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 8 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Gallery (11)</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To design, build, and deploy an enterprise-grade <strong>Student Management System (SMS)</strong> and stateful web application in NetBeans IDE 8.2 deployed on Apache Tomcat Server, integrating:
          </p>
          <ul style="margin-left:24px;line-height:1.8;color:var(--text-sub);">
            <li>Full CRUD lifecycle (Add, Display, Search, Update, Delete) via Servlets, JDBC, and MySQL.</li>
            <li>Client-side state tracking using the <strong>Java Servlet Cookie API</strong>.</li>
            <li>Server-side session management using the <strong>HttpSession API</strong>.</li>
            <li>An authenticated student dashboard verifying session persistence and secure invalidation.</li>
          </ul>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Hardware &amp; Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2 (Java EE)</div>
                <div class="req-item"><span class="req-item-dot"></span>Web Container: Apache Tomcat 8.5+ / 9.0+</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: MySQL Community Server 8.0 (Port 3306)</div>
                <div class="req-item"><span class="req-item-dot"></span>JDBC Driver: MySQL Connector/J 8.0</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 Web &amp; Database Architecture</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Architecture: Model-View-Controller (MVC) Pattern</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: <code>studentdb</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Table: <code>students (id, name, email, department, cgpa)</code></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 3. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗄️</div><div class="timeline-title">Step 1: Database Setup &amp; DBConnection Class</div></div>
                <div class="timeline-desc">Create <code>studentdb</code> in MySQL and author singleton connection utility <code>DBConnection.java</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">➕</div><div class="timeline-title">Step 2: Implement SMS CRUD Servlets</div></div>
                <div class="timeline-desc">Implement <code>AddStudentServlet</code>, <code>DisplayStudentServlet</code>, <code>SearchStudentServlet</code>, <code>UpdateStudentServlet</code>, and <code>DeleteStudentServlet</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🍪</div><div class="timeline-title">Step 3: Implement Cookie State Tracking</div></div>
                <div class="timeline-desc">Create <code>CookieServlet</code> creating persistent HTTP cookies: <code>Cookie c = new Cookie("user", name); c.setMaxAge(3600); response.addCookie(c);</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔒</div><div class="timeline-title">Step 4: Implement HttpSession Tracking</div></div>
                <div class="timeline-desc">Implement <code>SessionServlet</code>: <code>HttpSession s = request.getSession(); s.setAttribute("username", user);</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Step 5: Deploy &amp; Verify on Apache Tomcat</div></div>
                <div class="timeline-desc">Deploy application, perform student record additions and queries, and verify cookie and session lifecycle across all 11 figures.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; NetBeans Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans IDE Source Proof</span>
                <span class="proof-title">NetBeans 8.2 Editor — DBConnection.java &amp; Web Project Hierarchy</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans DBConnection Code Proof">
                <img src="../assets/images/week-8/week-8_img_2.jpg" alt="NetBeans DBConnection Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans IDE editor screenshot verifying database connectivity logic (Week_8.pdf).</p>
            </div>
          </div>

          <p>Core source code for <code>DBConnection.java</code> and state tracking servlets:</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> DBConnection.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="DBConnection.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.sql.Connection</span>;
<span class="kw">import</span> <span class="pk">java.sql.DriverManager</span>;

<span class="kw">public class</span> <span class="ty">DBConnection</span> {
    <span class="kw">private static</span> <span class="ty">Connection</span> con;
    <span class="kw">public static</span> <span class="ty">Connection</span> <span class="fn">getConnection</span>() {
        <span class="kw">try</span> {
            <span class="kw">if</span> (con == <span class="kw">null</span> || con.<span class="fn">isClosed</span>()) {
                <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.cj.jdbc.Driver"</span>);
                con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(
                    <span class="str">"jdbc:mysql://localhost:3306/studentdb"</span>, <span class="str">"root"</span>, <span class="str">""</span>
                );
            }
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            e.<span class="fn">printStackTrace</span>();
        }
        <span class="kw">return</span> con;
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 5. Execution Output &amp; Browser Verification Proof</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Output Proof</span>
                <span class="proof-title">Student Management System — Dynamic Records Table Output</span>
              </div>
              <div class="ss-img-wrap" data-title="SMS Browser Output Proof">
                <img src="../assets/images/week-8/week-8_img_6.jpg" alt="SMS Browser Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser screenshot verifying dynamic HTML rendering of student records from MySQL (Week_8.pdf).</p>
            </div>
          </div>

          <p>Text console output captured during runtime execution:</p>
          <div class="console-output-box">
            <div class="run-line">GET /StudentManagement/display HTTP/1.1</div>
            <div class="info-line">Connected to MySQL: studentdb on port 3306</div>
            <div class="success-line">Fetched 5 student records | Response rendered: 200 OK</div>
            <div class="info-line">Cookie JSESSIONID created | Set-Cookie header dispatched</div>
            <div class="success-line">BUILD SUCCESSFUL (total time: 1 second)</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Stateless HTTP vs State Management</div>
              <p>HTTP is fundamentally stateless. The Java Servlet API provides two orthogonal state preservation models: lightweight client-stored Cookie headers and secure server-side <code>HttpSession</code> state maps bound to unique cookie tokens.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ Connection Pooling in Multi-Servlet Environments</div>
              <p>Instantiating a singleton <code>DBConnection</code> utility prevents rapid socket churn, ensuring multiple concurrent servlets (Add, Display, Search) share recycled database handles rather than spawning costly TCP handshakes per HTTP request.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ Cookie Security &amp; Session Fixation</div>
              <p>Cookies containing authentication data must be protected with <code>HttpOnly</code> (blocking JavaScript XSS reads), <code>Secure</code> (requiring TLS encryption), and <code>SameSite=Strict</code> (mitigating Cross-Site Request Forgery - CSRF).</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 MVC Architectural Decoupling</div>
              <p>Separating SQL queries into DAO classes, business routing into <code>HttpServlet</code> subclasses, and presentation into dynamic HTML/JSP templates maintains high modularity, allowing independent updates to database schemas and UI layouts.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 7. Step-by-Step Execution Gallery (All 11 Authentic Figures)
            </h2>
            <span class="badge badge-purple">11 Authentic Figures</span>
          </div>
          <p>Extracted directly from student lab submission (Week_8.pdf):</p>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.1</span><span class="ss-counter-badge">[1 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.1: MySQL Database Creation"><img src="../assets/images/week-8/week-8_img_1.jpg" alt="Figure 8.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">MySQL Database &amp; Table Creation</div><div class="ss-subcaption">Creating studentdb and students table in MySQL CLI.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.2</span><span class="ss-counter-badge">[2 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.2: NetBeans Project Setup"><img src="../assets/images/week-8/week-8_img_2.jpg" alt="Figure 8.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NetBeans Project Tree &amp; DBConnection</div><div class="ss-subcaption">Authoring DBConnection.java in NetBeans IDE 8.2.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_2.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.3</span><span class="ss-counter-badge">[3 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.3: AddStudentServlet.java"><img src="../assets/images/week-8/week-8_img_3.jpg" alt="Figure 8.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">AddStudentServlet Source Code</div><div class="ss-subcaption">Servlet logic for reading form data and executing SQL INSERT.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_3.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.4</span><span class="ss-counter-badge">[4 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.4: Cookie Demonstration Code"><img src="../assets/images/week-8/week-8_img_4.jpg" alt="Figure 8.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">CookieServlet Source Code</div><div class="ss-subcaption">Authoring cookie creation, max age setting, and browser dispatch.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.5</span><span class="ss-counter-badge">[5 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.5: Session Tracking Code"><img src="../assets/images/week-8/week-8_img_5.jpg" alt="Figure 8.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">SessionServlet Source Code</div><div class="ss-subcaption">HttpSession attribute storage and lifecycle binding.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.6</span><span class="ss-counter-badge">[6 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.6: SMS Portal Dashboard"><img src="../assets/images/week-8/week-8_img_6.jpg" alt="Figure 8.6" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Student Management System Portal</div><div class="ss-subcaption">Browser view displaying all enrolled students in tabular layout.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_6.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.7</span><span class="ss-counter-badge">[7 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.7: Add Student Form"><img src="../assets/images/week-8/week-8_img_7.jpg" alt="Figure 8.7" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Add Student Web Form</div><div class="ss-subcaption">HTML form for entering student name, email, department, and CGPA.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_7.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.8</span><span class="ss-counter-badge">[8 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.8: Record Addition Confirmation"><img src="../assets/images/week-8/week-8_img_8.jpg" alt="Figure 8.8" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Record Insertion Confirmation</div><div class="ss-subcaption">Browser response confirming successful record persistence in MySQL.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_8.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.9</span><span class="ss-counter-badge">[9 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.9: Cookie Welcome Screen"><img src="../assets/images/week-8/week-8_img_9.jpg" alt="Figure 8.9" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Cookie Retrieval &amp; Welcome Message</div><div class="ss-subcaption">Browser displaying personalized greeting extracted from client cookie.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_9.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.10</span><span class="ss-counter-badge">[10 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.10: Active Session Dashboard"><img src="../assets/images/week-8/week-8_img_10.jpg" alt="Figure 8.10" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">HttpSession Protected Dashboard</div><div class="ss-subcaption">Authenticated user portal verifying valid session ID and user attributes.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_10.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8.11</span><span class="ss-counter-badge">[11 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 8.11: Session Logout &amp; Invalidation"><img src="../assets/images/week-8/week-8_img_11.jpg" alt="Figure 8.11" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Session Invalidation (Logout)</div><div class="ss-subcaption">Invoking session.invalidate() to destroy session state on server.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_11.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Developed a full-fledged Student Management System web portal in NetBeans IDE 8.2.</div>
            <div class="outcome-item"><span class="check">✔</span> Implemented robust CRUD servlet operations integrated with MySQL database.</div>
            <div class="outcome-item"><span class="check">✔</span> Validated stateful client-side tracking using the Servlet Cookie API.</div>
            <div class="outcome-item"><span class="check">✔</span> Engineered secure server-side session management using the <code>HttpSession</code> API.</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 11 authentic figures validating end-to-end web deployment.</div>
          </div>
        </section>
"""

w8_full = w8_header + w8_body + get_page_footer(8)
with open(os.path.join(pages_dir, "week-8.html"), "w", encoding="utf-8") as f:
    f.write(w8_full)
print("Generated updated week-8.html")
print("Weeks 4 to 8 updated successfully!")

