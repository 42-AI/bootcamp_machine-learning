# Interlude -  Normalization

The values inside the $x$ vector can vary quite a lot in magnitude, depending on the type of data you are working with. For example, if your dataset contains distances between planets in km, the numbers will be huge. On the other hand, if you are working with planet masses expressed as a fraction of the solar system's total mass, the numbers will be very small (between 0 and 1)  
Both cases may slow down convergence in Gradient Descent (or even sometimes prevent convergence at all). To avoid that kind of situation, normalization is a very effective way to proceed.  
  
The idea behind this technique is straightforward: **scaling the data**.  
   
With normalization, you can transform your $x$ vector into a new $x'$ vector whose values range between $[-1, 1]$ more or less. Doing this allows you to see much more easily how a training example compares to the other ones:
- If an $x'$ value is close to $1$, you know it's among the largest in the dataset
- If an $x'$ value is close to $0$, you know it's average
- If an $x'$ value is close to $-1$, you know it's among the smallest.

So with the upcoming normalization techniques, you'll be able to map your data to two different value ranges: $[0, 1]$ or $[-1, 1]$. Your algorithm will like it and thank you for it.  