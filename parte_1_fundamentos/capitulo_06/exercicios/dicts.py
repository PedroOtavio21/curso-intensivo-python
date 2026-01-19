"""
6.1 – Pessoa: 

Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário.
"""

person_1 = {
    'first_name': 'Pedro',
    'last_name': 'Otávio',
    'age': 23,
    'city': 'Fortaleza/CE'
}

"""
6.2 – Números favoritos: 

Use um dicionário para armazenar os números favoritos
de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
dicionário. Pense em um número favorito para cada pessoa e armazene cada um
como um valor em seu dicionário. Exiba o nome de cada pessoa e seu número
favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos
e obtenha alguns dados reais para o seu programa.
"""

favorite_numbers = {
    'Pedro': 14,
    'Luiz': 7,
    'Pires': 9,
    'Davi': 49,
    'Bia': 32
}

print('O número favorito do Luiz é: ' + str(favorite_numbers['Luiz']))
# ...

"""
6.3 – Glossário: 

Um dicionário Python pode ser usado para modelar um dicionário
de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu nos
capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores.
• Mostre cada palavra e seu significado em uma saída formatada de modo
elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
significado, ou apresentar a palavra em uma linha e então exibir seu significado
indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
para inserir uma linha em branco entre cada par palavra-significado em sua
saída.
"""

glossario_dev = {
    'Código Limpo': 'Um código legivel, direto e com tudo o que seria necessário para representar sua lógica',
    'Arrays': 'Variável que armazena valores ligados a um determinado endereço na memória',
    'Debug': 'Termo utilizado para localizar e corrigir algum bug, inconsistência ou erro dentro de um software qualquer',
    'Refatorar': 'Termo utilizado quando o usuário procurar modificar o código, tornando mais performático, sem alterar lógica principal.',
    'Classe': 'Protótipo de uma representação de objeto do mundo real.'
}

# Incrementar mais 3 informações e depois printá-las quando necessário.

"""
6.4 – Glossário 2: 

Agora que você já sabe como percorrer um dicionário com um
laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de
instruções print por um laço que percorra as chaves e os valores do dicionário.
Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de
Python ao seu glossário. Ao executar seu programa novamente, essas palavras e
significados novos deverão ser automaticamente incluídos na saída.
"""

print('Glosário dev:')
for key, value in glossario_dev.items():
    print(key + ': ' + value)

"""
6.5 – Rios: 

Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
"""

rios_do_mundo = {
    'amazonas': 'brasil',
    'nilo': 'egito',
    'mississippi': 'estados unidos'
}

for key, value in rios_do_mundo.items():
    print('O ' + key.title() + ' corre pelo ' + value.title())
    print(key.title())
    print(value.title())

"""
6.6 – Enquete: 

Utilize o código em favorite_languages.py (página 150).
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.
Se ainda não participaram da enquete, apresente uma mensagem convidando-as
a responder.
"""

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

pessoas_para_enquete = ['jen', 'pedro', 'joão', 'sarah', 'phil']
for pessoa in pessoas_para_enquete:
    if pessoa not in favorite_languages.keys():
        print(pessoa.title() + ', participe da enquete, por favor!')
    else:
        print(pessoa.title() + ', obrigador por participar da enquete.')

"""
6.7 – Pessoas: 

Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista de
pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
sabe sobre cada pessoa.
"""

person_2 = {
    'first_name': 'João',
    'last_name': 'Guilerme',
    'age': 33,
    'city': 'Fortaleza/CE'
}

person_3 = {
    'first_name': 'Ana',
    'last_name': 'Beatriz',
    'age': 22,
    'city': 'Fortaleza/CE'
}

people = [person_1, person_2, person_3]
for person in people:
    print('Nome: ' + person['first_name'])
    print('Sobrenome: ' + person['last_name'])
    print('Idade: ' + str(person['age']))
    print('Cidade: ' + person['city'])
    print()

"""
6.8 – Animais de estimação: 

Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer
isso, apresente tudo que você sabe sobre cada animal de estimação.
"""

pet_1 = {
    'nome': 'zeus',
    'tipo': 'cachorro',
    'dono': 'luis'
}

pet_2 = {
    'nome': 'morfeu',
    'tipo': 'gato',
    'dono': 'maria'
}

pet_3 = {
    'nome': 'louro',
    'tipo': 'papagaio',
    'dono': 'Ana'
}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print('Nome de Pet: ' + pet['nome'].title())
    print('Tipo de Pet: ' + pet['tipo'].title())
    print('Dono do Pet: ' + pet['dono'].title())
    print('---')

"""
6.9 – Lugares favoritos: 

Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três lugares
favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o
dicionário com um laço e apresente o nome de cada pessoa e seus lugares
favoritos.
"""

favorite_places = {
    'paris': 'ana',
    'povoa': 'sophia',
    'mossoró': 'luis'
}

for place, person in favorite_places.items():
    print(key.title() + ' é o lugar favorito de ' + person.title())

"""
6.10 – Números favoritos: 

Modifique o seu programa do Exercício 6.2 (página
147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos.
"""

favorite_numbers = {
    'Pedro': [14, 8, 10],
    'Luiz': [7, 10],
    'Pires': [9],
    'Davi': [49, 32, 7],
    'Bia': [32, 10, 11]
}

for name, numbers in favorite_numbers.items():
    print('Nome: ' + name.title())
    print('Números: ' + str(numbers))
    print('---')

"""
6.11 – Cidades: 

Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
cada cidade e inclua o país em que a cidade está localizada, a população
aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
devem ser algo como country, population e fact. Apresente o nome de cada
cidade e todas as informações que você armazenou sobre ela
"""

cities = {
    'fortaleza': {
        'country': 'brasil',
        'population': 2578483,
        'fact': 'foi a primeira capital brasileira a abolir a escravidão'
    },
    'brasilia': {
        'country': 'brasil',
        'population': 2996899,
        'fact': 'vista de cima, tem o formato de um avião ou borboleta'
    },
    'salvador': {
        'country': 'brasil',
        'population': 2564204,
        'fact': 'uma igreja para cada dia do ano (mais de 365 templos)'
    }
}

for key, values in cities.items():
    print('Cidade: ' + key.title())
    print('Informações: ' + str(values))