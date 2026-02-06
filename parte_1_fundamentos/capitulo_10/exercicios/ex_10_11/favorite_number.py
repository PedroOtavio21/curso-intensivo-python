"""
10.11 – Número favorito: 

Escreva um programa que pergunte qual é o número
favorito de um usuário. Use json.dump() para armazenar esse número em um
arquivo. Escreva um programa separado que leia esse valor e apresente a
mensagem “Eu sei qual é o seu número favorito! É _____.”.
"""

import json
from pathlib import Path

file_path = Path(__file__).parent / 'result.json'

def set_favorite_number():
    favorite_number = int(input('Me informe qual o seu número favorito: ').strip())

    try:
        with open(file_path, 'w') as file_object:
            json.dump(favorite_number, file_object)
    except FileNotFoundError:
        print('Caminho inserido está errado ou não existe.')
    else:
        print(f'Número {str(favorite_number)} salvo com sucesso.') 

def get_favorite_number():
    try:
        with open(file_path) as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        print('Caminho inserido está errado ou não existe.')
    else:
        print(f'Eu sei qual é o seu número favorito! É {str(number)}.')

set_favorite_number()
get_favorite_number()