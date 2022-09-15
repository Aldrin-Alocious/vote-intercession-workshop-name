import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.image("SCT-LOGO.jpg")
st.title("\t\t\tPOOL LAB")
df=st.dataframe(st.file_uploader('Upload a CSV'))
st.dataframe(df)
