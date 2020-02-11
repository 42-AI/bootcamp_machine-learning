### Linear Algebra tricks II

Remember the linear algebra trick of yesterday? Lets use it again! 
If you add a column of ones to the vector $x$, for any example i in our new matrix X', $X_{i}^{(0)} = 1$.  
  
Therefore:  
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X'_i) - y_i)
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X'_i) - y_i)\cdot 1 
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X'_i) - y_i)X'_{i}^{(0)}
$$

This means that you can encapsulate the gradient for both $\theta_0$ and $\theta_1$ with the same calculation! 
$$
\nabla(J)_j = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(X_i) - y_i)X_{i}^{(j)} \text{ for j = 1, 2}
$$

And thus (using more linear algebra):  

$$
\nabla(J)_j = \frac{1}{m} (X\theta - y)X^{(j)} \text{ for j = 1, 2}
\nabla(J) = \frac{1}{m} X^T(X\theta - y)
$$  

If it does not seems obvious, play a bit with your vectors until you get it. 