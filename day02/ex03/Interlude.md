## Even more linear algebra tricks!

As you already did before for the univariate hypothesis, the multivariate hypothesis can be vectorized as well.  

If you add a column of ones as first column of the $X$ matrix, you got the $X'$ matrix.  
Then, you can calculate $\hat{y}$ with a simple product between $X'$ and $\theta$.

$$\hat{y} = X' \cdot \theta = 
\begin{bmatrix} 
1 & X_{1}^{(1)} & \dots & X_{1}^{(n)}\\
\vdots & \vdots & \ddots & \vdots\\
1 & X_{m}^{(1)} & \dots &  X_{m}^{(n)}\end{bmatrix}
\cdot
\begin{bmatrix}
\theta_0 \\ 
\theta_1 \\
\vdots \\
\theta_n
\end{bmatrix} 
= 
\begin{bmatrix} 
\theta_0 + \theta_{1} X_{1}^{(1)} + \dots + \theta_{n} X_{1}^{(n)}\\ 
\vdots \\ 
\theta_0 + \theta_{1} x_{m}^{(1)} + \dots + \theta_{n} X_{m}^{(n)}
\end{bmatrix} $$