import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.image("SCT-LOGO.jpg")
st.title("POOL LAB")
df=pd.read_csv(st.file_uploader('Upload a CSV'))
dfz=df;
g=dfz[['Unnamed: 8']]
g=g.to_numpy()
g=np.array(g,ndmin=2)
for i in range(1,np.size(g)):
  if g[i]=='Yes':
    dfz.drop([i])
st.dataframe(df)
st.dataframe(dfz)
AN=df[['Unnamed: 3']]
CT=df[['Unnamed: 4']]
AN=AN.to_numpy()
CT=CT.to_numpy()
nAI=0;nCS=0;nEC=0;nME=0;nMA=0;nBT=0;nCL=0;
AIE=[];CSE=[];ECE=[];MEE=[];MAE=[];BTE=[];CLE=[];
for i in range(1,np.size(AN)):
  if CT[i,0]=='Artificial Intelligence And Machine Learning':
    nAI=nAI+1
    AIE.append(AN[i,0])
  elif CT[i,0]=='Computer Science':
    nCS=nCS+1
    CSE.append(AN[i,0])
  elif CT[i,0]=='Electronics and Communication':
    nEC=nEC+1
    ECE.append(AN[i,0])
  elif CT[i,0]=='Mechanical':
    nME=nME+1
    MEE.append(AN[i,0])
  elif CT[i,0]=='Mechanical Automobile':
    nMA=nMA+1
    MAE.append(AN[i,0])
  elif CT[i,0]=='Biotechnology':
    nBT=nBT+1
    BTE.append(AN[i,0])
  elif CT[i,0]=='Civil':
    nCL=nCL+1
    CLE.append(AN[i,0])
nos=np.array([nAI,nCS,nEC,nME,nMA,nBT,nCL])
dep=np.array(['Artificial Intelligence And Machine Learning','Computer Science','Electronics and Communication','Mechanical','Mechanical Automobile','Biotechnology','Civil'])
fig1, ax1 = plt.subplots()
ax1.pie(nos, labels=dep, autopct='%1.1f%%')
ax1.axis('equal')
st.header("Admissions this year")
st.pyplot(fig1)
st.write('Artificial Intelligence And Machine Learning\t- ',nAI)
st.write('Computer Science\t\t\t\t- ',nCS)
st.write('Electronics and Communication\t\t\t- ',nEC)
st.write('Mechanical\t\t\t\t\t- ',nME)
st.write('Mechanical Automobile\t\t\t\t- ',nMA)
st.write('Biotechnology\t\t\t\t\t- ',nBT)
st.write('Civil\t\t\t\t\t\t- ',nCL)
AIE=np.array(AIE,ndmin=2)
CSE=np.array(CSE,ndmin=2)
ECE=np.array(ECE,ndmin=2)
MEE=np.array(MEE,ndmin=2)
MAE=np.array(MAE,ndmin=2)
BTE=np.array(BTE,ndmin=2)
CLE=np.array(CLE,ndmin=2)
def departments(a,b,d):
  c=pd.DataFrame()
  c=c.append(df.loc[0], ignore_index=False, verify_integrity=False, sort=None)
  for i in range(0,np.size(b)):
    for j in range(1,np.size(a)):
      if b[0,i]==a[j,0]:
        c=c.append(df.loc[j], ignore_index=False, verify_integrity=False, sort=None)
        break
  return c
AI=departments(AN,AIE,df)
CS=departments(AN,CSE,df)
EC=departments(AN,ECE,df)
ME=departments(AN,MEE,df)
MA=departments(AN,MAE,df)
BT=departments(AN,BTE,df)
CL=departments(AN,CLE,df)
def seats(d):
  AT=d[['Unnamed: 6']]
  AT=AT.to_numpy()
  m=0;mq=0;nri=0;tfw=0;
  for i in range(1,np.size(AT)):
    if AT[i]=='Merit':
      m=m+1
    elif AT[i]=='Management Quota':
      mq=mq+1
    elif AT[i]=='NRI':
      nri=nri+1
    elif AT[i]=='TFW-Merit':
      tfw=tfw+1
  snos=np.array([m,mq,nri,tfw])
  return snos
def vacancies(d):
  AD=d[['Unnamed: 8']]
  AD=AD.to_numpy()
  AT=d[['Unnamed: 6']]
  AT=AT.to_numpy()
  vm=0;vmq=0;vnri=0;vtfw=0;
  for i in range(1,np.size(AD)):
    if AD[i]=='No':
      if AT[i]=='Merit':
       vm=vm+1
      elif AT[i]=='Management Quota':
       vmq=vmq+1
      elif AT[i]=='NRI':
       vnri=vnri
      elif AT[i]=='TFW-Merit':
       vtfw=vtfw
  vsnos=np.array([vm,vmq,vnri,vtfw])
  return vsnos
