# -*- coding: utf-8 -*-
"""
Step-by-step screenshot metadata for all practical tasks (Week 2 to Week 13)
Each step contains: (step_num, title, filename, description)
"""

STEP_GALLERY_DATA = {
    "week-0": {
        "task-1": [
            ("Step 01", "Core Java vs Advanced Java Runtime Architecture", "step-01.png", "Inspect JDK 26 runtime environment verifying Java SE Desktop/CLI capabilities versus Jakarta EE distributed multi-tier server architectures."),
            ("Step 02", "Applet Sunsetting vs Modern Java Servlets", "step-02.png", "Analyze browser NPAPI deprecation and transition from client-side Applets to high-performance, container-managed Java Servlets."),
            ("Step 03", "GenericServlet vs HttpServlet Hierarchy", "step-03.png", "Implement protocol-independent GenericServlet service() and protocol-specific HttpServlet doGet()/doPost() in NetBeans IDE 8.2."),
            ("Step 04", "JDBC Type-4 vs ODBC Driver Architecture", "step-04.png", "Evaluate Type 1/2/3 drivers versus Type 4 Pure Java direct-socket database connectivity, eliminating native ODBC bridge dependencies."),
            ("Step 05", "HTTP State Management: Cookies vs Sessions", "step-05.png", "Inspect Set-Cookie headers in browser developer tools comparing client-side cookies (<4KB) with server-managed HttpSession heaps."),
            ("Step 06", "Spring Boot Auto-Configuration vs Spring Core IoC", "step-06.png", "Contrast legacy Spring XML bean wiring and external Tomcat setup with modern Spring Boot @SpringBootApplication embedded containers."),
            ("Step 07", "Apache Tomcat Port 8080 Listener Verification", "step-07.png", "Verify Apache Tomcat web server TCP port 8080 listener and Catalina servlet engine process execution in Linux environment."),
            ("Step 08", "Standalone Desktop JAR vs Enterprise WAR Deployment", "step-08.png", "Inspect Web Application Archive (WAR) directory structure: WEB-INF/classes, WEB-INF/lib, and standard web.xml deployment descriptors."),
            ("Step 09", "Java Database Connection Pipeline Execution", "step-09.png", "Execute direct JDBC socket connection pipeline verifying DriverManager connection pool initialization and transaction autocommit."),
            ("Step 10", "Theoretical Architectural Synthesis Verification", "step-10.png", "Complete holistic verification of all Advanced Java architectural foundations for student Venkata Sai Karthikeya Kaja (24EU08161).")
        ]
    },
    "week-1": {
        "task-1": [
            ("Step 01", "Multi-Language Benchmark Execution", "step-01.png", "Execute comparative benchmark suite evaluating execution latency and memory overhead across C, C++, Java SE 26, Python 3.12, and Node.js."),
            ("Step 02", "Java Bytecode Disassembly & JVM Stack Inspection", "step-02.png", "Execute javap -c -v to inspect Java bytecode instructions (iconst, istore, sipush, invokevirtual) and JVM operand stack frames."),
            ("Step 03", "NetBeans IDE Web Project Architecture Layout", "step-03.png", "Initialize multi-tiered enterprise Java web application in NetBeans IDE 8.2 configuring source packages, libraries, and compilation build targets."),
            ("Step 04", "Standard Web Deployment Descriptor (web.xml)", "step-04.png", "Configure web.xml deployment descriptor specifying servlet-name, servlet-class, and URL mapping patterns for container ingestion."),
            ("Step 05", "HTTP Request-Response Lifecycle Inspection", "step-05.png", "Inspect HTTP GET request headers, response status codes (200 OK), and JSON payloads in browser network developer tools."),
            ("Step 06", "JVM Heap & Memory Layout Verification", "step-06.png", "Execute java -XX:+PrintFlagsFinal to verify JVM ergonomic heap sizing (MaxHeapSize, InitialHeapSize) for enterprise server applications."),
            ("Step 07", "Java Classpath & Dependency Linking", "step-07.png", "Configure global and local CLASSPATH environment variables to link external library JARs (mysql-connector-j, servlet-api) to compilation targets."),
            ("Step 08", "Multi-Tier Web Topology Verification", "step-08.png", "Execute curl HTTP probes to test multi-tier decoupling between Presentation Tier, Business Logic Tier, and Persistence Layer."),
            ("Step 09", "JIT Compiler HotSpot Optimization Trace", "step-09.png", "Monitor HotSpot C2 JIT compiler tiered compilation converting frequently executed Java bytecode into optimized native x86_64 assembly."),
            ("Step 10", "Final Academic Synthesis Verification", "step-10.png", "Final verification and synthesis of programming language paradigms and web application architectures for Roll Number 24EU08161.")
        ]
    },
    "week-2": {
        "task-1": [
            ("Step 01", "Launch Ubuntu Terminal", "step-01.png", "Initialize Ubuntu Bash terminal session for JDK 26 installation and environment configuration."),
            ("Step 02", "Update Package Index", "step-02.png", "Execute sudo apt update to synchronize repository package lists and ensure system prerequisites are current."),
            ("Step 03", "Create JVM Target Directory", "step-03.png", "Execute sudo mkdir -p /usr/lib/jvm to create standard Linux system JVM storage location."),
            ("Step 04", "Download OpenJDK 26 Tarball", "step-04.png", "Execute wget to fetch official openjdk-26_linux-x64_bin.tar.gz archive directly from java.net."),
            ("Step 05", "Verify SHA256 Checksum", "step-05.png", "Verify cryptographic integrity of downloaded tarball against official manifest using sha256sum."),
            ("Step 06", "Extract JDK Archive", "step-06.png", "Execute sudo tar -xzf to uncompress JDK binaries and modular runtime directly into /usr/lib/jvm."),
            ("Step 07", "Verify Extracted File Tree", "step-07.png", "Inspect /usr/lib/jvm/jdk-26 directory verifying bin, lib, conf, include, and release metadata."),
            ("Step 08", "Register java Binary", "step-08.png", "Execute update-alternatives --install to register java runtime at system priority 1."),
            ("Step 09", "Register javac Compiler", "step-09.png", "Register javac compiler binary with update-alternatives for system-wide command resolution."),
            ("Step 10", "Configure Alternatives Selection", "step-10.png", "Run sudo update-alternatives --config java confirming JDK 26 is selected as the default runtime."),
            ("Step 11", "Configure JAVA_HOME in /etc/environment", "step-11.png", "Add JAVA_HOME=\"/usr/lib/jvm/jdk-26\" to /etc/environment for global system persistence."),
            ("Step 12", "Reload System Environment", "step-12.png", "Execute source /etc/environment and verify echo $JAVA_HOME returns /usr/lib/jvm/jdk-26."),
            ("Step 13", "Update Shell PATH in ~/.bashrc", "step-13.png", "Append export PATH=$JAVA_HOME/bin:$PATH to user ~/.bashrc configuration."),
            ("Step 14", "Verify java Runtime Version", "step-14.png", "Execute java -version confirming OpenJDK 26 Runtime Environment (build 26+35-2315)."),
            ("Step 15", "Verify javac Compiler Version", "step-15.png", "Execute javac -version confirming javac 26 is active on system path."),
            ("Step 16", "Compile & Run Test Program", "step-16.png", "Compile and run HelloJava.java verifying successful execution for Venkata Sai Karthikeya Kaja (24EU08161).")
        ]
    },
    "week-3": {
        "task-1": [
            ("Step 01", "Initialize Command Prompt", "step-01.png", "Open Windows Command Prompt and navigate to C:\\AccessDemo project directory."),
            ("Step 02", "Create Project Subdirectories", "step-02.png", "Execute mkdir lib src data to organize libraries, source files, and database storage."),
            ("Step 03", "Download UCanAccess JARs", "step-03.png", "Fetch pure-Java Type 4 UCanAccess driver package and Jackcess bridge components."),
            ("Step 04", "Verify Classpath Dependencies", "step-04.png", "Confirm all 5 JARs present: ucanaccess, jackcess, commons-lang3, commons-logging, hsqldb."),
            ("Step 05", "Create MS Access Database", "step-05.png", "Create Database.accdb Microsoft Access database container in data directory."),
            ("Step 06", "Design Users Table Schema", "step-06.png", "Design Users table with columns: ID (AutoNumber), StudentName, RollNumber, Department."),
            ("Step 07", "Pre-populate Test Records", "step-07.png", "Insert candidate record: ID=1, Venkata Sai Karthikeya Kaja, 24EU08161, Information Technology."),
            ("Step 08", "Author AccessDemo.java", "step-08.png", "Write Java source code establishing JDBC connection and Statement execution."),
            ("Step 09", "Load UCanAccess Driver", "step-09.png", "Invoke Class.forName(\"net.ucanaccess.jdbc.UcanaccessDriver\") to register driver."),
            ("Step 10", "Define Access Connection URL", "step-10.png", "Configure URL string: jdbc:ucanaccess://C:/AccessDemo/data/Database.accdb."),
            ("Step 11", "Author SQL SELECT Query", "step-11.png", "Implement stmt.executeQuery(\"SELECT * FROM Users\") and ResultSet cursor loop."),
            ("Step 12", "Configure CLASSPATH Variable", "step-12.png", "Set Windows CLASSPATH environment variable referencing .;lib/* to resolve driver classes."),
            ("Step 13", "Compile AccessDemo.java", "step-13.png", "Execute javac -cp \".;lib/*\" src\\AccessDemo.java -d bin without compiler errors."),
            ("Step 14", "Execute Program via java", "step-14.png", "Execute java -cp \"bin;lib/*\" AccessDemo establishing pure-Java Access bridge."),
            ("Step 15", "Verify Formatted Record Output", "step-15.png", "Terminal console prints tabular student records confirming 24EU08161 retrieved."),
            ("Step 16", "Clean Resource Closure", "step-16.png", "Safely close ResultSet, Statement, and Database Connection sockets.")
        ]
    },
    "week-4": {
        "task-1": [
            ("Step 01", "Launch NetBeans IDE 8.2", "step-01.png", "Launch NetBeans IDE workspace and prepare for remote database project initialization."),
            ("Step 02", "Create Java Application Project", "step-02.png", "Create new project RemoteMySQLApp with package com.karthik.remotedb."),
            ("Step 03", "Add MySQL Connector/J Library", "step-03.png", "Add mysql-connector-j-8.0.33.jar to NetBeans project libraries tree."),
            ("Step 04", "Ping Remote MySQL Server", "step-04.png", "Verify network ping and TCP connectivity to remote server 10.0.9.44 on port 3306."),
            ("Step 05", "Configure JDBC Connection URL", "step-05.png", "Set URL: jdbc:mysql://10.0.9.44:3306/labdb with credentials."),
            ("Step 06", "Load MySQL Driver", "step-06.png", "Execute Class.forName(\"com.mysql.cj.jdbc.Driver\") to register Type 4 driver."),
            ("Step 07", "Establish Socket Connection", "step-07.png", "Invoke DriverManager.getConnection() establishing socket with remote host."),
            ("Step 08", "Create Statement Object", "step-08.png", "Instantiate Statement object for remote SQL dispatch."),
            ("Step 09", "Execute INSERT Query", "step-09.png", "Dispatch INSERT INTO Employee VALUES (101, 'Karthik', 'IT', '24EU08161')."),
            ("Step 10", "Verify Insert Console Output", "step-10.png", "NetBeans output verifies 1 row inserted into remote MySQL database."),
            ("Step 11", "Execute SELECT Query", "step-11.png", "Dispatch SELECT * FROM Employee and initialize ResultSet cursor."),
            ("Step 12", "Parse ResultSet Columns", "step-12.png", "Iterate ResultSet printing emp_id, emp_name, dept, and roll_no to console."),
            ("Step 13", "Execute UPDATE Query", "step-13.png", "Dispatch UPDATE query modifying department field on remote server."),
            ("Step 14", "Verify Remote Updated Data", "step-14.png", "Console displays updated employee record confirming remote persistence."),
            ("Step 15", "Execute DELETE Query", "step-15.png", "Dispatch DELETE query removing test employee record from remote database."),
            ("Step 16", "Close Sockets & Build Success", "step-16.png", "Release remote database connection cleanly; NetBeans prints BUILD SUCCESSFUL.")
        ]
    },
    "week-5": {
        "task-1": [
            ("Step 01", "Open NetBeans Remote Workspace", "step-01.png", "Open NetBeans IDE configured for remote database operations."),
            ("Step 02", "Verify JDBC Driver in Tree", "step-02.png", "Inspect Libraries node verifying MySQL Connector/J driver dependency."),
            ("Step 03", "Connect to Remote MySQL Host", "step-03.png", "Establish authenticated TCP connection to remote database instance."),
            ("Step 04", "Author DatabaseOperations.java", "step-04.png", "Write class implementing batch processing and parameterized statements."),
            ("Step 05", "Implement PreparedStatement", "step-05.png", "Create PreparedStatement with parameterized SQL template for security."),
            ("Step 06", "Bind SQL Parameters", "step-06.png", "Bind candidate parameters (Roll: 24EU08161, Name: Karthik) dynamically."),
            ("Step 07", "Execute PreparedStatement Update", "step-07.png", "Execute ps.executeUpdate() persisting new employee record."),
            ("Step 08", "Verify Record Persistence", "step-08.png", "Confirm record ingestion on remote host via console verification."),
            ("Step 09", "Implement Dynamic Query Filter", "step-09.png", "Construct parameterized SELECT query filtering by employee roll number."),
            ("Step 10", "Execute Parameterized Search", "step-10.png", "Execute query and iterate through matched result rows."),
            ("Step 11", "Perform Transactional Batch Update", "step-11.png", "Batch multiple update operations in a single atomic transaction."),
            ("Step 12", "Commit Database Transaction", "step-12.png", "Invoke conn.commit() ensuring ACID transaction compliance."),
            ("Step 13", "Inspect Database Metadata", "step-13.png", "Query DatabaseMetaData inspecting column types and table privileges."),
            ("Step 14", "Execute Parameterized DELETE", "step-14.png", "Execute targeted DELETE query with bound employee identifier."),
            ("Step 15", "Clean Socket Termination", "step-15.png", "Close PreparedStatement and release TCP network connection cleanly."),
            ("Step 16", "Verify Final Console Output", "step-16.png", "Inspect NetBeans console logs verifying BUILD SUCCESSFUL.")
        ]
    },
    "week-6": {
        "task-1": [
            ("Step 01", "MySQL CLI Root Login", "step-01.png", "Open MySQL 8.0 Command Line Client and authenticate with root credentials."),
            ("Step 02", "Create Database studentdb", "step-02.png", "Execute CREATE DATABASE studentdb; in MySQL terminal."),
            ("Step 03", "Switch to Database Context", "step-03.png", "Execute USE studentdb; setting active database workspace."),
            ("Step 04", "Create Student Table", "step-04.png", "Execute CREATE TABLE Student (roll_no VARCHAR(20) PRIMARY KEY, name VARCHAR(50), department VARCHAR(50));"),
            ("Step 05", "Verify Table Schema", "step-05.png", "Run DESCRIBE Student; confirming columns, data types, and primary key."),
            ("Step 06", "Create NetBeans Project", "step-06.png", "Create Java Application project StudentCRUDApp in NetBeans IDE."),
            ("Step 07", "Add MySQL Connector/J", "step-07.png", "Add mysql-connector-j-8.0.33.jar to project Libraries."),
            ("Step 08", "Write StudentCRUD.java", "step-08.png", "Author imports and main class skeleton for full CRUD operations."),
            ("Step 09", "Implement getConnection()", "step-09.png", "Implement JDBC driver manager connection factory method."),
            ("Step 10", "Implement INSERT Operation", "step-10.png", "Write INSERT SQL query populating student 24EU08161 (Karthik, IT)."),
            ("Step 11", "Execute INSERT in NetBeans", "step-11.png", "Run INSERT routine; console verifies record successfully created."),
            ("Step 12", "Verify Record in MySQL CLI", "step-12.png", "Run SELECT * FROM Student; in MySQL CLI verifying student table row."),
            ("Step 13", "Implement SELECT Operation", "step-13.png", "Implement ResultSet iteration displaying all registered students."),
            ("Step 14", "Execute SELECT & View Records", "step-14.png", "NetBeans output renders formatted tabular student records."),
            ("Step 15", "Implement UPDATE Operation", "step-15.png", "Write and execute UPDATE query modifying department to Information Tech."),
            ("Step 16", "Verify UPDATE in MySQL CLI", "step-16.png", "Verify updated record fields in MySQL command line interface."),
            ("Step 17", "Implement DELETE Operation", "step-17.png", "Implement DELETE statement targeting roll number 24EU08161."),
            ("Step 18", "Final CRUD Execution Report", "step-18.png", "Console displays final CRUD summary; NetBeans confirms BUILD SUCCESSFUL.")
        ]
    },
    "week-7": {
        "task-1": [
            ("Step 01", "NetBeans WebApp Wizard", "step-01.png", "Create Web Application WebApplication8 in NetBeans 8.2 with Apache Tomcat."),
            ("Step 02", "Configure index.html", "step-02.png", "Configure index.html under Web Pages verifying 24EU08161 header.")
        ],
        "task-2": [
            ("Step 01", "Author NewServlet.java Code", "step-01.png", "NetBeans editor displaying NewServlet.java rendering roll number 24EU08161."),
            ("Step 02", "Browser Runtime Output", "step-02.png", "Browser window verifying Student Details and Roll Number 24EU08161."),
            ("Step 03", "NetBeans Project Hierarchy", "step-03.png", "Full NetBeans workspace verifying Tomcat server deployment and project tree."),
            ("Step 04", "NewServlet2.java Code", "step-04.png", "NetBeans editor verifying NewServlet2 with Register Number 24U08161."),
            ("Step 05", "NewServlet2 Browser Output", "step-05.png", "Browser output verifying HTTP Servlet rendering register details.")
        ],
        "task-3": [
            ("Step 01", "Author GET/POST HTML Form", "step-01.png", "HTML form authoring input elements for GET and POST dispatch testing."),
            ("Step 02", "Author GetPostServlet.java", "step-02.png", "Servlet overriding both doGet() and doPost() request handlers."),
            ("Step 03", "HTTP GET Request Output", "step-03.png", "Browser output displaying parameters received via HTTP GET query string."),
            ("Step 04", "HTTP POST Request Output", "step-04.png", "Browser output displaying parameters received via HTTP POST request payload.")
        ],
        "task-4": [
            ("Step 01", "Author MyGenericServlet.java", "step-01.png", "Servlet extending GenericServlet and implementing protocol-neutral service()."),
            ("Step 02", "Generic Servlet Output", "step-02.png", "Browser verifying response generated by GenericServlet implementation.")
        ],
        "task-5": [
            ("Step 01", "Author LifeCycleServlet.java", "step-01.png", "Servlet implementing init(), service(), and destroy() lifecycle methods."),
            ("Step 02", "Servlet Lifecycle Output", "step-02.png", "Browser and server console output logging sequential lifecycle states.")
        ],
        "task-6": [
            ("Step 01", "Student Form HTML Code", "step-01.png", "Authoring student registration form with fields for Name, Roll No, and Dept."),
            ("Step 02", "Browser Form Filled (karthik, 161, it)", "step-02.png", "Browser form displaying candidate inputs: Name: karthik, Roll No: 161, Dept: it."),
            ("Step 03", "StudentFormServlet.java Code", "step-03.png", "NetBeans editor displaying StudentFormServlet processing form inputs."),
            ("Step 04", "Student Form Submission Output", "step-04.png", "Browser output rendering dynamic confirmation of submitted student details.")
        ]
    },
    "week-8": {
        "task-1": [
            ("Step 01", "Initialize Web App in NetBeans", "step-01.png", "Create Web Application StudentManagementSystem in NetBeans with Tomcat runtime."),
            ("Step 02", "Configure Tomcat 8.5 Server", "step-02.png", "Configure Apache Tomcat server port 8080 and administration credentials."),
            ("Step 03", "Create student_mgmt MySQL Database", "step-03.png", "Create MySQL database student_mgmt and students table schema."),
            ("Step 04", "Add MySQL Driver to WEB-INF/lib", "step-04.png", "Place mysql-connector-j-8.0.33.jar in WEB-INF/lib directory."),
            ("Step 05", "Implement DBConnection Singleton", "step-05.png", "Author singleton connection helper class managing JDBC connections."),
            ("Step 06", "Implement AddStudentServlet", "step-06.png", "Author AddStudentServlet handling student data ingestion via POST."),
            ("Step 07", "Author add_student.html Form", "step-07.png", "Create HTML registration form with input fields for roll number and name."),
            ("Step 08", "Implement DisplayStudentServlet", "step-08.png", "Author DisplayStudentServlet rendering dynamic HTML table from ResultSet."),
            ("Step 09", "Implement SearchStudentServlet", "step-09.png", "Implement search filter querying students by roll number 24EU08161."),
            ("Step 10", "Implement UpdateStudentServlet", "step-10.png", "Author servlet handling record modifications and field updates."),
            ("Step 11", "Implement DeleteStudentServlet", "step-11.png", "Author servlet processing student record deletion via ID parameter."),
            ("Step 12", "Deploy WAR to Tomcat", "step-12.png", "Deploy StudentManagementSystem.war to Tomcat container."),
            ("Step 13", "Test Browser Form Ingestion", "step-13.png", "Submit candidate details (Roll: 24EU08161, Karthik, IT) via web browser."),
            ("Step 14", "View Student List Table", "step-14.png", "Browser displays student records in formatted HTML table with action links."),
            ("Step 15", "Test Search by Roll Number", "step-15.png", "Perform search query for 24EU08161 verifying matched record display."),
            ("Step 16", "Verify MySQL Persistence", "step-16.png", "Verify student record in MySQL database confirming full web app stack.")
        ],
        "task-2": [
            ("Step 01", "Create CookieDemoApp Project", "step-01.png", "Initialize new Java Web project CookieDemoApp in NetBeans."),
            ("Step 02", "Author login.html Form", "step-02.png", "Create HTML login form collecting username for cookie tracking."),
            ("Step 03", "Implement CookieServlet", "step-03.png", "Create CookieServlet extending HttpServlet to instantiate HTTP cookies."),
            ("Step 04", "Extract Request Parameters", "step-04.png", "Extract username parameter in doPost() method."),
            ("Step 05", "Instantiate Cookie Object", "step-05.png", "Create new Cookie(\"student_user\", username) key-value object."),
            ("Step 06", "Configure Cookie Max-Age", "step-06.png", "Set cookie expiration to 24 hours via c.setMaxAge(24 * 60 * 60)."),
            ("Step 07", "Add Cookie to HTTP Response", "step-07.png", "Invoke response.addCookie(c) attaching Set-Cookie header."),
            ("Step 08", "Implement WelcomeServlet", "step-08.png", "Author WelcomeServlet to read existing client cookies."),
            ("Step 09", "Iterate Over Request Cookies", "step-09.png", "Retrieve request.getCookies() array and loop through elements."),
            ("Step 10", "Extract Stored Cookie Value", "step-10.png", "Match cookie by key student_user and extract stored username."),
            ("Step 11", "Inspect Browser DevTools Cookies", "step-11.png", "Open DevTools Application > Cookies verifying student_user cookie storage."),
            ("Step 12", "View Welcome Message in Browser", "step-12.png", "Browser renders personalized welcome message using cookie state.")
        ]
    },
    "week-9": {
        "task-1": [
            ("Step 01", "Launch Spring Tool Suite 4", "step-01.png", "Open STS workspace configured with Java 17/21 runtime."),
            ("Step 02", "New Spring Starter Project", "step-02.png", "Open Spring Starter Project wizard in STS."),
            ("Step 03", "Configure Group & Artifact ID", "step-03.png", "Set Group: com.karthik, Artifact: spring-boot-demo, Packaging: Jar."),
            ("Step 04", "Select Java Version", "step-04.png", "Configure Java version 17 and Spring Boot 3.x release."),
            ("Step 05", "Select Spring Web Dependency", "step-05.png", "Select Spring Web dependency providing embedded Tomcat and REST support."),
            ("Step 06", "Inspect Project File Hierarchy", "step-06.png", "STS Package Explorer displays src/main/java and pom.xml."),
            ("Step 07", "Inspect Application Main Class", "step-07.png", "Inspect SpringBootDemoApplication annotated with @SpringBootApplication."),
            ("Step 08", "Configure application.properties", "step-08.png", "Set server.port=8080 and logging levels in application.properties."),
            ("Step 09", "Maven Update Project", "step-09.png", "Execute Maven -> Update Project ensuring all dependencies resolved."),
            ("Step 10", "Run Maven Clean Install", "step-10.png", "Execute Run As -> Maven clean install in STS."),
            ("Step 11", "Verify BUILD SUCCESS Console", "step-11.png", "STS console prints Maven BUILD SUCCESS with 0 test failures."),
            ("Step 12", "Run as Spring Boot App", "step-12.png", "Execute Run As -> Spring Boot App from context menu."),
            ("Step 13", "Inspect Spring Boot Banner", "step-13.png", "Console displays ASCII Spring Boot banner and initialization logs."),
            ("Step 14", "Verify Tomcat Started on 8080", "step-14.png", "Console verifies Tomcat started on port 8080 (http) with context path '/'."),
            ("Step 15", "Browser Verification at localhost:8080", "step-15.png", "Open browser confirming application is live with HTTP 200 response.")
        ],
        "task-2": [
            ("Step 01", "Create Web Controller Package", "step-01.png", "Create package com.karthik.springbootdemo.controller."),
            ("Step 02", "Author HelloController.java", "step-02.png", "Create class annotated with @RestController."),
            ("Step 03", "Implement @GetMapping Method", "step-03.png", "Implement @GetMapping(\"/\") returning personalized welcome message."),
            ("Step 04", "Inject Roll Number 24EU08161", "step-04.png", "Return candidate identity string in HTTP response."),
            ("Step 05", "Implement Parameterized Endpoint", "step-05.png", "Add @GetMapping(\"/greet\") with @RequestParam name binding."),
            ("Step 06", "Save Source Files", "step-06.png", "Save all modified controller classes in STS."),
            ("Step 07", "Spring DevTools Live Reload", "step-07.png", "Automatic application reload via Spring DevTools module."),
            ("Step 08", "Test Root Endpoint in Browser", "step-08.png", "Browser renders welcome message for Venkata Sai Karthikeya Kaja."),
            ("Step 09", "Test Greet Endpoint with Query Param", "step-09.png", "Browser test at localhost:8080/greet?name=Karthik."),
            ("Step 10", "Verify JSON Serialization", "step-10.png", "Inspect Jackson JSON serialization for entity endpoints."),
            ("Step 11", "Inspect STS Access Logs", "step-11.png", "STS console prints HTTP request dispatch and status 200 logs."),
            ("Step 12", "Final Web App Verification", "step-12.png", "Spring Boot web application successfully verified.")
        ],
        "task-3": [
            ("Step 01", "Open POM.xml in STS", "step-01.png", "Open project pom.xml in STS XML editor."),
            ("Step 02", "Inspect Parent Starter POM", "step-02.png", "Verify spring-boot-starter-parent version and configuration inheritance."),
            ("Step 03", "Inspect Project Coordinates", "step-03.png", "Review groupId, artifactId, and version tags."),
            ("Step 04", "Inspect Java Version Property", "step-04.png", "Confirm <java.version>17</java.version> property."),
            ("Step 05", "Inspect spring-boot-starter-web", "step-05.png", "Review web dependency bringing embedded Tomcat and Spring MVC."),
            ("Step 06", "Inspect spring-boot-starter-test", "step-06.png", "Review test dependency scope for JUnit and Mockito."),
            ("Step 07", "Add Spring Boot Maven Plugin", "step-07.png", "Configure spring-boot-maven-plugin for executable fat-JAR packaging."),
            ("Step 08", "Save POM.xml Changes", "step-08.png", "Save POM configuration triggering Maven dependency resolution."),
            ("Step 09", "Inspect Maven Dependencies Tree", "step-09.png", "Review resolved transitive dependencies in Package Explorer."),
            ("Step 10", "Execute Maven Build in STS", "step-10.png", "Run Maven clean package to generate executable JAR archive."),
            ("Step 11", "Verify Generated JAR in target/", "step-11.png", "Confirm spring-boot-demo-0.0.1-SNAPSHOT.jar generated in target/."),
            ("Step 12", "Verify BUILD SUCCESS", "step-12.png", "Console verifies Maven BUILD SUCCESS and dependency tree completeness.")
        ]
    },
    "week-10": {
        "task-1": [
            ("Step 01", "Open STS Workspace", "step-01.png", "Initialize Spring Tool Suite 4 for JdbcTemplate project setup."),
            ("Step 02", "Create Spring Starter Project", "step-02.png", "Create project SpringBootJdbcTemplateH2 in STS wizard."),
            ("Step 03", "Configure Dependencies (JDBC, H2)", "step-03.png", "Add Spring Web, Spring Data JDBC, and In-Memory H2 dependencies."),
            ("Step 04", "Inspect pom.xml Dependencies", "step-04.png", "Verify h2 and spring-boot-starter-jdbc artifacts in pom.xml."),
            ("Step 05", "Configure application.properties", "step-05.png", "Set spring.datasource.url=jdbc:h2:mem:testdb and enable H2 console."),
            ("Step 06", "Implement Author.java Entity", "step-06.png", "Create model class Author with fields: id, name, book."),
            ("Step 07", "Create AuthorService.java", "step-07.png", "Create service class annotated with @Service for business logic."),
            ("Step 08", "Inject JdbcTemplate", "step-08.png", "Inject JdbcTemplate via constructor or @Autowired annotation."),
            ("Step 09", "Implement @PostConstruct Hook", "step-09.png", "Implement lifecycle method to initialize database schema on startup."),
            ("Step 10", "Execute DDL Table Creation", "step-10.png", "Execute jdbcTemplate.execute(\"CREATE TABLE author (...)\")."),
            ("Step 11", "Implement Batch Insert", "step-11.png", "Pre-populate author table with batch update statements."),
            ("Step 12", "Implement Query with RowMapper", "step-12.png", "Query database and map results using RowMapper interface."),
            ("Step 13", "Run Application in STS", "step-13.png", "Launch application as Spring Boot App from STS."),
            ("Step 14", "Inspect SLF4J Console Logs", "step-14.png", "STS console logs verify table creation and batch record insertion."),
            ("Step 15", "Open H2 Web Console in Browser", "step-15.png", "Navigate to http://localhost:8080/h2-console and connect to testdb."),
            ("Step 16", "Execute SQL Query in H2 Console", "step-16.png", "Run SELECT * FROM AUTHOR; verifying stored author records.")
        ]
    },
    "week-11": {
        "task-1": [
            ("Step 01", "Open STS 4 Workspace", "step-01.png", "Initialize Spring Tool Suite 4 for Spring Data JPA project."),
            ("Step 02", "Configure Dependencies (JPA, MySQL)", "step-02.png", "Add Spring Data JPA, MySQL Connector/J, Thymeleaf, and Web dependencies."),
            ("Step 03", "Create MySQL Database employee_db", "step-03.png", "Execute CREATE DATABASE employee_db; in MySQL command client."),
            ("Step 04", "Configure application.properties", "step-04.png", "Configure MySQL URL, credentials, and hibernate.ddl-auto=update."),
            ("Step 05", "Implement Employee.java Entity", "step-05.png", "Create JPA entity with @Entity, @Id, @GeneratedValue, and roll number."),
            ("Step 06", "Create EmployeeRepository Interface", "step-06.png", "Extend JpaRepository<Employee, Long> for automated CRUD operations."),
            ("Step 07", "Implement EmployeeRestController", "step-07.png", "Author @RestController exposing /api/employees JSON endpoints."),
            ("Step 08", "Implement EmployeeViewController", "step-08.png", "Author @Controller routing /employees to Thymeleaf view template."),
            ("Step 09", "Author employees.html Thymeleaf View", "step-09.png", "Create HTML template rendering dynamic employee table using th:each."),
            ("Step 10", "Run Spring Boot App", "step-10.png", "Launch application as Spring Boot App from STS."),
            ("Step 11", "Inspect Hibernate DDL Console Logs", "step-11.png", "Console displays Hibernate automated DDL create table statements."),
            ("Step 12", "Verify Table Schema in MySQL", "step-12.png", "Run DESCRIBE employees; in MySQL verifying generated column types."),
            ("Step 13", "Open Browser Thymeleaf UI", "step-13.png", "Navigate to http://localhost:8080/employees in web browser."),
            ("Step 14", "Verify Formatted Employee Table", "step-14.png", "Browser renders employee records with candidate roll number 24EU08161."),
            ("Step 15", "Test REST JSON Endpoint", "step-15.png", "Navigate to http://localhost:8080/api/employees in browser/Postman."),
            ("Step 16", "Verify REST JSON Array Output", "step-16.png", "Browser confirms serialized JSON array returned by REST API.")
        ]
    },
    "week-12": {
        "task-1": [
            ("Step 01", "Open STS 4 Workspace", "step-01.png", "Initialize Spring Tool Suite 4 for Spring Data JPA with H2."),
            ("Step 02", "Configure Dependencies (JPA, H2)", "step-02.png", "Add Spring Data JPA, H2 In-Memory Database, and Spring Web dependencies."),
            ("Step 03", "Configure application.properties", "step-03.png", "Configure H2 in-memory URL, driver, and enable H2 web console."),
            ("Step 04", "Implement Student.java Entity", "step-04.png", "Create Student entity with @Entity, @Id, rollNo, name, and department."),
            ("Step 05", "Create StudentRepository Interface", "step-05.png", "Extend JpaRepository<Student, Long> inheriting full repository CRUD API."),
            ("Step 06", "Implement StudentController Class", "step-06.png", "Author @RestController exposing student ingestion and retrieval routes."),
            ("Step 07", "Implement @PostMapping Endpoint", "step-07.png", "Create /students/add endpoint binding parameters with @RequestParam."),
            ("Step 08", "Implement @GetMapping Endpoint", "step-08.png", "Create /students/all endpoint returning studentRepository.findAll()."),
            ("Step 09", "Run Spring Boot Application", "step-09.png", "Launch application as Spring Boot App from STS context menu."),
            ("Step 10", "Inspect Console Startup Logs", "step-10.png", "Console verifies embedded Tomcat started on port 8080 with H2."),
            ("Step 11", "Submit Student Record via Browser", "step-11.png", "Submit student record (Roll: 24EU08161, Karthik, IT) via HTTP POST."),
            ("Step 12", "Verify HTTP 200 Confirmation", "step-12.png", "Browser confirms successful entity persistence into in-memory database."),
            ("Step 13", "Retrieve All Students in Browser", "step-13.png", "Navigate to http://localhost:8080/students/all in web browser."),
            ("Step 14", "Verify JSON Array Output", "step-14.png", "Browser displays JSON array containing inserted student 24EU08161."),
            ("Step 15", "Access H2 Web Console", "step-15.png", "Login to http://localhost:8080/h2-console using jdbc:h2:mem:testdb."),
            ("Step 16", "Query Student Table in H2", "step-16.png", "Execute SELECT * FROM STUDENT; verifying database persistence.")
        ]
    },
    "week-13": {
        "task-1": [
            ("Step 01", "Open STS 4 Workspace", "step-01.png", "Initialize Spring Tool Suite 4 for derived and custom query implementation."),
            ("Step 02", "Configure Dependencies", "step-02.png", "Add Spring Data JPA, H2 Database, and Spring Web dependencies."),
            ("Step 03", "Implement Student Entity", "step-03.png", "Define Student entity with firstName, lastName, and rollNumber."),
            ("Step 04", "Open StudentRepository Interface", "step-04.png", "Prepare repository interface extending JpaRepository for query methods."),
            ("Step 05", "Declare findByFirstName Query", "step-05.png", "Declare derived query method List<Student> findByFirstName(String fn)."),
            ("Step 06", "Declare OrderBy Derived Query", "step-06.png", "Declare findByLastNameOrderByFirstNameAsc(String ln) query method."),
            ("Step 07", "Declare Compound AND Query", "step-07.png", "Declare findByFirstNameAndLastName(String fn, String ln) query method."),
            ("Step 08", "Declare Compound OR Query", "step-08.png", "Declare findByFirstNameOrLastName(String fn, String ln) query method."),
            ("Step 09", "Declare Custom JPQL @Query", "step-09.png", "Declare @Query(\"SELECT s FROM Student s WHERE s.rollNumber = :roll\")."),
            ("Step 10", "Declare Native SQL @Query", "step-10.png", "Declare @Query(value = \"SELECT * FROM student WHERE first_name = :fn\", nativeQuery = true)."),
            ("Step 11", "Implement QueryController", "step-11.png", "Expose REST endpoints for each derived and custom query method."),
            ("Step 12", "Run Application & Preload Data", "step-12.png", "Launch application in STS and insert test student records into database."),
            ("Step 13", "Test findByFirstName in Browser", "step-13.png", "Test /students/find?firstName=Karthik verifying single field query result."),
            ("Step 14", "Test OrderBy Query in Browser", "step-14.png", "Test /students/order?lastName=Kaja verifying sorted alphabetical result."),
            ("Step 15", "Test Compound Queries in Browser", "step-15.png", "Test compound AND / OR queries verifying multi-field filter results."),
            ("Step 16", "Test Native SQL Query in Browser", "step-16.png", "Test /students/native?fn=Karthik verifying native query output."),
            ("Step 17", "Inspect Hibernate SQL in Console", "step-17.png", "STS console logs display automated translation of method names to SQL."),
            ("Step 18", "Verify Execution Metrics", "step-18.png", "Verify query execution metrics and clean database connection cleanup.")
        ]
    }
}

