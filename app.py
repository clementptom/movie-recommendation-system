from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import streamlit as st
import pickle
import requests

movie = pickle.load(open('movies.pkl', 'rb'))
movies_list = movie['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(layout="wide")

def recommend(film):
    mov_index = movie[movie['title'] == film].index[0]
    distance = similarity[mov_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x:x[1])[1:31]
    
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        recommended_movies.append(movie['title'][i[0]])
        recommended_movies_posters.append(get_poster(movie['movie_id'][i[0]]))

    return recommended_movies, recommended_movies_posters

def get_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b32c6e535c509e0b5377c0a05f330c0b'.format(movie_id))
    data = response.json()
    path = "https://image.tmdb.org/t/p/original" + data['poster_path']

    return path

import streamlit as st
st.markdown("<h1 style='text-align: center; color: red;'>Movie Recommendation System</h1>", unsafe_allow_html=True)


option = st.selectbox('MOVIE NAME',(movies_list))


coll1, coll2, coll3, coll4, coll5, coll6, coll7, coll8, coll9, coll10, coll11 = st.columns(11)        
if coll6.button('Recommend'):
    name, posters = recommend(option)

    st.subheader('What to watch: ')

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

    with col1:
        st.text(name[0])
        st.image(posters[0])

        st.text(name[10])
        st.image(posters[10])

        st.text(name[20])
        st.image(posters[20])

    with col2:
        st.text(name[1])
        st.image(posters[1])

        st.text(name[11])
        st.image(posters[11])

        st.text(name[21])
        st.image(posters[21])

    with col3:
        st.text(name[2])
        st.image(posters[2])

        st.text(name[12])
        st.image(posters[12])

        st.text(name[22])
        st.image(posters[22])

    with col4:
        st.text(name[3])
        st.image(posters[3])

        st.text(name[13])
        st.image(posters[13])

        st.text(name[23])
        st.image(posters[23])

    with col5:
        st.text(name[4])
        st.image(posters[4])

        st.text(name[14])
        st.image(posters[14])

        st.text(name[24])
        st.image(posters[24])

    with col6:
        st.text(name[5])
        st.image(posters[5])
        
        st.text(name[15])
        st.image(posters[15])

        st.text(name[25])
        st.image(posters[25])

    with col7:
        st.text(name[6])
        st.image(posters[6])

        st.text(name[16])
        st.image(posters[16])

        st.text(name[26])
        st.image(posters[26])

    with col8:
        st.text(name[7])
        st.image(posters[7])

        st.text(name[17])
        st.image(posters[17])

        st.text(name[27])
        st.image(posters[27])

    with col9:
        st.text(name[8])
        st.image(posters[8])

        st.text(name[18])
        st.image(posters[18])

        st.text(name[28])
        st.image(posters[28])

    with col10:
        st.text(name[9])
        st.image(posters[9])

        st.text(name[19])
        st.image(posters[19])
        
        st.text(name[29])
        st.image(posters[29])