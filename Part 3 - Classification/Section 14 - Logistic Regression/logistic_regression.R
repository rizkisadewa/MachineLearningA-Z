# Logistic Regression 

# Data Processing 

# Importing Dataset
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset[, 3:5]

# Splitting the dataset into the Trainning set and Testing set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[, 1:2] = scale(training_set[, 1:2])
test_set[, 1:2] = scale(test_set[, 1:2])
# comment : training_set[, 2:3] means we only take the column number 2 and 3
# comment : This is comment : due the the scaling in must in numeric
# comment : colum number 1 and number 4 is still not numeric as we only changed into the categorical as a factor means
# comment : the origin value type still remembered by the machine

# Fitting Logistic Regression to the Training Set 
classifier = glm(formula = Purchased ~.,
                 family = binomial,
                 data = training_set)

# Predicting the Test set results
prob_pred = predict(classifier, type = 'response', newdata = test_set[-3])
y_pred = ifelse(prob_pred > 0.5, 1 , 0)