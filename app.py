import streamlit as st
st.title('Intercession Workshop 2023')
tab1, tab2 = st.tabs(["Vote", "Results"])
tab1.subheader("Holy Spirit guide us")
op1=tab1.radio('Pick one', ['Connect', 'Bridge', 'Kneel', 'Entreaty'])
if op1=='Connect':
  tab1.write('Intercession connects us with God. So we are actually connecting God while praying. And the workshop is all about helping people to stay in this connection./n/"Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I will come in to him, and will sup with him, and he with me./"/nRevelation 3:20')
elif op1=='Bridge':
  tab1.write('Intercession is a bridge between those who pray and the God. So those who pray is actually building a bridge to God and there is a two way transportation of information (intentions, messages, grace, etc.)/n/"Your Love is the Bridge,/nYou build with a Cross./"/n/nThe workshop is about teaching them to break all barriers, and build bridges through intercession')
elif op1=='Kneel':
  tab1.write('Know Now Eesho Earned Lives. We should pray because we belong to Him.')
elif op1=='Entreaty':
  tab1.write('We should entreat to Jesus to stand in prayer life without considering the barriers in it. Entreaty means an earnest or humble request.')
tab2.subheader("Results will be published here")
