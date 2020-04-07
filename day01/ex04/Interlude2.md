### Linear Algebra Tricks II

If you tried to run your code on a very large dataset, you'd find that it takes a long time to execute! That's because it doesn't use the power of optimized libraries that can perform multiple computations in parallel.

Remember the linear algebra trick of yesterday? Let's use it again!  
If you add a column of ones to the vector $x$, for any example $i$ in our new matrix $X'$.   

$$X' = \begin{bmatrix} 1 & x^{(1)} \\ \vdots & \vdots \\ 1 & x^{(m)}\end{bmatrix}$$

Actually, this transformation is convenient because we can rewrite each $1$ as $x_0^{(i)}$, and each $x^{(i)}$ as $x_1^{(i)}$. Now the $0$ and $1$ indices indicate which component should be multiplied by $\theta_0$ or by $\theta_1$. So now the $X'$ matrix looks like this:

$$X' = \begin{bmatrix} x_0^{(1)} & x_1^{(1)} \\ \vdots & \vdots \\ x_0^{(m)} & x_1^{(m)}\end{bmatrix}$$
  
Why does this matter?  
Well, if we take the equation from the previous exercise:  

$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})
$$
We can multiply it by $1$ without changing anything: 
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)}) \cdot 1
$$
And rewrite $1$ as  $x_0^{(i)}$:
$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_{0}^{(i)}
$$

This means that we found ONE general equation that can be used for both $\nabla(J)_0$ and $\nabla(J)_1$ :
$$
\begin{matrix}
\nabla(J)_j = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_{j}^{(i)} & & \text{ for j = 0, 1}    
\end{matrix}
$$

### Vectorizing the Gradient Calculation

Now it's to learn how to calculate the entire gradient in one short, pretty, linear algebra equation!  
- First, we'll use the $X'$ matrix and our vectorized prediction equation: $h_{\theta}(x)=X'\theta$

$$
\begin{matrix}
\nabla(J)_j = \frac{1}{m} (X'\theta - y)X'_{j} & & \text{ for j = 0, 1}
\end{matrix}
$$
- Second, we need to tweak the equation a bit so that it directly returns a $\nabla(J)$ vector containing both $\nabla(J)_0$ and $\nabla(J)_1$.
$$
\nabla(J) = \frac{1}{m} X'^\mathsf{T}(X'\theta - y)    
$$  

If it does not seems obvious, play a bit with your vectors, on paper and in your code, until you get it. 