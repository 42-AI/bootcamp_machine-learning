# Interlude - Gradient Descent

So far we've calculated the *gradient*, which indicates whether and by how much we should increase or decrease $\theta_0$ and $\theta_1$ in order to reduce the cost.   
What we have to do next is update the theta parameters accordingly, step by step, until we reach the minimum. This iterative process, called **Gradient Descent**, will progressively improve the performance of your regression model on the training data. 

The gradient descent **algorithm** can be summarized like this: for a certain number of cycles, at each step, both $\theta$ parameters are slightly moved in the opposite directions than what the gradient indicates.

The algorithm can be expressed in pseudocode as the following:

$$
\begin{matrix}
&\text{repeat until convergence:} & \{\\
&    \text{compute } \nabla{(J)}  \\
&	\theta_0 := \theta_0 - \alpha \nabla(J)_0  \\ 
&	\theta_1 := \theta_1 - \alpha \nabla(J)_1\\
	\} \hspace{0.5cm} 
\end{matrix}
$$

A few remarks on this algorithm:
- If you directly subtracted the gradient from $\theta$, your steps would be too big and you would quickly overshoot past the minimum. That's why we use $\alpha$ (alpha), called the *learning rate*. It's a small float number (usually between 0 and 1) that decreases the magnitude of each update.
- The pseudocode says "repeat until convergence", but in your implementation, you will not actually check for convergence at each iteration. You will instead set a number of cycles that is sufficient for your gradient descent to converge. 
- When training a linear regression model on a new dataset, you will have to choose appropriate alpha and the number of cycles through trial and error.

