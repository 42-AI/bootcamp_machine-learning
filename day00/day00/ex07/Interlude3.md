### Evaluate

<img src="day00/assets/Evaluate.png" />

## Introducing the cost function

How good is our model ?
It is hard to say by just looking at the plot. We can obviously observe that some lines seem to fit our data better than  others but it is not enough. 

[Ex mean (which is bad VS an opposite line which is the worst possible)]

To evaluate our model, we are going to use a **metric**, called a **cost function** (sometimes called **loss function**). The cost function tells us how bad is our model, how much it *costs* us to use it, how much we *loose* when we use it.  
If the model is good, we will not lost that much, if it's terrible it will cost us a lot!    

The metric you choose will impact deeply the results of your model.   

A very usual way to evaluate the performances of a regression model is to measure the distance between each predicted value and the true value it tries to predict. The smaller, the better.  

[img NEEDED HERE]