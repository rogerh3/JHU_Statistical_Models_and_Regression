#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Roger H Hayden III
# Johns Hopkins University
# Statistical Models and Regression Module 5 & 6 Assignment
# 03/09/2023


# In[54]:


import pandas as pd
import numpy as np
import statistics 
from scipy import stats
from scipy import linalg
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols


# In[55]:


# Read in Excel
df = pd.read_excel(r'C:\Users\roger\OneDrive\Desktop\Johns Hopkins Courses\Spring 2023\Statistical Models and Regression\Data Table B.5.xlsx')
print(df)


# In[57]:


# Assigning Data for Modeling Purposes
y = df[['y']]
x = df[['x1', 'x6']]


# In[58]:


# Adding the constant column to x for B0
x = sm.add_constant(x) 
print(x)


# In[59]:


# Creating our model and checking data results 
model = ols('y ~ x', data=df).fit()

est = sm.OLS(y, x).fit() 
est.summary()


# In[60]:


stud_res = model.outlier_test()
print(stud_res)


# In[61]:


student_residual_values = stud_res['student_resid']


# In[62]:


plt.scatter(y, student_residual_values)
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('Points')
plt.ylabel('Studentized Residuals') 


# Calculating the R-student (Externally Studentized Residuals)

# In[63]:


# Calculating the hat matrix (H)
hat = x.dot(np.linalg.inv(x.T.dot(x)).dot(x.T))
hat


# In[64]:


# Let's calculate the influence and obtain the standard residuals for our model
influence = model.get_influence()
standardized_residuals = influence.resid_studentized_internal
print(standardized_residuals)


# In[84]:


# Assigning ei
ei = df[['ei']]
print(ei)


# In[85]:


# Assigning the hat diagonal values
hii = pd.DataFrame(np.diag(hat))
print(hii)


# In[126]:


# Calculating S(i)^2
# S(i)^2 = (18(94.27) - ei^2/(1-hii)) / 17

# Calculating the second half of the Si equation
Si_calc_1 = pd.DataFrame(np.divide(ei**2, (1-hii)))
Si_calc_1.rename(columns = {'ei': 'Si_calc'}, inplace = True)
Si_calc_1 = pd.DataFrame(np.divide(Si_calc_1, 17))

print(Si_calc_1)


# In[127]:


# Finishing the Si equation to get our Si values
Si = pd.DataFrame(np.add(-Si_calc_1, (18*94.27)))
print(Si)


# In[134]:


# Officially solving for ti, or the Rstudent values
ti_denom = pd.DataFrame(np.sqrt(np.multiply(Si**2, (1-hii))))
ti = pd.DataFrame(np.divide(ei, ti_denom))
ti.rename(columns = {'ei': 'Rstudent Values'}, inplace = True)
print(ti)


# Calculating the PRESS Value of our model

# In[138]:


PRESS_numerator = pd.DataFrame(np.divide(ei, (1-hii)))
PRESS = pd.DataFrame(np.divide(PRESS_numerator, np.sqrt((np.var(ei)))))
PRESS.rename(columns = {'ei': 'PRESS values'}, inplace = True)
print(PRESS)


# Calculating Standardized Residuals

# In[141]:


# calculating di or the residuals
di = pd.DataFrame(np.divide(ei, np.sqrt(94.27)))
di.rename(columns = {'ei': 'Standardized Residuals'}, inplace = True)
print(di)


# In[ ]:




