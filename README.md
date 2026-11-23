# Advanced Java Programming Lab Record (24IT385)
## Interactive 3-Level Week-Wise Digital Engineering Laboratory Record (Week 0 – Week 13)

A comprehensive, interactive digital engineering laboratory record website built for **Advanced Java Programming Lab (24IT385)** at **Siddhartha Academy of Higher Education**, adhering to the structural layout and navigation experience of the academic reference portal (`https://sahelms.vrsiddhartha.ac.in/java/238W1A1275/`) while strictly preserving the existing **Emerald Documentation Theme** (`#059669`, `#10B981`, `#047857`, `#022C22`).

---

## 👨‍🎓 Candidate & Course Information

- **Student Name:** Venkata Sai Karthikeya Kaja
- **Roll Number:** 24EU08161
- **Department:** Information Technology
- **Course Title:** Advanced Java Programming Lab
- **Course Code:** 24IT385
- **Academic Year:** 2026–2027
- **Institution:** Siddhartha Academy of Higher Education

---

## 🏛️ Architectural Layout & Navigation Features

The portal follows the structural organization of the reference laboratory portal adapted to the Emerald design system:

### 1. Centered Top Navigation Header
- **Main Heading:** `ADVANCED JAVA PROGRAMMING` (centered, prominent typography)
- **Subtitle:** `Roll Number: 24EU08161` (centered directly beneath heading)
- **Interactive Profile Dropdown:** Positioned at the top right with avatar trigger (`assets/images/profile.png`), displaying candidate details on click:
  - Name: Venkata Sai Karthikeya Kaja
  - Roll Number: 24EU08161
  - Department: Information Technology
  - Institution: Siddhartha Academy of Higher Education
  - Course: Advanced Java Programming Lab (24IT385)
  - Academic Year: 2026–2027

### 2. Left Sidebar — "Lab Contents" (3-Level Navigation Hierarchy)
- **Sidebar Header:** `<i class="bi bi-journal-code"></i> Lab Contents`
- **Real-Time Search Bar:** Live input `#weekSearchInput` filtering simultaneously across Weeks, Tasks, and Individual Programs.
- **Level 1 (Weeks):** Accordion items for `WEEK 0` through `WEEK 13` with pill indicators (`W0` to `W13`) and expand arrows (`›`).
- **Level 2 (Tasks):** Direct task headings under each week (e.g. `Task 1: JDBC CRUD Operations`, `Task 2: Cookies Using Java Servlets`).
- **Level 3 (Programs):** Individual program and script links under each task with dot indicators (`.prog-dot`), enabling instant jump and scroll to specific program cards:
  - Example: `P1: INSERT Operation` → `#w6-t1-p1`
  - Example: `P2: SELECT Operation` → `#w6-t1-p2`
  - Example: `P3: UPDATE Operation` → `#w6-t1-p3`
  - Example: `P4: DELETE Operation` → `#w6-t1-p4`

### 3. Quick-Jump In-Page Secondary TOC Bar
- Sticky navigation bar providing one-click jump to each section on the current page:
  `🎯 Aim` | `⚙️ Requirements` | `🔧 Procedure` | `💻 Programs` | `📸 Step Screenshots` | `🏆 Result` | `📊 Result Analysis`

### 4. Program-by-Program Documentation Cards (`.program-card`)
Every program across all 14 weeks is presented in its own dedicated card structure:
- **Card Header:** Program number badge (`Program 1`), program title, and technology/type tag.
- **Objective Box:** Highlighted callout defining the program's specific functional objective.
- **Database Setup SQL Box:** Syntax-highlighted SQL block with copy button for table schemas, constraints, and initial records.
- **Source Code Viewer:** Windows / NetBeans / STS IDE tab with file icon, filename, Copy Code button, and Download Code button (**strictly zero Mac-style dots**).
- **Technical Explanation Table:** Structured table with headers `Component / Method / Annotation` and `Technical Explanation & Architectural Role`.
- **Execution Verification & Output Box:** Terminal / console simulation bar with dark background, output logs, and candidate roll number verification (`24EU08161`).
- **Verification Callout:** Confirmation of successful compilation and test execution.

