# Capítulo 8 - Funções

Neste capítulo, serão apresentadas as funções. Trechos de códigos reutilizáveis para qualquer tipo de situação.

## Sintaxe

Segue abaixo um exemplo de uso de uma função

```py
# definição de função com trecho de código
def greet_user():
    print('Hello!')

# chamada da função
greet_user()
```

### Entradas

Funções na programação, permitem que sejam identificados os seus "argumentos" na entrada.

Nas funções, podem ser chamados um ou vários argumentos

```py
def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('pedro')
```

Fique atento quando realizar a chamada de funções. Os atributos passados nos parâmetros da funções devem estar na mesma ordem, ou poderá gerar erros em caso de não tratamento do código, etc.

Uma solução do python para casos de troca de argumentos, é o uso de argumentos nomeados. Na prática, você não precisará se preocupar com a ordem dos argumentos.

```py
def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '´s name is ' + pet_name.title() + '.')

describe_pet(animal_type='hamster', pet_name='harry')
```

Fique atento ao nome dos parâmetros das funções, quando utilizar os argumentos nomeados, para não gerar erro.

### Valores default

Quando escrevemos uma função, podemos fazer com que os parâmetros tenham valores padrão, em caso dos argumentos não serem passados em sua chamada.

```Py
def describe_pet(pet_name, animal_type='dog'):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie') # seu tipo será 'dog'
```

Deixe o valor padrão sempre por último, após a utilização dos valores de atributos não padrão.

### Retorno

Além de especificar a entrada de funções, podemos também especificar o seu retorno

```py
def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

Seus retornos podem ser de diversos tipos, como strings, dicionários, números, etc.

Seguem abaixo outros exemplos de uso de funções:

```py
def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first', first_name, 'last': last_name}
    if age:
        person['age'] = age
    
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

## Listas em funções

Para lidar com listas em funções, nada de muito diferente do esperado. Passe como parâmetro e desenvolva o restante.

```py
def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

É possível lidar com modificações de funções como visto anteriormente, percorrer laços e afins.

Uma boa prática para manter o formato original da lista, seria passar a cópia da lista nos argumentos.

### Passando vários argumentos

Algumas abrem margem para receber uma quantidade indeterminada de argumentos do usuário, sendo nenhum ou muitos argumentos passados.

Em python, isto é feito através do uso de tuplas nos parâmetros da função, com a sintaxe `*nome_tupla`

```py
def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

Essa sintaxe permite combinar vários parâmetros, parâmetros simples geralmente postos antes, e parâmetros com valores default ao final da passagem de argumentos.

Também, é possível passar um dicionário com um números indefinido de chaves-valor, com a sintaxe similar, sendo `**nome_dict`

```py
def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo o que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(
    'albert', 
    'einstein', 
    location='princeton', 
    field='physics'
)
```

## Importação de módulos

Uma boa prática em criar funções auxiliares ao longo de seu projeto, é separa-las em um arquivo específico denominado `module`.

```py
# pizza.py
def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print(f'Making a {str(size)}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')
```

```py
# making_pizzas.py
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
```

Como pode ver, primeiro é criado uma função em um módulo específico, e depois importado com a palavra reservada `import`. 

Para utilizar um método específico, use a sintaxe: `nome_do_módulo.nome_da_função()`

### Funções específicas

Agora, para importar funções específicas, a sintaxe muda um pouco:
`from nome_do_módulo import nome_da_função`

Na mesma linha da sintaxe acima, pode ser feita a importação de quantos métodos quiser, separados por vírgula.

### Uso de alias

O `alias` é uma forma de facilitar o uso ou escrita de um determinado módulo ou função, muito utilizado em projetos mais extensos. 

Basta utilizar a palavra reservada `as` e dar um outro nome ao módulo/função. Ex.: `ìmport nome_do_módulo as nm`

### Importando tudo

Para específicar que você queira importar tudo existente dentre de um módilo, faça:

```py
from module import *
```