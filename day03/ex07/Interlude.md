# Improve

  <img src="../../day00/assets/Improve.png"/>  

### The logistic gradient 
  Given the cost function we selected, we can derive the gradient for the logistic regression as follow: 
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
- $h_{\theta}(x^{(i)})$ is the model's prediction for $y^{(i)}$: the result of  $\text{sigmoid}(\theta \cdot x'^{(i)})$  

This formula should be very familiar to you.  
It is the same as the linear regression gradient!  
The only difference is that $h_{\theta}(x^{(i)})$ correspond to **the logistic regression hypothesis instead of the linear regression hypothesis**.  

In other words:  
$h_{\theta}(x^{(i)}) = \frac{1} {1 + e^{-\theta \cdot x'^{(i)}}}$ instead of $\cancel{h_{\theta}(x^{(i)}) = \theta \cdot x'^{(i)}}$.  