from User import User
from Privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, user_name, registration):
        super().__init__(first_name, last_name, user_name, registration)
        self.privileges = Privileges()