### 5. Step-by-Step Practical Screenshot Galleries (234 Screenshots)
- Dedicated execution galleries for all practical laboratory weeks (Weeks 2–13) totaling **234 realistic high-resolution screenshots**.
- Each step card includes:
  - Step Number Badge (`Step 01`, `Step 02`...)
  - Step Title
  - High-Resolution Screenshot (`assets/images/week-X/task-Y/step-ZZ.png`)
  - Technical Step Description
  - Fullscreen Zoom Modal trigger (`🔍 Fullscreen`)
  - Direct Download button (`⬇ Download`)

### 6. Engineering Result Analysis (4-Card Technical Grid)
Four standardized evaluation cards at the end of each task:
1. **Execution & Latency Analysis:** Socket overhead, connection pool latency, bytecode caching, memory footprint.
2. **Architectural Trade-offs:** Type 1 vs Type 4 drivers, ORM abstraction vs raw SQL, stateless HTTP lifecycles.
3. **Exception & Edge Case Handling:** Try-with-resources closing, SQLException evaluation, rollback semantics.
4. **Industrial Standards & Scalability:** Enterprise specifications, DAO patterns, thread safety, ACID guarantees.

---

## 🧪 Laboratory Curriculum Mapping (Week 0 – Week 13)

| Week | Title & Focus | Tasks | Programs & Scripts | Step Screenshots | Output Verification |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **0** | **Advanced Java Introduction & Theory** | 1 | 5 Modules | Conceptual | Architecture & Q&A Matrices |
| **1** | **Comparative Paradigm Evaluation** | 1 | 1 Matrix | Conceptual | Multi-Language Benchmarks |
| **2** | **Java Environment Setup in Ubuntu** | 1 | 1 Script | 16 Steps | Terminal JDK 26 Verification |
| **3** | **Java MS Access Connectivity (UCanAccess)** | 1 | 1 Program | 16 Steps | Command Prompt & MS Access |
| **4** | **Remote MySQL Database Connectivity** | 1 | 1 Program | 16 Steps | NetBeans 8.2 Execution |
| **5** | **Remote MySQL Database Operations** | 1 | 1 Program | 16 Steps | NetBeans Transactions & Socket Teardown |
| **6** | **JDBC Student CRUD Operations** | 1 | 4 Programs | 18 Steps | MySQL CLI & NetBeans 8.2 |
| **7** | **Generic Servlet and HTTP Servlet** | 6 | 6 Programs | 19 Steps | Authentic NetBeans 8.2 & IE Browser |
| **8** | **Advanced Java Web Applications (SMS & Cookies)** | 2 | 8 Programs | 28 Steps | Tomcat SMS CRUD & Cookie Headers |
| **9** | **Maven & Spring Boot Development in STS** | 3 | 3 Programs | 39 Steps | STS 4, REST Controller & POM.xml |
| **10** | **Spring Boot JdbcTemplate with H2** | 1 | 3 Programs | 16 Steps | H2 Web Console & RowMapper Logs |
| **11** | **Spring Boot JPA with MySQL** | 1 | 4 Programs | 16 Steps | MySQL Tables & Thymeleaf UI |
| **12** | **Spring Data JPA Repository Operations with H2** | 1 | 3 Programs | 16 Steps | In-Memory H2 REST Endpoints |
| **13** | **Derived and Custom Query Methods in JPA** | 1 | 1 Program | 18 Steps | 8 Derived & Native Queries |
| **Total** | **Full Engineering Laboratory Record** | **21 Tasks** | **38 Programs** | **234 Screenshots** | **100% Roll 24EU08161 Verified** |

---

## 📁 Repository Organization

