# Interlude - A Simple Linear Algebra Trick

As you know, vectors and matrices can be multiplied to perform linear combinations.  
Let's do a little linear algebra trick to optimize our calculation and use matrix multiplication.  
If we add a column full of $1$'s to our vector of examples $x$, we can create the following matrix: 

$$
X' = \begin{bmatrix} 1 & x^{(1)} \\ \vdots & \vdots \\ 1 & x^{(m)}\end{bmatrix}
$$
  
We can then rewrite our hypothesis as: 

$$
\hat{y}^{(i)} = \theta \cdot x'^{(i)} = \begin{bmatrix}\theta_0 \\ \theta_1 \end{bmatrix}  \cdot \begin{bmatrix} 1 & x^{(i)} \end{bmatrix} = \theta_0 + \theta_1 x^{(i)}
$$

Therefore, the calculation of each $\hat{y}^{(i)}$can be done with only one vector multiplication. 

But we can even go further, by calculating the whole $\hat{y}$ vector in one operation: 

$$
\hat{y} = X' \cdot \theta = \begin{bmatrix} 1 & x^{(1)} \\ \vdots & \vdots \\ 1 & x^{(m)}\end{bmatrix}\cdot\begin{bmatrix}\theta_0 \\ \theta_1 \end{bmatrix} = \begin{bmatrix} \theta_0 + \theta_1 x^{(1)} \\ \vdots \\ \theta_0 + \theta_1 x^{(m)} \end{bmatrix}
$$

We can now get to the same result as in the previous exercise with just a single multiplication between our brand new $X'$ matrix and the $\theta$ vector!

## A Note on Notation:
In further Interludes, we will use the following convention:  
- Capital letters represent matrices (e.g.: $X'$)
- Lower case letters represent vectors and scalars (e.g.: $x^{(i)}$, $y$)