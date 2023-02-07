import streamlit as st
tab1, tab2 = st.tabs(["Internal Trade", "Communication Services"])
tab1.write("Internal Trade")
op1=st.selectbox('Pick one', ['Whole Sale Trade', 'Retail Trade'])
if op1=='Whole Sale Trade':
  tab1.image()
tab2.write("Communication Services")
