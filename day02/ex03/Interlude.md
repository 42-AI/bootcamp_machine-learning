## Even More Linear Algebra Tricks!

As you already did before with the univariate hypothesis, the multivariate hypothesis can be vectorized as well.  

If you add a column of ones as the first column of the $X$ matrix, you got the $X'$ matrix.  
Then, you can calculate $\hat{y}$ with a simple product between $X'$ and $\theta$.

$$X' \cdot \theta = 
\begin{bmatrix} 
1 & x_{1}^{(1)} & \dots & x_{n}^{(1)}\\
\vdots & \vdots & \ddots & \vdots\\
1 & x_{1}^{(m)} & \dots &  x_{n}^{(m)}\end{bmatrix}
\cdot
\begin{bmatrix}
\theta_0 \\ 
\theta_1 \\
\vdots \\
\theta_n
\end{bmatrix} 
= 
\begin{bmatrix} 
\theta_0 + \theta_{1} x_{1}^{(1)} + \dots + \theta_{n} x_{n}^{(1)}\\ 
\vdots \\ 
\theta_0 + \theta_{1} x_{1}^{(m)} + \dots + \theta_{n} x_{n}^{(m)}
\end{bmatrix}
=
\begin{bmatrix}
\hat{y}^{(1)} \\ 

\vdots \\
\hat{y}^{(m)}
\end{bmatrix} 
=
\hat{y} $$

Another way of understanding this is that we created a fake $x_0$ that is always equal to $1$. This facilitates the calculations because now, each $x_j$ feature has its corresponding $\theta_j$ parameter in the matrix multiplication.