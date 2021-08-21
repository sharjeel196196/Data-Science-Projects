#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df_energy = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Desktop\energy_train_1d_dirty.csv' , sep = ';')
df_wip = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Desktop\wip_2d_dirty.csv' , sep = ';')


# In[3]:


df_energy.info()
df_energy.describe()


# In[4]:


#Cleaning_df_energy

#Dropping Duplicate values
df_energy.drop_duplicates()

#Dropping Null values
df_energy.dropna()

#Eleminating negative values
df_energy = df_energy[(df_energy['value_max'] >= 0) & (df_energy['value_avg'] >=0) & (df_energy['value_min'] >=0)]
df_energy.info()


# In[5]:


df_wip.info()
df_wip.describe()


# In[6]:


#date format change function
def changeformat(data_series):
 style = ['%Y-%m-%d %H:%M:%S' , '%y%m%d %H:%M:%S']
 dates = []
 for p in style:
    dates.append(pd.to_datetime(data_series , format=p , errors='coerce'))
 return pd.concat(dates , axis=1).ffill(axis=1).iloc[:,-1]


# In[7]:


#function calling
df_wip['valid_from'] = changeformat(df_wip.valid_from)
df_wip['valid_to'] = changeformat(df_wip.valid_to)


# In[8]:


#Task_2 Data Analysis


# In[9]:


#1
df_wip['lc_recipe_id'].value_counts().keys()[0]


# In[10]:


#2
#df_energy['eqp_id'].count()

df_wip[['eqp_id' , 'entity_id' , 'wafer_id']].groupby('eqp_id').count()


# In[11]:


#3

df_energy.describe()


# In[12]:


#4

df_energy['from_ts'] = pd.to_datetime(df_energy['from_ts'] , format='%Y-%m-%d %H:%M:%S')
df_energy['to_ts'] = pd.to_datetime(df_energy['to_ts'] , format='%Y-%m-%d %H:%M:%S')
seg = df_energy.groupby([df_energy['eqp_id'] , df_energy['from_ts'].dt.hour]).value_avg.sum()
pd.Series.sort_values(seg , ascending = False)


# In[13]:


#5
#df_energy.head()

df_wip[(df_wip['eqp_id']==4216) & (df_wip['valid_from'] >'1999-08-01 07:00') & (df_wip['valid_to'] <'1999-08-01 08:00')].segment_name


# In[14]:


df_energy[(df_energy['eqp_id']==4216) & (df_energy['from_ts'] >'1999-08-01 07:00') & (df_energy['to_ts'] <'1999-08-01 08:00')].sum()


# In[15]:


df_energy.head()


# In[17]:


df_wip.tail()


# In[ ]:


combined_datafram = pd.merge(df_energy , df_wip , how = '')


# In[ ]:




