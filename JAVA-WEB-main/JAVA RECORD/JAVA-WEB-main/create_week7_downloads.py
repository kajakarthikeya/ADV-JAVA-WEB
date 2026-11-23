import os

downloads_dir = r"c:\Users\Vineeth Akkinapalli\Downloads\KARTHIK\JAVA-WEB-main\JAVA-WEB-main\assets\downloads"
os.makedirs(downloads_dir, exist_ok=True)

files = {
    "NewServlet.java": """import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Advanced Java Programming Lab - Week 7
 * Student: Venkata Sai Karthikeya Kaja
 * Roll Number: 24EU08161
 */
@WebServlet(name = "NewServlet", urlPatterns = {"/NewServlet"})
public class NewServlet extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Student Details</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>ADVANCED JAVA LAB</h1>");
            out.println("<h2>STUDENT DETAILS</h2>");
            out.println("<p><b>Roll Number:</b> 24EU08161</p>");
            out.println("<p><b>Subject:</b> Advanced Java</p>");
            out.println("<p><b>Lab:</b> Advanced Java Lab</p>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }
}
""",

    "GetPostServlet.java": """import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Advanced Java Programming Lab - Week 7: GET and POST Demonstration
 * Student: Venkata Sai Karthikeya Kaja (24EU08161)
 */
@WebServlet("/GetPostServlet")
public class GetPostServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        String name = request.getParameter("name");
        out.println("<h2>GET Request</h2>");
        out.println("<p>Hello " + (name != null ? name : "Guest") + "!</p>");
        out.println("<p>This is a GET request.</p>");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        String name = request.getParameter("name");
        out.println("<h2>POST Request</h2>");
        out.println("<p>Hello " + (name != null ? name : "Guest") + "!</p>");
        out.println("<p>This is a POST request.</p>");
    }
}
""",

    "MyGenericServlet.java": """import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.GenericServlet;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebServlet;

/**
 * Advanced Java Programming Lab - Week 7: Generic Servlet Implementation
 * Student: Venkata Sai Karthikeya Kaja (24EU08161)
 */
@WebServlet("/MyGenericServlet")
public class MyGenericServlet extends GenericServlet {

    @Override
    public void service(ServletRequest request, ServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<body>");
        out.println("<h2>Generic Servlet</h2>");
        out.println("<p>This servlet extends GenericServlet.</p>");
        out.println("<p>Hello from GenericServlet!</p>");
        out.println("</body>");
        out.println("</html>");
    }
}
""",

    "LifeCycleServlet.java": """import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.Servlet;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebServlet;

/**
 * Advanced Java Programming Lab - Week 7: Servlet Lifecycle
 * Student: Venkata Sai Karthikeya Kaja (24EU08161)
 */
@WebServlet("/LifeCycleServlet")
public class LifeCycleServlet implements Servlet {

    public void init(ServletConfig config) throws ServletException {
        System.out.println("init() method called");
    }

    public ServletConfig getServletConfig() {
        return null;
    }

    public void service(ServletRequest request, ServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<h2>Servlet Life Cycle</h2>");
        out.println("<p><b>init():</b> Servlet Initialized</p>");
        out.println("<p><b>service():</b> Request Processed</p>");
        out.println("<p><b>destroy():</b> Servlet Destroyed</p>");
    }

    public String getServletInfo() {
        return "Life Cycle Servlet";
    }

    public void destroy() {
        System.out.println("destroy() method called");
    }
}
""",

    "StudentFormServlet.java": """import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Advanced Java Programming Lab - Week 7: Student Registration Form Handler
 * Student: Venkata Sai Karthikeya Kaja (24EU08161)
 */
@WebServlet("/StudentFormServlet")
public class StudentFormServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String name = request.getParameter("name");
        String rollno = request.getParameter("rollno");
        String dept = request.getParameter("dept");

        out.println("<html>");
        out.println("<body>");
        out.println("<h2>Student Details</h2>");
        out.println("<p><b>Name:</b> " + name + "</p>");
        out.println("<p><b>Roll No:</b> " + rollno + "</p>");
        out.println("<p><b>Department:</b> " + dept + "</p>");
        out.println("</body>");
        out.println("</html>");
    }
}
"""
}

for fname, content in files.items():
    p = os.path.join(downloads_dir, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created download file: {fname}")

print("All Week 7 source download files generated!")
