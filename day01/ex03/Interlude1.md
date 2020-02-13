### Improve

<img src="day00/assets/Improve.png" />

Yesterday, you saw the first two steps of the learning process: start with a prediction and evaluate it. Now we are going to learn the third part: how to improve it!  

Given our measure of performance, improvement imply to **reduce the loss** measured by our cost function. If we plot the cost of our prediction given $\theta_1$ we obtain a curve like this one: 

[IMG cost func]

On the figure above, we can see that some value of $\theta_1$ are very bad to makes predictions and some others are way better to predict the values of $y$.

[IMG BAD / VS GOOD]

Knowing that fact, we can see that there is a specific value for $\theta_1$ which gives the minimum cost. This value is at the bottom of our graph. 

Therefore, given any value of $\theta_1$, improving our prediction means getting closer to the minimum of the cost function (the bottom of the curve). In other word: if we change the value of $\theta_1$ to get closer to that minimum, our prediction will be better.  

#### But, how to get closer to the minimum?

Excellent question dear reader. I am glad you asked!  
The first step is to find the direction in which you want to go.  
This can be done by calculating the derivative of our cost function. 

(If you do not feel comfortable with derivatives, having an overview of what it is about could be a good idea)
