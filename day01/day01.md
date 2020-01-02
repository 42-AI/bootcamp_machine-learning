
# Bootcamp ML

# Day01 - Linear Regression

During this day you will learn the first concepts constituing the field of machine learning.





## Notions of the day

Matrix operations, gradient descent, cost function, normal equation, MSE, RMSE R-score and learning rate. 

## General rules

* The version of Python to use is 3.7, you can check the version of Python with the following command: `python -V`
* The norm: during this bootcamp you will follow the Pep8 standards https://www.python.org/dev/peps/pep-0008/
* The function eval is never allowed.
* The exercices are ordered from the easiest to the hardest.
* Your exercises are going to be evaluated by someone else, so make sure that your variable names and function names are appropriate and civil. 
* Your manual is the internet.
* You can also ask question in the dedicated channel in Slack: 42-ai.slack.com.
* If you find any issue or mistakes in the subject please create an issue on our dedicated repository on Github: https://github.com/42-AI/bootcamp_machine-larning/issues.

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

## Algorithms

### Exercice 00 - Linear Regression
Reimplement a part of **sklearn.linear_model.LinearRegression** 

Methods:
  - .get_params() - get the parameters theta of the hypothesis,
  - .set_params() - set the parameters theta of the hypothesis,
  - .predict() - calculate the predicted values based on the fitted linear model,

Metric:
  - .mse() - mean square error metric.

### Exercise 01 - Multiples Features and Linear Gradient Descent  
Reimplement a part of **sklearn.linear_model.LinearRegression** and the metric RMSE:
  
Method:
  - .fit() - fit based on the method of the linear gradient descent.

Metric:
  - .rmse() - root mean square error metric.

### Exercice 02 - Multiples Features and Normal Equation
Implement the normal equation and the metric R-score:

Method:
  - .normalequation() - fit based on the method of the normal equation.

Metric:
  - .rscore() - R score metric.
