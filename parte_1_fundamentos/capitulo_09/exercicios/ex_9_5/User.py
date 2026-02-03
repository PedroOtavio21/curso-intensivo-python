"""
9.5 – Tentativas de login: 

Acrescente um atributo chamado login_attempts à sua
classe User do Exercício 9.3 (página 226). Escreva um método chamado
increment_login_attempts() que incremente o valor de login_attempts em 1.
Escreva outro método chamado reset_login_attempts() que reinicie o valor de
login_attempts com 0.
Crie uma instância da classe User e chame increment_login_attempts()
várias vezes. Exiba o valor de login_attempts para garantir que ele foi
incrementado de forma apropriada e, em seguida, chame
reset_login_attempts(). Exiba login_attempts novamente para garantir que
seu valor foi reiniciado com 0.
"""

class User():
    def __init__(self, first_name, last_name, user_name, registration):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.registration = registration
        self.login_attempts = 0

    def describe_user(self):
        print('\n-- Resumo de informações do usuário: --')
        print(
            f'\nNome - {self.first_name}\nSobrenome - {self.last_name}\nNome de Usuário - {self.user_name}\nAno de Registro - {str(self.registration)}'
        )
    
    def greet_user(self):
        print(f'Olá {self.user_name}! Bem-vindo a nossa aplicação!')

    def get_login_attempts(self):
        return self.login_attempts
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

pedro = User('pedro', 'otávio', 'pedro_21', 2021)
pedro.increment_login_attempts()
pedro.increment_login_attempts()
pedro.increment_login_attempts()
pedro.increment_login_attempts()
pedro.increment_login_attempts()
print(f'Tentativas de login: {str(pedro.get_login_attempts())}')
pedro.reset_login_attempts()
print(f'Tentativas de login: {str(pedro.get_login_attempts())}')