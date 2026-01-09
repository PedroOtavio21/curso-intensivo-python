# Capitulo 4 - Trabalhando com Listas

Neste capítulo, será apresentado como criar e trabalhar com elementos individuais em uma lista. Na prática, serão vistos como os laços funcionam.

## Percorrendo listas

Geralmente, haverão casos onde será necessário percorrer todos os elementos de uma determinada lista, executando uma determinada operação para cada item, ou até mesmo um print no console, seja a lista curta ou extensa. É aí que entram os chamados laços de repetição.

Quando sabemos o tamanho da lista e quando ela irá parar, utilizamos o laço 'for'.

```py
magicians= ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can´t wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
```

A linha acima extrai as variáveis de `magicians` e armazena na variável `magician`, e exibe cada um no console. Entenda como *'para todo mágico na lista de mágicos, exiba o nome do mágico, seguido do seu truque realizado.'*

**Nota:** escolha um nome conveniente para a variável temporária no loop.

```txt
for cat in cats:
for dog in dogs:
for item in list_of_items:
```

## Trabalhando com números

Além de iterar listas, os loops podem auxiliar na iteração de valores numéricos

### Usando range()

A função range() auxilia na geração de uma série de números, como uma espécie de "lista temporária".

Caso queira ler uma sequência de números, faça o seguinte:

```py
for value in range(1, 6):
    print(value) # faz uma contagem de 1 a 5
```

A função range() também pode ser usada para criar uma lista de números

```py
# A função list converte os valores da variável em uma lista!
numbers = list(range(1, 6))
print(list)

even_numbers = list(range(2, 11, 2)) # inicia com 2, vai até 11, soma 2
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
```

### Funções auxiliares aos números

Segue algumas funções que auxiliam em lista de números:

1. min(list) -> retorna o valor mínimo
2. max(list) -> retorna o valor máximo
3. sum(list) -> retorna a soma de uma lista

### List comprehensions

Forma simplificada de atribuir valores a uma lista.

Na prática, é uma combinação de um laço for e a criação de elementos em uma linha, concatenando cada novo elemento de forma automática.


Como é a sintaxe:
- Atribua o resultado a uma lista (escolha um nome intuitivo)
- Entre colchetes:
  1. Defina o valor que será armazenado (apenas um valor ou uma operação)
  2. Escreva o laço for que irá gerar os valores na mesma linha

```py
# Realiza o mesmo exemplo de lista de quadrados, mostrado anteriormente
squares = [value ** 2 for value in range(1, 11)]
print(squares)
```

## Trabalhando com partes de listas

Em Python, há a possibilidade em trabalhar apenas com uma parte específica (fatia) de uma lista

### Fatiando uma lista

Para criar uma fatia da lista, basta especificar o índice do primeiro e último elemento que precisa. A ideia é bastante similar a função range(), parando antes do segundo argumento especificado.

```py
players = ["Ronaldinho", "Fenômeno", "Beckham", "Roberto Carlos", "Messi"]
print(players[0:3]) # exibe os três primeiros jogadores
print(players[:4]) # exibe do primeiro ao último elemento
print(players[2:]) # exibe do segundo ao último elemento
print(players[-3:]) # exibe os 3 últimos elementos
```

Para percorrer os valores a partir de um laço, basta passar a fatia no laço for:

```py
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player)
```

### Copiando listas

Para copiar uma lista, basta utilizar uma fatia da lista que queira copiar e armazenar em uma nova lista, passando nada nos 2 argumentos iniciais da fatia "[:]"

```py
my_foods = ['Pizza', 'Hamburguer', 'Ice Cream', 'Sushi']
friends_food = my_foods[:]
```

Nota: Armazenar os valores de uma lista a outra, sem utilizar os colchetes, fará apenas com que uma lista aponte para outra!

## Tuplas

As listas são bastante úteis quando é necessário armazenas diversos itens de tipos diversos. Porém, as vezes acaba sendo necessário criar uma lista que não poderá mudar. Estas, são as listas imutáveis (tuplas)

### Sintaxe

Diferente de listas comuns, para criar uma tupla, deverá usar dos parênteses. A forma de acesso acaba sendo similar a uma lista comum.

```py
dimensions = (200, 50)
print('Dimensões do retângulo:')
for dimension in dimensions:
    print(dimension)

dimensions[0] = 255 # Irá gerar um erro!
```

A única forma de alterar os valores de uma tupla, seria reescrevendo os valores da tupla original.

```py
# Tupla original
dimensions = (200, 50)
print(dimensions)

# Tupla modificada
dimensions = (400, 100)
print(dimensions)
```