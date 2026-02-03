"""
9.4 – Pessoas atendidas: 

Comece com seu programa do Exercício 9.1 (página
225). Acrescente um atributo chamado number_served cujo valor default é 0. Crie
uma instância chamada restaurant a partir dessa classe. Apresente o número de
clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o
novamente.
Adicione um método chamado set_number_served() que permita definir o
número de clientes atendidos. Chame esse método com um novo número e mostre o
valor novamente.
Acrescente um método chamado increment_number_served() que permita
incrementar o número de clientes servidos. Chame esse método com qualquer
número que você quiser e que represente quantos clientes foram atendidos, por
exemplo, em um dia de funcionamento.
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

restaurant = Restaurant('mammo', 'l')
restaurant.describe_restaurant()
restaurant.set_number_served(45000)
restaurant.describe_restaurant()
restaurant.increment_number_served(150)
restaurant.describe_restaurant()