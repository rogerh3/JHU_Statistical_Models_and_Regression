#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Roger H Hayden III
# Johns Hopkins University
# Statistical Models and Regression Module 5 & 6 Assignment
# 02/26/2023


# In[2]:


import pandas as pd
import numpy as np
import statistics 
from scipy import stats
from scipy import linalg


# In[54]:


# Read in Excel
df = pd.read_excel(r'C:\Users\roger\OneDrive\Desktop\Johns Hopkins Courses\Spring 2023\Statistical Models and Regression\Question 7.18 Data.xlsx')
print(df)


# First we need to solve for B-hat

# Our X matrix will be different since we have a quadratic equation, we will need to account for every Beta value

# y = β0 + β1X1 + β2X2 + β3X3 + β11X1^2 + β22X2^2 + β33X3^2 + β12X1X2 + β13X1X3 + β23X2X3 + ε

# In[55]:


# Let's add the needed calculations to our df
df.loc[:, 'X1^2'] = df['X1']**2
df.loc[:, 'X2^2'] = df['X2']**2
df.loc[:, 'X3^2'] = df['X3']**2
df.loc[:, 'X1X2'] = df['X1']*df['X2']
df.loc[:, 'X1X3'] = df['X1']*df['X3']
df.loc[:, 'X2X3'] = df['X2']*df['X3']
print(df)


# In[56]:


# Assigning x and y matrices
x = np.matrix(df[['one','X1','X2','X3','X1^2','X2^2','X3^2','X1X2','X1X3','X2X3']])
y = np.matrix(df[['Y']])
print(x)


# In[57]:


# Creating x transpose matrix
x_transpose = x.transpose()
print(x_transpose)


# In[58]:


# Calculating the first part of calculating Beta-hat for Multiple Linear Regression Analysis
x_transpose_x = x_transpose @ x
print(x_transpose_x)


# In[59]:


# Calculating the second part of calculating Beta-hat for Multiple Linear Regression Analysis
x_transpose_y = x_transpose @ y
print(x_transpose_y)


# In[60]:


# Finding the inverse of part 1
x_transpose_x_inv = linalg.inv(x_transpose_x)
print(x_transpose_x_inv)


# In[61]:


# Multiplying the inverse of part 1 and part 2
b_hat = x_transpose_x_inv @ x_transpose_y
print(b_hat)


# Next we calculate SSR

# In[62]:


# First we need b_hat transpose
b_hat_transpose = b_hat.transpose()
print(b_hat_transpose)


# In[35]:


# We already have X' and y so next we need to calculate the summation of yi^2
# Lets use our y matrix and add all of the values then square them
ysum = 0
for i in y:
    ysum = ysum + i
print(ysum)


# In[36]:


ysum_squared = ysum ** 2
print(ysum_squared)


# In[37]:


# Now we need to divide ysum_squared by n
ysum_squared_n = ysum_squared / 18
print(ysum_squared_n)


# In[38]:


# From here we can calculate SSR
# We have x_transpose_y from part A
SSR = b_hat_transpose @ x_transpose_y - ysum_squared_n
print(SSR)


# Calculating SSRES

# In[39]:


# We have y, B-hat' and X'
# We need to get y' then we can calculate SSRES
y_transpose = y.transpose()
print(y_transpose)


# In[40]:


SSRES = (y_transpose @ y) - (b_hat_transpose @ x_transpose_y)
print(SSRES)


# Calculating SST

# In[41]:


SST = SSR + SSRES
print(SST)


# Calculating MSR

# In[42]:


MSR = SSR / 9
print(MSR)


# Calculating MSRES

# In[43]:


MSRES = SSRES / 8
print(MSRES)


# Calculating F0

# In[44]:


F0 = MSR / MSRES
print(F0)


# Calculating R^2 and R^2 adj

# In[45]:


R2 = 1 - (SSRES/SST)
print(R2)


# In[46]:


R2_adj = 1 - (SSRES/8)/(SST/17)
print(R2_adj)


# ---------------------------------------------------

# Calculating SSR with only squared values

# In[47]:


# Assigning x and y matrices
x2 = np.matrix(df[['X1^2','X2^2','X3^2']])


# In[67]:


x2_transpose = x2.transpose()

x2_transpose_y = x2_transpose @ y

b_hat_transpose2 = [2.98833969e-01, -1.55536293e-01,  7.08215483e-03]
print(b_hat_transpose2)


# In[68]:


SSR_2 = b_hat_transpose2 @ x2_transpose_y - ysum_squared_n
print(SSR_2)


# In[ ]:




