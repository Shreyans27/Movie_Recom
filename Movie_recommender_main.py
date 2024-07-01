import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests
# from streamlit_option_menu import option_menu

# import Movie_recommender

st.set_page_config(
    page_title = "Home",
    )

st.title("Movie Recommender System")
# st.sidebar.success("Select a page above")

# class Multiapp:
#     def __init__(self):
#          self.apps = []
#     def add_app(self,title,function):
#         self.apps.append({
#             "title":title,
#             "function":function
#             }
#         )
#     def run():
#         with st.sidebar:
#             app = option_menu(
#                 menu_title='Home',
#                 options = ['Recommender','Genre'])
            
#         if app == 'Home':
#             Movie_recommender.app()
        
#     run()

def get_poster(movie_id):
    #https://www.themoviedb.org/settings/api
    #https://developer.themoviedb.org/reference/movie-details
    url = "https://api.themoviedb.org/3/movie/"+str(movie_id)+"?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Y2FiY2JmMGZlZTdhMjM5N2QxOTk2YzI4NjAwNTQ3MyIsIm5iZiI6MTcxOTY2NzUxOS42Mjk2OTQsInN1YiI6IjY2ODAwNTE3ZGQ2MzhhZjY5NzY3ZGM5NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WzfH6LYzSqAGO980ayLCBBcfm4XQZa1YVDoU3O5xXdY"
    }
    response = requests.get(url, headers=headers)
    result = response.json().get("poster_path")
    result = "https://image.tmdb.org/t/p/w185" + result
    #print(result)
    return result

top_movies = pickle.load(open('top_movies.pkl','rb'))
top_movies_list = top_movies['title'].values
top_movies_id = top_movies['id'].values

st.header('Top Movies', divider='rainbow')   

row1 = st.columns(2)
row2 = st.columns(2)
row3 = st.columns(2)

count = 0
for col in row1+row2+row3:
    tile = col.container(height=300)
    tile.write(top_movies_list[count])
    image_path = get_poster(top_movies_id[count])
    tile.image(image_path)
    count += 1