# Bootcamp Machine Learning

## Day00: Mathematical Delights
Starting by recoding some usefull functions and formulas used later during the week. 
The idea is to help the student to 'tame' the mathematical jargon. 
They will have to simply implement the functions following the formulas without knowing what it is about. 
Then magically these already 'tamed' material will be used in context and understood without having to fight with its abstract notation.

* Iterative delights (loop only)
	- sum
	- mean
	- variance

	- zscore standardization
	- min-max standardization

	- linear cost function
	- logistic cost function
	- gradient descent
	- regularization (ridge regression)

	- Gini Impurity
	- Shannon's Entropy
	- Information Gain (w/ Gini impurity, Entropy, or variance)

* Vectorized delights (vectorized implementation)
 	- sum
	- mean
	- variance

	- zscore
	- min-max
	
	- linear cost function
	- linear cost function + reg
	- logistic cost function
	- logistic cost function + reg
	- gradient descent
	- gradient descent + reg


## Day01: Linear Regression
* Linear Cost Function
* Linear Gradient Descent
* Regularization

* Feature Engineering 0 - Standardization:
	- z score
	- min-max

* Model Evaluation:
	- Regression metric


## Day02: Logistic Regression
* Logistic Cost Function
* Logistic Gradient Descent

* Feature engineering 1:
	- polynomial features
	- interactions terms

* Model Evaluation:
	- Classification metric (precision, recall, specificity)

## Day03: Decision Tree
* Decision Tree Algo:
* Classification metric:
	- Entropy
	- Gini
* Regression metric:
	- Variance 

* Feature Importance

* Model Evaluation: 
	- Cross Validation

## Day04: Unsupervized Learning
* PCA
* Clustering 

* Feature engineering 2:
	- one-hot encoding

## Rush: Classification on MNSIT handwritten digits database.
The students have to build the best classifier for handwritten digits recognition. They will have access to two datasets:
	- Dataset1: A sample directly from the MNSIT with two missing classes (ex. no '8' and '6')
	- Dataset2: A bigger (and complete) but 'corrupted' sample from MNSIT with missing or abberant values.

### In order to get the best performance, the student will have to use both dataset which means:	
	- experiment several ways to find out the missing classes:
		1) KNN, unsuppervised learning
	- experiment several ways to deal with missing / aberrant values, e.g.: 
		1) replacement by mean/median/mode
		2) smarter replacement : KNN, RF, etc.

### They will also have to consider the use of  mixed classifiers, such that:
	- bagged classifiers 
	- random forest

