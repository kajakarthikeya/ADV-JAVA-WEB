import os
import sys

sys.path.append(r'c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main')
from generate_base import get_page_header, get_page_footer, pages_dir

header = get_page_header(
    7,
    "Implementation of Generic Servlet and HTTP Servlet",
    "NetBeans Web Applications, Protocol Semantics, Lifecycle Hooks, GET/POST Handling & Dynamic Student Records",
    ["☕ NetBeans IDE 8.2", "🐱 Apache Tomcat Server", "🌐 GenericServlet & HttpServlet", "👨‍🎓 Student Details Display (24EU08161)", "📋 GET & POST Forms"],
    "Servlets & Web"
)

content = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 7 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#activity-1" class="toc-item">4. Activity 1: Web App & index.html</a>
          <a href="#activity-2" class="toc-item">5. Activity 2: HTTP Servlet (24EU08161)</a>
          <a href="#activity-3" class="toc-item">6. Activity 3: GET & POST Servlet</a>
          <a href="#activity-4" class="toc-item">7. Activity 4: Generic Servlet</a>
          <a href="#activity-5" class="toc-item">8. Activity 5: Servlet Life Cycle</a>
          <a href="#activity-6" class="toc-item">9. Activity 6: Student Form Registration</a>
          <a href="#result-analysis" class="toc-item">10. Result Analysis & Discussion</a>
          <a href="#screenshots" class="toc-item">11. Screenshot Gallery (16 Figures)</a>
          <a href="#result" class="toc-item">12. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To design, configure, and execute modular Java Web Applications in NetBeans IDE 8.2 deployed on Apache Tomcat Server, implementing:
          </p>
          <ul style="margin-left:24px;line-height:1.8;color:var(--text-sub);">
            <li><strong>HTTP Servlet (NewServlet):</strong> Rendering styled student identity details (Roll Number: <strong>24EU08161</strong>).</li>
            <li><strong>HTTP GET &amp; POST Servlet (GetPostServlet):</strong> Intercepting HTTP form dispatches with distinct <code>doGet()</code> and <code>doPost()</code> request handlers.</li>
            <li><strong>Generic Servlet (MyGenericServlet):</strong> Extending protocol-independent <code>javax.servlet.GenericServlet</code> and implementing the <code>service()</code> lifecycle hook.</li>
            <li><strong>Servlet Life Cycle (LifeCycleServlet):</strong> Implementing <code>javax.servlet.Servlet</code> to log and demonstrate the three fundamental phases: <code>init()</code>, <code>service()</code>, and <code>destroy()</code>.</li>
            <li><strong>Student Registration Portal (StudentFormServlet):</strong> Form-based data ingestion rendering candidate submission output (Name: <strong>karthik</strong>, Roll No: <strong>161</strong>, Dept: <strong>it</strong>).</li>
          </ul>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Environment</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2 (Java EE Pack)</div>
                <div class="req-item"><span class="req-item-dot"></span>Web Container: Apache Tomcat Server 8.x / 9.x</div>
                <div class="req-item"><span class="req-item-dot"></span>Java Platform: JDK 8+ with Servlet API</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 Client &amp; Networking</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Client: Web Browser (Chrome / Edge / Internet Explorer)</div>
                <div class="req-item"><span class="req-item-dot"></span>Target Port: HTTP Port 8080</div>
                <div class="req-item"><span class="req-item-dot"></span>Deployment Contexts: /WebApplication8 and /GenericServletDemo</div>
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
                <div class="timeline-header"><div class="timeline-icon">📁</div><div class="timeline-title">Step 1: Web Application Initialization</div></div>
                <div class="timeline-desc">Launch NetBeans 8.2 → File → New Project → Java Web → Web Application. Name project <code>WebApplication8</code> and select Apache Tomcat as the runtime container.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Step 2: HTML Page Authoring</div></div>
                <div class="timeline-desc">Under <code>Web Pages</code>, configure <code>index.html</code> with document headers and test browser connectivity at <code>http://localhost:8080/WebApplication8/</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 3: Implement NewServlet (HttpServlet with 24EU08161)</div></div>
                <div class="timeline-desc">Create <code>NewServlet.java</code> extending <code>HttpServlet</code>. In <code>processRequest()</code>, output candidate details (Roll Number: <strong>24EU08161</strong>).</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔄</div><div class="timeline-title">Step 4: Implement GET &amp; POST Handling (GetPostServlet)</div></div>
                <div class="timeline-desc">Author <code>GetPostServlet.java</code> overriding both <code>doGet()</code> and <code>doPost()</code>, reading query parameters via <code>request.getParameter("name")</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Step 5: GenericServlet &amp; Servlet Lifecycle Implementation</div></div>
                <div class="timeline-desc">Create <code>GenericServletDemo</code> project. Implement <code>MyGenericServlet</code> (overriding <code>service()</code>) and <code>LifeCycleServlet</code> (implementing <code>init()</code>, <code>service()</code>, <code>destroy()</code>).</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">6</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📋</div><div class="timeline-title">Step 6: Interactive Student Registration Form</div></div>
                <div class="timeline-desc">Create <code>form.html</code> with fields for Name, Roll No, and Department. Route POST submission to <code>StudentFormServlet</code> to render submitted data dynamically.</div>
              </div>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 1 -->
        <section class="content-section" id="activity-1">
          <h2 class="content-section-title"><span class="section-icon">📁</span> 4. Activity 1: NetBeans Web Application Creation &amp; index.html</h2>
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans IDE Project Proof</span>
                <span class="proof-title">NetBeans 8.2 Workspace — WebApplication8 Hierarchy</span>
              </div>
              <div class="ss-img-wrap" data-title="NetBeans WebApplication8 Project Hierarchy">
                <img src="../assets/images/week-7/w7_web_app_setup.png" alt="NetBeans WebApplication8 Project Setup" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans IDE 8.2 workspace screenshot verifying project tree, Web Pages, WEB-INF, and index.html.</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">🌐</span> index.html</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-code-btn" data-filename="index.html">⬇ Download HTML</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;TODO supply a title&lt;/title&gt;
        &lt;meta charset="UTF-8"&gt;
        &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;div&gt;ADVANCED JAVA PROGRAMMING LAB 24EU08161&lt;/div&gt;
    &lt;/body&gt;
