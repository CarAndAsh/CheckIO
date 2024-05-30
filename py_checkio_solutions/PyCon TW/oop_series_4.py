#!/usr/bin/env checkio --domain=py run oop-series-4
# Taken from mission OOP 3: Initializing

# Taken from mission OOP 2: Class Attributes
# Taken from mission OOP 1: First Look at Class and Object
from collections import namedtuple
class Car:
    wheels = 'four'
    doors = 4
    
    def __init__(self, brand='', model=''):
        self.brand = brand
        self.model = model
        
        
my_car = Car()
some_car1 = Car('Ford','Mustang')
some_car2 = Car('', 'Camaro')


# show me some OOP magic here
