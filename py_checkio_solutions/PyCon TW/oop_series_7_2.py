#!/usr/bin/env checkio --domain=py run oop-series-7-2
class Car:
    wheels = 'four'
    doors = 4
    working_engine = False

    def __init__(self, brand='', model='', fuel_consumption=7):
        self.brand = brand
        self.model = model
        self.fuel_used = 0
        self.fuel_consumption = fuel_consumption

    def start_engine(self):
        print("Engine has started")
        self.working_engine = True

    def stop_engine(self):
        print("Engine has stopped")
        self.working_engine = False

    def drive(self, distance: int):
        if self.working_engine:
            self.fuel_used += distance / 100 * self.fuel_consumption
            print(f"Currently driven {distance} km, total fuel used - {self.fuel_used} l")
        else:
            print("Start the car before driving!")


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

    def drive(self, distance: int):
        if self.working_engine:
            print(f'Currently driven {distance} km on electric motor')
        else:
            print("Start the car before driving!")


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
some_car2.drive(100)
my_electric_car.drive(120)
my_electric_car.drive(120)
