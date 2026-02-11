# Capítulo 11 - Testando o seu código

Na programação, outro conceito fundamental para a permanência de um bom código em projetos extensos, são os testes.

Os testes garantem (ou não) que um determinado código funciona como deveria, em relação à diversas entradas.

Todo programador garante erros, querendo ou não. Portanto, é necessário que você teste seus códigos com frequência, identificando os problemas antes que os usuários encontrem.

## Testando

Antes de iniciar os estudos em testes, precisamos de algo para testar. 

```py
def get_formatted_name(first, last):
    """Gera um nome completo formatado de modo elegante."""
    full_name = f'{first} {last}'
    return full_name.title()
```

Vamos testar se esta função realmente funciona:

```py
from name_function import get_formatted_name

print('Enter "q" at any time to quit.')
while True:
    first = input('\nPlease give me a first name:')
    if first == 'q':
        break
    last = input('Please give me a last name:')
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print('\tNeatly formatted name: ' + formatted_name + '.')
```

O código aparentemente funciona como o esperado. Porém, imagine que o método seria modificado para lidar com nomes do meio também.

Python oferece uma forma eficiente para automatizar os testes da saída de uma função.

### Testes unitários e casos de teste

O módulo `unitest` pertence a biblioteca padrão de Python, fornecendo ferramentas para testar o código.

Um teste unitário verifica se um comportamento em específico de uma função está correto. Já o caso de teste, é uma coleção de testes unitários que, em conjunto, prova que uma funçãp se comporta como deveria em diversas situações que o programador espera que ela trate.

### Sintaxe

Para escrever um caso de teste para uma determinada função, importe o módulo `unittest` e a função que for testar. 

Em seguida crie uma classe que herde de unittest.TestCase e escreva métodos para testar diferentes aspectos do comportamento de sua função.

```py
import unittest
from name_funcion import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'"""
    def test_first_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formmated_name, 'Janis Joplin')
    
unittest.main()
```

Sempre nomeie a classe de acordo com a função que deseja testar, com a palavra "Test" ao final. Para os métodos, o mesmo: nomes de métodos que farão um teste unitário em específico.

O método acima, de asserção, verifica se o resultado recebido é igual ao resultado que você esperava receber.

A linha `unittedt.main()` diz ao Python executar todos os testes deste arquivo.

Segue agora um exemplo, onde ao executar o mesmo teste, a função irá falhar:

```py
def get_formatted_name(first, middle, last):
    """Gera um nome completo formatado de modo elegante."""
    full_name = f'{first} {middle} {last}'
    return full_name.title()

# NamesTestCase.py

import unittest
from name_funcion import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'"""
    def test_first_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formmated_name, 'Janis Joplin')
    
unittedt.main()
```

### Métodos de asserção

O módulo unittest possui uma variedade de métodos auxiliares na classe TestCase, ótimos para verificação de valores diversos

Segue abaixo algum exemplo deles:

```py
"""Método           Uso"""

assertEqual(a, b) # Verifica se a == b
assertNotEqual(a, b) # Verifica se a != b
assertTrue(x) # Verifica se x é True
assertFalse(x) # Verifica se x é False
assertIn(item, lista) # Verifica se item está em lista
assertNotIn(item, lista) # Verifica se item não está em lista
```

### Testando classes

Segue abaixo um exemplo de classe que será utilizada em testes mais para frente:

```py
class AnonymousSurvey():
    """Coleta respostas anônimas para uma pergunta de uma pesquisa."""
    def __init__(self, question):
        """Armazena uma pergunta e se prepara para armazenar as respostas."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Mostra a pergunta da pesquisa."""
        print(self.question)
    
    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa."""
        self.responses.append(new_response)
    
    def show_results(self):
        """Mostra todas as respostas dadas."""
        print('Survey results:')
        for response in responses:
            print(f'- {response}')

# Utilizando a classe

# Define uma pergunta e cria a pesquisa
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena as respostas à pergunta
my_survey.show_question()
print('Enter "q" at any time to quit.\n')
while True:
    response = input('Language: ').lower().strip()
    if response == 'q':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()
```

Agora, vamos testar se a classe permite respostas únicas

```py
import unittest
from survey import AnounymousSurvey

class TestAnounymousSurvey(unittest.TestCase):
    """Testa se uma única resposta é armazenada de forma apropriada."""
    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma apropriada."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
```

Note que, para o teste, é necessário criar uma instância da classe, para então verificar o comportamento esperado.

Um método auxiliar para testes, onde criar instâncias de forma simplificada, sem repetir as ações, é o método setUp já existente do TestCase.

```py
import unittest
from survey import AnounymousSurvey

class TestAnounymousSurvey(unittest.TestCase):
    """Testes para a classe AnounymousSurvey."""
    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas que poderão ser usados em todos os métodos de teste."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    """Testa se uma única resposta é armazenada de forma apropriada."""
    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma apropriada."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()