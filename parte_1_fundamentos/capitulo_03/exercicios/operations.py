"""
3.8 – Conhecendo o mundo: 

Pense em pelo menos cinco lugares do mundo que
você gostaria de visitar.
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em
ordem alfabética.
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista
propriamente dita.
• Mostre que sua lista manteve sua ordem original exibindo-a.
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a
ordem da lista original.
• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para
mostrar que ela voltou à sua ordem original.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
"""

places = ['Londres', 'Chicago', 'Tókio', 'Gramado', 'Barcelona']

print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

"""
3.10 – Todas as funções: 

Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
uma lista contendo esses itens e então utilize cada função apresentada neste
capítulo pelo menos uma vez.
"""

teams = ['Manchester United', 'Real Madrid', 'Barcelona', 'Bayern Munchen', 'Milan', 'Liverpool']
print('Tamanho da lista: ' + str(len(teams)))
print(sorted(teams, reverse=True))
teams.append('Santos Fc')
teams.pop(2)
print(teams)

# Há outros métodos que poderiam ser implementados, porém houve uma preguiça :)
