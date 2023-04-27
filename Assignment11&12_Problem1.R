# Roger Hayden 
# Johns Hopkins University
# 4/13/2023

# Module 11 & 12 Assignment - Problem 1

#install.packages('aod')
#install.packages('pscl')

library(aod)
library(ggplot2)
library(readxl)
library(pscl)

df = read.csv("C:\\Users\\roger\\OneDrive\\Desktop\\Education\\Johns Hopkins Courses\\Spring 2023\\Statistical Models and Regression\\Module11&12Assignment_Roger_Hayden\\Problem 13.2 Data.csv")
df

## Performing Logistic Regression Model ##
mylogit <- glm(Home.Ownership.Status ~ Income, data = df, family = "binomial")
summary(mylogit)

mylogit

## Producing McFadden R^2 ##
pscl::pR2(mylogit)["McFadden"]

## Performing Logistic Regression Model with Income Squared##
mylogit2 <- glm(Home.Ownership.Status ~ Income2, data = df, family = "binomial")
summary(mylogit2)

mylogit2

## Producing McFadden R^2 ##
pscl::pR2(mylogit2)["McFadden"]

## Checking with Income Squared another way ##
mylogit3 <- glm(Home.Ownership.Status ~ poly(Income, 2), data = df, family = "binomial")
summary(mylogit3)

anova(mylogit, mylogit3, test = "LRT")

