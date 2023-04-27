# Roger Hayden 
# Johns Hopkins University
# 4/13/2023

# Module 11 & 12 Assignment - Problem 2

library(aod)
library(ggplot2)
library(readxl)
library(pscl)
library(ggplot2)

df = read.csv("C:\\Users\\roger\\OneDrive\\Desktop\\Education\\Johns Hopkins Courses\\Spring 2023\\Statistical Models and Regression\\Module11&12Assignment_Roger_Hayden\\Problem 13.4 Data.csv")
df

## Performing Logistic Regression Model ##
mylogit <- glm(y ~ Discount, data = df, family = "binomial")
summary(mylogit)

pscl::pR2(mylogit)["McFadden"]

#plot logistic regression curve
ggplot(df, aes(x=Discount, y=y)) + 
  geom_point(alpha=.5) +
  stat_smooth(method="glm", se=FALSE, method.args = list(family=binomial))

plot(mylogit)

## Creating the model with a Quadratic Variable ##
mylogit2 <- glm(y ~ poly(Discount, 2), data = df, family = "binomial")
summary(mylogit2)

pscl::pR2(mylogit2)["McFadden"]

#plot logistic regression curve
plot(mylogit2)

# Checking Wald statistics for our Variables
wald.test(Sigma = vcov(mylogit2), b = coef(mylogit2), Terms = 1)
