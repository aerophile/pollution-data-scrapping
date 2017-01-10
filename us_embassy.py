import urllib
import time
from BeautifulSoup import *
import re
import pollution_data_class
import dpcc


# Data Source for pollution data can be found in variable base_page_url

base_page_url = "http://clonewdelhi.com/includes/aqnow.php"

url_suffix = {"us_embassy_chankyapuri":"/"}

def html_to_pollution_values_usembassy(html):
	"returns pm 2.5 and pm 10 values from dpcc html content. returns 0 values if data is not available"
	
	regex_pm25 = r'#ND_Cval"\).text\("(.*?)"\);'
	
	regex_aqi = r'#ND_val"\).text\("(.*?)"\);'
	list_of_values_25 = re.findall(regex_pm25,html)
	
	list_of_values_aqi = re.findall(regex_aqi,html)
	
	try:
		pm25 = float(list_of_values_25[0])
		pm10 = 0
		aqi = float(list_of_values_aqi[0])
	except:
		pm25 = 0
		pm10 = 0
		aqi = -999 #default for aqi not available is -999


	return pm25,pm10,aqi

def return_object_list():
	"returns pollution data as a list of object"
	return_list = []
	for location in url_suffix:
		pm25,pm10,aqi = html_to_pollution_values_usembassy(dpcc.url_to_html(base_page_url+url_suffix[location]))
		object_pollution = pollution_data_class.pollution_data(location,pm25,pm10,aqi)
		return_list.append(object_pollution)
		
	return return_list

def main():
	for location in url_suffix:
		pm25,pm10,aqi = html_to_pollution_values_usembassy(dpcc.url_to_html(base_page_url+url_suffix[location]))
		a = pollution_data_class.pollution_data(location,pm25,pm10,aqi)
		a.describe()
		


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()