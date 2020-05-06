# Interlude - Answers to the Vectorization Problem

So, how do you vectorize the following? 

$$
\sum_{i = j}^n \theta_j^2
$$ 

It's very similar to a **dot product** of $\theta$ with itself.  
The only problem here is to find a way to not take $\theta_0$ into account.  

Let's construct a vector $\theta'$ with the following rules : 
$$
\begin{matrix}
\theta'_0 & = 0 &\\
\theta'_j & =  \theta_j & \text{ for } j = 1, \dots, n\\    
\end{matrix}
$$

In other words: 
$$
\\
\theta' = \begin{bmatrix}
  0 \\
  \theta_1 \\
  \vdots \\
  \theta_n
\end{bmatrix}
$$

This way, we can perform the dot product without having $\theta_0$ interfering in our calculations: 

$$
\begin{matrix}
\theta' \cdot \theta' & = & 
\begin{bmatrix}
  0 \\
  \theta_1 \\
  \vdots \\
  \theta_n
\end{bmatrix} \cdot \begin{bmatrix}
  0 \\
  \theta_1 \\
  \vdots \\
  \theta_n
\end{bmatrix} \\ 
\\
& = & 0 \cdot 0 + \theta_1 \cdot \theta_1 + \dots + \theta_n \cdot \theta_n \\ 
\\
& = & \sum_{j= 1}^n \theta_j^2
\end{matrix}
$$