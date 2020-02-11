## Introducting polynomial models

### Polynomial hypothesis
Being able to handle multivariate linear regression allows us to manipulate polynomial features and then create polynomial hypothesis. 

Polynomial hypothesis look like this: 
$$
\hat{y}_i = \theta_0 + \theta_1 x  +\theta_2 x^{2} + \dots + \theta_n x^{n}
$$  

In the above formula, the same parameter $x_i$ is duplicated and raised to some power. This allows more complex hypothesis to be represented.  
Sometimes (often?) the relationship between the variables is not linear.  
  
For example, the predicted variable could be better represented by a formula such as $\hat{y}_i = 17 -  3x  + 5 x^{2}$.

In order to do polynomial models, you have to add more columns to your dataset. Each new column contains a version of your original vector raised to some given power. 