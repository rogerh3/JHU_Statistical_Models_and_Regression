# Roger Hayden 
# Johns Hopkins University
# 4/17/2023

# Module 11 & 12 Assignment - Problem 3

library(aod)
library(ggplot2)
library(readxl)
library(pscl)


df = read.csv("C:\\Users\\roger\\OneDrive\\Desktop\\Education\\Johns Hopkins Courses\\Spring 2023\\Statistical Models and Regression\\Module11&12Assignment_Roger_Hayden\\Problem 13.26 Data.csv")
df

## Performing Logistic Regression Model ##
model <- glm(y ~ Temperature + Oil + Time, data = df, family = "poisson")
summary(model)

pscl::pR2(model)["McFadden"]

plot(model)