package br.com.edu.ifsertaope;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Login
 */
@WebServlet("/login")
public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Login() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		String usuario = request.getParameter("email");
		String senha = request.getParameter("senha");
		
		String usuariocad = "admin@gmail.com";
		String senhacad = "1234567890";
		
		if((!(usuario.isEmpty() || senha.isEmpty())) && 
				((usuario.equals(usuariocad) && senha.equals(senhacad)))) {
			RequestDispatcher rd = request.getRequestDispatcher("loginsucesso.jsp");
			rd.include(request,response);
			
			response.getWriter().append("<h1> Seja bem-vindo, " + usuario + "</h1>");
			response.getWriter().append("</body>");
			response.getWriter().append("</html>");
				
			
		}else {
			RequestDispatcher rd = request.getRequestDispatcher("login.jsp");
			rd.include(request,response);
			response.getWriter().append("<h1> Email ou senha incorretas!</h1>");
			response.getWriter().append("</body>");
			response.getWriter().append("</html>");
			
		}
	}

}
