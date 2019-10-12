# Natural Language Processing 
# Import Data 
dataset = read.delim('Restaurant_Reviews.tsv', quote='', stringsAsFactors = FALSE)

# Cleaning the text
# install.packages('tm')
install.packages('SnowballC')
library(tm)
corpus = VCorpus(VectorSource(dataset$Review))
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, stopwords())
