#!/usr/bin/env checkio --domain=py run oop-series-6
# Taken from mission OOP 5: Parent - Child
# Taken from mission OOP 4: Adding Methods
# Taken from mission OOP 3: Initializing
# Taken from mission OOP 2: Class Attributes
# Taken from mission OOP 1: First Look at Class and Object


class Car:
    wheels = 'four'
    doors = 4
    working_engine = False

    def __init__(self, brand='', model=''):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print("Engine has started")
        self.working_engine = True

    def stop_engine(self):
        print("Engine has stopped")
        self.working_engine = False


class ElectricCar(Car):
    def __init__(self, battery_capacity: int, brand='', model=''):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print("Electric motor has started")
        self.working_engine = True

    def stop_engine(self):
        print("Electric motor has stopped")
        self.working_engine = False


my_car = Car()
some_car1 = Car('Ford', 'Mustang')
some_car2 = Car('', 'Camaro')
some_car1.start_engine()
some_car2.start_engine()
my_electric_car = ElectricCar(100, "Tesla", "Model 3")
my_electric_car.start_engine()
my_electric_car2 = ElectricCar(60, "Toyota", "Prius")
my_electric_car2.start_engine()
my_electric_car2.stop_engine()
