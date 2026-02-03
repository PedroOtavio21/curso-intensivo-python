"""
9.10 – Importando Restaurant: 

Usando sua classe Restaurant mais recente,
armazene-a em um módulo. Crie um arquivo separado que importe Restaurant.
Crie uma instância de Restaurant e chame um de seus métodos para mostrar que
a instrução import funciona de forma apropriada.
"""

from Restaurant import Restaurant

my_restaurant = Restaurant('Arretado', 'l')
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)