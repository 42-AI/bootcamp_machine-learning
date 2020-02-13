# Exercise 03 - Vectorized Logistic Loss Function

|                         |                         |
| -----------------------:| ----------------------- |
|   Turn-in directory :   |  ex03                   |
|   Files to turn in :    |  vec_log_loss.py        |
|   Forbidden functions : |  None                   |
|   Remarks :             |  n/a                    |

## Objectives:

Now that you understood how we can calculate the loss, you will see how to do it with vectorized operations.
The goal of this exercise is to produce the same result as in ex01 but this time you will use numpy ndarrays.

You must implement the following formula as a function:  

$$
J( \theta) = -\frac{1} {m} \lbrack y \cdot log(h) + (1 - y) \cdot log(1 - h)\rbrack
$$

Where:  
* $J( \theta)$ is the cost function with theta being the weights.
* $m$ is the length of $y$, i.e. the number of observations in our sample.
* $h$ also called y_pred or y_hat, is the calculated hypothesis and it represents the vector of predicted outputs (cf ex01).
* $y$, also called y_true, represents the vector of desired outputs, either 1 or 0.

## Instructions:

In the vec_log_loss.py file create the following function as per the instructions below: 
```python
def vec_log_loss_(x, y, theta, eps=1e-15):
    """
    Compute the logistic loss value.
    Args:
        x: has to be an numpy.ndarray, a matrice of dimension m * n.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector (n + 1) * 1.
        eps: epsilon (default=1e-15)
    Returns:
        The logistic loss value as a float.
        None on any error.
    Raises:
        This function should not raise any Exception.
    """
```

N.B: you might want to update your sigmoid function to work with numpy ndarrays ;) !

## Examples:
```python
from sigmoid import sigmoid_
from log_loss import log_loss_

# Example 1:
x1 = 4
y1 = 1
theta1 = 0.5
vec_log_loss_(x1, y1, theta1)
# Output:
0.12692801104297152

# Example 2:
x2 = [1, 2, 3, 4]
y2 = 0
theta2 = [-1.5, 2.3, 1.4, 0.7]
vec_log_loss_(x2, y2, theta2)
# Output:
10.100041078687479

# Example 3:
x3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
y3_true = [1, 0, 1]
theta3 = [-1.5, 2.3, 1.4, 0.7]
vec_log_loss_(x3, y3, theta3)
# Output:
7.233346147374828
```

