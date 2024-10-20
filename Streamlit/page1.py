import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LogisticRegression
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import csv
import requests
import plotly.express as px


def page1():

    st.write("")
    st.write("")
    st.write("")

    # Load dataset
    df = pd.read_csv("Big_dataset_tracks.csv")

    # Define audio features
    features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'speechiness', 'valence', 'tempo']

    # Create an empty list to store selected features
    selected_features = []
    track_info = ['artist','title', 'id']
    nrows = 1

    # Create a checkbox for each feature and store the selected ones
    for feature in features:
        if st.sidebar.checkbox(feature):
            selected_features.append(feature)

    st.header("Number of tracks to consider : ")
    nrows = st.selectbox("", options=list(range(1,11)), index=4)        


    # Display the selected features as a list
    if not selected_features:
        st.warning("Please select at least one feature.")

    # Display the selected features as a list
    elif not nrows:
        st.warning("Please select number of songs you wish to choose from your 'Liked Songs' ")
        # Create a dropdown menu for the number of rows to display in the sidebar
        nrows = st.selectbox("Select the number of rows to display:", options=list(range(1,11)), index=4)
        st.write("Selected features : ", selected_features)
        

    # Define the path to the My_Liked_songs CSV file
    csv_path = "My_liked_songs_with_features.csv"

    # Read the first 5 rows of the CSV file and extract the specified columns
    df2 = pd.read_csv(csv_path, usecols=selected_features, nrows=nrows)
    df3 = pd.read_csv(csv_path, usecols=track_info + selected_features, nrows=nrows)
    df4 = pd.read_csv(csv_path, usecols=track_info, nrows=nrows)


    # customize the appearance of the table using CSS
    st.header("Spotify Track : ")
    st.table(df3)

    # Convert the DataFrame to an array
    features_array = df2.values

    def knn_model(input_song):

        # input_song_selected_features = df.loc[:, [selected_features]]
        # st.write(input_song_selected_features)

        scaler = StandardScaler()
        X = scaler.fit_transform(df[selected_features])

        # Normalize the input song
        X_input = scaler.transform([input_song])

        # Train the KNN model
        k = 2
        knn = KNeighborsRegressor(n_neighbors=k, metric='euclidean')
        knn.fit(X, df['title'])
    
        # Find the k-nearest neighbors
        distances, indices = knn.kneighbors(X_input)

        # Recommend songs based on the k-nearest neighbors
        # recommended_songs = df.loc[indices[0], ['name', 'artists_name', 'id']]
        recommended_songs = df.loc[indices[0]]
        recommended_songs['Distance'] = distances[0]
        selected_cols = ['title', 'artist', 'id', 'Distance']

        # Display recommended_songs in a table
        st.header("Recommended Songs - ")
        st.table(recommended_songs[selected_cols + selected_features])

        # Plot KNN distances of recommended songs with song index
        fig, ax = plt.subplots()
        ax.bar(np.arange(len(recommended_songs)), distances[0])
        ax.set_xticks(np.arange(len(recommended_songs)))
        ax.set_xticklabels(recommended_songs.index)
        ax.set_xlabel('Song Index')
        ax.set_ylabel('Distance from Input Song')
        ax.set_title('KNN Distance of Recommended Songs')
        st.pyplot(fig)    

        st.write("")
        st.write("")
        st.write("")


        # just a bar plot of each audio feature of the recommend song.

        # for i in range(len(recommended_songs)):
        #     song = recommended_songs.iloc[i]
        #     fig, ax = plt.subplots()
        #     ax.bar(selected_features, song[selected_features])
        #     ax.set_title(song['name'])
        #     st.pyplot(fig)


    input_song = []
    for row in features_array:
        input_song = row.tolist()
        knn_model(input_song)
