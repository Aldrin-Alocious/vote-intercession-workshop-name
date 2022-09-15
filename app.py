import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.image("SCT-LOGO.jpg")
st.title("POOL LAB")
df=pd.read_csv(st.file_uploader('Upload a CSV'))
st.dataframe(df)
AN=df[['Unnamed: 3']]
CT=df[['Unnamed: 4']]
AN=AN.to_numpy()
CT=CT.to_numpy()
nAI=0;nCS=0;nEC=0;nME=0;nMP=0;nMA=0;nBT=0;nCL=0;
AIE=[];CSE=[];ECE=[];MEE=[];MPE=[];MAE=[];BTE=[];CLE=[];
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
  elif CT[i,0]=='Mechanical Production':
    nMP=nMP+1
    MPE.append(AN[i,0])
  elif CT[i,0]=='Mechanical Automobile':
    nMA=nMA+1
    MAE.append(AN[i,0])
  elif CT[i,0]=='Biotechnology':
    nBT=nBT+1
    BTE.append(AN[i,0])
  elif CT[i,0]=='Civil':
    nCL=nCL+1
    CLE.append(AN[i,0])
nos=np.array([nAI,nCS,nEC,nME,nMP,nMA,nBT,nCL])
dep=np.array(['Artificial Intelligence And Machine Learning','Computer Science','Electronics and Communication','Mechanical','Mechanical Production','Mechanical Automobile','Biotechnology','Civil'])
fig1, ax1 = plt.subplots()
ax1.pie(nos, labels=dep, autopct='%1.1f%%')
ax1.axis('equal')
st.header("Admissions this year")
st.pyplot(fig1)
st.write('Artificial Intelligence And Machine Learning\t- ',nAI)
st.write('Computer Science\t\t\t\t- ',nCS)
st.write('Electronics and Communication\t\t\t- ',nEC)
st.write('Mechanical\t\t\t\t\t- ',nME)
st.write('Mechanical Production\t\t\t\t- ',nMP)
st.write('Mechanical Automobile\t\t\t\t- ',nMA)
st.write('Biotechnology\t\t\t\t\t- ',nBT)
st.write('Civil\t\t\t\t\t\t- ',nCL)
AIE=np.array(AIE,ndmin=2)
CSE=np.array(CSE,ndmin=2)
ECE=np.array(ECE,ndmin=2)
MEE=np.array(MEE,ndmin=2)
MPE=np.array(MPE,ndmin=2)
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
MP=departments(AN,MPE,df)
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
  stype=np.array(["Merit","Management Quota","NRI","TFW-Merit"])
  fig2, ax2 = plt.subplots(figsize=(1,1))
  ax2.pie(snos, labels=stype, autopct='%1.1f%%', textprops={'fontsize': 2})
  ax2.axis('equal')
  st.pyplot(fig2)
  st.write("Merit\t\t-",m)
  st.write("Management\t-",mq)
  st.write("NRI\t\t-",nri)
  st.write("TFW-Merit\t-",tfw)
st.header('Artificial Intelligence And Machine Learning')
seats(AI)
st.header('Computer Science Engineering')
seats(CS)
st.header('Electronics and Communication Engineering')
seats(EC)
st.header('Mechanical Engineering')
seats(ME)
st.header('Mechanical Production Engineering')
seats(MP)
st.header('Mechanical Automobile Engineering')
seats(MA)
st.header('Biotechnology and Biochemical Engineering')
seats(BT)
st.header('Civil Engineering')
seats(CL)
#width = st.sidebar.slider("plot width", 1, 25, 3)
#height = st.sidebar.slider("plot height", 1, 25, 1)
