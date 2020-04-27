# Fighting overfitting... enter Regularization

  ![titre](../assets/Evaluate.png){width=300px}  

In the **day02**, we talked about the problem of overfitting and how to be able to detect it by splitting the dataset into a **training set** and a **test set**.  

However, being able to detect overfitting does not mean being able to avoid it.  

To do so, we are now introducing an important new notion: the **regularization**.

The idea beahind regularization is to **penalize the model for putting too much weight on certain** (usually heavy polynomials) **features**.  

$$
\text{regularized cost function} = \text{cost function} + \frac{\lambda}{2m} \sum_{j = 1}^n \theta_j^2
$$

By doing so, **we are encouraging the model to keep its** $\theta$ **values as small as possible**. Indeed, the values of $\theta$ are now took into account to calculate the loss function of the model.  

$\lambda$ (called 'lambda') is the parameter wich will directly determine how much we want the reglarization to drive the model's construction.  
- If $\lambda = 0$, we are in the case usual models we built until now: there is no regularization.
- If $\lambda$ is very big, it will drive all the $\theta$ to be $0$.

You can see that we are starting the sum at $j = 1$, because we do not want to penalize the value of $\theta_0$, corresponding to the y-intercept.

## Be carefull!  
Machine Learning is essentially done by computer scientists (not mathematicians) which tends to be sometimes a bit messy in the way they represent things mathematically.  
For example: the fact we are using the notation $\theta_0$ to represent the y-intercept makes things easy fo applying linear algebra tricks, **but** it completly messed the overall matrix notation!  

According to that notation, the matrix $X'$ has the following properties: 
* its row index, $x'^{(i)}$, use the mathematical indexing: starting at 1.
* its column index, $x'_j$, use the computer indexing: starting at 0. 

$$
X' =
\underbrace{
\begin{bmatrix}
1 & x_1^{(1)} & \dots & x_n^{(1)} \\
\vdots & \vdots & \ddots & \vdots \\ 
1 & x_1^{(m)} & \dots & x_n^{(m)} \\ 
\end{bmatrix}  
}_{\begin{matrix}
    j = 0, \dots, n
\end{matrix}}
=     


\left .
\begin{bmatrix}
x_0^{(1)} & x_1^{(1)} & \dots & x_n^{(1)} \\
\vdots & \vdots & \ddots & \vdots \\ 
x_0^{(m)} & x_1^{(m)} & \dots & x_n^{(m)} \\ 
\end{bmatrix}
\right \} i = 1, \dots, m
$$

## Terminology:
The kind of regularization we are introducing here is named $L_2 \text{ regularization}$, because it add the squared $L_2 \text{ norm}$ of the vector $\theta$ to the cost function.  
The $L_2 \text{ norm}$ of a given vector $x$, written
$$
L_2(x) = ||x||_2 = \sqrt{\sum_i x_i^2 } \\
L_2(x)^2 = ||x||_2^2 = \sum_i x_i^2  \\

$$ 
is its **euclidean norm** (i.e. the sum of the components squared).  

It exists an infinite number of norms which could be used as regularization terms, and which leads to different kinds of results. Here, we will use only $L_2$, which is the most commonly used.

## Our old friend vectorization ...

It is not a surprise, we can use vectorization to calculate $L_2(x)^2$ more efficiently. It could be a good exercise for you to try to find by yourself how to do it. We suggest you to think by yourself about it and to check the answer on the next page.
