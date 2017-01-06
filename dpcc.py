import urllib
import time
from BeautifulSoup import *
import re
import pollution_data_class


# Data Source for pollution data can be found in variable base_page_url

base_page_url = "http://www.dpccairdata.com/dpccairdata/display/"

url_suffix = {"anand_vihar":"avView15MinData.php","mandir_marg":"mmView15MinData.php",\
"punjabi_bagh":"pbView15MinData.php","rk_puram":"rkPuramView15MinData.php",\
"igi_airport":"airpoView15MinData.php","civil_lines":"civilLinesView15MinData.php"}


def url_to_html(url):
	"returns html froom url. I'll make this more robust later"
	try:
		html = urllib.urlopen(url).read()
		return html
	except:
		print "error : check internet connectivity at" , datetime.datetime.now().time()
		exit()
		
	

def html_to_pollution_values(html):
	"returns pm 2.5 and pm 10 values from dpcc html content. returns 0 values if data is not available"
	soup = BeautifulSoup(html)
	list_of_values = re.findall(r'>(.+)&micro',html)
	#time = re.findall(r'>(.+)</td>',html)
	#print time
	try:
		pm25 = int(list_of_values[3])
		pm10 = int(list_of_values[1])
	except:
		pm25 = 0
		pm10 = 0

	return pm25,pm10


def main():
	for location in url_suffix:
		pm25,pm10 = html_to_pollution_values(url_to_html(base_page_url+url_suffix[location]))
		a = pollution_data_class.pollution_data(location,pm25,pm10)
		a.describe()


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
		