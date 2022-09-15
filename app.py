import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(st.file_uploader('Upload a CSV'))
st.dataframe(df)
