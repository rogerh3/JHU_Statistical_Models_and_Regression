#!/usr/bin/env python
# coding: utf-8

# In[83]:


# Roger H Hayden III
# Johns Hopkins University
# Statistical Models and Regression Assignment 2 Problem 3


# In[84]:


import pandas as pd
import numpy as np
import statistics 
from scipy import stats
from scipy import linalg


# # Homework Problems

# In[122]:


# Read in Excel
df = pd.read_excel(r'C:\Users\roger\OneDrive\Desktop\Johns Hopkins Courses\Spring 2023\Statistical Models and Regression\Table B.5 Analysis for HW Modules 3 & 4.xlsx')
print(df)


# In[123]:


# Setting Numpy value settings
np.set_printoptions(precision = 3, suppress = True)


# Part A

# Calculating Beta-Hat for Multiple Linear Regression y = Xβ + ε

# β-hat = (X’X)^(-1) X’y

# In[124]:


# Assigning x and y matrices
x = np.matrix(df[['one','X6', 'X7']])
y = np.matrix(df[['Y']])

print(x)


# In[125]:


print(y)


# In[126]:


# Creating x transpose matrix
x_transpose = x.transpose()
print(x_transpose)


# In[127]:


# Calculating the first part of calculating Beta-hat for Multiple Linear Regression Analysis
x_transpose_x = x_transpose @ x
print(x_transpose_x)


# In[128]:


# Calculating the second part of calculating Beta-hat for Multiple Linear Regression Analysis
x_transpose_y = x_transpose @ y
print(x_transpose_y)


# In[129]:


# Finding the inverse of part 1
x_transpose_x_inv = linalg.inv(x_transpose_x)
print(x_transpose_x_inv)


# In[130]:


# Multiplying the inverse of part 1 and part 2
b_hat = x_transpose_x_inv @ x_transpose_y
print(b_hat)


# Part B

# For this portion I calculate out everything need to create an ANOVA table and find the R^2 Values

# Testing for Significance of the regression and calculated R^2 and the adjusted R^2

# ![image.png](attachment:image.png)

# First we Caculate SSR

# In[131]:


# First we need b_hat transpose
b_hat_transpose = b_hat.transpose()
print(b_hat_transpose)


# In[132]:


# We already have X' and y so next we need to calculate the summation of yi^2
# Lets use our y matrix and add all of the values then square them
ysum = 0
for i in y:
    ysum = ysum + i
print(ysum)


# In[133]:


ysum_squared = ysum ** 2
print(ysum_squared)


# In[134]:


# Now we need to divide ysum_squared by n
ysum_squared_n = ysum_squared / 20
print(ysum_squared_n)


# In[135]:


# From here we can calculate SSR
# We have x_transpose_y from part A
SSR = b_hat_transpose @ x_transpose_y - ysum_squared_n
print(SSR)


# Next, we calculate SSRES

# ![image.png](attachment:image.png)

# In[136]:


# We have y, B-hat' and X'
# We need to get y' then we can calculate SSRES
y_transpose = y.transpose()
print(y_transpose)


# In[137]:


SSRES = (y_transpose @ y) - (b_hat_transpose @ x_transpose_y)
print(SSRES)


# Now we can find SST

# In short SST = SSR + SSRES

# In[138]:


SST = SSR + SSRES
print(SST)


# Last we find MSR and MSRES

# In[139]:


MSR = SSR / 2
print(MSR)


# In[140]:


MSRES = SSRES / 17
print(MSRES)


# Now we can find F0 with MSR and MSRES

# In[141]:


F0 = MSR / MSRES
print(F0)


# Now we can find the p value associated with the F0

# The p value for this would be 0.000138 which is significant at p < 0.05

# Following, we can calculate R^2 and R^2 adj

# In[149]:


R2 = 1 - (SSRES/SST)
print(R2)


# In[150]:


R2_adj = 1 - (SSRES/17)/(SST/19)
print(R2_adj)


# Part E

# For Part E I must recreate the above model only using our x6 variable rather than x6 and x7

# I will perform these calculations slightly faster with this runthrough

# In[182]:


