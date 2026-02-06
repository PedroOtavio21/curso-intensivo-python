"""
10.7 – Calculadora para adição: 

Coloque o código do Exercício 10.6 em um
laço while para que o usuário possa continuar fornecendo números, mesmo se
cometerem um erro e digitarem um texto no lugar de um número.
"""


def adicionar(num_1, num_2):
    try:
        result = num_1 + num_2
    except TypeError:
        return 'Um ou dois dos valores apresentados não é de tipo numérico.'
    else:
        return result
    
while True:
    num_1 = input('Insira o primeiro número: ')
    num_2 = input('Insira o segundo número: ')

    print('Resultado:')
    print(f'- {adicionar(num_1, num_2)}')

    confirm = input('Deseja continuar somando? (sim-"s"/não-"n")').lower().strip()
    if confirm == 'n':
        break
