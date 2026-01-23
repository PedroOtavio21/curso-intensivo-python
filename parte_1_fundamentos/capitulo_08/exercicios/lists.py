"""
8.9 – Mágicos: 

Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da lista.
"""

magics = ['Normandus', 'Ariadus', 'Eliates']

def show_magicians(magicians):
    for magic in magicians:
        print('Oah! ' + magic + ' is a great magician!')

show_magicians(magics)

"""
8.10 – Grandes mágicos: 

Comece com uma cópia de seu programa do Exercício
8.9. Escreva uma função chamada make_great() que modifique a lista de
mágicos acrescentando a expressão o Grande ao nome de cada mágico. Chame
show_magicians() para ver se a lista foi realmente modificada.
"""

def make_great(magicians):
    
    
    for i, magic in enumerate(magicians):
        magicians[i] = f'o Grande {magic}'

make_great(magics)
show_magicians(magics)

"""
8.11 – Mágicos inalterados: 

Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em uma
lista separada. Chame show_magicians() com cada lista para mostrar que você
tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.
"""

def make_great(magicians):
    return [f'o Grande {magic}' for magic in magicians]

new_magics = make_great(magics[:])
show_magicians(magics)
show_magicians(new_magics)

"""
8.12 – Sanduíches: 

Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos
itens quantos forem fornecidos pela chamada da função e deve apresentar um
resumo do sanduíche pedido. Chame a função três vezes usando um número
diferente de argumentos a cada vez.
"""

def listar_ingredientes(*pedidos):
    print('\nResumo de pedido:')
    for pedido in pedidos:
        print(f' - {pedido.capitalize()}')

listar_ingredientes('pão', 'alface', 'cebola caramelizada', 'hamburguer', 'chedar')
listar_ingredientes('pão', 'alface', 'molho especial', 'frango', 'chedar')
listar_ingredientes('pão', 'bacon', '2x hamburguer', 'chedar', 'molho especial')

"""
8.13 – Perfil do usuário: 

Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome e
o sobrenome, além de três outros pares chave-valor que o descrevam.
"""

def build_profile(first, last, **user_infos):
    profile = dict()
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_infos.items():
        profile[key] = value
    return profile

my_perfil = build_profile('pedro', 'otávio', course='Computação', age=23)
for key, value in my_perfil.items():
    print(f'{key}: {value}')

"""
8.14 – Carros: Escreva uma função que armazene informações sobre um carro em
um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
Chame a função com as informações necessárias e dois outros pares nome-valor,
por exemplo, uma cor ou um opcional. Sua função deve ser apropriada para uma
chamada como esta:
car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
Mostre o dicionário devolvido para garantir que todas as informações foram
armazenadas corretamente.
"""

def build_car(fabricante, modelo, **infos):
    new_car = dict()
    new_car['fabricante'] = fabricante
    new_car['modelo'] = modelo
    for key, value in infos.items():
        new_car[key] = value
    return new_car

my_car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)