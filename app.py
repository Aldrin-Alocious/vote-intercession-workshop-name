import streamlit as st
if "secretcode" not in st.session_state:
  st.session_state.secretcode=['1JT','XA7','Q5R','R1V','PL8','J6F','MI7','MA5','2EM','LI8']
if "vote" not in st.session_state:
  st.session_state.vote=[]
if "voted" not in st.session_state:
  st.session_state.voted=[]
if "publish" not in st.session_state:
  st.session_state.publish=False
st.title('Intercession Workshop 2023')
tab1, tab2 = st.tabs(["Vote", "Results"])
tab1.subheader("Holy Spirit guide us")
with tab1.form("my_form",clear_on_submit=True):
  pc=st.text_input('Pass code')
  op1=st.radio('Pick one', ['Connect', 'Bridge', 'Kneel', 'Entreaty'])
  if op1=='Connect':
    st.write('Intercession connects us with God. So we are actually connecting God while praying. And the workshop is all about helping people to stay in this connection. "Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I will come in to him, and will sup with him, and he with me." Revelation 3:20')
  elif op1=='Bridge':
    st.write('Intercession is a bridge between those who pray and the God. So those who pray is actually building a bridge to God and there is a two way transportation of information (intentions, messages, grace, etc.) "Your Love is the Bridge, You build with a Cross." The workshop is about teaching them to break all barriers, and build bridges through intercession')
  elif op1=='Kneel':
    st.write('Know Now Eesho Earned Lives. We should pray because we belong to Him.')
  elif op1=='Entreaty':
    st.write('We should entreat to Jesus to stand in prayer life without considering the barriers in it. Entreaty means an earnest or humble request.')
  submitted=st.form_submit_button(label='Submit')
  if submitted:
    for i in range(0,10):
      if pc==st.session_state['secretcode']:
        st.session_state['voted'].append(pc)
        st.session_state['vote'].append(op1)
        st.session_state['secretcode'].remove(pc)
    if pc=='FFF':
      st.session_state['publish']=True
tab2.subheader("Results will be published here")
if st.session_state['publish']==True:
  results=pd.DataFrame()
  results['Passcode']=st.session_state['voted']
  results['Vote']=st.session_state['vote']
  tab1.write(results)
