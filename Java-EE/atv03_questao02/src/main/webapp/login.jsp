<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Login</title>
</head>
<body>

	<form action="login" method="post">
		<fieldset>
			<legend><h1>Login</h1></legend>
			<label>Usuário</label>
			<input type="email" name="email" placeholder="Digite o seu email"> <br><br>
			
			<label>senha</label>
			<input type="password" name="senha" placeholder="Digite a sua senha"> <br><br>
			
			<input type="submit" value="Login">
		</fieldset>
	</form>
