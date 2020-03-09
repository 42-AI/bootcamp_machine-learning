## Normalization

The values inside the $x$ vector can vary quite a lot in magnitude, depending on the type of data you are working with. For example, if your dataset contains distances between planets in km, the numbers will be huge. On the other hand, if you are working with planet masses expressed as a fraction of the solar system's total mass, the numbers will be very small.  
Both cases may slow down convergence in Gradient Descent (or even sometimes prevent convergence at all). To avoid that kind of situation, normalization is a very effective way to proceed.  
  
The idea behind this technique is straightforward: **scaling the data**.  
   
With normalization, you can transform your $x$ vector into a new $x'$ vector whose values range between $[-1, 1]$ more or less. Doing this allows you to see much more easily if a training example is large or small :
- If an $x'$ value close to $1$, you know it's among the largest in the dataset
- If an $x'$ value is close to $0$, you know it's average
- If an $x'$ value is close to $-1$, you know it's among the smallest.

So with the upcoming normalization techniques, you'll be able to transform your data within the $[0, 1]$ or $[-1, 1]$ range. Your algorithm will like it and thank you for it.  

### Helpful resources:
https://www.coursera.org/learn/machine-learning/lecture/xx3Da/gradient-descent-in-practice-i-feature-scaling