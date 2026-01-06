# Lista original
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Alterando primeiro elemento
motorcycles[0] = 'ducati'
print(motorcycles)

# Adicionando novo elemento ao fim da lista
motorcycles.append('honda')

# Adicionando novo elemento no início da lista
# Demais elementos deslocados para a direita
motorcycles.insert(0, 'bmw')

# Removendo primeiro elemento da lista com del
del motorcycles[0]

# Removendo último elemento da lista com pop
moto_removida = motorcycles.pop()

# Removendo primeiro elemento da lista com pop
primeira_moto = motorcycles.pop(0)

# Removendo um elemento a partir de seu valor com remove
cars = ['celta', 'palio', 'corsa', 'classic']
cars.remove('corsa') # primeira ocorrência de 'corsa' removida