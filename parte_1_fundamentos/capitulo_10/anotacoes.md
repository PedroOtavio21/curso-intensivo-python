# Capítulo 10 - Arquivos e Exceções

Agora que todo o "básico" da linguagem foi visto, está na hora de deixar o código mais robusto, a partir do trabalho com arquivos e tratamento de erros.

## Lendo dados de arquivos

Ler dados em um determinado arquivo é essencial em diversas aplicações, principalmente em aplicações de análise de dados.

Por exemplo, podemos ler o conteúdo de um arquivo-texto e reescrever o arquivo em um formato que o navegador possa exibir.

### Lendo um arquivo por inteiro

Segue o arquivo em texto abaixo de exemplo:

```txt
<!-- pi_digits.txt -->
3.1415926535
8979323846
2643383279
```

Para abrir o arquivo e exibir o conteúdo em python, há o seguinte trecho de código abaixo:

```py
# Ficar atento onde o código será executado!!!
whit open('pi_digits.txt') as file_object:
    contents = file_objects.read()
    print(contents)
```

Sempre que trabalhar com arquivos, independente de como seja, precisará da função `open()`, seguido de seu argumento, o caminho do arquivo.

A palavra reservada `with` fecha o arquivo após o seu uso

Fique atento ao tratar o fechamento de arquivos. Nunca confie que um arquivo será fechado automaticamente após a execução de um código!

### Paths de arquivos

As vezes, trabalhar com arquivos pode gerar bastante dor de cabeça, pelo simples fato de seu arquivo desejado não estar no mesmo diretório em que o arquivo python é executado.

Pesquise por bibliotecas padrões ou extras que resolvem estes problemas!

### Lendo arquivos, linha a linha

Digamos que você queira alterar uma linha específica de um arquivo de texto. Para isso, será necessário ler o arquivo, linha a linha, até encontrar o conteúdo que deseja alterar

Segue abaixo um exemplo de leitura linha a linha de um arquivo:

```py
file_name = 'teste.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line)

```

### Criando uma lista de linhas de um arquivo

Para armazenar o conteúdo de cada linha presente em um arquivo, basta seguir a seguinte sintaxe:

```py
file_name = 'teste.txt'

with open(file_name) as file_object:
    lines = file_name.readlines()

for line in lines:
    print(line.strip())
```

O método readline, basicamente armazena cada linha do arquivo em uma lista.

Agora, segue outro exemplo de uso de trabalho com arquivos:

```py
file_name = 'teste.txt'

with open(file_name) as file_object:
    lines = file_name.readlines()

file_string = ''
for line in lines:
    file_string += line.strip()

print(file_string)
print(len(file_string))
```

## Escrevendo dados em arquivos

Para escrever um conteúdo dentro de um arquivo de texto, a operação é bem similar a leitura de um arquivo:

```py
file_path = 'programming.txt'

with open(file_path, 'w') as file_object:
    file_object.write('I love programming.')
```

Como pode perceber, foi passado um segundo argumento no método open, 'w'.

Anteriomente não foi passado, pois por padrão, o método open sempre irá ler um arquivo, caso não passe um dos modos abaixo:

1. 'r': Realiza a leitura de um arquivo
2. 'w': Realiza a escrita de um arquivo
3. 'a': Realiza a concatenação de um conteúdo em um arquivo
4. 'r+': Realiza a leitura e escrita dentro de um arquivo

A função open SEMPRE cria um arquivo automaticamente, caso ele não exista. Em caso de abrir em modo de escrita, o python apagará qualquer conteúdo existente em um arquivo, caso exista.

### Inserindo vários dados

Para a inserção de dados, é necessário sempre colocar um '\n' ao fim de cada linha, caso queira a quebra de linha.

```py
file_path = 'programming.txt'

with open(file_path, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')
```

### Concatenando dados

A solução para inserir dados, não apagando um conteúdo já existente, é utilizar o `open()` no modo de concatenação (`a`).

