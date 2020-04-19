# Predict II : Hypothesis 

We hope your curiosity led you to plot your sigmoid function. If you didn't, well here is what it looks like:

<img src="../../day03/assets/sigmoid.png"/>  

As you can see, **the results of the sigmoid are in the (0,1) range**.  
You can take real numbers as big as you want (positive or negative), they will always land within this range. This will be very helpfull for the next part.

# Logistic Hypothesis

Now you have your sigmoid function, let's look at **the logistic regression's hypothesis**.

$$
\begin{matrix}
\hat{y}^{(i)} & = & \text{sigmoid}(\theta \cdot X'^{(i)}) 
& =  &\frac{1} {1 + e^{-\theta \cdot X'^{(i)}}} & &\text{ for i = 1, \dots, m}    
\end{matrix}
$$

**This is simply the sigmoid function applied to the output of the linear regression hypothesis!!**  

Which can be vectorized as: 

$$
\begin{matrix}
\hat{y} & = & \text{sigmoid}(X' \cdot \theta) & =  &\frac{1} {1 + e^{-X' \cdot \theta}}    
\end{matrix}
$$

As we said before: the **sigmoid function** is just a way to **map the result of a linear equation onto a range of values between 0 and 1**.  

This transformation allows us to interpret the the result as a **probability for an individual to be a member of a class**.

