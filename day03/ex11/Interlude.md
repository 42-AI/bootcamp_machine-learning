# More evaluation metrics!

Once your classifier is trained, additionnaly to the cross-entropy, there is a lot of ways to evaluate its performances. Depending on which you'll choose, you will consider some errors more important than others.  

## Types of errors
Classification errors falls into two categories:
- **false positive:** where you give a positive label instead of a negative one.  
  For example: considering that someone has a cancer when she does not. 

- **false negative**  where you give a negative label instead of a positive one.  
  For example: considering that somone has not a cancer whe he does.

Given what you are trying to classify, what type of error is worst will change.  
According to your opinion of which type of error is better, you will choose different metrics.