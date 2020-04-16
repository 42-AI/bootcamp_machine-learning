# Improve 

<img src="../../day00/assets/Improve.png" />  

## Multivariate Gradient

From our multivariate linear hypothesis we can derive our multivariate gradient. It looks a lot like the one we saw yesterday, but instead of having just two components, the gradient now has as many as there are parameters. This means that now we need to calculate $\nabla(J)_0,\nabla(J)_1,\dots,\nabla(J)_n$  

If we take the univariate equations we used yesterday and replace the formula for $\nabla(J)_1$ by a more general $\nabla(J)_j$, we get the following:
$$
\begin{matrix}
\nabla(J)_0 &  = &\frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)}) & \\
\nabla(J)_j & = &\frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_{j}^{(i)} & \text{ for j = 1, ..., n}    
\end{matrix}
$$

Where:  
- $\nabla(J)$ is a vector of size $(n + 1) * 1$,
- $\nabla(J)_j$ is the $j^{th}$ component of $\nabla(J)$
- $X$ is a matrix of dimension $m * n$, the design matrix
- $y$ is a vector of dimension $m * 1$
- $\theta$ is a vector of dimension $(n+1) * 1$, the parameter vector
- $x^{(i)}$ is the $i^{th}$ row of the $X$ matrix, a vector of dimension $m * 1$
- $y^{(i)}$ is the $i^{th}$ component of vector $y$
- $h_{\theta}(x^{(i)})$ is the model's prediction for $y^{(i)}$: the result of  $\theta^T \cdot x^{(i)}$  


### Vectorized Form

As usual, we can use some linear algebra magic to get a more comptact (and computationally efficient) formula: 

$$
\nabla(J) = \frac{1}{m} X'^T(X'\theta - y)
$$  

Where:  
- $\nabla(J)$ is the gradient vector of size $(n + 1) * 1$
- $X'$ is a matrix of dimension $m * (n + 1)$, the design matrix onto which a column of ones is added as the first column
- $X'^T$ means the matrix has been transposed
- $\theta$ is a vector of size $(n + 1) * 1$ 
- $y$ is a vector of size $m * 1$

The vectorized equation can output the entire gradient vector all at once, in one calculation! So if you understand the linear algebra operations, you can forget about the equations we presented at the top of the page and just use the vectorized one.