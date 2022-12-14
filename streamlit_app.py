import streamlit as sl
import pandas as pd 

sl.title('My Parents New Healthy Diner')

sl.header('Breakfast Menu')
sl.text('🥣Omega 3 & Blueberry Oatmeal')
sl.text('🥗Kale, Spinach & Rocket Smoothie')
sl.text('🐔 Hard-boiled Free-Range Egg')
sl.text('🥑🍞Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = sl.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
sl.dataframe(fruits_to_show)

sl.header("Fruityvice Fruit Advice!")
fruit_choice = sl.text_input('What fruit would you like information about?','Kiwi')
sl.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")


# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
sl.dataframe(fruityvice_normalized)
