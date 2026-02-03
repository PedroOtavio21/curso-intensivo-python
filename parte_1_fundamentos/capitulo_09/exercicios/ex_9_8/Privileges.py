"""
9.8 – Privilégios: 

Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie uma
instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios.
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
            f'\nNome - {self.first_name.title()}\nSobrenome - {self.last_name.title()}\nNome de Usuário - {self.user_name}\nAno de Registro - {str(self.registration)}'
        )
    
    def greet_user(self):
        print(f'Olá {self.user_name}! Bem-vindo a nossa aplicação!')

class Privileges():
    def __init__(self):
        self.privileges = []

    def add_privileges(self, *privileges):
        self.privileges.extend(privileges)

    def show_privileges(self):
        print('Principais privilégios:')
        for privilege in self.privileges:
            print(f'-{privilege}')

class Admin(User):
    def __init__(self, first_name, last_name, user_name, registration):
        super().__init__(first_name, last_name, user_name, registration)
        self.privileges = Privileges()

admin = Admin('pedro', 'otávio', 'pedro_21', 2021)
admin.privileges.add_privileges('can add post', 'can delete post', 'can ban user')
admin.privileges.show_privileges()