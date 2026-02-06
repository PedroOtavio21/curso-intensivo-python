"""
10.2 – Aprendendo C: 

Você pode usar o método replace() para substituir
qualquer palavra por uma palavra diferente em uma string. Eis um exemplo rápido
que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
> message = "I really like dogs."
> message.replace('dog', 'cat')
'I really like cats.'
Leia cada linha do arquivo learning_python.txt que você acabou de criar e
substitua a palavra Python pelo nome de outra linguagem, por exemplo, C. Mostre
cada linha modificada na tela.
"""

path_exercise = './parte_1_fundamentos/capitulo_10/exercicios/ex_10_1/learning_python.txt'

with open(path_exercise) as path_object:
    file_content = path_object.readlines()

for line in file_content:
    modified_line = line.strip().replace('Python', 'C')
    print(modified_line)