&lt;/html&gt;</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 2 -->
        <section class="content-section" id="activity-2">
          <h2 class="content-section-title"><span class="section-icon">☕</span> 5. Activity 2: HTTP Servlet Rendering Student Details (24EU08161)</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans Source Code Proof</span>
                <span class="proof-title">NetBeans IDE — NewServlet.java Code Displaying Roll: 24EU08161</span>
              </div>
              <div class="ss-img-wrap" data-title="NewServlet.java Code Proof">
                <img src="../assets/images/week-7/w7_newservlet_code_24EU08161.png" alt="NewServlet.java Code Displaying Roll 24EU08161" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans code editor proof verifying processRequest() writing Roll Number: 24EU08161.</p>
            </div>

            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Execution Output Proof</span>
                <span class="proof-title">Web Browser — NewServlet Student Details Output (24EU08161)</span>
              </div>
              <div class="ss-img-wrap" data-title="NewServlet Browser Output Proof">
                <img src="../assets/images/week-7/w7_newservlet_browser_24EU08161.png" alt="NewServlet Browser Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser execution proof showing ADVANCED JAVA LAB, STUDENT DETAILS, Roll Number: 24EU08161.</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> NewServlet.java</div>
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
    <span class="kw">protected void</span> <span class="fn">processRequest</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
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

        <!-- ACTIVITY 3 -->
        <section class="content-section" id="activity-3">
          <h2 class="content-section-title"><span class="section-icon">🔄</span> 6. Activity 3: GET &amp; POST Request Handling (GetPostServlet.java)</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans Source Code Proof</span>
                <span class="proof-title">GetPostServlet.java Code &amp; index.html Form</span>
              </div>
              <div class="ss-img-wrap" data-title="GetPostServlet.java Source Code Proof">
                <img src="../assets/images/week-7/w7_get_post_servlet_code.png" alt="GetPostServlet.java Source Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans code editor proof verifying doGet() and doPost() method implementations.</p>
            </div>

            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Execution Output Proof</span>
                <span class="proof-title">Browser GET &amp; POST Responses ("Hello karthik!")</span>
              </div>
              <div class="ss-img-wrap" data-title="Browser GET Request Output">
                <img src="../assets/images/week-7/w7_get_request_output.png" alt="Browser GET Request Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser output confirming GET request processing: "Hello karthik! This is a GET request."</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> GetPostServlet.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="GetPostServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="an">@WebServlet</span>(<span class="str">"/GetPostServlet"</span>)
