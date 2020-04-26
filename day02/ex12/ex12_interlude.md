# Plotting curves with matplotlib

We asked you to plot straight lines in the day00. Now you are working with polynomial models, the results are not straight lines but curves.   
Plotting curves is a bit more tricky, because if you do not have enough data point, you will get an ugly succession of little straight lines instead of a curve.  
Here is a way to do it.  

Lets begin with a simple dataset:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11).reshape(-1,1)
y = np.array([[ 1.39270298],
           [ 3.88237651],
           [ 4.37726357],
           [ 4.63389049],
           [ 7.79814439],
           [ 6.41717461],
           [ 8.63429886],
           [ 8.19939795],
           [10.37567392],
           [10.68238222]])

plt.scatter(x,y)
```
![titre](../assets/ex12_data.png){width=300px}

Now, we build and plot a polynomial model up to power 3.

```python
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR

# Build the model:
x_ = add_polynomial_features(x, 3)
my_lr = MyLR(np.one(4).reshape(-1,1)).fit(x_, y)

# Plot:
## To get a smooth curve, we need a lot of data points
continuous_x = np.arange(1,10.1, 0.1).reshape(-1,1)
x_ = add_polynomial_features(continuous_x, 3)
y_hat = my_lr.predict(continuous_x)

plt.scatter(x,y)
plt.plot(continuous_x, y_hat, color='orange')
```
![titre](../assets/ex12_plot.png){width=300px}
