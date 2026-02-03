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