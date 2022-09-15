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
plt.pie(nos,labels=dep)
