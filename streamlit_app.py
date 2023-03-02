import streamlit as st
import pandas as pd
import numpy as np
from pydataset import data


def pydata():
    # Pydataset controls
    selected_data = st.sidebar.selectbox('Select a dataset', data().dataset_id)
    title_data = data()[ data()['dataset_id'] == selected_data]['title']

    st.header('Datasets')
    st.subheader('List of dataset')
    with st.expander('Show list of dataset'):
        st.write(data())

    st.subheader(f'Selected data (`{selected_data}`)')
    st.info(title_data)
    st.write(data(selected_data))
    return

st.title('My Health Metrics')
st.sidebar.text_input("Your name", key="name")
greeting = "Hello "+ st.session_state.name
st.write(greeting)

#df =load_apple_health()
pydata()

# References
# https://towardsdatascience.com/analyse-your-health-with-python-and-apple-health-11c12894aae2
# https://github.com/dataprofessor/pydataset/
# https://blog.streamlit.io/streamlit-firestore/