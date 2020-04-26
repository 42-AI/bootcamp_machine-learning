# Regularized Gradient

  ![titre](../assets/Improve.png){width=300px}  

To derive the gradient of the regularized cost function, $\nabla(J)$ you have to change a bit the formula of the unregularized gradient.  
Given the fact that we are not penalizing $\theta_0$, the formula will remains the same as before for this parameter. For the other parameters ($\theta_1, \dots, \theta_n$), we must add the partial derivative of the regularization terms: $\lambda \theta_j$.

Therefore, we get:
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)}) \\
\nabla(J)_j = \frac{1}{m}\left(\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} + \lambda \theta_j\right) \text{ for j = 1, ..., n}
$$

Where:  
- $\nabla(J)$ is a vector of dimension (n + 1) * 1, the gradient vector,
- $X$ is a matrix of dimension m * n, the design matrix,
- $y$ is a vector of dimension $m * 1$, the vector of expected values,
- $h_\theta(X)$ is a vector of dimension $m * 1$, the vector of predicted values,
- $x^{(i)}$ is the ith component of $x$ of dimension n * 1,
- $y^{(i)}$ is the ith component of $y$,
- $h_\theta(x^{(i)})$ is the ith component of $h_\theta(X)$,
- $\nabla(J)_j$ is the $j^{th}$ component of $\nabla(J)$,
- $\alpha$ is a constant,
- $\lambda$ is a constant,

Which can be vectorized as:
$$
\nabla(J) = \frac{1}{m} [X'^T(h_\theta(X) - y) + \lambda \theta']
$$  

Where:  
- $\nabla(J)$ is a vector of dimension (n + 1) * 1, the gradient vector,
- $X$ is a matrix of dimension m * n, the design matrix,
- $X'$ is a matrix of dimension m * (n + 1), the design matrix onto which a column of ones is added as a first column,
- $y$ is a vector of dimension m * 1, the vector of expected values,
- $h_\theta(X)$ is a vector of dimension $m * 1$, the vector of predicted values,  
- $\theta$ is a vector of dimension (n + 1) * 1, the parameter vector,
- $\lambda$ is a constant,
- $\theta'$ is a vector of dimension n * 1, constructed using the following rules: 
$$
\begin{matrix}
\theta'_0 & =  0 \\
\theta'_j & =  \theta_j & \text{ for } j = 1, \dots, n\\    
\end{matrix}
$$

## Linear Gradient vs Logistic Gradient

As before, **the only difference between the gradient of the linear and the logistic regression is** $h_\theta(X)$.  

- In the linear regression: $h_\theta(X) = X'\theta$ 
- In the logistic regression: $h_\theta(X) = \text{sigmoid}(X'\theta)$