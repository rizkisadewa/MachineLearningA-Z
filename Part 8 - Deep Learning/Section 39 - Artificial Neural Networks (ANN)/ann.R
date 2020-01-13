# Artificial Neural Network

# Data Processing 

# Importing Dataset
dataset = read.csv('Churn_Modelling.csv')
dataset = dataset[4:14]

# Encoding the categorical variables as factors
dataset$Geography = as.numeric(factor(dataset$Geography,
                                      levels = c(
                                        'France',
                                        'Spain',
                                        'Germany'
                                      ),
                                      labels = c(1,2,3)
                                      ))
dataset$Gender = as.numeric(factor(dataset$Gender, 
                                   levels = c('Female', 'Male'),
                                   labels = c(1,2)))

# Splitting the dataset into the Trainning set and Testing set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Exited, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[-11] = scale(training_set[-11])
test_set[-11] = scale(test_set[-11])
# comment : training_set[, 2:3] means we only take the column number 2 and 3
# comment : This is comment : due the the scaling in must in numeric
# comment : colum number 1 and number 4 is still not numeric as we only changed into the categorical as a factor means
# comment : the origin value type still remembered by the machine

# Fitting Classifier Regression to the Training Set 
# Create your classifier

# Make artificial neural networdk
# install.packages('h2o')
library(h2o)
h2o.init(nthreads = -1)

# Predicting the Test set results
prob_pred = predict(classifier, type = 'response', newdata = test_set[-3])
y_pred = ifelse(prob_pred > 0.5, 1 , 0)

# Making the Confusion Matrix
cm = table(test_set[,3], y_pred)