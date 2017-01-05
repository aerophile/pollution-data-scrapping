import urllib
import datetime
from BeautifulSoup import *

# Data Source for pollution data can be found in variable base_page_url

base_page_url = "http://www.dpccairdata.com/dpccairdata/display/"

url_suffix = {"anand_vihar":"avView15MinData.php","mandir_marg":"mmView15MinData.php",\
"punjabi_bagh":"pbView15MinData.php","rk_puram":"rkPuramView15MinData.php",\
"igi_airport":"airpoView15MinData.php","civil_lines":"civilLinesView15MinData.php"}




print "Checked on ",datetime.datetime.now().time()



for page in url_suffix:
	
	try:
		html = urllib.urlopen(base_page_url+url_suffix[page]).read()
		
	except:
		print "error : check internet connectivity "
		
	soup = BeautifulSoup(html)
	list_of_tables = soup("table")
	
	if len(list_of_tables) > 7 :
		print "Pollution data available at : " + page
