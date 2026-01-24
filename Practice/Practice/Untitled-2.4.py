class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        self.mileage += km

    def info(self):
        print(self.brand, self.year, self.mileage)

    def __str__(self):
        return self.brand + " " + str(self.year) + " " + str(self.mileage)


car = Car("Toyota", 2018, 45000)
print(car)
car.drive(150)
car.info()
