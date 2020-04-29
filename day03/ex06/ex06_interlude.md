# Interlude - Linear Algebra Strikes Again!
You've become quite used to vectorization by now. You may have already tried to vectorize the logistic cost function by yourself. Let's look one last time at the former equation:

$$
J( \theta) = -\cfrac{1} {m} \lbrack \sum_{i = 1}^{m} y^{(i)}\log(\hat{y}^{(i)})) + (1 - y^{(i)})\log(1 - \hat{y}^{(i)})\rbrack
$$

## Vectorized Logistic Cost Function

In the **vectorized version**, we remove the sum ( $\sum$ )because it is captured by the dot products:
$$
J( \theta) = -\cfrac{1} {m} \lbrack y \cdot \log(\hat{y}) + (\vec{1} - y) \cdot \log(\vec{1} - \hat{y})\rbrack
$$

Where: 
- $\vec{1}$ is a vector full of $1$'s with the same dimensions as $y$ : $(m * 1)$  

$$
\vec{1} = \begin{bmatrix}
    1 \\
    \vdots \\
    1
\end{bmatrix}
$$

## Note: Operations Between Vectors and Scalars 

We use the $\vec{1}$ notation to be rigorous, because **addition (or subtraction) between a vector and a scalar is not defined**. In other words, mathematically, you cannot write this: $1 - y$  
The only operation defined between a scalar and a vector is multiplication, remember?  

### However...
`NumPy` is a bit permissive on vectors and matrix operations...  
The following instructions will get you the same results:
```python
# Proper mathematical notation
y = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
ones = np.ones(y.shape[0]).reshape((-1,1))
ones - y
# Output
array([[-3.  ],
       [-6.16],
       [-2.2 ],
       [-8.37],
       [ 0.44]])

# Incorrect mathematical notation
y = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
1 - y
# Output
array([[-3.  ],
       [-6.16],
       [-2.2 ],
       [-8.37],
       [ 0.44]])
```
Strange, isn't it?  
It happens because of one of `NumPy`'s loose operations called **Broadcasting**. Broadcasting is a powerful feature whereby `NumPy` is able to figure out that you actually wanted to perform a subtraction on each element in the vector, so it does it for you automatically. It's very handy to write concise lines of code, but it can insert very sneaky bugs if you aren't 100% confident in what you're doing. 

Many of the bugs you will encounter while working on Machine Learning problems will come from `NumPy`'s permissiveness. 
Such bugs generaly don't throw any errors, but mess they up the content of your vectors and matrices and you'll spend an awful lot of time looking for why your model doesn't learn. This is why we **strongly** suggest that you pay attention to your vector (and matrix) dimensions and **stick as much as possible to the actual mathematical operations**.  

For more information, you can watch [this video on dealing with Broadcasting](https://www.youtube.com/watch?v=V2QlTmh6P2Y&t=213s).