# Capítulo 9 - Classes

Neste capítulo, será dada uma introdução sobre a POO em Python, algo bastante utilizado hoje em programação.

## Criando e utilizando classes

Uma classe é nada mais que a representação de um objeto ou ser do mundo real. Esta representação pode ter suas próprias características (atributos) e comportamentos (métodos).

Segue abaixo um exemplo de classe que representa qualquer cachorro do mundo real, onde possui nome, idade, além de sentar e rolar. 

```py
class Dog():
    """Uma tentativa simples de modelar um cachorro"""
    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(f'{self.name.title()} rolled over!')
```

### Método __init__()

O método `__init__()` nada mais é que o método construtor. Ele sempre será executado automaticamente sempre que um objeto é instanciado.

No exemplo anterior, o parâmetro `self` é obrigatório na definição deste método, estando antes dos parâmetros escolhidos por você. O self é similar ao `this` de outras linguagens de programação.

Segue agora abaixo o uso da instância da classe, o objeto Dog:

```py
my_dog = Dog('willie', 6) 
print(f'my dog´s name is {my_dog.name.title()}.')
print(f'my dog is {str(my_dog.age)} years old.')

my_dog.sit()
my_dog.roll_over()
```

Note que, você não especificou o retorno do método `__init__()`, porém Python retorna automaticamente

### Acessando atributos e métodos do objeto

Como pode ver acima, foi acessado o nome e a idade do cachorro no print, após a criação do próprio.

Para acessar quaisquer informações do objeto, basta utilizar um `.` após a variável onde foi feita a instância da classe.

## Trabalhando com atributos e métodos

Umas das principais atividades de um desenvolvedor em poo é a modificação de atributos de instâncias de classes.

Podemos alterar atributos manualmente, ou desenvolver métodos de classes que modificam os atributos da classe por si só.

```py
class car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = f'{str(self.year)} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print(f'This car has {str(self.odometer_reading)} miles on it.')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_get_descriptive_name())
my_new_car.read_odometer()
```

### Modificando valores de atributos

Geralmente, valores de atributos são passados no momento em que as classes são instanciadas, ou quando queremos altera-los por métodos ou incrementando o próprio.

Segue um exemplo, continuando a modificar a classe carro:

```py
class Car():
    # continuação
    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor especificado
Rejeita a alteração se for tentativa de definir um valor menor
para o hodômetro"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can´t roll back an odometer!')
    
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do
        hodômetro."""
        self.odometer_reading += miles

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

## Herança

Agora, será apresentado um dos principais pilares na orientação a objetos na programação: a herança

A herança nada mais é, que uma forma de se criar classes-filhas a partir de uma classe-pai. Estas "sub-classes" possuem os mesmos atributos e métodos da classe pai, porém com a possibilidade de possuirém elementos próprios.

Segue abaixo um exemplo de herança comum:

```py
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles onit.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class EletricCar(Car):
    """Representa aspectos específicos de veículos elétricos"""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai."""
        super().__init__(make, model, year)

my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

Para fazer a herança acontecer, é necessário 2 coisas:
1. A classe filha estar no mesmo arquivo da classe pai
2. A classe pai deve ser passada nos parênteses da classe filha da definição da classe

A função super é especial do python, onde executa algum método existente da classe pai a sua escolha a partir da classe filha.

### Adicionando elementos na classe filha

Do que adianta criar uma classe filha se não diferença da classe pai? Vamos deixa agora a EletricCar um pouco diferente:

```py
class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        print(f"This car has a {str(self.batery_size)}-kWh battery")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

### Sobrescrevendo métodos

Outro diferencial presente nas classes filhas é a possibilidade de sobrescrever métodos existentes em classes pai

Geralmente, isso é feito quando há necessidade de incrementar uma funcionalidade do método, ou então refazê-lo por completo

Para fazer isto, basta gerar um método de nome idêntico na classe filha

```py
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self):
        print(f'{self.name} está gerando um som!')

class Dog(Animal):
    def __init__(self, name, age):
        super.__init__(name, age)

    def sound(self):
        print(f'{self.name} está latindo!')
```

### Instâncias como atributos

Com o avanço dos estudos, o uso de classes em projetos mais extensos acaba ganhando muita flexibilidade.

Um exemplo disto é passar instâncias de classes como atributos em outras classes:

```py
class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    def __init__(self, battery_size=70)
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f"This car has a {str(self.battery_size)}-kWhbattery.")

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif slef.battery_size == 85:
            range = 270
        message = f'This car can go approximately {str(range)}'
        message += ' miles on a full charge.'
        print(message)

class EletricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

## Importando classes

Ser um bom desenvolvedor, significa utilizar de boas práticas de código limpo, como código legível e código simplificado. 

Ou seja, quanto menos código desnecessário atrelado a um único arquivo, melhor.

Uma boa prática em poo, seria separar classes em módulos únicos e importá-las quando necessário.

```py
# Car.py
class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo formatado de modo elegante."""
        long_name = f'{str(self.year)} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhadem do carro."""
        print(f'This car has {str(self.odometer_reading)} miles on it.')

    def update_odometer(self, mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado.
        
        Rejeita alteração se for tenttiva de definir um valor menor para o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can´t roll back an odometer!')
        
    def incremente_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer += miles

class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    def __init__(self, battery_size=60):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f"This car has a {str(self.battery_size)}-kWh")

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro pode percorrer com a bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f"This car can go approximately {str(range)}"
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
"""Modela aspectos de um carro específicos de veículos elétricos."""
    def __init__(self, make, model, year):
    """Inicializa os atributos da classe-pai.
    Em seguida, inicializa os atributos específicos de um carro
    elétrico."""
        super().__init__(make, model, year)
        self.battery = Battery()
```py

```py
from Car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

### Importando várias classes

Existe também a possibilidade de importar quantas classes forem necessárias de um mesmo módulo.

```py
from car import Car, EletricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = EletricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

### Importando tudo de um módulo

Há também a opção de importar todos os elementos de um mesmo módulo:

```py
from nome_modulo import *
```

Porém, não é muito recomendado utilizar desta forma por n motivos, sendo melhor importar somente o que você irá trabalhar.

## Bibliotecas-padrão do Python

Python, assim como outras linguagens de programação em sua maioria, possui bibliotecas padrão para diversos tipos de uso.

```py
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

from key, value in favorite_languages.items():
    print(f"{name.title()} ´s favorite language is {language.title()}.")
```

