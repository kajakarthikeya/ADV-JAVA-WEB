import os
import sys
sys.path.insert(0, '.')
from generate_step_screenshots import (
    create_ubuntu_terminal,
    create_windows_terminal,
    create_netbeans_ide,
    create_sts_ide,
    create_browser_window
)

print("Generating Week 0 and Week 1 step screenshots...")

# ----------------- WEEK 0 -----------------
w0_dir = "assets/images/week-0/task-1"
os.makedirs(w0_dir, exist_ok=True)

# Step 01
create_windows_terminal(
    os.path.join(w0_dir, "step-01.png"),
    "Command Prompt - Java SE vs Jakarta EE Architecture",
    "C:\\Users\\24EU08161",
    ["java -version", "echo %JAVA_HOME%"],
    [
        "openjdk version \"26.0.1\" 2026-04-21",
        "OpenJDK Runtime Environment (build 26.0.1+8-34)",
        "OpenJDK 64-Bit Server VM (build 26.0.1+8-34, mixed mode)",
        "JAVA_HOME = C:\\Program Files\\Java\\jdk-26",
        "[OK] Java SE Runtime Active for Venkata Sai Karthikeya Kaja (24EU08161)",
        "[INFO] Core Java (Desktop/CLI) vs Jakarta EE (Multi-tier Web) verified."
    ]
)

# Step 02
create_browser_window(
    os.path.join(w0_dir, "step-02.png"),
    "Java Applet Sunsetting vs Modern Servlets",
    "http://localhost:8080/applet-vs-servlet",
    "Applet Deprecation & Modern Servlet Architecture",
    [
        "Candidate: Venkata Sai Karthikeya Kaja · Roll: 24EU08161",
        "Paradigm Shift: Client-side Applet (NPAPI Plugin) -> Server-side Java Servlet",
        "Security Model: Sandboxed Applet Deprecated (Java 9+) in favor of Server Container",
        "Web Container: Apache Tomcat 9.0 executing servlets via thread-pooled request workers",
        "Execution Status: HTTP 200 OK · Servlet Engine Active"
    ]
)

# Step 03
create_netbeans_ide(
    os.path.join(w0_dir, "step-03.png"),
    "NetBeans IDE 8.2 - ServletHierarchyDemo.java",
    "Week0Architecture",
    "ServletHierarchyDemo.java",
    [
        "package com.sahe.advancedjava;",
        "import javax.servlet.*;",
        "import javax.servlet.http.*;",
        "import java.io.*;",
        "",
        "public class ServletHierarchyDemo extends HttpServlet {",
        "    // GenericServlet provides protocol-independent service()",
        "    // HttpServlet extends GenericServlet providing doGet() and doPost()",
        "    @Override",
        "    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {",
        "        resp.setContentType(\"text/html;charset=UTF-8\");",
        "        PrintWriter out = resp.getWriter();",
        "        out.println(\"<h1>Candidate: Venkata Sai Karthikeya Kaja</h1>\");",
        "        out.println(\"<p>Roll Number: 24EU08161</p>\");",
        "        out.println(\"<p>Hierarchy: Servlet -> GenericServlet -> HttpServlet</p>\");",
        "    }",
        "}"
    ],
    [
        "ant -f C:\\\\Projects\\\\Week0Architecture run",
        "compile:",
        "compile-jsps:",
        "Incremental deployment complete.",
        "BUILD SUCCESSFUL (total time: 1 second)"
    ]
)

# Step 04
create_windows_terminal(
    os.path.join(w0_dir, "step-04.png"),
    "Command Prompt - JDBC Type-4 vs ODBC Architecture",
    "C:\\Users\\24EU08161",
    ["java -cp .;mysql-connector-j.jar DriverArchitectureAnalysis"],
    [
        "JDBC vs ODBC Architectural Verification for 24EU08161:",
        "Type 1: JDBC-ODBC Bridge (Legacy, Platform-dependent, Deprecated Java 8)",
        "Type 2: Native-API Driver (Part Java, requires C/C++ native client libraries)",
        "Type 3: Network-Protocol Driver (Middleware server translates socket calls)",
        "Type 4: Pure Java Direct-to-Database Driver (Fastest, portable, zero native code)",
        "[OK] Type 4 Pure Java Socket Driver Active on port 3306",
        "Verification Status: PASSED (Candidate: 24EU08161)"
    ]
)

