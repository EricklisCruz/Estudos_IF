package br.com.edu.ifsertaope;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Cad_registro
 */
@WebServlet("/cad_registro")
public class Cad_registro extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Cad_registro() {
        super();
    }

	/**
	 * @see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String nome = request.getParameter("nome");
		String sobrenome = request.getParameter("sobrenome");
		String usuario = request.getParameter("email");
		String senha = request.getParameter("senha");
		String telefone = request.getParameter("telefone");
		
		
		if((nome.isEmpty() || sobrenome.isEmpty() || usuario.isEmpty() 
				|| senha.isEmpty() || telefone.isEmpty())) {
			RequestDispatcher rd = request.getRequestDispatcher("cadastro.jsp");
			rd.forward(request,response);
			
		}else {
			
			RequestDispatcher rd = request.getRequestDispatcher("sucesso.jsp");
					rd.forward(request,response);
			
		}
	}

}
