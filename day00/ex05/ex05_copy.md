# Exercise 05 - Prediction with mutiple variables

|                         |                    |
| -----------------------:| ------------------ |
|   Turn-in directory :   |  ex05              |
|   Files to turn in :    |  prediction.py     |
|   Forbidden functions : |  None              |
|   Remarks :             |  n/a               |

**Objective:**
You must implement the following formula as a function:  

$$\hat{y} = X \cdot \theta = 
&
\begin{bmatrix} 
1 & x_{1}^{(1)} & \dots & x_{1}^{(n)}\\
\vdots & \vdots & \ddots & \vdots\\
1 & x_{m}^{(1)} & \dots & x_{m}^{(n)}\end{bmatrix}
\cdot
\begin{bmatrix}
\theta_0 \\ 
\theta_1 \\
\vdots \\
\theta_n
\end{bmatrix} 
&
= 
\begin{bmatrix} 
\theta_0 + \theta_{1} x_{1}^{(1)} + \dots + \theta_{n} x_{1}^{(n)}\\ 
\vdots \\ 
\theta_0 + \theta_{1} x_{m}^{(1)} + \dots + \theta_{n} x_{m}^{(n)}
\end{bmatrix} $$
  

Be careful: 
- the x you will get as an input is a m * n matrix 
- theta is an (n + 1) * 1 vector. 

You have to transform x into X to fit the dimension of theta!


**Instructions:**
In the prediction.py file create the following function as per the instructions given below:
```python
def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * n.
      theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
      y_hat as a numpy.ndarray, a vector of dimension m * 1.
      None if x or theta are empty numpy.ndarray.
      None if x or theta dimensions are not appropriate.
    Raises:
      This function should not raise any Exception.
    """
```

**Examples**

```python
import numpy as np
x = np.arange(1,6)

#Example 1:
theta1 = np.array([5, 0])
predict_(x, theta1)
# Ouput:
array([5., 5., 5., 5., 5.])
# Do you remember why y_hat contains only 5 here?  


#Example 2:
theta2 = np.array([0, 1])
predict_(x, theta2)
# Output:
array([1., 2., 3., 4., 5.])
# Do you remember why y_hat == x here?  


#Example 3:
theta3 = np.array([5, 3])
predict_(X, theta3)
# Output:
array([ 8., 11., 14., 17., 20.])


#Example 4:
theta4 = np.array([-3, 1])
predict_(x, theta4)
# Output:
array([-2., -1.,  0.,  1.,  2.])
```
