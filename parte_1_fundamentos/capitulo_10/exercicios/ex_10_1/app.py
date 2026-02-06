"""
10.1 – Aprendendo Python: 

Abra um arquivo em branco em seu editor de texto e
escreva algumas linhas que sintetizem o que você aprendeu sobre Python até
agora. Comece cada linha com a expressão Em Python podemos.... Salve o
arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios
deste capítulo. Escreva um programa que leia o arquivo e mostre o que você
escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez
percorrendo o objeto arquivo com um laço e outra armazenando as linhas em uma
lista e então trabalhando com ela fora do bloco with.
"""

from pathlib import Path

path_exercise = './parte_1_fundamentos/capitulo_10/exercicios/ex_10_1/learning_python.txt'

# Leitura 1
file = ''
with open(path_exercise) as path_object:
    file = path_object.read()

print(file)

# Leitura 2
with open(path_exercise) as path_object:
    for line in path_object:
        print(line)

# Leitura 3
with open(path_exercise) as path_object:
    lines = path_object.readlines()

for line in lines:
    print(line)