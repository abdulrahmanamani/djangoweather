from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=5&API_KEY=7EE5B4E9-59A6-4BC2-96D1-D9ABD114E7AA")

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
		  	category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="good"
		elif api[0]['Category']['Name'] == "Moderate":
		  	category_description = "(51-100) Air quality is acceptable; satisfactory, and air pollution poses little or no risk."
		  	category_color ="moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		  	category_description = "(101-150) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
		  	category_description = "(151-200) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
		  	category_description = "(201-300) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
		  	category_description = "(301-500) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="hazardous"
		


		#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=7EE5B4E9-59A6-4BC2-96D1-D9ABD114E7AA
		return render(request,'home.html',{'api': api,
			'category_description': category_description,
			'category_color': category_color })
	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=7EE5B4E9-59A6-4BC2-96D1-D9ABD114E7AA")

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
		  	category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="good"
		elif api[0]['Category']['Name'] == "Moderate":
		  	category_description = "(51-100) Air quality is acceptable; satisfactory, and air pollution poses little or no risk."
		  	category_color ="moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		  	category_description = "(101-150) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
		  	category_description = "(151-200) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
		  	category_description = "(201-300) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
		  	category_description = "(301-500) Air quality is considered satisfactory, and air pollution poses little or no risk."
		  	category_color ="hazardous"
		


		#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=7EE5B4E9-59A6-4BC2-96D1-D9ABD114E7AA
		return render(request,'home.html',{'api': api,
			'category_description': category_description,
			'category_color': category_color })

def about(request):
	return render(request,'about.html',{})