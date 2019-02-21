# Data Processing 

# Importing Dataset
dataset = read.csv('Data.csv')

# Encoding Categorical Data 
dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c('Yes', 'No'),
                           labels = c(0,1))