<span class="kw">public class</span> <span class="ty">GetPostServlet</span> <span class="kw">extends</span> <span class="ty">HttpServlet</span> {
    <span class="kw">protected void</span> <span class="fn">doGet</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        <span class="ty">String</span> name = request.<span class="fn">getParameter</span>(<span class="str">"name"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;GET Request&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;Hello "</span> + name + <span class="str">"!&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;This is a GET request.&lt;/p&gt;"</span>);
    }

    <span class="kw">protected void</span> <span class="fn">doPost</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        <span class="ty">String</span> name = request.<span class="fn">getParameter</span>(<span class="str">"name"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;POST Request&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;Hello "</span> + name + <span class="str">"!&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;This is a POST request.&lt;/p&gt;"</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 4 -->
        <section class="content-section" id="activity-4">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 7. Activity 4: Generic Servlet Implementation (MyGenericServlet.java)</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans Source Code Proof</span>
                <span class="proof-title">MyGenericServlet.java Code Editor — service() Override</span>
              </div>
              <div class="ss-img-wrap" data-title="MyGenericServlet Code Proof">
                <img src="../assets/images/week-7/w7_generic_servlet_code.png" alt="MyGenericServlet Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans code editor proof verifying class extending GenericServlet.</p>
            </div>

            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Execution Output Proof</span>
                <span class="proof-title">Browser Output — Generic Servlet Dynamic Output</span>
              </div>
              <div class="ss-img-wrap" data-title="Generic Servlet Output Proof">
                <img src="../assets/images/week-7/w7_generic_servlet_output.png" alt="Generic Servlet Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser execution proof showing: "This servlet extends GenericServlet. Hello from GenericServlet!"</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">⚙️</span> MyGenericServlet.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="MyGenericServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="an">@WebServlet</span>(<span class="str">"/MyGenericServlet"</span>)
<span class="kw">public class</span> <span class="ty">MyGenericServlet</span> <span class="kw">extends</span> <span class="ty">GenericServlet</span> {
    <span class="kw">public void</span> <span class="fn">service</span>(<span class="ty">ServletRequest</span> request, <span class="ty">ServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;Generic Servlet&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;This servlet extends GenericServlet.&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;Hello from GenericServlet!&lt;/p&gt;"</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 5 -->
        <section class="content-section" id="activity-5">
          <h2 class="content-section-title"><span class="section-icon">⏳</span> 8. Activity 5: Servlet Life Cycle Implementation (LifeCycleServlet.java)</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">NetBeans Source Code Proof</span>
                <span class="proof-title">LifeCycleServlet.java Code — init(), service() &amp; destroy()</span>
              </div>
              <div class="ss-img-wrap" data-title="LifeCycleServlet Code Proof">
                <img src="../assets/images/week-7/w7_lifecycle_servlet_code.png" alt="LifeCycleServlet Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic NetBeans code editor proof verifying class implementing Servlet interface lifecycle methods.</p>
            </div>

            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Execution Output Proof</span>
                <span class="proof-title">Browser Output — Servlet Life Cycle Phase Display</span>
              </div>
              <div class="ss-img-wrap" data-title="LifeCycleServlet Output Proof">
                <img src="../assets/images/week-7/w7_lifecycle_servlet_output.png" alt="LifeCycleServlet Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser execution proof showing init(): Servlet Initialized, service(): Request Processed.</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">⏳</span> LifeCycleServlet.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="LifeCycleServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="an">@WebServlet</span>(<span class="str">"/LifeCycleServlet"</span>)
<span class="kw">public class</span> <span class="ty">LifeCycleServlet</span> <span class="kw">implements</span> <span class="ty">Servlet</span> {
    <span class="kw">public void</span> <span class="fn">init</span>(<span class="ty">ServletConfig</span> config) { <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"init() method called"</span>); }
    <span class="kw">public</span> <span class="ty">ServletConfig</span> <span class="fn">getServletConfig</span>() { <span class="kw">return null</span>; }
    <span class="kw">public void</span> <span class="fn">service</span>(<span class="ty">ServletRequest</span> req, <span class="ty">ServletResponse</span> res) <span class="kw">throws</span> <span class="ty">IOException</span> {
        res.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = res.<span class="fn">getWriter</span>();
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;Servlet Life Cycle&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;init():&lt;/b&gt; Servlet Initialized&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;service():&lt;/b&gt; Request Processed&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;destroy():&lt;/b&gt; Servlet Destroyed&lt;/p&gt;"</span>);
    }
    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">getServletInfo</span>() { <span class="kw">return</span> <span class="str">"Life Cycle Servlet"</span>; }
    <span class="kw">public void</span> <span class="fn">destroy</span>() { <span class="ty">System</span>.out.<span class="fn">println</span>(<span class="str">"destroy() method called"</span>); }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 6 -->
        <section class="content-section" id="activity-6">
          <h2 class="content-section-title"><span class="section-icon">📋</span> 9. Activity 6: Interactive Student Registration Form Processing</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Form Input Proof</span>
                <span class="proof-title">Student Registration Form — Inputs (karthik, 161, it)</span>
              </div>
              <div class="ss-img-wrap" data-title="Student Form Input Proof">
                <img src="../assets/images/week-7/w7_student_form_browser_input.png" alt="Student Form Input Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser form proof filled with Name: karthik, Roll No: 161, Department: it.</p>
            </div>

            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Submitted Output Proof</span>
                <span class="proof-title">StudentFormServlet Response Output</span>
              </div>
              <div class="ss-img-wrap" data-title="Student Form Output Proof">
                <img src="../assets/images/week-7/w7_student_form_browser_output.png" alt="Student Form Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser response confirming dynamic processing of submitted candidate records.</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">📋</span> StudentFormServlet.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="StudentFormServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="an">@WebServlet</span>(<span class="str">"/StudentFormServlet"</span>)
<span class="kw">public class</span> <span class="ty">StudentFormServlet</span> <span class="kw">extends</span> <span class="ty">HttpServlet</span> {
    <span class="kw">protected void</span> <span class="fn">doPost</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        <span class="ty">String</span> name = request.<span class="fn">getParameter</span>(<span class="str">"name"</span>);
        <span class="ty">String</span> rollno = request.<span class="fn">getParameter</span>(<span class="str">"rollno"</span>);
        <span class="ty">String</span> dept = request.<span class="fn">getParameter</span>(<span class="str">"dept"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;Student Details&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Name:&lt;/b&gt; "</span> + name + <span class="str">"&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Roll No:&lt;/b&gt; "</span> + rollno + <span class="str">"&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Department:&lt;/b&gt; "</span> + dept + <span class="str">"&lt;/p&gt;"</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- RESULT ANALYSIS -->
        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 10. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Servlet Dispatch Pipeline &amp; Thread Safety</div>
              <p>Tomcat instantiates only a single servlet instance per registered class in memory, spawning lightweight worker threads per incoming HTTP socket. Because instance variables are shared across concurrent requests, servlets must remain strictly stateless to guarantee thread safety.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ GenericServlet vs HttpServlet Routing Overhead</div>
              <p><code>HttpServlet.service()</code> inspects <code>request.getMethod()</code> to dynamically route traffic to <code>doGet()</code>, <code>doPost()</code>, <code>doPut()</code>, or <code>doDelete()</code>. GenericServlet avoids HTTP header parsing, delivering minimal overhead for raw socket stream protocols.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ HTTP GET vs POST Payload Security</div>
              <p>GET requests append form data into plaintext URL query strings subject to server access log leakage and browser history exposure. POST packages form bodies into HTTP message payloads, enabling transmission of large payloads without URI length limits.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 Lifecycle Hooks &amp; Resource Teardown</div>
              <p><code>init()</code> executes exactly once during servlet class loading (or eagerly via <code>&lt;load-on-startup&gt;</code>) to initialize database connection pools. <code>destroy()</code> triggers during server shutdown to gracefully flush caches and close open file descriptors.</p>
            </div>
          </div>
        </section>

        <!-- 16 AUTHENTIC SCREENSHOTS GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 11. Authentic Laboratory Execution Screenshot Gallery (16 Figures)
            </h2>
            <span class="badge badge-purple">16 Authentic Student Screenshots</span>
          </div>
          <p>
            All 16 high-resolution screenshots captured directly from NetBeans IDE 8.2 and browser execution environments:
          </p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.1</span><span class="ss-counter-badge">[1 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.1: NetBeans WebApplication8 Setup"><img src="../assets/images/week-7/w7_web_app_setup.png" alt="Figure 7.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">WebApplication8 Project Structure</div><div class="ss-subcaption">NetBeans IDE 8.2 showing project tree, Web Pages, WEB-INF, and index.html.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_web_app_setup.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.2</span><span class="ss-counter-badge">[2 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.2: NewServlet Code (24EU08161)"><img src="../assets/images/week-7/w7_newservlet_code_24EU08161.png" alt="Figure 7.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NewServlet.java Code (24EU08161)</div><div class="ss-subcaption">NetBeans editor displaying processRequest() writing Roll Number: 24EU08161.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet_code_24EU08161.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.3</span><span class="ss-counter-badge">[3 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.3: NewServlet Browser View (24EU08161)"><img src="../assets/images/week-7/w7_newservlet_browser_24EU08161.png" alt="Figure 7.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NewServlet Browser View (24EU08161)</div><div class="ss-subcaption">Browser rendering ADVANCED JAVA LAB, STUDENT DETAILS with Roll Number: 24EU08161.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet_browser_24EU08161.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.4</span><span class="ss-counter-badge">[4 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.4: NewServlet IDE Workspace"><img src="../assets/images/week-7/w7_newservlet_netbeans_ide.jpg" alt="Figure 7.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NewServlet IDE Workspace</div><div class="ss-subcaption">NetBeans IDE showing project navigator, compile status, and BUILD SUCCESSFUL.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet_netbeans_ide.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.5</span><span class="ss-counter-badge">[5 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.5: NewServlet2 Code"><img src="../assets/images/week-7/w7_newservlet2_code.jpg" alt="Figure 7.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NewServlet2.java Code Editor</div><div class="ss-subcaption">HttpServlet authoring Register Number: 24U08161 and ADV JAVA LAB header.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet2_code.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.6</span><span class="ss-counter-badge">[6 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.6: NewServlet2 Output"><img src="../assets/images/week-7/w7_newservlet2_browser.png" alt="Figure 7.6" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">NewServlet2 Browser Output</div><div class="ss-subcaption">Browser rendering HTTP Servlet, Student Details, and Register Number: 24U08161.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet2_browser.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.7</span><span class="ss-counter-badge">[7 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.7: GetPostServlet Code"><img src="../assets/images/week-7/w7_get_post_servlet_code.png" alt="Figure 7.7" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">GetPostServlet.java Source Code</div><div class="ss-subcaption">NetBeans editor displaying @WebServlet("/GetPostServlet") with doGet() and doPost().</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_get_post_servlet_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.8</span><span class="ss-counter-badge">[8 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.8: HTML Form Markup for GET/POST"><img src="../assets/images/week-7/w7_get_post_html_form_code.png" alt="Figure 7.8" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">HTML Form Markup for GET/POST</div><div class="ss-subcaption">HTML form markup containing both GET and POST submission buttons to GetPostServlet.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_get_post_html_form_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.9</span><span class="ss-counter-badge">[9 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.9: Browser GET Request Execution"><img src="../assets/images/week-7/w7_get_request_output.png" alt="Figure 7.9" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Browser GET Request Execution</div><div class="ss-subcaption">Browser response showing "Hello karthik! This is a GET request."</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_get_request_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.10</span><span class="ss-counter-badge">[10 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.10: Browser POST Request Execution"><img src="../assets/images/week-7/w7_post_request_output.png" alt="Figure 7.10" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Browser POST Request Execution</div><div class="ss-subcaption">Browser response showing "Hello karthik! This is a POST request."</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_post_request_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.11</span><span class="ss-counter-badge">[11 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.11: MyGenericServlet Code"><img src="../assets/images/week-7/w7_generic_servlet_code.png" alt="Figure 7.11" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">MyGenericServlet.java Source Code</div><div class="ss-subcaption">GenericServletDemo project showing class extending GenericServlet with service() method.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_generic_servlet_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.12</span><span class="ss-counter-badge">[12 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.12: Generic Servlet Output"><img src="../assets/images/week-7/w7_generic_servlet_output.png" alt="Figure 7.12" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Generic Servlet Browser View</div><div class="ss-subcaption">Browser rendering "This servlet extends GenericServlet. Hello from GenericServlet!"</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_generic_servlet_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.13</span><span class="ss-counter-badge">[13 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.13: LifeCycleServlet Code"><img src="../assets/images/week-7/w7_lifecycle_servlet_code.png" alt="Figure 7.13" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">LifeCycleServlet.java Source Code</div><div class="ss-subcaption">Class implementing Servlet interface with init(), service(), and destroy() hooks.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_lifecycle_servlet_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.14</span><span class="ss-counter-badge">[14 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.14: Servlet Life Cycle Output"><img src="../assets/images/week-7/w7_lifecycle_servlet_output.png" alt="Figure 7.14" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Servlet Life Cycle Browser View</div><div class="ss-subcaption">Browser output demonstrating init(): Servlet Initialized, service(): Request Processed.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_lifecycle_servlet_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.15</span><span class="ss-counter-badge">[15 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.15: Student Registration Form Input"><img src="../assets/images/week-7/w7_student_form_browser_input.png" alt="Figure 7.15" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Student Registration Form Input</div><div class="ss-subcaption">Browser rendering form.html with entered details: Name: karthik, Roll No: 161, Dept: it.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_student_form_browser_input.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.16</span><span class="ss-counter-badge">[16 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Figure 7.16: Student Form Output"><img src="../assets/images/week-7/w7_student_form_browser_output.png" alt="Figure 7.16" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Submitted Student Record View</div><div class="ss-subcaption">StudentFormServlet browser response dynamically displaying Name: karthik, Roll No: 161, Dept: it.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_student_form_browser_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 12. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Deployed modular Java Web Applications on Apache Tomcat Server in NetBeans IDE 8.2.</div>
            <div class="outcome-item"><span class="check">✔</span> Verified <code>HttpServlet</code> (NewServlet) rendering candidate Roll Number <strong>24EU08161</strong>.</div>
            <div class="outcome-item"><span class="check">✔</span> Validated dual GET &amp; POST request dispatching with query parameter extraction.</div>
            <div class="outcome-item"><span class="check">✔</span> Overrode <code>service()</code> in protocol-independent <code>GenericServlet</code>.</div>
            <div class="outcome-item"><span class="check">✔</span> Profiled the 3-phase Servlet Lifecycle (<code>init()</code>, <code>service()</code>, <code>destroy()</code>).</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 16 authentic figures including candidate form submission (<strong>karthik</strong>, <strong>161</strong>).</div>
          </div>
        </section>
"""

w7_full = header + content + get_page_footer(7)
with open(os.path.join(pages_dir, "week-7.html"), "w", encoding="utf-8") as f:
    f.write(w7_full)
print("Updated pages/week-7.html with proof cards, ide-tab (no Mac dots), and Result Analysis!")