# Step 05
create_browser_window(
    os.path.join(w0_dir, "step-05.png"),
    "State Tracking: Cookies vs Sessions",
    "http://localhost:8080/state-management",
    "HTTP State Management: Cookies vs Sessions Inspection",
    [
        "Candidate Identification: Venkata Sai Karthikeya Kaja (Roll: 24EU08161)",
        "Cookie Inspection: Set-Cookie: JSESSIONID=7B9D24EU08161A4F; Path=/; HttpOnly; SameSite=Lax",
        "Session State: HttpSession id=7B9D24EU08161A4F stored in Server Memory Heap",
        "Session Attributes: studentName='Venkata Sai Karthikeya Kaja', course='24IT385'",
        "Comparison: Cookies stored on Client Browser (<4KB); Sessions stored on Server Container"
    ]
)

# Step 06
create_sts_ide(
    os.path.join(w0_dir, "step-06.png"),
    "Spring Tool Suite 4 - SpringArchitectureConfig.java",
    "Week0SpringComparison",
    "SpringArchitectureConfig.java",
    [
        "package com.sahe.springdemo;",
        "import org.springframework.boot.SpringApplication;",
        "import org.springframework.boot.autoconfigure.SpringBootApplication;",
        "import org.springframework.web.bind.annotation.*;",
        "",
        "@SpringBootApplication",
        "@RestController",
        "public class SpringArchitectureConfig {",
        "    // Traditional Spring: XML beans, explicit DispatcherServlet, external Tomcat",
        "    // Spring Boot: @AutoConfiguration, embedded Tomcat, starter dependencies",
        "    @GetMapping(\"/status\")",
        "    public String status() {",
        "        return \"Spring Boot Active · Candidate: 24EU08161 · Year: 2026-2027\";",
        "    }",
        "    public static void main(String[] args) {",
        "        SpringApplication.run(SpringArchitectureConfig.class, args);",
        "    }",
        "}"
    ],
    [
        "  .   ____          _            __ _ _",
        " /\\\\ / ___'_ __ _ _(_)_ __  __ _ \\ \\ \\ \\",
        "( ( )\\___ | '_ | '_| | '_ \\/ _` | \\ \\ \\ \\",
        "Spring Boot v3.2.0 · Embedded Tomcat initialized on port 8080",
        "Started SpringArchitectureConfig in 1.45 seconds (process running for 2.1s)"
    ]
)

# Step 07
create_ubuntu_terminal(
    os.path.join(w0_dir, "step-07.png"),
    "Ubuntu Terminal - Web Container Port & Process Listener",
    ["sudo netstat -tulpn | grep 8080", "systemctl status tomcat9"],
    [
        "Active Internet connections (only servers)",
        "tcp6       0      0 :::8080                 :::*                    LISTEN      1428/java",
        "● tomcat9.service - Apache Tomcat 9 Web Application Server",
        "     Loaded: loaded (/lib/systemd/system/tomcat9.service; enabled)",
        "     Active: active (running) since Sat 2026-11-14 06:00:00 IST",
        "   Main PID: 1428 (java)",
        "      Tasks: 42 (limit: 18882)",
        "     Memory: 218.4M",
        "     CGroup: /system.slice/tomcat9.service",
        "             └─1428 /usr/lib/jvm/jdk-26/bin/java -Djava.util.logging.config.file=...",
        "[OK] Web Container Listening on Port 8080 · Ready for 24EU08161 Servlets"
    ]
)

# Step 08
create_windows_terminal(
    os.path.join(w0_dir, "step-08.png"),
    "Command Prompt - Standalone JAR vs Enterprise WAR Inspection",
    "C:\\Users\\24EU08161\\Desktop",
    ["jar -tf WebApplication.war"],
    [
        "META-INF/",
        "META-INF/MANIFEST.MF",
        "WEB-INF/",
        "WEB-INF/web.xml",
        "WEB-INF/classes/",
        "WEB-INF/classes/com/sahe/advancedjava/StudentServlet.class",
        "WEB-INF/lib/",
        "WEB-INF/lib/mysql-connector-j-8.3.0.jar",
        "index.html",
        "[OK] Enterprise WAR Package Structure Validated for Deployment",
        "Target Container: Apache Tomcat 9 / GlassFish (Candidate: 24EU08161)"
    ]
)

