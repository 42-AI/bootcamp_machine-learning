## Linear Algebra strikes again!
You should have become quite used to vectorization for now.  
You may have already come up with the vectorized version of the logistic loss when you saw it in the previous exercice.  If you don't, check what comes next.

$$
J( \theta) = -\frac{1} {m} \lbrack \sum_{i = 1}^{m} y^{(i)}\log(\hat{y}^{(i)})) + (1 - y^{(i)})\log(1 - \hat{y}^{(i)})\rbrack
$$

$$
J( \theta) = -\frac{1} {m} \lbrack y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y})\rbrack
$$