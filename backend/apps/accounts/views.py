from dj_rest_auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    """
        Verifica as credenciais e retorne o token REST
        se as credenciais são válidas e autenticadas.   
        Chama o método de login do Django Auth para registrar o ID do usuário
        no framework de sessão Django

        Aceita os seguintes parâmetros via POST: email e senha
        Retorna a chave o Token do REST Framework.
    """

    
