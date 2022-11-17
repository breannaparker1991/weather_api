#DSC 510
#Week 12
#API weather final
#Author Breanna Parker
#11/7/22

import json
import requests
from env import API_KEY
from urllib.request import urlopen


BACKOFF_TIME = 30

state_codes = {"Alabama":	"AL",	"Nebraska":	"NE", "Alaska":	"AK", "Nevada":	"NV", "Arizona":	"AZ", "New Hampshire":	"NH", "Arkansas":	"AR",	"New Jersey":	"NJ", "California":	"CA",	"New Mexico":	"NM", "Colorado":	"CO",	"New York":	"NY", "Connecticut":	"CT",	"North Carolina":	"NC", "Delaware":	"DE",	"North Dakota":	"ND", "District of Columbia":	"DC",	'Ohio':	'OH', 'Florida':	'FL',	'Oklahoma':	'OK', 'Georgia':	'GA', 	'Oregon':	'OR', 'Hawaii':	'HI',	'Pennsylvania':	'PA', 'Idaho':	'ID', 'Illinois':	'IL',	'Rhode Island':	'RI', 'Indiana':	'IN',	'South Carolina':	'SC', 'Iowa':	'IA',	'South Dakota':	'SD', 'Kansas':	'KS',	'Tennessee':	'TN', 'Kentucky':	'KY',	'Texas':	'TX', 'Louisiana':	'LA',	'Utah':	'UT', 'Maine':	'ME',	'Vermont':	'VT', 'Maryland':	'MD',	'Virginia':	'VA', 'Massachusetts':	'MA',	 'Michigan':	'MI',	'Washington':	'WA', 'Minnesota':	'MN',	'West Virginia':	'WV', 'Mississippi':	'MS',	'Wisconsin':	'WI', 'Missouri':	'MO',	'Wyoming':	'WY', 'Montana':	'MT'}

class openWeather():
  def __init__(self):
    self.appid = "API_KEY"
    self.lat = "lat"
    self.lon = "lon"
  
  def lat_lon(self,response):
    try:
      url_lat_lon = f'http://api.openweathermap.org/data/2.5/weather?lat={response["lat"]}&lon={response["lon"]}&&appid={API_KEY}' #uses previous data from dictionary to input into api url
      response2 = requests.get(url_lat_lon).json() #runs api and gets results
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
        print("Pressure:", response2["main"]["pressure"], "pa")
        print("Sky:", response2["weather"][0]["description"])
    # elif temp_quest.lower() == 'f':
    #     self.k_to_f(temp_dict)
    # elif temp_quest.lower() == 'k':
    #   for word in sorted(temps, key = temps.get):         
    #     print (word, temps[word])
    except:
        print("Error, city, state or zip code was incorrect") 
    else:
      print("Connection to lat/long API was succesful!")
    
  
  def weather_city(self,city_name,state):
    try:
      url_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state},us&limit=1&appid={API_KEY}'     #used f string to bring input values directly into url
      res = requests.get(url_city).json()  #runs api code and results
      response = {}      #makes sure code is in a dictionary for easy use in next code
      for r in res:     #adds all data to dictionary
        response.update(r)
      self.lat_lon(response)      #uses dictionary data in next function
    except TypeError:
      print("A Type Error occured!!")
    else:
      print("Connection to city/state API was succesful!")
  
  def weather_zip(self,zip_code):
    try:
      url_zip = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},us&appid={API_KEY}'  #used f string to bring input values directly into url
      response = requests.get(url_zip).json()  #run api code and results
      self.lat_lon(response) #this set of code is already in a dictionary so can be pushed directly into the next function
    
    except:
      print("Error, pick a valid zip code!")
    else:
      print("Connection to zip code API was succesful!")


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
    print("Pressure:", response2["main"]["pressure"], "pa")
    print("Humdity:", response2["main"]["humidity"], "%")
    print("Sky:", response2["weather"][0]["description"])
    
    
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
    print("Pressure:", response2["main"]["pressure"], "pa")
    print("Humdity:", response2["main"]["humidity"], "%")
    print("Sky:", response2["weather"][0]["description"])
    
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
      try:
        check = int(zip_code)
      except ValueError:
        print("This is not a number. Please enter a valid number")
      if len(zip_code) != 5: 
        print("please enter a 5 character zip code")
      else:
        user_name.weather_zip(zip_code)     #passes zip code input through the zip code function with the API
    
    elif line.lower() == "city":    #makes sure user can enter upper or lower case and get same method
      city_name = input("what is the city name?\n")
      state = input("what is the two character state code?\n")
      if len(state) != 2:
        print("incorrect state code length")
        for k, v in sorted(state_codes.items()):    #prints list of states in case user isn't sure what to use
          print(k, v)
      user_name.weather_city(city_name,state)  #passes both city and state through to the city function with the API

    elif line.lower() == "quit":    #exits loop
      break
    
    else:
      print("Error, please enter valid city, zip, or quit")
  print("Done!")
  
  
if __name__ == '__main__':
  main()

