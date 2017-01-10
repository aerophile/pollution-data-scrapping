import pollution_data_class
import dpcc
import cpcb
import safar
import us_embassy
import json



def get_data():
	"returns list of pollution data objects"
	combined_data_list = []	
	combined_data_list.extend(cpcb.return_object_list())
	combined_data_list.extend(safar.return_object_list())
	combined_data_list.extend(us_embassy.return_object_list())
	combined_data_list.extend(dpcc.return_object_list())
	combined_data_list.sort(key=lambda x: x.location) # sorts alphabetically by location
	return combined_data_list

def main():
	make_json()

def make_json():
	"converts and prints object list to json"
	combined_data_list = get_data()
	for a in combined_data_list:
		a.describe()
	#need to add the actual Json part here

if __name__ == '__main__':
	main()
