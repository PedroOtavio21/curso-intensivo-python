"""
9.6 – Sorveteria: 

Uma sorveteria é um tipo específico de restaurante. Escreva uma
classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer versão da
classe funcionará; basta escolher aquela de que você mais gosta. Adicione um
atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva
um método para mostrar esses sabores. Crie uma instância de IceCreamStand e
chame esse método.
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'Nome do Restaurante: {self.restaurant_name}.\nTipo de cosinha: {self.cuisine_type}\nNúmero de clientes atendidos: {str(self.number_served)}')
    
    def open_restaurant():
        print('O Restaurante está oficialmente aberto!')

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
    
    def increment_number_served(self, number_served):
        self.number_served += number_served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors[:]
    
    def show_flavors(self):
        print('Principais sabores:')
        for flavor in self.flavors:
            print(f'-{flavor}')
    
my_icecream_stand = IceCreamStand('Bambu', 'Camburão', ['chocolate', 'baunilha', 'flocos'])
my_icecream_stand.show_flavors() 