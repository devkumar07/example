from car import *

# Instantiating an object

arr = [12,25,27,28]
car1 = car('toyota','red','sedan',25, 15, arr)
car2 = car('lexus','blue','SUV',17, 15, arr)
print(car1.get_range())
print(car2.get_range())
print(car1.mileage)
car1.set_mileage(15)
print(car1.mileage)
print(car1.get_avg_mileage())
