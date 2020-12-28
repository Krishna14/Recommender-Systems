# Recommender Systems
 This folder contains the codes implemented as part of CSE 258 course during Fall 2020.
 
 Homework 1 - Basic linear regression
 Homework 2 - Logistic Regression + Graph cut based similarity
 Homework 3 - Similarity based metrics (Jaccard, similarity)
 Homework 4 - Basic TF/IDF metrics
 
 Assignment 1 - Two tasks
  Task 1 - Play prediction task based on dataset obtained from Steam game reviews
  Task 2 - Hours played prediction based on the same dataset as obtained above.
  
Models used for task 1 - 
 1. Similarity based metrics (Jaccard, Cosine)
 2. Popularity based metrics
 3. Features extracted from these metrics passed through a classifier
 4. Things to do - Test the performance of SVD and SVD++ as per Netflix Prize
 
 Models used for task 2 -
 1. Single variable latent factor model given by the following equation -
 
 ![equation](https://latex.codecogs.com/gif.latex?Time%20played%20%3D%20%5Calpha%20&plus;%20%5Cbeta_u%20&plus;%20%5Cbeta_i)
 
       ![equation](https://latex.codecogs.com/gif.latex?%5Calpha) denotes the average time spent by all users;
       
       ![equation](https://latex.codecogs.com/gif.latex?%5Cbeta_u) represents the time spent by user u;
       
       ![equation](https://latex.codecogs.com/gif.latex?%5Cbeta_i) represents the time spent for game i;
 
 All the above mentioned values were obtained using Stochastic gradient descent with MSE as the loss function.
 
 2. Multiple variable latent factor model provided by the following equation -
 
 ![equation](https://latex.codecogs.com/gif.latex?Timeplayed%20%3D%20%5Calpha%20&plus;%20%5Cbeta_u%20&plus;%20%5Cbeta_i%20&plus;%20%5Cgamma_u%20.%20%5Cgamma_i)
 
       ![equation](https://latex.codecogs.com/gif.latex?%5Calpha) denotes the average time spent by all users;
       
       ![equation](https://latex.codecogs.com/gif.latex?%5Cbeta_u) represents the time spent by user u;
       
       ![equation](https://latex.codecogs.com/gif.latex?%5Cbeta_i) represents the time spent for game i;
       
       ![equation](https://latex.codecogs.com/gif.latex?%5Cgamma_u) represents the interaction of user u with k values
       
       ![equation](https://latex.codecogs.com/gif.latex?%5Cgamma_i) represents the interaction of game i with k values
       
       The dot product signifies the interaction between game i and user u while modeling the problem.
 
 To avoid overfitting the problem to this dataset, we use one regularizer to compute the values of all the above mentioned parameters.
 
$$ SE = \frac{\sigma}{\sqrt{n}} $$
