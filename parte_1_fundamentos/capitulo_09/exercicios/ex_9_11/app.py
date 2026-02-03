"""
9.11 – Importando Admin: 

Comece com seu programa do Exercício 9.8 (página
241). Armazene as classes User, Privileges e Admin em um módulo. Crie um
arquivo separado e uma instância de Admin e chame show_privileges() para
mostrar que tudo está funcionando de forma apropriada.
"""

from Admin import Admin
my_admin = Admin('pedro', 'otávio', 'pedro_21', 2021)

my_admin.describe_user()
my_admin.privileges.show_privileges()
my_admin.privileges.add_privileges('can add user', 'can delete user')
my_admin.privileges.show_privileges()