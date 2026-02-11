class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_raise(self, new_raise=5000):
        self.salary += new_raise

    def show_anual_salary(self):
        return self.salary