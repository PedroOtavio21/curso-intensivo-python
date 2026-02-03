"""
9.14 – Dados: 

O módulo random contém funções que geram números aleatórios
de várias maneiras. A função randint() devolve um inteiro no intervalo
especificado por você. O código a seguir devolve um número entre 1 e 6:
from random import randint
x = randint(1, 6)
Crie uma classe Die com um atributo chamado sides, cujo valor default é 6.
Escreva um método chamado roll_die() que exiba um número aleatório entre 1 e
o número de lados do dado. Crie um dado de seis dados e lance-o dez vezes.
Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez vezes.
"""

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

def roll_test(sides=6):
    new_die = Die(sides)
    count = 1
    print(f'Rodando dado de {sides} lados!')
    while count < 11:
        print(f'- Valor atingido: {new_die.roll_die()}')
        count += 1
    print('-----')

roll_test()
roll_test(10)
roll_test(20)