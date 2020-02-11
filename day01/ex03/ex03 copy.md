# Exercise 03 - Linear Gradient - iterative version

|                         |                    |
| -----------------------:| ------------------ |
|   Turn-in directory :   |  ex03              |
|   Files to turn in :    |  gradient.py       |
|   Forbidden functions : |  None              |
|   Remarks :             |  n/a               |

**Objective:**

You must implement the following formula as a function:  

$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X_i) - y_i)
\nabla(J)_j = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X_i) - y_i)X_{i}^{(j)} \text{ for j = 1, ..., n}
$$

Where:  
- $\nabla(J)$ is a vector of size n * 1, (this strange symbol : $\nabla$ is called nabla)
- $X$ is a matrix of size m * n (i.e. a matrix containing m vectors of dimension n * 1)
- $y$ is a vector of dimension m * 1
- $\theta$ is a vector of dimension n * 1
- $x_i$ is the ith component of vector $x$
- $y_i$ is the ith component of vector $y$
- $\nabla(J)_j$ is the jth component of $\nabla(J)$
- $h_{\theta}(x_i)$ is our prediction for $y_i$: the result of the dot product of the vector $\theta$ and the vector $x_i$


**Instructions:**
In the gradient.py file create the following function as per the instructions given below:
```python
def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, without any for-loop. The three arrays must have the compatible dimensions.
    Args:
      x: has to be an numpy.ndarray, a matrice of dimension m * n.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a vector n * 1.
    Returns:
      The gradient as a numpy.ndarray, a vector of dimensions n * 1, containg the result of the formula for all j.
      None if x, y, or theta are empty numpy.ndarray.
      None if x, y and theta do not have compatible dimensions.
    Raises:
      This function should not raise any Exception.
    """
```
`
**Examples** 
```python
>>> import numpy as np
>>> X = np.array([
	[ -6,  -7,  -9],
        [ 13,  -2,  14],
        [ -7,  14,  -1],
        [ -8,  -4,   6],
        [ -5,  -9,   6],
        [  1,  -5,  11],
        [  9, -11,   8]])
>>> Y = np.array([2, 14, -13, 5, 12, 4, -19])
>>> Z = np.array([3,0.5,-6])
>>> vec_gradient(X, Y, Z)
array([ -37.35714286,  183.14285714, -393.        ])
>>>
>>> W = np.array([0,0,0])
>>> vec_gradient(X, Y, W)
array([  0.85714286,  23.28571429, -26.42857143])
>>>
>>> vec_gradient(X, X.dot(Z), Z)
array([0., 0., 0.])
```