Nota: Também irá criar um novo arquivo, caso não exista.

```py
file_path = 'programming.txt'

with open(file_path, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')
```

## Exceções

Sempre que ocorrer um erro, onde Python não tem certeza do que deverá ser feito em seguida, um objeto deste erro será criado. Ao criar um código que trate este erro, o código continuará funcionando normalmente.

Tratar estes "tracebacks" é um trabalho de grande importancia para o programador. Os seus tratamentos ocorrem por meio dos blocos try-except (try-catch em outras linguagens).

### Usando blocos try-except

Na prática, tratar um erro com o try-except ocorre da seguinte forma:

```py
print("Give me two numbers, and I´ll divie them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number) # Não será possível, caso divida por 0!
    except ZeroDivisionError: # Objeto de erro identificado
        print("You can´t divide by 0!")
    else:
        print(answer)
```

Em um uso de bloco try-except:
1. Se o bloco de código dentro do "`try`" não apresentar um erro, o código funciona normalmente
2. Se no bloco "`try`" ocorrer o erro experado, o código "pausa", caindo no `except`, mostrando uma mensagem personalizada, ou alguma funcionalidade expecífica.
3. O bloco `else` ao final do código, é uma saída "padrão", caso não ocorra um erro

### Tratando arquivos não encontrados

Provavelmente, ao abrir e trabalhar com arquivos no python, você deve ter encontrado o seguinte erro: `FileNotFoundError`. 

Isso ocorre geralmente porquê você especificou errado o caminho, ou o caminho utilizado não existe.

Segue um exemplo de tratamento deste erro:

```py
def count_words(filename):
    """COnta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = f'Sorry, the file {filename} does not exist.'
        print(msg)
    else:
        # Conta o número aproximado de palavras no arquivo
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has about {str(num_words)} words.')

filenames = ['alice.txt', 'siddhartha.txt', 'mob_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

```

## Armazenando dados

Armazenar dados após o uso de determinados programas, é muito comum no meio do desenvolvimento. Uma forma de fazer com que dados persistam mesmo após a execução, é por meio de arquivos ou módulos json. 

O Json (JavaScript Object Notation) permite implementar estruturas de dados Python em um arquivo, podendo carregar os dados deste arquivo sempre que executar na próxima vez. Este formato é uma convenção global de uso.

### Usando json.dump() e json.load()

Abaixo, há um exemplo que armazena um conjunto de números e outro que leia esses números. 

O primeio, utiliza o `json.dump()`, método que aceita dois argumentos:
1. Um dado para armazenar (conjunto de números)
2. Objeto arquivo onde armazenará os dados (file_object)

```py
import json

numbers = [2,3,5,7,11,13]
file_name = 'numbers.json'

try:
    with open(file_name, 'w') as file_object:
        json.dump(numbers, file_object) # Armazena os dados no Json
except FileNotFoundError:
    pass
```

Já o `json.load()`, utiliza como argumento apenas o objeto arquivo, que deve ser utilizado para a leitura de seus dados, além de retornar os dados lidos.

```py
import json

file_name = 'numbers.json'

try:
    with open(file_name) as file_object:
        numbers = json.load(file_object)
except FileNotFoundError:
    pass
else:
    print('Conjunto de números: ')
    for number in numbers:
        print(f"{number}")
```

Segue abaixo um exemplo mais completo das duas funcionalidades:

```py
import json

def get_stored_username(file_path):
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    file_name = file_path
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(file_path):
    """Pede um novo nome de usuário."""
    username = input('What´s your name?').strip()
    file_name = file_path
    with open(file_name, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user(file_path):
    """Saúda o usuário pelo nome."""
    username = get_new_username(file_path)
    if username:
        print(f'Welcome back, {username}!')
    else:
        username = get_new_username(file_path)
        print(f'We´ll remember you when you come back, {username}!')

greet_user('username.json')
```