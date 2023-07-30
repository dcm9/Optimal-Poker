#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import streamlit as st #can incorporate streamlit last, first use matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans, AgglomerativeClustering


# In[107]:


df = pd.read_csv('new_cleaned_dataset.csv').drop('Unnamed: 0',axis=1).dropna()
df


# In[108]:


df = df[df['aggression_factor'] >= 0]
#df = df[df['num_players'] > 3]
x = df[['river_equity']]
y = df['earnings']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

model1 = LinearRegression()
model1.fit(x_train,y_train).score(x_test,y_test)

#vpip statistics still contain errors


# In[109]:


df.dropna().shape


# In[110]:


filtered_df = df.dropna().groupby('player').filter(lambda x:x['player'].count()>30)
filtered_df = filtered_df.groupby('player').mean()


# In[111]:


feature_df = filtered_df[['aggression_factor','preflop_rank']]
feature_df


# In[112]:


X_1 = preprocessing.StandardScaler().fit(feature_df).transform(feature_df)

kmeans1 = KMeans(n_clusters=4,n_init=20)
clust_1 = kmeans1.fit(X_1)
feature_df['clusters'] = clust_1.labels_
feature_df


# In[113]:


for i in range(0,4):
    plt.scatter(feature_df.loc[feature_df['clusters'] == i, 'aggression_factor'],feature_df.loc[feature_df['clusters'] == i, 'preflop_rank'])


# In[115]:


from sklearn.linear_model import LinearRegression
    
#encode dummies

x = pd.get_dummies(feature_df['clusters']).iloc[:,1].array.reshape(-1,1)
y = filtered_df['earnings']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

linreg = LinearRegression()
linreg.fit(x_train,y_train).score(x_test,y_test)


# In[122]:


x = filtered_df[['pos']]
y = filtered_df['preflop_rank']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

linreg = LinearRegression()
linreg.fit(x_train,y_train).score(x_test,y_test)


# In[123]:


filtered_df


# In[ ]:




