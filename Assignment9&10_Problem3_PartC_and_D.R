# Roger Hayden 
# Johns Hopkins University
# 3/27/2023

# Assignment 9 & 10 Problem 3

# Installing/loading libraries
#install.packages("olsrr")
#install.packages("readxl")
#install.packages("leaps")
library(olsrr)
library(readxl)
library(leaps)

df = read.csv("C:\\Users\\roger\\OneDrive\\Desktop\\Education\\Johns Hopkins Courses\\Spring 2023\\Statistical Models and Regression\\Module9&10Assignment_Roger_Hayden\\Data Table B.2.csv")
df

############
## Part C ##
############

model = lm(ï..y ~ x1 + x2 + x3 + x4 + x5, data = df)

# Starting with an empty model
FitStart = lm(ï..y ~ 1, data = df)
summary(FitStart)

step(FitStart, direction = "both", scope = formula(model))

############
## Part D ##
############

x <- df[, c('x1', 'x2','x3','x4','x5')]
x

y <- df[,c('ï..y')]
y

bestmodels <- leaps(x, y, method="Cp", nbest = 1)
bestmodels
bestmodels$Cp

bestmodels2 <- leaps(x, y, method="adjr2", nbest = 1)
bestmodels2
bestmodels2$adjr2

bestmodels3 <- leaps(x, y, method="r2", nbest = 1)
bestmodels3
bestmodels3$r2


min(bestmodels$Cp)

regfit_full = regsubsets(ï..y~., data = df)
summary(regfit_full)
