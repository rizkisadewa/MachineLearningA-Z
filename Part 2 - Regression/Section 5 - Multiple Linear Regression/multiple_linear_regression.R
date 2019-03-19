# Multiple Linear Regression 

# Data Processing 

# Importing Dataset
dataset = read.csv('50_Startups.csv')
# dataset = dataset[, 2:3]

#Encoding Categorical Data 
dataset$State = factor(dataset$State,
                         levels = c('New York', 'California', 'Florida'),
                         labels = c(1,2,3))

# Splitting the dataset into the Trainning set and Testing set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
# comment : training_set[, 2:3] means we only take the column number 2 and 3
# comment : This is comment : due the the scaling in must in numeric
# comment : colum number 1 and number 4 is still not numeric as we only changed into the categorical as a factor means
# comment : the origin value type still remembered by the machine

# Fitting Multiple Linear Regression to the Trainset
# Option 2 : Much simpler
regressor = lm(formula = Profit ~ R.D.Spend,
               data = training_set)

# Predicting the Test set results
Y_pred = predict(regressor, newdata = test_set)

# Building predicting optimal model using Backward Elimination 
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, 
               data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, 
               data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, 
               data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend, 
               data = dataset)
summary(regressor)



