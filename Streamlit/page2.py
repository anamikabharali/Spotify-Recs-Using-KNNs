
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

def page2():

    # authenticate to spotify      
    client_id = "73d8939b2df341b49308c2705babd9e8"
    client_secret = "0fac4b5ca15942c5ad44d57bbb37524d"
    REDIRECT_URI = "http://localhost:8001"
    scope = "user-library-read"


    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,client_secret,REDIRECT_URI,scope=scope))

    dua_lipa_id = '37i9dQZF1DX3fRquEp6m8D'
    hans_zimmer_id = '37i9dQZF1DWWF3yivn1m3D'

    id = dua_lipa_id

    # Add GIF
    if id == dua_lipa_id:
        st.image("dua_lipa.gif", use_column_width=True)
    else :
        st.image("hans_zimmer.gif", use_column_width=True)

    # Get playlist data
    playlist = sp.playlist(id)


    # Get track data
    tracks = playlist['tracks']['items']

    # Initialize DataFrame
    df_artist = pd.DataFrame(columns=["id","artist", "title", "album", "danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "type", "duration_ms", "time_signature"])
    # df_artist = pd.DataFrame(columns=["id","artist"])

    # Loop through tracks and get features
    for track in tracks:
        # Get track ID
        track_id = track['track']['id']
        
        artist = track['track']['artists'][0]['name']
        title = track['track']['name']
        album = track['track']['album']['name']

        # Get track features
        features = sp.audio_features(track_id)[0]

        # Append data to DataFrame
        df_artist = df_artist.append({
            "id": features["id"],
            "artist": artist,
            "title": title,
            "album": album,
            "danceability": features["danceability"],
            "energy": features["energy"],
            "key": features["key"],
            "loudness": features["loudness"],
            "mode": features["mode"],
            "speechiness": features["speechiness"],
            "acousticness": features["acousticness"],
            "instrumentalness": features["instrumentalness"],
            "liveness": features["liveness"],
            "valence": features["valence"],
            "tempo": features["tempo"],
            "type": features["type"],
            "duration_ms": features["duration_ms"],
            "time_signature": features["time_signature"]
        }, ignore_index=True)

    # st.table(df_artist.head())

    # Get a list of column names to exclude from the dropdown
    exclude_cols = ["id", "artist", "title", "album", "type"]

    # Create a list of column names to include in the dropdown
    include_cols = [col for col in df_artist.columns if col not in exclude_cols]

    # Create a dropdown to select the column to compare
    final_column = st.selectbox("Select a column to compare:",include_cols)

    # Create a plotly figure
    fig = px.line(df_artist, x=df_artist.index, y=final_column)

    # Show the plotly figure using st.plotly_chart
    st.plotly_chart(fig)

    st.header("Mean value : ")
    mean_value = df_artist.mean()
    st.table(mean_value)