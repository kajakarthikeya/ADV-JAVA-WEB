# -*- coding: utf-8 -*-
"""
Generator for Weeks 9 to 13
Advanced Java Programming Lab (24IT385)
Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os
from generate_base import get_page_header, get_page_footer

pages_dir = r'C:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\pages'

# ==============================================================================
# WEEK 9: Maven and Spring Boot Development
# ==============================================================================
def generate_week_9():
    header = get_page_header(
        9,
        "Maven Project Lifecycle and Spring Boot Application Development",
        "Configuring Maven Projects, Building REST Web Services in STS, and POM.xml Architecture",
        ["🍃 Spring Tool Suite 4 (STS)", "📦 Apache Maven 3.x", "🌱 Spring Boot 3.3.5", "📄 POM.xml Dependencies", "🌐 REST Endpoints"],
        "Spring Boot & JPA"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 9 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#intro" class="toc-item">2. Overview & Theory</a>
          <a href="#requirements" class="toc-item">3. Requirements</a>
          <a href="#act1" class="toc-item">4. Activity 1: SpringMavenDemo</a>
          <a href="#act2" class="toc-item">5. Activity 2: StudentManagement</a>
          <a href="#act3" class="toc-item">6. Activity 3: POM.xml Deep-Dive</a>
          <a href="#code" class="toc-item">7. Source Code Files</a>
          <a href="#screenshots" class="toc-item">8. Screenshot Gallery (11)</a>
          <a href="#result" class="toc-item">9. Result & Conclusion</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim</h2>
          <p>
            To master the Apache Maven project build lifecycle in Spring Tool Suite (STS), construct standalone Spring Boot web applications, configure dependencies and build plugins in <code>pom.xml</code>, execute <code>clean install</code> builds, and verify REST endpoints in a web browser.
          </p>
        </section>

        <section class="content-section" id="intro">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 2. Theoretical Background</h2>
          <p>
            <strong>Apache Maven</strong> is a comprehensive software project management and comprehension tool. Based on the concept of a Project Object Model (POM), Maven manages a project's build, reporting, and documentation from a central configuration file (<code>pom.xml</code>).
          </p>
          <p>
            <strong>Spring Boot</strong> eliminates traditional enterprise Java boilerplate by introducing:
          </p>
          <ul style="margin-left:20px;line-height:1.8;">
            <li><strong>Starter POMs:</strong> Curated dependency descriptors (e.g., <code>spring-boot-starter-web</code>) bundling Spring MVC, Jackson JSON, and Hibernate Validator.</li>
            <li><strong>Auto-Configuration:</strong> Automatic configuration of beans based on JARs present on the classpath.</li>
            <li><strong>Embedded Web Servers:</strong> Standalone deployment packaging Tomcat directly inside the executable JAR.</li>
          </ul>
        </section>

        <section class="content-section" id="requirements">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 3. Software Requirements</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">💻 Development Tools</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4 (STS 4.41.0+)</div>
                <div class="req-item"><span class="req-item-dot"></span>JDK: Java SE 17 LTS (Eclipse Adoptium)</div>
                <div class="req-item"><span class="req-item-dot"></span>Build Tool: Apache Maven (embedded in STS)</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">🌐 Deployment & Browser</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Browser: Google Chrome / Edge</div>
                <div class="req-item"><span class="req-item-dot"></span>Ports: 8080 (Demo) & 8081 (StudentManagement)</div>
                <div class="req-item"><span class="req-item-dot"></span>OS: Microsoft Windows 10/11 64-bit</div>
              </div>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 1 -->
        <section class="content-section" id="act1">
          <h2 class="content-section-title"><span class="section-icon">🚀</span> 4. Activity 1: Steps to Build Maven + Spring Boot Application in STS</h2>
          <p><strong>Project Name:</strong> <code>springmavendemo</code> | <strong>Artifact:</strong> <code>springmavendemo</code> | <strong>Port:</strong> <code>8080</code></p>
          
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📁</div><div class="timeline-title">Create Maven Project</div></div>
                <div class="timeline-desc">Open STS → File → New → Maven Project → Select <em>Create a simple project (skip archetype selection)</em>. Group Id: <code>com.example</code>, Artifact Id: <code>springmavendemo</code>, Packaging: <code>jar</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Configure Java Build Path</div></div>
                <div class="timeline-desc">Project Properties → Java Build Path → Libraries → Set JRE System Library to <code>JavaSE-17</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📄</div><div class="timeline-title">Configure pom.xml & Update Project</div></div>
                <div class="timeline-desc">Add <code>spring-boot-starter-parent</code> (3.3.5) and <code>spring-boot-starter-web</code>. Right-click project → Maven → Update Project.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Create Application & Controller</div></div>
                <div class="timeline-desc">Create <code>SpringMavenDemoApplication.java</code> with <code>@SpringBootApplication</code> and <code>HelloController.java</code> with <code>@RestController</code> returning <code>"Hello, Maven + Spring Boot!"</code> at <code>/</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🔨</div><div class="timeline-title">Maven Build & Verification</div></div>
                <div class="timeline-desc">Run As → Maven Build (<code>clean install</code>) → verify <code>BUILD SUCCESS</code>. Launch application and test <code>http://localhost:8080/</code>.</div>
              </div>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 2 -->
        <section class="content-section" id="act2">
          <h2 class="content-section-title"><span class="section-icon">🎓</span> 5. Activity 2: Develop a Simple Spring Boot Web Application in STS</h2>
          <p><strong>Project Name:</strong> <code>StudentManagement</code> | <strong>Artifact:</strong> <code>studentmanagement</code> | <strong>Port:</strong> <code>8081</code></p>
          
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📁</div><div class="timeline-title">Scaffold studentmanagement Project</div></div>
                <div class="timeline-desc">Create simple Maven project in STS: Group Id: <code>com.example</code>, Artifact Id: <code>studentmanagement</code>, Version: <code>1.0.0</code>, Name: <code>StudentManagement</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">💻</div><div class="timeline-title">Implement StudentController</div></div>
                <div class="timeline-desc">
                  Create package <code>com.example.studentmanagement.controller</code> and class <code>StudentController</code> with <code>@GetMapping("/students")</code> returning <code>"Student Management System"</code>.
                </div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Configure application.properties</div></div>
                <div class="timeline-desc">Inside <code>src/main/resources/application.properties</code>, add <code>server.port=8081</code> to prevent port conflicts with port 8080.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Browser Verification</div></div>
                <div class="timeline-desc">Launch application in STS and navigate to <code>http://localhost:8081/students</code>, verifying output string <code>Student Management System</code>.</div>
              </div>
            </div>
          </div>
        </section>

        <!-- ACTIVITY 3 -->
        <section class="content-section" id="act3">
          <h2 class="content-section-title"><span class="section-icon">📄</span> 6. Activity 3: POM.xml Configuration Deep-Dive</h2>
          <div class="table-wrap">
            <table>
              <thead><tr><th>POM Element</th><th>Configured Value</th><th>Architectural Purpose</th></tr></thead>
              <tbody>
                <tr><td><code>&lt;parent&gt;</code></td><td><code>spring-boot-starter-parent (3.3.5)</code></td><td>Provides dependency management, plugin management, and sensible defaults.</td></tr>
                <tr><td><code>&lt;properties&gt;</code></td><td><code>&lt;java.version&gt;17&lt;/java.version&gt;</code></td><td>Instructs maven-compiler-plugin to target Java 17 bytecode semantics.</td></tr>
                <tr><td><code>&lt;dependencies&gt;</code></td><td><code>spring-boot-starter-web</code></td><td>Transitively imports Spring MVC, Tomcat 10, Jackson JSON, and validation.</td></tr>
                <tr><td><code>&lt;build&gt;&lt;plugins&gt;</code></td><td><code>spring-boot-maven-plugin</code></td><td>Packages compiled classes into a fat executable uber-JAR with embedded server.</td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- SOURCE CODE -->
        <section class="content-section" id="code">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 7. Source Code Modules</h2>
          
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">pom.xml</span>
              <div class="editor-actions"><button class="copy-btn">📋 Copy</button><button class="dl-java-btn" data-filename="pom.xml">⬇ Download .xml</button></div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">&lt;project</span> <span class="ty">xmlns</span>=<span class="str">"http://maven.apache.org/POM/4.0.0"</span>
         <span class="ty">xmlns:xsi</span>=<span class="str">"http://www.w3.org/2001/XMLSchema-instance"</span>
         <span class="ty">xsi:schemaLocation</span>=<span class="str">"http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"</span><span class="kw">&gt;</span>
    <span class="kw">&lt;modelVersion&gt;</span>4.0.0<span class="kw">&lt;/modelVersion&gt;</span>
    <span class="kw">&lt;parent&gt;</span>
        <span class="kw">&lt;groupId&gt;</span>org.springframework.boot<span class="kw">&lt;/groupId&gt;</span>
        <span class="kw">&lt;artifactId&gt;</span>spring-boot-starter-parent<span class="kw">&lt;/artifactId&gt;</span>
        <span class="kw">&lt;version&gt;</span>3.3.5<span class="kw">&lt;/version&gt;</span>
        <span class="kw">&lt;relativePath/&gt;</span>
    <span class="kw">&lt;/parent&gt;</span>
    <span class="kw">&lt;groupId&gt;</span>com.example<span class="kw">&lt;/groupId&gt;</span>
    <span class="kw">&lt;artifactId&gt;</span>studentmanagement<span class="kw">&lt;/artifactId&gt;</span>
    <span class="kw">&lt;version&gt;</span>1.0.0<span class="kw">&lt;/version&gt;</span>
    <span class="kw">&lt;properties&gt;</span>
        <span class="kw">&lt;java.version&gt;</span>17<span class="kw">&lt;/java.version&gt;</span>
    <span class="kw">&lt;/properties&gt;</span>
    <span class="kw">&lt;dependencies&gt;</span>
        <span class="kw">&lt;dependency&gt;</span>
            <span class="kw">&lt;groupId&gt;</span>org.springframework.boot<span class="kw">&lt;/groupId&gt;</span>
            <span class="kw">&lt;artifactId&gt;</span>spring-boot-starter-web<span class="kw">&lt;/artifactId&gt;</span>
        <span class="kw">&lt;/dependency&gt;</span>
    <span class="kw">&lt;/dependencies&gt;</span>
    <span class="kw">&lt;build&gt;</span>
        <span class="kw">&lt;plugins&gt;</span>
            <span class="kw">&lt;plugin&gt;</span>
                <span class="kw">&lt;groupId&gt;</span>org.springframework.boot<span class="kw">&lt;/groupId&gt;</span>
                <span class="kw">&lt;artifactId&gt;</span>spring-boot-maven-plugin<span class="kw">&lt;/artifactId&gt;</span>
            <span class="kw">&lt;/plugin&gt;</span>
        <span class="kw">&lt;/plugins&gt;</span>
    <span class="kw">&lt;/build&gt;</span>
<span class="kw">&lt;/project&gt;</span></code></pre>
            </div>
          </div>
        </section>

        <!-- SCREENSHOT GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 8. Original Lab Screenshots (All 11 Screenshots)
            </h2>
            <span class="badge badge-purple">11 Authentic STS Screenshots</span>
          </div>
          <p>Extracted from original laboratory documents (Steps to Build Maven...docx, Develop A Simple...docx, POM.XML...docx):</p>

          <div class="gallery-grid">
            <!-- Act 1 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 1.1</span><span class="ss-counter-badge">[1 / 11]</span></div>
              <div class="ss-img-wrap" data-title="STS Package Explorer & Console Banner">
                <img src="../assets/images/week-9/maven_demo_step_1.png" alt="STS Package Explorer & Console Banner" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">STS Console & Explorer</div>
                <div class="ss-subcaption">Spring Tool Suite 4 showing springmavendemo project tree and Spring Boot banner.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 1.2</span><span class="ss-counter-badge">[2 / 11]</span></div>
              <div class="ss-img-wrap" data-title="STS Package Explorer Tree View">
                <img src="../assets/images/week-9/maven_demo_step_2.png" alt="STS Package Explorer Tree View" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Project Package Structure</div>
                <div class="ss-subcaption">Detailed tree view of springmavendemo packages, classes, and pom.xml.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 1.3</span><span class="ss-counter-badge">[3 / 11]</span></div>
              <div class="ss-img-wrap" data-title="SpringMavenDemoApplication.java Code">
                <img src="../assets/images/week-9/maven_demo_step_3.png" alt="SpringMavenDemoApplication.java Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Main Application Class</div>
                <div class="ss-subcaption">STS editor showing @SpringBootApplication entry point class.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 1.4</span><span class="ss-counter-badge">[4 / 11]</span></div>
              <div class="ss-img-wrap" data-title="HelloController.java RestController">
                <img src="../assets/images/week-9/maven_demo_step_4.png" alt="HelloController.java RestController" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">HelloController REST Endpoint</div>
                <div class="ss-subcaption">STS editor showing @RestController and @GetMapping("/") handler method.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_4.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 1.5</span><span class="ss-counter-badge">[5 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Browser: localhost:8080 Output">
                <img src="../assets/images/week-9/maven_demo_step_5.png" alt="Browser: localhost:8080 Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Browser: Port 8080 Endpoint</div>
                <div class="ss-subcaption">Browser verifying endpoint response: "Hello, Maven + Spring Boot!".</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/maven_demo_step_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Act 2 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 2.1</span><span class="ss-counter-badge">[6 / 11]</span></div>
              <div class="ss-img-wrap" data-title="StudentManagement STS Structure">
                <img src="../assets/images/week-9/student_mgmt_step_1.png" alt="StudentManagement STS Structure" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">StudentManagement Project</div>
                <div class="ss-subcaption">STS workspace displaying studentmanagement project tree and editor panes.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 2.2</span><span class="ss-counter-badge">[7 / 11]</span></div>
              <div class="ss-img-wrap" data-title="StudentManagement Tree Explorer">
                <img src="../assets/images/week-9/student_mgmt_step_2.png" alt="StudentManagement Tree Explorer" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Package Explorer Tree</div>
                <div class="ss-subcaption">Detailed tree view with application.properties and student packages.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 2.3</span><span class="ss-counter-badge">[8 / 11]</span></div>
              <div class="ss-img-wrap" data-title="StudentManagementApplication Code">
                <img src="../assets/images/week-9/student_mgmt_step_3.png" alt="StudentManagementApplication Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">StudentManagementApplication</div>
                <div class="ss-subcaption">STS editor showing main Spring Boot application runner class.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 2.4</span><span class="ss-counter-badge">[9 / 11]</span></div>
              <div class="ss-img-wrap" data-title="StudentController Code">
                <img src="../assets/images/week-9/student_mgmt_step_4.png" alt="StudentController Code" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">StudentController Endpoint</div>
                <div class="ss-subcaption">STS editor showing @GetMapping("/students") controller method.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_4.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 2.5</span><span class="ss-counter-badge">[10 / 11]</span></div>
              <div class="ss-img-wrap" data-title="Browser: Port 8081 Output">
                <img src="../assets/images/week-9/student_mgmt_step_5.png" alt="Browser: Port 8081 Output" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Browser: Port 8081 Endpoint</div>
                <div class="ss-subcaption">Browser response at localhost:8081/students displaying Student Management System.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/student_mgmt_step_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <!-- Act 3 -->
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Activity 3.1</span><span class="ss-counter-badge">[11 / 11]</span></div>
              <div class="ss-img-wrap" data-title="POM.xml Editor View">
                <img src="../assets/images/week-9/pom_xml_step_1.png" alt="POM.xml Editor View" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">POM.xml Configuration</div>
                <div class="ss-subcaption">STS XML editor displaying spring-boot-starter-parent, web starter, and Java 17 properties.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-9/pom_xml_step_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result & Conclusion</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);">
            <p style="font-size:0.92rem;color:var(--text-sub);line-height:1.75;">
              Thus, Maven project lifecycle management, Spring Boot application development, and POM.xml dependency configuration were successfully demonstrated in Spring Tool Suite 4. Both applications compiled with <code>BUILD SUCCESS</code> and verified across web endpoints on ports 8080 and 8081.
            </p>
          </div>
        </section>
    """

    footer = get_page_footer(9)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-9.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_9()

