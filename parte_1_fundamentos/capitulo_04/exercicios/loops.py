"""
4.1 – Pizzas: 

Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
pizza.
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez
de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na
saída contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe
quanto você gosta de pizza. A saída deve ser constituída de três ou mais linhas
sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo,
Eu realmente adoro pizza!
"""

pizzas = ["Calabresa", "Mussarela", "Carne de Sol"]

for pizza in pizzas:
    print('Gosto de pizza de ' + pizza)
print('Eu realmente adoro pizza!')

"""
4.2 – Animais: 

Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo,
Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses animais
têm em comum. Você poderia exibir uma frase como Qualquer um desses
animais seria um ótimo animal de estimação!
"""

animals = ["Tigre", "Cachorro", "Jacaré"]
for animal in animals:
    print('Um ' + animal + ' seria um ótimo animal de estimação!')
print('Qualquer um desses animais seria um ótimo animal de estimação!')

"""
4.3 – Contando até vinte: 

Use um laço for para exibir os números de 1 a 20,
incluindo-os.
"""
print('Contando de um até 20:')
for value in range(1, 21):
    print(value)

"""
4.4 – Um milhão: 

Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais, interrompa
pressionando CTRL-C ou feche a janela de saída.)
"""

print('Contando de 1 até 1 milhão')
for value in (1, 1000001):
    print(value)

"""
4.5 – Somando um milhão: 

Crie uma lista de números de um a um milhão e, em
seguida, use min() e max() para garantir que sua lista realmente começa em um e
termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com
que Python é capaz de somar um milhão de números.
"""

numbers = [value for value in range(1, 1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

"""
4.6 – Números ímpares: 

Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os
números.
"""

print('Printando valores ímpares de 1 a 20:\n')
for value in range(1, 21, 2):
    print(value)

"""
4.7– Três: 

Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.
"""

multiplos_de_tres = [value * 3 for value in range(1, 11)]
for value in multiplos_de_tres:
    print(value)

"""
4.8 – Cubos: 

Um número elevado à terceira potência é chamado de cubo. Por
exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
para exibir o valor de cada cubo.
"""

for value in range(1, 11):
    print(value ** 3)

"""
4.9 – Comprehension de cubos: 

Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
"""

dez_cubos = [value ** 3 for value in range(1, 11)]