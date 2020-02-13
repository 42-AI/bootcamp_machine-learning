# Predict 

<img src="day00/assets/Predict.png" />

## A very simple model
[Intro : simple data set + plot
We have some data.   We want to model it. First we need to make some assumptions, some hypothesis about the relationship tying together]

Let's start with a very simple **hypothesis**: the relation between our variables can be represented using a linear equation. 
[hypothesis: We will consider that the larger a house is, the more expensive it is. Furthermore, we will assume that the price increase is proportional to the size increase. By saying that, we assume that there is a linear relationship between the two variables. Then, all we need to do is to use the **linear equation** and adjust its parameters.]

This means that we are trying to represent the prediction as $\hat{y} = ax + b$.  

We are putting this symbol '^' over the $y$ to represent the fact that $\hat{y}$ is a **prediction** of the true value of $y$ given the **parameters** $a$ and $b$ and the input value $x$.  

For example, if $a = 5$ and $b = 33$, then $\hat{y} = 5x + 33$.  

We are going to do a slightly change in our notation now.  
Instead of $\hat{y} = ax + b$ we will use the following notation:  
$\hat{y} = \theta_0 + \theta_1 x$$.  

You might have two questions at the moment:  
- **WTF is that weird $\theta$ symbol?**  
This strange symbol, $\theta$, is called "theta".  

- **Why change for this notation?**  
We are using the theta notation because, despite the fact it will a first seem more complicated, it is actually done to simplify the notation later.  
Why?  
Imagine we have to build a more complex model using a lot of parameters.  
Something like $\hat{y} = ax_1 + bx_2 + ... + z$. What if we run out of letters?  
On the other hand, if you describe all your parameters using the theta notation, you can use as much parameters as you need. 
With theta, you just have to increment the number to name the parameter: $\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + ... + \theta_{2468} x_{2468}$ ... Easy right?
  

So now, we have $\hat{y} = \theta_0 + \theta_1 x$.  
If $\theta_0 = 33$ and $\theta_1 = 5$, then $\hat{y} = 33+ 5x$.    

This simple equation represents our **model**, also called our **hypothesis**. This model draws a **linear relationship between $\hat{y}$ and $x$**.  

Because $\hat{y}$ is build from our hypothesis, using $\theta$ and $x$, it is sometimes written as $h_{\theta}(x)$.
The $h$ stands for *hypothesis*, and can be read as *"the result of our hypothesis h given x and theta"*.  

Then if $x = 7$ we can calculate that $\hat{y} = h_{\theta}(x) = 33 + 5 \times 7 = 68$.
We can now say that according to our linear model, the **predicted value** of $y$ given $x  = 7$ is 68.     

To go a little further, lets consider a dataset containing $m$ data points called **examples**.  

What we have now are not single values for $x$ and $hat{y}$ but vectors of dimensions m * 1. The relation between our vectors can then be represented by the following formula:  
$$
\begin{matrix}
\hat{y}_i = \theta_0 + \theta_1 x_i & & \text{ for i = 1, ..., m}
\end{matrix}
$$  
  
Where:
- $y_i$ is the *ith* component of vector $y$
- $x_i$ is the *ith* component of vector $x$   

Which can be experessed as:  
$$
\hat{y} = \begin{bmatrix}\theta_0 + \theta_1 \times x_1 \\ \vdots \\  \theta_0 + \theta_1 \times x_m\ \end{bmatrix}
$$  

For example,
$$
\text{given } \theta = \begin{bmatrix}33 \\ 5 \end{bmatrix} \text{ and } x = \begin{bmatrix}1 \\ 3 \end{bmatrix} \text{: }$$
$$\hat{y} = h_{\theta}(x) = \begin{bmatrix} 33 +  1 \times 5 \\ 33 + 3 \times 5\end{bmatrix}  = \begin{bmatrix} 38 \\ 48 \end{bmatrix} 
$$    
