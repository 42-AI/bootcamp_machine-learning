# Bootcamp ML

# Day02 - Logistic Regression

Welcome to the day02 of the machine learning bootcamp ! Today you will see how to implement a logistic regression
class using a gradient descent algorithm. We will first go through a bit of maths, then we will implement our
class and to finish we will build our model evaluation functions.

## Notions of the day

* Sigmoid
* Log loss
* Gradient descent
* Logistic regression
* Model evaluation
* Confusion matrix

## General rules

* The version of Python to use is 3.7.x, you can check the version of Python with the following command: `python -V`
* The norm: during this bootcamp you will follow the Pep8 standards https://www.python.org/dev/peps/pep-0008/
* The function eval is never allowed.
* The exercises are ordered from the easiest to the hardest.
* Your exercises are going to be evaluated by someone else so make sure that variables and functions names are appropriated. 
* Your man is internet.
* You can also ask question in the dedicated channel in Slack: 42-ai.slack.com.
* If you find any issue or mistakes in the subject please create an issue on our dedicated repository on Github: https://github.com/42-AI/bootcamp_machine-learning/issues.

## Helper 

Ensure that you have the right Python version.

```
$> which python
/goinfre/miniconda/bin/python
$> python -V
Python 3.7.*
$> which pip
/goinfre/miniconda/bin/pip
```

## Mathematical delights (continued)

### Exercise 00 - Sigmoid

### Exercise 01 - Logistic Loss Function

### Exercise 02 - Logistic Gradient

### Exercise 03 - Vectorized Logistic Loss Function

### Exercise 04 - Vectorized Logistic Gradient


## Algorithm

### Exercise 05 - Logistic Regression
Reimplement **sklearn.linear_model.LogisticRegression**
Parameters:
  - alpha - learning rate
  - max_iter - int, optional (default=1000)
  - verbose - display epochs with log loss
  - learning_rate - str, 'constant' or 'invscaling'

Methods:
    .fit() - gradient descent
    .predict() - model predictions
    .score() - score on predictions

## Model Evaluation

### Exercice 06 - Accuracy
Reimplement **sklearn.metrics.accuracy_score**
Parameters:  
  - y_true: array
  - y_pred: array

### Exercise 07 - Precision
Reimplement **sklearn.metrics.precision_score**
Parameters:  
  - y_true: array
  - y_pred: array

### Exercise 08 - Recall
Reimplement **sklearn.metrics.recall_score**
Parameters:  
  - y_true: array
  - y_pred: array
  
### Exercise 09 - F1 Score
Reimplement **sklearn.metrics.f1_score**
Parameters:  
  - y_true: array
  - y_pred: array
  
 ### Exercise 10 - Confusion matrix
Reimplement **sklearn.metrics.confusion_matrix**
Parameters:  
  - y_true: array
  - y_pred: array
