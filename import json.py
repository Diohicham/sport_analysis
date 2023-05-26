import json
import urllib.request
import pandas as pd
import numpy as np
from pygal.maps.world import World

# with open("data.json", "r") as infile:
#   data = json.load(infile)

url = 'https://restcountries.com/v3.1/all'
request = urllib.request.urlopen(url)
data = json.loads(request.read())

countries= []
info = []
pop_dict = {}

for item in data:
  for key, value in item.items():
    if key == "name":
      #print(f"{key}: "+ value["common"])
      
      countries.append(value["common"])
    # if key == "capital":
    #   #print(value[0])
    #   info.append(value[0])
      
    if key == "population":
      #print(value)
      
        info.append(value)
    for country in countries:
      for x in info:
        pop_dict[country] = x
        
      info.clear()
  countries.clear()      

with open("population.json", "w") as outfile:
  json.dump(pop_dict, outfile)

'''==========================Block for the Transfomation for PYGAL=========================='''

#imported the countries code from the World map country code map
df_country = pd.read_csv('Country_code_list.csv')

#transformed it into a dictionary
code_dict = df_country.set_index('Country').to_dict()['code']

#code to inner join the dictionnary by Country
#only matching key of countries are added to the dicitionary
new_dict = {}
for pop_key, pop_value in pop_dict.items():
  for code_key, code_value in code_dict.items():
    if pop_key == code_key:
      new_dict[code_value] = pop_value

with open("country_population.json", "w") as outfile:
  json.dump(new_dict, outfile)

#Create a World map chart
worldmap_chart = World()

# Add the data to the chart
worldmap_chart.title = 'Countries by population'

# Add the data to chart
worldmap_chart.add(' 2019 year', new_dict)

# Customize the chart
worldmap_chart.legend_at_bottom = True
worldmap_chart.legend_box_size = 20

#Render the chart as an SVG image
worldmap_chart.render_to_file("Rest_Countries_population.svg")

user_input = str(input("What country would you like to know the population of?\n")).title()

for key, value in pop_dict.items():
  if key == user_input:
    print(f"The population of {key} is {value} people")
'''======================================================================================================'''
countries= []
info = []
curr_dict = {}

for item in data:
  for key, value in item.items():
    if key == "name":
      countries.append(value["common"])
      
    if key == "currencies":
      for curr_symbol, curr_name in value.items():
        #print(curr_symbol, "  ", curr_name["name"])
        info.append(curr_name["name"])
    
    #Create new dictionary with the necessary info
    for country in countries:
      for x in info:
        curr_dict[country] = x
        
      info.clear()
  countries.clear()


with open("currencies.json", "w") as outfile:
  json.dump(curr_dict, outfile)


'''==========================Block for the Transfomation for PYGAL=========================='''

#imported the countries code from the World map country code map
df_country = pd.read_csv('Country_code_list.csv')

#transformed it into a dictionary
code_dict = df_country.set_index('Country').to_dict()['code']

#code to inner join the dictionnary by Country
#only matching key of countries are added to the dicitionary
new_dict_2 = {}
for curr_key, curr_value in curr_dict.items():
  for code_key, code_value in code_dict.items():
    if curr_key == code_key:
      new_dict_2[code_value] = curr_value

with open("country_currencies.json", "w") as outfile:
  json.dump(new_dict_2, outfile)



for dict_key, dict_value in new_dict_2:
  print(dict_value,[dict_key])

# "=========================================="

# #Create a World map chart
# worldmap_chart_2 = World()

# # Add the data to the chart
# worldmap_chart_2.title = 'Currency of countries'

# worldmap_chart_2.tooltip_font_size = 14
# worldmap_chart_2.tooltip_border_radius = 10
# # Add the data to chart lambda argument x , return a list 
# #https://stackoverflow.com/questions/74701228/how-do-i-display-text-in-a-pygal-map


# worldmap_chart_2.add('Currencies', new_dict)
# # adding the countries

# # Customize the chart
# worldmap_chart_2.legend_at_bottom = True
# worldmap_chart_2.legend_box_size = 20

# #Render the chart as an SVG image
# worldmap_chart_2.render_to_file("Countries_currency.svg")

# # user_input = str(input("What country currency would you like to know?\n")).title()

# # for key, value in curr_dict.items():
# #   if key == user_input:
# #     print(f"The currency of {key} is {value}")


# '''======================================================================================================'''