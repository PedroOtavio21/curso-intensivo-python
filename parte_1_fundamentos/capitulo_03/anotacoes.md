# Capítulo 3 - Introdução às Listas

Neste capítulo, o foco de estudo principal serão as listas em Python.

## O que são listas?

Uma lista é uma coleção de itens. Os itens podem ser apenas strings, ou números, ou até mesmo os dois juntos.

Uma boa prática é que o nome da variável esteja no plural. Ex.:

```py
games = ["Call Of Duty", "Counter Strike", "Dark Souls", "Hollow Night"]
print(games)
```

Executando o código acima, é exibido na mesma forma do exemplo, inclusive com os colchetes

### Como acessar uma lista?

Para acessar um determinado elemento de uma lista através de seu índice (posição), você deve inserir a posição em colchetes menos 1. Ex.:

```py
books = ["Entendendo Algoritmos", "Código Limpo", "Hábitos Atômicos", "Ultra-Aprendizado", "O Hobbit"]

# primeira posição
book[0]

# terceira posição
book[2]

# Última posição
book[-1] # forma simplificada, caso não saiba o tamanho da lista
book[4] # caso saiba
```

### Operações em listas

Em Python, as listas são dinâmicas, permitindo operações diversas ao decorrer da execução de um código qualquer.

#### Alteração em listas

Para alterar um determinado elemento, basta atribuir o valor ao índice indicado:

```py
books = ["Entendendo Algoritmos", "Código Limpo", "Hábitos Atômicos", "Ultra-Aprendizado", "O Hobbit"]

books[0] = "Lógica de Programação e Algoritmos com JavaScript"
books[-1] = ""
```

#### Adicionando elementos

Há duas formas de se adicionar elementos em Python:

1. Concatenando um novo elemento com a lista
2. Inserindo um novo elemento na lista pelo índice

```py
cars = ["HB20S", "Kicks", "Toro"]

cars.append("Fusion") # adiciona ao final
cars.insert(0, "Renegade") # adiciona ao início da lista (índice 0)
print(cars)
```

#### Removendo elementos

Segue abaixo algumas das formas de se remover elementos das listas:

1. Quando se conhece o índice, por meio do del
2. Quando se conhece o índice, por meio do pop
3. O último elemento da lista, por meio do pop
4. Quando o conhece seu valor, por meio do remove

```py
compras = ["Banana", "Café", "Leite", "Açucar", "Arroz", "Farinha", "Biscoito"]

del compras[0]
arroz = compras.pop(4)
biscoito = compras.pop()
compras.remove("Farinha")

print(compras)
```

## Ordenando listas

Geralmente, quando trabalhamos com listas, num primeiro momento nós adquirimos os elementos de forma desordenada, na medida em que os elementos são adicionados. 

Para facilitar sua busca, utilizamos de metodos ou algoritmos que ordenam os elementos presentes nas listas. 

### Operações em listas

Veja algumas destas operações abaixo:

1. Ordenando lista de forma crescente - sort()
2. Ordenando lista de forma decrescente - sort(reverse=True)
3. Ordenando lista, sem alterar sua ordem original - sorted()
4. Revertendo valores de lista - reverse()
5. Informando tamanho de lista - len(lista)