import statistics
class car:

    #constructor: creates an instance of an object
    def __init__(self, make, color, type, mileage, fuelCap, arr):
        self.make = make  
        self.color = color
        self.type = type
        self.mileage = mileage
        self.fuelCap = fuelCap
        self.arr = arr

    #get method
    def get_make(self):
        return self.make
    #method 2
    def get_range(self):
        return self.mileage * self.fuelCap
    #set method 
    def set_mileage(self, mileage):
        self.mileage = mileage
    
    #get method
    def get_avg_mileage(self):
        return statistics.mean(self.arr)