## Lost in overfitting
The two previous exercises lead you, dear reader, in a very dangerous territory: in the realm of **overfitting**.  You did not see it coming but now, you are in a bad situation...  

By increasing the polynomial degree of your model you built a **very complex one**.  
Is it wrong?  
Not always.  
Some models are indeed very complex because the relationships they represent are very complex as well. 

But, if you look at the plots of the previous model evaluated as the best one, you should feel that something is wrong. 

### Something is rotten in the state of our model...
Take a look at the following plot. 

<img src="day03/assets/overfitt.png" />  

You can see that the prediction line fits perfectly each data points but miss totaly to capture properly the relationship between $x$ and $y$.  
And now, if we add some data points to our model, we see that the prediction on such new examples will be performed terribly. 

<img src="day03/assets/overfitt_with_dots.png" />  

This situation is called overfitting, because our model do a too good job at fitting the data. Because of that is now impossible for the model to properly generalise to new data.

### The training set, the test set, and the happy data scientist
To avoid overfitting, **you should always evaluate your model on new data**.  
  
To do so, now and forever you must always divide your dataset in (at least) two parts: one for the training, and one for the evaluation of your model. 