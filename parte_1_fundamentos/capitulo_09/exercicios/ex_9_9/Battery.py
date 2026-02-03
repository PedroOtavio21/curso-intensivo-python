"""
9.9 – Upgrade de bateria: 

Use a última versão de electric_car.py desta seção.
Acrescente um método chamado upgrade_battery() na classe Battery. Esse
método deve verificar a capacidade da bateria e defini-la com 85 se o valor for
diferente. Crie um carro elétrico com uma capacidade de bateria default, chame
get_range() uma vez e, em seguida, chame get_range() uma segunda vez após
fazer um upgrade da bateria. Você deverá ver um aumento na distância que o
carro é capaz de percorrer.
"""

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f'this car can go approximately {str(range)}'
        message += ' miles on a full charge'
        print(message)

    def describe_battery(self):
        print(f'This car has a {str(self.battery_size)}')

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

byd_dolphin = EletricCar('byd', 'dolphin mini', 2025)
byd_dolphin.battery.get_range()
byd_dolphin.battery.upgrade_battery()
byd_dolphin.battery.get_range()