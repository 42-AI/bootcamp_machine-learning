# Interlude - To the Multivariate Universe and Beyond!

Until now we've used a very simple hypothesis: $h_{\theta}(x) = \theta_0 + \theta_1 x$  
With this very simple hypothesis we found a way to evaluate and improve our predictions.  

That's all very neat, but we live in a world full of complex phenomena that a model using this hypothesis would fail miserably at predicting. If we take weather forecasting for example, how easy do you think it would be to predict tomorrow's temperature with just one variable (say, the current atmospheric pressure)? A model based on just one variable is too simple to account for the complexity of this phenomenon.  

 Now what if, on top of the atmospheric pressure, we could take into account the current temperature, humidity, wind, sunlight, and any useful information we can get our hands on?

We'd need a model where more than one variable (or even thousands of variables) are involved. That's what we call a **multivariate model**. And that's today's topic!  


## Predict

![The Learning Cycle - Predict](../assets/Predict.png){width=400px}  

## Representing the examples as an m * n matrix
First we need to reconsider how we represent the training examples.  Now that we want to characterize each training example with not just one, but many variables, we need more than a vector. We need a __matrix__!  

So instead of an $x$ vector of dimension $m * 1$, we now have a matrix of dimension $m * n$, where $n$ is the number of **features** (or variables) that characterize each training example. We call it the **design matrix**, denoted by a capital $X$.   

$$
X = \begin{bmatrix} 
x_{1}^{(1)} & \dots & x_{n}^{(1)}\\
\vdots & \ddots & \vdots\\
x_{1}^{(m)} & \dots & x_{n}^{(m)}\end{bmatrix}
$$

Where:
- $x^{(i)}$ is the feature vector of the $i^{th}$ training example, ($i^{th}$ row of the $X$ matrix) 
- $x_{j}$ is the $j^{th}$ column of the $X$ matrix 
- $x_{j}^{(i)}$ is the $j^{th}$ feature of the $i^{th}$ training example (at the intersection of the $i^{th}$ row and the $j^{th}$ column of the $X$ matrix). It's a real number.
  

## The multivariate hypothesis
Then, we must update our hypothesis to take more than one feature into account. 

$$
\begin{matrix}\large
\hat{y}^{(i)} = \theta_0 + \theta_1 x_{1}^{(i)} + \dots + \theta_n x_{n}^{(i)} & & \text{ for i = 1, ..., m}    
\end{matrix}\normalsize
$$  

Where:
- $\hat{y}^{(i)}$ is the model's prediction for the $i^{th}$ example,
- $x_{1}^{(i)}$ is the first feature of the $i^{th}$ example,
- $x_{n}^{(i)}$ is the $n^{th}$ feature of the $i^{th}$example
- $\theta$ is a vector of dimension $(n + 1) * 1$, the parameter vector.
  
You will notice that we end up with two indices: $i$ and $j$. They should not be confused:
- $i$ refers to one of the $m$ examples in the dataset (line number in the $X$ matrix)
- $j$ refers to one of the $n$ features that describe each example (column number in the $X$ matrix)