```
JAVA-WEB-main/
│
├── index.html                   ← Master Interactive Portal (14 Dynamic Week Panes, Deep Program Anchoring)
├── style.css                    ← Global Emerald Theme, 3-Level Sidebar, Profile Dropdown & Modal Styles
├── script.js                    ← Portal Controller (Pane Switcher, Search Filter, Modal Zoom, Copy/Download)
├── README.md                    ← Authoritative Project Documentation
├── build_3level_portal.py       ← Master Portal & Standalone Page Generator
├── hierarchy_metadata.py        ← Comprehensive 3-Level Curriculum Tree Data
├── step_gallery_data.py         ← Metadata for 234 Practical Step Screenshots
├── validate_lab_record.py       ← Comprehensive Automated Validation Test Suite
├── verify_portal.py             ← Structural & Content Verification Engine
│
├── pages/                       ← 14 Standalone Laboratory Record Pages
│   ├── week-0.html              ← Advanced Java Foundations & Theory
│   ├── week-1.html              ← Comparative Paradigm Evaluation Matrix
│   ├── week-2.html              ← OpenJDK & Oracle JDK SE 26 on Ubuntu Linux
│   ├── week-3.html              ← Java MS Access Connectivity via UCanAccess
│   ├── week-4.html              ← Remote MySQL Database Connectivity
│   ├── week-5.html              ← Remote MySQL Database Operations
│   ├── week-6.html              ← Complete Student JDBC CRUD Operations
│   ├── week-7.html              ← GenericServlet & HttpServlet in NetBeans 8.2
│   ├── week-8.html              ← Student Management System (SMS) & Cookies
│   ├── week-9.html              ← Maven & Spring Boot in Spring Tool Suite (STS)
│   ├── week-10.html             ← Spring Boot JdbcTemplate with In-Memory H2
│   ├── week-11.html             ← Spring Boot JPA with MySQL & Thymeleaf
│   ├── week-12.html             ← Spring Data JPA with In-Memory H2
│   └── week-13.html             ← Derived & Custom Query Methods in JPA
│
└── assets/
    ├── css/topic-page.css       ← Emerald Topic Page Stylesheet
    ├── downloads/               ← Authoritative Java, SQL, Script & Config Files
    └── images/                  ← 234 Practical Execution Screenshots Organized by Week & Task
        ├── profile.png          ← Student Avatar (Roll: 24EU08161)
        ├── week-2/task-1/       ← 16 Ubuntu Terminal Screenshots
        ├── week-3/task-1/       ← 16 Windows CMD & MS Access Screenshots
        ├── week-4/task-1/       ← 16 NetBeans Remote MySQL Screenshots
        ├── week-5/task-1/       ← 16 NetBeans Remote Operations Screenshots
        ├── week-6/task-1/       ← 18 MySQL CLI & CRUD Screenshots
        ├── week-7/task-1..6/    ← 19 Authentic NetBeans 8.2 & IE Screenshots
        ├── week-8/task-1..2/    ← 28 SMS & Cookie Screenshots
        ├── week-9/task-1..3/    ← 39 STS & Spring Boot Screenshots
        ├── week-10/task-1/      ← 16 STS & H2 Console Screenshots
        ├── week-11/task-1/      ← 16 STS, MySQL & Thymeleaf Screenshots
        ├── week-12/task-1/      ← 16 STS & H2 REST Screenshots
        └── week-13/task-1/      ← 18 STS & Derived Query Screenshots
```

---

## ⚙️ Automated Quality Verification

To run automated validation across all 15 portal HTML files, images, downloads, and identity consistency:

```bash
# Run comprehensive image, download, and roll number validation
python validate_lab_record.py

# Run structural portal verification (Headers, 3-Level Sidebars, Step Cards, No Mac Dots)
python verify_portal.py
```

**Validation Output:**
- `ALL 14 WEEK PAGES PRESENT!`
- `Verified 262 image references in week pages. Errors: 0`
- `ALL PAGES STRICTLY USE ROLL NUMBER 24EU08161!`
- `ALL 15 PORTAL HTML FILES PERFECT: True (0 Mac-style dots detected)`
