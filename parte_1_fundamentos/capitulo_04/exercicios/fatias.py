"""
4.10 – Fatias: 

Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia
para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três
itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir
os três últimos itens da lista.
"""

numbers = [value for value in range(1, 21)]

print('Os três primeiros itens da lista são:')
for value in numbers[:3]:
    print(value)

print('Os três itens do meio da lista são:')
for value in numbers[9:12]:
    print(value)

print('Os três últimos itens da lista são:')
for value in numbers[-3:]:
    print(value)

"""
4.11 – Minhas pizzas, suas pizzas: 

Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a
mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço
for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja
armazenada na lista apropriada.
"""

pizzas = ["Calabresa", "Mussarela", "Carne de Sol"]
friend_pizzas = pizzas[:]

pizzas.append("4 Queijos")
friend_pizzas.append("Portuguesa")

print('Minhas pizzas favoritas são:')
for pizza in pizzas:
    print(pizza)

print('As pizzas favoritas de meu amigo são:')
for pizza in friend_pizzas:
    print(pizza)

"""
4.12 – Mais laços: 

Todas as versões de foods.py nesta seção evitaram usar laços
for para fazer exibições a fim de economizar espaço. Escolha uma versão de
foods.py e escreva dois laços for para exibir cada lista de comidas.
"""

# Resolvi criar uma lista de comidas e apresentar os elementos de forma diferente.

foods = ['Pizza', 'Sandwich', 'Ice Cream', 'MilkShake', 'Sushi']
for food in foods[2:]:
    print(food)

for food in foods[-2:]:
    print(food)

for food in foods:
    print(food)

"""
4.13 – Buffet: 

Um restaurante do tipo buffet oferece apenas cinco tipos básicos de
comida. Pense em cinco pratos simples e armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida,
use um laço for para exibir cada um dos itens do cardápio revisado.
"""

menu = (
    'Peixe a Delícia', 
    'Fettuccini ao Molho com Camarão', 
    'Assado de Panela',
    'Filé à Parmegiana',
    'Petit Gateau'
)

print('Principais pratos do buffet:')
for food in menu:
    print(food)

# testando a edição de um único item
# menu[0] = 'Pão de Alho'

# Reescrevendo cardápio:
menu = (
    'Peixe a Delícia', 
    'Panelada', 
    'Assado de Panela',
    'Filé à Parmegiana',
    'Feijoada'
)

print('Cardápio atualizado do Buffet:')
for food in menu:
    print(food)