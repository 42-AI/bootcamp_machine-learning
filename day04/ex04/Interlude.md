# Fighting overfitting... enter Regularisation. 

In the **day02**, we talked about the problem of overfitting and how to be able to detect it by splitting the dataset into a **training set** and a **test set**.  

However, being able to detect overfitting does not mean being able to avoid it.  

To do so, we are now introducing an important new notion: the **regularization**.

The idea beahind regularization is to **penalize the model for putting too much weight on certain** (usually heavy polynomials) **features**.  

$$
\text{regularized cost function} = \text{cost function} + \lambda \sum_{j = 2}^n \theta_j^2
$$

By doing so, **we are encouraging the model to keep its** $\theta$ **values as small as possible**. Indeed, the values of $\theta$ are now took into account to calculate the loss function of the model.  
$\lambda$ (called 'lambda') is the parameter wich will directly determine how much we want the reglarization to drive the model's construction.  
- If $\lambda = 0$, we are in the case usual models we built until now: there is no regularization.
- If $\lambda$ is very big, it will drive all the $\theta$ to be $0$.