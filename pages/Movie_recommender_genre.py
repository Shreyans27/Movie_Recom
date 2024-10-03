import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests


top_movies = pickle.load(open('top_movies.pkl','rb'))
top_movies_list = top_movies['title'].values
top_movies_id = top_movies['id'].values

top_movies['genres'] = top_movies['genres'].apply(' '.join)
genres = top_movies['genres'].values

genre_main = {}
genre_main_list = []
for i in genres:
    temp = i.split()
    for j in temp:
        if j in genre_main:
            genre_main[j] += 1
        else:
            genre_main[j] = 1
            genre_main_list.append(j)
            
            
def get_poster(movie_id):
    #https://www.themoviedb.org/settings/api
    #https://developer.themoviedb.org/reference/movie-details
    url = "https://api.themoviedb.org/3/movie/"+str(movie_id)+"?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Your_API_KEY_Here"
    }
    response = requests.get(url, headers=headers)
    result = response.json().get("poster_path")
    result = "https://image.tmdb.org/t/p/w185" + result
    #print(result)
    return result            

def recommend_content(genre,same = 10):
    movie_index = top_movies[top_movies['genres'].apply(lambda x: genre in x)]['id'].values[0:same]
    movie_arr = top_movies[top_movies['genres'].apply(lambda x: genre in x)]['title'].values[0:same]
    poster_arr = []
    for i in movie_index:
        poster = get_poster(i)
        poster_arr.append(poster)
    return movie_arr, poster_arr

genre_main_list.sort()
st.header('Genres', divider='rainbow')  

option = st.selectbox("Type in your genre", genre_main_list,index=None,placeholder="Type Genre...",)
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
