"""
10.6 – Adição: 

Um problema comum quando pedir entradas numéricas ocorre
quando as pessoas fornecem texto no lugar de números. Ao tentar converter a
entrada para um int, você obterá um TypeError. Escreva um programa que peça
dois números ao usuário. Some-os e mostre o resultado. Capture o TypeError caso
algum dos valores de entrada não seja um número e apresente uma mensagem de
erro simpática. Teste seu programa fornecendo dois números e, em seguida, digite
um texto no lugar de um número.
"""

def adicionar(num_1, num_2):
    try:
        result = num_1 + num_2
    except TypeError:
        return 'Um ou dois dos valores apresentados não é de tipo numérico.'
    else:
        return result
    
# print(adicionar(5, 6))
# print(adicionar(5, '6'))