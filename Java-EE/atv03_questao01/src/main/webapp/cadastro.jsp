<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Cadastro</title>
</head>
<body>
	<form action="cad_registro" method="post">
		<fieldset>
			<legend><h1>Cadastro</h1></legend>
			<label>Nome</label>
			<input type="text" name="nome" placeholder="Digite o seu nome"> <br><br>
			
			<label>Sobrenome</label>
			<input type="text" name="sobrenome" placeholder="Digite o seu sobrenome"> <br><br>
			
			<label>Usuário</label>
			<input type="email" name="email" placeholder="Digite o seu email"> <br><br>
			
			<label>senha</label>
			<input type="password" name="senha" placeholder="Digite a sua senha"> <br><br>
			
			<label>Telefone</label>
			<input type="text" name="telefone" placeholder="Digite o seu telefone"> <br><br>
			<input type="submit" value="Cadastrar">
		</fieldset>
	</form>

</body>
</html>