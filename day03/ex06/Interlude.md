## Linear Algebra strikes again!
You should have become quite used to vectorization for now.  
You may have already come up with the vectorized version of the logistic loss when you saw it in the previous exercice.  If you don't, check what comes next.

$$
J( \theta) = -\frac{1} {m} \lbrack \sum_{i = 1}^{m} y^{(i)}\log(\hat{y}^{(i)})) + (1 - y^{(i)})\log(1 - \hat{y}^{(i)})\rbrack
$$

$$
J( \theta) = -\frac{1} {m} \lbrack y \cdot \log(\hat{y}) + (\vec{1} - y) \cdot \log(\vec{1} - \hat{y})\rbrack
$$

Where: 
- $\vec{1}$ is a vector full of $1$ having the same dimensions $(m * 1)$ as $y$:  $\vec{1} = \begin{bmatrix}
    1 \\
    \vdots \\
    1
\end{bmatrix}$

Using $\vec{1}$ instead of $1$ is mandatory in this case because **addition (or substraction) between vectors and scalars is not defined**. You cannot do the operation $1 - y$.  
The only operation defined between these objects are multiplication, remember?  

### However...
However, `numpy` is a bit loosy on vectors and matrix operations...  
These following instructions will get the same results:
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
A lot of machine learning problems you will encounter will come from `numpy` loosy operations, and essentially **broadcasting**. Broadcasting is a powerfull tool but wich can lead you in very tricky situation, if you do not pay attention to your vectors (and matrices) shapes.  
Therefore, we **strongly** suggest you **to stay as close as possible to the true mathematical notation** of your operations. 