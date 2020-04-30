# Interlude - Regularized Gradient

![The Learning Cycle - Improve](../assets/Improve.png){width=300px}  

To derive the gradient of the regularized cost function, $\nabla(J)$ you have to change a bit the formula of the unregularized gradient.  
Given the fact that we are not penalizing $\theta_0$, the formula will remain the same as before for this parameter. For the other parameters ($\theta_1, \dots, \theta_n$), we must add the partial derivative of the regularization term: $\lambda \theta_j$.

Therefore, we get:
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})
$$
$$
\nabla(J)_j = \frac{1}{m}\left(\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} + \lambda \theta_j\right) \text{ for j = 1, ..., n}
$$

Where:  
- $\nabla(J)_j$ is the $j^{th}$ component of the gradient vector $\nabla(J)$,
- $m$ is the number of training examples used,
- $h_\theta(x^{(i)})$ is the model's prediction for the $i^{th}$ training example,
- $x^{(i)}$ is the feature vector of the $i^{th}$ training example,
- $y^{(i)}$ is the expected target value for the $i^{th}$ example,
- $\lambda$ is a constant, the regularization hyperparameter
- $\theta_j$ is the $j^{th}$ parameter of the $\theta$ vector,

Which can be vectorized as:
$$
\nabla(J) = \frac{1}{m} [X'^T(h_\theta(X) - y) + \lambda \theta']
$$  

Where:  
- $\nabla(J)$ is a vector of dimension $(n + 1) * 1,$ the gradient vector,
- $m$ is the number of training examples used,
- $X$ is a matrix of dimension $m * n$, the design matrix,
- $X'$ is a matrix of dimension $m * (n + 1)$, the design matrix onto which a column of ones is added as a first column,
- $y$ is a vector of dimension $m * 1$, the vector of expected values,
- $h_\theta(X)$ is a vector of dimension $m * 1$, the vector of predicted values, 
- $\lambda$ is a constant, 
- $\theta$ is a vector of dimension $(n + 1) * 1$, the parameter vector,
- $\theta'$ is a vector of dimension $n * 1$, constructed using the following rules: 

$$
\begin{matrix}
\theta'_0 & =  0 \\
\theta'_j & =  \theta_j & \text{ for } j = 1, \dots, n\\    
\end{matrix}
$$

## Linear Gradient vs Logistic Gradient

As before, we draw your attention on the only difference between linear regression and logistic regression's gradient equations: **the hypothesis function** $h_\theta(X)$.  

- In the linear regression: $h_\theta(X) = X'\theta$ 
- In the logistic regression: $h_\theta(X) = \text{sigmoid}(X'\theta)$