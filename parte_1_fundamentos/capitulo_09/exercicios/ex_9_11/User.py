class User():
    def __init__(self, first_name, last_name, user_name, registration):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.registration = registration

    def describe_user(self):
        print('\n-- Resumo de informações do usuário: --')
        print(
            f'\nNome - {self.first_name.title()}\nSobrenome - {self.last_name.title()}\nNome de Usuário - {self.user_name}\nAno de Registro - {str(self.registration)}'
        )
    
    def greet_user(self):
        print(f'Olá {self.user_name}! Bem-vindo a nossa aplicação!')