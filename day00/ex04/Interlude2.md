# A simple linear algebra trick

Let's do a little linear algebra trick to optimize 
If we add a column full of ones to our vector of examples $x$ we can create the following matrix: 

$$X' = \begin{bmatrix} 1 & x_1 \\ \vdots & \vdots \\ 1 & x_m\end{bmatrix}$$
  
We can now get exactly the same result as in the previous exercise using only a product between our brand new $X'$ matrix and the $\theta$ vector!

$$\hat{y} = X' \cdot \theta = \begin{bmatrix} 1 & x_1 \\ \vdots & \vdots \\ 1 & x_m\end{bmatrix}\cdot\begin{bmatrix}\theta_0 \\ \theta_1 \end{bmatrix} = \begin{bmatrix} \theta_0 + \theta_1 x_1 \\ \vdots \\ \theta_0 + \theta_1 x_m \end{bmatrix} $$
