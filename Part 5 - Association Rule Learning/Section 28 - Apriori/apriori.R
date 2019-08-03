# Association Rule Learnign - Apriori Algorithm
# Data Preprocessing 
dataset = read.csv('Market_Basket_Optimisation.csv', header = FALSE)
# install.packages('arules')
library(arules)

# create a sparse matrix
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)