# Data Processing 

# Importing Dataset
dataset = read.csv('Data.csv')

# Taking case of missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)