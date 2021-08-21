#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[53]:


data = pd.read_csv(r"C:\Users\Lenovo\Music\Datasets\covid-nationality.csv")


# In[34]:


data.head()


# In[37]:


data.columns


# In[39]:


data.describe()


# In[40]:


data.tail()


# In[44]:


data.isnull().sum()


# In[55]:


sns.relplot(x="total_cases" , y="recovered" , data = data)


# In[56]:


sns.relplot(x="total_cases" , y="deaths" , data = data)


# In[60]:


sns.relplot(x="total_cases" , y="total_confirmed_cases" , data = data)


# In[61]:


sns.relplot(x="total_cases" , y="total_hospitalized" , hue = "recovered" , data = data)


# In[64]:


sns.relplot(x="total_cases" , y="total_hospitalized" , kind="line"  , data = data)


# In[ ]:


sns.catplot(x="total_cases" , y="total_hospitalized" , hue = "recovered" , data = data)


# In[ ]:




