#DSC 510
#Week 12
#API weather final
#Author Breanna Parker
#11/7/22

# Display the weather forecast in a readable format to the user. Do not display the weather data in Kelvin, since this is not readable to the average person.  You should allow the user to choose between Celsius and Fahrenheit and ideally also Kelvin.
# Use comments within the application where appropriate in order to document what the program is doing. Comments should add value to the program and describe important elements of the program.
# Validate whether the user entered valid data. If valid data isn’t presented notify the user. Your program should never crash with bad user input.
# Use the Requests library in order to request data from the webservice.
# Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.
# You must have proper coding convention including proper variable names (See PEP8).

import json
import requests
from env import API_KEY
from urllib.request import urlopen


BACKOFF_TIME = 30


class openWeather():
  def __init__(self):
    self.appid = "API_KEY"
    self.lat = "lat"
    self.lon = "lon"
  
  def lat_lon(self,response):
    url_lat_lon = f'http://api.openweathermap.org/data/2.5/weather?lat={response["lat"]}&lon={response["lon"]}&&appid={API_KEY}'
    response2 = requests.get(url_lat_lon).json()
    print(response2)
    # temps = response2["main"]
    # weather_dict = {}
    # temp_dict = {}
    # weather_dict["weather_sky"] = response2["weather"][0]["main"]
    # weather_dict["humidity"] = response2["main"]["humidity"]
    # temp_dict["Current Temperature"] = response2["main"]["temp"]
    # temp_dict["Feels Like"] = response2["main"]["feels_like"]
    # temp_dict["Minimum Temperature"] = response2['main']["temp_min"]
    # temp_dict["Maximum Temperature"] = response2["main"]["temp_max"]
    # print(weather_dict, temp_dict)
    temp_quest = input ("select one: c for celcius, f for fahrenheit, or k for kelvin?\n")
    if temp_quest.lower() == "c":
        self.k_to_c(response2)
    elif temp_quest.lower() == 'f':
        self.k_to_f(response2)
    elif temp_quest.lower() == 'k':
      print("For city:", response2["name"])
      print("Current Temperature:", round(response2["main"]["temp"]), "K")
      print("Feels Like:", round(response2["main"]["feels_like"]), "K")  
      print("Minimum Temperature:", round(response2['main']["temp_min"]), "K") 
      print("Maximum Temperature:", round(response2["main"]["temp_max"]), "K")
      print("Humdity:", response2["main"]["humidity"], "%")
      print("Sky:", response2["weather"][0]["main"])
    # elif temp_quest.lower() == 'f':
    #     self.k_to_f(temp_dict)
    # elif temp_quest.lower() == 'k':
    #   for word in sorted(temps, key = temps.get):         
    #     print (word, temps[word])
    else:
        print("Error") 
    
  
  def weather_city(self,city_name,state):
    try:
      url_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state}&limit=5&appid={API_KEY}'
      res = requests.get(url_city).json()
      response = {}
      for r in res:
        response.update(r)
      self.lat_lon(response)      
    
    except:
      print("Error, try again!")
  
  def weather_zip(self,zip_code):
    try:
      url_zip = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={API_KEY}'
      response = requests.get(url_zip).json()
      self.lat_lon(response)
    
    except:
      print("Error, pick a valid zip code!")
    # else:
    #   data = json.loads(source)

  def k_to_c(self,response2):
    print("For city:", response2["name"])
    curr_temp = round(response2["main"]["temp"] - 273.15)
    feels_like = round(response2["main"]["feels_like"] - 273.15)
    min_temp = round(response2['main']["temp_min"] - 273.15)
    max_temp = round(response2["main"]["temp_max"] - 273.15)
    print("Current Temperature:", curr_temp, "C")
    print("Feels Like:", feels_like, "C")  
    print("Minimum Temperature:", min_temp, "C") 
    print("Maximum Temperature:", max_temp, "C")
    print("Humdity:", response2["main"]["humidity"], "%")
    print("Sky:", response2["weather"][0]["main"])
    
    
  def k_to_f(self,response2):
    print("For city:", response2["name"])
    curr_temp = round((response2["main"]["temp"] - 273.15) * 9 / 5 + 32)
    feels_like = round((response2["main"]["feels_like"] - 273.15) * 9 / 5 + 32)
    min_temp = round((response2['main']["temp_min"] - 273.15) * 9 / 5 + 32)
    max_temp = round((response2["main"]["temp_max"] - 273.15) * 9 / 5 + 32)
    print("Current Temperature:", curr_temp, "F")
    print("Feels Like:", feels_like, "F")  
    print("Minimum Temperature:", min_temp, "F") 
    print("Maximum Temperature:", max_temp, "F")
    print("Humdity:", response2["main"]["humidity"], "%")
    print("Sky:", response2["weather"][0]["main"])
    
    # for val in temp_dict.keys():
    #   converted = (val - 273.15) * 9 / 5 + 32
    #   return int(converted)
    # for k,v in temp_dict.items():
    #       # temp_dict[k] = int((temp_dict[v] - 273.15) * 9 / 5 + 32)
    #   new_val = (temp_dict[v] - 273.15) * 9 / 5 + 32
    #   print(k)
    #   print(v)
    #   print(new_val)
    #       # temp_dict.update({k: new_val})
    # print(temp_dict)

def main():
  user_name = input('What is your name?\n')       #weclomes user
  print("Hello",user_name)
  user_name = openWeather()   #connects user to the openweather class method
  
  while True:       #creates a loop for user to continue using code until they choose to exit
    line = input ("Choose zip or city or quit \n") #asks for user input
    
    if line == "zip":      
      zip_code = input("What is the zip code?\n")
      user_name.weather_zip(zip_code)     #passes zip code input through the zip code function
    
    elif line.lower() == "city":    #makes sure user can enter upper or lower case and get same method
      city_name = input("what is the city name?\n")
      state = input("what is the state?\n")
      user_name.weather_city(city_name,state)  #passes both city and state through to the API

    elif line.lower() == "quit":    #exits loop
      break
    
    else:
      print("Error, please enter valid city, zip, or quit")
  print("Done!")
  
  
if __name__ == '__main__':
  main()

  