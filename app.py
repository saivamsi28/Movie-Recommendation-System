import pickle

import numpy as np
import pandas as pd
import streamlit as st

def recommend(movie):
    # Ensure new_df contains the title column and similarity is a square matrix of appropriate size
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    # Ensure distances is an array
    if isinstance(distances, np.ndarray):
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommend_movies=[]
        for i in movie_list:
            recommend_movies.append(movies.iloc[i[0]].title)
        return recommend_movies
    else:
        print("Error: distances is not an array")

movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

st.title('Movie Recommendor Sysyem')
selected_movie = st.selectbox(
    'Select Your Favourite Movie:',
    movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
