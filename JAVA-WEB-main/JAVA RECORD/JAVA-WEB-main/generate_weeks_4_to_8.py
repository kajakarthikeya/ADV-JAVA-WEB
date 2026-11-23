# -*- coding: utf-8 -*-
"""
Generator for Weeks 4 to 8
Advanced Java Programming Lab (24IT385)
Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os
from generate_base import get_page_header, get_page_footer

pages_dir = r'C:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\pages'

# ==============================================================================
# WEEK 4: Remote MySQL Database Connectivity
# ==============================================================================
def generate_week_4():
    header = get_page_header(
        4,
        "Remote MySQL Database Connectivity",
        "Connecting to Remote MySQL Server over TCP/IP (10.0.9.20:3306) and Record Insertion",
        ["🐬 Remote MySQL (10.0.9.20:3306)", "🗄️ Database: ai", "📦 Package: javaapplication59", "📝 Class: JavaApplication59"],
        "JDBC & Databases"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 4 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview</a>
          <a href="#requirements" class="toc-item">3. Requirements</a>
          <a href="#procedure" class="toc-item">4. Procedure</a>
          <a href="#program" class="toc-item">5. Java Program</a>
          <a href="#explanation" class="toc-item">6. Program Explanation</a>
          <a href="#output" class="toc-item">7. NetBeans Output</a>
          <a href="#screenshots" class="toc-item">8. Screenshot Gallery</a>
          <a href="#result" class="toc-item">9. Result & Observation</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To design, implement, and execute a Java JDBC program (<code>JavaApplication59.java</code>) connecting to a remote MySQL database server over a TCP/IP network connection (<code>10.0.9.20:3306/ai</code>), initialize a statement, execute an INSERT operation for employee record ('9', 'Karthik'), and display the resulting dataset.
          </p>
        </section>

        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Overview</h2>
          <p>
            In production enterprise architectures, database engines do not reside on local client workstations but are centralized on dedicated server nodes. JDBC Type-4 drivers (pure Java network protocol drivers) translate JDBC API calls directly into the database vendor's native network protocol. By specifying a socket address (IP: <code>10.0.9.20</code> and Port: <code>3306</code>) in the JDBC connection string, client applications establish raw TCP stream communication with the remote mysqld daemon.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 3. System Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware & Network</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Client RAM: 4 GB minimum</div>
                <div class="req-item"><span class="req-item-dot"></span>Network: Local Area Network (LAN) routing to <code>10.0.9.20</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Remote Port: TCP Port 3306 open</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Software Specifications</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE 8+ / OpenJDK</div>
                <div class="req-item"><span class="req-item-dot"></span>Driver: MySQL Connector/J (com.mysql.jdbc.Driver)</div>
                <div class="req-item"><span class="req-item-dot"></span>Remote DB: MySQL <code>ai</code> with table <code>employee</code></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔌</div><div class="timeline-title">Step 1: Load MySQL JDBC Driver</div></div>
                <div class="timeline-desc">Register MySQL Connector/J with DriverManager via <code>Class.forName("com.mysql.jdbc.Driver")</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Step 2: Connect to Remote Server</div></div>
                <div class="timeline-desc">Open socket connection to <code>jdbc:mysql://10.0.9.20:3306/ai</code> with credentials (username: <code>root</code>, password: <code>""</code>).</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📜</div><div class="timeline-title">Step 3: Create Statement Object</div></div>
                <div class="timeline-desc">Create <code>Statement st = con.createStatement()</code> to execute remote SQL queries.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">➕</div><div class="timeline-title">Step 4: Execute Record Insertion</div></div>
                <div class="timeline-desc">Execute <code>st.executeUpdate("INSERT INTO employee VALUES('9','Karthik')")</code> and verify row count &gt; 0.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📊</div><div class="timeline-title">Step 5: Query & Display Records</div></div>
                <div class="timeline-desc">Execute <code>SELECT * FROM employee</code> and iterate over ResultSet cursor, displaying <code>rollno</code> and <code>name</code>.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 5. Java Program (JavaApplication59.java)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">JavaApplication59.java</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="JavaApplication59.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <div class="line-numbers" aria-hidden="true">1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35</div>
              <pre><code><span class="kw">package</span> <span class="pk">javaapplication59</span>;

<span class="kw">import</span> <span class="pk">java.sql.*</span>;

<span class="kw">public class</span> <span class="ty">JavaApplication59</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="ty">String</span>[] args) {
        <span class="kw">try</span> {
            <span class="co">// Step 1: Load Driver</span>
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.jdbc.Driver"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Step 1: JDBC Driver Loaded Successfully."</span>);

            <span class="co">// Step 2: Connect to Remote Database</span>
            <span class="ty">Connection</span> con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(
                <span class="str">"jdbc:mysql://10.0.9.20:3306/ai"</span>,
                <span class="str">"root"</span>,
                <span class="str">""</span>
            );
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Step 2: Remote Connection Established Successfully."</span>);

            <span class="co">// Step 3: Create Statement</span>
            <span class="ty">Statement</span> st = con.<span class="fn">createStatement</span>();
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Step 3: Statement Created Successfully."</span>);

            <span class="co">// Step 4: Insert Record</span>
            <span class="kw">int</span> i = st.<span class="fn">executeUpdate</span>(<span class="str">"INSERT INTO employee VALUES('9','Karthik')"</span>);
            <span class="kw">if</span> (i &gt; 0) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nStep 4: Record Inserted Successfully."</span>);
            }

            <span class="co">// Step 5: Display Records</span>
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\n===== Records After Insert ====="</span>);
            <span class="ty">ResultSet</span> rs = st.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM employee"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Roll No\\tName"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"--------------------------"</span>);
            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(rs.<span class="fn">getString</span>(<span class="str">"rollno"</span>) + <span class="str">"\\t"</span> + rs.<span class="fn">getString</span>(<span class="str">"name"</span>));
            }
            rs.<span class="fn">close</span>();
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            e.<span class="fn">printStackTrace</span>();
        }
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="explanation">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 6. Program Explanation</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Line / Expression</th>
                  <th>Component</th>
                  <th>Explanation</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>"jdbc:mysql://10.0.9.20:3306/ai"</code></td>
                  <td>Remote Connection URL</td>
                  <td>Target server IP (10.0.9.20), listening port (3306), and database schema name (ai).</td>
                </tr>
                <tr>
                  <td><code>st.executeUpdate("INSERT INTO employee...")</code></td>
                  <td>DML Execution</td>
                  <td>Dispatches insert query across socket to insert employee ID 9 with name Karthik.</td>
                </tr>
                <tr>
                  <td><code>rs.getString("rollno")</code></td>
                  <td>Column Value Fetch</td>
                  <td>Extracts the value of column rollno from the active row of the ResultSet cursor.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 7. NetBeans IDE Output</h2>
          <div class="netbeans-output">
            <div class="netbeans-header">
              <div class="netbeans-tabs"><div class="netbeans-tab"><span class="netbeans-tab-icon">☕</span> JavaApplication59 (run)</div></div>
              <div class="netbeans-actions"><span class="nb-status-badge">SUCCESS</span></div>
            </div>
            <div class="netbeans-body">
              <span class="nb-line-run">run:</span>
              <span class="nb-line-info">Step 1: JDBC Driver Loaded Successfully.</span>
              <span class="nb-line-info">Step 2: Remote Connection Established Successfully.</span>
              <span class="nb-line-info">Step 3: Statement Created Successfully.</span>
              <span class="nb-line-info">Step 4: Record Inserted Successfully.</span>
              <br />
              <span class="nb-line-out">===== Records After Insert =====</span>
              <span class="nb-line-out">Roll No	Name</span>
              <span class="nb-line-out">--------------------------</span>
              <span class="nb-line-out">7	akhil</span>
              <span class="nb-line-out">2	harshith</span>
              <span class="nb-line-out">3	haswika</span>
              <span class="nb-line-out" style="color:#4ade80;font-weight:bold;">9	Karthik</span>
              <span class="nb-line-out">8	priya</span>
              <span class="nb-line-out">1	ramesh</span>
              <span class="nb-line-out">6	sailendra</span>
              <span class="nb-line-out">5	suresh</span>
            </div>
          </div>
        </section>

        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Original Lab Output Screenshot
            </h2>
            <span class="badge badge-purple">Authentic PDF Screenshot</span>
          </div>
          <p>Extracted directly from original laboratory record document (Week_4.pdf):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Execution Proof</span><span class="ss-counter-badge">[1 / 1]</span></div>
              <div class="ss-img-wrap" data-title="Remote MySQL Output: Insertion Verification">
                <img src="../assets/images/week-4/week-4_img_1.jpg" alt="Remote MySQL Output Insertion Verification" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NetBeans Remote MySQL Output</div>
                <div class="ss-subcaption">Authentic console telemetry showing remote connection, insertion of record '9 Karthik', and employee roster.</div>
                <div class="ss-actions">
                  <button class="ss-btn ss-replace-btn">📷 Replace Image</button>
                  <a href="../assets/images/week-4/week-4_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a>
                  <input type="file" class="ss-file-input" accept="image/*" />
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result & Observation</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, remote MySQL database connectivity was successfully established over TCP/IP port 3306 at address 10.0.9.20. The employee record ('9', 'Karthik') was persisted, and the updated remote table records were verified.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(4)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-4.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_4()

# ==============================================================================
# WEEK 5: Remote MySQL Database Operations
# ==============================================================================
def generate_week_5():
    header = get_page_header(
        5,
        "Remote MySQL Database Operations",
        "Record Update, Deletion, State Verification, and Resource Cleanup",
        ["🐬 Remote MySQL (10.0.9.20:3306)", "🔄 Record Update & Delete", "🔒 Lifecycle Management", "✅ BUILD SUCCESSFUL"],
        "JDBC & Databases"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 5 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview</a>
          <a href="#requirements" class="toc-item">3. Requirements</a>
          <a href="#procedure" class="toc-item">4. Procedure</a>
          <a href="#program" class="toc-item">5. Java Program</a>
          <a href="#explanation" class="toc-item">6. Program Explanation</a>
          <a href="#output" class="toc-item">7. NetBeans Output</a>
          <a href="#screenshots" class="toc-item">8. Screenshot Gallery</a>
          <a href="#result" class="toc-item">9. Result & Observation</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To execute advanced transactional manipulation on a remote MySQL database over JDBC (<code>10.0.9.20:3306/ai</code>), updating employee record 9 to 'Karthikeyan', subsequently deleting the record, verifying state at each phase, and closing all database connection sockets cleanly.
          </p>
        </section>

        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Overview</h2>
          <p>
            Operating across networked databases necessitates resilient query lifecycle management. Modifications executed via <code>UPDATE</code> and <code>DELETE</code> statements must be verified through immediate cursor queries to confirm transactional integrity. Furthermore, explicitly releasing database resources (closing <code>ResultSet</code>, <code>Statement</code>, and <code>Connection</code>) in reverse order of creation prevents remote connection leakage and memory leaks on enterprise database servers.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 3. System Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Network & Client</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Client OS: Windows 10/11 / Linux</div>
                <div class="req-item"><span class="req-item-dot"></span>Network: Socket connection to <code>10.0.9.20:3306</code></div>
                <div class="req-item"><span class="req-item-dot"></span>RAM: 4 GB minimum</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Software Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE 8+ / OpenJDK</div>
                <div class="req-item"><span class="req-item-dot"></span>Driver: MySQL Connector/J</div>
                <div class="req-item"><span class="req-item-dot"></span>Remote Schema: <code>ai.employee</code></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">6</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">✏️</div><div class="timeline-title">Step 6: Update Employee Record</div></div>
                <div class="timeline-desc">Execute <code>UPDATE employee SET name='Karthikeyan' WHERE rollno='9'</code> via <code>st.executeUpdate()</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">7</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔍</div><div class="timeline-title">Step 7: Verify Updated Dataset</div></div>
                <div class="timeline-desc">Query <code>SELECT * FROM employee</code> to verify that rollno 9 now displays 'Karthikeyan'.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">8</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗑️</div><div class="timeline-title">Step 8: Delete Employee Record</div></div>
                <div class="timeline-desc">Execute <code>DELETE FROM employee WHERE rollno='9'</code> and verify positive integer return code.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">9</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📋</div><div class="timeline-title">Step 9: Confirm Record Deletion</div></div>
                <div class="timeline-desc">Query <code>SELECT * FROM employee</code> to verify rollno 9 is completely purged from table.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">10</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔒</div><div class="timeline-title">Step 10: Close Connection Sockets</div></div>
                <div class="timeline-desc">Invoke <code>rs.close()</code>, <code>st.close()</code>, and <code>con.close()</code> and print completion confirmation.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 5. Complete Java Program (JavaApplication59.java)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">JavaApplication59.java</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="JavaApplication59.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <div class="line-numbers" aria-hidden="true">1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58</div>
              <pre><code><span class="kw">package</span> <span class="pk">javaapplication59</span>;

<span class="kw">import</span> <span class="pk">java.sql.*</span>;

<span class="kw">public class</span> <span class="ty">JavaApplication59</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="ty">String</span>[] args) {
        <span class="kw">try</span> {
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.jdbc.Driver"</span>);
            <span class="ty">Connection</span> con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(
                <span class="str">"jdbc:mysql://10.0.9.20:3306/ai"</span>, <span class="str">"root"</span>, <span class="str">""</span>
            );
            <span class="ty">Statement</span> st = con.<span class="fn">createStatement</span>();

            <span class="co">// Step 6: Update Record</span>
            <span class="kw">int</span> u = st.<span class="fn">executeUpdate</span>(<span class="str">"UPDATE employee SET name='Karthikeyan' WHERE rollno='9'"</span>);
            <span class="kw">if</span> (u &gt; 0) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nStep 6: Record Updated Successfully."</span>);
            }

            <span class="co">// Step 7: Display After Update</span>
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\n===== Records After Update ====="</span>);
            <span class="ty">ResultSet</span> rs = st.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM employee"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Roll No\\tName"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"--------------------------"</span>);
            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(rs.<span class="fn">getString</span>(<span class="str">"rollno"</span>) + <span class="str">"\\t"</span> + rs.<span class="fn">getString</span>(<span class="str">"name"</span>));
            }
            rs.<span class="fn">close</span>();

            <span class="co">// Step 8: Delete Record</span>
            <span class="kw">int</span> d = st.<span class="fn">executeUpdate</span>(<span class="str">"DELETE FROM employee WHERE rollno='9'"</span>);
            <span class="kw">if</span> (d &gt; 0) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nStep 8: Record Deleted Successfully."</span>);
            }

            <span class="co">// Step 9: Display After Delete</span>
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\n===== Records After Delete ====="</span>);
            rs = st.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM employee"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Roll No\\tName"</span>);
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"--------------------------"</span>);
            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(rs.<span class="fn">getString</span>(<span class="str">"rollno"</span>) + <span class="str">"\\t"</span> + rs.<span class="fn">getString</span>(<span class="str">"name"</span>));
            }
            rs.<span class="fn">close</span>();
            st.<span class="fn">close</span>();
            con.<span class="fn">close</span>();

            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nStep 10: Connection Closed Successfully."</span>);
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            e.<span class="fn">printStackTrace</span>();
        }
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="explanation">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 6. Program Explanation</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Method / Statement</th>
                  <th>Action</th>
                  <th>Outcome</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>st.executeUpdate("UPDATE ... WHERE rollno='9'")</code></td>
                  <td>Data Modification</td>
                  <td>Updates employee tuple attribute from 'Karthik' to 'Karthikeyan'.</td>
                </tr>
                <tr>
                  <td><code>st.executeUpdate("DELETE ... WHERE rollno='9'")</code></td>
                  <td>Data Deletion</td>
                  <td>Removes tuple matching rollno 9, returning affected row count (1).</td>
                </tr>
                <tr>
                  <td><code>con.close()</code></td>
                  <td>Connection Cleanup</td>
                  <td>Terminates the TCP socket connection to remote MySQL server safely.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 7. NetBeans IDE Output</h2>
          <div class="netbeans-output">
            <div class="netbeans-header">
              <div class="netbeans-tabs"><div class="netbeans-tab"><span class="netbeans-tab-icon">☕</span> JavaApplication59 (run)</div></div>
              <div class="netbeans-actions"><span class="nb-status-badge">SUCCESS</span></div>
            </div>
            <div class="netbeans-body">
              <span class="nb-line-info">Step 6: Record Updated Successfully.</span>
              <br />
              <span class="nb-line-out">===== Records After Update =====</span>
              <span class="nb-line-out">Roll No	Name</span>
              <span class="nb-line-out">--------------------------</span>
              <span class="nb-line-out">7	akhil</span>
              <span class="nb-line-out">2	harshith</span>
              <span class="nb-line-out">3	haswika</span>
              <span class="nb-line-out" style="color:#4ade80;font-weight:bold;">9	Karthikeyan</span>
              <span class="nb-line-out">8	priya</span>
              <span class="nb-line-out">1	ramesh</span>
              <span class="nb-line-out">6	sailendra</span>
              <span class="nb-line-out">5	suresh</span>
              <br />
              <span class="nb-line-info">Step 8: Record Deleted Successfully.</span>
              <br />
              <span class="nb-line-out">===== Records After Delete =====</span>
              <span class="nb-line-out">Roll No	Name</span>
              <span class="nb-line-out">--------------------------</span>
              <span class="nb-line-out">7	akhil</span>
              <span class="nb-line-out">2	harshith</span>
              <span class="nb-line-out">3	haswika</span>
              <span class="nb-line-out">8	priya</span>
              <span class="nb-line-out">1	ramesh</span>
              <span class="nb-line-out">6	sailendra</span>
              <span class="nb-line-out">5	suresh</span>
              <br />
              <span class="nb-line-info">Step 10: Connection Closed Successfully.</span>
              <span class="nb-line-success" style="color:#4ade80;font-weight:bold;">BUILD SUCCESSFUL (total time: 0 seconds)</span>
            </div>
          </div>
        </section>

        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Original Lab Output Screenshot
            </h2>
            <span class="badge badge-purple">Authentic PDF Screenshot</span>
          </div>
          <p>Extracted directly from original laboratory record document (Week_5.pdf):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Execution Proof</span><span class="ss-counter-badge">[1 / 1]</span></div>
              <div class="ss-img-wrap" data-title="Remote MySQL Output: Update, Delete & BUILD SUCCESSFUL">
                <img src="../assets/images/week-5/week-5_img_1.jpg" alt="Remote MySQL Output Update Delete Verification" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NetBeans Output Telemetry</div>
                <div class="ss-subcaption">Authentic console log displaying Step 6 (Update), Step 8 (Delete), Step 10 (Close), and BUILD SUCCESSFUL.</div>
                <div class="ss-actions">
                  <button class="ss-btn ss-replace-btn">📷 Replace Image</button>
                  <a href="../assets/images/week-5/week-5_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a>
                  <input type="file" class="ss-file-input" accept="image/*" />
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result & Observation</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, remote database update and delete operations were successfully performed over JDBC on the employee table. Both state transitions were verified via intermediate queries, and remote sockets were closed successfully.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(5)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-5.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_5()

# ==============================================================================
# WEEK 6: JDBC CRUD Operations
# ==============================================================================
def generate_week_6():
    header = get_page_header(
        6,
        "JDBC Program to Perform Complete CRUD Operations on Student Database",
        "Create, Read, Update, and Delete Relational Persistence Using Java JDBC and MySQL",
        ["🐬 MySQL Database: it", "📋 Table: Student", "🔄 CRUD: INSERT, SELECT, UPDATE, DELETE", "☕ StudentCRUD.java"],
        "JDBC & Databases"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 6 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview</a>
          <a href="#requirements" class="toc-item">3. Requirements</a>
          <a href="#procedure" class="toc-item">4. Procedure</a>
          <a href="#schema" class="toc-item">5. MySQL Database Schema</a>
          <a href="#program" class="toc-item">6. Java Program</a>
          <a href="#explanation" class="toc-item">7. Program Explanation</a>
          <a href="#output" class="toc-item">8. NetBeans Output</a>
          <a href="#screenshots" class="toc-item">9. Screenshot Gallery (4)</a>
          <a href="#result" class="toc-item">10. Result & Observation</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To write and execute a Java JDBC program (<code>StudentCRUD.java</code>) to perform complete Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE) operations on the <code>Student</code> table in MySQL database <code>it</code>.
          </p>
        </section>

        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Overview</h2>
          <p>
            The acronym CRUD designates the fundamental persistence cycle in relational database software:
          </p>
          <ul style="margin-left:20px;line-height:1.8;">
            <li><strong>Create (INSERT):</strong> Writes new relational rows into the target table using <code>st.executeUpdate()</code>.</li>
            <li><strong>Read (SELECT):</strong> Retrieves data using <code>st.executeQuery()</code>, returning a scrollable <code>ResultSet</code> cursor.</li>
            <li><strong>Update (UPDATE):</strong> Modifies existing attribute values matching predicate filters using <code>st.executeUpdate()</code>.</li>
            <li><strong>Delete (DELETE):</strong> Purges matching tuples from relational storage using <code>st.executeUpdate()</code>.</li>
          </ul>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 3. System Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Processor: Intel Core i3 / i5 or higher</div>
                <div class="req-item"><span class="req-item-dot"></span>RAM: 4 GB minimum</div>
                <div class="req-item"><span class="req-item-dot"></span>Storage: 500 MB free space</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Software Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE 8+</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: MySQL Server 8.0 (Port 3306)</div>
                <div class="req-item"><span class="req-item-dot"></span>Driver: MySQL Connector/J</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗄️</div><div class="timeline-title">Step 1: Create Database & Table in MySQL</div></div>
                <div class="timeline-desc">Create database <code>it</code> and table <code>Student(id, name, course, marks)</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 2: Create NetBeans Project & Java Class</div></div>
                <div class="timeline-desc">Create <code>StudentCRUD.java</code> under package <code>javaapplication26</code> and add MySQL driver to Libraries.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">➕</div><div class="timeline-title">Step 3: Execute INSERT & SELECT</div></div>
                <div class="timeline-desc">Insert student <code>(101, 'Rahul', 'CSE', 90)</code> and query all rows into console.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">✏️</div><div class="timeline-title">Step 4: Execute UPDATE & Verify</div></div>
                <div class="timeline-desc">Update marks to 95 for id 101, then query table again to verify updated record.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗑️</div><div class="timeline-title">Step 5: Execute DELETE & Close</div></div>
                <div class="timeline-desc">Delete student 101, close connection, and verify <code>BUILD SUCCESSFUL</code>.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="schema">
          <h2 class="content-section-title"><span class="section-icon">🗄️</span> 5. MySQL Database Schema (schema_student.sql)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">schema_student.sql</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="dl-java-btn" data-filename="schema_student.sql">⬇ Download .sql</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">USE</span> it;

<span class="kw">CREATE TABLE</span> Student
(
    id <span class="ty">INT PRIMARY KEY</span>,
    name <span class="ty">VARCHAR(30)</span>,
    course <span class="ty">VARCHAR(30)</span>,
    marks <span class="ty">INT</span>
);</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 6. Java Program (StudentCRUD.java)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">StudentCRUD.java</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="StudentCRUD.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <div class="line-numbers" aria-hidden="true">1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53</div>
              <pre><code><span class="kw">package</span> <span class="pk">javaapplication26</span>;

<span class="kw">import</span> <span class="pk">java.sql.*</span>;

<span class="kw">public class</span> <span class="ty">StudentCRUD</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="ty">String</span>[] args) {
        <span class="kw">try</span> {
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.jdbc.Driver"</span>);
            <span class="ty">Connection</span> con = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(
                <span class="str">"jdbc:mysql://localhost/it"</span>,
                <span class="str">"root"</span>,
                <span class="str">""</span>
            );
            <span class="ty">Statement</span> st = con.<span class="fn">createStatement</span>();

            <span class="co">// INSERT</span>
            <span class="kw">int</span> insert = st.<span class="fn">executeUpdate</span>(
                <span class="str">"INSERT INTO Student VALUES(101,'Rahul','CSE',90)"</span>
            );
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"Record Inserted Successfully"</span>);

            <span class="co">// DISPLAY</span>
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nStudent Records"</span>);
            <span class="ty">ResultSet</span> rs = st.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM Student"</span>);
            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(
                    rs.<span class="fn">getInt</span>(1) + <span class="str">"  "</span> +
                    rs.<span class="fn">getString</span>(2) + <span class="str">"  "</span> +
                    rs.<span class="fn">getString</span>(3) + <span class="str">"  "</span> +
                    rs.<span class="fn">getInt</span>(4)
                );
            }

            <span class="co">// UPDATE</span>
            <span class="kw">int</span> update = st.<span class="fn">executeUpdate</span>(
                <span class="str">"UPDATE Student SET marks=95 WHERE id=101"</span>
            );
            <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"\\nRecord Updated Successfully"</span>);

            <span class="co">// DISPLAY AFTER UPDATE</span>
            rs = st.<span class="fn">executeQuery</span>(<span class="str">"SELECT * FROM Student"</span>);
            <span class="kw">while</span> (rs.<span class="fn">next</span>()) {
                <span class="ty">System</span>.out.<span class="fn">println</span>(
                    rs.<span class="fn">getInt</span>(1) + <span class="str">"  "</span> +
                    rs.<span class="fn">getString</span>(2) + <span class="str">"  "</span> +
                    rs.<span class="fn">getString</span>(3) + <span class="str">"  "</span> +
                    rs.<span class="fn">getInt</span>(4)
                );
            }

            <span class="co">// DELETE</span>
            <span class="kw">int</span> delete = st.<span class="fn">executeUpdate</span>(
                <span class="str">"DELETE FROM Student WHERE id=101"</span>
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

        <section class="content-section" id="explanation">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 7. Program Explanation</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Operation</th>
                  <th>SQL Command</th>
                  <th>API Method</th>
                  <th>Description</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Create</strong></td>
                  <td><code>INSERT INTO Student VALUES(101,'Rahul','CSE',90)</code></td>
                  <td><code>st.executeUpdate()</code></td>
                  <td>Creates new student entity tuple with ID 101 and marks 90.</td>
                </tr>
                <tr>
                  <td><strong>Read</strong></td>
                  <td><code>SELECT * FROM Student</code></td>
                  <td><code>st.executeQuery()</code></td>
                  <td>Returns a ResultSet cursor to iterate through all student attributes.</td>
                </tr>
                <tr>
                  <td><strong>Update</strong></td>
                  <td><code>UPDATE Student SET marks=95 WHERE id=101</code></td>
                  <td><code>st.executeUpdate()</code></td>
                  <td>Alters the marks attribute for the row matching primary key id=101.</td>
                </tr>
                <tr>
                  <td><strong>Delete</strong></td>
                  <td><code>DELETE FROM Student WHERE id=101</code></td>
                  <td><code>st.executeUpdate()</code></td>
                  <td>Permanently removes the student tuple matching id=101 from table.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 8. NetBeans IDE Output</h2>
          <div class="netbeans-output">
            <div class="netbeans-header">
              <div class="netbeans-tabs"><div class="netbeans-tab"><span class="netbeans-tab-icon">☕</span> Output - JavaApplication26 (run)</div></div>
              <div class="netbeans-actions"><span class="nb-status-badge">SUCCESS</span></div>
            </div>
            <div class="netbeans-body">
              <span class="nb-line-run">run:</span>
              <span class="nb-line-info">Record Inserted Successfully</span>
              <br />
              <span class="nb-line-out">Student Records</span>
              <span class="nb-line-out">101  Rahul  CSE  90</span>
              <br />
              <span class="nb-line-info">Record Updated Successfully</span>
              <span class="nb-line-out">101  Rahul  CSE  95</span>
              <br />
              <span class="nb-line-info">Record Deleted Successfully</span>
              <span class="nb-line-success" style="color:#4ade80;font-weight:bold;">BUILD SUCCESSFUL (total time: 0 seconds)</span>
            </div>
          </div>
        </section>

        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 9. Original Lab Screenshots (Execution & MySQL CLI)
            </h2>
            <span class="badge badge-purple">4 Authentic Screenshots</span>
          </div>
          <p>Extracted directly from student lab report (JDBC CRUD OPERATIONS 24EU08161.docx):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">NetBeans Output</span><span class="ss-counter-badge">[1 / 4]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans Output: StudentCRUD Execution">
                <img src="../assets/images/week-6/crud_image_1.png" alt="NetBeans Output StudentCRUD Execution" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NetBeans CRUD Execution</div>
                <div class="ss-subcaption">Output window showing Inserted, Displayed (90), Updated (95), and Deleted.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">MySQL CLI</span><span class="ss-counter-badge">[2 / 4]</span></div>
              <div class="ss-img-wrap" data-title="MySQL CLI: CREATE TABLE Student">
                <img src="../assets/images/week-6/crud_image_6.png" alt="MySQL CLI CREATE TABLE Student" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">MySQL Table Initialization</div>
                <div class="ss-subcaption">MySQL terminal commands: USE it, SHOW TABLES, and CREATE TABLE Student.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_6.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">MySQL DML</span><span class="ss-counter-badge">[3 / 4]</span></div>
              <div class="ss-img-wrap" data-title="MySQL CLI: Table Data Manipulation">
                <img src="../assets/images/week-6/crud_image_7.png" alt="MySQL CLI Table Data Manipulation" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">MySQL DML Commands</div>
                <div class="ss-subcaption">MySQL console executing table creation, insertions, and constraints.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_7.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Stored Procedures</span><span class="ss-counter-badge">[4 / 4]</span></div>
              <div class="ss-img-wrap" data-title="MySQL Procedures & Tables">
                <img src="../assets/images/week-6/crud_image_8.png" alt="MySQL Procedures & Tables" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">MySQL Schema Verification</div>
                <div class="ss-subcaption">Creating stored procedures and related relational tables in MySQL.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-6/crud_image_8.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 10. Result & Observation</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, a Java JDBC program was successfully written and executed in NetBeans IDE 8.2 to perform all four CRUD operations (INSERT, SELECT, UPDATE, DELETE) on the Student database table in MySQL, with verification confirmed in NetBeans console output.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(6)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-6.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_6()

# ==============================================================================
# WEEK 7: Generic Servlet and HTTP Servlet
# ==============================================================================
def generate_week_7():
    header = get_page_header(
        7,
        "Implementation of Generic Servlet and HTTP Servlet Using NetBeans",
        "Building Java Web Applications with Apache Tomcat to Render Dynamic Student Details",
        ["☕ NetBeans IDE 8.2", "🐱 Apache Tomcat Server", "🌐 GenericServlet & HttpServlet", "👨‍🎓 Student Details Display"],
        "Servlets & Web"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 7 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview & Theory</a>
          <a href="#requirements" class="toc-item">3. Requirements</a>
          <a href="#procedure" class="toc-item">4. Step-by-Step Procedure</a>
          <a href="#http-servlet" class="toc-item">5. HTTP Servlet Program</a>
          <a href="#generic-servlet" class="toc-item">6. Generic Servlet Program</a>
          <a href="#explanation" class="toc-item">7. Program Explanation</a>
          <a href="#screenshots" class="toc-item">8. Screenshot Gallery (8)</a>
          <a href="#result" class="toc-item">9. Result & Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To create a Java Web Application using NetBeans IDE 8.2, configure and deploy it on Apache Tomcat Server, and implement both <code>GenericServlet</code> and <code>HttpServlet</code> to dynamically display student details (Roll Number: <strong>24EU08161</strong>) through a web browser.
          </p>
        </section>

        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Background</h2>
          <p>
            A <strong>Servlet</strong> is a Java program executing on a web server that intercepts client requests and generates dynamic responses. Two primary servlet classes exist in the servlet specification:
          </p>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">1. GenericServlet (Protocol-Independent)</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <code>javax.servlet.GenericServlet</code> is an abstract class implementing the <code>Servlet</code> and <code>ServletConfig</code> interfaces. It is protocol-independent and requires overriding the single lifecycle method:
                <br /><code>public void service(ServletRequest req, ServletResponse res)</code>.
              </p>
            </div>
            <div class="req-card">
              <div class="req-card-title">2. HttpServlet (HTTP-Specific)</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <code>javax.servlet.http.HttpServlet</code> extends <code>GenericServlet</code> specifically for HTTP protocol semantics. It provides specialized request methods:
                <br /><code>doGet(HttpServletRequest, HttpServletResponse)</code> and <code>doPost(HttpServletRequest, HttpServletResponse)</code>.
              </p>
            </div>
          </div>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 3. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Environment</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2 (with Java EE pack)</div>
                <div class="req-item"><span class="req-item-dot"></span>Server: Apache Tomcat Server 8.x / 9.x</div>
                <div class="req-item"><span class="req-item-dot"></span>Java Platform: JDK 8+</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 Client & OS</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Client: Web Browser (Chrome / Edge / Internet Explorer)</div>
                <div class="req-item"><span class="req-item-dot"></span>OS: Microsoft Windows / Linux</div>
                <div class="req-item"><span class="req-item-dot"></span>Server Port: Default Port 8080</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📁</div><div class="timeline-title">Step 1: Create Web Application in NetBeans</div></div>
                <div class="timeline-desc">Open NetBeans 8.2 → File → New Project → Java Web → Web Application. Enter project name (<code>WebApplication8</code>) and select Apache Tomcat as the target server.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Step 2: Create HTML Page</div></div>
                <div class="timeline-desc">Create <code>index.html</code> under Web Pages containing header <code>ADVANCED JAVA PROGRAMMING LAB 24EU08161</code> and test deployment.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 3: Create HTTP Servlet (NewServlet.java)</div></div>
                <div class="timeline-desc">Right-click Source Packages → New → Servlet → name <code>NewServlet</code>. Extend <code>HttpServlet</code> and write HTML response logic with Roll Number 24EU08161.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Step 4: Create Generic Servlet (NewServlet1.java)</div></div>
                <div class="timeline-desc">Right-click Source Packages → New → Servlet → name <code>NewServlet1</code>. Extend <code>GenericServlet</code>, override <code>service()</code> method, and output student details.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Step 5: Run Application & Browser Verification</div></div>
                <div class="timeline-desc">Run project and verify endpoints: <code>http://localhost:8080/WebApplication8/NewServlet</code> and <code>.../NewServlet1</code>.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="http-servlet">
          <h2 class="content-section-title"><span class="section-icon">🌐</span> 5. HTTP Servlet Program (NewServlet.java)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">NewServlet.java (HttpServlet)</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="NewServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.io.IOException</span>;
<span class="kw">import</span> <span class="pk">java.io.PrintWriter</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletException</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServletRequest</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServletResponse</span>;

<span class="kw">public class</span> <span class="ty">NewServlet</span> <span class="kw">extends</span> <span class="ty">HttpServlet</span> {
    <span class="kw">protected void</span> <span class="fn">processRequest</span>(<span class="ty">HttpServletRequest</span> request,
            <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html;charset=UTF-8"</span>);
        <span class="kw">try</span> (<span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>()) {
            out.<span class="fn">println</span>(<span class="str">"&lt;!DOCTYPE html&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;html&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;head&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;title&gt;Student Details&lt;/title&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;/head&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;body&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;h1&gt;ADVANCED JAVA LAB&lt;/h1&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;STUDENT DETAILS&lt;/h2&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Roll Number:&lt;/b&gt; 24EU08161&lt;/p&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Subject:&lt;/b&gt; Advanced Java&lt;/p&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Lab:&lt;/b&gt; Advanced Java Lab&lt;/p&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;/body&gt;"</span>);
            out.<span class="fn">println</span>(<span class="str">"&lt;/html&gt;"</span>);
        }
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="generic-servlet">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 6. Generic Servlet Program (NewServlet1.java)</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">NewServlet1.java (GenericServlet)</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="NewServlet1.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.io.IOException</span>;
<span class="kw">import</span> <span class="pk">java.io.PrintWriter</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.GenericServlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletException</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletRequest</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletResponse</span>;

<span class="kw">public class</span> <span class="ty">NewServlet1</span> <span class="kw">extends</span> <span class="ty">GenericServlet</span> {
    <span class="kw">@Override</span>
    <span class="kw">public void</span> <span class="fn">service</span>(<span class="ty">ServletRequest</span> request,
            <span class="ty">ServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html;charset=UTF-8"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        out.<span class="fn">println</span>(<span class="str">"&lt;!DOCTYPE html&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;html&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;head&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;title&gt;Generic Servlet&lt;/title&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;/head&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;body&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h1&gt;Generic Servlet&lt;/h1&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;Student Details&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Register Number:&lt;/b&gt; 24EU08161&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Subject:&lt;/b&gt; ADV JAVA LAB&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;/body&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;/html&gt;"</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="explanation">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 7. Program Explanation</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Component</th>
                  <th>GenericServlet (NewServlet1)</th>
                  <th>HttpServlet (NewServlet)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Base Class</strong></td>
                  <td><code>javax.servlet.GenericServlet</code></td>
                  <td><code>javax.servlet.http.HttpServlet</code></td>
                </tr>
                <tr>
                  <td><strong>Lifecycle Method</strong></td>
                  <td>Overrides <code>service(ServletRequest, ServletResponse)</code></td>
                  <td>Overrides <code>doGet()</code> / <code>doPost()</code> via <code>processRequest()</code></td>
                </tr>
                <tr>
                  <td><strong>Protocol</strong></td>
                  <td>Protocol-independent (supports generic socket services)</td>
                  <td>Exclusively tailored for HTTP protocol requests/responses</td>
                </tr>
                <tr>
                  <td><strong>Response Writing</strong></td>
                  <td><code>response.setContentType("text/html;charset=UTF-8")</code></td>
                  <td><code>response.setContentType("text/html;charset=UTF-8")</code></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Original Lab Execution Screenshots (All 8 Screenshots)
            </h2>
            <span class="badge badge-purple">8 Authentic Screenshots</span>
          </div>
          <p>Extracted directly from student lab report (ADVANCED JAVA PROGRAMMING LAB 24EU08161.docx):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 1</span><span class="ss-counter-badge">[1 / 8]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans Web Application Structure">
                <img src="../assets/images/week-7/servlet_image_1.png" alt="NetBeans Web Application Structure" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 1: Web Application Setup</div>
                <div class="ss-subcaption">NetBeans IDE 8.2 showing project tree, WebApplication8, and index.html.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 2</span><span class="ss-counter-badge">[2 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Browser: index.html Execution">
                <img src="../assets/images/week-7/servlet_image_2.png" alt="Browser index.html Execution" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 2: HTML Page Display</div>
                <div class="ss-subcaption">Browser rendering index.html with ADVANCED JAVA PROGRAMMING LAB header.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 3</span><span class="ss-counter-badge">[3 / 8]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: NewServlet.java HTTP Servlet Code">
                <img src="../assets/images/week-7/servlet_image_3.png" alt="NetBeans NewServlet.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 3: HTTP Servlet Code Editor</div>
                <div class="ss-subcaption">NetBeans editor displaying NewServlet extending HttpServlet and BUILD SUCCESSFUL.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 3 Output</span><span class="ss-counter-badge">[4 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Browser: HTTP Servlet Student Details">
                <img src="../assets/images/week-7/servlet_image_4.png" alt="Browser HTTP Servlet Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 3: HTTP Servlet Browser View</div>
                <div class="ss-subcaption">Browser output showing ADVANCED JAVA LAB, STUDENT DETAILS, Roll: 24EU08161.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_4.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 4</span><span class="ss-counter-badge">[5 / 8]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: NewServlet1.java Generic Servlet">
                <img src="../assets/images/week-7/servlet_image_5.png" alt="NetBeans NewServlet1.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 4: Generic Servlet Code</div>
                <div class="ss-subcaption">NetBeans editor displaying NewServlet1 extending GenericServlet overriding service().</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 4 Output</span><span class="ss-counter-badge">[6 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Browser: Generic Servlet Output">
                <img src="../assets/images/week-7/servlet_image_6.png" alt="Browser Generic Servlet Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 4: Generic Servlet Browser View</div>
                <div class="ss-subcaption">Browser rendering Generic Servlet output with student details and Register Number.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_6.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 5</span><span class="ss-counter-badge">[7 / 8]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: NewServlet2.java Code Editor">
                <img src="../assets/images/week-7/servlet_image_7.png" alt="NetBeans NewServlet2.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 5: HttpServlet doGet() Mapping</div>
                <div class="ss-subcaption">NetBeans IDE showing NewServlet2 overriding doGet() and deploying to Tomcat.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_7.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Step 5 Output</span><span class="ss-counter-badge">[8 / 8]</span></div>
              <div class="ss-img-wrap" data-title="Browser: Final HTTP Servlet Output">
                <img src="../assets/images/week-7/servlet_image_8.png" alt="Browser Final HTTP Servlet Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Step 5: Final Browser Verification</div>
                <div class="ss-subcaption">Browser confirming HTTP Servlet Student Details rendering on Apache Tomcat.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/servlet_image_8.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result & Conclusion</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, the web application was successfully created and executed in NetBeans IDE 8.2 on Apache Tomcat. The Generic Servlet and HTTP Servlet were successfully implemented to display student details (Roll Number: <strong>24EU08161</strong>) through a web browser.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(7)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-7.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_7()

# ==============================================================================
# WEEK 8: Advanced Java Web Applications
# ==============================================================================
def generate_week_8():
    header = get_page_header(
        8,
        "Advanced Java Web Applications: Student Management, Cookies & Sessions",
        "Full CRUD Web Tier, Client-Side Cookie State & Server-Side HttpSession Security",
        ["🐱 Apache Tomcat 9.0", "🐬 MySQL studentdb", "🍪 javax.servlet.http.Cookie", "🔒 HttpSession Security", "📦 Full CRUD Web Tier"],
        "Servlets & Web"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 8 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview & Modules</a>
          <a href="#q1-sms" class="toc-item">3. Student Management (CRUD)</a>
          <a href="#q2-cookie" class="toc-item">4. Cookie Demonstration</a>
          <a href="#q3-session" class="toc-item">5. Session Management</a>
          <a href="#q4-integrated" class="toc-item">6. Authenticated SMS Portal</a>
          <a href="#code" class="toc-item">7. Source Code Modules</a>
          <a href="#screenshots" class="toc-item">8. Screenshot Gallery (11)</a>
          <a href="#result" class="toc-item">9. Result & Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To design, develop, and validate an integrated suite of enterprise Java Web Applications using Java Servlets, JDBC, and MySQL: constructing a complete Student Management System executing CRUD operations, demonstrating client-side state management using Cookies, implementing server-side session management using HttpSession, and architecting an integrated authenticated web portal with secure session logout.
          </p>
        </section>

        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Architectural Overview</h2>
          <p>
            Enterprise web systems require a cohesive orchestration of three foundational layers:
          </p>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">1. Relational Persistence Layer</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">MySQL <code>studentdb</code> database storing student tuples (id, name, department, marks) manipulated via JDBC <code>PreparedStatement</code> to prevent SQL injection.</p>
            </div>
            <div class="req-card">
              <div class="req-card-title">2. Client-Side Cookie State</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">Lightweight browser cookies (<code>javax.servlet.http.Cookie</code>) transmitting user identification across HTTP request headers.</p>
            </div>
            <div class="req-card" style="grid-column:1/-1;">
              <div class="req-card-title">3. Server-Side HttpSession Security</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">Container-managed sessions (<code>HttpSession</code>) securing dashboard access, persisting authentication states, and terminating securely via <code>session.invalidate()</code>.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="q1-sms">
          <h2 class="content-section-title"><span class="section-icon">📋</span> 3. Question 1: Student Management System (CRUD)</h2>
          <p>
            <strong>Objective:</strong> Develop a Student Management System using Java Servlets, JDBC, and MySQL performing Add, Display, Search, Update, and Delete operations.
          </p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">studentdb Schema (MySQL)</span>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">CREATE DATABASE</span> studentdb;
<span class="kw">USE</span> studentdb;

<span class="kw">CREATE TABLE</span> student (
    id <span class="ty">INT PRIMARY KEY</span>,
    name <span class="ty">VARCHAR(100) NOT NULL</span>,
    department <span class="ty">VARCHAR(100) NOT NULL</span>,
    marks <span class="ty">DECIMAL(5,2) NOT NULL</span>
);</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="q2-cookie">
          <h2 class="content-section-title"><span class="section-icon">🍪</span> 4. Question 2: Cookie Demonstration</h2>
          <p>
            <strong>Objective:</strong> Accept user's name via an HTML form, store it in a browser cookie via <code>response.addCookie()</code>, and upon subsequent requests, retrieve it via <code>request.getCookies()</code> to display a customized welcome banner.
          </p>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Cookie Operation</th><th>Java Servlet Code</th><th>Description</th></tr></thead>
              <tbody>
                <tr><td>Create &amp; Add</td><td><code>Cookie userCookie = new Cookie("user", name); response.addCookie(userCookie);</code></td><td>Generates HTTP Set-Cookie header.</td></tr>
                <tr><td>Retrieve</td><td><code>Cookie[] cookies = request.getCookies();</code></td><td>Parses client Cookie header.</td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="q3-session">
          <h2 class="content-section-title"><span class="section-icon">🔒</span> 5. Question 3: Session Management (HttpSession)</h2>
          <p>
            <strong>Objective:</strong> Accept user name, establish a server-side session using <code>request.getSession()</code>, bind the name using <code>session.setAttribute("username", name)</code>, and verify its availability on another page.
          </p>
        </section>

        <section class="content-section" id="q4-integrated">
          <h2 class="content-section-title"><span class="section-icon">🛡️</span> 6. Question 4: Integrated Authenticated Portal</h2>
          <p>
            An integrated web portal combining Login validation, session creation, Cookie remembering, protected Dashboard operations, and secure Logout:
          </p>
          <pre class="timeline-code"><code>Login -&gt; Validate Credentials -&gt; Create HttpSession -&gt; Store Cookie -&gt; Dashboard (Add, Display, Search, Update, Delete) -&gt; Logout (Invalidate Session & Clear Cookie)</code></pre>
        </section>

        <section class="content-section" id="code">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 7. Source Code Modules</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">DBConnection.java</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="dl-java-btn" data-filename="DBConnection.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.sms.util</span>;

<span class="kw">import</span> <span class="pk">java.sql.Connection</span>;
<span class="kw">import</span> <span class="pk">java.sql.DriverManager</span>;

<span class="kw">public class</span> <span class="ty">DBConnection</span> {
    <span class="kw">private static</span> <span class="ty">Connection</span> connection = <span class="kw">null</span>;

    <span class="kw">public static</span> <span class="ty">Connection</span> <span class="fn">getConnection</span>() {
        <span class="kw">if</span> (connection != <span class="kw">null</span>) <span class="kw">return</span> connection;
        <span class="kw">try</span> {
            <span class="ty">Class</span>.<span class="fn">forName</span>(<span class="str">"com.mysql.cj.jdbc.Driver"</span>);
            connection = <span class="ty">DriverManager</span>.<span class="fn">getConnection</span>(
                <span class="str">"jdbc:mysql://localhost:3306/studentdb"</span>, <span class="str">"root"</span>, <span class="str">""</span>
            );
        } <span class="kw">catch</span> (<span class="ty">Exception</span> e) {
            e.<span class="fn">printStackTrace</span>();
        }
        <span class="kw">return</span> connection;
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Original Lab Screenshots (All 11 Figures)
            </h2>
            <span class="badge badge-purple">11 Authentic Screenshots</span>
          </div>
          <p>Extracted directly from original laboratory record document (Week_8.pdf):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 1</span><span class="ss-counter-badge">[1 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Display All Students (MySQL Record)">
                <img src="../assets/images/week-8/week-8_img_1.jpg" alt="Figure 1 Display All Students" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 1: Display All Students</div>
                <div class="ss-subcaption">Browser display showing student record retrieved from MySQL (137 karthik atluri IT 90.0).</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 2</span><span class="ss-counter-badge">[2 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Search Student by ID">
                <img src="../assets/images/week-8/week-8_img_2.jpg" alt="Figure 2 Search Student" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 2: Search Student</div>
                <div class="ss-subcaption">Student record retrieved successfully using student ID lookup.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_2.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 3</span><span class="ss-counter-badge">[3 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Update Student Success">
                <img src="../assets/images/week-8/week-8_img_3.jpg" alt="Figure 3 Update Student" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 3: Update Student</div>
                <div class="ss-subcaption">Student details updated successfully in MySQL database.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_3.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 4</span><span class="ss-counter-badge">[4 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Cookie Demonstration">
                <img src="../assets/images/week-8/week-8_img_4.jpg" alt="Figure 4 Cookie Demonstration" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 4: Cookie Demonstration</div>
                <div class="ss-subcaption">Browser verifying stored name retrieved from Cookie: "Hello, Karthikeyan A!".</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 5</span><span class="ss-counter-badge">[5 / 11]</span></div>
              <div class="ss-img-wrap" data-title="HttpSession Demonstration">
                <img src="../assets/images/week-8/week-8_img_5.jpg" alt="Figure 5 HttpSession Demonstration" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 5: HttpSession Demonstration</div>
                <div class="ss-subcaption">Server session created successfully and username stored in session attribute.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 6</span><span class="ss-counter-badge">[6 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Student Management System Dashboard">
                <img src="../assets/images/week-8/week-8_img_6.jpg" alt="Figure 6 Dashboard" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 6: System Dashboard</div>
                <div class="ss-subcaption">Student Management System dashboard providing Add, Display, Search, Update, Delete buttons.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_6.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7</span><span class="ss-counter-badge">[7 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Add Student Success">
                <img src="../assets/images/week-8/week-8_img_7.jpg" alt="Figure 7 Add Student" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 7: Add Student</div>
                <div class="ss-subcaption">Confirmation message: Student added successfully!</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_7.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 8</span><span class="ss-counter-badge">[8 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Display All Students Table">
                <img src="../assets/images/week-8/week-8_img_8.jpg" alt="Figure 8 Display All Students" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 8: Display All Students</div>
                <div class="ss-subcaption">Retrieved records from MySQL showing ID 137, Karthik Atluri, Cyber, 100.0.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_8.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9</span><span class="ss-counter-badge">[9 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Search Result Display">
                <img src="../assets/images/week-8/week-8_img_9.jpg" alt="Figure 9 Search Student" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 9: Search Result</div>
                <div class="ss-subcaption">Search query returning exact match tuple from MySQL database.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_9.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10</span><span class="ss-counter-badge">[10 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Update Student Record">
                <img src="../assets/images/week-8/week-8_img_10.jpg" alt="Figure 10 Update Student" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 10: Update Student</div>
                <div class="ss-subcaption">Student updated successfully confirmation page.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_10.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11</span><span class="ss-counter-badge">[11 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Delete Student Success">
                <img src="../assets/images/week-8/week-8_img_11.jpg" alt="Figure 11 Delete Student" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 11: Delete Student</div>
                <div class="ss-subcaption">Confirmation message verifying student record deleted successfully.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-8/week-8_img_11.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result & Conclusion</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, advanced Java Web Applications encompassing the Student Management System, Cookie tracking, and HttpSession management were successfully developed and deployed on Apache Tomcat, fulfilling all requirements with verified execution evidence.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(8)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-8.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_8()
print("Weeks 4 to 8 successfully generated!")

