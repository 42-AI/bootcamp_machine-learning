# A simple linear algebra trick

As you know, vectors and matrices can be multiplied to perform linear combinations.  
Let's do a little linear algebra trick to optimize our calculation and use matrix multiplication.  
If we add a column full of ones to our vector of examples $x$, we can create the following matrix: 

$$X' = \begin{bmatrix} 1 & x^{(1)} \\ \vdots & \vdots \\ 1 & x^{(m)}\end{bmatrix}$$
  
We can now get to the same result as in the previous exercise with just a singla multiplication between our brand new $X'$ matrix and the $\theta$ vector!

$$\hat{y} = X' \cdot \theta = \begin{bmatrix} 1 & x^{(1)} \\ \vdots & \vdots \\ 1 & x^{(m)}\end{bmatrix}\cdot\begin{bmatrix}\theta_0 \\ \theta_1 \end{bmatrix} = \begin{bmatrix} \theta_0 + \theta_1 x^{(1)} \\ \vdots \\ \theta_0 + \theta_1 x^{(m)} \end{bmatrix} $$