def vslashs(a,b):
  c=[];
  for i in range(0,np.size(a)):
    c.append(str(a[i])+" out of "+str(b[i]))
  return c
vdf=pd.DataFrame()
vdf['']=['Merit','Management Quota','NRI','TFW-Merit']
seat1=seats(AI)
vac1=vacancies(AI)
vdf['Artificial Intelligence']=vslashs(vac1,seat1)
seat2=seats(CS)
vac2=vacancies(CS)
vdf['Computer Science']=vslashs(vac2,seat2)
seat3=seats(EC)
vac3=vacancies(EC)
vdf['Electronics and Communication']=vslashs(vac3,seat3)
seat4=seats(ME)
vac4=vacancies(ME)
vdf['Mechanical Engineering']=vslashs(vac4,seat4)
seat5=seats(MA)
vac5=vacancies(MA)
vdf['Automobile Engineering']=vslashs(vac5,seat5)
seat6=seats(BT)
vac6=vacancies(BT)
vdf['Biotechnology']=vslashs(vac6,seat6)
seat7=seats(CL)
vac7=vacancies(CL)
vdf['Civil Engineering']=vslashs(vac7,seat7)
st.header("Vacancies and Seats")
st.dataframe(vdf)
options=[];
if vac1[0]>0:
  options.append('AI-SM')
if vac1[1]>0:
  options.append('AI-MG')
if vac2[0]>0:
  options.append('CS-SM')
if vac2[1]>0:
  options.append('CS-MG')
if vac3[0]>0:
  options.append('EC-SM')
if vac3[1]>0:
  options.append('EC-MG')
if vac4[0]>0:
  options.append('ME-SM')
if vac4[1]>0:
  options.append('ME-MG')
if vac5[0]>0:
  options.append('MA-SM')
if vac5[1]>0:
  options.append('MA-MG')
if vac6[0]>0:
  options.append('BT-SM')
if vac6[1]>0:
  options.append('BT-MG')
if vac7[0]>0:
  options.append('CL-SM')
if vac7[1]>0:
  options.append('CL-MG')
def oplist(op):
  c='';
  for i in range(0,np.size(op)):
    c=str(c)+' '+str(op[i])
  return c
def decode(ss):
  z=[];
  for i in range(0,ss.count('#')):
    x=ss.partition('#')
    z.append(str(x[0]).strip())
    ss=str(x[2])
  z.append(ss)
  return z
if "appno" not in st.session_state:
  st.session_state.appno=''
if "name" not in st.session_state:
  st.session_state.name=''
if "keam" not in st.session_state:
  st.session_state.keam=''
if "reserve" not in st.session_state:
  st.session_state.reserve=''
if "opti" not in st.session_state:
  st.session_state.opti=''
st.header("Form for Spot Entry")
with st.form("my_form",clear_on_submit=True):
  ga=st.text_input('Application Number')
  gb=st.text_input('Name')
  gc=st.text_input('KEAM Rank')
  gd=st.selectbox('Reservation Category', ['General', 'EWS', 'OEC', 'OBC', 'Latin Catholic and Anglo Indian (LA)', 'Other Backward Hindu (BH)', 'Ezhava (EZ)', 'Muslim (MU)', 'Viswakarma and related communities(VK)'])
  op=st.multiselect('Options', options)
  ge=oplist(op)
  submitted=st.form_submit_button(label='Submit')
  if submitted:
    st.session_state['appno']=str(st.session_state['appno'])+'#'+str(ga)
    st.session_state['name']=str(st.session_state['name'])+'#'+str(gb)
    st.session_state['keam']=str(st.session_state['keam'])+'#'+str(gc)
    st.session_state['reserve']=str(st.session_state['reserve'])+'#'+str(gd)
    st.session_state['opti']=str(st.session_state['opti'])+'#'+str(ge)
    for item in st.session_state.items():
      st.write(item)
finished=st.button(label='Finish')
if finished:
  a=st.session_state['appno'].lstrip('#');
  b=st.session_state['name'].lstrip('#');
  c=st.session_state['keam'].lstrip('#');
  d=st.session_state['reserve'].lstrip('#');
  e=st.session_state['opti'].lstrip('#');
  y1=decode(a)
  y2=decode(b)
  y3=decode(c)
  y4=decode(d)
  y5=decode(e)
  spotdf=pd.DataFrame()
  spotdf['Application Number']=y1
  spotdf['Name']=y2
  spotdf['KEAM Rank']=y3
  spotdf['Reservation Category']=y4
  spotdf['Opted']=y5
  st.subheader("Spot Application List")
  sdf=spotdf.to_csv().encode('utf-8')
  st.dataframe(spotdf)
  st.download_button("Press to Download",sdf,"file.csv","text/csv",key='download-csv')
  st.session_state.appno=''
  st.session_state.name=''
  st.session_state.keam=''
  st.session_state.reserve=''
  st.session_state.opti=''
  st.balloons()
  exit()
  st.write("Failed")
