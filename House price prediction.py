#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Step 1: Load the data
# Assuming you have a CSV file with house data
data = pd.read_csv("C:/Users/sreet/Downloads/Housing.csv")

data.head()


# In[14]:


# Step 2: Data Preprocessing
# Check for missing values
print(data.isnull().sum())

# Fill or drop missing values
data.fillna(method='ffill', inplace=True)

# Convert categorical variables to numeric using one-hot encoding
data = pd.get_dummies(data)



# In[20]:


plt.scatter(data['area'], data['price'])
plt.scatter(data['area'], data['price'], alpha=0.5)  # Adjust alpha for visibility

plt.xlabel('Area (sq ft)')
plt.ylabel('Price')
plt.title('Price vs Area')
plt.show()



# In[19]:


fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].scatter(data['area'], data['price'], alpha=0.5)
axs[0, 0].set_title('Price vs Area')
axs[0, 0].set_xlabel('Area (sq ft)')
axs[0, 0].set_ylabel('Price')

axs[0, 1].scatter(data['bedrooms'], data['price'], alpha=0.5)
axs[0, 1].set_title('Price vs Bedrooms')
axs[0, 1].set_xlabel('Bedrooms')
axs[0, 1].set_ylabel('Price')

axs[1, 0].scatter(data['bathrooms'], data['price'], alpha=0.5)
axs[1, 0].set_title('Price vs Bathrooms')
axs[1, 0].set_xlabel('Bathrooms')
axs[1, 0].set_ylabel('Price')

axs[1, 1].scatter(data['stories'], data['price'], alpha=0.5)
axs[1, 1].set_title('Price vs Stories')
axs[1, 1].set_xlabel('Stories')
axs[1, 1].set_ylabel('Price')

plt.tight_layout()
plt.show()


# In[ ]:




