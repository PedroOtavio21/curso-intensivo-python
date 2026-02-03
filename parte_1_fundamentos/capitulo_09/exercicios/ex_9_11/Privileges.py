class Privileges():
    def __init__(self):
        self.privileges = []

    def add_privileges(self, *privileges):
        self.privileges.extend(privileges)

    def show_privileges(self):
        print('Principais privilégios:')
        for privilege in self.privileges:
            print(f'-{privilege}')