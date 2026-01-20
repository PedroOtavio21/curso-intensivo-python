"""
7.4 – Ingredientes para uma pizza: 

Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
"""
prompt_1 = 'Insira quais ingredientes sua pizza deverá ter (1 por vez)'
prompt_1 += '\nPara encerrar a execução, escreva "quit": '

message = ''
while message != 'quit':
    message = input(prompt_1)
    if message != 'quit':
        print('Ingrediente ' + message + ' adicionado à pizza!')
    else:
        print('Finalizando execução.')
        break

"""
7.5 – Ingressos para o cinema: 

Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.
Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
o preço do ingresso do cinema.
"""

prompt_2 = 'Insira a sua idade para lhe informar qual o valor do ingresso.'
prompt_2 += '\nPara sair do programa, escreva "quit": '

question = ''
age = 0
while question != 'não':
    question = input('Você deseja inserir a sua idade? ("sim"/"não")\n')
    if question == 'não':
        break
    else:
        age = int(input(prompt_2))
        if age < 3 and age > 0:
            print('Você possui um ingresso gratuito!')
        elif age < 13:
            print('Seu ingresso custará 10 dólares.')
        elif age >= 13:
            print('Seu ingresso custará 15 dólares.')

"""
7.8 – Lanchonete: 

Crie uma lista chamada sandwich_orders e a preencha com os
nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche
de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
mensagem que liste cada sanduíche preparado.
"""

sandwich_orders = ['big mac', 'quarteirão', 'mcmelt', 'mccrispy']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('Seu sanduíche ' + sandwich + ' está pronto!')
    finished_sandwiches.append(sandwich)

print('Segue a lista de pedidos finalizados:')
print(finished_sandwiches)

"""
7.9 – Sem pastrami: 

Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um laço
while para remover todas as ocorrências de 'pastrami' e sandwich_orders.
Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.
"""

sandwich_orders = ['big mac', 'pastrami', 'quarteirão', 'mcmelt', 'pastrami', 'mccrispy', 'pastrami']
finished_sandwiches = []

print(sandwich_orders)
print('Removendo sanduíche de pastrami nos pedidos.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('Seu sanduíche ' + sandwich + ' está pronto!')
    finished_sandwiches.append(sandwich)

print('Segue a lista de pedidos finalizados:')
print(finished_sandwiches)

"""
7.10 – Férias dos sonhos: 

Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete.
"""

results = {}

active = True
confirm = ''
while active:
    name = input('Qual é o seu nome?')
    place = input('pudesse visitar um lugar do mundo, para onde você iria?')
    results[name] = place

    confirm = input('Deseja continuar a enquete? ("sim"/"não")').lower()
    if confirm == 'não' or confirm == 'nao':
        active = False

print('\nResultados da enquete:')
for name, place in results.items():
    print(name.title() + ' gostaria de visitar ' + place.title())