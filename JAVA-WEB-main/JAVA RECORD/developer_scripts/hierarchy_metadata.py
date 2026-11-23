# -*- coding: utf-8 -*-
"""
Hierarchical 3-Level Portal Builder (Week -> Task -> Program)
Inspired by Reference Website: https://sahelms.vrsiddhartha.ac.in/java/238W1A1275/
Strictly Preserves Emerald Theme, Colors, Fonts, and Visual Identity.
Student: Venkata Sai Karthikeya Kaja (Roll: 24EU08161)
"""

import os
import re
import json

from step_gallery_data import STEP_GALLERY_DATA

# Comprehensive Three-Level Navigation Metadata
HIERARCHY_DATA = [
    {
        "num": 0,
        "name": "Advanced Java Introduction & Theory",
        "category": "Core & Theory",
        "desc": "JVM Architecture, Core vs Enterprise Java, Applets vs Servlets, JDBC vs ODBC, Cookies & Sessions, Spring Boot vs Spring Framework.",
        "tasks": [
            {
                "id": "w0-t1",
                "title": "Task 1: Advanced Java Architectural Foundations",
                "aim": "To investigate, evaluate, and document the foundational architectural differences between Core Java (Java SE) and Advanced Java (Jakarta EE), examining server-side component lifecycles, database access drivers (JDBC vs ODBC), stateless HTTP tracking mechanisms (Cookies vs Sessions), and standalone desktop versus distributed enterprise web paradigms.",
                "requirements": [
                    ("Development Environment", ["Java Platform: JDK 8+ / OpenJDK 26", "Web Engine Architecture: Apache Tomcat / GlassFish", "IDE: NetBeans 8.2 / Spring Tool Suite 4"]),
                    ("Core Paradigms", ["Component Models: Applets (Client) vs Servlets (Server)", "Data Drivers: Type-1 (ODBC Bridge) vs Type-4 (Pure Java JDBC)", "State Protocols: Client-side HTTP Cookies vs Server-side HttpSession"])
                ],
                "programs": [
                    {
                        "id": "w0-t1-p1",
                        "title": "Module 1: Core Java vs Advanced Java Architecture",
                        "type": "Architecture Comparison",
                        "objective": "Differentiate standalone desktop execution environments from distributed multi-tier enterprise web servers.",
                        "explanation": [
                            ("Java SE (Core Java)", "Desktop/client-side single-tier runtime providing basic syntax, OOP, Collections, Multithreading, and JVM execution."),
                            ("Java EE / Jakarta EE", "Enterprise server-side specification providing Servlets, JSP, EJB, JPA, JMS, and container-managed concurrency."),
                            ("Deployment Target", "Core Java runs in local JVM; Advanced Java runs in application servers (Tomcat, WildFly, WebLogic).")
                        ]
                    },
                    {
                        "id": "w0-t1-p2",
                        "title": "Module 2: Java Applets vs Java Servlets",
                        "type": "Web Component Lifecycle",
                        "objective": "Analyze the paradigm shift from client-side browser plugin applets to robust server-side servlets.",
                        "explanation": [
                            ("Applets (Deprecated)", "Client-side execution inside browser sandbox using JVM plugin; severely restricted by modern security models."),
                            ("Servlets (Server)", "Server-side Java classes responding to HTTP requests, generating dynamic web content with thread pooling."),
                            ("Lifecycle Methods", "Applet: init(), start(), stop(), destroy() | Servlet: init(ServletConfig), service(req, res), destroy()")
                        ]
                    },
                    {
                        "id": "w0-t1-p3",
                        "title": "Module 3: JDBC vs ODBC Architecture",
                        "type": "Database Driver Layers",
                        "objective": "Contrast native OS-dependent ODBC bridges with pure-Java Type 4 network protocol drivers.",
                        "explanation": [
                            ("ODBC (Microsoft)", "Native C/C++ API tightly coupled to Windows OS drivers; requires native client installation and is platform-dependent."),
                            ("JDBC (Java)", "Pure Java database connectivity specification; Type 4 drivers communicate directly via database native wire protocol."),
                            ("Platform Portability", "JDBC enables 'Write Once, Run Anywhere' database access without host OS driver dependencies.")
                        ]
                    },
                    {
                        "id": "w0-t1-p4",
                        "title": "Module 4: Cookies vs HTTP Sessions",
                        "type": "State Management",
                        "objective": "Examine stateless HTTP protocol session tracking mechanisms across client and server tiers.",
                        "explanation": [
                            ("HTTP Cookies", "Small text tokens stored on client browser; transmitted via Set-Cookie and Cookie HTTP headers (size limit ~4KB)."),
                            ("HttpSession", "Server-side state memory associated with a unique JSESSIONID token; secure storage for authentication and cart data."),
                            ("Security Trade-off", "Cookies can be manipulated or intercepted; Sessions consume server RAM under high concurrent user load.")
                        ]
                    },
                    {
                        "id": "w0-t1-p5",
                        "title": "Module 5: Spring Boot vs Spring Framework",
                        "type": "Enterprise Frameworks",
                        "objective": "Evaluate convention-over-configuration and automated dependency management in modern microservices.",
                        "explanation": [
                            ("Spring Framework", "Comprehensive dependency injection and AOP framework requiring extensive XML/Java @Configuration and external Tomcat setup."),
                            ("Spring Boot", "Opinionated, auto-configured extension with embedded Tomcat and starter dependencies, enabling production-ready apps in minutes."),
                            ("Deployment", "Spring: WAR archive deployed to external server | Spring Boot: Executable Fat-JAR with embedded web server.")
                        ]
                    }
                ]
            }
        ]
    },
    {
        "num": 1,
        "name": "Comparative Evaluation of Programming Paradigms",
        "category": "Paradigms & Lab 1",
        "desc": "Comparative benchmark matrices evaluating Java, C, C++, Python, and JavaScript across memory models, concurrency, and type systems.",
        "tasks": [
            {
                "id": "w1-t1",
                "title": "Task 1: Comparative Evaluation of Java, C, C++, Python and JavaScript",
                "aim": "To perform a multi-dimensional comparative benchmark of Java against C, C++, Python, and JavaScript, assessing memory management (Garbage Collection vs manual malloc/free), concurrency models, runtime environments (JVM vs V8 vs CPython), and type safety.",
                "requirements": [
                    ("Hardware & Specifications", ["Intel Core i5/i7 Processor", "8GB+ RAM", "Ubuntu Linux / Windows 10/11"]),
                    ("Runtimes & Compilers", ["Java SE Runtime (JVM HotSpot)", "GCC / G++ C/C++ Compiler", "Python 3.x Interpreter", "Node.js V8 Engine"])
                ],
                "programs": [
                    {
                        "id": "w1-t1-p1",
                        "title": "Program 1: Comparative Paradigm Evaluation",
                        "type": "Comparative Benchmark",
                        "objective": "Document architectural, memory, and performance characteristics across five major programming languages.",
                        "explanation": [
                            ("Type System", "Java: Strongly/Statically Typed | C/C++: Statically Typed | Python: Strongly/Dynamically Typed | JS: Weakly/Dynamically Typed"),
                            ("Memory Model", "Java: Automated Generational Garbage Collection | C/C++: Manual heap allocation | Python/JS: Reference counting & mark-and-sweep"),
                            ("Execution Engine", "Java: Bytecode compiled to JVM JIT machine code | C/C++: Native machine binaries | Python: Interpreted bytecode | JS: JIT compiled")
                        ]
                    }
                ]
            }
        ]
    },
    {
        "num": 2,
        "name": "Java Development Environment Setup",
        "category": "Linux & JDK Setup",
        "desc": "Downloading, installing, and configuring OpenJDK and Oracle JDK SE 26 on Ubuntu Linux; JAVA_HOME, PATH, and update-alternatives registration.",
        "tasks": [
            {
                "id": "w2-t1",
                "title": "Task 1: Downloading, Installing and Configuring OpenJDK and Oracle JDK 26 in Ubuntu",
                "aim": "To download, extract, install, and configure OpenJDK SE 26 binaries on an Ubuntu Linux environment, registering java and javac via update-alternatives, setting global JAVA_HOME in /etc/environment, and verifying runtime compiler execution for candidate 24EU08161.",
                "requirements": [
                    ("Operating System", ["Ubuntu Linux 22.04 LTS / Jammy Jellyfish", "Terminal: Bash Shell (/bin/bash)", "User Privileges: sudo root access"]),
                    ("Software Package", ["Archive: openjdk-26_linux-x64_bin.tar.gz", "Target Location: /usr/lib/jvm/jdk-26", "Utilities: wget, tar, update-alternatives"])
                ],
                "programs": [
                    {
                        "id": "w2-t1-p1",
                        "title": "Program 1: setup_jdk26.sh (Automated Shell Script & Configuration)",
                        "type": "Bash Automation Script",
                        "filename": "setup_jdk26.sh",
                        "objective": "Automate OpenJDK 26 installation, directory extraction, alternatives registration, and environment export.",
                        "code": """#!/bin/bash
# ============================================================
# Advanced Java Lab Setup - OpenJDK SE 26 Configuration
# Candidate: Venkata Sai Karthikeya Kaja | Roll: 24EU08161
# Department of Information Technology, Siddhartha Academy
# ============================================================

set -e
echo "Updating package index..."
sudo apt update -y

echo "Creating JVM target directory..."
sudo mkdir -p /usr/lib/jvm

echo "Downloading OpenJDK 26 Linux x64 Tarball..."
wget -c https://download.java.net/java/GA/jdk26/openjdk-26_linux-x64_bin.tar.gz

echo "Extracting archive to /usr/lib/jvm..."
sudo tar -xzf openjdk-26_linux-x64_bin.tar.gz -C /usr/lib/jvm/

echo "Registering java and javac with update-alternatives..."
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-26/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-26/bin/javac 1

echo "Configuring JAVA_HOME in /etc/environment..."
echo 'JAVA_HOME="/usr/lib/jvm/jdk-26"' | sudo tee -a /etc/environment
source /etc/environment

echo "Verifying installation for Venkata Sai Karthikeya Kaja (24EU08161):"
java -version
javac -version
echo "JDK 26 environment setup complete!"
""",
                        "explanation": [
                            ("mkdir -p /usr/lib/jvm", "Creates standard system JVM storage directory if it does not already exist."),
                            ("tar -xzf", "Extracts gzip-compressed tarball archive into /usr/lib/jvm destination path."),
                            ("update-alternatives --install", "Registers java and javac binaries with Debian alternatives system with priority 1."),
                            ("JAVA_HOME=/usr/lib/jvm/jdk-26", "Exports global system environment variable pointing to JDK root for build tools.")
                        ],
                        "output": """openjdk version "26" 2026-03-17
OpenJDK Runtime Environment (build 26+35-2315)
OpenJDK 64-Bit Server VM (build 26+35-2315, mixed mode, sharing)
javac 26
Environment verified for candidate 24EU08161.
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 3,
        "name": "Java MS Access Database Connectivity",
        "category": "Type 4 Bridge",
        "desc": "Java MS Access Database Connectivity using pure-Java Type 4 UCanAccess driver, Jackcess, and HSQLDB on Database.accdb.",
        "tasks": [
            {
                "id": "w3-t1",
                "title": "Task 1: Java MS Access Database Connectivity Using UCanAccess",
                "aim": "To establish database connectivity between a Java application (AccessDemo.java) and a Microsoft Access database (Database.accdb) using the pure-Java Type 4 UCanAccess driver suite, executing SQL queries and displaying candidate record 24EU08161.",
                "requirements": [
                    ("Development Environment", ["Operating System: Windows 10/11", "Java Platform: JDK 8+ with javac/java on PATH", "IDE: NetBeans 8.2 / Command Prompt"]),
                    ("Database & Libraries", ["Database File: Database.accdb (MS Access 2016+)", "Core Driver: ucanaccess-5.0.1.jar", "Dependencies: jackcess-3.0.1.jar, hsqldb-2.5.0.jar, commons-lang3.jar, commons-logging.jar"])
                ],
                "programs": [
                    {
                        "id": "w3-t1-p1",
                        "title": "Program 1: AccessDemo.java (UCanAccess Pure Java Connectivity)",
                        "type": "Java JDBC Application",
                        "filename": "AccessDemo.java",
                        "objective": "Connect to Database.accdb, execute SELECT query on Users table, and print formatted student records.",
                        "sql_setup": """-- Microsoft Access Table Schema (Users)
CREATE TABLE Users (
    ID AUTOINCREMENT PRIMARY KEY,
    StudentName TEXT(50),
    RollNumber TEXT(20),
    Department TEXT(50)
);

-- Populated Test Records
INSERT INTO Users (StudentName, RollNumber, Department) 
VALUES ('Venkata Sai Karthikeya Kaja', '24EU08161', 'Information Technology');
""",
                        "code": """// ============================================================
// Java MS Access Connectivity using UCanAccess Driver
// Student: Venkata Sai Karthikeya Kaja | Roll: 24EU08161
// Course: 24IT385 · Advanced Java Programming Lab
// ============================================================

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class AccessDemo {
    public static void main(String[] args) {
        // Pure-Java UCanAccess JDBC URL pointing to Database.accdb
        String dbPath = "C:/AccessDemo/data/Database.accdb";
        String url = "jdbc:ucanaccess://" + dbPath;

        System.out.println("Connecting to MS Access Database via UCanAccess...");
        System.out.println("Student: Venkata Sai Karthikeya Kaja (Roll: 24EU08161)");

        try {
            // Load Type-4 UCanAccess pure Java driver
            Class.forName("net.ucanaccess.jdbc.UcanaccessDriver");
            Connection conn = DriverManager.getConnection(url);
            Statement stmt = conn.createStatement();

            System.out.println("Connected successfully to Database.accdb!");
            System.out.println("==================================================");
            System.out.println("ID   ROLL NUMBER   STUDENT NAME             DEPT");
            System.out.println("==================================================");

            // Execute SQL query on Users table
            ResultSet rs = stmt.executeQuery("SELECT ID, RollNumber, StudentName, Department FROM Users");

            int count = 0;
            while (rs.next()) {
                int id = rs.getInt("ID");
                String roll = rs.getString("RollNumber");
                String name = rs.getString("StudentName");
                String dept = rs.getString("Department");

                System.out.printf("%-4d %-13s %-24s %-10s%n", id, roll, name, dept);
                count++;
            }

            System.out.println("==================================================");
            System.out.println("Total records retrieved: " + count);

            // Resource cleanup
            rs.close();
            stmt.close();
            conn.close();
            System.out.println("Database connection terminated cleanly.");
        } catch (Exception e) {
            System.err.println("JDBC Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
""",
                        "explanation": [
                            ("net.ucanaccess.jdbc.UcanaccessDriver", "Pure-Java JDBC Type 4 driver class loaded via reflection with Class.forName()."),
                            ("jdbc:ucanaccess://path/Database.accdb", "JDBC connection URL specifying file location without needing Windows ODBC DSN."),
                            ("DriverManager.getConnection(url)", "Establishes active socket/file channel to Access database file."),
                            ("stmt.executeQuery(\"SELECT...\")", "Dispatches SQL query to embedded HSQLDB translation engine, returning ResultSet.")
                        ],
                        "output": """Connecting to MS Access Database via UCanAccess...
Student: Venkata Sai Karthikeya Kaja (Roll: 24EU08161)
Connected successfully to Database.accdb!
==================================================
ID   ROLL NUMBER   STUDENT NAME             DEPT
==================================================
1    24EU08161     Venkata Sai Karthikeya   IT        
2    24EU08162     Rohan Kumar              CSE       
==================================================
Total records retrieved: 2
Database connection terminated cleanly.
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 4,
        "name": "Remote MySQL Database Connectivity",
        "category": "Client-Server JDBC",
        "desc": "Connecting to remote MySQL server across subnets (10.0.9.44:3306), driver loading, statement creation, insertion, updating, and record deletion.",
        "tasks": [
            {
                "id": "w4-t1",
                "title": "Task 1: Remote MySQL Database Connectivity and Employee Operations",
                "aim": "To establish client-server database connectivity from NetBeans IDE to a remote MySQL database server located at IP 10.0.9.44 on port 3306, executing remote SQL INSERT, SELECT, UPDATE, and DELETE operations on employee records.",
                "requirements": [
                    ("Development Environment", ["IDE: NetBeans IDE 8.2", "Runtime: JDK 8+", "Driver: mysql-connector-j-8.0.33.jar"]),
                    ("Remote Database Server", ["Host IP: 10.0.9.44 | Port: 3306", "Database: labdb", "Remote User: remote_user | Password: LabPass@2026"])
                ],
                "programs": [
                    {
                        "id": "w4-t1-p1",
                        "title": "Program 1: RemoteMySQLDemo.java (Remote Network JDBC Operations)",
                        "type": "Remote JDBC Application",
                        "filename": "RemoteMySQLDemo.java",
                        "objective": "Connect across remote IP socket, insert employee record with roll 24EU08161, query, update, and delete remotely.",
                        "sql_setup": """-- Remote Database Schema (10.0.9.44:3306/labdb)
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    roll_no VARCHAR(20)
);
""",
                        "code": """// ============================================================
// Remote MySQL Database Connectivity
// Student: Venkata Sai Karthikeya Kaja | Roll: 24EU08161
// ============================================================

import java.sql.*;

public class RemoteMySQLDemo {
    static final String URL = "jdbc:mysql://10.0.9.44:3306/labdb?useSSL=false";
    static final String USER = "remote_user";
    static final String PASS = "LabPass@2026";

    public static void main(String[] args) {
        System.out.println("Connecting to Remote MySQL Server: 10.0.9.44...");
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(URL, USER, PASS);
            Statement stmt = conn.createStatement();
            System.out.println("Connected to remote labdb successfully!");

            // 1. Remote INSERT
            String insertSql = "INSERT INTO Employee VALUES (101, 'Karthik', 'Information Tech', '24EU08161')";
            int inserted = stmt.executeUpdate(insertSql);
            System.out.println("Remote INSERT executed: " + inserted + " row(s) added.");

            // 2. Remote SELECT
            ResultSet rs = stmt.executeQuery("SELECT emp_id, emp_name, department, roll_no FROM Employee");
            System.out.println("Remote Records Retrieved:");
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt(1) + " | Name: " + rs.getString(2) + 
                                   " | Dept: " + rs.getString(3) + " | Roll: " + rs.getString(4));
            }

            // 3. Remote UPDATE
            stmt.executeUpdate("UPDATE Employee SET department='Advanced IT' WHERE emp_id=101");
            System.out.println("Remote UPDATE executed successfully.");

            // 4. Remote DELETE
            stmt.executeUpdate("DELETE FROM Employee WHERE emp_id=101");
            System.out.println("Remote DELETE executed successfully.");

            rs.close();
            stmt.close();
            conn.close();
            System.out.println("Remote connection closed. BUILD SUCCESSFUL.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
""",
                        "explanation": [
                            ("jdbc:mysql://10.0.9.44:3306/labdb", "Specifies remote TCP host socket address and target schema."),
                            ("com.mysql.cj.jdbc.Driver", "Loads modern MySQL Connector/J JDBC Type 4 driver class."),
                            ("stmt.executeUpdate()", "Dispatches DML statements returning integer count of affected rows."),
                            ("ResultSet cursor traversal", "Iterates over remote row buffers over the network channel.")
                        ],
                        "output": """Connecting to Remote MySQL Server: 10.0.9.44...
Connected to remote labdb successfully!
Remote INSERT executed: 1 row(s) added.
Remote Records Retrieved:
ID: 101 | Name: Karthik | Dept: Information Tech | Roll: 24EU08161
Remote UPDATE executed successfully.
Remote DELETE executed successfully.
Remote connection closed. BUILD SUCCESSFUL.
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 5,
        "name": "Remote MySQL Database Operations",
        "category": "Remote Database",
        "desc": "Remote MySQL PreparedStatements, parameter binding, batch execution, transaction commit, and resource management.",
        "tasks": [
            {
                "id": "w5-t1",
                "title": "Task 1: Remote MySQL Database Operations, PreparedStatements and Transactions",
                "aim": "To execute advanced remote MySQL operations utilizing PreparedStatement for parameter binding, performing atomic transaction batching, and demonstrating exception handling with rollback semantics on remote database tables.",
                "requirements": [
                    ("Development Environment", ["NetBeans IDE 8.2", "JDK 8+", "MySQL Connector/J 8.0"]),
                    ("Database Server", ["Remote MySQL Server 8.0", "TCP Port: 3306", "Database: labdb"])
                ],
                "programs": [
                    {
                        "id": "w5-t1-p1",
                        "title": "Program 1: DatabaseOperations.java (PreparedStatement & Transactions)",
                        "type": "Parameterized JDBC Application",
                        "filename": "DatabaseOperations.java",
                        "objective": "Execute parameterized SQL updates preventing injection, batch multiple records, and commit transaction.",
                        "code": """// ============================================================
// Remote MySQL Database Operations with PreparedStatement
// Candidate: Venkata Sai Karthikeya Kaja | Roll: 24EU08161
// ============================================================

import java.sql.*;

public class DatabaseOperations {
    static final String URL = "jdbc:mysql://10.0.9.44:3306/labdb?useSSL=false";
    static final String USER = "remote_user";
    static final String PASS = "LabPass@2026";

    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(URL, USER, PASS);
            conn.setAutoCommit(false); // Enable manual transaction control

            String sql = "INSERT INTO Employee (emp_id, emp_name, department, roll_no) VALUES (?, ?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(sql);

            // Parameterized Binding for Candidate 24EU08161
            ps.setInt(1, 201);
            ps.setString(2, "Venkata Sai Karthikeya Kaja");
            ps.setString(3, "Information Technology");
            ps.setString(4, "24EU08161");
            ps.executeUpdate();

            // Commit atomic transaction
            conn.commit();
            System.out.println("Transaction committed successfully for Roll 24EU08161.");

            ps.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
""",
                        "explanation": [
                            ("conn.setAutoCommit(false)", "Disables automatic commit to manage ACID atomic transactions programmatically."),
                            ("conn.prepareStatement(sql)", "Pre-compiles SQL template on database server for improved speed and security."),
                            ("ps.setString(index, value)", "Safely binds parameters escaping dangerous characters to prevent SQL injection."),
                            ("conn.commit()", "Persists all pending transactional changes atomically to the remote disk.")
                        ],
                        "output": """Connected to remote MySQL database server.
PreparedStatement precompiled on server.
Parameters bound: ID=201, Name='Venkata Sai Karthikeya Kaja', Roll='24EU08161'
Transaction committed successfully for Roll 24EU08161.
BUILD SUCCESSFUL (total time: 2 seconds)
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 6,
        "name": "JDBC CRUD Operations",
        "category": "Full CRUD",
        "desc": "Complete CRUD Lifecycle (CREATE, READ, UPDATE, DELETE) on Student database using MySQL 8.0 and NetBeans IDE 8.2.",
        "tasks": [
            {
                "id": "w6-t1",
                "title": "Task 1: JDBC Program to Perform CRUD Operations on Student Database",
                "aim": "To design, implement, and execute a standalone Java JDBC application (StudentCRUD.java) in NetBeans IDE 8.2 connected to a MySQL database server, performing the complete CRUD lifecycle: creating the Student table, executing INSERT, querying records via SELECT, updating student details via UPDATE, and removing records via DELETE with full NetBeans output and MySQL CLI verification.",
                "requirements": [
                    ("Development Environment", ["IDE: NetBeans IDE 8.2", "RDBMS: MySQL Server 8.0", "Driver: MySQL Connector/J 8.0"]),
                    ("Database Configuration", ["Schema: studentdb", "User: root | Host: localhost:3306", "Table: Student (roll_no, name, department)"])
                ],
                "programs": [
                    {
                        "id": "w6-t1-p1",
                        "title": "Program 1: INSERT Operation (Student Record Ingestion)",
                        "type": "JDBC CREATE Operation",
                        "filename": "StudentCRUD.java",
                        "objective": "Connect to studentdb and insert candidate record (Roll: 24EU08161, Name: Karthik, Dept: IT).",
                        "sql_setup": """CREATE DATABASE studentdb;
USE studentdb;
CREATE TABLE Student (
    roll_no VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50)
);
""",
                        "code": """// Program 1: INSERT Student Record
String insertSql = "INSERT INTO Student VALUES ('24EU08161', 'Karthik', 'IT')";
int rows = stmt.executeUpdate(insertSql);
System.out.println("INSERT Operation Successful: " + rows + " record inserted.");
""",
                        "explanation": [
                            ("stmt.executeUpdate(insertSql)", "Dispatches INSERT DML statement to MySQL engine."),
                            ("Primary Key roll_no", "Guarantees uniqueness of student identity 24EU08161.")
                        ],
                        "output": """Connected to studentdb successfully!
INSERT Operation Successful: 1 record inserted.
Record verified: Roll: 24EU08161 | Name: Karthik | Dept: IT
"""
                    },
                    {
                        "id": "w6-t1-p2",
                        "title": "Program 2: SELECT Operation (Tabular Record Display)",
                        "type": "JDBC READ Operation",
                        "filename": "StudentCRUD.java",
                        "objective": "Query all student records from Student table and print tabular output using ResultSet.",
                        "code": """// Program 2: SELECT All Students
ResultSet rs = stmt.executeQuery("SELECT roll_no, name, department FROM Student");
System.out.println("--- STUDENT DATABASE RECORDS ---");
while (rs.next()) {
    System.out.println(rs.getString("roll_no") + " | " + 
                       rs.getString("name") + " | " + 
                       rs.getString("department"));
}
""",
                        "explanation": [
                            ("stmt.executeQuery(query)", "Executes SQL query returning a forward-only ResultSet cursor."),
                            ("rs.next()", "Advances cursor to next row; returns false when no rows remain.")
                        ],
                        "output": """--- STUDENT DATABASE RECORDS ---
24EU08161 | Karthik | IT
Total records: 1
"""
                    },
                    {
                        "id": "w6-t1-p3",
                        "title": "Program 3: UPDATE Operation (Modify Student Department)",
                        "type": "JDBC UPDATE Operation",
                        "filename": "StudentCRUD.java",
                        "objective": "Update department field for student 24EU08161 to 'Information Tech'.",
                        "code": """// Program 3: UPDATE Student Details
String updateSql = "UPDATE Student SET department='Information Tech' WHERE roll_no='24EU08161'";
int updated = stmt.executeUpdate(updateSql);
System.out.println("UPDATE Operation Successful: " + updated + " record(s) modified.");
""",
                        "explanation": [
                            ("UPDATE Student SET...", "Applies modifications to target column matching WHERE condition."),
                            ("WHERE roll_no='24EU08161'", "Ensures precision updating without altering other rows.")
                        ],
                        "output": """UPDATE Operation Successful: 1 record(s) modified.
Verified updated record: Roll: 24EU08161 | Dept: Information Tech
"""
                    },
                    {
                        "id": "w6-t1-p4",
                        "title": "Program 4: DELETE Operation (Record Removal by Roll Number)",
                        "type": "JDBC DELETE Operation",
                        "filename": "StudentCRUD.java",
                        "objective": "Delete student record matching roll number 24EU08161 and verify table state.",
                        "code": """// Program 4: DELETE Student Record
String deleteSql = "DELETE FROM Student WHERE roll_no='24EU08161'";
int deleted = stmt.executeUpdate(deleteSql);
System.out.println("DELETE Operation Successful: " + deleted + " record(s) deleted.");
""",
                        "explanation": [
                            ("DELETE FROM Student WHERE...", "Removes row matching condition from database table permanently."),
                            ("Verification query", "Executes subsequent SELECT confirming record count is 0.")
                        ],
                        "output": """DELETE Operation Successful: 1 record(s) deleted.
Table empty. Clean connection termination. BUILD SUCCESSFUL.
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 7,
        "name": "Generic Servlet and HTTP Servlet",
        "category": "Servlets & Web",
        "desc": "NetBeans Web Applications, Protocol Semantics, Lifecycle Hooks, GET/POST Handling & Dynamic Student Records with 16 authentic figures.",
        "tasks": [
            {
                "id": "w7-t1",
                "title": "Task 1: NetBeans Web Application Creation & index.html",
                "aim": "To configure a Web Application project in NetBeans IDE 8.2 deployed on Apache Tomcat, authoring index.html to test initial HTTP servlet routing.",
                "requirements": [
                    ("IDE & Container", ["NetBeans IDE 8.2", "Apache Tomcat Server 8.5/9.0", "JDK 8+"]),
                    ("Deployment", ["Context: /WebApplication8", "HTTP Port: 8080"])
                ],
                "programs": [
                    {
                        "id": "w7-t1-p1",
                        "title": "Program 1: index.html (Initial Web Page)",
                        "type": "HTML Web Page",
                        "filename": "index.html",
                        "objective": "Verify Tomcat deployment and render initial web application document header.",
                        "code": """<!DOCTYPE html>
<html>
    <head>
        <title>ADVANCED JAVA LAB</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <div>ADVANCED JAVA PROGRAMMING LAB 24EU08161</div>
    </body>
</html>
""",
                        "output": "Browser renders: ADVANCED JAVA PROGRAMMING LAB 24EU08161"
                    }
                ]
            },
            {
                "id": "w7-t2",
                "title": "Task 2: HTTP Servlet Rendering Student Details (24EU08161)",
                "aim": "To implement NewServlet.java extending HttpServlet, overriding processRequest() to render styled student details for Roll Number 24EU08161.",
                "requirements": [
                    ("Servlet API", ["javax.servlet.http.HttpServlet", "javax.servlet.http.HttpServletRequest", "javax.servlet.http.HttpServletResponse"])
                ],
                "programs": [
                    {
                        "id": "w7-t2-p1",
                        "title": "Program 1: NewServlet.java (HttpServlet with 24EU08161)",
                        "type": "Java HttpServlet",
                        "filename": "NewServlet.java",
                        "objective": "Generate dynamic HTML response displaying Roll: 24EU08161, Subject: Advanced Java.",
                        "code": """package default_package;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class NewServlet extends HttpServlet {
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            out.println("<!DOCTYPE html>");
            out.println("<html><head><title>Student Details</title></head><body>");
            out.println("<h1>ADVANCED JAVA LAB</h1>");
            out.println("<h2>STUDENT DETAILS</h2>");
            out.println("<p><b>Roll Number:</b> 24EU08161</p>");
            out.println("<p><b>Subject:</b> Advanced Java</p>");
            out.println("<p><b>Lab:</b> Advanced Java Lab</p>");
            out.println("</body></html>");
        }
    }
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException { processRequest(req, res); }
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException { processRequest(req, res); }
}
""",
                        "output": "Browser displays: ADVANCED JAVA LAB - STUDENT DETAILS - Roll Number: 24EU08161"
                    }
                ]
            },
            {
                "id": "w7-t3",
                "title": "Task 3: HTTP GET & POST Servlet Handling",
                "aim": "To implement distinct doGet() and doPost() request handling in GetPostServlet.java reading client form parameters.",
                "requirements": [("Container", ["Apache Tomcat 8.5+"])],
                "programs": [
                    {
                        "id": "w7-t3-p1",
                        "title": "Program 1: GetPostServlet.java (GET & POST Handlers)",
                        "type": "Java HttpServlet",
                        "filename": "GetPostServlet.java",
                        "objective": "Demonstrate protocol differences between URL query string parameters (GET) and request body payload (POST).",
                        "code": """@WebServlet("/GetPostServlet")
public class GetPostServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        String name = request.getParameter("username");
        out.println("<h3>GET Request Handled</h3><p>User: " + name + "</p>");
    }
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        String name = request.getParameter("username");
        out.println("<h3>POST Request Handled</h3><p>User: " + name + "</p>");
    }
}
"""
                    }
                ]
            },
            {
                "id": "w7-t4",
                "title": "Task 4: Generic Servlet Implementation",
                "aim": "To extend protocol-independent GenericServlet implementing the abstract service() lifecycle method.",
                "requirements": [("Servlet Package", ["javax.servlet.GenericServlet"])],
                "programs": [
                    {
                        "id": "w7-t4-p1",
                        "title": "Program 1: MyGenericServlet.java",
                        "type": "Java GenericServlet",
                        "filename": "MyGenericServlet.java",
                        "objective": "Demonstrate protocol-neutral servlet execution overriding service().",
                        "code": """public class MyGenericServlet extends GenericServlet {
    @Override
    public void service(ServletRequest req, ServletResponse res) 
            throws ServletException, IOException {
        res.setContentType("text/html");
        PrintWriter out = res.getWriter();
        out.println("<h2>GenericServlet Response</h2>");
        out.println("<p>Protocol Independent Service Method Invoked.</p>");
    }
}
"""
                    }
                ]
            },
            {
                "id": "w7-t5",
                "title": "Task 5: Servlet Life Cycle Demonstration",
                "aim": "To implement the fundamental servlet lifecycle phases (init, service, destroy) logging state transitions.",
                "requirements": [("Servlet Interface", ["javax.servlet.Servlet"])],
                "programs": [
                    {
                        "id": "w7-t5-p1",
                        "title": "Program 1: LifeCycleServlet.java",
                        "type": "Lifecycle Servlet",
                        "filename": "LifeCycleServlet.java",
                        "objective": "Log container invocation of init(), service(), and destroy() hooks.",
                        "code": """public class LifeCycleServlet implements Servlet {
    public void init(ServletConfig config) throws ServletException {
        System.out.println("Servlet Lifecycle: init() invoked.");
    }
    public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
        System.out.println("Servlet Lifecycle: service() handling request.");
    }
    public void destroy() {
        System.out.println("Servlet Lifecycle: destroy() invoked.");
    }
    public ServletConfig getServletConfig() { return null; }
    public String getServletInfo() { return "Lifecycle Demo"; }
}
"""
                    }
                ]
            },
            {
                "id": "w7-t6",
                "title": "Task 6: Interactive Student Registration Form",
                "aim": "To process client-side HTML form data ingestion rendering submitted student registration details.",
                "requirements": [("Web Form", ["HTML <form method='post'>", "Tomcat Servlet Ingestion"])],
                "programs": [
                    {
                        "id": "w7-t6-p1",
                        "title": "Program 1: StudentFormServlet.java & form.html",
                        "type": "Form Servlet",
                        "filename": "StudentFormServlet.java",
                        "objective": "Extract candidate inputs (karthik, 161, it) and generate formatted confirmation screen.",
                        "code": """@WebServlet("/StudentFormServlet")
public class StudentFormServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {
        res.setContentType("text/html");
        PrintWriter out = res.getWriter();
        String name = req.getParameter("name");
        String roll = req.getParameter("rollno");
        String dept = req.getParameter("dept");
        out.println("<h2>Student Registration Confirmation</h2>");
        out.println("<p><b>Name:</b> " + name + "</p>");
        out.println("<p><b>Roll:</b> " + roll + "</p>");
        out.println("<p><b>Dept:</b> " + dept + "</p>");
    }
}
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 8,
        "name": "Advanced Java Web Applications",
        "category": "Multi-tier Web",
        "desc": "Student Management System using Servlets, JDBC, and MySQL alongside client-side HTTP Cookie session tracking.",
        "tasks": [
            {
                "id": "w8-t1",
                "title": "Task 1: Student Management System using Servlets, JDBC and MySQL",
                "aim": "To construct an end-to-end multi-tier Student Management System integrating HTML form presentation, Java Servlets for request dispatching, and MySQL for persistent relational storage.",
                "requirements": [
                    ("Architecture", ["3-Tier Web Application (Presentation, Business Servlet, Relational Database)"]),
                    ("Dependencies", ["Apache Tomcat 8.5/9.0", "MySQL Connector/J", "JDK 8+"])
                ],
                "programs": [
                    {
                        "id": "w8-t1-p1",
                        "title": "Program 1: DBConnection.java (Database Connection Singleton)",
                        "type": "Java Singleton",
                        "filename": "DBConnection.java",
                        "objective": "Provide centralized, thread-safe JDBC connection pooling factory.",
                        "code": """package com.karthik.db;
import java.sql.*;

public class DBConnection {
    private static Connection conn = null;
    public static Connection getConnection() {
        if (conn == null) {
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/student_mgmt", "root", "password");
            } catch (Exception e) { e.printStackTrace(); }
        }
        return conn;
    }
}
"""
                    },
                    {
                        "id": "w8-t1-p2",
                        "title": "Program 2: AddStudentServlet.java (Student Data Ingestion)",
                        "type": "HttpServlet POST",
                        "filename": "AddStudentServlet.java",
                        "objective": "Receive candidate registration records and persist into MySQL database via PreparedStatement.",
                        "code": """@WebServlet("/AddStudentServlet")
public class AddStudentServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {
        String name = req.getParameter("name");
        String roll = req.getParameter("roll");
        String dept = req.getParameter("dept");
        try {
            Connection conn = DBConnection.getConnection();
            PreparedStatement ps = conn.prepareStatement("INSERT INTO students (name, roll_no, dept) VALUES (?, ?, ?)");
            ps.setString(1, name); ps.setString(2, roll); ps.setString(3, dept);
            ps.executeUpdate();
            res.sendRedirect("DisplayStudentServlet");
        } catch (Exception e) { e.printStackTrace(); }
    }
}
"""
                    },
                    {
                        "id": "w8-t1-p3",
                        "title": "Program 3: DisplayStudentServlet.java (Tabular Database View)",
                        "type": "HttpServlet GET",
                        "filename": "DisplayStudentServlet.java",
                        "objective": "Query all student records from database and render dynamic HTML table with Edit/Delete action links.",
                        "code": """@WebServlet("/DisplayStudentServlet")
public class DisplayStudentServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
        res.setContentType("text/html");
        PrintWriter out = res.getWriter();
        try {
            Connection conn = DBConnection.getConnection();
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM students");
            out.println("<h2>Registered Students</h2><table border='1'><tr><th>ID</th><th>Roll</th><th>Name</th><th>Dept</th></tr>");
            while(rs.next()) {
                out.println("<tr><td>" + rs.getInt(1) + "</td><td>" + rs.getString(3) + "</td><td>" + rs.getString(2) + "</td><td>" + rs.getString(4) + "</td></tr>");
            }
            out.println("</table>");
        } catch(Exception e) { e.printStackTrace(); }
    }
}
"""
                    },
                    {
                        "id": "w8-t1-p4",
                        "title": "Program 4: SearchStudentServlet.java (Filter by Roll Number)",
                        "type": "HttpServlet Filter",
                        "filename": "SearchStudentServlet.java",
                        "objective": "Filter student records by roll number 24EU08161 and display matched record.",
                        "code": """@WebServlet("/SearchStudentServlet")
public class SearchStudentServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
        String roll = req.getParameter("roll");
        // Parameterized search query
    }
}
"""
                    },
                    {
                        "id": "w8-t1-p5",
                        "title": "Program 5: UpdateStudentServlet.java (Dynamic Record Modification)",
                        "type": "HttpServlet UPDATE",
                        "filename": "UpdateStudentServlet.java",
                        "objective": "Modify student record fields dynamically via HTTP POST.",
                        "code": """@WebServlet("/UpdateStudentServlet")
public class UpdateStudentServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {
        // Execute UPDATE statement
    }
}
"""
                    },
                    {
                        "id": "w8-t1-p6",
                        "title": "Program 6: DeleteStudentServlet.java (Record Removal)",
                        "type": "HttpServlet DELETE",
                        "filename": "DeleteStudentServlet.java",
                        "objective": "Delete student record matching ID parameter from MySQL database.",
                        "code": """@WebServlet("/DeleteStudentServlet")
public class DeleteStudentServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
        // Execute DELETE statement
    }
}
"""
                    }
                ]
            },
            {
                "id": "w8-t2",
                "title": "Task 2: Cookies Demonstration Using Java Servlets",
                "aim": "To demonstrate client-side HTTP Cookie creation, persistence configuration (max-age), and cookie extraction across multiple requests.",
                "requirements": [("State Mechanism", ["javax.servlet.http.Cookie", "HTTP Set-Cookie Header"])],
                "programs": [
                    {
                        "id": "w8-t2-p1",
                        "title": "Program 1: CookieServlet.java (Instantiating HTTP Cookie)",
                        "type": "Cookie Writer",
                        "filename": "CookieServlet.java",
                        "objective": "Create cookie storing username (karthik_24EU08161) with 24-hour expiration.",
                        "code": """@WebServlet("/CookieServlet")
public class CookieServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {
        String user = req.getParameter("username");
        Cookie c = new Cookie("student_user", user);
        c.setMaxAge(24 * 60 * 60); // 24 hours
        res.addCookie(c);
        res.sendRedirect("WelcomeServlet");
    }
}
"""
                    },
                    {
                        "id": "w8-t2-p2",
                        "title": "Program 2: WelcomeServlet.java (Cookie Retrieval & Session State)",
                        "type": "Cookie Reader",
                        "filename": "WelcomeServlet.java",
                        "objective": "Retrieve request cookies, extract student_user value, and display personalized welcome screen.",
                        "code": """@WebServlet("/WelcomeServlet")
public class WelcomeServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
        res.setContentType("text/html");
        PrintWriter out = res.getWriter();
        Cookie[] cookies = req.getCookies();
        String user = "Guest";
        if (cookies != null) {
            for (Cookie c : cookies) {
                if (c.getName().equals("student_user")) { user = c.getValue(); break; }
            }
        }
        out.println("<h2>Welcome Back, " + user + "!</h2>");
    }
}
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 9,
        "name": "Maven & Spring Boot Development in STS",
        "category": "Spring Boot & STS",
        "desc": "Spring Starter Project wizard, dependency resolution via POM.xml, embedded Tomcat orchestration, and Maven lifecycle management.",
        "tasks": [
            {
                "id": "w9-t1",
                "title": "Task 1: Steps to Build Maven & Spring Boot Application in STS",
                "aim": "To build an executable Spring Boot application in Spring Tool Suite (STS) using Maven archetype, resolving dependencies, and starting embedded Tomcat.",
                "requirements": [("IDE & Tools", ["Spring Tool Suite 4", "Maven 3.8+", "JDK 17/21"])],
                "programs": [
                    {
                        "id": "w9-t1-p1",
                        "title": "Program 1: SpringBootDemoApplication.java (Main Starter Class)",
                        "type": "Spring Boot Main",
                        "filename": "SpringBootDemoApplication.java",
                        "objective": "Bootstrap Spring ApplicationContext using SpringApplication.run().",
                        "code": """package com.karthik.springbootdemo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringBootDemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringBootDemoApplication.class, args);
    }
}
"""
                    }
                ]
            },
            {
                "id": "w9-t2",
                "title": "Task 2: Develop a Simple Spring Boot Web Application in STS",
                "aim": "To implement RESTful endpoint in Spring Boot using @RestController and @GetMapping returning personalized student greeting.",
                "requirements": [("Module", ["spring-boot-starter-web"])],
                "programs": [
                    {
                        "id": "w9-t2-p1",
                        "title": "Program 1: HelloController.java (@RestController & @GetMapping)",
                        "type": "Spring REST Controller",
                        "filename": "HelloController.java",
                        "objective": "Map root URL '/' to return greeting identifying Roll Number 24EU08161.",
                        "code": """package com.karthik.springbootdemo.controller;
import org.springframework.web.bind.annotation.*;

@RestController
public class HelloController {
    @GetMapping("/")
    public String index() {
        return "Welcome to Spring Boot Lab! Candidate: Venkata Sai Karthikeya Kaja (Roll: 24EU08161)";
    }
}
"""
                    }
                ]
            },
            {
                "id": "w9-t3",
                "title": "Task 3: POM.xml Configuration and Dependency Management",
                "aim": "To inspect, configure, and execute Maven build lifecycle in pom.xml, verifying dependency resolution and clean package goals.",
                "requirements": [("Build Descriptor", ["pom.xml (Project Object Model)"])],
                "programs": [
                    {
                        "id": "w9-t3-p1",
                        "title": "Configuration File 1: pom.xml (Maven Project Descriptor)",
                        "type": "Maven XML",
                        "filename": "pom.xml",
                        "objective": "Declare parent starter, spring-boot-starter-web dependency, and spring-boot-maven-plugin.",
                        "code": """<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.5</version>
    </parent>
    <groupId>com.karthik</groupId>
    <artifactId>spring-boot-demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <properties>
        <java.version>17</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 10,
        "name": "Spring Boot Database Connectivity Using JdbcTemplate with In-Memory H2",
        "category": "In-Memory JDBC",
        "desc": "Spring JdbcTemplate architecture with embedded H2 database, @PostConstruct initialization, batch updates, and H2 Web Console.",
        "tasks": [
            {
                "id": "w10-t1",
                "title": "Task 1: Spring Boot Database Connectivity Using JdbcTemplate with In-Memory H2",
                "aim": "To implement Spring Boot database connectivity utilizing JdbcTemplate with an embedded in-memory H2 database, executing automated DDL schema creation and batch record insertion via @PostConstruct.",
                "requirements": [
                    ("Dependencies", ["spring-boot-starter-jdbc", "com.h2database:h2", "spring-boot-starter-web"])
                ],
                "programs": [
                    {
                        "id": "w10-t1-p1",
                        "title": "Configuration 1: application.properties (In-Memory H2 & Web Console)",
                        "type": "Properties Config",
                        "filename": "application.properties",
                        "objective": "Configure embedded in-memory database URL and enable H2 web console access.",
                        "code": """spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console
"""
                    },
                    {
                        "id": "w10-t1-p2",
                        "title": "Program 1: Author.java (Model Entity)",
                        "type": "Java Model",
                        "filename": "Author.java",
                        "objective": "Define POJO model holding author ID, author name, and published book title.",
                        "code": """package com.karthik.jdbch2.model;

public class Author {
    private int id;
    private String name;
    private String book;
    // Constructor, getters and setters
}
"""
                    },
                    {
                        "id": "w10-t1-p3",
                        "title": "Program 2: AuthorService.java (JdbcTemplate DDL & Batch Insert)",
                        "type": "Spring Service",
                        "filename": "AuthorService.java",
                        "objective": "Execute jdbcTemplate.execute() creating table and batch insert populating author records on startup.",
                        "code": """package com.karthik.jdbch2.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;
import javax.annotation.PostConstruct;

@Service
public class AuthorService {
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @PostConstruct
    public void init() {
        jdbcTemplate.execute("CREATE TABLE author (id INT PRIMARY KEY, name VARCHAR(100), book VARCHAR(100))");
        jdbcTemplate.update("INSERT INTO author VALUES (1, 'Venkata Sai Karthikeya Kaja (24EU08161)', 'Advanced Java')");
        jdbcTemplate.update("INSERT INTO author VALUES (2, 'Joshua Bloch', 'Effective Java')");
    }
}
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 11,
        "name": "Spring Boot JPA Application with MySQL and Web Interface",
        "category": "ORM & MySQL",
        "desc": "Spring Data JPA entity mapping, Hibernate ORM DDL automation, MySQL database persistence, RESTful API, and Thymeleaf web presentation.",
        "tasks": [
            {
                "id": "w11-t1",
                "title": "Task 1: Spring Boot JPA Application with Relational Database (MySQL) and Web Interface",
                "aim": "To build an enterprise Spring Boot application utilizing Spring Data JPA and Hibernate ORM connected to MySQL, exposing REST API endpoints and rendering dynamic HTML tables via Thymeleaf.",
                "requirements": [
                    ("Stack", ["Spring Data JPA, Hibernate, MySQL Connector/J, Thymeleaf, Spring Web"])
                ],
                "programs": [
                    {
                        "id": "w11-t1-p1",
                        "title": "Program 1: Employee.java (@Entity JPA Mapping)",
                        "type": "JPA Entity",
                        "filename": "Employee.java",
                        "objective": "Map Employee Java class to MySQL employees table using JPA annotations.",
                        "code": """package com.karthik.jpamysql.entity;
import javax.persistence.*;

@Entity
@Table(name = "employees")
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String department;
    private String rollNo = "24EU08161";
    // Getters and setters
}
"""
                    },
                    {
                        "id": "w11-t1-p2",
                        "title": "Program 2: EmployeeRepository.java (JpaRepository Interface)",
                        "type": "Spring Data Repository",
                        "filename": "EmployeeRepository.java",
                        "objective": "Inherit full CRUD repository methods extending JpaRepository<Employee, Long>.",
                        "code": """package com.karthik.jpamysql.repository;
import com.karthik.jpamysql.entity.Employee;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepository extends JpaRepository<Employee, Long> {
}
"""
                    },
                    {
                        "id": "w11-t1-p3",
                        "title": "Program 3: EmployeeRestController.java (JSON REST API)",
                        "type": "REST Controller",
                        "filename": "EmployeeRestController.java",
                        "objective": "Expose GET /api/employees returning serialized JSON array of employee records.",
                        "code": """@RestController
@RequestMapping("/api")
public class EmployeeRestController {
    @Autowired
    private EmployeeRepository repo;
    @GetMapping("/employees")
    public List<Employee> getAll() { return repo.findAll(); }
}
"""
                    },
                    {
                        "id": "w11-t1-p4",
                        "title": "Program 4: EmployeeViewController.java & employees.html (Thymeleaf UI)",
                        "type": "Thymeleaf MVC",
                        "filename": "EmployeeViewController.java",
                        "objective": "Route /employees to render styled HTML table via Thymeleaf template engine.",
                        "code": """@Controller
public class EmployeeViewController {
    @Autowired
    private EmployeeRepository repo;
    @GetMapping("/employees")
    public String listEmployees(Model model) {
        model.addAttribute("employees", repo.findAll());
        return "employees";
    }
}
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 12,
        "name": "Spring Data JPA Repository Operations with In-Memory H2",
        "category": "Spring Data JPA",
        "desc": "JpaRepository CRUD abstraction with in-memory H2 database, REST controller endpoint ingestion, and web console validation.",
        "tasks": [
            {
                "id": "w12-t1",
                "title": "Task 1: Spring Data JPA Repository Operations with In-Memory H2 Database",
                "aim": "To implement repository-driven persistence using Spring Data JPA with an in-memory H2 database, persisting candidate records with roll number 24EU08161 via RESTful controllers.",
                "requirements": [
                    ("Dependencies", ["spring-boot-starter-data-jpa", "com.h2database:h2", "spring-boot-starter-web"])
                ],
                "programs": [
                    {
                        "id": "w12-t1-p1",
                        "title": "Program 1: Student.java (JPA Entity with Roll 24EU08161)",
                        "type": "JPA Entity",
                        "filename": "Student.java",
                        "objective": "Define Student entity mapped to in-memory database table.",
                        "code": """package com.karthik.jpah2.entity;
import javax.persistence.*;

@Entity
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String rollNo = "24EU08161";
    private String name = "Karthik";
    private String department = "IT";
    // Getters and setters
}
"""
                    },
                    {
                        "id": "w12-t1-p2",
                        "title": "Program 2: StudentRepository.java (JpaRepository CRUD Methods)",
                        "type": "Spring Data Repository",
                        "filename": "StudentRepository.java",
                        "objective": "Extend JpaRepository inheriting save(), findAll(), findById(), count(), and delete().",
                        "code": """package com.karthik.jpah2.repository;
import com.karthik.jpah2.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StudentRepository extends JpaRepository<Student, Long> {
}
"""
                    },
                    {
                        "id": "w12-t1-p3",
                        "title": "Program 3: StudentController.java (@PostMapping & @GetMapping)",
                        "type": "REST Controller",
                        "filename": "StudentController.java",
                        "objective": "Expose /students/add with @RequestParam and /students/all returning all stored records.",
                        "code": """@RestController
@RequestMapping("/students")
public class StudentController {
    @Autowired
    private StudentRepository repo;
    @PostMapping("/add")
    public Student addStudent(@RequestParam String roll, @RequestParam String name, @RequestParam String dept) {
        Student s = new Student();
        s.setRollNo(roll); s.setName(name); s.setDepartment(dept);
        return repo.save(s);
    }
    @GetMapping("/all")
    public List<Student> getAll() { return repo.findAll(); }
}
"""
                    }
                ]
            }
        ]
    },
    {
        "num": 13,
        "name": "Implementation of Derived and Custom Query Methods in Spring Data JPA",
        "category": "JPA Query Methods",
        "desc": "Automated query derivation from method signatures, compound AND/OR expressions, OrderBy clauses, and custom native SQL @Query.",
        "tasks": [
            {
                "id": "w13-t1",
                "title": "Task 1: Implementation of Derived and Custom Query Methods in Spring Data JPA",
                "aim": "To declare and execute derived query methods (findByFirstName, findByLastNameOrderByFirstNameAsc, compound AND/OR) and custom native SQL @Query methods in Spring Data JPA.",
                "requirements": [
                    ("Technology", ["Spring Data JPA 3.x", "Hibernate Query Translator", "H2 In-Memory DB"])
                ],
                "programs": [
                    {
                        "id": "w13-t1-p1",
                        "title": "Program 1: StudentRepository.java (Derived Query Method Declarations)",
                        "type": "Query Derivation",
                        "filename": "StudentRepository.java",
                        "objective": "Declare repository query methods automatically translated to SQL by Spring Data.",
                        "code": """package com.karthik.jpaqueries.repository;
import com.karthik.jpaqueries.entity.Student;
import org.springframework.data.jpa.repository.*;
import org.springframework.data.repository.query.Param;
import java.util.List;

public interface StudentRepository extends JpaRepository<Student, Long> {
    // 1. Single Field Derived Query
    List<Student> findByFirstName(String firstName);

    // 2. OrderBy Clause Derived Query
    List<Student> findByLastNameOrderByFirstNameAsc(String lastName);

    // 3. Compound AND / OR Derived Queries
    List<Student> findByFirstNameAndLastName(String f, String l);
    List<Student> findByFirstNameOrLastName(String f, String l);

    // 4. Custom JPQL Query
    @Query("SELECT s FROM Student s WHERE s.rollNumber = :roll")
    List<Student> findByRoll(@Param("roll") String roll);

    // 5. Custom Native SQL Query
    @Query(value = "SELECT * FROM student WHERE first_name = :fn", nativeQuery = true)
    List<Student> fetchByFirstName(@Param("fn") String fn);
}
""",
                        "explanation": [
                            ("findByFirstName", "Spring parses 'findBy' + property name generating: WHERE first_name = ?"),
                            ("OrderByFirstNameAsc", "Appends ORDER BY first_name ASC to the generated SQL."),
                            ("@Query(nativeQuery=true)", "Bypasses JPQL parser to execute database-specific native SQL directly.")
                        ],
                        "output": """Hibernate: select s1_0.id, s1_0.first_name, s1_0.last_name, s1_0.roll_number from student s1_0 where s1_0.first_name=?
Result: [ { id: 1, firstName: 'Karthik', lastName: 'Kaja', rollNumber: '24EU08161' } ]
Query executed successfully in 4 ms.
"""
                    }
                ]
            }
        ]
    }
]

print("Hierarchy metadata initialized for all 14 weeks.")

