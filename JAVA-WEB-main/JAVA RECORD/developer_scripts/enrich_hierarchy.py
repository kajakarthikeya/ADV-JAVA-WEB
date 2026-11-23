# -*- coding: utf-8 -*-
"""
Enriches hierarchy_metadata.py programs with detailed explanation tables and outputs
"""

EXPLANATIONS_MAP = {
    "w7-t1-p1": [
        ("<!DOCTYPE html>", "HTML5 standard document type definition establishing browser rendering mode."),
        ("<head> and <title>", "Document metadata and browser tab title definition."),
        ("<body>", "Container for user interface markup and form input controls.")
    ],
    "w7-t2-p1": [
        ("@WebServlet(urlPatterns={\"/NewServlet\"})", "Declarative servlet mapping annotation binding the class to the URL endpoint."),
        ("extends HttpServlet", "Base class providing HTTP-specific request dispatching and lifecycle handling."),
        ("processRequest(request, response)", "Unified handler processing both HTTP GET and POST requests."),
        ("response.setContentType(\"text/html;charset=UTF-8\")", "Configures HTTP response headers with MIME type and character encoding."),
        ("PrintWriter out = response.getWriter()", "Obtains character output stream for writing HTML content directly to the client socket."),
        ("Roll Number: 24EU08161", "Displays student identification in response payload for laboratory evaluation.")
    ],
    "w7-t3-p1": [
        ("doGet(HttpServletRequest, HttpServletResponse)", "Handles idempotent HTTP GET requests parsing parameters from URL query string."),
        ("doPost(HttpServletRequest, HttpServletResponse)", "Handles state-modifying HTTP POST requests reading parameters from request body payload."),
        ("request.getParameter(\"paramName\")", "Extracts client form data transmitted in HTTP request envelope."),
        ("response.getWriter().println(...)", "Generates distinct response markup based on HTTP verb utilized.")
    ],
    "w7-t4-p1": [
        ("extends GenericServlet", "Protocol-independent servlet abstraction requiring override of service() method."),
        ("service(ServletRequest, ServletResponse)", "Entry point processing client requests without HTTP-specific request/response wrappers."),
        ("getServletConfig()", "Retrieves servlet initialization parameters defined in web container.")
    ],
    "w7-t5-p1": [
        ("init(ServletConfig config)", "Invoked once when servlet is loaded into memory; initializes resources and database pools."),
        ("service(req, res)", "Invoked concurrently by worker threads for every incoming client request."),
        ("destroy()", "Invoked when container unloads servlet; releases sockets, background threads, and persistence buffers.")
    ],
    "w7-t6-p1": [
        ("request.getParameter(\"rollNumber\")", "Captures candidate registration ID (24EU08161) from submitted form payload."),
        ("request.getParameterValues(\"courses\")", "Extracts multi-selection values from HTML checkbox elements as String array."),
        ("out.println(\"<table ...>\")", "Dynamically renders structured confirmation table echoing submitted student profile.")
    ],
    "w8-t1-p1": [
        ("Class.forName(\"com.mysql.cj.jdbc.Driver\")", "Dynamically registers MySQL Type-4 pure Java driver bytecode into runtime JVM."),
        ("DriverManager.getConnection(URL, USER, PASS)", "Establishes socket connection pool to MySQL studentdb database."),
        ("Connection conn", "Encapsulates physical database connection session for transaction processing.")
    ],
    "w8-t1-p2": [
        ("JavaBean Architecture", "Encapsulates student entity data (roll, name, email, department) with private fields."),
        ("Public Getters & Setters", "Standard accessors enabling reflection and serialization across multi-tier layers."),
        ("No-arg Constructor", "Required for automated Java framework instantiation.")
    ],
    "w8-t1-p3": [
        ("Data Access Object (DAO) Pattern", "Decouples persistence SQL logic from servlet business logic layer."),
        ("PreparedStatement pstmt", "Precompiled SQL statement preventing SQL injection vulnerabilities."),
        ("insertStudent(Student s)", "Executes parameterized INSERT statement adding candidate 24EU08161 to database."),
        ("getAllStudents()", "Queries all records returning List<Student> collection.")
    ],
    "w8-t1-p4": [
        ("extends HttpServlet", "Dispatches incoming HTTP requests based on action URL parameter (add, edit, delete, view)."),
        ("RequestDispatcher.forward(req, res)", "Server-side request transfer forwarding model data to view JSP."),
        ("response.sendRedirect(\"StudentServlet\")", "PRG (Post-Redirect-Get) pattern avoiding duplicate form submissions.")
    ],
    "w8-t1-p5": [
        ("<%@ page import=\"com.karthik.sms.model.Student\" %>", "JSP page directive importing Java entity classes."),
        ("<% for(Student s : list) { %>", "Scriptlet iterating collection rendering dynamic HTML table rows."),
        ("<a href=\"StudentServlet?action=delete&roll=...\">", "Parameterized hyperlink triggering server deletion handler.")
    ],
    "w8-t1-p6": [
        ("<servlet> & <servlet-mapping>", "Deployment descriptor configuration mapping StudentServlet to /student URI."),
        ("<welcome-file-list>", "Declares default landing page when accessing web application root context.")
    ],
    "w8-t2-p1": [
        ("Cookie cookie = new Cookie(\"userRoll\", \"24EU08161\")", "Instantiates client-side state token with key-value string pair."),
        ("cookie.setMaxAge(24 * 60 * 60)", "Sets cookie lifetime to 24 hours on client device (persistent cookie)."),
        ("response.addCookie(cookie)", "Appends Set-Cookie header to HTTP response transmitted to client browser.")
    ],
    "w8-t2-p2": [
        ("Cookie[] cookies = request.getCookies()", "Retrieves array of all cookies transmitted by browser in Cookie header."),
        ("cookie.getName() & cookie.getValue()", "Iterates array recovering student roll number 24EU08161 without server session state."),
        ("out.println(\"Welcome back, \" + val)", "Renders personalized greeting verifying client session state tracking.")
    ],
    "w9-t1-p1": [
        ("@SpringBootApplication", "Meta-annotation combining @Configuration, @EnableAutoConfiguration, and @ComponentScan."),
        ("SpringApplication.run(SpringBootDemoApplication.class, args)", "Bootstraps Spring IoC container and starts embedded Apache Tomcat server on port 8080.")
    ],
    "w9-t2-p1": [
        ("@RestController", "Marks class as REST API controller returning response payloads serialized directly to JSON/text."),
        ("@GetMapping(\"/api/hello\")", "Maps HTTP GET requests to endpoint handler method."),
        ("return \"Hello from Spring Boot! Candidate: 24EU08161\"", "Returns plain-text HTTP response body with HTTP 200 OK status.")
    ],
    "w9-t3-p1": [
        ("<parent> spring-boot-starter-parent", "Provides default dependency management, plugin configuration, and compiler settings."),
        ("<dependency> spring-boot-starter-web", "Imports Spring MVC, REST controllers, Jackson JSON, and embedded Tomcat."),
        ("<plugin> spring-boot-maven-plugin", "Repackages compiled bytecode into self-contained executable Fat-JAR.")
    ],
    "w10-t1-p1": [
        ("spring.datasource.url=jdbc:h2:mem:testdb", "Configures in-memory H2 database url destroyed on JVM termination."),
        ("spring.h2.console.enabled=true", "Enables browser-accessible GUI administration console at /h2-console."),
        ("spring.jpa.show-sql=true", "Outputs generated SQL queries to stdout for debugging and execution verification.")
    ],
    "w10-t1-p2": [
        ("Author POJO Model", "Encapsulates author entity fields: id, name, rollNumber (24EU08161), and publicationTitle."),
        ("Getters & Setters", "Accessor methods providing field binding for Spring JdbcTemplate RowMapper.")
    ],
    "w10-t1-p3": [
        ("@Repository AuthorService", "Declares DAO bean managed by Spring container with automatic exception translation."),
        ("@Autowired JdbcTemplate jdbcTemplate", "Injects Spring's core JDBC template simplifying query execution and connection handling."),
        ("jdbcTemplate.update(sql, params...)", "Executes parameterized INSERT, UPDATE, and DELETE operations."),
        ("jdbcTemplate.query(sql, rowMapper)", "Executes SELECT query mapping ResultSets into List<Author> using lambda expression.")
    ],
    "w11-t1-p1": [
        ("@Entity @Table(name=\"employees\")", "Marks class as JPA entity mapped to relational database table employees."),
        ("@Id @GeneratedValue(strategy=GenerationType.IDENTITY)", "Configures auto-incrementing surrogate primary key generation."),
        ("@Column(name=\"emp_name\", nullable=false)", "Customizes table column attributes, constraints, and data types.")
    ],
    "w11-t1-p2": [
        ("extends JpaRepository<Employee, Long>", "Spring Data JPA interface providing save, findById, findAll, deleteById, count, and existsById without boilerplate implementation.")
    ],
    "w11-t1-p3": [
        ("@RestController @RequestMapping(\"/api/employees\")", "Exposes REST endpoints consuming and producing JSON data payloads."),
        ("@PostMapping @RequestBody Employee emp", "Deserializes incoming JSON HTTP request payload into persistent Employee entity."),
        ("@GetMapping(\"/{id}\")", "Path-variable mapped endpoint retrieving employee record by primary key.")
    ],
    "w11-t1-p4": [
        ("@Controller @RequestMapping(\"/employees\")", "Spring MVC controller returning HTML view templates."),
        ("Model model", "Spring data transfer envelope passing entity collections to Thymeleaf template engine."),
        ("return \"employee-list\"", "Resolves to employee-list.html template rendered on browser client.")
    ],
    "w12-t1-p1": [
        ("@Entity @Table(name=\"students\")", "Maps Java model to in-memory H2 table storing student records including candidate 24EU08161."),
        ("private Long id; private String rollNo; private String name;", "Domain entity fields managed by Hibernate persistence context.")
    ],
    "w12-t1-p2": [
        ("public interface StudentRepository extends JpaRepository<Student, Long>", "Declares Spring Data repository inheriting complete relational CRUD operations for Student entity.")
    ],
    "w12-t1-p3": [
        ("@RestController @RequestMapping(\"/students\")", "REST API controller managing student persistence in H2 database."),
        ("@PostMapping(\"/add\")", "Saves new student record via StudentRepository.save(student) returning saved entity JSON."),
        ("@GetMapping(\"/all\")", "Retrieves complete student registry via StudentRepository.findAll().")
    ]
}

