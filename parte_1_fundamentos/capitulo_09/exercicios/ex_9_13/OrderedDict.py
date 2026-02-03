"""
9.13 – Reescrevendo o programa com OrderedDict: 

Comece com o Exercício
6.4 (página 155), em que usamos um dicionário-padrão para representar um
glossário. Reescreva o programa usando a classe OrderedDict e certifique-se de
que a ordem da saída coincida com a ordem em que os pares chave-valor foram
adicionados ao dicionário.
"""

from collections import OrderedDict

glossario_dev = OrderedDict()
glossario_dev['Código Limpo'] = 'Um código legivel, direto e com tudo o que seria necessário para representar sua lógica'
glossario_dev['Arrays'] = 'Variável que armazena valores ligados a um determinado endereço na memória'
glossario_dev['Debug'] = 'Termo utilizado para localizar e corrigir algum bug, inconsistência ou erro dentro de um software qualquer'
glossario_dev['Refatorar'] = 'Termo utilizado quando o usuário procurar modificar o código, tornando mais performático, sem alterar lógica principal'
glossario_dev['Classe'] = 'Protótipo de uma representação de objeto do mundo real'

print('Glosário de informações de desenvolvedor!\n')
for key, value in glossario_dev.items():
    print(f'{key}: \n-{value}')