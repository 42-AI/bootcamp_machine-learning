## Gradient Descent

We calculated the *gradient*, which indicates whether we should increase or decrease $\theta_0$ and $\theta_1$ in order to reduce the cost.   
What we have to do next is to move the theta parameters accordingly, step by step, until we reach the minimum. This iterative process is called **Gradient Descent**. It is a very common way to improve the performance of Machine Learning models. 


More specifically, linear gradient descent is an iterative algorithm whereby at each step, $\theta$ is slightly moved in the opposite direction of the gradient.

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
- Here, $\alpha$ (alpha) is what we call the *learning rate*. It is a small number (usually between 0 and 1) that you will need to decrease the size of your steps and avoid overshooting getting *past* the minimum.
- In your implementation, you will not directly verify whether convergence has been reached at each iteration. You will instead set a number of cycles that is sufficiently large for your gradient descent to converge.

### Helpful ressources: 
- **Parameter learning section:** https://www.coursera.org/learn/machine-learning/home/week/1

