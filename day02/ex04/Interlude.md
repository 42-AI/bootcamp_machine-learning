### Improve 

<img src="day00/assets/Predict.png" />  

#### Multivariate gradient

From our multivariate linear hypothesis we can derive our multivariate gradient:  
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}X^{(i)} - y^{(i)}) \\
\nabla(J)_j = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X^{(i)} - y^{(i)})X_{j}^{(i)} \text{ for j = 1, ..., n}
$$

Where:  
- $\nabla(J)$ is a vector of size (n + 1) * 1,
- $X$ is a matrix of dimension m * n, the matrix of examples
- $y$ is a vector of dimension m * 1
- $\theta$ is a vector of dimension n * 1
- $X^{(i)}$ is the ith column of matrix $X$, a vector of dimension m * 1
- $y^{(i)}$ is the ith component of vector $y$
- $\nabla(J)_j$ is the jth component of $\nabla(J)$
- $h_{\theta}(X^{(i)})$ is our prediction for $y^{(i)}$: the result of the dot product of the vector $\theta$ and the vector $X^{(i)}$  

Therefore, as in the previous days, we can use some linear algebra magic to get a more comptact (and computationally efficient) formula: 

$$
\nabla(J) = \frac{1}{m} X'^T(X'\theta - y)
$$  

Where:  
- $\nabla(J)$ is a vector of size (n + 1) * 1
- $X$ is a matrix of dimension m * n, the matrix of examples
- $X'$ is a matrix of dimension m * (n + 1), the matrix of examples onto which a column of ones is added as first column
- $y$ is a vector of size m * 1
- $\theta$ is a vector of size (n + 1) * 1 