### Multivariate gradient

From our multivariate linear hypothesis we can derive our multivariate gradient:  
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X_i) - y_i)
\nabla(J)_j = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X_i) - y_i)X_{i}^{(j)} \text{ for j = 1, ..., n}
$$

Where:  
- $\nabla(J)$ is a vector of size n * 1,
- $X$ is a matrix of size m * n (i.e. a matrix containing m vectors of dimension n * 1)
- $y$ is a vector of dimension m * 1
- $\theta$ is a vector of dimension n * 1
- $x_i$ is the ith component of vector $x$
- $y_i$ is the ith component of vector $y$
- $\nabla(J)_j$ is the jth component of $\nabla(J)$
- $h_{\theta}(x_i)$ is our prediction for $y_i$: the result of the dot product of the vector $\theta$ and the vector $x_i$  

Therefore, as in the previous day, we can use some linear algebra magic to get a more comptact (and computationally efficient) formula: 

$$
\nabla(J) = \frac{1}{m} X^T(X\theta - y)
$$  

Where:  
- $\nabla(J)$ is a vector of size (n + 1) * 1
- $X$ is a matrix of size m * n 
- $y$ is a vector of size m * 1
- $\theta$ is a vector of size (n + 1) * 1 