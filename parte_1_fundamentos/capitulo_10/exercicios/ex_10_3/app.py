"""
10.3 – Convidado: 

Escreva um programa que pergunte o nome ao usuário.
Quando ele responder, escreva o nome em um arquivo chamado guest.txt.
"""

from pathlib import Path

file_name = Path(__file__).parent / 'guest.txt'

text = input('Qual o seu nome de usuário?').strip()
text = f'Nome de Usuário: {text}\n'

with open(file_name, 'w') as file_object:
    file_object.write(text)