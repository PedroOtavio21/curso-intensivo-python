"""
10.4 – Lista de convidados: 

Escreva um laço while que pergunte o nome aos
usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
acrescente uma linha que registre a visita do usuário em um arquivo chamado
guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
arquivo.
"""

from pathlib import Path

file_path = Path(__file__).parent / 'guest_book.txt'
new_user = ''
print('Olá, bem-vindo a lista de chamada de novos usuários!')
message = ''

with open(file_path, 'w') as file_object:
    while True:
        confirm = ''
        new_user = input('Insira o seu nome: ')
        message = input('Deseja inserir um novo usuário (sim/não)? ').strip().lower()
        file_object.write(f'- {new_user}\n')
        if message == 'não' or message == 'nao':
            break

with open(file_path) as file_object:
    lines = file_object.readlines()

print('Segue abaixo a lista criada anteriormente:')
for line in lines:
    print(line.strip())