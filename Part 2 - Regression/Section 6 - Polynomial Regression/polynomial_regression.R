# Polynomial Regression 
# Data Processing 

# Importing Dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Splitting the dataset into the Trainning set and Testing set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
# comment : training_set[, 2:3] means we only take the column number 2 and 3
# comment : This is comment : due the the scaling in must in numeric
# comment : colum number 1 and number 4 is still not numeric as we only changed into the categorical as a factor means
# comment : the origin value type still remembered by the machine

# Fitting Linear Regression to the dataset 
lin_reg = lm(formula = Salary ~.,
             data = dataset)

# Fitting Polynomial Regression to the dataset 
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
dataset$Level5 = dataset$Level^5
dataset$Level6 = dataset$Level^6
poly_reg = lm(formula = Salary ~. , 
              data = dataset)

# Visualizing the Linear Regressiong results 
library(ggplot2)

ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour='red')+
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)), colour='blue')+
  ggtitle('Truth or Bluff (Linear Regression)')+
  xlab('Level')+
  ylab('Salary')

# Visualizing the Polynomial Regression results
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour='red')+
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)), colour='blue')+
  ggtitle('Truth or Bluff (Polynomial Regression)')+
  xlab('Level')+
  ylab('Salary')

# Predicting a new Result with Linear Regression 
Y_pred = predict(lin_reg, data.frame(Level = 6.5))

# Predicting a new result with Polynomial Regression
Y_pred = predict(poly_reg, data.frame(Level = 6.5,
                                      Level2 = 6.5^2,
                                      Level3 = 6.5^3, 
                                      Level4 = 6.5^4,
                                      Level5 = 6.5^5,
                                      Level6 = 6.5^6))


