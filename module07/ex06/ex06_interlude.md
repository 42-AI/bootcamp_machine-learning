# Interlude - Gradient Descent
Now comes the fun part: _gradient descent_!  

The algorithm is not that different from the one used in univariate linear regression. As you might have guessed, what will change is that the $j$ indice needs to run from $0$ to $n$ instead of $0$ to $1$. So all you need is a more generic algorithm, which can be expressed in pseudocode as the following:

$$
\begin{matrix}
\text{repeat until convergence} \hspace{1cm}\{\\
    \text{compute } \nabla{(J)}  \\
	\theta_j := \theta_j - \alpha \nabla(J)_j  \\ 
	\} \hspace{0.5cm} \text{ simultaneously update $\theta$ for $j=0,1,...,n$}  \\ 
    \\
\end{matrix}
$$

If you started to like vectorized forms, you might have noticed that that the $\theta_j$ notation is actually redundant here, since all components of $\theta$ need to be updated simultaneously. $\theta$ is a vector, $\nabla{(J)}$ also, they both have dimension $(n+1) * 1$. So all we need to do is this:  
$$
\begin{matrix}
    &   \text{repeat until convergence} \hspace{1cm} &  \{  \\
    &   \text{compute } \nabla{(J)}  \\
    &	\theta := \theta - \alpha \nabla(J)                 \\ 
\} 
\end{matrix}
$$

Where:
- $\theta$ is the entire parameter vector
- $\alpha$ (alpha) is the learning rate (a small number, usually between 0 and 1)
- $\nabla{(J)}$ is the entire gradient vector

### Note: Do you still wonder why there is a subtraction in the equation?  
By definition, the gradient indicates the direction towards which we should adjust the $\theta$ parameters if we wanted to *increase* the cost. But since our optimization objective is to *minimize* the cost, we move $\theta$ in the opposite direction of the gradient (hence the name *gradient descent*).