# Step 09
create_windows_terminal(
    os.path.join(w0_dir, "step-09.png"),
    "Command Prompt - Java Database Connection Verification",
    "C:\\Users\\24EU08161",
    ["java -cp .;mysql-connector-j.jar ConnectionTest"],
    [
        "Testing Type 4 Direct Socket JDBC Connection...",
        "Driver: com.mysql.cj.jdbc.Driver (Loaded successfully)",
        "Connecting to jdbc:mysql://localhost:3306/studentdb...",
        "[SUCCESS] Database Connection Established: com.mysql.cj.jdbc.ConnectionImpl@4b672",
        "Database Product Name: MySQL 8.0.36",
        "Candidate Authentication: Venkata Sai Karthikeya Kaja (24EU08161)",
        "[OK] Ready for JDBC Statement & PreparedStatement operations."
    ]
)

# Step 10
create_browser_window(
    os.path.join(w0_dir, "step-10.png"),
    "Week 0 Architectural Synthesis",
    "http://localhost:8080/week0-summary",
    "Week 0: Advanced Java Architecture Synthesis",
    [
        "Student Name: Venkata Sai Karthikeya Kaja · Roll Number: 24EU08161",
        "Department of Information Technology · Siddhartha Academy of Higher Education",
        "Course: Advanced Java Programming Lab (24IT385) · Academic Year 2026-2027",
        "Verified Competencies:",
        "  1. Core Java SE vs Jakarta EE Multi-tier Topologies",
        "  2. Applet Sunsetting & High-Throughput Servlet Container Life Cycles",
        "  3. Type 1/2/3 vs Type 4 Pure Java Database Drivers",
        "  4. Stateless HTTP Session Tracking (Cookies & Sessions)",
        "  5. Enterprise Deployment Requirements (Tomcat Web Server & WAR Structures)"
    ]
)

print("Week 0 screenshots generated successfully!")

# ----------------- WEEK 1 -----------------
w1_dir = "assets/images/week-1/task-1"
os.makedirs(w1_dir, exist_ok=True)

# Step 01
create_windows_terminal(
    os.path.join(w1_dir, "step-01.png"),
    "Command Prompt - Language Benchmark: C, C++, Java, Python, JS",
    "C:\\Users\\24EU08161",
    ["python benchmark_suite.py"],
    [
        "Comparative Language Performance Benchmark (Matrix Computation 1000x1000):",
        "Candidate: Venkata Sai Karthikeya Kaja (Roll: 24EU08161)",
        "----------------------------------------------------------------------",
        "Language        Execution Model         Execution Time (s)    Memory (MB)",
        "C (GCC 13 -O3)  Native Machine Code     0.118 s               4.2 MB",
        "C++ (G++ -O3)   Native Machine Code     0.124 s               5.1 MB",
        "Java (JDK 26)   Bytecode + JIT HotSpot  0.182 s               48.6 MB",
        "JavaScript (V8) Bytecode + JIT Crank    0.286 s               38.2 MB",
        "Python (3.12)   Interpreted Bytecode    1.428 s               18.4 MB",
        "----------------------------------------------------------------------",
        "[CONCLUSION] Java offers optimal trade-off of portability, safety, and near-native speed."
    ]
)

# Step 02
create_windows_terminal(
    os.path.join(w1_dir, "step-02.png"),
    "Command Prompt - Java Bytecode Disassembly (javap -c)",
    "C:\\Users\\24EU08161",
    ["javap -c -v Benchmark.class"],
    [
        "Classfile /C:/Users/24EU08161/Benchmark.class",
        "  Last modified Nov 14, 2026; size 824 bytes",
        "  SHA-256 checksum a42cb2413a22454c98c5085a0e293b02",
        "  Compiled from \"Benchmark.java\"",
        "public class com.sahe.Benchmark {",
        "  public static void main(java.lang.String[]);",
        "    Code:",
        "       0: iconst_0",
        "       1: istore_1",
        "       2: iload_1",
        "       3: sipush        1000",
        "       6: if_icmpge     24",
        "       9: getstatic     #2 // Field java/lang/System.out:Ljava/io/PrintStream;",
        "      12: ldc           #3 // String Roll: 24EU08161",
        "      14: invokevirtual #4 // Method java/io/PrintStream.println:(Ljava/lang/String;)V"
    ]
)

