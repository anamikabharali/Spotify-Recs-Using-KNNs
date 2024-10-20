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

from page0 import page0
from page1 import page1
from page2 import page2


# =================================================================================

# Create a sidebar menu
menu = ["Home", "Get Song Recommendations", "Analyse an Artist"]
choice = st.sidebar.selectbox("Select a page", menu)


# Display the selected page
if choice == "Home":
    st.title("")
    page0()
elif choice == "Get Song Recommendations":
    st.title("Select any of the audio features on the sidebar and the model recommend songs based on those features")
    page1()
else:
    page2()

# ==============================================================
