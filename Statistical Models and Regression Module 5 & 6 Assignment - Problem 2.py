#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Roger H Hayden III
# Johns Hopkins University
# Statistical Models and Regression Module 5 & 6 Assignment
# 03/05/2023


# In[2]:


import pandas as pd
import numpy as np
import statistics 
from scipy import stats
from scipy import linalg


# In[3]:


# Read in Excel
df = pd.read_excel(r'C:\Users\roger\OneDrive\Desktop\Johns Hopkins Courses\Spring 2023\Statistical Models and Regression\Table B.12 Data.xlsx')
print(df)


# Part 1 of our assignment is to create an overall analysis of our model using Temp and Soaktime as a continuous variable

# Calculating beta-hat

# In[5]:


# Assigning x and y matrices
x = np.matrix(df[['One','Soaktime']])
y = np.matrix(df[['Temp']])


# In[6]:


# Creating x transpose matrix
x_transpose = x.transpose()
print(x_transpose)


# In[7]:


# Calculating the first part of calculating Beta-hat for Multiple Linear Regression Analysis
x_transpose_x = x_transpose @ x
print(x_transpose_x)


# In[8]:


# Calculating the second part of calculating Beta-hat for Multiple Linear Regression Analysis
x_transpose_y = x_transpose @ y
print(x_transpose_y)


# In[9]:


# Finding the inverse of part 1
x_transpose_x_inv = linalg.inv(x_transpose_x)
print(x_transpose_x_inv)


# In[10]:


# Multiplying the inverse of part 1 and part 2
b_hat = x_transpose_x_inv @ x_transpose_y
print(b_hat)


# Calculating SSR

# In[11]:


# First we need b_hat transpose
b_hat_transpose = b_hat.transpose()
print(b_hat_transpose)


# In[12]:


# We already have X' and y so next we need to calculate the summation of yi^2
# Lets use our y matrix and add all of the values then square them
ysum = 0
for i in y:
    ysum = ysum + i
print(ysum)


# In[13]:


ysum_squared = ysum ** 2
print(ysum_squared)


# In[14]:


# Now we need to divide ysum_squared by n
ysum_squared_n = ysum_squared / 15
print(ysum_squared_n)


# In[15]:


# From here we can calculate SSR
# We have x_transpose_y from part A
SSR = b_hat_transpose @ x_transpose_y - ysum_squared_n
print(SSR)


# Calculating SSRES

# In[16]:


# We have y, B-hat' and X'
# We need to get y' then we can calculate SSRES
y_transpose = y.transpose()
print(y_transpose)


# In[17]:


SSRES = (y_transpose @ y) - (b_hat_transpose @ x_transpose_y)
print(SSRES)


# Calculating SST

# In[18]:


SST = SSR + SSRES
print(SST)


# Calculating MSR

# In[19]:


MSR = SSR / 1
print(MSR)


# Calculating MSRES

# In[22]:


MSRES = SSRES / 13
print(MSRES)


# Calculating F0

# In[23]:


F0 = MSR / MSRES
print(F0)


# Calculating R^2 and R^2 adj

# In[24]:


R2 = 1 - (SSRES/SST)
print(R2)


# In[25]:


R2_adj = 1 - (SSRES/13)/(SST/14)
print(R2_adj)


# In[ ]:




