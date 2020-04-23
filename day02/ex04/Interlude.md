# Evaluate

![titre](../../day00/assets/Evaluate.png){width=400px}

## Back to the Cost Function

How is our model doing?  

To evaluate our model, remember before we used a **metric** called the **cost function** (also known as **loss function**). The cost function is basically just a measure of how wrong the model is, in all its predictions.   

Two days ago, we defined the cost function as the average of the squared distances between each prediction and its expected value : 
![titre](../../day00/assets/bad_pred_with_distance.png){width=400px}

The formula was the following: 
$$
J(\theta) = \frac{1}{2m}\sum_{i=1}^{m}(\hat{y}^{(i)} - y^{(i)})^2
$$
And its vectorized form:
$$
\begin{matrix}
J(\theta) = \frac{1}{2m}(\hat{y} - y)^{T}(\hat{y}- y)
\end{matrix}
$$  

#### So, now that we moved to multivariate linear regression, what needs to change?
You may have noticed that variables such as $x_j$ and $\theta_j$ don't intervene in the equation. Indeed, the cost function only uses the predictions ( $\hat{y}$ ) and the expected values ( $y$ ), so the internal working of the model doesn't matter. This means we can use the exact same cost function as we did before! 