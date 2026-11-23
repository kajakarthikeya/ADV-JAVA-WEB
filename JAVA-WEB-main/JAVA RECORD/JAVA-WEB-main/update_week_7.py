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
          <a href="#intro" class="toc-item">2. Theoretical Background</a>
          <a href="#requirements" class="toc-item">3. Software Requirements</a>
          <a href="#procedure" class="toc-item">4. Step-by-Step Procedure</a>
          <a href="#activity-1" class="toc-item">5. Activity 1: Web App & index.html</a>
          <a href="#activity-2" class="toc-item">6. Activity 2: HTTP Servlet (24EU08161)</a>
          <a href="#activity-3" class="toc-item">7. Activity 3: GET & POST Servlet</a>
          <a href="#activity-4" class="toc-item">8. Activity 4: Generic Servlet</a>
          <a href="#activity-5" class="toc-item">9. Activity 5: Servlet Life Cycle</a>
          <a href="#activity-6" class="toc-item">10. Activity 6: Student Form Registration</a>
          <a href="#explanation" class="toc-item">11. Architecture Matrix</a>
          <a href="#screenshots" class="toc-item">12. Screenshot Gallery (16 Figures)</a>
          <a href="#result" class="toc-item">13. Result & Conclusion</a>
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

        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Background</h2>
          <p>
            A <strong>Java Servlet</strong> is a server-side component executing inside a Java Web Container (such as Apache Tomcat) that intercepts HTTP requests, executes business logic, and dynamically synthesizes response documents (HTML/JSON).
          </p>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">1. GenericServlet (Protocol-Independent)</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <code>javax.servlet.GenericServlet</code> is an abstract class implementing <code>Servlet</code> and <code>ServletConfig</code>. It decouples servlet code from HTTP specifics and requires overriding only:
                <br /><code>public void service(ServletRequest req, ServletResponse res)</code>.
              </p>
            </div>
            <div class="req-card">
              <div class="req-card-title">2. HttpServlet (HTTP-Specific)</div>
              <p style="font-size:0.85rem;color:var(--text-muted);line-height:1.6;">
                <code>javax.servlet.http.HttpServlet</code> extends <code>GenericServlet</code> specifically for HTTP protocol semantics. It provides specialized request routing for:
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
                <div class="req-item"><span class="req-item-dot"></span>IDE: NetBeans IDE 8.2 (Java EE Pack)</div>
                <div class="req-item"><span class="req-item-dot"></span>Web Container: Apache Tomcat Server 8.x / 9.x</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE Development Kit 8+</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 Client &amp; Networking</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Client: Web Browser (Chrome / Edge / Internet Explorer)</div>
                <div class="req-item"><span class="req-item-dot"></span>Target Port: HTTP Port 8080</div>
                <div class="req-item"><span class="req-item-dot"></span>Deployment Context: /WebApplication8 and /GenericServletDemo</div>
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
          <h2 class="content-section-title"><span class="section-icon">📁</span> 5. Activity 1: NetBeans Web Application Creation &amp; index.html</h2>
          <p>
            Setting up <code>WebApplication8</code> in NetBeans IDE 8.2 and authoring the initial <code>index.html</code> landing page.
          </p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">index.html (WebApplication8 Landing Page)</span>
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
          <h2 class="content-section-title"><span class="section-icon">☕</span> 6. Activity 2: HTTP Servlet Rendering Student Details (NewServlet.java)</h2>
          <p>
            An <code>HttpServlet</code> implementation using <code>processRequest()</code> to emit HTML document markup with candidate roll number <strong>24EU08161</strong>.
          </p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">NewServlet.java (Student Details HTTP Servlet)</span>
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
<span class="kw">import</span> <span class="pk">javax.servlet.annotation.WebServlet</span>;
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

    <span class="kw">@Override</span>
    <span class="kw">protected void</span> <span class="fn">doGet</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        processRequest(request, response);
    }

    <span class="kw">@Override</span>
    <span class="kw">protected void</span> <span class="fn">doPost</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        processRequest(request, response);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 3 -->
        <section class="content-section" id="activity-3">
          <h2 class="content-section-title"><span class="section-icon">🔄</span> 7. Activity 3: GET &amp; POST Request Dispatching (GetPostServlet.java)</h2>
          <p>
            Demonstrating dual HTTP method handling using a form in <code>index.html</code> dispatching GET and POST queries to <code>GetPostServlet</code>.
          </p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">GetPostServlet.java (HTTP GET &amp; POST Handler)</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="GetPostServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.io.IOException</span>;
