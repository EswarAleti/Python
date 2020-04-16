class CarRecord:
	def __init__(self):
		self.year_made = 0
		self.car_vin=''
	def __str__(self):
		return 'Year: '+str(self.year_made)+', VIN: '+self.car_vin
my_car = CarRecord()
my_car.year_made = int(input())
my_car.car_vin = input()
print(my_car)