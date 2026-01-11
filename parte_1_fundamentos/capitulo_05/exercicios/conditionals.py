"""
5.1 – Testes condicionais: 

Escreva uma série de testes condicionais. Exiba uma
frase que descreva o teste e o resultado previsto para cada um. Seu código deverá
ser semelhante a:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Observe atentamente seus resultados e certifique-se de que compreende por que
cada linha é avaliada como True ou False.
• Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como True e
outros cinco avaliados como False.
"""

car = 'celta'
print('O car == "subaru"? Eu prevejo que é False')
print(car == 'subaru')

print('O car == "corsa"? Eu prevejo que é False')
print(car == 'corsa')

print('O car == "palio"? Eu prevejo que é False')
print(car == 'palio')

print('O car == "hb20"? Eu prevejo que é False')
print(car == 'hb20')

print('O car == "focus"? Eu prevejo que é False')
print(car == 'focus')

car = 'onix'
print('O car == "onix"? Eu prevejo que é False')
print(car == 'onix')

car = 'kicks'
print('O car == "kicks"? Eu prevejo que é False')
print(car == 'kicks')

car = 'fiesta'
print('O car == "fiesta"? Eu prevejo que é False')
print(car == 'fiesta')

car = 'uno'
print('O car == "uno"? Eu prevejo que é False')
print(car == 'uno')

car = 'compas'
print('O car == "compas"? Eu prevejo que é False')
print(car == 'compas')

"""
5.2 – Mais testes condicionais: 

Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescenteos
em conditional_tests.py. Tenha pelo menos um resultado True e um False para
cada um dos casos a seguir:
• testes de igualdade e de não igualdade com strings;
• testes usando a função lower();
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
maior ou igual a e menor ou igual a;
• testes usando as palavras reservadas and e or;
• testes para verificar se um item está em uma lista;
• testes para verificar se um item não está em uma lista.
"""

string = 'Teste'
if string == 'teste':
    print('As strings são iguais')
else:
    print('As strings são diferentes')

string = 'Olá Mundo'
if string.lower() == 'olá mundo':
    print('As strings são iguais')
else:
    print('As strings são diferentes')

age = 18
if age >= 18:
    print('Você é maior de idade')
elif age >= 12:
    print('Você é um adolescente')
elif age >= 5:
    print('Você é uma criança')
elif age >= 0 and age <= 5:
    print('Você é um bebê')

points = 500
if points > 450 or points < 650:
    print('Você venceu o jogo!')

cars = ['Gol', 'Golf']
if 'Uno' in cars:
    print('O carro está na lista')
else:
    print('O carro não está na lista')

if 'Palio' not in cars:
    print('O carro não está na lista')

"""
5.3 – Cores de alienígenas #1: 

Suponha que um alienígena acabou de ser
atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
valor igual a 'green', 'yellow' ou 'red'.
• Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
mostre uma mensagem informando que o jogador acabou de ganhar cinco
pontos.
• Escreva uma versão desse programa em que o teste if passe e outro em que ele
falhe. (A versão que falha não terá nenhuma saída.)
"""

alien_color = 'green'
if alien_color == 'green':
    print('Você acabou de ganhar 5 pontos')

if alien_color != 'green': 
    print('Você não ganhou nada')

"""
5.4 – Cores de alienígenas #2: 

Escolha uma cor para um alienígena, como foi
feito no Exercício 5.3, e escreva uma cadeia if-else.
• Se a cor do alienígena for verde, mostre uma frase informando que o jogador
acabou de ganhar cinco pontos por atingir o alienígena.
• Se a cor do alienígena não for verde, mostre uma frase informando que o
jogador acabou de ganhar dez pontos.
• Escreva uma versão desse programa que execute o bloco if e outro que execute
o bloco else.
"""

if alien_color == 'green':
    print('Você acabou de ganhar 5 pontos')
else:
    print('Você acabou de ganhar 10 pontos')

# Há diversos outros exercícios, porém evitei fazê-los devido sua simplicidade