<span class="kw">import</span> <span class="pk">java.io.PrintWriter</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletException</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.annotation.WebServlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServletRequest</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServletResponse</span>;

<span class="an">@WebServlet</span>(<span class="str">"/GetPostServlet"</span>)
<span class="kw">public class</span> <span class="ty">GetPostServlet</span> <span class="kw">extends</span> <span class="ty">HttpServlet</span> {

    <span class="kw">@Override</span>
    <span class="kw">protected void</span> <span class="fn">doGet</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        <span class="ty">String</span> name = request.<span class="fn">getParameter</span>(<span class="str">"name"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;GET Request&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;Hello "</span> + name + <span class="str">"!&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;This is a GET request.&lt;/p&gt;"</span>);
    }

    <span class="kw">@Override</span>
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
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 8. Activity 4: Generic Servlet Implementation (MyGenericServlet.java)</h2>
          <p>
            Implementing <code>MyGenericServlet</code> by extending <code>javax.servlet.GenericServlet</code> and overriding the protocol-agnostic <code>service()</code> method.
          </p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">MyGenericServlet.java (GenericServlet Protocol-Independent)</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="MyGenericServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.io.IOException</span>;
<span class="kw">import</span> <span class="pk">java.io.PrintWriter</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.GenericServlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletException</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletRequest</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletResponse</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.annotation.WebServlet</span>;

<span class="an">@WebServlet</span>(<span class="str">"/MyGenericServlet"</span>)
<span class="kw">public class</span> <span class="ty">MyGenericServlet</span> <span class="kw">extends</span> <span class="ty">GenericServlet</span> {

    <span class="kw">@Override</span>
    <span class="kw">public void</span> <span class="fn">service</span>(<span class="ty">ServletRequest</span> request, <span class="ty">ServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        out.<span class="fn">println</span>(<span class="str">"&lt;html&gt;&lt;body&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;Generic Servlet&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;This servlet extends GenericServlet.&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;Hello from GenericServlet!&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;/body&gt;&lt;/html&gt;"</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 5 -->
        <section class="content-section" id="activity-5">
          <h2 class="content-section-title"><span class="section-icon">⏳</span> 9. Activity 5: Servlet Life Cycle Implementation (LifeCycleServlet.java)</h2>
          <p>
            Directly implementing the <code>javax.servlet.Servlet</code> interface to trace the fundamental lifecycle phases: <code>init()</code>, <code>service()</code>, and <code>destroy()</code>.
          </p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">LifeCycleServlet.java (Servlet Lifecycle Tracer)</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="LifeCycleServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.io.IOException</span>;
<span class="kw">import</span> <span class="pk">java.io.PrintWriter</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.Servlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletConfig</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletException</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletRequest</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletResponse</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.annotation.WebServlet</span>;

<span class="an">@WebServlet</span>(<span class="str">"/LifeCycleServlet"</span>)
<span class="kw">public class</span> <span class="ty">LifeCycleServlet</span> <span class="kw">implements</span> <span class="ty">Servlet</span> {

    <span class="kw">public void</span> <span class="fn">init</span>(<span class="ty">ServletConfig</span> config) <span class="kw">throws</span> <span class="ty">ServletException</span> {
        System.out.<span class="fn">println</span>(<span class="str">"init() method called"</span>);
    }

    <span class="kw">public</span> <span class="ty">ServletConfig</span> <span class="fn">getServletConfig</span>() { <span class="kw">return null</span>; }

    <span class="kw">public void</span> <span class="fn">service</span>(<span class="ty">ServletRequest</span> request, <span class="ty">ServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;Servlet Life Cycle&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;init():&lt;/b&gt; Servlet Initialized&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;service():&lt;/b&gt; Request Processed&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;destroy():&lt;/b&gt; Servlet Destroyed&lt;/p&gt;"</span>);
    }

    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">getServletInfo</span>() { <span class="kw">return</span> <span class="str">"Life Cycle Servlet"</span>; }

    <span class="kw">public void</span> <span class="fn">destroy</span>() {
        System.out.<span class="fn">println</span>(<span class="str">"destroy() method called"</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 6 -->
        <section class="content-section" id="activity-6">
          <h2 class="content-section-title"><span class="section-icon">📋</span> 10. Activity 6: Student Form Registration &amp; POST Handler</h2>
          <p>
            An end-to-end form ingestion workflow: <code>form.html</code> provides an HTML entry form routed to <code>StudentFormServlet</code>, which dynamically formats and outputs the student record.
          </p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">StudentFormServlet.java (Form Ingestion Processor)</span>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="StudentFormServlet.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">import</span> <span class="pk">java.io.IOException</span>;
<span class="kw">import</span> <span class="pk">java.io.PrintWriter</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.ServletException</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.annotation.WebServlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServlet</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServletRequest</span>;
<span class="kw">import</span> <span class="pk">javax.servlet.http.HttpServletResponse</span>;

<span class="an">@WebServlet</span>(<span class="str">"/StudentFormServlet"</span>)
<span class="kw">public class</span> <span class="ty">StudentFormServlet</span> <span class="kw">extends</span> <span class="ty">HttpServlet</span> {

    <span class="kw">protected void</span> <span class="fn">doPost</span>(<span class="ty">HttpServletRequest</span> request, <span class="ty">HttpServletResponse</span> response)
            <span class="kw">throws</span> <span class="ty">ServletException</span>, <span class="ty">IOException</span> {
        response.<span class="fn">setContentType</span>(<span class="str">"text/html"</span>);
        <span class="ty">PrintWriter</span> out = response.<span class="fn">getWriter</span>();

        <span class="ty">String</span> name = request.<span class="fn">getParameter</span>(<span class="str">"name"</span>);
        <span class="ty">String</span> rollno = request.<span class="fn">getParameter</span>(<span class="str">"rollno"</span>);
        <span class="ty">String</span> dept = request.<span class="fn">getParameter</span>(<span class="str">"dept"</span>);

        out.<span class="fn">println</span>(<span class="str">"&lt;html&gt;&lt;body&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;h2&gt;Student Details&lt;/h2&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Name:&lt;/b&gt; "</span> + name + <span class="str">"&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Roll No:&lt;/b&gt; "</span> + rollno + <span class="str">"&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;p&gt;&lt;b&gt;Department:&lt;/b&gt; "</span> + dept + <span class="str">"&lt;/p&gt;"</span>);
        out.<span class="fn">println</span>(<span class="str">"&lt;/body&gt;&lt;/html&gt;"</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- EXPLANATION -->
        <section class="content-section" id="explanation">
          <h2 class="content-section-title"><span class="section-icon">📝</span> 11. Architectural Comparison Matrix</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Architectural Dimension</th>
                  <th>GenericServlet (MyGenericServlet)</th>
                  <th>HttpServlet (NewServlet / GetPostServlet)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Base Hierarchy</strong></td>
                  <td>Direct subclass of <code>java.lang.Object</code> implementing <code>Servlet</code></td>
                  <td>Subclass of <code>javax.servlet.GenericServlet</code></td>
                </tr>
                <tr>
                  <td><strong>Protocol Binding</strong></td>
                  <td>Protocol-independent (applicable to FTP, SMTP, raw TCP sockets)</td>
                  <td>HTTP/HTTPS protocol specific (RFC 7231)</td>
                </tr>
                <tr>
                  <td><strong>Core Lifecycle Method</strong></td>
                  <td>Overrides <code>service(ServletRequest, ServletResponse)</code></td>
                  <td>Overrides <code>doGet()</code>, <code>doPost()</code>, <code>doPut()</code>, <code>doDelete()</code></td>
                </tr>
                <tr>
                  <td><strong>Request/Response Types</strong></td>
                  <td>Accepts generic <code>ServletRequest</code> and <code>ServletResponse</code></td>
                  <td>Accepts HTTP-typed <code>HttpServletRequest</code> and <code>HttpServletResponse</code></td>
                </tr>
                <tr>
                  <td><strong>Typical Production Use</strong></td>
                  <td>Custom non-HTTP daemons or low-level protocol interceptors</td>
                  <td>REST APIs, MVC controllers, and enterprise web applications</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 16 AUTHENTIC SCREENSHOTS GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 12. Authentic Laboratory Execution Screenshot Gallery (16 Figures)
            </h2>
            <span class="badge badge-purple">16 Authentic Student Screenshots</span>
          </div>
          <p>
            All 16 high-resolution screenshots captured directly from NetBeans IDE 8.2 and browser execution environments:
          </p>

          <div class="gallery-grid">

            <!-- FIGURE 1 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.1</span><span class="ss-counter-badge">[1 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: WebApplication8 Project Hierarchy">
                <img src="../assets/images/week-7/w7_web_app_setup.png" alt="NetBeans WebApplication8 Project Setup" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">WebApplication8 Project Structure</div>
                <div class="ss-subcaption">NetBeans IDE 8.2 showing project tree, Web Pages, WEB-INF, and index.html.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_web_app_setup.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 2 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.2</span><span class="ss-counter-badge">[2 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: NewServlet.java HTTP Servlet Code">
                <img src="../assets/images/week-7/w7_newservlet_code_24EU08161.png" alt="NewServlet.java Code with 24EU08161" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NewServlet.java Code (24EU08161)</div>
                <div class="ss-subcaption">NetBeans editor displaying processRequest() writing Roll Number: 24EU08161.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet_code_24EU08161.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 3 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.3</span><span class="ss-counter-badge">[3 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: NewServlet Output (24EU08161)">
                <img src="../assets/images/week-7/w7_newservlet_browser_24EU08161.png" alt="Browser Output for NewServlet 24EU08161" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NewServlet Browser View (24EU08161)</div>
                <div class="ss-subcaption">Browser rendering ADVANCED JAVA LAB, STUDENT DETAILS with Roll Number: 24EU08161.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet_browser_24EU08161.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 4 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.4</span><span class="ss-counter-badge">[4 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans IDE: NewServlet Full Editor">
                <img src="../assets/images/week-7/w7_newservlet_netbeans_ide.jpg" alt="NetBeans IDE NewServlet Full View" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NewServlet IDE Workspace</div>
                <div class="ss-subcaption">NetBeans IDE showing project navigator, compile status, and BUILD SUCCESSFUL.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet_netbeans_ide.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 5 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.5</span><span class="ss-counter-badge">[5 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: NewServlet2.java Code Editor">
                <img src="../assets/images/week-7/w7_newservlet2_code.jpg" alt="NewServlet2.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NewServlet2.java Code Editor</div>
                <div class="ss-subcaption">HttpServlet authoring Register Number: 24U08161 and ADV JAVA LAB header.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet2_code.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 6 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.6</span><span class="ss-counter-badge">[6 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: NewServlet2 Execution Output">
                <img src="../assets/images/week-7/w7_newservlet2_browser.png" alt="Browser NewServlet2 Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">NewServlet2 Browser Output</div>
                <div class="ss-subcaption">Browser rendering HTTP Servlet, Student Details, and Register Number: 24U08161.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_newservlet2_browser.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 7 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.7</span><span class="ss-counter-badge">[7 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: GetPostServlet.java Code">
                <img src="../assets/images/week-7/w7_get_post_servlet_code.png" alt="GetPostServlet.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">GetPostServlet.java Source Code</div>
                <div class="ss-subcaption">NetBeans editor displaying @WebServlet("/GetPostServlet") with doGet() and doPost().</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_get_post_servlet_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 8 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.8</span><span class="ss-counter-badge">[8 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: GET &amp; POST index.html Form Code">
                <img src="../assets/images/week-7/w7_get_post_html_form_code.png" alt="GET and POST index.html Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">HTML Form Markup for GET/POST</div>
                <div class="ss-subcaption">HTML form markup containing both GET and POST submission buttons to GetPostServlet.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_get_post_html_form_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 9 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.9</span><span class="ss-counter-badge">[9 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: GET Request Output (karthik)">
                <img src="../assets/images/week-7/w7_get_request_output.png" alt="Browser GET Request Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Browser GET Request Execution</div>
                <div class="ss-subcaption">Browser response showing "Hello karthik! This is a GET request."</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_get_request_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 10 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.10</span><span class="ss-counter-badge">[10 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: POST Request Output (karthik)">
                <img src="../assets/images/week-7/w7_post_request_output.png" alt="Browser POST Request Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Browser POST Request Execution</div>
                <div class="ss-subcaption">Browser response showing "Hello karthik! This is a POST request."</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_post_request_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 11 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.11</span><span class="ss-counter-badge">[11 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: MyGenericServlet.java Code">
                <img src="../assets/images/week-7/w7_generic_servlet_code.png" alt="MyGenericServlet.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">MyGenericServlet.java Source Code</div>
                <div class="ss-subcaption">GenericServletDemo project showing class extending GenericServlet with service() method.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_generic_servlet_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 12 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.12</span><span class="ss-counter-badge">[12 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: Generic Servlet Output">
                <img src="../assets/images/week-7/w7_generic_servlet_output.png" alt="Generic Servlet Browser Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Generic Servlet Browser View</div>
                <div class="ss-subcaption">Browser rendering "This servlet extends GenericServlet. Hello from GenericServlet!"</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_generic_servlet_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 13 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.13</span><span class="ss-counter-badge">[13 / 16]</span></div>
              <div class="ss-img-wrap" data-title="NetBeans: LifeCycleServlet.java Code">
                <img src="../assets/images/week-7/w7_lifecycle_servlet_code.png" alt="LifeCycleServlet.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">LifeCycleServlet.java Source Code</div>
                <div class="ss-subcaption">Class implementing Servlet interface with init(), service(), and destroy() hooks.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_lifecycle_servlet_code.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 14 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.14</span><span class="ss-counter-badge">[14 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: Servlet Life Cycle Output">
                <img src="../assets/images/week-7/w7_lifecycle_servlet_output.png" alt="Servlet Life Cycle Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Servlet Life Cycle Browser View</div>
                <div class="ss-subcaption">Browser output demonstrating init(): Servlet Initialized, service(): Request Processed.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_lifecycle_servlet_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 15 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.15</span><span class="ss-counter-badge">[15 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: Student Registration Form (karthik, 161, it)">
                <img src="../assets/images/week-7/w7_student_form_browser_input.png" alt="Student Form Input" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Student Registration Form Input</div>
                <div class="ss-subcaption">Browser rendering form.html with entered details: Name: karthik, Roll No: 161, Dept: it.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_student_form_browser_input.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- FIGURE 16 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 7.16</span><span class="ss-counter-badge">[16 / 16]</span></div>
              <div class="ss-img-wrap" data-title="Browser: Student Form Submission Output">
                <img src="../assets/images/week-7/w7_student_form_browser_output.png" alt="Student Form Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Submitted Student Record View</div>
                <div class="ss-subcaption">StudentFormServlet browser response dynamically displaying Name: karthik, Roll No: 161, Dept: it.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-7/w7_student_form_browser_output.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

          </div>
        </section>

        <!-- RESULT -->
        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 13. Result &amp; Learning Outcomes</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Successfully created and deployed Java Web Applications on Apache Tomcat Server in NetBeans IDE 8.2.</div>
            <div class="outcome-item"><span class="check">✔</span> Implemented <code>HttpServlet</code> (NewServlet) rendering student details with Roll Number <strong>24EU08161</strong>.</div>
            <div class="outcome-item"><span class="check">✔</span> Implemented <code>GetPostServlet</code> with dedicated <code>doGet()</code> and <code>doPost()</code> request handlers.</div>
            <div class="outcome-item"><span class="check">✔</span> Mastered protocol-independent <code>GenericServlet</code> via <code>service()</code> method overriding.</div>
            <div class="outcome-item"><span class="check">✔</span> Validated the 3-phase Servlet Life Cycle (<code>init()</code>, <code>service()</code>, <code>destroy()</code>) via <code>LifeCycleServlet</code>.</div>
            <div class="outcome-item"><span class="check">✔</span> Built an interactive Student Registration form successfully processing candidate inputs (<strong>karthik</strong>, Roll: <strong>161</strong>).</div>
          </div>
        </section>
"""

footer = get_page_footer(7)

full_page = header + content + footer

out_path = os.path.join(pages_dir, "week-7.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_page)

print("Updated pages/week-7.html successfully!")
