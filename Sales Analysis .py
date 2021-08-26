#!/usr/bin/env python
# coding: utf-8

# #### Task # 01 ----- Concatinating all files in 1 dataframe
# 

# In[1]:


import pandas as pd
import os


# In[2]:


df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Sales_Data\Sales_April_2019.csv")
df.tail()


# In[3]:



files = [file for file in os.listdir(r"C:\Users\Lenovo\OneDrive\Desktop\Sales_Data")]
all_months_data = pd.DataFrame()
for file in files:
    df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data , df])
    
    
all_months_data.tail()                     
all_months_data.to_csv("all_data.csv" , index=False)    
    


# #### Read in updated dataframe

# In[4]:


all_data = pd.read_csv("all_data.csv")
all_data.head()


# #### Data Cleaning

# In[5]:


all_data = all_data.dropna()
all_data.isnull().sum()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### Task # 02 ----- Add month as new column and change type to int32

# In[6]:


all_data['Month'] = all_data['Order Date'].str[0:2]
all_data.head()


# In[16]:



all_data['Month'].astype("int32")


# In[15]:


all_data = all_data[all_data["Month"] != "Or"]
all_data.head()


# #### Changing types of columns

# In[31]:


all_data["Quantity Ordered"] = pd.to_numeric(all_data["Quantity Ordered"])
all_data["Price Each"] = pd.to_numeric(all_data["Price Each"])
pd.options.mode.chained_assignment = None 


# In[32]:


all_data.head()


# In[33]:


all_data.info()


# #### Add a Sales column

# In[34]:


all_data["Sales"] = all_data["Quantity Ordered"] * all_data["Price Each"]
all_data.head()


# #### Add a new column "City"

# In[35]:


all_data["City"] = all_data["Purchase Address"].apply(lambda x: f"{x.split(',')[1]} ({x.split(',')[2]})")


all_data.head()


# #### What was the best month for sales and how much was earned in that month?

# In[36]:


all_data[["Month" ,"Sales"]].max()


# In[37]:


results = all_data.groupby("Month").sum()


# In[38]:


import matplotlib.pyplot as plt

months = range(1,13)
plt.bar(months , results["Sales"])

plt.xticks(months)
plt.ylabel("Sales in USD")
plt.xlabel("Month number")
plt.show()


# #### Which city has the highest number of sales?

# In[39]:


highest_sales = all_data.groupby("City").sum()
print(highest_sales)


# In[40]:


import matplotlib.pyplot as plt
cities = all_data["City"].unique()
plt.bar(cities , highest_sales["Sales"])

plt.xticks(cities , rotation = 'vertical' , size ='10')
plt.ylabel("Sales in USD")
plt.xlabel("City Name")
plt.show()


# #### What time we should advertise the most to increase the likelihood of purchase?

# In[41]:


all_data.head()


# In[42]:


all_data["Order Date"] = pd.to_datetime(all_data["Order Date"])


# In[44]:


all_data["Hour"] = all_data["Order Date"].dt.hour
all_data["Minute"] = all_data["Order Date"].dt.minute
all_data.head()


# In[51]:


hours = [hour for hour, df in all_data.groupby("Hour")]
plt.plot(hours , all_data.groupby("Hour").count())
plt.xticks(hours)
plt.grid()
plt.xlabel("Hours")
plt.ylabel("Number of sales")
plt.show()


# In[ ]:


# My recommendations to put advertisement is at 11.00-12.00 and then 19.00


# #### What products are often sold together?

# In[60]:


df = all_data[all_data["Order ID"].duplicated(keep=False)]

df["Grouped"] = df.groupby("Order ID")["Product"].transform(lambda x: ',' .join(x))
df.head()


# In[62]:


df = df[["Order ID" , "Grouped"]].drop_duplicates()
df.head()


# In[69]:


from itertools import combinations
from collections import Counter

count = Counter()

for row in df["Grouped"]:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list , 2)))
    
for key, value in count.most_common(10):
    print(key, value)


# #### Which product was sold the most? Why do you think so?

# In[80]:


product_group  = all_data.groupby("Product")
quantity_ordered = product_group.sum()["Quantity Ordered"]
products = [product for product , df in product_group]
plt.xlabel("Products")
plt.ylabel("Quantity Ordered")
plt.bar(products , quantity_ordered)
plt.xticks(products , rotation = 'vertical')
plt.show()


# In[81]:


all_data.head()


# In[97]:


import seaborn as sns
price = all_data.groupby("Product").mean()['Price Each']
fig , ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(products , quantity_ordered)
ax2.plot(products , price , 'b-')
ax1.set_xlabel("Products")
ax1.set_ylabel("Qauntity Ordered" , color = 'g')
ax2.set_ylabel("price ($)" , color = 'b')
ax1.set_xticklabels(products , rotation = 'vertical')
plt.show()


# In[ ]:





# In[ ]:




