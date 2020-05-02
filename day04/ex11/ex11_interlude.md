# Interlude - Regularized Logistic Regression is still Logistic Regression

As opposed to linear regression, **regularized logistic regression is still called logistic regression**.  

Working without regularization parameters can be considered simply as a special case where $\lambda = 0$. 

$$
\begin{matrix}
\text{if } \lambda = 0 \text{: }\\
\nabla(J) & = & \frac{1}{m} [X'^T(h_\theta(X) - y) + \lambda \theta'] \\
\\
& = & \frac{1}{m} [X'^T(h_\theta(X) - y) + 0 \cdot \theta'] \\
\\
& = & \frac{1}{m} [X'^T(h_\theta(X) - y)]    
\end{matrix}
$$  