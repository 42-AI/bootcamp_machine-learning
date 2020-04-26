## Vectorized Logistic Gradient 

Given the previous logistic gradient formula, it is quite easy to produce a vectorized version.  

Actually, you almost already implemented it on day02!  

As with the previous exercice, **the only thing you have to change is your hypothesis** in order to calculate your logistic gradient.  

$$
\begin{matrix}
\nabla(J)_0 &  = &\frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)}) & \\
\nabla(J)_j & = &\frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_{j}^{(i)} & \text{ for j = 1, ..., n}    
\end{matrix}
$$

Can be vectorized as:

$$
\nabla(J) = \frac{1}{m} X'^T(h_\theta(X) - y)
$$  
