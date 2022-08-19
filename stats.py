import json
import webbrowser

# dictionary with parallel logic
stats_list = {'text': ['Total items', 'Trimmed items', 'Remaining'], 'data': [0, 0, 0]}

def show_stats(new_data, unique_data_list):
	'''Function to calculate and
	show statistics'''
	global stats_list
	print("\n---------- STATS ----------")

	# if new_data then update dict or else keep it in initial form
	if new_data:
		stats_list['data'][0] = len(new_data)

		trimmed_content = len(new_data) - len(unique_data_list)

		# Calculates trimmed items in numbers and in percentage.
		stats_list['data'][1] = trimmed_content 

		# Calculates trimmed items in numbers and in percentage.
		stats_list['data'][2] = len(unique_data_list)


	# Converting and Writing the data to json file
	file = open('stats.json', 'w')
	file.write(json.dumps(stats_list))
	file.close()

	url = "file:///C:/Users/786%20computers/Desktop/python_work/data_sanitizer/chart.html"
	
	return webbrowser.open(url, new=2)
