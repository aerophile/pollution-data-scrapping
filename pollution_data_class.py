import time


#class definatons to be followed by all different wesbite scripts
class pollution_data:
	def __init__(self,location,pm25 = 0,pm10 = 0,aqi=-999,data_source = "NA"):#adopting us embassy aqi default non functioning value equivalent as -999
		self.location = location
		self.data_time = time.time()
		self.pm10 = pm10
		self.pm25 = pm25
		self.aqi = aqi
		self.data_source = data_source
	

	def describe(self):
		print self.location, self.data_time , self.pm25 , self.pm10 , self.aqi , self.data_source





