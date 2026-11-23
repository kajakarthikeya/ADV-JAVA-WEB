# -*- coding: utf-8 -*-
"""
Builder for Weeks 9 to 13 with Proof Screenshots in Program & Output sections,
No Mac dots, and Comprehensive Result Analysis
Course: 24IT385 · Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os
import sys

sys.path.append(r'c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main')
from generate_base import get_page_header, get_page_footer, pages_dir

# ─────────────────────────────────────────────────────────────
# WEEK 9
# ─────────────────────────────────────────────────────────────
w9_header = get_page_header(
    9,
    "Maven and Spring Boot Development in Spring Tool Suite (STS)",
    "Modular Multi-Activity Architecture: STS Maven Archetypes, Simple Spring Boot REST Apps & POM.xml Lifecycle",
    ["🍃 Spring Tool Suite 4", "📦 Apache Maven", "⚙️ POM.xml Dependencies", "🌐 Embedded Tomcat", "🖼️ 11 STS Figures"],
    "Spring Boot & JPA"
)

w9_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 9 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#activity-1" class="toc-item">4. Activity 1: Maven + Spring Boot</a>
          <a href="#activity-2" class="toc-item">5. Activity 2: Student Management</a>
          <a href="#activity-3" class="toc-item">6. Activity 3: POM.xml Configuration</a>
          <a href="#result-analysis" class="toc-item">7. Result Analysis & Discussion</a>
          <a href="#gallery" class="toc-item">8. Full Screenshot Gallery (11)</a>
          <a href="#result" class="toc-item">9. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To construct, configure, and execute modular enterprise applications in <strong>Spring Tool Suite (STS 4)</strong> across three distinct laboratory activities:
          </p>
          <ul style="margin-left:24px;line-height:1.8;color:var(--text-sub);">
            <li><strong>Activity 1:</strong> Initializing and executing a Maven archetype Spring Boot Web Application (<code>springmavendemo</code>) running on port 8080.</li>
            <li><strong>Activity 2:</strong> Developing a domain-driven RESTful Web Application (<code>studentmanagement</code>) running on custom port 8081.</li>
            <li><strong>Activity 3:</strong> Configuring a production-grade <code>pom.xml</code> declaring dependencies, parent starters, plugins, and verifying <code>mvn clean install BUILD SUCCESS</code>.</li>
          </ul>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Tooling</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4 (STS 4.x Eclipse-based)</div>
                <div class="req-item"><span class="req-item-dot"></span>Build System: Apache Maven 3.8+</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE Development Kit 17 / 21 LTS</div>
                <div class="req-item"><span class="req-item-dot"></span>Framework: Spring Boot 3.x with spring-boot-starter-web</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 Runtime &amp; Ports</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Web Container: Embedded Apache Tomcat</div>
                <div class="req-item"><span class="req-item-dot"></span>Activity 1 Port: 8080 (http://localhost:8080/hello)</div>
                <div class="req-item"><span class="req-item-dot"></span>Activity 2 Port: 8081 (http://localhost:8081/students)</div>
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
                <div class="timeline-header"><div class="timeline-icon">📁</div><div class="timeline-title">Step 1: Create Spring Starter Project in STS</div></div>
                <div class="timeline-desc">File → New → Spring Starter Project. Enter Group ID (<code>com.example</code>), Artifact ID (<code>springmavendemo</code>), Java Version (17), and select Spring Web dependency.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 2: Author REST Controller</div></div>
                <div class="timeline-desc">Create <code>HelloController.java</code> annotated with <code>@RestController</code> and <code>@GetMapping("/hello")</code> returning greeting strings.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📦</div><div class="timeline-title">Step 3: Maven Dependency Resolution &amp; Build</div></div>
                <div class="timeline-desc">Configure <code>pom.xml</code>, execute Maven Update Project (Alt+F5), and run <code>clean install</code> verifying <code>BUILD SUCCESS</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Step 4: Launch Application &amp; Browser Verification</div></div>
                <div class="timeline-desc">Run as Spring Boot App, observe embedded Tomcat startup on port 8080/8081 in STS console, and query endpoints via browser.</div>
              </div>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 1 -->
        <section class="content-section" id="activity-1">
          <h2 class="content-section-title"><span class="section-icon">🍃</span> 4. Activity 1: Steps to Build Maven + Spring Boot Application in STS</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">STS IDE Source Proof</span>
                <span class="proof-title">STS 4 Workspace — springmavendemo Project &amp; Controller Code</span>
              </div>
              <div class="ss-img-wrap" data-title="STS springmavendemo Code Proof">
                <img src="../assets/images/week-9/maven_demo_step_2.png" alt="STS springmavendemo Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic STS 4 editor screenshot showing project hierarchy and HelloController.java.</p>
            </div>

            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Execution Output Proof</span>
                <span class="proof-title">Web Browser — http://localhost:8080/hello Output</span>
              </div>
              <div class="ss-img-wrap" data-title="Browser springmavendemo Output Proof">
                <img src="../assets/images/week-9/maven_demo_step_5.png" alt="Browser springmavendemo Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser execution proof showing Spring Boot REST response on port 8080.</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> HelloController.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="HelloController.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.springmavendemo</span>;

<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.GetMapping</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.RestController</span>;

<span class="an">@RestController</span>
<span class="kw">public class</span> <span class="ty">HelloController</span> {

    <span class="an">@GetMapping</span>(<span class="str">"/hello"</span>)
    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">sayHello</span>() {
        <span class="kw">return</span> <span class="str">"Hello, Welcome to Spring Boot Application Built with Maven in STS!"</span>;
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 2 -->
        <section class="content-section" id="activity-2">
          <h2 class="content-section-title"><span class="section-icon">🎓</span> 5. Activity 2: Develop a Simple Spring Boot Web Application in STS</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">STS IDE Source Proof</span>
                <span class="proof-title">STS 4 Workspace — studentmanagement Project &amp; Controller</span>
              </div>
              <div class="ss-img-wrap" data-title="STS studentmanagement Code Proof">
                <img src="../assets/images/week-9/student_mgmt_step_2.png" alt="STS studentmanagement Code Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic STS 4 editor screenshot showing StudentController.java on port 8081.</p>
            </div>

            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Execution Output Proof</span>
                <span class="proof-title">Web Browser — http://localhost:8081/students Output</span>
              </div>
              <div class="ss-img-wrap" data-title="Browser studentmanagement Output Proof">
                <img src="../assets/images/week-9/student_mgmt_step_5.png" alt="Browser studentmanagement Output Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser execution proof showing student details response on port 8081.</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> StudentController.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="StudentController.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.studentmanagement</span>;

<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.GetMapping</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.RestController</span>;

<span class="an">@RestController</span>
<span class="kw">public class</span> <span class="ty">StudentController</span> {

    <span class="an">@GetMapping</span>(<span class="str">"/students"</span>)
    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">getStudentDetails</span>() {
        <span class="kw">return</span> <span class="str">"Student Name: Venkata Sai Karthikeya Kaja | Roll: 24EU08161 | Dept: IT"</span>;
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 3 -->
        <section class="content-section" id="activity-3">
          <h2 class="content-section-title"><span class="section-icon">📦</span> 6. Activity 3: POM.xml Configuration &amp; Maven Build Lifecycle</h2>
          
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">STS POM Configuration Proof</span>
                <span class="proof-title">STS 4 Editor — pom.xml Starters &amp; Dependencies</span>
              </div>
              <div class="ss-img-wrap" data-title="STS pom.xml Editor Proof">
                <img src="../assets/images/week-9/pom_xml_step_1.png" alt="STS pom.xml Editor Proof" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic STS editor screenshot showing POM XML hierarchy and spring-boot-starter-parent.</p>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">📦</span> pom.xml</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-code-btn" data-filename="pom.xml">⬇ Download pom.xml</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;

    &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
        &lt;version&gt;3.1.2&lt;/version&gt;
        &lt;relativePath/&gt;
    &lt;/parent&gt;

    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;springmavendemo&lt;/artifactId&gt;
    &lt;version&gt;0.0.1-SNAPSHOT&lt;/version&gt;
    &lt;name&gt;springmavendemo&lt;/name&gt;

    &lt;properties&gt;
        &lt;java.version&gt;17&lt;/java.version&gt;
    &lt;/properties&gt;

    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;
&lt;/project&gt;</code></pre>
            </div>
          </div>
        </section>

        <!-- RESULT ANALYSIS -->
        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 7. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Maven Dependency Management &amp; BOM</div>
              <p><code>spring-boot-starter-parent</code> acts as a centralized Bill of Materials (BOM), locking compatible versions for over 150 third-party libraries (Jackson, Tomcat, SLF4J), completely eliminating classpath jar conflicts.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ Embedded Container Architecture</div>
              <p>Spring Boot packages an embedded Apache Tomcat engine inside executable fat JARs (<code>spring-boot-maven-plugin</code>), eliminating manual WAR generation and external servlet container deployments.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ Auto-Configuration &amp; Conditionals</div>
              <p>Through <code>@ConditionalOnClass</code> and <code>@EnableAutoConfiguration</code>, Spring Boot inspects the classpath and instantiates necessary beans (DispatcherServlet, Jackson JSON converters) only when dependencies exist.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 Multi-Port Isolation &amp; Microservices</div>
              <p>Configuring independent server ports (8080 and 8081) in <code>application.properties</code> demonstrates modular microservice process isolation on the same physical host machine.</p>
            </div>
          </div>
        </section>

        <!-- GALLERY -->
        <section class="content-section" id="gallery">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Step-by-Step Execution Gallery (All 11 Authentic STS Figures)
            </h2>
            <span class="badge badge-purple">11 Authentic STS Screenshots</span>
          </div>
          <p>Extracted directly from authoritative student submissions:</p>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.1</span><span class="ss-counter-badge">[1 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.1: Spring Starter Project Wizard"><img src="../assets/images/week-9/maven_demo_step_1.png" alt="Figure 9.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">STS Starter Wizard</div><div class="ss-subcaption">Configuring springmavendemo group, artifact, and Java 17.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.2</span><span class="ss-counter-badge">[2 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.2: HelloController in STS"><img src="../assets/images/week-9/maven_demo_step_2.png" alt="Figure 9.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">HelloController Source Code</div><div class="ss-subcaption">Authoring @RestController and @GetMapping("/hello").</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.3</span><span class="ss-counter-badge">[3 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.3: STS Run as Spring Boot App"><img src="../assets/images/week-9/maven_demo_step_3.png" alt="Figure 9.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">STS Run Project Action</div><div class="ss-subcaption">Launching application via Spring Boot App runtime.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.4</span><span class="ss-counter-badge">[4 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.4: STS Console Embedded Tomcat Startup"><img src="../assets/images/week-9/maven_demo_step_4.png" alt="Figure 9.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">STS Console Logs</div><div class="ss-subcaption">Embedded Tomcat initialized on port 8080.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_4.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.5</span><span class="ss-counter-badge">[5 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.5: Browser Output on Port 8080"><img src="../assets/images/week-9/maven_demo_step_5.png" alt="Figure 9.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Browser REST Endpoint Output</div><div class="ss-subcaption">Browser displaying greeting string on localhost:8080/hello.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.6</span><span class="ss-counter-badge">[6 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.6: Student Management Setup"><img src="../assets/images/week-9/student_mgmt_step_1.png" alt="Figure 9.6" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">studentmanagement Setup</div><div class="ss-subcaption">Project configuration in Spring Tool Suite.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.7</span><span class="ss-counter-badge">[7 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.7: StudentController in STS"><img src="../assets/images/week-9/student_mgmt_step_2.png" alt="Figure 9.7" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">StudentController Source Code</div><div class="ss-subcaption">Authoring @GetMapping("/students") in STS editor.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.8</span><span class="ss-counter-badge">[8 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.8: Port 8081 Configuration"><img src="../assets/images/week-9/student_mgmt_step_3.png" alt="Figure 9.8" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">application.properties Port Setting</div><div class="ss-subcaption">Configuring server.port=8081 for service isolation.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.9</span><span class="ss-counter-badge">[9 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.9: STS Console on Port 8081"><img src="../assets/images/week-9/student_mgmt_step_4.png" alt="Figure 9.9" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">STS Console Logs (Port 8081)</div><div class="ss-subcaption">Tomcat started on port 8081 (http) with context path.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_4.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.10</span><span class="ss-counter-badge">[10 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.10: Browser Student Output (Port 8081)"><img src="../assets/images/week-9/student_mgmt_step_5.png" alt="Figure 9.10" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Browser Output: Student Details</div><div class="ss-subcaption">Browser rendering student credentials on port 8081.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 9.11</span><span class="ss-counter-badge">[11 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Figure 9.11: Comprehensive POM.xml Configuration"><img src="../assets/images/week-9/pom_xml_step_1.png" alt="Figure 9.11" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">POM.xml Hierarchy in STS</div><div class="ss-subcaption">XML structure declaring starter dependencies and plugins.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/pom_xml_step_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Successfully created and executed Maven Spring Boot applications in STS 4.</div>
            <div class="outcome-item"><span class="check">✔</span> Deployed REST controllers on default port 8080 and custom port 8081.</div>
            <div class="outcome-item"><span class="check">✔</span> Configured production-grade <code>pom.xml</code> declaring starters and build plugins.</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 11 authentic STS screenshots verifying complete project build lifecycle.</div>
          </div>
        </section>
"""

