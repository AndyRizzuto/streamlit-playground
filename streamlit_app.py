import streamlit as st
import pandas as pd
import numpy as np

st.title('My Health Metrics')

df = pd.DataFrame({
    'date': ["1/1/2023","1/3/2023","1/9/2023"],
    'weight': [165,168,168.5]
})

st.write(df)