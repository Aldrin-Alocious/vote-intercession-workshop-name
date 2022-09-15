import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.file_uploader('Upload a CSV')
df=pd.read_csv("et lab report.csv")
st.dataframe(df)
