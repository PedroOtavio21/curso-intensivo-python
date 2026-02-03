"""
9.1 – Restaurante: 

Crie uma classe chamada Restaurant. O método __init__()
de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type.
Crie um método chamado describe_restaurant() que mostre essas duas
informações, e um método de nome open_restaurant() que exiba uma
mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois
atributos individualmente e, em seguida, chame os dois métodos.
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Nome do Restaurante: {self.restaurant_name}.\nTipo de cosinha: {self.cuisine_type}')
    
    def open_restaurant():
        print('O Restaurante está oficialmente aberto!')

my_restaurant = Restaurant('gusteau chef´s', 'ilha')
print(my_restaurant.name.title())
print(my_restaurant.cuisine_type.title())
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

"""
9.2 – Três restaurantes: 

Comece com a classe do Exercício 9.1. Crie três
instâncias diferentes da classe e chame describe_restaurant() para cada
instância.
"""

pe_de_fava = Restaurant('pé de fava', 'l')
pe_de_fava.describe_restaurant()

heroes_burguer = Restaurant('heroes burguer', 'americana')
heroes_burguer.describe_restaurant()

arretado = Restaurant('arretado', 'self service')
arretado.describe_restaurant()