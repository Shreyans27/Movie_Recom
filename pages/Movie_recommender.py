# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:42:35 2024

@author: shahs
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests


top_movies = pickle.load(open('top_movies.pkl','rb'))
top_movies_list = top_movies['title'].values
top_movies_id = top_movies['id'].values

recommend_movies = pickle.load(open('recommend_movies.pkl','rb'))
movies_options = recommend_movies['title'].values

cosine_output = pickle.load(open('cosine_output.pkl','rb'))

def app():
    st.write("test")

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
    
get_poster(19995)

def recommend_content(name,same = 10):
    movie_index = recommend_movies[recommend_movies['title'] == name].index[0]
    distance = cosine_output[movie_index]
    final = sorted(enumerate(distance), reverse = True, key=lambda x: x[1])[1:same+1]
    movie_arr = []
    poster_arr = []
    for i in final:
        movie_id = recommend_movies.iloc[i[0]].id
        poster = get_poster(movie_id)
        poster_arr.append(poster)
        movie_arr.append(recommend_movies.iloc[i[0]].title)
    return movie_arr, poster_arr


st.title("Movie Recommender System")



st.header('Recommend Movies', divider='rainbow')  

option = st.selectbox("Type in your movie", movies_options,index=None,placeholder="Type Movie...",)
st.write("You selected:", option)


if st.button("Recommend"):
    movie_array = []
    movie_array,poster_arr = recommend_content(option)
    
    r1 = st.columns(2)
    r2 = st.columns(2)
    r3 = st.columns(2)
    r4 = st.columns(2)
    r5 = st.columns(2)
    
    count = 0
    for col in r1+r2+r3+r4+r5:
        tile = col.container(height=300)
        tile.write(movie_array[count])
        tile.image(poster_arr[count])
        count += 1
    