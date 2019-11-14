
# Bootcamp ML

# Day02 - Logistic Regression

A brief description of the day goes here.

## Notions of the day

Notion 1, Notion 2, ...

## General rules

* The version of Python to use is 3.7, you can check the version of Python with the following command: `python -V`
* The norm: during this bootcamp you will follow the Pep8 standards https://www.python.org/dev/peps/pep-0008/
* The function eval is never allowed.
* The exercices are ordered from the easiest to the hardest.
* Your exercices are going to be evaluated by someone else so make sure that variables and functions names are appropriated. 
* Your man is internet.
* You can also ask question in the dedicated channel in Slack: 42-ai.slack.com.
* If you find any issue or mistakes in the subject please create an issue on our dedicated repository on Github: https://github.com/42-AI/bootcamp_python/issues.

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

### Exercise 01 - Logistic Cost Function

### Exercise 02 - Logistic Gradient

### Exercise 03 - Vectorized Logistic Cost Function

### Exercise 04 - Vectorized Logistic Gradient


## Algorithm

### Exercise 00 - Logistic Regression

Reimplement **sklearn.linear_model.LogisticRegression**
Parameters:
  - normal: bool, (default=True) (use normal equation instead of gradient descent)
  - alpha - learning rate if `normal == False`
  - penalty: str, ‘l2’ or ‘none’, optional (default=’l2’)
  - max_iter : int, optional (default=100)

Methods:
    .score() - cost function
    .fit() - gradient descent
    .predict()
    .predict_proba()
    .predict_log_proba()
    ? .get_params()
    ? .set_params()


## Feature Engineering

### Exercise 00 - Polynomial features

Reimplement **sklearn.preprocessing.PolynomialFeatures**
Parameters:
    - degree : integer, optional (default=2)
    - interaction_only : boolean, optional (default = False)
    - include_bias : boolean, optional (default = True)
Methods:
    - .fit()
    - .fit_transform()
    - .transform()


## Model Evaluation

### Exercice 00 - Accuracy
Reimplement  **sklearn.metrics.accuracy_score**
Parameters:  
  - y_true: array
  - y_pred: array

### Exercise 01 - Precision
Reimplement  **sklearn.metrics.precision_score**
Parameters:  
  - y_true: array
  - y_pred: array

### Exercise 02 - Recall
Reimplement  **sklearn.metrics.recall_score**
Parameters:  
  - y_true: array
  - y_pred: array
  
### Exercise 03 - F1 Score
Reimplement  **sklearn.metrics.f1_score**
Parameters:  
  - y_true: array
  - y_pred: array
