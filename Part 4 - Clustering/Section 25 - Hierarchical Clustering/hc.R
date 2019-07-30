# Hierarchical Clustering 
# Import the mall dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

# Using the dendogram to find the optimal number of cluster
dendogram = hclust(dist(X, method = 'euclidean'),
                   method = 'ward.D')

# ploting the dendogram
plot(dendogram, 
     main = paste('Dendogram'),
     xlab = 'Customer',
     ylab = 'Euclidean distance')

# Fitting Hierarchical Clustering to the mall dataset 
hc = hclust(dist(X, method = 'euclidean'),
            method = 'ward.D')
y_hc = cutree(hc, 5)

# Visualising the Cluster
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         plotchar = FALSE,
         span = TRUE,
         main = paste("Cluster of clients"),
         xlab = "Anual Income",
         ylab = "Spending Score")
