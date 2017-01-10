import urllib
import time
from BeautifulSoup import *
import re
import pollution_data_class
import dpcc


# Data Source for pollution data can be found in variable base_page_url

base_page_url = "http://www.cpcb.gov.in/CAAQM/frmCurrentDataNew.aspx?"

url_suffix = {"anand_vihar":"StationName=Anand5Vihar&StateId=6&CityId=85","mandir_marg":"StationName=Mandir5Marg&StateId=6&CityId=85",\
"punjabi_bagh":"StationName=Punjabi5Bagh&StateId=6&CityId=85","rk_puram":"StationName=R5K5Puram&StateId=6&CityId=85",\
"igi_airport":"StationName=IGI5Airport&StateId=6&CityId=85","civil_lines":"StationName=Civil5Lines&StateId=6&CityId=85",
"dtu":"StationName=DTU&StateId=6&CityId=85","east_arjun_nagar":"StationName=East5Arjun5Nagar-Delhi5CPCB&StateId=6&CityId=85",
"shadipur":"StationName=Shadipur&StateId=6&CityId=85","sirifort":"StationName=Sirifort&StateId=6&CityId=85",
"dwarka":"StationName=Dwarka&StateId=6&CityId=85","ihbas":"StationName=Ihbas&StateId=6&CityId=85"}


	

def html_to_pollution_values_cpcb(html):
	"returns pm 2.5 and pm 10 values from dpcc html content. returns 0 values if data is not available"
	
	regex_pm25 = r"PM2.5<\/td><td Width='8%' align='center'>.*?<\/td><td Width='8%' align='center'>.*?<\/td><td Width='8%' align='right' ><span style='color:Blue;'>(.*?)<\/span>"
	regex_pm10 = r"PM10<\/td><td Width='8%' align='center'>.*?<\/td><td Width='8%' align='center'>.*?<\/td><td Width='8%' align='right' ><span style='color:Blue;'>(.*?)<\/span>"

	list_of_values_25 = re.findall(regex_pm25,html)
	list_of_values_10 = re.findall(regex_pm10,html)
	
	try:
		pm25 = float(list_of_values_25[0])
		pm10 = float(list_of_values_10[0])
	except:
		pm25 = 0
		pm10 = 0


	return pm25,pm10


def main():
	for location in url_suffix:
		pm25,pm10 = html_to_pollution_values_cpcb(dpcc.url_to_html(base_page_url+url_suffix[location]))
		a = pollution_data_class.pollution_data(location,pm25,pm10)
		a.describe()

def return_object_list():
	"returns pollution data as a list of object"
	return_list = []
	for location in url_suffix:
		pm25,pm10 = html_to_pollution_values_cpcb(dpcc.url_to_html(base_page_url+url_suffix[location]))
		object_pollution = pollution_data_class.pollution_data(location,pm25,pm10,-999)
		return_list.append(object_pollution)
		
	return return_list
		

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
		
