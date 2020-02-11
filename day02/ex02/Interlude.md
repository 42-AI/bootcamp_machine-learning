## To the multivariate universe and beyond!

Until now we used only very simple hypothesis: $h_{\theta}(x) = \theta_0 + \theta_1 x$. From this very simple hypothesis we have find a way to evaluate and improve our initial hypothesis.   
But we are living a complex world, full of complex phenomenons.  
How to build a model where more than one parameter (or even thousands of parameters) are involved?  
Such cases are called **multivariate models**. We are going to study them today.  


### Predict 
<img src="day00/assets/Predict.png" />  

#### The examples as a m * n matrix
The first thing is to consider our training examples. If x was a vector of dimensions m * 1, it should now become a matrix of dimension m * n, where n is the number of parameters (sometimes called **features**) we want to use in our model.   
$$
X = \begin{bmatrix} 
X_{1}^{(1)} & \dots & X_{1}^{(n)}\\
\vdots & \ddots & \vdots\\
X_{m}^{(1)} & \dots & X_{m}^{(n)}\end{bmatrix}
$$

Where:
- $X_i$ is the *ith* row of our matrix X, a vector of dimension n * 1
- $X^{(i)}$ is the *ith* column of our matrix X, a vector of dimension m * 1
- $X_i^{(j)}$ is the intersection of the *ith* row and the *jth* column of our matrix X, a real number
  

#### The multivariate hypothesis
Then, we must update our hypothesis to take more than one parameter into account. 

$$
\hat{y}_i = \theta_0 + \theta_1 X_{i}^{(1)} + \dots + \theta_n X_{i}^{(n)} \text{ for i = 1, ..., m}
$$  

Where:
- $X$ is a matrix of dimension m * n, the matrix of examples
- $\hat{y}$ is a vector of dimension m * 1, the vector of predicted values
- $\theta$ is a vector of dimension (n + 1) * 1, the vector of parameters
  

