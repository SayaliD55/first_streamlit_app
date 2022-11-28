import streamlit
streamlit.title('My Moms New Healthy dinner')
streamlit.header('breakfast')
streamlit.text('🥣 Omega 3 n blueberry oatmeal')
streamlit.text('🥗 kale, spinach and Rocket smoothie')
streamlit.text('🐔 Hard boil , Free-Range egg')
streamlit.text(' 🥑🍞 Avocado Tost')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(my_fruit_list)


