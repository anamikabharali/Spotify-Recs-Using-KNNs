import streamlit as st

def page0():

    st.header(" Spotify provides a set of audio features that are computed for each track in their database.\n\n\n")

    st.write("\nDanceability: This feature describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength. The values range from 0 to 1, with higher values indicating higher danceability. \n\n\n")

    st.write("\nEnergy: This feature measures the intensity and activity level of a track. It includes elements such as loudness, timbre, and the amount of noise in the recording. The values range from 0 to 1, with higher values indicating higher energy. \n\n\n")

    st.write("\nLoudness: This feature represents the overall volume of a track in decibels (dB) and ranges from -60 dB to 0 dB. It is calculated by taking the average amplitude of the waveform and converting it to decibels using a logarithmic scale. \n\n\n")

    st.write("\nSpeechiness: This feature measures the presence of spoken words in a track. Values range from 0 to 1, with higher values indicating a greater presence of spoken words. Values closer to 1 represent tracks that are mostly spoken word (e.g. audiobooks or podcasts), while values closer to 0 represent instrumental or purely musical tracks. \n\n\n")

    st.write("\nAcousticness: This feature measures the degree to which a track is acoustic (i.e. not electronic). It is represented on a scale from 0 to 1, with higher values indicating greater acousticness. \n\n\n")

    st.write("\nInstrumentalness: This feature measures the degree to which a track contains no vocals or other non-instrumental sounds. It ranges from 0 to 1, with higher values indicating greater instrumentalness. \n\n\n")

    st.write("\nValence: This feature measures the musical positiveness conveyed by a track. It ranges from 0 to 1, with higher values indicating more positive, happy, or euphoric feelings. \n\n\n")

    st.write("\nTempo: This feature measures the overall tempo or speed of a track, represented in beats per minute (BPM). \n\n\n")

    st.write("\nKey: This feature identifies the key in which a track is performed. It is represented as a value between 0 and 11, with each value representing a different key (e.g. 0 represents C, 1 represents C#, 2 represents D, and so on). \n\n\n")

    st.write("\nMode: This feature indicates the modality (major or minor) of a track, represented as either 0 (minor) or 1 (major). \n\n\n")