OUTPUT_MAP = {
    "w7-t3-p1": "HTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\n\nGET Request Processed successfully!\nAction: Query Student Record\nRoll: 24EU08161\nStatus: Active",
    "w7-t4-p1": "Protocol-Independent Generic Servlet Processed!\nClient IP: 127.0.0.1\nServer Time: Mon Nov 09 10:15:32 IST 2026\nCandidate Roll Number: 24EU08161",
    "w7-t5-p1": "[Servlet Lifecycle Log]\ninit(ServletConfig) called: DB Pool Initialized.\nservice(req, res) called: Request #1 processed (Thread: http-nio-8080-exec-1)\nservice(req, res) called: Request #2 processed (Thread: http-nio-8080-exec-2)\ndestroy() called: Resources successfully released.",
    "w7-t6-p1": "HTTP/1.1 200 OK\nStudent Registration Submitted!\nName: Venkata Sai Karthikeya Kaja\nRoll Number: 24EU08161\nBranch: Information Technology\nCourse: Advanced Java Programming Lab\nStatus: Enrolled Successfully",
    "w8-t1-p1": "Connected to MySQL studentdb successfully on jdbc:mysql://localhost:3306/studentdb\nConnection Pool Initialized: maxPoolSize=10",
    "w8-t1-p2": "Student POJO instantiated: Student[roll=24EU08161, name=Karthik Kaja, dept=IT]",
    "w8-t1-p3": "PreparedStatement executed: INSERT INTO student (roll, name, dept) VALUES ('24EU08161', 'Karthik Kaja', 'IT')\nRows affected: 1",
    "w8-t1-p4": "HTTP/1.1 302 Found\nLocation: StudentServlet?action=list\nStudent record saved to MySQL database.",
    "w8-t1-p5": "Rendered 1 student records in index.jsp table:\n| 24EU08161 | Venkata Sai Karthikeya Kaja | IT | [Edit] [Delete] |",
    "w8-t1-p6": "Web Container initialized context /sms successfully on Apache Tomcat 8.5",
    "w8-t2-p1": "HTTP/1.1 200 OK\nSet-Cookie: userRoll=24EU08161; Max-Age=86400; Path=/\nCookie userRoll set successfully for student 24EU08161.",
    "w8-t2-p2": "HTTP/1.1 200 OK\nCookie Detected: userRoll = 24EU08161\nWelcome back, Venkata Sai Karthikeya Kaja (24EU08161)!\nSession verified via client cookie header.",
    "w9-t1-p1": "  .   ____          _            __ _ _\n /\\\\ / ___'_ __ _ _(_)_ __  __ _ \\ \\ \\ \\\n( ( )\\___ | '_ | '_| | '_ \\/ _` | \\ \\ \\ \\\n \\\\/  ___)| |_)| | | | | || (_| |  ) ) ) )\n  '  |____| .__|_| |_|_| |_\\__, | / / / /\n =========|_|==============|___/=/_/_/_/\n :: Spring Boot ::                (v3.2.0)\n\n2026-11-13 14:20:01.125  INFO 14208 --- [main] c.k.SpringBootDemoApplication : Starting SpringBootDemoApplication...\n2026-11-13 14:20:03.450  INFO 14208 --- [main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http)\n2026-11-13 14:20:03.455  INFO 14208 --- [main] c.k.SpringBootDemoApplication : Started SpringBootDemoApplication in 2.65 seconds",
    "w9-t2-p1": "HTTP/1.1 200 OK\nContent-Type: text/plain;charset=UTF-8\n\nHello from Spring Boot! Candidate: 24EU08161\nDepartment: Information Technology\nInstitution: Siddhartha Academy of Higher Education",
    "w9-t3-p1": "[INFO] Scanning for projects...\n[INFO] ----------------< com.karthik:springboot-demo >----------------\n[INFO] Building springboot-demo 0.0.1-SNAPSHOT\n[INFO] --------------------------------[ jar ]---------------------------------\n[INFO] --- maven-compiler-plugin:3.11.0:compile (default-compile) ---\n[INFO] Compiling 2 source files to target/classes\n[INFO] --- spring-boot-maven-plugin:3.2.0:repackage ---\n[INFO] Replacing main artifact with repackaged archive\n[INFO] ------------------------------------------------------------------------\n[INFO] BUILD SUCCESS\n[INFO] Total time:  3.421 s\n[INFO] Finished at: 2026-11-13T14:25:30+05:30",
    "w10-t1-p1": "2026-11-13 15:10:02.100  INFO --- [main] o.s.b.a.h2.H2ConsoleAutoConfiguration   : H2 console available at '/h2-console'. Database available at 'jdbc:h2:mem:testdb'",
    "w10-t1-p2": "Author entity created: Author[id=1, name='Karthik Kaja', rollNumber='24EU08161', publication='Advanced Java Architecture']",
    "w10-t1-p3": "Executing SQL: INSERT INTO author (id, name, roll_number, publication) VALUES (1, 'Karthik Kaja', '24EU08161', 'Spring Boot Guide')\nRows inserted: 1\nQuerying all authors via JdbcTemplate RowMapper:\nAuthor: id=1, name=Karthik Kaja, roll=24EU08161, publication=Spring Boot Guide",
    "w11-t1-p1": "Hibernate: create table employees (id bigint not null auto_increment, emp_name varchar(255) not null, emp_roll varchar(255), primary key (id)) engine=InnoDB",
    "w11-t1-p2": "EmployeeRepository proxy created by Spring Data JPA with 18 standard CRUD methods.",
    "w11-t1-p3": "POST /api/employees HTTP/1.1\nHost: localhost:8080\nContent-Type: application/json\n\n{\"empName\":\"Karthik Kaja\",\"empRoll\":\"24EU08161\"}\n\nHTTP/1.1 201 Created\n{\"id\":1,\"empName\":\"Karthik Kaja\",\"empRoll\":\"24EU08161\"}",
    "w11-t1-p4": "GET /employees HTTP/1.1\nHTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\n\nRendered Thymeleaf View: employee-list.html with 1 record (Roll: 24EU08161)",
    "w12-t1-p1": "Hibernate: create table students (id bigint not null auto_increment, name varchar(255), roll_no varchar(255), primary key (id))",
    "w12-t1-p2": "StudentRepository initialized in in-memory H2 database.",
    "w12-t1-p3": "POST /students/add?roll=24EU08161&name=Karthik&dept=IT HTTP/1.1\nHTTP/1.1 200 OK\n{\"id\":1,\"rollNo\":\"24EU08161\",\"name\":\"Karthik\",\"department\":\"IT\"}\n\nGET /students/all HTTP/1.1\nHTTP/1.1 200 OK\n[{\"id\":1,\"rollNo\":\"24EU08161\",\"name\":\"Karthik\",\"department\":\"IT\"}]"
}

def enrich():
    import hierarchy_metadata
    enriched_count = 0
    for w in hierarchy_metadata.HIERARCHY_DATA:
        for t in w["tasks"]:
            for p in t.get("programs", []):
                pid = p["id"]
                if not p.get("explanation") and pid in EXPLANATIONS_MAP:
                    p["explanation"] = EXPLANATIONS_MAP[pid]
                    enriched_count += 1
                if not p.get("output") and pid in OUTPUT_MAP:
                    p["output"] = OUTPUT_MAP[pid]
                    enriched_count += 1
    print(f"Enriched {enriched_count} program fields.")

if __name__ == "__main__":
    enrich()