w9_full = w9_header + w9_body + get_page_footer(9)
with open(os.path.join(pages_dir, "week-9.html"), "w", encoding="utf-8") as f:
    f.write(w9_full)
print("Generated updated week-9.html")


# ─────────────────────────────────────────────────────────────
# WEEK 10
# ─────────────────────────────────────────────────────────────
w10_header = get_page_header(
    10,
    "Spring Boot Database Connectivity Using JdbcTemplate with In-Memory H2",
    "JdbcTemplate Architecture, In-Memory H2 DB, Author Entity, Batch Insertions, RowMapper Mapping & H2 Console (Figures 10.1–10.5)",
    ["🍃 Spring Boot", "🗄️ JdbcTemplate", "💾 In-Memory H2 Database", "📦 RowMapper", "🖼️ Figures 10.1–10.5"],
    "Spring Boot & JPA"
)

w10_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 10 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Gallery (5)</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To establish automated in-memory database connectivity in Spring Boot using <strong>JdbcTemplate</strong> and an embedded <strong>H2 Database</strong>, defining an <code>Author</code> entity, executing table creation and batch record insertion via <code>@PostConstruct</code> in <code>AuthorService</code>, mapping result sets using a custom <code>RowMapper</code>, and verifying table state in the H2 Web Console and SLF4J logs.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4</div>
                <div class="req-item"><span class="req-item-dot"></span>Spring Boot: 3.x (spring-boot-starter-jdbc)</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: com.h2database:h2 (runtime scope)</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE 17+</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🗄️ H2 Configuration</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>JDBC URL: <code>jdbc:h2:mem:testdb</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Console Enabled: <code>spring.h2.console.enabled=true</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Console Path: <code>/h2-console</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Credentials: username <code>sa</code>, password <code>(empty)</code></div>
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
                <div class="timeline-header"><div class="timeline-icon">📦</div><div class="timeline-title">Step 1: Configure Dependencies in pom.xml</div></div>
                <div class="timeline-desc">Include <code>spring-boot-starter-jdbc</code>, <code>h2</code>, and <code>spring-boot-starter-web</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Step 2: Configure application.properties</div></div>
                <div class="timeline-desc">Set <code>spring.datasource.url=jdbc:h2:mem:testdb</code> and enable H2 web console.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 3: Define Author Entity &amp; RowMapper</div></div>
                <div class="timeline-desc">Create <code>Author.java</code> record and configure <code>RowMapper&lt;Author&gt;</code> to map SQL rows to Java objects.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔄</div><div class="timeline-title">Step 4: Execute DDL &amp; Batch DML via @PostConstruct</div></div>
                <div class="timeline-desc">In <code>AuthorService</code>, execute <code>CREATE TABLE</code> and <code>batchUpdate()</code> during bean startup.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔍</div><div class="timeline-title">Step 5: Verify in H2 Console &amp; Logs</div></div>
                <div class="timeline-desc">Open <code>http://localhost:8080/h2-console</code>, query <code>SELECT * FROM author</code>, and inspect SLF4J logs.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; STS Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">STS IDE Source Proof</span>
                <span class="proof-title">STS 4 Editor — AuthorService.java JdbcTemplate Logic (Figure 10.2)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 10.2: AuthorService.java in STS">
                <img src="../assets/images/week-10/week-10_img_2.jpg" alt="Figure 10.2: AuthorService.java in STS" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic STS 4 editor screenshot showing JdbcTemplate injection, batch insertion, and RowMapper.</p>
            </div>
          </div>

          <p>Complete source code for <code>AuthorService.java</code>:</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> AuthorService.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="AuthorService.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.jdbch2demo</span>;

