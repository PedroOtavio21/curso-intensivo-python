"""
10.5 – Enquete sobre programação: 

Escreva um laço while que pergunte às
pessoas por que elas gostam de programação. Sempre que alguém fornecer um
motivo, acrescente-o em um arquivo que armazene todas as respostas.
"""

from pathlib import Path

file_path = Path(__file__).parent / 'responses.txt'

# Criando o arquivo
with open(file_path, 'w') as file_object:
    file_object.write('Porquê vocês gostam de programação?\n')

# Adicionando respostas
while True:
    with open(file_path, 'a') as file_object:
        name_person = input('Me diga o seu primeiro nome: ')
        new_response = input('Me explique o motivo de você gostar de programação: ')
        file_object.write(f'- {name_person}: {new_response}\n')
        confirm = input('Você deseja inserir uma nova resposta para a enquete (sim/não)? ')
        if confirm == 'não' or confirm == 'nao':
            break

# Lendo respostas
with open(file_path) as file_object:
    lines = file_object.readlines()

print('\nSegue abaixo as respostas da enquete realizada:\n')
for line in lines:
    print(line.split())