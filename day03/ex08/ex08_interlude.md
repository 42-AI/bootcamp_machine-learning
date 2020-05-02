# Interlude -  Vectorized Logistic Gradient 

Given the previous logistic gradient formula, it's quite easy to produce a vectorized version.  

Actually, you almost already implemented it on day02!  

As with the previous exercice, **the only thing you have to change is your hypothesis** in order to calculate your logistic gradient.  

$$
\begin{matrix}
\nabla(J)_0 &  = &\cfrac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)}) & \\
\nabla(J)_j & = &\cfrac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_{j}^{(i)} & \text{ for j = 1, ..., n}    
\end{matrix}
$$

## Vectorized Version

Can be vectorized the same way as you did before:

$$
\nabla(J) = \cfrac{1}{m} X'^T(h_\theta(X) - y)
$$  