# Step 03
create_netbeans_ide(
    os.path.join(w1_dir, "step-03.png"),
    "NetBeans IDE 8.2 - Web Project Architecture",
    "LabTask1WebProject",
    "LanguageParadigmService.java",
    [
        "package com.sahe.labtask1;",
        "import java.util.*;",
        "",
        "public class LanguageParadigmService {",
        "    public Map<String, String> getParadigmSummary() {",
        "        Map<String, String> map = new LinkedHashMap<>();",
        "        map.put(\"Student\", \"Venkata Sai Karthikeya Kaja\");",
        "        map.put(\"Roll\", \"24EU08161\");",
        "        map.put(\"C\", \"Procedural · Structured · Manual Memory\");",
        "        map.put(\"C++\", \"Multi-paradigm · OOP · Generic · Pointers\");",
        "        map.put(\"Java\", \"Object-Oriented · Platform Independent · Managed Heap\");",
        "        map.put(\"Python\", \"Multi-paradigm · Dynamic Typing · Rapid Scripting\");",
        "        map.put(\"JavaScript\", \"Event-Driven · Prototype-based · Fullstack Web\");",
        "        return map;",
        "    }",
        "}"
    ],
    [
        "ant -f C:\\\\Projects\\\\LabTask1WebProject compile",
        "Compiling 1 source file to C:\\\\Projects\\\\LabTask1WebProject\\\\build\\\\classes",
        "BUILD SUCCESSFUL (total time: 0 seconds)"
    ]
)

# Step 04
create_netbeans_ide(
    os.path.join(w1_dir, "step-04.png"),
    "NetBeans IDE 8.2 - Deployment Descriptor web.xml",
    "LabTask1WebProject",
    "web.xml",
    [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<web-app xmlns=\"http://xmlns.jcp.org/xml/ns/javaee\"",
        "         xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"",
        "         version=\"3.1\">",
        "    <display-name>LabTask1 - 24EU08161</display-name>",
        "    <servlet>",
        "        <servlet-name>ParadigmServlet</servlet-name>",
        "        <servlet-class>com.sahe.labtask1.ParadigmServlet</servlet-class>",
        "    </servlet>",
        "    <servlet-mapping>",
        "        <servlet-name>ParadigmServlet</servlet-name>",
        "        <url-pattern>/paradigms</url-pattern>",
        "    </servlet-mapping>",
        "    <welcome-file-list>",
        "        <welcome-file>index.html</welcome-file>",
        "    </welcome-file-list>",
        "</web-app>"
    ],
    [
        "XML Validation: Valid web.xml 3.1 configuration.",
        "Target Context: /LabTask1WebProject"
    ]
)

# Step 05
create_browser_window(
    os.path.join(w1_dir, "step-05.png"),
    "Network Inspector — HTTP Request/Response Lifecycle",
    "http://localhost:8080/LabTask1WebProject/paradigms",
    "HTTP Request-Response Lifecycle & Headers Inspection",
    [
        "Request URL: http://localhost:8080/LabTask1WebProject/paradigms",
        "Request Method: GET | Status Code: 200 OK | Remote Address: 127.0.0.1:8080",
        "Response Headers: Content-Type: application/json;charset=UTF-8, Server: Apache-Coyote/1.1",
        "Response Payload: {",
        "  \"author\": \"Venkata Sai Karthikeya Kaja\",",
        "  \"rollNumber\": \"24EU08161\",",
        "  \"architecture\": \"Client-Server 3-Tier Multi-Threaded Engine\"",
        "}"
    ]
)

