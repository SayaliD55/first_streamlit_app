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
streamlit.dataframe(my_fruit_list)


