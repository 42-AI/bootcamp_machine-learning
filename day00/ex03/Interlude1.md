### Predict 

<img src="day00/assets/Predict.png" />


## A very simple model
[Intro : simple data set + plot
We have some data.   We want to model it. First we need to make some assumptions, some hypothesis about the relationship tying together]

Let's start with a very simple **assumption**: the relation between our variables can be represented using a linear equation.  

This means that we are trying to represent $\hat{y} = ax + b$.  

We are putting this symbol '^' over the $y$ to represent the fact that $\hat{y}$ is a **prediction** of the true value of $y$ given the **parameters** $a$ and $b$ and the input value $x$.  

For example, if $a = 5$ and $b = 33$, then $\hat{y} = 5x + 33$.  

We are going to do a slightly change in our notation now.  
Instead of $\hat{y} = ax + b$ we will use the following notation:  
$$\hat{y} = \theta_0 + \theta_1 x$$.  

You have probably two questions now:  
- WTF is that weird $\theta$ symbol?
This strange symbol, $theta$, is called "theta".  

- Why change for this notation?  
We are using the theta notation because, despite the fact it will a first seems more complicated, it is actually done to simplify the notations later.  
Why?  
Imagine we have to build a more complex model using a lot of parameters.  
Something like $\hat{y} = ax1 + bx2 + ... + z$. How do you handle more than 23 paremeters?  
On the other hand, if you describe all your parameters using the theta notation, you can use as much parameters as you need. 
With theta, you just have to increment the number to name the parameter: $\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x2 + ... + \theta_2468 x_2468$ ... Easy right?
  

So now, we have $\hat{y} = \theta_0 + \theta_1 x$.  
If $\theta_0 = 33$ and $\theta_1 = 5$, then $\hat{y} = 33+ 5x$.    

This simple equation is now our **model**. This model draws a **relation between $y$ and $x$**.  
Using directly $y$ and not $\hat{y}$ in the previous sentence was done on purpose: **the relation we are looking for is not between our prediction and our inputs values, but between what we want to predict and our inputs values**.  

Then if $x = 7$ we can calculate that $\hat{y} = 33 + 5 \times 7 = 68$.
We can now say that according to our linear model, the **predicted value** of $y$ given $x  = 7$ is 68.     

To go a little further, lets consider a dataset containing $m$ data points called **examples**.  

What we have now are not single values for $x$ and $hat{y}$ but vectors of dimensions m * 1. The relation between our vectors can then be represented by the following formula:  
$$
\hat{y}_i = \theta_0 + \theta_1 x_i \text{ for i = 1, ..., m}
$$  
  
Where:
- $y_i$ is the *ith* component of vector $y$
- $x_i$ is the *ith* component of vector $x$   

Which can be experessed as:  
$$\hat{y} = \begin{bmatrix}\theta_0 + \theta_1 \times x_1\ \vdots\  \theta_0 + \theta_1 \times x_m\ \end{bmatrix}$$  

For example,
$$\text{given } \theta = \begin{bmatrix}33 \ 5 \end{bmatrix} \text{ and } x = \begin{bmatrix}1 \ 3 \end{bmatrix} \text{: }$$    
$$\hat{y} = \begin{bmatrix} 33 +  1 \times 5 \ 33 + 3 \times 5\theta_1 \end{bmatrix}  = \begin{bmatrix} 38 \ 48 \end{bmatrix} $$    