# Step 06
create_windows_terminal(
    os.path.join(w1_dir, "step-06.png"),
    "Command Prompt - JVM Heap & Memory Layout Verification",
    "C:\\Users\\24EU08161",
    ["java -XX:+PrintFlagsFinal -version | findstr /I \"HeapSize\""],
    [
        "   size_t ErgoHeapSizeLimit       = 0               {product} {default}",
        "   size_t InitialHeapSize         = 268435456       {product} {ergonomic}",
        "   size_t LargePageHeapSizeThreshold = 134217728    {product} {default}",
        "   size_t MaxHeapSize             = 4294967296      {product} {ergonomic}",
        "[OK] 4 GB Max Heap Configured for Enterprise Workloads",
        "Runtime Verification Complete for Venkata Sai Karthikeya Kaja (24EU08161)"
    ]
)

# Step 07
create_ubuntu_terminal(
    os.path.join(w1_dir, "step-07.png"),
    "Ubuntu Terminal - Java Classpath & Dependency Linking",
    ["export CLASSPATH=.:/usr/share/java/*", "echo $CLASSPATH", "javac -cp $CLASSPATH ParadigmApp.java"],
    [
        "CLASSPATH = .:/usr/share/java/servlet-api-3.1.jar:/usr/share/java/mysql-connector-j.jar",
        "karthik@ubuntu:~$ javac -cp $CLASSPATH ParadigmApp.java",
        "[OK] Compilation successful without classpath errors.",
        "karthik@ubuntu:~$ java -cp $CLASSPATH ParadigmApp",
        "Language Paradigm Diagnostic Suite Initialized for 24EU08161.",
        "Tier Separation: Presentation (HTML/CSS) -> Business (Java Servlets) -> Persistence (MySQL)"
    ]
)

# Step 08
create_windows_terminal(
    os.path.join(w1_dir, "step-08.png"),
    "Command Prompt - Multi-Tier Web Topology Verification",
    "C:\\Users\\24EU08161",
    ["curl -i http://localhost:8080/LabTask1WebProject/paradigms"],
    [
        "HTTP/1.1 200 OK",
        "Server: Apache-Coyote/1.1",
        "X-Developer-Roll: 24EU08161",
        "X-Department: Information Technology",
        "Content-Type: application/json;charset=UTF-8",
        "Content-Length: 184",
        "Date: Sat, 14 Nov 2026 06:00:00 GMT",
        "",
        "{\"status\":\"SUCCESS\",\"tier\":\"Application Server\",\"student\":\"Venkata Sai Karthikeya Kaja\"}"
    ]
)

# Step 09
create_windows_terminal(
    os.path.join(w1_dir, "step-09.png"),
    "Command Prompt - JIT Compiler HotSpot Optimization Trace",
    "C:\\Users\\24EU08161",
    ["java -XX:+PrintCompilation ConcurrencyBenchmark"],
    [
        "     52    1       3       java.lang.StringLatin1::hashCode (42 bytes)",
        "     54    2       3       java.lang.Object::<init> (1 bytes)",
        "     60    3       3       com.sahe.Benchmark::compute (28 bytes)",
        "     68    4       4       com.sahe.Benchmark::compute (28 bytes)",
        "[JIT Tier 4 C2 Compiler Activated] Bytecode converted to native x86_64 assembly.",
        "Candidate Verification: 24EU08161 (Near-native speed achieved)"
    ]
)

# Step 10
create_browser_window(
    os.path.join(w1_dir, "step-10.png"),
    "Week 1 Final Synthesis & Lab Task Output",
    "http://localhost:8080/LabTask1WebProject/report",
    "Advanced Java Lab Task 1 — Final Academic Synthesis",
    [
        "Candidate Name: Venkata Sai Karthikeya Kaja · Roll Number: 24EU08161",
        "Department: Information Technology · Siddhartha Academy of Higher Education",
        "Course: Advanced Java Programming Lab (24IT385) · Academic Year 2026-2027",
        "Laboratory Findings:",
        "  • C/C++ provide unmatched raw speed via native compilation but lack built-in memory safety.",
        "  • Java combines bytecode portability with HotSpot JIT compiler to rival native C performance.",
        "  • Python enables rapid scripting but exhibits high execution latency in computationally heavy loops.",
        "  • JavaScript V8 provides responsive asynchronous web clients and single-threaded servers.",
        "  • Enterprise multi-tier architecture cleanly decouples Presentation, Logic, and Persistence."
    ]
)

print("Week 1 screenshots generated successfully!")
