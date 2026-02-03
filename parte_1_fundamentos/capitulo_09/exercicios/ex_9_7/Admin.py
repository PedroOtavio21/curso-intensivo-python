"""
9.7 – Admin: 

Um administrador é um tipo especial de usuário. Escreva uma classe
chamada Admin que herde da classe User escrita no Exercício 9.3 (página 226),
ou no Exercício 9.5 (página 232). Adicione um atributo privileges que armazene
uma lista de strings como "can add post", "can delete post" "can ban user",
e assim por diante. Escreva um método chamado show_privileges() que liste o
conjunto de privilégios de um administrador. Crie uma instância de Admin e chame
seu método.
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

class Admin(User):
    def __init__(self, first_name, last_name, user_name, registration):
        super().__init__(first_name, last_name, user_name, registration)
        self.privileges = []

    def add_privileges(self, *privileges):
        # self.privileges = [privilege for privilege in privileges]
        self.privileges.extend(privileges)
    
    def show_privileges(self):
        print('Privilégios do administrados:')
        for privilege in self.privileges:
            print(f'-{privilege}')

pedro_admin = Admin('pedro', 'otávio', 'pedro_21', 2021)
pedro_admin.add_privileges('can add post', 'can delete post')
pedro_admin.show_privileges()