# Simple Linear Regression 

# Importing Dataset
dataset = read.csv('Salary_Data.csv')
# dataset = dataset[, 2:3]

# Splitting the dataset into the Trainning set and Testing set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$YearsExperience, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
# comment : training_set[, 2:3] means we only take the column number 2 and 3
# comment : This is comment : due the the scaling in must in numeric
# comment : colum number 1 and number 4 is still not numeric as we only changed into the categorical as a factor means
# comment : the origin value type still remembered by the machine

# Fitting Simple Linear Regression to the Training Set 
regressor = lm(formula = Salary ~ YearsExperience, 
               data = training_set)