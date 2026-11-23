# -*- coding: utf-8 -*-
"""
Generator for all 14 Week Pages (Week 0 to Week 13)
Advanced Java Programming Lab (24IT385)
Student: Venkata Sai Karthikeya Kaja (24EU08161)
"""

import os

pages_dir = r'C:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\pages'
os.makedirs(pages_dir, exist_ok=True)

WEEKS_META = [
    {
        "num": 0,
        "slug": "week-0",
        "title": "Advanced Java Introduction and Theory",
        "subtitle": "Core Java vs Advanced Java, Applets, Servlets, JDBC, Cookies, Sessions & Spring Boot",
        "category": "Core & Theory",
        "pills": ["☕ Core vs Advanced", "🌐 Servlets & Applets", "🔌 JDBC & ODBC", "🍪 Cookies & Sessions", "🌱 Spring Boot Architecture"],
        "aim": "To comprehend the foundational concepts, enterprise evolution, and architectural distinctions of Java technologies, contrasting Core Java with enterprise web frameworks, distributed architectures, and state management mechanisms.",
        "intro": "Advanced Java extends the object-oriented foundation of Core Java to provide enterprise-grade capabilities for distributed, web-based, and multi-tier application development. While Core Java focuses on standalone desktop computing, memory management, multithreading, and standard I/O, Advanced Java encompasses server-side technologies including Servlets, JSP, JDBC, enterprise security, and contemporary microservice architectures with Spring Boot.",
        "reqs": {
            "hw": ["Processor: Intel Core i3 / i5 or higher", "RAM: 4 GB minimum", "Storage: 500 MB free space"],
            "sw": ["OS: Ubuntu Linux / Windows 10/11", "JDK: Java SE 8+ / OpenJDK 21", "Browser: Chrome / Firefox", "Documentation: Week_0.odt / Task-1 Syllabus"]
        }
    },
    {
        "num": 1,
        "slug": "week-1",
        "title": "Advanced Java Lab Task 1: Programming Language Comparative Analysis",
        "subtitle": "20-Parameter Architectural Comparison of Java, C, C++, Python, and JavaScript",
        "category": "Core & Theory",
        "pills": ["📊 20-Parameter Matrix", "⚡ 5 Major Languages", "🎯 Domain Suitability", "🏆 Architectural Synthesis"],
        "aim": "To conduct an in-depth comparative analysis of five foundational programming languages (Java, C, C++, Python, JavaScript) across twenty standardized architectural, runtime, and ecosystem criteria, evaluating their specific domain suitability.",
        "intro": "Modern software engineering demands precise language selection based on memory constraints, execution models, platform requirements, and concurrency semantics. This study compares Java (managed bytecode on JVM), C (compiled procedural systems language), C++ (zero-cost abstraction multi-paradigm language), Python (interpreted dynamic high-level language), and JavaScript (event-driven asynchronous browser/server runtime).",
        "reqs": {
            "hw": ["Processor: Intel Core i3 / i5 or AMD Ryzen", "RAM: 4 GB minimum", "Display: 1080p resolution"],
            "sw": ["OS: Cross-platform (Windows / Linux)", "Official Specs: ISO C/C++, Java SE 25/26, ECMAScript 2026, Python 3.14", "Documentation: Lab 1.docx & Task-1 Report"]
        }
    },
    {
        "num": 2,
        "slug": "week-2",
        "title": "Java Development Environment Setup",
        "subtitle": "Downloading, Installing and Configuring OpenJDK and Oracle JDK SE 26 in Ubuntu",
        "category": "Environment & Setup",
        "pills": ["🐧 Ubuntu Linux", "☕ OpenJDK / Oracle JDK 26", "⚙️ update-alternatives", "💻 ~/.bashrc & JAVA_HOME"],
        "aim": "To download, extract, install, and configure OpenJDK and Oracle JDK SE 26 on an Ubuntu Linux system, register Java and Javac binaries with update-alternatives, and establish system-wide environment variables.",
        "intro": "A standardized Java Development Kit (JDK) setup on Linux is essential for enterprise server software. Modern production environments utilize OpenJDK LTS or latest feature releases deployed into /opt/. System registration through update-alternatives allows seamless switching between multiple runtime environments, while JAVA_HOME and PATH exports in ~/.bashrc ensure CLI build tools (Maven, Gradle) function reliably.",
        "reqs": {
            "hw": ["Processor: 64-bit x86_64 architecture", "RAM: 4 GB minimum", "Disk: 2 GB free in /opt/ and /home"],
            "sw": ["OS: Ubuntu 22.04 LTS / Linux Mint", "Archive: openjdk-26*_bin.tar.gz", "Shell: GNU Bash / zsh", "Privileges: Sudo / Root"]
        }
    },
    {
        "num": 3,
        "slug": "week-3",
        "title": "Java MS Access Database Connectivity",
        "subtitle": "Java MS Access Connectivity Using UCanAccess Pure Java JDBC Driver",
        "category": "JDBC & Databases",
        "pills": ["🗂️ MS Access (.accdb)", "🔌 UCanAccess 5.1.3", "☕ AccessDemo.java", "🐧 Terminal Execution"],
        "aim": "To write, compile, and execute a Java program (AccessDemo.java) to connect to a Microsoft Access database (StudentDB.accdb) on Linux using the pure Java UCanAccess JDBC driver without Windows DSN dependencies.",
        "intro": "Traditional Microsoft Access connectivity relied on the Type-1 JDBC-ODBC Bridge, which was deprecated in Java 8 and completely removed in Java 9. UCanAccess is a pure Java (Type-4 style) JDBC driver architecture leveraging Jackcess and HSQLDB to read and manipulate MS Access (.mdb and .accdb) files directly across all operating systems without native Windows ODBC drivers.",
        "reqs": {
            "hw": ["Processor: Intel Core i3 / i5 or higher", "RAM: 4 GB minimum", "Storage: 300 MB free space"],
            "sw": ["OS: Ubuntu Linux / Windows", "JDK: Java SE 8+ / OpenJDK 21", "Driver: ucanaccess-5.1.3.jar & dependencies (jackcess, hsqldb, commons-lang3, commons-logging)", "Database File: StudentDB.accdb"]
        }
    },
    {
        "num": 4,
        "slug": "week-4",
        "title": "Remote MySQL Database Connectivity",
        "subtitle": "Remote MySQL Database Connectivity and Employee Record Insertion",
        "category": "JDBC & Databases",
        "pills": ["🐬 Remote MySQL (10.0.9.20:3306)", "🗄️ Database: ai", "📦 Package: javaapplication59", "📝 Class: JavaApplication59"],
        "aim": "To develop and execute a Java JDBC program to connect to a remote MySQL database server over TCP/IP (10.0.9.20:3306/ai), create a statement, insert an employee record ('9', 'Karthik'), and display updated records.",
        "intro": "In enterprise client-server applications, databases reside on dedicated remote database hosts. Java Database Connectivity (JDBC) Type-4 network drivers communicate directly with the remote database server via socket connections over port 3306 without requiring local client installations. This experiment demonstrates opening a remote socket connection, executing DML statements, and reading the resulting tabular stream.",
        "reqs": {
            "hw": ["Processor: Intel Core i3 or equivalent", "RAM: 4 GB", "Network: LAN / Wi-Fi connected to 10.0.9.20"],
            "sw": ["IDE: NetBeans IDE 8.2 / STS", "JDK: Java SE 8+ / OpenJDK", "RDBMS: MySQL Server running at 10.0.9.20:3306", "Driver: mysql-connector-java.jar"]
        }
    },
    {
        "num": 5,
        "slug": "week-5",
        "title": "Remote MySQL Database Operations",
        "subtitle": "Remote MySQL Database Operations (Update, Delete, Verification & Disconnect)",
        "category": "JDBC & Databases",
        "pills": ["🐬 Remote MySQL (10.0.9.20:3306)", "🔄 Record Update & Delete", "🔒 Lifecycle Management", "✅ BUILD SUCCESSFUL"],
        "aim": "To execute comprehensive update and delete operations on a remote MySQL database over JDBC, verify relational state changes at each execution milestone, and ensure proper database resource closing.",
        "intro": "Building upon initial remote connectivity, robust database programming requires transactional manipulation (updating existing records and deleting obsolete entries) combined with strict resource lifecycle management. Closing ResultSets, Statements, and Connection sockets prevents database server connection pool starvation and socket leaks in networked enterprise environments.",
        "reqs": {
            "hw": ["Processor: Intel Core i3 / i5", "RAM: 4 GB", "Network: TCP/IP connectivity to 10.0.9.20:3306"],
            "sw": ["IDE: NetBeans IDE 8.2 / STS", "JDK: Java SE 8+ / OpenJDK", "RDBMS: MySQL Server (Database: ai)", "Driver: mysql-connector-java.jar"]
        }
    },
    {
        "num": 6,
        "slug": "week-6",
        "title": "JDBC CRUD Operations",
        "subtitle": "JDBC Program to Perform Complete CRUD Operations on Student Database",
        "category": "JDBC & Databases",
        "pills": ["🐬 MySQL Database: it", "📋 Table: Student", "🔄 CRUD: INSERT, SELECT, UPDATE, DELETE", "☕ StudentCRUD.java"],
        "aim": "To write and execute a Java JDBC program (StudentCRUD.java) to perform complete Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE) operations on the Student table in MySQL database it.",
        "intro": "CRUD operations represent the four fundamental primitives of persistent storage in relational databases. JDBC provides java.sql.Statement and executeUpdate() for DML operations (INSERT, UPDATE, DELETE) which return the number of affected rows, and executeQuery() for DQL (SELECT) queries returning a scrollable, cursor-based java.sql.ResultSet.",
        "reqs": {
            "hw": ["Processor: Intel Core i3 / i5 or higher", "RAM: 4 GB", "Storage: 500 MB free space"],
            "sw": ["OS: Windows 10/11 / Linux", "IDE: NetBeans IDE 8.2", "JDK: Java SE 8+", "RDBMS: MySQL Server 8.0 (Port 3306)", "Driver: com.mysql.jdbc.Driver"]
        }
    },
    {
        "num": 7,
        "slug": "week-7",
        "title": "Generic Servlet and HTTP Servlet",
        "subtitle": "Implementation of Generic Servlet and HTTP Servlet Using NetBeans and Apache Tomcat",
        "category": "Servlets & Web",
        "pills": ["☕ NetBeans IDE 8.2", "🐱 Apache Tomcat Server", "🌐 GenericServlet & HttpServlet", "👨‍🎓 Student Details Display"],
        "aim": "To create a Java Web Application in NetBeans IDE 8.2, configure Apache Tomcat Server, and implement both GenericServlet and HttpServlet to dynamically display student details (Roll Number: 24EU08161) through a web browser.",
        "intro": "Servlets are server-side Java components that handle client requests and generate dynamic web pages. javax.servlet.GenericServlet provides a protocol-independent servlet implementation requiring developers to override the service() method. In contrast, javax.servlet.http.HttpServlet extends GenericServlet specifically for the HTTP protocol, offering request-specific handlers such as doGet() and doPost().",
        "reqs": {
            "hw": ["Processor: Intel Core i3 / i5", "RAM: 4 GB minimum", "Storage: 1 GB free space"],
            "sw": ["IDE: NetBeans IDE 8.2 with Java EE", "Server: Apache Tomcat 8.x / 9.x", "JDK: Java SE 8+", "Browser: Internet Explorer / Chrome", "OS: Windows / Linux"]
        }
    },
    {
        "num": 8,
        "slug": "week-8",
        "title": "Advanced Java Web Applications",
        "subtitle": "Student Management System, Cookies, Sessions & Integrated Authenticated Application",
        "category": "Servlets & Web",
        "pills": ["🐱 Apache Tomcat 9.0", "🐬 MySQL studentdb", "🍪 javax.servlet.http.Cookie", "🔒 HttpSession Security", "📦 Full CRUD Web Tier"],
        "aim": "To develop a comprehensive suite of enterprise Java Web applications utilizing Java Servlets, JDBC, and MySQL: building a full-featured Student Management System, demonstrating client-side Cookie state tracking, implementing server-side HttpSession management, and architecting an integrated authenticated web portal.",
        "intro": "HTTP is fundamentally a stateless protocol; web servers treat each HTTP request as an independent interaction without retaining user identity. To maintain conversational state across multiple page views, Java Servlets provide client-side Cookies (transmitted via HTTP headers) and server-side HttpSession objects (retained in servlet container memory). Coupling state management with JDBC persistence creates secure, multi-user web portals.",
        "reqs": {
            "hw": ["Processor: Intel Core i5 or AMD Ryzen", "RAM: 8 GB recommended", "Storage: 2 GB free disk space"],
            "sw": ["IDE: NetBeans IDE 8.2", "Web Server: Apache Tomcat 9.0.120", "JDK: Java SE 8", "Database: MySQL Server 8.0 & MySQL Workbench", "Connector: mysql-connector-j-8.0.33.jar"]
        }
    },
    {
        "num": 9,
        "slug": "week-9",
        "title": "Maven and Spring Boot Development",
        "subtitle": "Maven Project Lifecycle, Spring Boot Web REST Services & POM.xml Configuration",
        "category": "Spring Boot & JPA",
        "pills": ["🍃 Spring Tool Suite 4 (STS)", "📦 Apache Maven 3.x", "🌱 Spring Boot 3.3.5", "📄 POM.xml Dependencies", "🌐 REST Endpoints"],
        "aim": "To master the Apache Maven project build lifecycle in Spring Tool Suite (STS), construct standalone Spring Boot web applications, configure dependencies and build plugins in pom.xml, execute clean install builds, and verify REST endpoints in a web browser.",
        "intro": "Apache Maven is the industry-standard software project management and build automation tool for Java. It utilizes a Project Object Model (POM.xml) to declare dependencies, transitive artifact resolution, and build lifecycles. Spring Boot revolutionized enterprise Java by introducing opinionated starter dependencies, automated classpath configuration, and embedded servlet containers (Tomcat), enabling developers to run production-ready web services with minimal boilerplate.",
        "reqs": {
            "hw": ["Processor: Intel Core i5 / AMD Ryzen 5", "RAM: 8 GB minimum (16 GB recommended)", "Storage: 5 GB free disk space"],
            "sw": ["IDE: Spring Tool Suite 4 (STS 4.41.0+)", "JDK: Eclipse Adoptium JDK 17 / OpenJDK 17 LTS", "Build Tool: Apache Maven (embedded in STS)", "Web Client: Google Chrome / Edge"]
        }
    },
    {
        "num": 10,
        "slug": "week-10",
        "title": "Spring Boot JdbcTemplate with In-Memory H2 Database",
        "subtitle": "Spring Boot Database Connectivity Using JdbcTemplate with In-Memory Database (H2)",
        "category": "Spring Boot & JPA",
        "pills": ["🌱 Spring Boot 3.2.x", "⚡ Spring JdbcTemplate", "🗄️ In-Memory H2 Engine", "🖥️ H2 Web Console (Port 83)", "📝 RowMapper Lambdas"],
        "aim": "To design, develop, and validate a database-driven Spring Boot application utilizing Spring JdbcTemplate to connect to an embedded in-memory H2 database, automatically create tables, perform batch data insertions, execute SQL queries using RowMapper lambdas, and verify live database state via the H2 Web Console.",
        "intro": "Traditional JDBC requires extensive boilerplate code for connection acquisition, statement preparation, result set iteration, and checked exception handling. Spring Framework's JdbcTemplate abstracts these repetitive chores, automating resource disposal and translating vendor-specific SQLExceptions into Spring's portable DataAccessException hierarchy. Paired with in-memory H2, it delivers an ultra-fast execution environment ideal for rapid testing.",
        "reqs": {
            "hw": ["Processor: 64-bit multi-core CPU", "RAM: 8 GB minimum", "Storage: 2 GB free disk space"],
            "sw": ["OS: Microsoft Windows 11 Enterprise (64-bit) / Linux", "Java Platform: OpenJDK 21.0.11 LTS 64-Bit", "IDE: Spring Tool Suite 4 (STS 4.41.0)", "Framework: Spring Boot 3.2.x", "Database: H2 Database Engine 2.2.x", "Client: Google Chrome"]
        }
    },
    {
        "num": 11,
        "slug": "week-11",
        "title": "Spring Boot JPA Application with Relational Database (MySQL) and Web Interface",
        "subtitle": "Spring Boot JPA Application with Relational Database (MySQL) and Web Interface",
        "category": "Spring Boot & JPA",
        "pills": ["🐬 MySQL 8.0 Server (Port 3306)", "🍃 Spring Data JPA & Hibernate", "🚀 Dual Controllers (REST & View)", "🎨 Server-Side Thymeleaf", "📋 Employee Entity ORM"],
        "aim": "To design, develop, and deploy an enterprise Spring Boot application connecting to an external MySQL relational database using Spring Data JPA and Hibernate, implement Object-Relational Mapping (ORM) for an Employee entity, and provide dual client interfaces: a RESTful JSON API and a server-side rendered Thymeleaf HTML web page.",
        "intro": "Object-Relational Mapping (ORM) bridges the fundamental impedance mismatch between Java's object-oriented paradigm and SQL's relational tables. Spring Data JPA dramatically simplifies database interactions by generating dynamic repository proxies at runtime for interfaces extending JpaRepository<T, ID>. In this architecture, a dual-controller setup demonstrates serving both programmatic API consumers (via @RestController returning JSON) and human web users (via @Controller rendering Thymeleaf templates).",
        "reqs": {
            "hw": ["Processor: Intel Core i5 / AMD Ryzen", "RAM: 8 GB minimum", "Storage: 3 GB free disk space"],
            "sw": ["OS: Windows 11 Enterprise (64-bit) / Linux", "Java Platform: JDK 21.0.11 LTS", "IDE: Spring Tool Suite 4 (STS 4.41.0)", "RDBMS: MySQL Server 8.0.36 & Workbench 8.0 CE", "Driver: MySQL Connector/J 8.0.33", "Framework: Spring Boot 3.2.x (Data JPA, Web, Thymeleaf)"]
        }
    },
    {
        "num": 12,
        "slug": "week-12",
        "title": "Spring Data JPA Repository Operations with In-Memory H2 Database",
        "subtitle": "Spring Data JPA Repository Operations with In-Memory H2 Database",
        "category": "Spring Boot & JPA",
        "pills": ["🗄️ In-Memory H2 Engine", "🍃 JpaRepository<Student, Long>", "🌐 Browser GET Endpoints", "🖥️ H2 Web Console Verification", "📦 Zero-Boilerplate ORM"],
        "aim": "To implement, configure, and evaluate Spring Data JPA repository operations on a Student entity using an in-memory H2 database, establish browser-accessible HTTP GET endpoints to perform record insertion and retrieval without external testing utilities, and verify database state via the H2 Console.",
        "intro": "Spring Data JPA introduces powerful repository proxy generation, where declaring an interface extending JpaRepository<Student, Long> automatically equips developers with standard CRUD operations (save, findAll, findById, delete, count) without writing a single line of SQL or DAO implementation code. To facilitate immediate classroom validation without Postman, this experiment maps GET endpoints with @RequestParam to trigger repository mutations directly from browser URLs.",
        "reqs": {
            "hw": ["Processor: 64-bit multi-core CPU", "RAM: 8 GB minimum", "Storage: 2 GB free disk space"],
            "sw": ["OS: Microsoft Windows 11 Enterprise (64-bit) / Linux", "Java Platform: OpenJDK 21.0.11 LTS", "IDE: Spring Tool Suite 4 (STS 4.41.0)", "Framework: Spring Boot 3.2.x (Spring Web, Spring Data JPA, H2 Database)", "Client: Google Chrome Browser"]
        }
    },
    {
        "num": 13,
        "slug": "week-13",
        "title": "Implementation of Derived and Custom Query Methods in Spring Data JPA",
        "subtitle": "Implementation of Derived and Custom Query Methods in Spring Data JPA",
        "category": "Spring Boot & JPA",
        "pills": ["🔍 8 Query Methods", "🧩 Query Derivation AST", "⚡ Custom @Query (Native SQL)", "📊 Hibernate SQL Telemetry", "🎯 Predicate Conjunctions"],
        "aim": "To design, declare, implement, and validate specialized derived query methods and custom queries utilizing the @Query annotation (both JPQL and Native SQL) in Spring Data JPA repository interfaces for a Student entity, and observe runtime SQL generation and result sets.",
        "intro": "One of the most powerful features of Spring Data JPA is its query derivation mechanism. By parsing repository method names according to structured naming conventions (findBy..., ...And..., ...Or..., ...OrderBy...), Spring Data automatically constructs Abstract Syntax Trees (AST) that translate into JPQL and optimized native SQL queries at runtime. When requirements demand complex queries, the @Query annotation enables explicit JPQL or raw native SQL execution.",
        "reqs": {
            "hw": ["Processor: 64-bit multi-core CPU", "RAM: 8 GB minimum", "Storage: 3 GB free disk space"],
            "sw": ["OS: Microsoft Windows 11 Enterprise (64-bit) / Linux", "Java Platform: OpenJDK 21.0.11 LTS", "IDE: Spring Tool Suite 4 (STS 4.41.0)", "Framework: Spring Boot 3.2.x, Spring Data JPA, Hibernate 6.x", "Database: H2 In-Memory / MySQL", "Client: Google Chrome Browser"]
        }
    }
]

print("Metadata defined successfully for all 14 weeks!")

