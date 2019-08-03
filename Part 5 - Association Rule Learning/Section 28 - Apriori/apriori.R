# Association Rule Learnign - Apriori Algorithm
# Data Preprocessing 
dataset = read.csv('Market_Basket_Optimisation.csv', header = FALSE)
# install.packages('arules')
library(arules)

# create a sparse matrix
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)

# ploting the most frequent data
itemFrequencyPlot(dataset, topN = 100)

# Training Apriori on the dataset 
rules = apriori(data = dataset, parameter = list(support = 0.004, confidence = 0.2))

# Visualizing The Result
inspect(sort(rules, by = 'lift')[1:10])