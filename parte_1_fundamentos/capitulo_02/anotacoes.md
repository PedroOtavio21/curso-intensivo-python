# Capítulo 2 - Variáveis e tipos de dados simples

Neste capítulo, será apresentado os diferentes tipos de dados utilizados no dia a dia como um desenvolvedor python.

Além disso, será apresentado como se armazenam estes valores em variáveis em diversos programas

## O python em ação

Um programa python é indicado pela extensão _.py_. Logo, o editor de código passa o programa pelo _interpretador Python_, onde lê o programa e determina o que cada comando irá fazer

Fique atento ao seu editor de código. Sempre que possível ele indicará erros de sintaxe, variáveis e funções em cores distintas, dentre outras coisas que auxiliarão no dia-a-dia do programador

## Variáveis

Como citado anteriormente, uma variável é uma forma de armazenar um valor dentro de um programa. 

Você pode armazenar um nome de usuário, sua idade, o peso de um carro, uma senha criptografada para maior segurança, dentre outros demais tipos de uso de variáveis.

Ex.:

```python
hello = 'Hello World'
python = 'Python!'
print(hello, python)
```

### Nomenclatura de variáveis

*Tenha o cuidado e zelo ao criar nomes em variáveis*. Evite criar nomes pouco descritivos como "a" ou "x". Utilize algo como "nome_aluno", "media_ponderada", "university_code", etc.

Sobre as regras de nomenclatura, estão as seguintes:

1. Nomes pondem conter letras, números e underscores.
2. Variáveis são case sensitives, ou seja: "Aluno" é diferente de "aluno"
3. Espaços não são permitidos. Utilize os underscores nos espaços: 'nome_aluno', 'media_notas', etc
4. Existem palavras já utilizadas em python que não podem ser utilizadas como variáveis. Tenha cuidado!

## Strings

O primeiro tipo de dado a ser visto, são as **strings**.

As strings dada mais são do que um conjunto de caracteres, ou seja, dados em texto! 

Tudo o que estiver em aspas são strings no python. Podem ser aspas simples ou aspas duplas

ex.:

```python
"This is a string"
'This is also a string'
```

### Métodos de strings

Métodos em linguagem de programação, são formas de atrelar uma funcionalidade a uma determinada variável. Entenda agora que, toda variável em python é *UM OBJETO* (Será explicado mais a frente).

Segue abaixo alguns métodos utilitários de strings:

1. title() -> primeira letra maiúscula, demais minúsculas
2. uppser() -> todas as letras maiúsculas
3. lower() -> todas as letras minúsculas
4. strip() -> remove os espaços em branco no início e final da string

### Concatenação de strings

Concatenar é o mesmo que combinar strings em uma só!

Para combinar strings, basta utilizar o (+) entre strings

Ex.:

```py
first_name = 'Pedro'
last_name = 'Otávio'

full_name = first_name + '' + last_name
print(full_name)
```

### Acrescentando tab e quebra de linha

É possível também alterar o formato em que o texto da string é exibido no terminal.

As formas de se fazer isso são:

- Tab: "\t"
- Quebra de linha: "\n"

Ex.:

```py
message = 'Languages:\n\tPython\n\tJavaScript\n\tC++'
print(message)
```

## Números

Em python, o tipo numérico aceita 2 formatos de números:
1. Os inteiros (int)
2. Os de ponto flutuante (float)

Além disso, é possivél realizar operações matemáticas com estes números, a partir dos operadores:
- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Exponenciação (**)
- Etc

Nota: fique atento ao operador de adição (+), pois ele funcionará de maneira diferente dependendo do tipo utilizado:
1. Em strings, realizará a concatenação (junção de 2 strings)
2. Em inteiros, realizará a adição comum

## Comentários

São uma forma de descrever, anotar ou mencionar fatos por exemplo, de trechos de código na programação em geral.

Cada linugagem possui sua própria forma de utilizar comentários. Em python é da seguinte forma:

```py
# Diga olá a todos
print('Hello Python people')
```

O trecho de código ou texto presente no comentário, não será executado pelo interpretador!