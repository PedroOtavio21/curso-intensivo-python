"""
2.3 - Mensagem pessoal:  
Armazene o nome de uma pessoa em uma variável e
apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples, como
“Alô Eric, você gostaria de aprender um pouco de Python hoje?”.
"""

name_person = 'Pedro'
print('Alô, ' + name_person + ', você gostaria de aprender um pouco de Python hoje?')


"""
2.4 - Letras maiúsculas e minúsculas em nomes:

Armazene o nome de uma
pessoa em uma variável e então apresente o nome dessa pessoa em letras
minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula.
"""

person = 'Pedro'
print('Nome em maiúsculo: ' + person.upper())
print('Nome em minúsculo: ' + person.lower())
print('Primeira letra maiúscula: ' + person.title())

"""
2.5 - Citação famosa:

Encontre uma citação de uma pessoa famosa que você
admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparência a
seguir, incluindo as aspas:
Albert Einstein certa vez disse: “Uma pessoa que nunca cometeu um erro jamais
tentou nada novo.”
"""

quote = '"Se pude enxergar mais longe, foi porque me apoiei em ombros de gigantes" - Isaac Newton'
print(quote)

"""
2.6 - Citação famosa 2:

Repita o Exercício 2.5, porém, desta vez, armazene o
nome da pessoa famosa em uma variável chamada famous_person. Em seguida,
componha sua mensagem e armazene-a em uma nova variável chamada message.
Exiba sua mensagem.
"""

person = 'Isaac Newton'
quote = '"Se pude chegar mais longe, foi porque me apoiei em ombros de gigantes" - ' + person
print(quote)

"""
2.7 - Removendo caracteres em branco de nomes:

Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembrese
de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do nome
sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções de
remoção de espaços: lstrip(), rstrip() e strip().
"""

new_person = '\tPedro\n'
print(new_person)
print(new_person.lstrip())
print(new_person.rstrip())
print(new_person.strip())