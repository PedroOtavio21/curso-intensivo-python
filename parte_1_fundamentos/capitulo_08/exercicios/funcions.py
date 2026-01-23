"""
8.1 – Mensagem: 

Escreva uma função chamada display_message() que mostre
uma frase informando a todos o que você está aprendendo neste capítulo. Chame
a função e certifique-se de que a mensagem seja exibida corretamente.
"""

def display_message():
    print('Neste capítulo, estou aprendendo sobre funções em python.')

display_message()

"""
8.2 – Livro favorito: 
Escreva uma função chamada favorite_book() que aceite

um parâmetro title. A função deve exibir uma mensagem como Um dos meus
livros favoritos é Alice no país das maravilhas. Chame a função e não
se esqueça de incluir o título do livro como argumento na chamada da função.
"""

def favorite_book(title):
    print('Um dos meus livros favoritos é ' + title)

favorite_book('Alice no país das maravilhas')

"""
8.3 – Camiseta: 

Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta. A
função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem
estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.
"""

def make_shirt(size, text):
    print('Tamanho da camisa: ' + size.title())
    print('Mensagem estampada: ' + text)

make_shirt('m', 'Do More')
make_shirt(size='g', text='I love Python')

"""
8.4 – Camisetas grandes: 

Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta de
qualquer tamanho com uma mensagem diferente.
"""

def make_shirt(size='m', text='Eu amo Python'):
    print('Tamanho da camisa: ' + size.title())
    print('Mensagem estampada: ' + text)

make_shirt('m')
make_shirt()
make_shirt('g', 'Eu amo Programar')

"""
8.5 – Cidades: 

Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades diferentes
em que pelo menos uma delas não esteja no país default.
"""

def describe_city(name, country='Islândia'):
    print(name + ' está localizada em ' + country)

describe_city('Fortaleza', 'Brasil')
describe_city('Texas', 'Estados Unidos')
describe_city('Reykjavik')

"""
8.6 – Nomes de cidade: 

Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim:
"Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.
"""

def city_country(name, country):
    full_string = name + ', ' + country
    return full_string.title()

city_country('Santiago', 'Chile')
city_country('Las Vegas', 'EUA')
city_country('Barcelona', 'Espanha')

"""
8.7 – Álbum: 

Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas duas
informações. Use a função para criar três dicionários que representem álbuns
diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão
armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar o
número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor
para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
menos uma nova chamada da função incluindo o número de faixas em um álbum.
"""

def make_album(artist, title):
    new_album = {'name': artist, 'title': title}
    return new_album

print(make_album('avicii', 'wake me up'))
print(make_album('avicii', 'hey brother'))
print(make_album('major lazer', 'lean on'))

"""
8.8 – Álbuns dos usuários: 

Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e o
título de um álbum. Depois que tiver essas informações, chame make_album() com
as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um
valor de saída no laço while.
"""

active = True
while active:
    name_artist = input('Insira o nome de seu artista: ')
    album_name = input('Insira o nome do album do artista: ')
    album = make_album(name_artist, album_name)
    print('Album criado com sucesso.')
    print(album)

    info = input('Deseja continuar criando albuns? ("sim"/"não")').lower()
    if info == 'não' or info == 'nao':
        active = False