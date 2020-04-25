# Exercise 06 - Regularized Logistic Gradient

|                         |                    |
| -----------------------:| ------------------ |
|   Turn-in directory :   |  ex06              |
|   Files to turn in :    |  reg_logistic_grad.py|
|   Authorized modules :  |  Numpy             |
|   Forbidden modules :   |  sklearn           |

# Objectives
You must implement the following formula as a function:  
### I - Iterative:
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)}) \\
\nabla(J)_j = \frac{1}{m}\left(\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_j^{(i)} + \lambda \theta_j\right) \text{ for j = 1, ..., n}
$$

Where:  
- $\nabla(J)$ is a vector of dimension (n + 1) * 1, the gradient vector,
- $X$ is a matrix of dimension m * n, the design matrix,
- $y$ is a vector of dimension m * 1
- $x^{(i)}$ is the ith component of $x$ of dimension n * 1
- $y^{(i)}$ is the ith component of $y$
- $\nabla(J)_j$ is the $j^{th}$ component of $\nabla(J)$
- $h_{\theta}(x^{(i)})$ corresponds to the model's prediction of $y^{(i)}$: **the logistic prediction**.
- $\alpha$ is a constant
- $\lambda$ is a constant

### II - Vectorized:
$$
\nabla(J) = \frac{1}{m} [X'^T(h_\theta(X) - y) + \lambda \theta']
$$  

Where:  
- $\nabla(J)$ is a vector of dimension (n + 1) * 1, the gradient vector,
- $X$ is a matrix of dimension m * n, the design matrix,
- $X'$ is a matrix of dimension m * (n + 1), the design matrix onto which a column of ones is added as a first column,
- $\theta$ is a vector of dimension (n + 1) * 1, the parameter vector,


FINISH HERE
- $h_\theta(X)$ IS
  



- $y$ is a vector of dimension m * 1, the vector of expected values,
- $\lambda$ is a constant,
- $\theta'$ is a vector of dimension n * 1, constructed using the following rules: 
$$
\begin{matrix}
\theta'_0 & =  0 \\
\theta'_j & =  \theta_j & \text{ for } j = 1, \dots, n\\    
\end{matrix}
$$
## Instructions:
In the reg_logistic_grad.py file create the following function as per the instructions given below:
```python
def reg_logistic_grad(y, x, theta, lambda_):
    """Computes the regularized linear gradient of three non-empty numpy.ndarray, with two for-loop. The three arrays must have compatible dimensions.
    Args:
      y: has to be a numpy.ndarray, a vector of dimension m * 1.
      x: has to be a numpy.ndarray, a matrix of dimesion m * n.
      theta: has to be a numpy.ndarray, a vector of dimension n * 1.
      lambda_: has to be a float.
    Returns:
      A numpy.ndarray, a vector of dimension n * 1, containing the results of the formula for all j.
      None if y, x, or theta are empty numpy.ndarray.
      None if y, x or theta does not share compatibles dimensions.
    Raises:
      This function should not raise any Exception.
    """
```

**Examples**
```python
>>> X = np.array([
      	[ -6,  -7,  -9],
        [ 13,  -2,  14],
        [ -7,  14,  -1],
        [ -8,  -4,   6],
        [ -5,  -9,   6],
        [  1,  -5,  11],
        [  9, -11,   8]])
>>> Y = np.array([1,0,1,1,1,0,0])
>>> Z = np.array([1.2,0.5,-0.32])
>>> reg_logistic_grad(Y, X, Z, 1)
array([ 6.69780169, -0.33235792,  2.71787754])
>>> reg_logistic_grad(Y, X, Z, 0.5)
array([ 6.61208741, -0.3680722,   2.74073468])
>>> reg_logistic_grad(Y, X, Z, 0.0)
array([ 6.52637312, -0.40378649,  2.76359183])
```
