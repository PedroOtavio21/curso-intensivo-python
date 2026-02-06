"""
10.10 – Palavras comuns: 

Acesse o Projeto Gutenberg (http://gutenberg.org/ ) e
encontre alguns textos que você gostaria de analisar. Faça download dos arquivostexto
dessas obras ou copie o texto puro de seu navegador para um arquivo-texto
em seu computador.
Você pode usar o método count() para descobrir quantas vezes uma palavra ou
expressão aparece em uma string. Por exemplo, o código a seguir conta quantas
vezes a palavra 'row' aparece em uma string:
>line = "Row, row, row your boat"
>line.count('row')
2
>line.lower().count('row')
3
Observe que converter a string para letras minúsculas usando lower() faz com
que todas as formas da palavra que você está procurando sejam capturadas,
independentemente do modo como elas estiverem grafadas.
Escreva um programa que leia os arquivos que você encontrou no Projeto
Gutenberg e determine quantas vezes a palavra 'the' aparece em cada texto.
"""

from pathlib import Path

file_path = Path(__file__).parent / 'example.txt'

try:
    with open(file_path) as file_object:
        content = file_object.read()
except FileNotFoundError:
    pass
else:
    print(content)

palavras = content.lower().split()
print(f'\nQuantidade de vezes que "Love" aparece: {palavras.count("love")}')
