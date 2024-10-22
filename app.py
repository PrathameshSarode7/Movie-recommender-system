<<<<<<< Updated upstream
import streamlit as st
import pickle
import pandas as pd
import requests
import base64

st.set_page_config(layout="wide")


# Function to fetch movie posters from TMDB
def get_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=enter youru api key &language=en-US')
    data = response.json()

    # Check if 'poster_path' exists and is not None
    if data.get("poster_path"):
        return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]
    else:
        # Return a placeholder image URL if poster_path is not available
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"


# Recommender function
def recommender(movie):
    movie_index = movies_tmdb[movies_tmdb['title'] == movie].index[0]
    distances = cosine_sim[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies_tmdb.iloc[i[0]].movie_id
        recommended_movies.append(movies_tmdb.iloc[i[0]].title)
        recommended_posters.append(get_poster(movie_id))
    return recommended_movies, recommended_posters


# Load pre-trained data
movies_tmdb = pd.DataFrame(pickle.load(open('movies_tmdb.pkl', 'rb')))
cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))


# Add a stylish background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 0.8; /* Transparency effect */
        }}
        .title {{
            color: #ff6347;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
        }}
        .recommendation {{
            color: #f0f0f0;
            font-family: 'Arial', sans-serif;
            font-size: 1.2rem;
            text-align: center;
            margin-top: 15px;
        }}
        .movie-poster:hover {{
            transform: scale(1.05);
            transition: 0.3s;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Set the background image
add_bg_from_local("arrangement-cinema-elements-red-background-with-copy-space.jpg")

# App title with custom font and color
st.markdown('<h1 class="title">Movie Recommender System</h1>', unsafe_allow_html=True)

# Movie selection dropdown
movie_selected = st.selectbox(
    'Choose a movie you want recommendations on',
    movies_tmdb['title'].values)

if st.button("Recommend"):
    with st.spinner('Fetching recommendations...'):
        recommendations, posters = recommender(movie_selected)

    # Determine how many recommendations were returned
    num_recommendations = len(recommendations)

    # Adjust the number of columns based on the number of recommendations
    cols = st.columns(min(5, num_recommendations))

    # Iterate through the first 5 recommendations or less
    for i in range(min(5, num_recommendations)):
        with cols[i]:
            st.markdown(f'<p class="recommendation">{recommendations[i]}</p>', unsafe_allow_html=True)
            st.image(posters[i], width=200, caption=recommendations[i], use_column_width=True)

    # If there are more than 5 recommendations, display them in a new row
    if num_recommendations > 5:
        cols2 = st.columns(min(5, num_recommendations - 5))

        # Iterate through the remaining recommendations (if any)
        for i in range(min(5, num_recommendations - 5)):  # Adjust loop range to avoid index errors
            with cols2[i]:
                st.markdown(f'<p class="recommendation">{recommendations[i + 5]}</p>', unsafe_allow_html=True)
                st.image(posters[i + 5], width=200, caption=recommendations[i + 5], use_column_width=True)
=======
import streamlit as st
import pickle
import pandas as pd
import requests
import base64

st.set_page_config(layout="wide")


# Function to fetch movie posters from TMDB
def get_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=enter youru api key &language=en-US')
    data = response.json()

    # Check if 'poster_path' exists and is not None
    if data.get("poster_path"):
        return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]
    else:
        # Return a placeholder image URL if poster_path is not available
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"


# Recommender function
def recommender(movie):
    movie_index = movies_tmdb[movies_tmdb['title'] == movie].index[0]
    distances = cosine_sim[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies_tmdb.iloc[i[0]].movie_id
        recommended_movies.append(movies_tmdb.iloc[i[0]].title)
        recommended_posters.append(get_poster(movie_id))
    return recommended_movies, recommended_posters


# Load pre-trained data
movies_tmdb = pd.DataFrame(pickle.load(open('movies_tmdb.pkl', 'rb')))
cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))


# Add a stylish background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 0.8; /* Transparency effect */
        }}
        .title {{
            color: #ff6347;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
        }}
        .recommendation {{
            color: #f0f0f0;
            font-family: 'Arial', sans-serif;
            font-size: 1.2rem;
            text-align: center;
            margin-top: 15px;
        }}
        .movie-poster:hover {{
            transform: scale(1.05);
            transition: 0.3s;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Set the background image
add_bg_from_local("arrangement-cinema-elements-red-background-with-copy-space.jpg")

# App title with custom font and color
st.markdown('<h1 class="title">Movie Recommender System</h1>', unsafe_allow_html=True)

# Movie selection dropdown
movie_selected = st.selectbox(
    'Choose a movie you want recommendations on',
    movies_tmdb['title'].values)

if st.button("Recommend"):
    with st.spinner('Fetching recommendations...'):
        recommendations, posters = recommender(movie_selected)

    # Determine how many recommendations were returned
    num_recommendations = len(recommendations)

    # Adjust the number of columns based on the number of recommendations
    cols = st.columns(min(5, num_recommendations))

    # Iterate through the first 5 recommendations or less
    for i in range(min(5, num_recommendations)):
        with cols[i]:
            st.markdown(f'<p class="recommendation">{recommendations[i]}</p>', unsafe_allow_html=True)
            st.image(posters[i], width=200, caption=recommendations[i], use_column_width=True)

    # If there are more than 5 recommendations, display them in a new row
    if num_recommendations > 5:
        cols2 = st.columns(min(5, num_recommendations - 5))

        # Iterate through the remaining recommendations (if any)
        for i in range(min(5, num_recommendations - 5)):  # Adjust loop range to avoid index errors
            with cols2[i]:
                st.markdown(f'<p class="recommendation">{recommendations[i + 5]}</p>', unsafe_allow_html=True)
                st.image(posters[i + 5], width=200, caption=recommendations[i + 5], use_column_width=True)
>>>>>>> Stashed changes
