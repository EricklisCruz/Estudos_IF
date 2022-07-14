# Java-EE
Atividades da disciplina de Programa Web II utilizando JAVA EE

- Questão 01
            <ul>
              <li>Criar um formulário de (cadastro.jsp) com os seguintes campos: Nome, sobrenome, usuário, senha, telefone.</li>
              <li>Criar um servlet (cad_registro) para receber os dados do formulário (cadastro.jsp).</li>
              <li>Verificar se todos os campos do formulário foram preenchidos; (Dica: isEmpty()).</li>
              <li>Se os campos do formulário estiverem vazios, ao enviar o formulário, este deve voltar para a página (cadastro.jsp).</li>
              <li>Se os campos estiverem preenchidos, o usuário deverá ser direcionada para uma outa página (sucesso.jsp), com uma mensagem de boas vindas! (Dica: RequestDispatcher).</li>
            </ul>
            
           
    
- Questão 02
          <ul>
            <li>Assim como o formulário de cadastro, criar um formulário (acesso.jsp), com os campos: usuário e senha.
            <li> Cria uma servlet (verifica) para receber os dados do formulário (acesso.jsp).
            <li>Verificar se todos os campos do formulário foram preenchidos e os dados preenchidos são (usuário: admin, senha: adm123); (Dica: isEmpty() e equals()).
            <li>Se os campos foram preenchidos corretamente, redirecionar para outra página (login_sucesso.jsp), com uma mensagem "seja bem, usuário!".
            <li>Se os campos estiverem vazios ou usuário e senha incorretos, mostrar uma mensagem na tela "Usuário ou Senha Incorretos", voltar para a página principal (acesso.jsp).
            </ul>