# First Calculating b_hat2
# Assigning x and y matrices
x2 = np.matrix(df[['one','X6']])
y2 = np.matrix(df[['Y']])

# Creating x transpose matrix
x2_transpose = x2.transpose()

# Calculating the first part of calculating Beta-hat for Multiple Linear Regression Analysis
x2_transpose_x2 = x2_transpose @ x2

# Calculating the second part of calculating Beta-hat for Multiple Linear Regression Analysis
x2_transpose_y2 = x2_transpose @ y2

# Finding the inverse of part 1
x2_transpose_x2_inv = linalg.inv(x2_transpose_x2)

# Multiplying the inverse of part 1 and part 2
b_hat2 = x2_transpose_x2_inv @ x2_transpose_y2
print(b_hat2)


# In[184]:


# Calulating SSR2
b_hat2_transpose = b_hat2.transpose()
SSR2 = b_hat2_transpose @ x2_transpose_y2 - ysum_squared_n
print(SSR2)


# In[185]:


# Calculating SSRES2
y2_transpose = y2.transpose()
SSRES2 = (y2_transpose @ y2) - (b_hat2_transpose @ x2_transpose_y2)
print(SSRES2)


# In[186]:


# Calculating SST2
SST2 = SSR2 + SSRES2
print(SST2)


# In[191]:


# Calculating MSR2
MSR2 = SSR2 / 1
print(MSR2)


# In[192]:


# Calculating MSRES2
MSRES2 = SSRES2 / 18
print(MSRES2)


# In[193]:


# Calculating F02
F02 = MSR2 / MSRES2
print(F02)


# In[194]:


# Calculating R22
R22 = 1 - (SSRES2/SST2)
print(R22)


# In[196]:


# Calculating R22_adj
R22_adj = 1 - (SSRES2/18)/(SST2/19)
print(R22_adj)


# # Calculation Tests

# Testing multiplication and applications versus data where I know the answer to ensure I am performing calculations correctly

# In[103]:


# Read in Excel
test_df = pd.read_excel(r'C:\Users\roger\OneDrive\Desktop\Johns Hopkins Courses\Spring 2023\Statistical Models and Regression\Test Matrix Data.xlsx')
print(test_df)


# In[104]:


x_test = np.matrix(test_df[['one','X1', 'X2']])
y_test = np.matrix(test_df[['Y']])

print(x_test)


# In[105]:


print(y_test)


# Calculating B-hat

# In[106]:


x_transpose_test = x_test.transpose()
print(x_transpose_test)


# In[107]:


x_transpose_x_test = x_transpose_test @ x_test
print(x_transpose_x_test)


# In[108]:


x_transpose_y_test = x_transpose_test @ y_test
print(x_transpose_y_test)


# In[109]:


x_transpose_x_inv_test = linalg.inv(x_transpose_x_test)
b_hat_test = x_transpose_x_inv_test @ x_transpose_y_test
print(b_hat_test)


# Caclulating Statisical values for the ANOVA table 

# In[110]:


b_hat_test_transpose = b_hat_test.transpose()
b_hat_test_transpose


# In[111]:


# We already have X' and y so next we need to calculate the summation of yi^2
# Lets use our y matrix and add all of the values then square them
ysum_test = 0
for i in y_test:
    ysum_test = ysum_test + i
print(ysum_test)


# In[112]:


ysum_test_squared = ysum_test ** 2
print(ysum_test_squared)


# In[113]:


ysum_test_squared_n = ysum_test_squared / 25
print(ysum_test_squared_n)


# In[114]:


SSR_test = b_hat_test_transpose @ x_transpose_y_test - ysum_test_squared_n
print(SSR_test)


# In[115]:


# Calculating SSRES
y_transpose_test = y_test.transpose()

SSRES_test = (y_transpose_test @ y_test) - (b_hat_test_transpose @ x_transpose_y_test)
SSRES_test


# In[116]:


# Calculating SST
SST_test = SSR_test + SSRES_test
SST_test


# In[181]:


# Testing how to find Cjj for the t0 calculations
x_transpose_x_inv @ [0,1,0]


# In[ ]:




