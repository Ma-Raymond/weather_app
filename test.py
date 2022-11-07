# import datetime as dt
# import requests

# BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
# API_KEY = "286ab1a2e60badb11ca2831fad6bd006"
# CITY = "Toronto"

# url = BASE_URL + "appid=" + API_KEY + "&q="+CITY + "&units=metric"

# response = requests.get(url).json()

# feelslike = response['main']['feels_like']
# humidity = response['main']['humidity']
# description = response['weather'][0]['description']

# sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
# sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# print(sunrise_time)
# print(response)



theInput = [1,2,2,2,3,3,4,2,5,6,6]

other_list = []
for i in range(len(theInput)):
    if theInput[i] in other_list:
        theInput[i] = 0
    else:
        other_list.append(theInput[i])
    
for i in range(len(theInput)-1):
    for j in range(i,len(theInput)-1):
        if theInput[j] == 0:
            temp = theInput[j]
            theInput[j] = theInput[j+1]
            theInput[j+1] = temp
print(theInput)