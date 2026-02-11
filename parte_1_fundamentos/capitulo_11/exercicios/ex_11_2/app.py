"""
11.2 – População: 

Modifique sua função para que ela exija um terceiro
parâmetro, population. Agora ela deve devolver uma única string no formato
Cidade, País – população xxx, por exemplo, Santiago, Chile – população
5000000. Execute test_cities.py novamente. Certifique-se de que
test_city_country() falhe dessa vez.
Modifique a função para que o parâmetro population seja opcional. Execute
test_cities.py novamente e garanta que test_city_country() passe novamente.
Escreva um segundo teste chamado test_city_country_population() que
verifique se você pode chamar sua função com os valores 'santiago', 'chile' e
'population=5000000'. Execute test_cities.py novamente e garanta que esse novo
teste passe.
"""

import unittest

def add_cities(city_name, country_name, population=0):
    if population:
        return f'{city_name.title()}, {country_name.title()} - população {str(population)}'
    else:
        return f'{city_name.title()}, {country_name.title()}'

class CityTestCases(unittest.TestCase):
    def test_city_country(self):
        city_string = add_cities('santiago', 'chile')
        self.assertEquals(city_string, 'Santiago, Chile')
    
    def test_city_country_population(self):
        city_string = add_cities('santiago', 'chile', 5000000)
        self.assertEquals(city_string, 'Santiago, Chile - população 5000000')

unittest.main()