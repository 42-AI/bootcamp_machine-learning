# Bootcamp Machine Learning
Bootcamp to learn basics in Machine Learning by 42 AI

## Day00: Mathematical Delights
Starting by recoding some usefull functions and formulas used later during the week. 
The idea is to help the student to 'tame' the mathematical jargon. 
They will have to simply implement the functions following the formulas without knowing what it is about. 
Then magically these already 'tamed' material will be used in context and understood without having to fight with its abstract notation.

### Iterative delights (loop only)
	* sum
	* mean
	* variance
	* zscore standardization
	* min-max standardization
	* linear cost function
	* gradient descent
	* regularization (ridge regression)
### Vectorized delights (vectorized implementation)
 	* sum
	* mean
	* variance
	* zscore
	* min-max
	* linear cost function + reg
	* logistic cost function + reg
	* gradient descent + reg

## Day01: Linear Regression
### Algorithm
	* Linear Cost Function
	* Linear Gradient Descent
	* Regularization
### Feature Engineering - Standardization
	* z score
	* min-max
### Model Evaluation
	* Regression metric


## Day02: Logistic Regression
### Math
	* logistic cost function
### Algorithm
	* Logistic Cost Function
	* Logistic Gradient Descent
### Feature Engineering
	* polynomial features
	* interactions terms
### Model Evaluation
	* Classification metric (precision, recall, specificity)


## Day03: Decision Tree
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
### Model Evaluation
	* Cross Validation


## Day04: Unsupervised Learning
### Algorithm
	* PCA
	* Clustering
### Feature Engineering
	* one-hot encoding


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
