# Capitulo 6 - Dicionários

Neste capítulo, serão apresentados os dicionários em Python, similar aos objetos em linguagens de programação. Servirão para representar objetos no mundo real, trabalhando em conjunto com diversas estruturas.

## Sintaxe

Imagine que queira armazenar as ingormações de uma pessoa:

```py
person = {
    'name': 'Pedro',
    'color_eyes': 'Castanho',
    'old': 23,
    'friends': ['Bia', 'Luis', 'João']
}

print(person['name'])
```

Como pode ver, um dicionarío é uma coleção de pares chave-valor, onde cada chave armazena armazena um valor associado a ela. Este valor pode ser qualquer tipo, dentre strings, numeros, listas e até outros dicionários.

### Acessando e adicionando chaves

Para acessar um valor, coloque o nome do dicionário, seguido do valor da chave onde o valor escolhido estará armazenado da seguinte forma:

```py
print(pessoa['color_eyes']) # retorna 'Castanho'
```

Agora, caso queira criar uma nova chave com valores associados, basta dar o nome da chave e atribuir um valor qualquer:

```py
person['address'] = {
    'street': 'Rua do Saber',
    'number': '123'
}
```

Para adicionar um novo valor a uma determinada chave, basta reatribuir um valor para aquela mesma chave.

### Removendo chaves

Para remover uma determinada chave de um dicionário, basta utilizar da palavra reservada 'del', seguida da chave que queira excluir

```py
alien = {'color': 'green', 'points': 5}
del alien['points']
print(alien)
```

## Percorrendo dicionários

Em python, também é possível percorrer os dicionários por meio de laços for

```py
user = {
    'user_name': 'PedroOta_21',
    'first_name': 'Pedro',
    'last_name': 'Otávio'
}

for key, value in user.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
```

Note que os primeiros valores do for podem receber qualquer nome, porém é obrigatório utilizar o método `items()` do dicionário, para percorrer todos os elementos existentes

Para percorrer apenas as chaves de um dicionário, há duas formas:

```py
# Utilizando o método keys(), sendo mais recomendado
for key in user.keys():
    print(key)

# Utilizando a saída padrão:
for key in user:
    print(key)
```

O método `key()` também pode ser usado para verificar se uma determinada chave existe em um dicionário

```py
if 'Jacaré' not in animals_friends.key():
    print('Jacaré, vá embora!')
```

Outro método utilizado para percorrer a lista, seria o values(), utilizado para percorrer os valores de chave-valor.

```py
for languages in favorite_languages.values():
    print(language.title())
```

Outra forma de percorrer uma lista, porém apresentando valores não duplicados, seria com o método set():

```py
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

### Percorrendo um dicionário ordenado

Para fazer com que um determinado laço esteja ordenado e percorrê-lo, basta fazer o seguinte:

```py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')
```

O Método sorted() utilizado, retorna uma lista ordenada, a partir de um objeto iterável (lista, tupla, string, etc).