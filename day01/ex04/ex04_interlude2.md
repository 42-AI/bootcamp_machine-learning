# Interlude - Linear Algebra Tricks II

If you tried to run your code on a very large dataset, you'd find that it takes a long time to execute! That's because it doesn't use the power of Python libraries that are optimized for matrix operations.

Remember the linear algebra trick of yesterday? Let's use it again!  
If you concatenate a column of $1$'s to the left of the $x$ vector, you get what we called matrix $X'$.   

$$
X' = \begin{bmatrix} 1 & x^{(1)} \\ \vdots & \vdots \\ 1 & x^{(m)}\end{bmatrix}
$$

This transformation is very convenient because we can rewrite each $1$ as $x_0^{(i)}$, and each $x^{(i)}$ as $x_1^{(i)}$. So now the $X'$ matrix looks like this:

$$
X' = \begin{bmatrix} x_0^{(1)} & x_1^{(1)} \\ \vdots & \vdots \\ x_0^{(m)} & x_1^{(m)}\end{bmatrix}
$$

Notice that each $x^{(i)}$ example becomes e vector made of $(x^{(i)}_0, x^{(i)}_1)$.  
The $0$ and $1$ indices on the $x$ features correspond to the indices of the $\theta$ parameters with which they will be multiplied.

Why does this matter? Well, if we take the equation from the previous exercise:  

$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})
$$

We can multiply it by $1$ without changing its value:

$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)}) \cdot 1
$$

And rewrite $1$ as $x_0^{(i)}$:

$$
\nabla(J)_0 = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_{0}^{(i)}
$$

This means that now the equation for $\nabla(J)_0$ is no different from the equation we had for $\nabla(J)_1$, so they can both be captured by ONE **generic equation**:

$$
\begin{matrix}
\nabla(J)_j = \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)}) - y^{(i)})x_{j}^{(i)} & & \text{ for j = 0, 1}    
\end{matrix}
$$

And as you probably suspected, a generic equation opens the door to vectorization...

## Vectorizing the Gradient Calculation

Now it's time to learn how to calculate the entire gradient in one short, pretty, linear algebra equation!  
- First, we'll use the $X'$ matrix and our vectorized hypothesis equation: $h_{\theta}(x)=X'\theta$

$$
\begin{matrix}
\nabla(J)_j = \frac{1}{m} (X'\theta - y)X'_{j} & & \text{ for j = 0, 1}
\end{matrix}
$$

- Second, we need to tweak the equation a bit so that it directly returns a $\nabla(J)$ vector containing both $\nabla(J)_0$ and $\nabla(J)_1$.

$$
\nabla(J) = \frac{1}{m} {X'}^T(X'\theta - y)    
$$

If the equation does not seems obvious, play a bit with your vectors, on paper and in your code, until you get it. 

### Notation Remark: 
${X'}^T$ : You might wonder what the $^T$ is for. It means the $X'$ matrix must be **transposed**. Transposing a matrix flips it on its diagonal so that its rows become its columns and vice versa. Here we need to do it so that matrix dimensions are appropriate multiplication and to multiply the right elements together. 