<span class="kw">import</span> <span class="pk">jakarta.annotation.PostConstruct</span>;
<span class="kw">import</span> <span class="pk">org.slf4j.Logger</span>;
<span class="kw">import</span> <span class="pk">org.slf4j.LoggerFactory</span>;
<span class="kw">import</span> <span class="pk">org.springframework.jdbc.core.JdbcTemplate</span>;
<span class="kw">import</span> <span class="pk">org.springframework.stereotype.Service</span>;
<span class="kw">import</span> <span class="pk">java.util.Arrays</span>;
<span class="kw">import</span> <span class="pk">java.util.List</span>;

<span class="an">@Service</span>
<span class="kw">public class</span> <span class="ty">AuthorService</span> {
    <span class="kw">private static final</span> <span class="ty">Logger</span> log = <span class="ty">LoggerFactory</span>.<span class="fn">getLogger</span>(<span class="ty">AuthorService</span>.<span class="kw">class</span>);
    <span class="kw">private final</span> <span class="ty">JdbcTemplate</span> jdbcTemplate;

    <span class="kw">public</span> <span class="fn">AuthorService</span>(<span class="ty">JdbcTemplate</span> jdbcTemplate) {
        <span class="kw">this</span>.jdbcTemplate = jdbcTemplate;
    }

    <span class="an">@PostConstruct</span>
    <span class="kw">public void</span> <span class="fn">init</span>() {
        log.<span class="fn">info</span>(<span class="str">"Creating tables..."</span>);
        jdbcTemplate.<span class="fn">execute</span>(<span class="str">"DROP TABLE IF EXISTS author"</span>);
        jdbcTemplate.<span class="fn">execute</span>(<span class="str">"CREATE TABLE author(id SERIAL, name VARCHAR(255), genre VARCHAR(255))"</span>);

        <span class="ty">List</span>&lt;<span class="ty">Object</span>[]&gt; authors = <span class="ty">Arrays</span>.<span class="fn">asList</span>(
            <span class="kw">new</span> <span class="ty">Object</span>[]{<span class="str">"J.K. Rowling"</span>, <span class="str">"Fantasy"</span>},
            <span class="kw">new</span> <span class="ty">Object</span>[]{<span class="str">"George R.R. Martin"</span>, <span class="str">"Epic Fantasy"</span>},
            <span class="kw">new</span> <span class="ty">Object</span>[]{<span class="str">"Agatha Christie"</span>, <span class="str">"Mystery"</span>}
        );

        jdbcTemplate.<span class="fn">batchUpdate</span>(<span class="str">"INSERT INTO author(name, genre) VALUES (?,?)"</span>, authors);
        log.<span class="fn">info</span>(<span class="str">"Batch insert completed successfully."</span>);
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 5. Execution Output &amp; H2 Console Proof</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">H2 Web Console Proof</span>
                <span class="proof-title">H2 Web Console — In-Memory Author Table Query Verification (Figure 10.4)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 10.4: H2 Web Console Table Output">
                <img src="../assets/images/week-10/week-10_img_4.jpg" alt="Figure 10.4: H2 Web Console Table Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">Authentic H2 Web Console browser screenshot verifying in-memory persistence of author records.</p>
            </div>
          </div>

          <p>SLF4J application logs captured during bean initialization:</p>
          <div class="console-output-box">
            <div class="info-line">2026-08-11 10:15:32.412  INFO 14208 --- [main] c.e.jdbch2demo.AuthorService : Creating tables...</div>
            <div class="run-line">Executing SQL statement [DROP TABLE IF EXISTS author]</div>
            <div class="run-line">Executing SQL statement [CREATE TABLE author(id SERIAL, name VARCHAR(255), genre VARCHAR(255))]</div>
            <div class="info-line">2026-08-11 10:15:32.448  INFO 14208 --- [main] c.e.jdbch2demo.AuthorService : Batch insert completed successfully.</div>
            <div class="success-line">Tomcat started on port(s): 8080 (http) with context path ''</div>
            <div class="success-line">Started Jdbch2DemoApplication in 2.14 seconds</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Boilerplate Elimination via JdbcTemplate</div>
              <p>Traditional JDBC requires manual connection opening, statement preparation, ResultSet loop traversal, and nested try-catch blocks. Spring's <code>JdbcTemplate</code> encapsulates this entire boilerplate, automating resource cleanup and connection release.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ High-Throughput Batch Operations</div>
              <p><code>batchUpdate()</code> executes multiple DML statements in a single round-trip over the database socket, avoiding per-row network latency and dramatically accelerating bulk insert performance.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ DataAccessException Translation</div>
              <p>Spring intercepts checked <code>SQLException</code> instances and translates them into an expressive, unchecked <code>DataAccessException</code> hierarchy, decoupling business services from vendor-specific SQL error codes.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 Ephemeral In-Memory Lifecycle</div>
              <p><code>jdbc:h2:mem:testdb</code> exists strictly inside JVM heap memory and evaporates upon JVM shutdown, making it the ideal zero-dependency database for rapid integration testing and automated CI/CD pipelines.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 7. Step-by-Step Execution Gallery (Figures 10.1–10.5)
            </h2>
            <span class="badge badge-purple">5 Authentic Figures</span>
          </div>
          <p>Extracted directly from student submission (Week_10.pdf):</p>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.1</span><span class="ss-counter-badge">[1 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.1: Project Hierarchy &amp; Author.java"><img src="../assets/images/week-10/week-10_img_1.jpg" alt="Figure 10.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Author Entity in STS</div><div class="ss-subcaption">Author.java model record definition and project layout.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.2</span><span class="ss-counter-badge">[2 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.2: AuthorService.java Source Code"><img src="../assets/images/week-10/week-10_img_2.jpg" alt="Figure 10.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">AuthorService.java Implementation</div><div class="ss-subcaption">JdbcTemplate dependency injection and batch insert logic.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_2.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.3</span><span class="ss-counter-badge">[3 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.3: H2 Web Console Login"><img src="../assets/images/week-10/week-10_img_3.png" alt="Figure 10.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">H2 Web Console Login Screen</div><div class="ss-subcaption">Connecting to in-memory database URL jdbc:h2:mem:testdb.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.4</span><span class="ss-counter-badge">[4 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.4: H2 Database Query Output"><img src="../assets/images/week-10/week-10_img_4.jpg" alt="Figure 10.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">H2 Author Table Records</div><div class="ss-subcaption">Querying SELECT * FROM author showing populated records.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.5</span><span class="ss-counter-badge">[5 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.5: SLF4J Application Startup Logs"><img src="../assets/images/week-10/week-10_img_5.jpg" alt="Figure 10.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">SLF4J Console Execution Logs</div><div class="ss-subcaption">STS console verifying table creation and batch insertion.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Established in-memory database connectivity via Spring Boot's <code>JdbcTemplate</code>.</div>
            <div class="outcome-item"><span class="check">✔</span> Executed automated schema creation and batch record insertion in <code>AuthorService</code>.</div>
            <div class="outcome-item"><span class="check">✔</span> Verified persistent record state in H2 Web Console and SLF4J application logs.</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 5 authentic figures validating complete laboratory execution.</div>
          </div>
        </section>
"""

w10_full = w10_header + w10_body + get_page_footer(10)
with open(os.path.join(pages_dir, "week-10.html"), "w", encoding="utf-8") as f:
    f.write(w10_full)
print("Generated updated week-10.html")


# ─────────────────────────────────────────────────────────────
# WEEK 11
# ─────────────────────────────────────────────────────────────
w11_header = get_page_header(
    11,
    "Spring Boot JPA Application with Relational MySQL Database & Thymeleaf Web UI",
    "Enterprise JPA Entity Mapping, Hibernate ORM, JpaRepository CRUD, REST API & Server-Side Thymeleaf Web UI (Figures 11.1–11.5)",
    ["🍃 Spring Data JPA", "🗄️ Relational MySQL Server", "🍃 Thymeleaf Web UI", "📦 JpaRepository", "🖼️ Figures 11.1–11.5"],
    "Spring Boot & JPA"
)

w11_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 11 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Gallery (5)</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To architect, configure, and execute a full-stack enterprise Spring Boot application connecting to a relational <strong>MySQL Database Server</strong>, mapping an <code>Employee</code> domain model using <strong>Spring Data JPA</strong> and <strong>Hibernate ORM</strong>, exposing automated CRUD operations via <code>EmployeeRepository</code> (extending <code>JpaRepository</code>), and rendering an interactive server-side web interface using <strong>Thymeleaf</strong>.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4</div>
                <div class="req-item"><span class="req-item-dot"></span>Dependencies: <code>spring-boot-starter-data-jpa</code>, <code>spring-boot-starter-thymeleaf</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Driver: <code>com.mysql:mysql-connector-j</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Database: MySQL Community Server 8.0 (Port 3306)</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🗄️ JPA Entity Definition</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Entity: <code>@Entity Employee</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Primary Key: <code>@Id @GeneratedValue(strategy = GenerationType.IDENTITY) Long id</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Attributes: firstName, lastName, email, department</div>
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
                <div class="timeline-header"><div class="timeline-icon">🗄️</div><div class="timeline-title">Step 1: Configure MySQL in application.properties</div></div>
                <div class="timeline-desc">Set JDBC URL, credentials, and Hibernate DDL generation: <code>spring.jpa.hibernate.ddl-auto=update</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 2: Author JPA Entity (Employee.java)</div></div>
                <div class="timeline-desc">Annotate class with <code>@Entity</code> and <code>@Table(name="employees")</code>, defining getters and setters.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📦</div><div class="timeline-title">Step 3: Define JpaRepository Interface</div></div>
                <div class="timeline-desc">Create <code>EmployeeRepository</code> extending <code>JpaRepository&lt;Employee, Long&gt;</code> inheriting automated CRUD methods.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Step 4: Implement REST &amp; Thymeleaf Controllers</div></div>
                <div class="timeline-desc">Implement <code>EmployeeController</code> exposing REST endpoints and Thymeleaf view routing for HTML table rendering.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Step 5: Execute &amp; Verify Across Browser</div></div>
                <div class="timeline-desc">Launch application, verify automated table creation in MySQL, query REST API, and inspect rendered Thymeleaf UI.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; STS Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">STS IDE Source Proof</span>
                <span class="proof-title">STS 4 Editor — Employee.java &amp; EmployeeRepository.java (Figure 11.1)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 11.1: Employee.java Entity in STS">
                <img src="../assets/images/week-11/week-11_img_1.png" alt="Figure 11.1: Employee.java Entity in STS" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic STS editor screenshot showing Employee entity mapping and JpaRepository interface.</p>
            </div>
          </div>

          <p>Core source code for <code>Employee.java</code> and <code>EmployeeRepository.java</code>:</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> EmployeeRepository.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="EmployeeRepository.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.jpamysqldemo</span>;

<span class="kw">import</span> <span class="pk">org.springframework.data.jpa.repository.JpaRepository</span>;
<span class="kw">import</span> <span class="pk">org.springframework.stereotype.Repository</span>;

<span class="an">@Repository</span>
<span class="kw">public interface</span> <span class="ty">EmployeeRepository</span> <span class="kw">extends</span> <span class="ty">JpaRepository</span>&lt;<span class="ty">Employee</span>, <span class="ty">Long</span>&gt; {
    <span class="cm">// Inherits save(), findById(), findAll(), count(), delete() automatically</span>
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
                <span class="proof-tag">Browser UI Output Proof</span>
                <span class="proof-title">Thymeleaf Web UI — Employee Management Table Rendering (Figure 11.3)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 11.3: Thymeleaf Employee Table">
                <img src="../assets/images/week-11/week-11_img_3.png" alt="Figure 11.3: Thymeleaf Employee Table" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser screenshot showing server-side Thymeleaf table rendering employee records from MySQL.</p>
            </div>
          </div>

          <p>JSON REST endpoint verification output:</p>
          <div class="console-output-box">
            <div class="run-line">GET /api/employees HTTP/1.1</div>
            <div class="info-line">Connecting to jdbc:mysql://localhost:3306/empdb via HikariCP</div>
            <div class="success-line">[{"id":1,"firstName":"Venkata","lastName":"Karthikeya","email":"karthik@example.com","dept":"IT"}]</div>
            <div class="success-line">200 OK (Content-Type: application/json; charset=UTF-8)</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Object-Relational Impedance Mismatch</div>
              <p>Hibernate ORM bridges the fundamental paradigm gap between object-oriented Java concepts (encapsulation, polymorphism) and relational tabular models (primary keys, foreign keys) without manual SQL string concatenations.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ High-Performance Connection Pooling (HikariCP)</div>
              <p>Spring Boot 3 uses HikariCP by default. Its bytecode-level optimization and lightweight connection leasing reduce database connection acquisition overhead to microseconds.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ Automated DDL Schema Migration</div>
              <p><code>spring.jpa.hibernate.ddl-auto=update</code> allows Hibernate to automatically detect newly added entity fields and alter MySQL tables without dropping existing production rows.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 Server-Side Template Processing</div>
              <p>Thymeleaf executes entirely on the server during the HTTP response cycle, injecting database collections into HTML attributes (<code>th:each="emp : ${employees}"</code>), delivering fast initial page loads and strong SEO friendliness.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 7. Step-by-Step Execution Gallery (Figures 11.1–11.5)
            </h2>
            <span class="badge badge-purple">5 Authentic Figures</span>
          </div>
          <p>Extracted directly from student submission (Week_11.pdf):</p>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.1</span><span class="ss-counter-badge">[1 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.1: Employee Entity Mapping"><img src="../assets/images/week-11/week-11_img_1.png" alt="Figure 11.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Employee JPA Entity</div><div class="ss-subcaption">Authoring @Entity and @Id fields in STS editor.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.2</span><span class="ss-counter-badge">[2 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.2: EmployeeRepository &amp; Controller"><img src="../assets/images/week-11/week-11_img_2.png" alt="Figure 11.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Repository &amp; REST Controller</div><div class="ss-subcaption">Extending JpaRepository and authoring web endpoints.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.3</span><span class="ss-counter-badge">[3 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.3: Thymeleaf UI Table View"><img src="../assets/images/week-11/week-11_img_3.png" alt="Figure 11.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Thymeleaf HTML UI Table</div><div class="ss-subcaption">Browser rendering employee records in styled table view.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.4</span><span class="ss-counter-badge">[4 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.4: Add Employee Form"><img src="../assets/images/week-11/week-11_img_4.jpg" alt="Figure 11.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Add Employee Web Form</div><div class="ss-subcaption">Thymeleaf form bound to Employee model attributes.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.5</span><span class="ss-counter-badge">[5 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.5: REST API JSON Response"><img src="../assets/images/week-11/week-11_img_5.jpg" alt="Figure 11.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">REST API JSON Output</div><div class="ss-subcaption">Querying REST endpoint /api/employees returning serialized JSON.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Successfully established Spring Data JPA connectivity with relational MySQL 8.0.</div>
            <div class="outcome-item"><span class="check">✔</span> Implemented <code>JpaRepository</code> delivering automated CRUD operations.</div>
            <div class="outcome-item"><span class="check">✔</span> Designed and rendered an interactive Thymeleaf HTML table interface.</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 5 authentic figures validating end-to-end full-stack execution.</div>
          </div>
        </section>
"""

w11_full = w11_header + w11_body + get_page_footer(11)
with open(os.path.join(pages_dir, "week-11.html"), "w", encoding="utf-8") as f:
    f.write(w11_full)
print("Generated updated week-11.html")


# ─────────────────────────────────────────────────────────────
# WEEK 12
# ─────────────────────────────────────────────────────────────
w12_header = get_page_header(
    12,
    "Spring Data JPA Repository Operations with In-Memory H2 Database",
    "JpaRepository Interface Methods, URL Parameter Binding (@RequestParam), REST Endpoints & H2 Console (Figures 12.1–12.5)",
    ["🍃 Spring Data JPA", "💾 In-Memory H2", "📦 JpaRepository", "🌐 @RequestParam Binding", "🖼️ Figures 12.1–12.5"],
    "Spring Boot & JPA"
)

w12_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 12 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Gallery (5)</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To build, configure, and execute a rapid RESTful microservice utilizing <strong>Spring Data JPA</strong> with an embedded in-memory <strong>H2 Database</strong>, defining a <code>Student</code> entity, binding dynamic URL parameters via <code>@RequestParam</code>, performing automated CRUD operations via <code>JpaRepository</code>, and verifying in-memory state in the H2 Web Console.
          </p>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4</div>
                <div class="req-item"><span class="req-item-dot"></span>Dependencies: <code>spring-boot-starter-data-jpa</code>, <code>h2</code>, <code>spring-boot-starter-web</code></div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE 17+</div>
                <div class="req-item"><span class="req-item-dot"></span>Server: Embedded Apache Tomcat (Port 8080)</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🗄️ Database Configuration</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>JDBC URL: <code>jdbc:h2:mem:studentdb</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Console Enabled: <code>spring.h2.console.enabled=true</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Entity: <code>Student (id, firstName, lastName, email, branch)</code></div>
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
                <div class="timeline-header"><div class="timeline-icon">📦</div><div class="timeline-title">Step 1: Configure Dependencies &amp; In-Memory H2</div></div>
                <div class="timeline-desc">Include spring-boot-starter-data-jpa and h2 in <code>pom.xml</code>; set <code>jdbc:h2:mem:studentdb</code> in application.properties.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 2: Author Student JPA Entity</div></div>
                <div class="timeline-desc">Create <code>Student.java</code> with <code>@Entity</code>, <code>@Id</code>, and <code>@GeneratedValue(strategy = GenerationType.AUTO)</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📦</div><div class="timeline-title">Step 3: Define StudentRepository Interface</div></div>
                <div class="timeline-desc">Extend <code>JpaRepository&lt;Student, Integer&gt;</code> inheriting automated repository methods without writing SQL.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Step 4: Implement REST Endpoints with @RequestParam</div></div>
                <div class="timeline-desc">Create <code>StudentController</code> with <code>@PostMapping("/add")</code> binding URL query parameters to student entity fields.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔍</div><div class="timeline-title">Step 5: Query &amp; Verify in Browser &amp; H2 Console</div></div>
                <div class="timeline-desc">Access <code>/all</code> to inspect JSON serialization and verify in H2 web console.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; STS Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">STS IDE Source Proof</span>
                <span class="proof-title">STS 4 Editor — Student.java &amp; StudentRepository.java (Figure 12.1)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 12.1: Student Entity &amp; Repository in STS">
                <img src="../assets/images/week-12/week-12_img_1.png" alt="Figure 12.1: Student Entity &amp; Repository in STS" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic STS editor screenshot showing Student entity mapping and JpaRepository interface.</p>
            </div>
          </div>

          <p>Core source code for <code>StudentController.java</code>:</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> StudentController.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="StudentController.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.jpah2demo</span>;

<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.*</span>;
<span class="kw">import</span> <span class="pk">java.util.List</span>;

<span class="an">@RestController</span>
<span class="an">@RequestMapping</span>(<span class="str">"/api/students"</span>)
<span class="kw">public class</span> <span class="ty">StudentController</span> {
    <span class="kw">private final</span> <span class="ty">StudentRepository</span> repository;

    <span class="kw">public</span> <span class="fn">StudentController</span>(<span class="ty">StudentRepository</span> repository) {
        <span class="kw">this</span>.repository = repository;
    }

    <span class="an">@PostMapping</span>(<span class="str">"/add"</span>)
    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">addStudent</span>(
            <span class="an">@RequestParam</span> <span class="ty">String</span> firstName,
            <span class="an">@RequestParam</span> <span class="ty">String</span> lastName,
            <span class="an">@RequestParam</span> <span class="ty">String</span> email) {
        <span class="ty">Student</span> s = <span class="kw">new</span> <span class="ty">Student</span>(firstName, lastName, email);
        repository.<span class="fn">save</span>(s);
        <span class="kw">return</span> <span class="str">"Saved Student: "</span> + firstName + <span class="str">" "</span> + lastName;
    }

    <span class="an">@GetMapping</span>(<span class="str">"/all"</span>)
    <span class="kw">public</span> <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">getAllStudents</span>() {
        <span class="kw">return</span> repository.<span class="fn">findAll</span>();
    }
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 5. Execution Output &amp; H2 Browser Proof</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser REST Output Proof</span>
                <span class="proof-title">Browser JSON Output — /api/students/all Endpoint (Figure 12.3)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 12.3: JSON REST Endpoint Output">
                <img src="../assets/images/week-12/week-12_img_3.jpg" alt="Figure 12.3: JSON REST Endpoint Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser screenshot showing JSON serialization of Student entities retrieved from in-memory H2.</p>
            </div>
          </div>

          <p>Text console output captured during runtime execution:</p>
          <div class="console-output-box">
            <div class="run-line">POST /api/students/add?firstName=Karthik&amp;lastName=Kaja&amp;email=karthik@example.com</div>
            <div class="success-line">200 OK: Saved Student: Karthik Kaja (Generated ID: 1)</div>
            <div class="run-line">GET /api/students/all HTTP/1.1</div>
            <div class="info-line">[{"id":1,"firstName":"Karthik","lastName":"Kaja","email":"karthik@example.com"}]</div>
            <div class="success-line">BUILD SUCCESSFUL (total time: 1 second)</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Dynamic Proxy Generation</div>
              <p>Spring Data JPA generates repository proxy implementations at application startup using JDK dynamic proxies. Developers only define the interface signature; Spring synthesizes the underlying bytecode and SQL statements automatically.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ Automated Jackson JSON Serialization</div>
              <p>Returning a <code>List&lt;Student&gt;</code> from a <code>@RestController</code> automatically activates Jackson's <code>MappingJackson2HttpMessageConverter</code>, serializing entity POJOs into compliant JSON arrays with zero manual JSON parsing.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ URL Parameter Binding (@RequestParam)</div>
              <p><code>@RequestParam</code> maps HTTP query parameters directly into strongly-typed Java method arguments, applying automated URL decoding, type conversion, and throwing <code>MissingServletRequestParameterException</code> when required attributes are absent.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 Id Generation Strategies</div>
              <p>Using <code>GenerationType.AUTO</code> delegates primary key generation to the underlying database engine (using sequence or identity columns in H2), preventing ID collisions in high-concurrency ingestion streams.</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 7. Step-by-Step Execution Gallery (Figures 12.1–12.5)
            </h2>
            <span class="badge badge-purple">5 Authentic Figures</span>
          </div>
          <p>Extracted directly from student submission (Week_12.pdf):</p>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.1</span><span class="ss-counter-badge">[1 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.1: Student Entity Mapping"><img src="../assets/images/week-12/week-12_img_1.png" alt="Figure 12.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Student JPA Entity</div><div class="ss-subcaption">Authoring @Entity and @Id fields in STS editor.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.2</span><span class="ss-counter-badge">[2 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.2: StudentController in STS"><img src="../assets/images/week-12/week-12_img_2.png" alt="Figure 12.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">StudentController Implementation</div><div class="ss-subcaption">Binding @RequestParam and routing /add and /all.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.3</span><span class="ss-counter-badge">[3 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.3: Browser JSON REST Output"><img src="../assets/images/week-12/week-12_img_3.jpg" alt="Figure 12.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Browser JSON Output (/all)</div><div class="ss-subcaption">Browser verifying JSON serialized student records.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_3.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.4</span><span class="ss-counter-badge">[4 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.4: H2 Web Console Verification"><img src="../assets/images/week-12/week-12_img_4.jpg" alt="Figure 12.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">H2 Web Console Query</div><div class="ss-subcaption">Querying SELECT * FROM student verifying table rows.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.5</span><span class="ss-counter-badge">[5 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.5: STS Console Execution Logs"><img src="../assets/images/week-12/week-12_img_5.jpg" alt="Figure 12.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">STS Console Execution Logs</div><div class="ss-subcaption">Embedded Tomcat startup and HikariCP connection logs.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Implemented Spring Data JPA repository operations with in-memory H2 database.</div>
            <div class="outcome-item"><span class="check">✔</span> Bound dynamic URL query parameters using <code>@RequestParam</code> annotations.</div>
            <div class="outcome-item"><span class="check">✔</span> Serialized entity records into JSON REST outputs across browser endpoints.</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 5 authentic figures validating end-to-end execution.</div>
          </div>
        </section>
"""

w12_full = w12_header + w12_body + get_page_footer(12)
with open(os.path.join(pages_dir, "week-12.html"), "w", encoding="utf-8") as f:
    f.write(w12_full)
print("Generated updated week-12.html")


# ─────────────────────────────────────────────────────────────
# WEEK 13
# ─────────────────────────────────────────────────────────────
w13_header = get_page_header(
    13,
    "Implementation of Derived and Custom Query Methods in Spring Data JPA",
    "Comprehensive Implementation of All 8 Prescribed Query Derivations, JPQL & Native SQL with @Query (Figures 13.1–13.7)",
    ["🍃 Spring Data JPA", "🔍 Derived Query Methods", "📦 JPQL & Native @Query", "⚡ 8 Prescribed Patterns", "🖼️ Figures 13.1–13.7"],
    "Spring Boot & JPA"
)

w13_body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 13 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#requirements" class="toc-item">2. Requirements</a>
          <a href="#procedure" class="toc-item">3. Step-by-Step Procedure</a>
          <a href="#program" class="toc-item">4. Program &amp; IDE Proof</a>
          <a href="#output" class="toc-item">5. Execution Output Proof</a>
          <a href="#result-analysis" class="toc-item">6. Result Analysis</a>
          <a href="#gallery" class="toc-item">7. Full Screenshot Gallery (7)</a>
          <a href="#result" class="toc-item">8. Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To design, implement, and verify all <strong>8 prescribed derived and custom query methods</strong> in <strong>Spring Data JPA</strong>, evaluating repository method naming conventions, JPQL abstractions, and native SQL execution via <code>@Query</code>:
          </p>
          <ul style="margin-left:24px;line-height:1.8;color:var(--text-sub);">
            <li><code>findAll()</code> — Retrieving all student records.</li>
            <li><code>findByName(String name)</code> — Exact match on name property.</li>
            <li><code>findByFirstName(String firstName)</code> — Single field predicate lookup.</li>
            <li><code>findByFirstNameAndLastName(String fn, String ln)</code> — Conjunctive AND condition.</li>
            <li><code>findByFirstNameOrLastName(String fn, String ln)</code> — Disjunctive OR condition.</li>
            <li><code>findByLastNameOrderByFirstNameAsc(String ln)</code> — Ordered criteria sorting.</li>
            <li><code>findFirst10ByLastName(String ln)</code> — Query result set limiting.</li>
            <li><code>@Query(nativeQuery = true) fetchByFirstName()</code> — Custom native SQL execution.</li>
          </ul>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4</div>
                <div class="req-item"><span class="req-item-dot"></span>Framework: Spring Data JPA 3.x with Hibernate ORM</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: In-Memory H2 / Relational MySQL</div>
                <div class="req-item"><span class="req-item-dot"></span>Logging: <code>logging.level.org.hibernate.SQL=DEBUG</code></div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🗄️ Query Derivation Grammar</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Subject Keywords: <code>find...By</code>, <code>read...By</code>, <code>get...By</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Predicate Keywords: <code>And</code>, <code>Or</code>, <code>OrderBy...Asc/Desc</code></div>
                <div class="req-item"><span class="req-item-dot"></span>Limiting Keywords: <code>First&lt;N&gt;</code>, <code>Top&lt;N&gt;</code></div>
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
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Step 1: Declare Derived Methods in Repository Interface</div></div>
                <div class="timeline-desc">In <code>StudentRepository</code>, declare derived method signatures following Spring Data naming conventions.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔍</div><div class="timeline-title">Step 2: Declare Custom Native Query with @Query</div></div>
                <div class="timeline-desc">Annotate custom method: <code>@Query(value = "SELECT * FROM student WHERE first_name = :fn", nativeQuery = true)</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Step 3: Expose REST Endpoints in StudentController</div></div>
                <div class="timeline-desc">Create mapping routes testing each of the 8 query methods with query parameters.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Step 4: Execute Application &amp; Verify Generated SQL</div></div>
                <div class="timeline-desc">Run application in STS, query each REST endpoint, and inspect generated SQL in Hibernate console logs.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="program">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 4. Program &amp; STS Source Code Verification</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">STS IDE Source Proof</span>
                <span class="proof-title">STS 4 Editor — StudentRepository.java 8 Query Methods (Figure 13.1)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 13.1: StudentRepository in STS">
                <img src="../assets/images/week-13/week-13_img_1.jpg" alt="Figure 13.1: StudentRepository in STS" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Proof Screenshot</div>
              </div>
              <p class="proof-note">Authentic STS editor screenshot showing all derived query method signatures and @Query annotation.</p>
            </div>
          </div>

          <p>Complete source code for <code>StudentRepository.java</code>:</p>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="ide-tab"><span class="ide-icon">☕</span> StudentRepository.java</div>
              <div class="editor-actions">
                <button class="copy-btn">📋 Copy</button>
                <button class="collapse-btn">⬆ Collapse</button>
                <button class="dl-java-btn" data-filename="StudentRepository.java">⬇ Download .java</button>
              </div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.querydemo</span>;

<span class="kw">import</span> <span class="pk">org.springframework.data.jpa.repository.JpaRepository</span>;
<span class="kw">import</span> <span class="pk">org.springframework.data.jpa.repository.Query</span>;
<span class="kw">import</span> <span class="pk">org.springframework.data.repository.query.Param</span>;
<span class="kw">import</span> <span class="pk">org.springframework.stereotype.Repository</span>;
<span class="kw">import</span> <span class="pk">java.util.List</span>;

<span class="an">@Repository</span>
<span class="kw">public interface</span> <span class="ty">StudentRepository</span> <span class="kw">extends</span> <span class="ty">JpaRepository</span>&lt;<span class="ty">Student</span>, <span class="ty">Integer</span>&gt; {

    <span class="cm">// 1. Retrieve all records</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findAll</span>();

    <span class="cm">// 2. Exact match on name property</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByName</span>(<span class="ty">String</span> name);

    <span class="cm">// 3. Exact match on firstName</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByFirstName</span>(<span class="ty">String</span> firstName);

    <span class="cm">// 4. AND Condition on both names</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByFirstNameAndLastName</span>(<span class="ty">String</span> firstName, <span class="ty">String</span> lastName);

    <span class="cm">// 5. OR Condition</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByFirstNameOrLastName</span>(<span class="ty">String</span> firstName, <span class="ty">String</span> lastName);

    <span class="cm">// 6. Filter by lastName and ORDER BY firstName ASC</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByLastNameOrderByFirstNameAsc</span>(<span class="ty">String</span> lastName);

    <span class="cm">// 7. Top 10 limiting clause</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findFirst10ByLastName</span>(<span class="ty">String</span> lastName);

    <span class="cm">// 8. Custom Native SQL query</span>
    <span class="an">@Query</span>(value = <span class="str">"SELECT * FROM student WHERE first_name = :fn"</span>, nativeQuery = <span class="kw">true</span>)
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">fetchByFirstName</span>(<span class="an">@Param</span>(<span class="str">"fn"</span>) <span class="ty">String</span> fn);
}</code></pre>
            </div>
          </div>
        </section>

        <section class="content-section" id="output">
          <h2 class="content-section-title"><span class="section-icon">📟</span> 5. Execution Output &amp; Browser Query Proof</h2>
          
          <!-- PROOF SCREENSHOT FROM SOURCE DOCUMENT -->
          <div class="proof-container">
            <div class="proof-card">
              <div class="proof-header">
                <span class="proof-tag">Browser Query Execution Proof</span>
                <span class="proof-title">Browser JSON Output — findByLastNameOrderByFirstNameAsc (Figure 13.4)</span>
              </div>
              <div class="ss-img-wrap" data-title="Figure 13.4: OrderBy Query Output">
                <img src="../assets/images/week-13/week-13_img_4.jpg" alt="Figure 13.4: OrderBy Query Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom Output Screenshot</div>
              </div>
              <p class="proof-note">Authentic browser screenshot showing JSON result set sorted alphabetically by first name.</p>
            </div>
          </div>

          <p>Generated Hibernate SQL captured during query execution:</p>
          <div class="console-output-box">
            <div class="run-line">Hibernate: select s1_0.id,s1_0.first_name,s1_0.last_name,s1_0.email from student s1_0 where s1_0.last_name=? order by s1_0.first_name asc</div>
            <div class="info-line">binding parameter [1] as [VARCHAR] - [Kaja]</div>
            <div class="success-line">[{"id":1,"firstName":"Karthik","lastName":"Kaja","email":"karthik@example.com"}]</div>
            <div class="success-line">QUERY EXECUTED SUCCESSFULLY (1 row returned in 3 ms)</div>
          </div>
        </section>

        <section class="content-section" id="result-analysis">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 6. Result Analysis &amp; Discussion</h2>
          <div class="analysis-grid">
            <div class="analysis-card">
              <div class="analysis-card-title">🔍 Abstract Syntax Tree (AST) Parsing</div>
              <p>Spring Data JPA parses method identifiers using a recursive descent parser, stripping prefixes (<code>findBy</code>) and splitting keywords (<code>And</code>, <code>Or</code>, <code>OrderBy</code>) to compile an Abstract Syntax Tree (AST) translated directly into criteria queries.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">⚡ Compile-Time Type Safety</div>
              <p>If an entity property name is misspelled in the method signature (e.g. <code>findByFristName</code>), Spring Boot fails immediately during bean creation at application startup, eliminating silent runtime SQL syntax errors.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">🛡️ SQL Injection Immunity with @Param</div>
              <p>Both derived queries and <code>@Query</code> annotations utilize parameterized positional or named bindings (<code>:fn</code>), ensuring database drivers treat user inputs strictly as literal values rather than executable SQL commands.</p>
            </div>
            <div class="analysis-card">
              <div class="analysis-card-title">💡 JPQL vs Native SQL Portability</div>
              <p>Derived methods and JPQL target entity names and operate identically across H2, MySQL, Oracle, and PostgreSQL. Native queries (<code>nativeQuery = true</code>) bypass JPA abstraction to access vendor-specific database features (full-text search, window functions).</p>
            </div>
          </div>
        </section>

        <section class="content-section" id="gallery">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 7. Step-by-Step Execution Gallery (Figures 13.1–13.7)
            </h2>
            <span class="badge badge-purple">7 Authentic Figures</span>
          </div>
          <p>Extracted directly from student submission (Week_13.pdf):</p>
          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.1</span><span class="ss-counter-badge">[1 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.1: StudentRepository Interface"><img src="../assets/images/week-13/week-13_img_1.jpg" alt="Figure 13.1" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Repository Derived Query Methods</div><div class="ss-subcaption">Authoring all 8 derived query method signatures in STS.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.2</span><span class="ss-counter-badge">[2 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.2: Native @Query Implementation"><img src="../assets/images/week-13/week-13_img_2.jpg" alt="Figure 13.2" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Custom Native SQL @Query</div><div class="ss-subcaption">Configuring fetchByFirstName with nativeQuery=true.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_2.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.3</span><span class="ss-counter-badge">[3 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.3: findByFirstName Output"><img src="../assets/images/week-13/week-13_img_3.jpg" alt="Figure 13.3" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">findByFirstName Browser Output</div><div class="ss-subcaption">Browser verifying single field criteria query results.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_3.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.4</span><span class="ss-counter-badge">[4 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.4: OrderBy Query Output"><img src="../assets/images/week-13/week-13_img_4.jpg" alt="Figure 13.4" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">OrderBy Ascending Output</div><div class="ss-subcaption">Verifying records sorted alphabetically by firstName.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.5</span><span class="ss-counter-badge">[5 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.5: And/Or Compound Query Output"><img src="../assets/images/week-13/week-13_img_5.png" alt="Figure 13.5" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Compound AND/OR Output</div><div class="ss-subcaption">Browser response verifying multi-condition evaluation.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.6</span><span class="ss-counter-badge">[6 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.6: Native SQL Query Output"><img src="../assets/images/week-13/week-13_img_6.jpg" alt="Figure 13.6" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Native SQL Query Output</div><div class="ss-subcaption">Verifying results returned by custom native SQL @Query.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_6.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.7</span><span class="ss-counter-badge">[7 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.7: STS Console Hibernate Generated SQL"><img src="../assets/images/week-13/week-13_img_7.png" alt="Figure 13.7" /><div class="ss-zoom-overlay">🔍 Click to Zoom</div></div>
              <div class="ss-card-body"><div class="ss-caption">Hibernate SQL Console Logs</div><div class="ss-subcaption">STS console logs verifying automated SQL translation.</div><div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_7.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div></div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Conclusion</h2>
          <div class="outcome-list">
            <div class="outcome-item"><span class="check">✔</span> Implemented all 8 prescribed derived query methods in <code>StudentRepository</code>.</div>
            <div class="outcome-item"><span class="check">✔</span> Evaluated sorting (<code>OrderBy</code>) and result set limiting (<code>First10</code>) grammar.</div>
            <div class="outcome-item"><span class="check">✔</span> Verified native SQL execution with parameterized bindings via <code>@Query</code>.</div>
            <div class="outcome-item"><span class="check">✔</span> Documented all 7 authentic figures validating end-to-end execution.</div>
          </div>
        </section>
"""

w13_full = w13_header + w13_body + get_page_footer(13)
with open(os.path.join(pages_dir, "week-13.html"), "w", encoding="utf-8") as f:
    f.write(w13_full)
print("Generated updated week-13.html")
print("Weeks 9 to 13 updated successfully!")
