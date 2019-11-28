# Bootcamp Machine Learning
Bootcamp to learn basics in Machine Learning by 42 AI

## Day00: Mathematical Delights
Starting by recoding some usefull functions and formulas used later during the week. 
The idea is to help the student to 'tame' the mathematical jargon. 
They will have to simply implement the functions following the formulas without knowing what it is about. 
Then magically these already 'tamed' material will be used in context and understood without having to fight with its abstract notation.

 	* sum
	* mean
	* variance
 	* standard deviation
  
 	* dot product
 	* matrix-vector multiplication
 	* matrix-matrix multiplication
  
	* MSE - iterative
	* MSE - vectorized
 	* MSE as linear cost function - iterative
 	* MSE as linear cost function - iterative 
 	* linear gradient - iterative
 	* linear gradient - vectorized
  
  
## Day01: Linear Regression
### Algorithm
	* Linear Cost Function
	* Linear Gradient Descent
	* Regularization
### Model Evaluation
	* MSE
	* MAE
	* RMSE

## Day02: Logistic Regression
### Math
	* logistic cost function
  * sigmoid
  * logistic gradient 
### Algorithm
	* Logistic Cost Function
	* Logistic Gradient Descent
### Model Evaluation
	* accuracy
	* precision 
	* recall 
	* f1-score


## Day03: Feature Engineering and Regularization
### Math
  	* ridge regularization part - iterative 
  	* ridge regularization part - vectorized
  	* regularized MSE - iterative
  	* regularized MSE - vectorized
  	* regularized Linear Gradient - iterative
  	* regularized Linear Gradient - vectorized
  	* regularized Logistic Gradient - iterative
  	* regularized Logistic Gradient - vectorized
  
### Feature Engineering
#### Standardization
	* z score
	* min-max
#### Feature creation
	* polynomial features
	* interactions terms
  
### Regularization - Ridge Regression
#### Regularized Linear Regression
  	* regularized cost function
  	* regularized gradient descent
#### Regularized Logistic Regression
  	* regularized cost function
  	* regularized gradient descent


## Day04: Decision Tree
### Math
  * Gini Impurity
	* Shannon's Entropy
	* Information Gain (w/ Gini impurity, Entropy, or variance)
### Algorithm
	* Decision Tree for classification
		* Entropy
		* Gini
	* Decision Tree for regression
		* Variance
	* Feature importance


## Rush: Classification on MNIST handwritten digits database.
### The students have to build the best classifier for handwritten digits recognition. They will have access to two datasets.
	* Dataset1: A sample from the MNIST with two missing classes (ex. no '8' and '6')  
	* Dataset2: A bigger (and complete) but 'corrupted' sample from MNIST with missing or abberant values.

### In order to get the best performance, the student will have to use both datasets which means

#### * experiment several ways to find out the missing classes:
	* KNN, unsupervised learning
#### * experiment several ways to deal with missing / aberrant values, e.g.: 
	* replacement by mean/median/mode
	* smarter replacement : KNN, RF, etc.

### They will also have to consider the use of  mixed classifiers, such that:
	* bagged classifiers 
	* random forest

