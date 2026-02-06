"""
10.9 – Gatos e cachorros silenciosos: 

Modifique o seu bloco except do Exercício
10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.
"""

from pathlib import Path

file_path = Path(__file__).parent / 'teste.txt'

try:
    with open(file_path) as file_object:
        content = file_object.read()
except FileNotFoundError:
    pass
else:
    print(content)
