
# Bootcamp ML

# Day01 - Linear Regression

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

## Algorithms

### Exercice 00 - Linear Regression
Reimplement **sklearn.linear_model.LinearRegression**  
Parameters:
  - alpha: double - learning rate

Methods:
  - .score() - cost function
  - .fit() - normal equation OR gradient descent
  - .predict()
  - ? .get_params()
  - ? .set_params()

### Exercise 01 - Regularized Linear Regression  
Reimplement **sklearn.linear_model.Ridge**
Parameters:  
  - alpha: double - learning rate
  - lambda: double - regularisarion term
  
Methods:
  - .score() - cost function
  - .fit() - gradient descent
  - .predict()
  - ? .get_params()
  - ? .set_params()

### Exercice 02 - Normal equation
Change the two previous classes: 
  - add a parameter : 
    - normal: bool, (default=True) (use normal equation instead of gradient descent)
  - change alpha to be used only if `normal == False`
  
  - .fit() should use gradient descent or normal equation according to the parameters


## Feature Engineering
### Exercise 00 - Standardization: z-score
Reimplement  **sklearn.preprocessing.StandardScaler**
Parameters:  
  - None
Methods:
  - fit()
  - fit_transform()
  
### Exercise 01 - Standardization: min-max
Reimplement  **sklearn.preprocessing.MinMaxScaler**
Parameters:  
  - None
Methods:
  - fit()
  - fit_transform()
  
## Model Evaluation
### Exercise 00 - Mean Squared Error
Reimplement  **sklearn.metrics.mean_squared_error**
Parameters:  
  - y_true: array
  - y_pred: array
