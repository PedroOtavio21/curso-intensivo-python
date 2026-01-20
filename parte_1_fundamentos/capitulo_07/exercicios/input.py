"""
7.1 – Locação de automóveis: 

Escreva um programa que pergunte ao usuário qual
tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse carro, por
exemplo, “Deixe-me ver se consigo um Subaru para você.”
"""

car = input('Me diga qual tipo de carro gostaria de alugar: ')
print('Deixe-me ver se consigo um ' + car + ' para você')

"""
7.2 – Lugares em um restaurante: 

Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta.
"""

number_of_persons = input('Quantas pessoas estão em seu grupo? ')
if int(number_of_persons) > 8:
    print('Você terá de esperar uma mesa ser liberada')
else:
    print('Temos uma mesa a sua espera!')

"""
7.3 – Múltiplos de dez: 

Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.
"""

number = input('Insira um valor qualquer: ')
number = int(number)
if number % 10 == 0:
    print('Seu número é múltiplo de 10!')
else:
    print('Seu número não é múltiplo de 10')
