# Roger Hayden 
# Johns Hopkins University
# 3/27/2023

# Assignment 9 & 10 Problem 2

# Installing/loading libraries
#install.packages("olsrr")
#install.packages("readxl")
#install.packages("leaps")
library(olsrr)
library(readxl)
library(leaps)

df = read.csv("C:\\Users\\roger\\OneDrive\\Desktop\\Education\\Johns Hopkins Courses\\Spring 2023\\Statistical Models and Regression\\Module9&10Assignment_Roger_Hayden\\Data Table B.11.csv")
df

x <- df[, c('Aroma', 'Body','Flavor','Oakiness','ï..Clarity', 'Region')]
x

y <- df[,c('Quality')]
y

bestmodels <- leaps(x, y)
bestmodels

min(bestmodels$Cp)

bestmodel <- leaps(x, y, nbest = 1)
bestmodel