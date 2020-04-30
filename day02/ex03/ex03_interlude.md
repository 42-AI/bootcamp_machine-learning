# Interlude - Even More Linear Algebra Tricks!

As you already did before with the univariate hypothesis, the multivariate hypothesis can be vectorized as well.  

If you add a column of $1$'s as the first column of the $X$ matrix, you get what we'll call the $X'$ matrix.  
Then, you can calculate $\hat{y}$ by multiplying $X'$ and $\theta$.

$$
X' \cdot \theta = 
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
\hat{y}
$$

Another way of understanding this algebra trick is to pretend that each training example has an artificial $x_0$ feature that is always equal to $1$. This simplifies the equations because now, each $x_j$ feature has its corresponding $\theta_j$ parameter in the multiplication.

$$
\theta_0x_0^{(i)} + \theta_{1} x_{1}^{(i)} + \dots + \theta_{n} x_{n}^{(i)} = \theta \cdot x'^{(i)}
$$