# ==============================================================================
# WEEK 10: Spring Boot JdbcTemplate with In-Memory Database (H2)
# ==============================================================================
def generate_week_10():
    header = get_page_header(
        10,
        "Spring Boot Database Connectivity Using JdbcTemplate with In-Memory Database (H2)",
        "Automated Schema Creation, Batch Data Seeding, RowMapper Lambdas & H2 Web Console",
        ["🌱 Spring Boot 3.2.x", "⚡ Spring JdbcTemplate", "🗄️ In-Memory H2 Engine", "🖥️ H2 Web Console (Port 83)", "📝 RowMapper Lambdas"],
        "Spring Boot & JPA"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 10 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#specs" class="toc-item">2. Specifications</a>
          <a href="#theory" class="toc-item">3. Theory & Architecture</a>
          <a href="#procedure" class="toc-item">4. Implementation Procedure</a>
          <a href="#code" class="toc-item">5. Source Code Implementation</a>
          <a href="#screenshots" class="toc-item">6. Screenshot Gallery (5)</a>
          <a href="#matrix" class="toc-item">7. Test Case Matrix</a>
          <a href="#result" class="toc-item">8. Result</a>
          <a href="#note" class="toc-item">9. Observation Note</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim of the Experiment</h2>
          <p>
            To design, develop, and validate a database-driven Spring Boot application utilizing Spring <code>JdbcTemplate</code> to connect to an embedded in-memory H2 database, automatically create tables, perform batch data insertions, execute SQL queries using <code>RowMapper</code> lambdas, and verify live database state via the H2 Web Console.
          </p>
        </section>

        <section class="content-section" id="specs">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software and Hardware Specifications</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware & OS</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Operating System: Microsoft Windows 11 Enterprise (64-bit) / Linux</div>
                <div class="req-item"><span class="req-item-dot"></span>Java Platform: OpenJDK 21.0.11 LTS 64-Bit Server VM</div>
                <div class="req-item"><span class="req-item-dot"></span>Client: Google Chrome (H2 Web Console browser client)</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Software Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4 (STS 4.41.0)</div>
                <div class="req-item"><span class="req-item-dot"></span>Framework: Spring Boot 3.2.x (Data JDBC, Web)</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: H2 Database Engine 2.2.x (In-Memory mode: <code>jdbc:h2:mem:testdb</code>)</div>
                <div class="req-item"><span class="req-item-dot"></span>Application Port: <code>83</code></div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="theory">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 3. Theoretical Foundation & JdbcTemplate Architecture</h2>
          <p>
            Traditional Java Database Connectivity (JDBC) requires extensive boilerplate code: opening physical connections, creating prepared statements, iterating result sets, managing checked exceptions, and closing resources in finally blocks. Spring Framework's <code>JdbcTemplate</code> eliminates this overhead by handling resource creation, transaction management, and automatic exception translation from vendor-specific SQLExceptions to Spring's portable <code>DataAccessException</code> hierarchy.
          </p>
          <p>
            The <strong>H2 Database Engine</strong> is a lightweight, pure-Java open-source relational database supporting both in-memory and disk-based operational modes. In-memory mode (<code>jdbc:h2:mem</code>) creates tables directly in the JVM's heap memory, providing ultra-fast execution speeds ideal for rapid prototyping and testing.
          </p>
          <p>
            The <code>@PostConstruct</code> annotation marks a lifecycle method automatically invoked after Spring completes dependency injection. This provides the optimal hook for executing database DDL scripts (<code>CREATE TABLE</code>) and seeding initial relational records prior to handling external user requests.
          </p>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Implementation Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌱</div><div class="timeline-title">Scaffold Project in STS</div></div>
                <div class="timeline-desc">Generate new Spring Boot project in STS incorporating Spring Web, Spring Data JDBC, and H2 Database dependencies.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Configure application.properties</div></div>
                <div class="timeline-desc">Configure custom port 83 (<code>server.port=83</code>), in-memory datasource URL (<code>jdbc:h2:mem:testdb</code>), default <code>sa</code> credentials, and enable H2 Console (<code>spring.h2.console.enabled=true</code>).</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Create Author POJO Model</div></div>
                <div class="timeline-desc">Create <code>Author.java</code> encapsulating <code>firstName</code> and <code>lastName</code> attributes with standard getters, setters, and constructors.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚡</div><div class="timeline-title">Develop AuthorService with Lifecycle Hook</div></div>
                <div class="timeline-desc">Develop <code>AuthorService.java</code> annotated with <code>@Service</code> and autowire Spring's <code>JdbcTemplate</code>. Define <code>@PostConstruct postConstruct()</code> method to DROP/CREATE table, insert records, and query via RowMapper lambda.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🖥️</div><div class="timeline-title">Run & Verify via H2 Console</div></div>
                <div class="timeline-desc">Run application and navigate to <code>http://localhost:83/h2-console</code> in Chrome. Execute <code>SELECT * FROM AUTHOR;</code> and inspect persisted rows.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="code">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 5. Source Code Implementation</h2>
          
          <div class="code-editor" style="margin-bottom:24px;">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">application.properties</span>
            </div>
            <div class="code-editor-body">
              <pre><code>server.port=83
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect</code></pre>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">AuthorService.java</span>
              <div class="editor-actions"><button class="copy-btn">📋 Copy</button><button class="dl-java-btn" data-filename="AuthorService.java">⬇ Download .java</button></div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.demo</span>;

<span class="kw">import</span> <span class="pk">java.util.Arrays</span>;
<span class="kw">import</span> <span class="pk">java.util.List</span>;
<span class="kw">import</span> <span class="pk">org.slf4j.Logger</span>;
<span class="kw">import</span> <span class="pk">org.slf4j.LoggerFactory</span>;
<span class="kw">import</span> <span class="pk">org.springframework.beans.factory.annotation.Autowired</span>;
<span class="kw">import</span> <span class="pk">org.springframework.jdbc.core.JdbcTemplate</span>;
<span class="kw">import</span> <span class="pk">org.springframework.stereotype.Service</span>;
<span class="kw">import</span> <span class="pk">jakarta.annotation.PostConstruct</span>;

<span class="kw">@Service</span>
<span class="kw">public class</span> <span class="ty">AuthorService</span> {
    <span class="kw">private static final</span> <span class="ty">Logger</span> log = <span class="ty">LoggerFactory</span>.<span class="fn">getLogger</span>(<span class="ty">AuthorService</span>.<span class="kw">class</span>);

    <span class="kw">@Autowired</span>
    <span class="kw">private</span> <span class="ty">JdbcTemplate</span> jdbcTemplate;

    <span class="kw">@PostConstruct</span>
    <span class="kw">public void</span> <span class="fn">postConstruct</span>() {
        <span class="ty">Author</span> author1 = <span class="kw">new</span> <span class="ty">Author</span>(<span class="str">"ramesh"</span>, <span class="str">"it"</span>);
        <span class="ty">Author</span> author2 = <span class="kw">new</span> <span class="ty">Author</span>(<span class="str">"harshith"</span>, <span class="str">"it"</span>);
        <span class="ty">List</span>&lt;<span class="ty">Author</span>&gt; authors = <span class="ty">Arrays</span>.<span class="fn">asList</span>(author1, author2);

        log.<span class="fn">info</span>(<span class="str">"Creating tables"</span>);
        jdbcTemplate.<span class="fn">execute</span>(<span class="str">"DROP TABLE author IF EXISTS"</span>);
        jdbcTemplate.<span class="fn">execute</span>(<span class="str">"CREATE TABLE author(first_name varchar(255), last_name varchar(255))"</span>);

        authors.<span class="fn">forEach</span>(i -&gt; jdbcTemplate.<span class="fn">update</span>(
            <span class="str">"INSERT INTO author(first_name, last_name) VALUES (?,?)"</span>,
            i.<span class="fn">getFirstName</span>(), i.<span class="fn">getLastName</span>()
        ));
        log.<span class="fn">info</span>(<span class="str">"Records Saved"</span>);

        log.<span class="fn">info</span>(<span class="str">"Retrieving records"</span>);
        authors = jdbcTemplate.<span class="fn">query</span>(
            <span class="str">"SELECT * FROM author"</span>,
            (rs, rowNum) -&gt; <span class="kw">new</span> <span class="ty">Author</span>(rs.<span class="fn">getString</span>(<span class="str">"first_name"</span>), rs.<span class="fn">getString</span>(<span class="str">"last_name"</span>))
        );
        authors.<span class="fn">forEach</span>(i -&gt; log.<span class="fn">info</span>(i.<span class="fn">getFirstName</span>() + <span class="str">" "</span> + i.<span class="fn">getLastName</span>()));
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- SCREENSHOT GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 6. Realistic Screenshots of Code & Execution (All 5 Figures)
            </h2>
            <span class="badge badge-purple">5 Authentic PDF Screenshots</span>
          </div>
          <p>Extracted directly from original laboratory record document (Week_10.pdf):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.1</span><span class="ss-counter-badge">[1 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.1: Author.java POJO Domain Model">
                <img src="../assets/images/week-10/week-10_img_1.jpg" alt="Figure 10.1 Author.java POJO domain model" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 10.1: Author.java POJO</div>
                <div class="ss-subcaption">STS editor showing Author.java POJO domain model encapsulating fields and getters/setters.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.2</span><span class="ss-counter-badge">[2 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.2: AuthorService.java with JdbcTemplate">
                <img src="../assets/images/week-10/week-10_img_2.jpg" alt="Figure 10.2 AuthorService.java" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 10.2: AuthorService.java</div>
                <div class="ss-subcaption">STS editor showing AuthorService.java with JdbcTemplate lifecycle operations and @PostConstruct.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_2.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.3</span><span class="ss-counter-badge">[3 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.3: STS Console displaying SLF4J logs">
                <img src="../assets/images/week-10/week-10_img_3.png" alt="Figure 10.3 STS Console logs" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 10.3: Console SLF4J Logs</div>
                <div class="ss-subcaption">STS Console displaying SLF4J logs showing table creation, data insertion, and retrieved records.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.4</span><span class="ss-counter-badge">[4 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.4: H2 Web Console Login Page">
                <img src="../assets/images/week-10/week-10_img_4.jpg" alt="Figure 10.4 H2 Console Login Page" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 10.4: H2 Console Login</div>
                <div class="ss-subcaption">Web browser displaying H2 Web Console login page at http://localhost:83/h2-console.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 10.5</span><span class="ss-counter-badge">[5 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 10.5: H2 Console Table Verification">
                <img src="../assets/images/week-10/week-10_img_5.jpg" alt="Figure 10.5 H2 Console Table Verification" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 10.5: H2 Console Query</div>
                <div class="ss-subcaption">H2 Console executing 'SELECT * FROM AUTHOR;' and displaying table records ramesh and harshith.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-10/week-10_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <!-- TEST MATRIX -->
        <section class="content-section" id="matrix">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 7. Test Cases and Observation Matrix</h2>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Test Case</th><th>Operation / Component</th><th>Expected Output</th><th>Actual Output</th><th>Status</th></tr></thead>
              <tbody>
                <tr><td>TC-01</td><td>Schema Initialization</td><td>Table 'author' created via jdbcTemplate.execute()</td><td>Log: 'Creating tables' executed cleanly</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-02</td><td>Batch Insert</td><td>2 records inserted via jdbcTemplate.update()</td><td>Log: 'Records Saved' confirmed</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-03</td><td>Data Retrieval & Mapping</td><td>Query mapped via RowMapper lambda to Author POJOs</td><td>Console logged: 'ramesh it', 'harshith it'</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-04</td><td>H2 Console Authentication</td><td>Login to jdbc:h2:mem:testdb with user 'sa'</td><td>Connected to H2 schema workspace successfully</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-05</td><td>Interactive SQL Query</td><td>SELECT * FROM AUTHOR returns 2 rows</td><td>Visual grid displays ramesh and harshith</td><td><span class="badge badge-green">PASS</span></td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Result</h2>
          <p>
            Thus, database connectivity using Spring Boot JdbcTemplate with an in-memory H2 database was successfully implemented. Schema creation, record persistence, parameterized queries, and RowMapper object hydration were verified via SLF4J console telemetry and the interactive H2 Web Console.
          </p>
        </section>

        <section class="content-section" id="note">
          <h2 class="content-section-title"><span class="section-icon">📋</span> 9. Laboratory Observation Note</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);line-height:1.75;">
            <p><strong>Note Type:</strong> Laboratory Observation &amp; Execution Verification</p>
            <p><strong>Student:</strong> Venkata Sai Karthikeya Kaja (Roll No: 24EU08161)</p>
            <p><strong>Date:</strong> 31-03-2026</p>
            <p><strong>Observation Summary:</strong> Execution verified. Server started on port 83. Schema initialized in <code>jdbc:h2:mem:testdb</code>. Console logs confirmed records 'ramesh it' and 'harshith it'. H2 Web Console verified table contents. All test cases passed.</p>
          </div>
        </section>
    """

    footer = get_page_footer(10)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-10.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_10()

# ==============================================================================
# WEEK 11: Spring Boot JPA Application with Relational Database (MySQL)
# ==============================================================================
def generate_week_11():
    header = get_page_header(
        11,
        "Spring Boot JPA Application with Relational Database (MySQL) and Web Interface",
        "Object-Relational Mapping (ORM), Hibernate, RESTful JSON Endpoints & Thymeleaf Views",
        ["🐬 MySQL 8.0 Server (Port 3306)", "🍃 Spring Data JPA & Hibernate", "🚀 Dual Controllers (REST & View)", "🎨 Server-Side Thymeleaf", "📋 Employee Entity ORM"],
        "Spring Boot & JPA"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 11 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#specs" class="toc-item">2. Specifications</a>
          <a href="#theory" class="toc-item">3. Theory & Architecture</a>
          <a href="#procedure" class="toc-item">4. Procedure</a>
          <a href="#code" class="toc-item">5. Source Code & Schema</a>
          <a href="#screenshots" class="toc-item">6. Screenshot Gallery (5)</a>
          <a href="#matrix" class="toc-item">7. Test Case Matrix</a>
          <a href="#result" class="toc-item">8. Result</a>
          <a href="#note" class="toc-item">9. Observation Note</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim of the Experiment</h2>
          <p>
            To design, develop, and deploy an enterprise Spring Boot application connecting to an external MySQL relational database using Spring Data JPA and Hibernate, implement Object-Relational Mapping (ORM) for an Employee entity, and provide dual client interfaces: a RESTful JSON API and a server-side rendered Thymeleaf HTML web page.
          </p>
        </section>

        <section class="content-section" id="specs">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software and Hardware Specifications</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware & Platform</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>OS: Microsoft Windows 11 Enterprise (64-bit) / Linux</div>
                <div class="req-item"><span class="req-item-dot"></span>Java Platform: JDK 21.0.11 LTS</div>
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4 (STS 4.41.0)</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Database & Frameworks</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Database: MySQL Community Server 8.0.36 &amp; Workbench 8.0 CE</div>
                <div class="req-item"><span class="req-item-dot"></span>Connector: MySQL Connector/J 8.0.33 (Type-4 Driver)</div>
                <div class="req-item"><span class="req-item-dot"></span>Frameworks: Spring Data JPA, Hibernate ORM, Spring Web MVC, Thymeleaf</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="theory">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 3. Theoretical Foundation & Architectural Overview</h2>
          <p>
            <strong>Object-Relational Mapping (ORM)</strong> bridges the conceptual mismatch between the object-oriented paradigm of Java and the relational paradigm of SQL databases. The Java Persistence API (JPA) defines standard interfaces for entity mapping, while Hibernate serves as the core persistence provider implementing SQL query translation, first-level caching, dirty checking, and automatic schema synchronization.
          </p>
          <p>
            <strong>Spring Data JPA</strong> simplifies data layer development by providing repository abstractions. By creating an interface extending <code>JpaRepository&lt;Employee, Integer&gt;</code>, developers inherit robust implementations of standard CRUD operations (<code>save</code>, <code>findById</code>, <code>findAll</code>, <code>delete</code>) without writing tedious SQL queries or DAO classes.
          </p>
          <p>
            To serve both programmatic API consumers and human users, this project employs a <strong>dual-controller architecture</strong>: <code>EmployeeRestController</code> (<code>@RestController</code>) serializes entity domain objects directly into standardized JSON payloads at <code>/api/employees</code>, while <code>EmployeeViewController</code> (<code>@Controller</code>) binds repository data to the Spring UI Model and renders a dynamic Thymeleaf HTML template at <code>/employees</code>.
          </p>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Implementation Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🗄️</div><div class="timeline-title">Initialize MySQL Database & Table</div></div>
                <div class="timeline-desc">Open MySQL Workbench on port 3306, create database <code>testdb</code> and table <code>employee</code>, inserting baseline rows: ('Ramesh', 'IT'), ('Suresh', 'CSE'), and ('Mahesh', 'ECE').</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌱</div><div class="timeline-title">Scaffold Spring Boot Project in STS</div></div>
                <div class="timeline-desc">Select dependencies: Spring Data JPA, Spring Web, Thymeleaf, and MySQL Driver. Configure <code>application.properties</code> with MySQL credentials, dialect, and <code>ddl-auto=update</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Define Entity & Repository</div></div>
                <div class="timeline-desc">Create <code>Employee.java</code> with <code>@Entity</code>, <code>@Id</code>, <code>@GeneratedValue(strategy = GenerationType.IDENTITY)</code>. Define <code>EmployeeRepository.java</code> extending <code>JpaRepository&lt;Employee, Integer&gt;</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Implement Dual Controllers</div></div>
                <div class="timeline-desc">Implement <code>EmployeeRestController</code> mapping <code>GET /api/employees</code> (JSON) and <code>EmployeeViewController</code> mapping <code>GET /employees</code> (Thymeleaf model).</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🎨</div><div class="timeline-title">Create Thymeleaf Template & Verify</div></div>
                <div class="timeline-desc">Create <code>employees.html</code> with <code>th:each="e : ${employees}"</code>. Launch application and verify REST JSON and HTML table outputs in Chrome.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="code">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 5. Database Schema & Source Code</h2>
          
          <div class="code-editor" style="margin-bottom:24px;">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">schema.sql (MySQL)</span>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">CREATE DATABASE IF NOT EXISTS</span> testdb;
<span class="kw">USE</span> testdb;

<span class="kw">CREATE TABLE IF NOT EXISTS</span> employee (
    id <span class="ty">INT PRIMARY KEY AUTO_INCREMENT</span>,
    name <span class="ty">VARCHAR(100) NOT NULL</span>,
    department <span class="ty">VARCHAR(100) NOT NULL</span>
);

<span class="kw">INSERT INTO</span> employee (name, department) <span class="kw">VALUES</span>
(<span class="str">'Ramesh'</span>, <span class="str">'IT'</span>),
(<span class="str">'Suresh'</span>, <span class="str">'CSE'</span>),
(<span class="str">'Mahesh'</span>, <span class="str">'ECE'</span>);</code></pre>
            </div>
          </div>

          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">EmployeeController.java (Dual Controllers)</span>
              <div class="editor-actions"><button class="copy-btn">📋 Copy</button><button class="dl-java-btn" data-filename="EmployeeController.java">⬇ Download .java</button></div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.demo</span>;

<span class="kw">import</span> <span class="pk">java.util.List</span>;
<span class="kw">import</span> <span class="pk">org.springframework.beans.factory.annotation.Autowired</span>;
<span class="kw">import</span> <span class="pk">org.springframework.stereotype.Controller</span>;
<span class="kw">import</span> <span class="pk">org.springframework.ui.Model</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.GetMapping</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.RequestMapping</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.RestController</span>;

<span class="kw">@RestController</span>
<span class="kw">@RequestMapping</span>(<span class="str">"/api"</span>)
<span class="kw">class</span> <span class="ty">EmployeeRestController</span> {
    <span class="kw">@Autowired</span>
    <span class="kw">private</span> <span class="ty">EmployeeRepository</span> repo;

    <span class="kw">@GetMapping</span>(<span class="str">"/employees"</span>)
    <span class="kw">public</span> <span class="ty">List</span>&lt;<span class="ty">Employee</span>&gt; <span class="fn">getAll</span>() {
        <span class="kw">return</span> repo.<span class="fn">findAll</span>();
    }
}

<span class="kw">@Controller</span>
<span class="kw">class</span> <span class="ty">EmployeeViewController</span> {
    <span class="kw">@Autowired</span>
    <span class="kw">private</span> <span class="ty">EmployeeRepository</span> repo;

    <span class="kw">@GetMapping</span>(<span class="str">"/employees"</span>)
    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">employeesPage</span>(<span class="ty">Model</span> model) {
        model.<span class="fn">addAttribute</span>(<span class="str">"employees"</span>, repo.<span class="fn">findAll</span>());
        <span class="kw">return</span> <span class="str">"employees"</span>;
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- SCREENSHOT GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 6. Realistic Screenshots of Code & Execution (All 5 Figures)
            </h2>
            <span class="badge badge-purple">5 Authentic PDF Screenshots</span>
          </div>
          <p>Extracted directly from original laboratory record document (Week_11.pdf):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.1</span><span class="ss-counter-badge">[1 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.1: Employee.java Entity with JPA">
                <img src="../assets/images/week-11/week-11_img_1.png" alt="Figure 11.1 Employee.java Entity" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 11.1: Employee Entity</div>
                <div class="ss-subcaption">STS editor showing Employee.java entity with @Entity, @Id, and @GeneratedValue annotations.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.2</span><span class="ss-counter-badge">[2 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.2: Dual Controllers (REST & View)">
                <img src="../assets/images/week-11/week-11_img_2.png" alt="Figure 11.2 Dual Controllers" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 11.2: Dual Controllers</div>
                <div class="ss-subcaption">STS editor showing EmployeeRestController (JSON) and EmployeeViewController (Thymeleaf).</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.3</span><span class="ss-counter-badge">[3 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.3: MySQL Workbench Table Records">
                <img src="../assets/images/week-11/week-11_img_3.png" alt="Figure 11.3 MySQL Workbench" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 11.3: MySQL Workbench</div>
                <div class="ss-subcaption">MySQL Workbench displaying testdb.employee records (Ramesh, Suresh, Mahesh).</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_3.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.4</span><span class="ss-counter-badge">[4 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.4: REST API JSON Response">
                <img src="../assets/images/week-11/week-11_img_4.jpg" alt="Figure 11.4 REST API JSON Response" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 11.4: REST API JSON</div>
                <div class="ss-subcaption">Chrome browser displaying JSON payload at http://localhost:8080/api/employees.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 11.5</span><span class="ss-counter-badge">[5 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 11.5: Thymeleaf HTML Table View">
                <img src="../assets/images/week-11/week-11_img_5.jpg" alt="Figure 11.5 Thymeleaf HTML Table View" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 11.5: Thymeleaf Web View</div>
                <div class="ss-subcaption">Chrome browser displaying styled HTML employee table at http://localhost:8080/employees.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-11/week-11_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <!-- TEST MATRIX -->
        <section class="content-section" id="matrix">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 7. Test Cases and Observation Matrix</h2>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Test Case</th><th>Endpoint / Action</th><th>Expected Result</th><th>Actual Result</th><th>Status</th></tr></thead>
              <tbody>
                <tr><td>TC-01</td><td>Database Connectivity</td><td>Connect to MySQL 3306 testdb</td><td>Connection established; dialect MySQL8Dialect active</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-02</td><td>GET /api/employees</td><td>Return JSON array of employee records</td><td>HTTP 200 OK; JSON payload with 3 records returned</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-03</td><td>GET /employees</td><td>Render HTML page with employee table</td><td>Thymeleaf rendered styled HTML table in browser</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-04</td><td>Hibernate SQL logging</td><td>Output generated SELECT queries to console</td><td>Console showed: 'Hibernate: select e1_0.id... from employee'</td><td><span class="badge badge-green">PASS</span></td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Result</h2>
          <p>
            Thus, an enterprise Spring Boot application connecting to an external MySQL relational database via Spring Data JPA and Hibernate was successfully architected, developed, and validated. Dual interfaces—RESTful JSON endpoint and server-side Thymeleaf web view—were verified with complete relational integrity.
          </p>
        </section>

        <section class="content-section" id="note">
          <h2 class="content-section-title"><span class="section-icon">📋</span> 9. Laboratory Observation Note</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);line-height:1.75;">
            <p><strong>Note Type:</strong> Laboratory Observation &amp; Execution Verification</p>
            <p><strong>Student:</strong> Venkata Sai Karthikeya Kaja (Roll No: 24EU08161)</p>
            <p><strong>Date:</strong> 07-04-2026</p>
            <p><strong>Observation Summary:</strong> Execution verified. MySQL connection successful. REST API returned JSON list of employees with HTTP 200. Thymeleaf rendered styled employee table. Hibernate SQL telemetry verified. All test cases passed.</p>
          </div>
        </section>
    """

    footer = get_page_footer(11)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-11.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_11()

# ==============================================================================
# WEEK 12: Spring Data JPA Repository Operations with In-Memory H2 Database
# ==============================================================================
def generate_week_12():
    header = get_page_header(
        12,
        "Spring Data JPA Repository Operations with In-Memory H2 Database",
        "Zero-Boilerplate ORM Persistence, Browser-Based HTTP GET Endpoints & H2 Web Console",
        ["🗄️ In-Memory H2 Engine", "🍃 JpaRepository<Student, Long>", "🌐 Browser GET Endpoints", "🖥️ H2 Web Console Verification", "📦 Zero-Boilerplate ORM"],
        "Spring Boot & JPA"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 12 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#specs" class="toc-item">2. Specifications</a>
          <a href="#theory" class="toc-item">3. Theory</a>
          <a href="#procedure" class="toc-item">4. Procedure</a>
          <a href="#code" class="toc-item">5. Source Code</a>
          <a href="#screenshots" class="toc-item">6. Screenshot Gallery (5)</a>
          <a href="#matrix" class="toc-item">7. Test Case Matrix</a>
          <a href="#result" class="toc-item">8. Result</a>
          <a href="#note" class="toc-item">9. Observation Note</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim of the Experiment</h2>
          <p>
            To implement, configure, and evaluate Spring Data JPA repository operations on a Student entity using an in-memory H2 database, establish browser-accessible HTTP GET endpoints to perform record insertion and retrieval without external testing utilities, and verify database state via the H2 Console.
          </p>
        </section>

        <section class="content-section" id="specs">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software and Hardware Specifications</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware & Platform</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Operating System: Microsoft Windows 11 Enterprise (64-bit) / Linux</div>
                <div class="req-item"><span class="req-item-dot"></span>Java Platform: OpenJDK 21.0.11 LTS 64-Bit Server VM</div>
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4 (STS 4.41.0)</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Software Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Framework: Spring Boot 3.2.x (Spring Web, Spring Data JPA, H2 Database)</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: H2 Database Engine (In-Memory mode: <code>jdbc:h2:mem:testdb</code>)</div>
                <div class="req-item"><span class="req-item-dot"></span>Client: Google Chrome (Browser client for direct GET queries)</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="theory">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 3. Theoretical Foundation</h2>
          <p>
            Spring Data JPA represents a powerful abstraction over the Java Persistence API. Rather than requiring developers to manually write boilerplate Data Access Object (DAO) classes, EntityManager logic, and transaction management, Spring Data JPA introduces dynamic repository proxy generation. By declaring an interface extending <code>JpaRepository&lt;Student, Long&gt;</code>, Spring Data creates a runtime proxy executing standard persistence operations (<code>save</code>, <code>findAll</code>, <code>findById</code>, <code>count</code>, <code>delete</code>).
          </p>
          <p>
            In typical REST applications, state-modifying operations (such as creating records) utilize HTTP POST requests containing JSON bodies, often requiring dedicated API tools like Postman or curl. For lightweight development and immediate classroom verification, controller methods can map HTTP GET requests with URL query parameters (<code>@RequestParam</code>). This enables instant browser-based interaction, such that navigating to <code>/add?name=Anand&city=Vijayawada</code> triggers entity instantiation, repository persistence, and database commit.
          </p>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 4. Step-by-Step Implementation Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌱</div><div class="timeline-title">Create Spring Boot Project</div></div>
                <div class="timeline-desc">Create new Spring Boot app in STS selecting Spring Web, Spring Data JPA, and H2 Database starters.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">⚙️</div><div class="timeline-title">Configure application.properties</div></div>
                <div class="timeline-desc">Configure datasource parameters: <code>spring.datasource.url=jdbc:h2:mem:testdb</code>, <code>driverClassName=org.h2.Driver</code>, <code>username=sa</code>, H2Dialect, and <code>spring.h2.console.enabled=true</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Create Entity Student.java</div></div>
                <div class="timeline-desc">Create entity class <code>Student.java</code> annotated with <code>@Entity</code>, configuring 'id' as <code>@Id</code> with <code>@GeneratedValue(strategy = GenerationType.IDENTITY)</code> along with 'name' and 'city'.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🍃</div><div class="timeline-title">Define StudentRepository.java</div></div>
                <div class="timeline-desc">Define <code>StudentRepository.java</code> as an interface extending <code>JpaRepository&lt;Student, Long&gt;</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Develop StudentController with GET Endpoints</div></div>
                <div class="timeline-desc">Develop <code>StudentController.java</code> annotated with <code>@RestController</code>: <code>GET /</code> (health check), <code>GET /add?name=...&city=...</code> (save entity), and <code>GET /students</code> (findAll JSON list).</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">6</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🚀</div><div class="timeline-title">Browser Verification & H2 Console</div></div>
                <div class="timeline-desc">Visit <code>http://localhost:8080/</code>, execute <code>/add</code> to persist students, <code>/students</code> to view JSON, and <code>/h2-console</code> to inspect relational table.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="code">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 5. Source Code Implementation</h2>
          
          <div class="code-editor" style="margin-bottom:24px;">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">StudentController.java</span>
              <div class="editor-actions"><button class="copy-btn">📋 Copy</button><button class="dl-java-btn" data-filename="Week12_StudentController.java">⬇ Download .java</button></div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.demo</span>;

<span class="kw">import</span> <span class="pk">java.util.List</span>;
<span class="kw">import</span> <span class="pk">org.springframework.beans.factory.annotation.Autowired</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.GetMapping</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.RequestParam</span>;
<span class="kw">import</span> <span class="pk">org.springframework.web.bind.annotation.RestController</span>;

<span class="kw">@RestController</span>
<span class="kw">public class</span> <span class="ty">StudentController</span> {

    <span class="kw">@Autowired</span>
    <span class="kw">private</span> <span class="ty">StudentRepository</span> repo;

    <span class="kw">@GetMapping</span>(<span class="str">"/"</span>)
    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">home</span>() {
        <span class="kw">return</span> <span class="str">"Spring Boot + H2 + JPA Example Running!"</span>;
    }

    <span class="co">// Add new student using browser URL query params</span>
    <span class="co">// Example: http://localhost:8080/add?name=Anand&city=Vijayawada</span>
    <span class="kw">@GetMapping</span>(<span class="str">"/add"</span>)
    <span class="kw">public</span> <span class="ty">String</span> <span class="fn">addStudent</span>(<span class="kw">@RequestParam</span> <span class="ty">String</span> name, <span class="kw">@RequestParam</span> <span class="ty">String</span> city) {
        repo.<span class="fn">save</span>(<span class="kw">new</span> <span class="ty">Student</span>(name, city));
        <span class="kw">return</span> <span class="str">"Student Added Successfully!"</span>;
    }

    <span class="co">// View all students using browser URL</span>
    <span class="co">// Example: http://localhost:8080/students</span>
    <span class="kw">@GetMapping</span>(<span class="str">"/students"</span>)
    <span class="kw">public</span> <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">getStudents</span>() {
        <span class="kw">return</span> repo.<span class="fn">findAll</span>();
    }
}</code></pre>
            </div>
          </div>
        </section>

        <!-- SCREENSHOT GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 6. Realistic Screenshots of Code & Execution (All 5 Figures)
            </h2>
            <span class="badge badge-purple">5 Authentic PDF Screenshots</span>
          </div>
          <p>Extracted directly from original laboratory record document (Week_12.pdf):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.1</span><span class="ss-counter-badge">[1 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.1: Student.java and StudentRepository.java">
                <img src="../assets/images/week-12/week-12_img_1.png" alt="Figure 12.1 Student Entity & Repository" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 12.1: Entity & Repository</div>
                <div class="ss-subcaption">STS editor showing Student.java entity and StudentRepository interface extending JpaRepository.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_1.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.2</span><span class="ss-counter-badge">[2 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.2: StudentController.java with Browser Endpoints">
                <img src="../assets/images/week-12/week-12_img_2.png" alt="Figure 12.2 StudentController.java" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 12.2: StudentController</div>
                <div class="ss-subcaption">STS editor showing StudentController.java with browser endpoints (/add, /students).</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_2.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.3</span><span class="ss-counter-badge">[3 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.3: Browser displaying /add confirmation">
                <img src="../assets/images/week-12/week-12_img_3.jpg" alt="Figure 12.3 Browser /add confirmation" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 12.3: Browser /add</div>
                <div class="ss-subcaption">Chrome browser displaying student addition confirmation at /add?name=Anand&city=Vijayawada.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_3.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.4</span><span class="ss-counter-badge">[4 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.4: Browser displaying JSON list at /students">
                <img src="../assets/images/week-12/week-12_img_4.jpg" alt="Figure 12.4 Browser JSON list" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 12.4: Browser /students</div>
                <div class="ss-subcaption">Chrome browser displaying JSON list of students retrieved from in-memory H2 database.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 12.5</span><span class="ss-counter-badge">[5 / 5]</span></div>
              <div class="ss-img-wrap" data-title="Figure 12.5: H2 Console showing table STUDENT">
                <img src="../assets/images/week-12/week-12_img_5.jpg" alt="Figure 12.5 H2 Console Table STUDENT" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 12.5: H2 Console Table</div>
                <div class="ss-subcaption">H2 Console showing table STUDENT populated with persisted records (Anand, Karthikeyan).</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-12/week-12_img_5.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <!-- TEST MATRIX -->
        <section class="content-section" id="matrix">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 7. Test Cases and Observation Matrix</h2>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Test Case</th><th>Input Action / URL</th><th>Expected Output</th><th>Actual Output</th><th>Status</th></tr></thead>
              <tbody>
                <tr><td>TC-01</td><td>GET http://localhost:8080/</td><td>'Spring Boot + H2 + JPA Example Running!'</td><td>Status message returned successfully</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-02</td><td>GET /add?name=Anand&city=Vijayawada</td><td>'Student Added Successfully!'</td><td>Entity persisted with generated ID 1</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-03</td><td>GET /add?name=Karthikeyan&city=Coimbatore</td><td>'Student Added Successfully!'</td><td>Entity persisted with generated ID 2</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-04</td><td>GET http://localhost:8080/students</td><td>JSON array containing all added students</td><td>JSON returned: Anand (1), Karthikeyan (2)</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>TC-05</td><td>H2 Console: SELECT * FROM STUDENT</td><td>Relational rows for Anand and Karthikeyan</td><td>Visual grid displays table records accurately</td><td><span class="badge badge-green">PASS</span></td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 8. Result</h2>
          <p>
            Thus, Spring Data JPA repository operations on an in-memory H2 database were successfully implemented. Browser-based CRUD operations without external tools were validated, confirming seamless entity mapping, repository proxy execution, and live database persistence.
          </p>
        </section>

        <section class="content-section" id="note">
          <h2 class="content-section-title"><span class="section-icon">📋</span> 9. Laboratory Observation Note</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);line-height:1.75;">
            <p><strong>Note Type:</strong> Laboratory Observation &amp; Execution Verification</p>
            <p><strong>Student:</strong> Venkata Sai Karthikeya Kaja (Roll No: 24EU08161)</p>
            <p><strong>Date:</strong> 14-04-2026</p>
            <p><strong>Observation Summary:</strong> Execution verified. Application started on port 8080. GET /add persisted students Anand and Karthikeyan. GET /students returned JSON array with HTTP 200. H2 Console confirmed rows in STUDENT table. All test cases passed.</p>
          </div>
        </section>
    """

    footer = get_page_footer(12)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-12.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_12()

# ==============================================================================
# WEEK 13: Implementation of Derived and Custom Query Methods in Spring Data JPA
# ==============================================================================
def generate_week_13():
    header = get_page_header(
        13,
        "Implementation of Derived and Custom Query Methods in Spring Data JPA",
        "AST Query Derivation, Method Naming Grammar, Predicate Conjunctions, and Custom Native @Query",
        ["🔍 8 Query Methods", "🧩 Query Derivation AST", "⚡ Custom @Query (Native SQL)", "📊 Hibernate SQL Telemetry", "🎯 Predicate Conjunctions"],
        "Spring Boot & JPA"
    )

    body = """
    <div class="topic-content-wrap container">
      <aside class="topic-sidebar" aria-label="Table of contents">
        <p class="toc-title">Week 13 Index</p>
        <nav class="toc-list">
          <a href="#aim" class="toc-item">1. Aim</a>
          <a href="#specs" class="toc-item">2. Specifications</a>
          <a href="#theory" class="toc-item">3. Query Derivation Theory</a>
          <a href="#methods" class="toc-item">4. The 8 Query Methods</a>
          <a href="#procedure" class="toc-item">5. Procedure</a>
          <a href="#code" class="toc-item">6. Source Code</a>
          <a href="#screenshots" class="toc-item">7. Screenshot Gallery (7)</a>
          <a href="#matrix" class="toc-item">8. Test Case Matrix</a>
          <a href="#result" class="toc-item">9. Result</a>
          <a href="#note" class="toc-item">10. Observation Note</a>
        </nav>
      </aside>

      <article class="topic-main">
        <section class="content-section" id="aim">
          <h2 class="content-section-title"><span class="section-icon">🎯</span> 1. Aim of the Experiment</h2>
          <p>
            To design, declare, implement, and validate specialized derived query methods and custom queries utilizing the <code>@Query</code> annotation (both JPQL and Native SQL) in Spring Data JPA repository interfaces for a Student entity, and observe runtime SQL generation and result sets.
          </p>
        </section>

        <section class="content-section" id="specs">
          <h2 class="content-section-title"><span class="section-icon">⚙️</span> 2. Software and Hardware Specifications</h2>
          <div class="req-grid">
            <div class="req-card">
              <div class="req-card-title">🖥️ Hardware & Platform</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Operating System: Microsoft Windows 11 Enterprise (64-bit) / Linux</div>
                <div class="req-item"><span class="req-item-dot"></span>Java Platform: OpenJDK 21.0.11 LTS</div>
                <div class="req-item"><span class="req-item-dot"></span>IDE: Spring Tool Suite 4 (STS 4.41.0)</div>
              </div>
            </div>
            <div class="req-card">
              <div class="req-card-title">💾 Software Stack</div>
              <div class="req-list">
                <div class="req-item"><span class="req-item-dot"></span>Framework: Spring Boot 3.2.x, Spring Data JPA, Hibernate 6.x</div>
                <div class="req-item"><span class="req-item-dot"></span>Database: H2 In-Memory Database / MySQL 8.0</div>
                <div class="req-item"><span class="req-item-dot"></span>Browser: Google Chrome (REST query verification client)</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="theory">
          <h2 class="content-section-title"><span class="section-icon">📖</span> 3. Theoretical Foundation & Query Derivation Mechanism</h2>
          <p>
            One of the most revolutionary features of Spring Data JPA is its <strong>query derivation mechanism</strong>. By parsing repository method names according to structured naming conventions, Spring Data automatically builds Abstract Syntax Trees (AST) that are translated into JPQL and native SQL queries at runtime. This eliminates the necessity of writing manual SQL statements for common filtering, logical conjunctions/disjunctions, sorting, and pagination.
          </p>
          <p>
            The method naming grammar consists of:
          </p>
          <ul style="margin-left:20px;line-height:1.8;">
            <li><strong>Subject Prefixes:</strong> <code>findBy</code>, <code>readBy</code>, <code>queryBy</code>, <code>countBy</code>, <code>getBy</code>.</li>
            <li><strong>Predicate Properties:</strong> Matching entity field names (e.g., <code>FirstName</code>, <code>LastName</code>).</li>
            <li><strong>Conjunctions &amp; Operators:</strong> <code>And</code>, <code>Or</code>, <code>Between</code>, <code>LessThan</code>, <code>GreaterThan</code>, <code>Like</code>.</li>
            <li><strong>Ordering Directives:</strong> <code>OrderBy&lt;Property&gt;Asc</code> or <code>OrderBy&lt;Property&gt;Desc</code>.</li>
            <li><strong>Limiting Directives:</strong> <code>findFirst&lt;N&gt;By</code> or <code>findTop&lt;N&gt;By</code>.</li>
          </ul>
          <p>
            When requirements exceed the capabilities of derived method naming (such as complex joins, subqueries, or database-specific functions), the <code>@Query</code> annotation allows developers to provide explicit JPQL queries or raw native SQL queries (via <code>nativeQuery = true</code>), binding parameters through positional placeholders (<code>?1</code>) or named parameters (<code>:param</code>).
          </p>
        </section>

        <!-- THE 8 QUERY METHODS -->
        <section class="content-section" id="methods">
          <h2 class="content-section-title"><span class="section-icon">🔍</span> 4. The 8 Prescribed Query Methods</h2>
          <div class="table-wrap">
            <table>
              <thead><tr><th>#</th><th>Method Signature</th><th>Technical Purpose</th><th>Generated SQL Predicate</th></tr></thead>
              <tbody>
                <tr><td>1</td><td><code>findAll()</code></td><td>Retrieve all records without filtering.</td><td><code>SELECT * FROM student</code></td></tr>
                <tr><td>2</td><td><code>findByName(String name)</code></td><td>Exact match by entity name property.</td><td><code>WHERE name = ?</code></td></tr>
                <tr><td>3</td><td><code>findByFirstName(String firstName)</code></td><td>Exact match by firstName attribute.</td><td><code>WHERE first_name = ?</code></td></tr>
                <tr><td>4</td><td><code>findByFirstNameAndLastName(String fn, String ln)</code></td><td>Conjunction (AND) matching both criteria.</td><td><code>WHERE first_name = ? AND last_name = ?</code></td></tr>
                <tr><td>5</td><td><code>findByFirstNameOrLastName(String fn, String ln)</code></td><td>Disjunction (OR) matching either criterion.</td><td><code>WHERE first_name = ? OR last_name = ?</code></td></tr>
                <tr><td>6</td><td><code>findByLastNameOrderByFirstNameAsc(String ln)</code></td><td>Matching lastName, sorted ascending by firstName.</td><td><code>WHERE last_name = ? ORDER BY first_name ASC</code></td></tr>
                <tr><td>7</td><td><code>findFirst10ByLastName(String ln)</code></td><td>Top 10 matching results by lastName.</td><td><code>FETCH FIRST 10 ROWS ONLY</code></td></tr>
                <tr><td>8</td><td><code>@Query(nativeQuery=true) fetchByFirstName(String fn)</code></td><td>Direct native SQL query execution bypassing JPQL.</td><td><code>SELECT * FROM student WHERE first_name = ?</code></td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="procedure">
          <h2 class="content-section-title"><span class="section-icon">🔧</span> 5. Step-by-Step Implementation Procedure</h2>
          <div class="timeline-procedure">
            <div class="timeline-step">
              <div class="timeline-marker">1</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">☕</div><div class="timeline-title">Define Student Query Entity</div></div>
                <div class="timeline-desc">Define <code>Student.java</code> with fields <code>id</code>, <code>name</code>, <code>firstName</code>, <code>lastName</code>, <code>city</code>, and <code>course</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">2</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🍃</div><div class="timeline-title">Declare Methods in StudentRepository</div></div>
                <div class="timeline-desc">Declare all 8 required derived and custom query methods inside <code>StudentRepository.java</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">3</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌱</div><div class="timeline-title">Seed Test Records via CommandLineRunner</div></div>
                <div class="timeline-desc">Implement <code>DataLoader.java</code> to seed diverse student records with shared last names and unique first names upon application startup.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">4</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">🌐</div><div class="timeline-title">Expose Query Controller Endpoints</div></div>
                <div class="timeline-desc">Develop <code>StudentQueryController.java</code> mapping GET endpoints: <code>/by-name</code>, <code>/by-firstname</code>, <code>/by-first-last</code>, <code>/by-first-or-last</code>, <code>/order-asc</code>, <code>/first10</code>, and <code>/native-query</code>.</div>
              </div>
            </div>
            <div class="timeline-step">
              <div class="timeline-marker">5</div>
              <div class="timeline-card">
                <div class="timeline-header"><div class="timeline-icon">📊</div><div class="timeline-title">Inspect Hibernate SQL Telemetry</div></div>
                <div class="timeline-desc">Enable <code>spring.jpa.show-sql=true</code> in <code>application.properties</code> and observe console output verifying AST query translations.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="content-section" id="code">
          <h2 class="content-section-title"><span class="section-icon">💻</span> 6. Source Code Implementation</h2>
          <div class="code-editor">
            <div class="code-editor-header">
              <div class="editor-dots"><span class="editor-dot red"></span><span class="editor-dot yellow"></span><span class="editor-dot green"></span></div>
              <span class="editor-filename">StudentRepository.java</span>
              <div class="editor-actions"><button class="copy-btn">📋 Copy</button><button class="dl-java-btn" data-filename="Week13_StudentRepository.java">⬇ Download .java</button></div>
            </div>
            <div class="code-editor-body">
              <pre><code><span class="kw">package</span> <span class="pk">com.example.demo</span>;

<span class="kw">import</span> <span class="pk">java.util.List</span>;
<span class="kw">import</span> <span class="pk">org.springframework.data.jpa.repository.JpaRepository</span>;
<span class="kw">import</span> <span class="pk">org.springframework.data.jpa.repository.Query</span>;
<span class="kw">import</span> <span class="pk">org.springframework.stereotype.Repository</span>;

<span class="kw">@Repository</span>
<span class="kw">public interface</span> <span class="ty">StudentRepository</span> <span class="kw">extends</span> <span class="ty">JpaRepository</span>&lt;<span class="ty">Student</span>, <span class="ty">Long</span>&gt; {
    <span class="co">// 1. Retrieve all records without filtering</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findAll</span>();

    <span class="co">// 2. Exact match by name</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByName</span>(<span class="ty">String</span> name);

    <span class="co">// 3. Match by firstName</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByFirstName</span>(<span class="ty">String</span> firstName);

    <span class="co">// 4. Conjunction: firstName AND lastName</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByFirstNameAndLastName</span>(<span class="ty">String</span> firstName, <span class="ty">String</span> lastName);

    <span class="co">// 5. Disjunction: firstName OR lastName</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByFirstNameOrLastName</span>(<span class="ty">String</span> firstName, <span class="ty">String</span> lastName);

    <span class="co">// 6. Matching lastName, sorted ascending by firstName</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findByLastNameOrderByFirstNameAsc</span>(<span class="ty">String</span> lastName);

    <span class="co">// 7. Top 10 matching results by lastName</span>
    <span class="ty">List</span>&lt;<span class="ty">Student</span>&gt; <span class="fn">findFirst10ByLastName</span>(<span class="ty">String</span> lastName);

    <span class="co">// 8. Custom native SQL query via @Query</span>
    <span class="kw">@Query</span>(value = <span class="str">"SELECT * FROM student WHERE first_name = ?1"</span>, nativeQuery = <span class="kw">true</span>)
    <span class="ty">Student</span> <span class="fn">fetchByFirstName</span>(<span class="ty">String</span> firstName);
}</code></pre>
            </div>
          </div>
        </section>

        <!-- SCREENSHOT GALLERY -->
        <section class="content-section" id="screenshots">
          <div class="gallery-section-header">
            <h2 class="content-section-title mb-0" style="border-bottom:none;padding-bottom:0">
              <span class="section-icon">🖼️</span> 7. Realistic Screenshots of Code & Execution (All 7 Figures)
            </h2>
            <span class="badge badge-purple">7 Authentic PDF Screenshots</span>
          </div>
          <p>Extracted directly from original laboratory record document (Week_13.pdf):</p>

          <div class="gallery-grid">
            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.1</span><span class="ss-counter-badge">[1 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.1: StudentRepository.java Method Declarations">
                <img src="../assets/images/week-13/week-13_img_1.jpg" alt="Figure 13.1 StudentRepository.java" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 13.1: Repository Interface</div>
                <div class="ss-subcaption">STS editor showing StudentRepository.java declaring all derived query methods and native @Query.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_1.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.2</span><span class="ss-counter-badge">[2 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.2: StudentQueryController.java Endpoints">
                <img src="../assets/images/week-13/week-13_img_2.jpg" alt="Figure 13.2 StudentQueryController.java" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 13.2: Query Controller</div>
                <div class="ss-subcaption">STS editor showing StudentQueryController.java endpoint definitions for each query method.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_2.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.3</span><span class="ss-counter-badge">[3 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.3: Browser JSON for findByName('Kumar')">
                <img src="../assets/images/week-13/week-13_img_3.jpg" alt="Figure 13.3 findByName JSON" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 13.3: findByName Results</div>
                <div class="ss-subcaption">Chrome browser displaying JSON results for findByName("Kumar").</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_3.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.4</span><span class="ss-counter-badge">[4 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.4: Browser JSON for findByFirstNameAndLastName">
                <img src="../assets/images/week-13/week-13_img_4.jpg" alt="Figure 13.4 findByFirstNameAndLastName" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 13.4: AND Conjunction Query</div>
                <div class="ss-subcaption">Chrome browser displaying JSON results for findByFirstNameAndLastName.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_4.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.5</span><span class="ss-counter-badge">[5 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.5: Browser JSON for findByLastNameOrderByFirstNameAsc">
                <img src="../assets/images/week-13/week-13_img_5.png" alt="Figure 13.5 OrderBy Query" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 13.5: Sorted Query Results</div>
                <div class="ss-subcaption">Chrome browser displaying sorted JSON results for findByLastNameOrderByFirstNameAsc.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_5.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.6</span><span class="ss-counter-badge">[6 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.6: Browser JSON for Native SQL @Query">
                <img src="../assets/images/week-13/week-13_img_6.jpg" alt="Figure 13.6 Native @Query" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 13.6: Native SQL @Query</div>
                <div class="ss-subcaption">Chrome browser displaying JSON result for native SQL @Query execution.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_6.jpg" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>

            <div class="ss-card">
              <div class="ss-card-header"><span class="ss-step-badge">Figure 13.7</span><span class="ss-counter-badge">[7 / 7]</span></div>
              <div class="ss-img-wrap" data-title="Figure 13.7: STS Console showing generated Hibernate SQL">
                <img src="../assets/images/week-13/week-13_img_7.png" alt="Figure 13.7 Hibernate SQL Telemetry" />
                <div class="ss-zoom-overlay">🔍 Click to Zoom</div>
              </div>
              <div class="ss-card-body">
                <div class="ss-caption">Figure 13.7: Hibernate SQL Telemetry</div>
                <div class="ss-subcaption">STS Console showing generated Hibernate SQL query statements verifying AST translation.</div>
                <div class="ss-actions"><button class="ss-btn ss-replace-btn">📷 Replace</button><a href="../assets/images/week-13/week-13_img_7.png" download class="ss-btn ss-download-btn">⬇ Download</a><input type="file" class="ss-file-input" accept="image/*" /></div>
              </div>
            </div>
          </div>
        </section>

        <!-- TEST MATRIX -->
        <section class="content-section" id="matrix">
          <h2 class="content-section-title"><span class="section-icon">📊</span> 8. Test Cases and Observation Matrix</h2>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Test Method</th><th>HTTP Endpoint / Parameters</th><th>Generated SQL Condition</th><th>Observed Result</th><th>Status</th></tr></thead>
              <tbody>
                <tr><td>findAll()</td><td>/api/students/all</td><td>SELECT * FROM student</td><td>Retrieved all 5 seeded student records</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>findByName()</td><td>/api/students/by-name?name=Kumar</td><td>WHERE name = 'Kumar'</td><td>Retrieved 2 students named Kumar</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>findByFirstName()</td><td>/by-firstname?firstName=Kumar</td><td>WHERE first_name = 'Kumar'</td><td>Retrieved 2 matching records</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>findByFirstNameAndLastName()</td><td>/by-first-last?firstName=Kumar&lastName=Sharma</td><td>WHERE first_name=? AND last_name=?</td><td>Retrieved exact 1 record: Kumar Sharma</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>findByFirstNameOrLastName()</td><td>/by-first-or-last?firstName=Kumar&lastName=Sharma</td><td>WHERE first_name=? OR last_name=?</td><td>Retrieved 4 matching union records</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>findByLastNameOrderByFirstNameAsc()</td><td>/order-asc?lastName=Sharma</td><td>WHERE last_name=? ORDER BY first_name ASC</td><td>Returned Amit, Kumar, Rohit (sorted)</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>findFirst10ByLastName()</td><td>/first10?lastName=Sharma</td><td>FETCH FIRST 10 ROWS ONLY</td><td>Returned top matching records (3 records)</td><td><span class="badge badge-green">PASS</span></td></tr>
                <tr><td>fetchByFirstName() [@Query]</td><td>/native-query?firstName=Kumar</td><td>SELECT * FROM student WHERE first_name=?</td><td>Returned Kumar Sharma via raw SQL execution</td><td><span class="badge badge-green">PASS</span></td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="content-section" id="result">
          <h2 class="content-section-title"><span class="section-icon">🏁</span> 9. Result</h2>
          <p>
            Thus, all 8 specialized derived query methods and custom native SQL queries using @Query in Spring Data JPA repository were successfully implemented, executed, and validated. Hibernate SQL query telemetry confirmed precise AST SQL generation and accurate result filtering.
          </p>
        </section>

        <section class="content-section" id="note">
          <h2 class="content-section-title"><span class="section-icon">📋</span> 10. Laboratory Observation Note</h2>
          <div style="background:var(--bg-card);border:1px solid var(--border-glass);border-radius:var(--r-lg);padding:24px;border-left:4px solid var(--blue-primary);line-height:1.75;">
            <p><strong>Note Type:</strong> Laboratory Observation &amp; Execution Verification</p>
            <p><strong>Student:</strong> Venkata Sai Karthikeya Kaja (Roll No: 24EU08161)</p>
            <p><strong>Date:</strong> 21-04-2026</p>
            <p><strong>Observation Summary:</strong> Execution verified. All 8 derived and custom query methods executed correctly on Spring Data JPA repository. Hibernate SQL telemetry verified exact where-clause predicates and order directives. All test cases passed.</p>
          </div>
        </section>
    """

    footer = get_page_footer(13)
    full_html = header + body + footer
    out_file = os.path.join(pages_dir, 'week-13.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated: {out_file}')

generate_week_13()
print("Weeks 9 to 13 successfully generated!")

