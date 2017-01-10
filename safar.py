import urllib
import time
from BeautifulSoup import *
import re
import pollution_data_class
import dpcc


# Data Source for pollution data can be found in variable base_page_url

base_page_url = "http://safar.tropmet.res.in/safar_led_slider.php?"

url_suffix = {"pusa":"city_id=3&station_id=2","lodhi_road":"city_id=3&station_id=3",
"delhi_university":"city_id=3&station_id=4","igi_airport":"city_id=3&station_id=5",
"noida":"city_id=3&station_id=6","mathura_road":"city_id=3&station_id=7",
"ayanagar":"city_id=3&station_id=8","pitampura":"city_id=3&station_id=9",
"dhirpur":"city_id=3&station_id=10","gurgaon":"city_id=3&station_id=11"}

	

def html_to_pollution_values_safar(html):
	"returns pm 2.5 and pm 10 values from dpcc html content. returns 0 values if data is not available"
	
	regex_pm25 = r'PM 2.5<\/td>(.|\n)*?<td style="text-align:center !important">(.*?)<\/td>'
	regex_pm10 = r'PM10</td>(.|\n)*?<td style="text-align:center !important">(.*?)</td>'
	regex_aqi = r'AQI-(.*?)<'
	list_of_values_25 = re.findall(regex_pm25,html)
	list_of_values_10 = re.findall(regex_pm10,html)
	list_of_values_aqi = re.findall(regex_aqi,html)
	
	try:
		pm25 = float(list_of_values_25[0][1])
		pm10 = float(list_of_values_10[0][1])
		aqi = float(list_of_values_aqi[1])
	except:
		pm25 = 0
		pm10 = 0
		aqi = -999 #default for aqi not available is -999


	return pm25,pm10,aqi


def return_object_list():
	return_list = []
	for location in url_suffix:
		pm25,pm10,aqi = html_to_pollution_values_safar(dpcc.url_to_html(base_page_url+url_suffix[location]))
		object_pollution = pollution_data_class.pollution_data(location,pm25,pm10,aqi)
		return_list.append(object_pollution)
		
	return return_list
		

def main():
	for location in url_suffix:
		pm25,pm10,aqi = html_to_pollution_values_safar(dpcc.url_to_html(base_page_url+url_suffix[location]))
		a = pollution_data_class.pollution_data(location,pm25,pm10,aqi)
		a.describe()
		


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()