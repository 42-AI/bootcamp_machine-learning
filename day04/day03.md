# Bootcamp ML

# Day03 - Decision Tree

This day aims to present a different kind of ML algorithm: decision trees.
Decision trees are historically quite popular as it is easy to demonstrate the thought process of the algorithm when 
making a prediction. They are also the base of more complex algorithms (random trees...) that have very good performances.

If you don't have the time to recode everything try to at least grasps the key concepts to be able to use them wisely in the future.


## Notions of the day

### Gini impurity, entropy, information gain. 
Gini: https://victorzhou.com/blog/gini-impurity/
Entropy: https://www.youtube.com/watch?v=9r7FIXEAGvs&feature=youtu.be


### Decision trees overview
* Statquest:  
https://www.youtube.com/watch?v=7VeUPuFGJHk&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index=34

* Building a decision tree step by step:  
https://www.youtube.com/watch?v=LDRbO9a6XPU&feature=youtu.be

* Sklearn doc:  
https://scikit-learn.org/stable/modules/tree.html#tree

* On decision tree regressors:  
https://gdcoder.com/decision-tree-regressor-explained-in-depth/


### Digging deeper
* ML course on decision trees. Beware principles are the same but implementation algorithm is not sklearn's one.  
https://www.youtube.com/watch?v=eKD5gxPPeY0&list=PLBv09BD7ez_4temBw7vLA19p3tdQH6FYO

* Nice article. Not everything relevant for the day.  
https://mlcourse.ai/articles/topic3-dt-knn/

* SO on difference between several decision trees algorithms.
https://stackoverflow.com/questions/9979461/different-decision-tree-algorithms-with-comparison-of-complexity-or-performance



## General rules

* The version of Python to use is 3.7, you can check the version of Python with the following command: `python -V`
* The norm: during this bootcamp you will follow the Pep8 standards https://www.python.org/dev/peps/pep-0008/
* The function eval is never allowed.
* The exercices are ordered from the easiest to the hardest.
* Your exercises are going to be evaluated by someone else, so make sure that your variable names and function names are appropriate and civil. 
* Your manual is the internet.
* You can also ask question in the dedicated channel in Slack: 42-ai.slack.com.
* If you find any issue or mistakes in the subject please create an issue on our dedicated repository on Github: https://github.com/42-AI/bootcamp_machine-learning/issues.

## Helper 

Ensure that you have the right Python version.

```
$> which python
/goinfre/miniconda/bin/python
$> python -V
Python 3.7.*
$> which pip
/goinfre/miniconda/bin/pip
```

