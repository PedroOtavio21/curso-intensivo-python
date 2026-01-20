# Capítulo 7 - Entrada de usuários e Laços while

Neste capítulo, será visto como receber e tratar dados recebidos do usuário, além de como utilizar laços while.

## Função input()

O método input faz uma pausa momentânea na execução de seu código, até que o usuário forneça um texto qualquer. Depois que o dado é recebido, pode ser armazenado em uma variável qualquer para trabalhar como queira.

```py
message = input('Insira uma mensagem de texto qualquer')
print(message)
```

Tenha cuidado ao trabalhar com o método `input()`, pois ele obterá tudo o que você executar, além de terminar sua execução após finalizar com enter. A saída sempre será uma `string`.

A ideia, é escrever uma mensagem clara para o usuário digitar exatamente o que você queira.

## Laço while

Diferente do laço for, o laço while ocorre enquanto uma determinada condição for verdadeira. Ou seja, seu tempo de execução em um software pode ser curto ou demorado.

Geralmente, fazemos este tipo de laço quando não sabemos exatamente quando irá acabar sua execução.

```py
# laço while
current_number = 1
while current_number <= 5:
    print(current_number)
    # current_number = current_number + 1
    current_number += 1

# laço for
for index in range(1, 6):
    print(index)
```

Um exemplo comum, é fazer uma determinada operação, até que o usuário escolha sair do programa, interrompendo a operação.

```py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### Usando flag´s

Geralmente, em códigos onde onde deverão ser executados, até uma ou mais de uma condição ser atingida, são necessários o uso de flags

Uma flag nada mais é que um sinal para o programa, onde determinará se o código deve continuar ativo ou não.

```py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
active = True # nossa flag
while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active = False # fim de execução
```

### Usando break e continue

O uso de break seria um pouco similar ao uso de uma flag como no exemplo acima.

Na prática, ao utilizar a palavra reservada `break`, o laço em execução irá finalizar imediatamente (sendo laço `while` ou `for`)

```py
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break # laço é interrompido imediatamente
    else:
        print("I'd love to go to " + city.title() + "!")
```

Já no caso da palavra continue, ela pula um passo a ser realizado em um laço, não saindo do laço em execução.

```py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number) # irá exibir apenas os ímpares
```

## Modificando listas com while

Diferente do for, while é o ideal para trabalhar com modificação de listas em tempo de execução

```py
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    # confirmed_users.append(unconfirmed_users.pop())
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(curren_user)

print('\nThe following users have been confirmed:')
for user in confirmed_users:
    print(user.title())
```

Outro caso de uso interessante, seria remover valores repetidos dentro de uma determinada lista:

```py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```