# Regression Template 

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

# Fitting the Regression to the dataset 
# Create your regressor here 

# Predicting a new result
Y_pred = predict(regressor, data.frame(Level = 6.5))

# Visualizing the Regression Model results
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour='red')+
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), colour='blue')+
  ggtitle('Truth or Bluff (Regression Model)')+
  xlab('Level')+
  ylab('Salary')

# Visualizing the Regression Model results (for high resolution and smoother curve)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour='red')+
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))), colour='blue')+
  ggtitle('Truth or Bluff (Regression Model)')+
  xlab('Level')+
  ylab('Salary')


