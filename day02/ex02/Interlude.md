## To the multivariate universe and beyond!

Until now we used only very simple hypothesis: $h_{\theta}(x) = \theta_0 + \theta_1 x$.  
From this very simple hypothesis we found a way to evaluate and improve our initial hypothesis.   
But we are living a complex world, full of complex phenomenons.  
How to build a model where more than one parameter (or even thousands of parameters) are involved?  
Such cases are called **multivariate models**. We are going to study them today.  


### Predict 
<img src="../assets/Predict.png" />  

#### The examples as a m * n matrix
The first thing is to consider our training examples. If x was a vector of dimensions m * 1, it should now become a matrix of dimension m * n, where n is the number of parameters (sometimes called **features**) we want to use in our model.   
$$
X = \begin{bmatrix} 
x_{1}^{(1)} & \dots & x_{n}^{(1)}\\
\vdots & \ddots & \vdots\\
x_{1}^{(m)} & \dots & x_{n}^{(m)}\end{bmatrix}
$$

Where:
- $x^{(i)}$ is the *ith* row of our matrix $X$
- $x_{j}$ is the *jth* column of our matrix X
- $x_{j}^{(i)}$ is the intersection of the *ith* row and the *jth* column of our matrix X, a real number
  

#### The multivariate hypothesis
Then, we must update our hypothesis to take more than one parameter into account. 

$$
\begin{matrix}
\hat{y}_i = \theta_0 + \theta_1 x_{1}^{(i)} + \dots + \theta_n x_{n}^{(i)} & & \text{ for i = 1, ..., m}    
\end{matrix}
$$  

Where:
- $X$ is a matrix of dimension m * n, the matrix of examples
- $\hat{y}$ is a vector of dimension m * 1, the vector of predicted values
- $\theta$ is a vector of dimension (n + 1) * 1, the vector of parameters
  

