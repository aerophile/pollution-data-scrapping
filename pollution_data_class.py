import time


#class definatons to be followed by all different wesbite scripts
class pollution_data:
	def __init__(self,location,pm25 = 0,pm10 = 0):
		self.location = location
		self.data_time = time.time()
		self.pm10 = pm10
		self.pm25 = pm25
	

	def describe(self):
		print self.location, self.data_time , self.pm25 , self.pm10





