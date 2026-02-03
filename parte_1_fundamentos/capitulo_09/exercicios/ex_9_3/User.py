"""
9.3 – Usuários: 

Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada ao
usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário.
"""

class User():
    def __init__(self, first_name, last_name, user_name, registration):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.registration = registration

    def describe_user(self):
        print('\n-- Resumo de informações do usuário: --')
        print(
            f'\nNome - {self.first_name}\nSobrenome - {self.last_name}\nNome de Usuário - {self.user_name}\nAno de Registro - {str(self.registration)}'
        )
    
    def greet_user(self):
        print(f'Olá {self.user_name}! Bem-vindo a nossa aplicação!')

pedro_ota = User('pedro', 'otávio', 'pedro_ota', 2025)
ant_onio_123 = User('antonio', 'sanches', 'ant_onio_123', 2014)
luis_fellas = User('luis', 'felipe', 'luis_fellas', 2024)

pedro_ota.describe_user()
pedro_ota.greet_user()

ant_onio_123.describe_user()
ant_onio_123.greet_user()

luis_fellas.describe_user()
luis_fellas.greet_user()
