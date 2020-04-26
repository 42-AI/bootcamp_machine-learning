# More evaluation metrics!

Once your classifier is trained, there is a lot of ways to evaluate its performances (additionnaly to the cross-entropy). Depending on which you will choose, you will consider some errors to be more important than others.  

## Types of errors
Classification errors falls into two categories:
- **false positive:** where you give a positive label instead of a negative one.  
  For example: 
  - Considering that someone is sick when she does not.
  - Pull the fire alarm when there is no fire.

- **false negative**  where you give a negative label instead of a positive one.  
  For example: 
  - Considering that someone is not sick when he does.
  - Do not pull the fire alarm when there is a fire.

Given what you are trying to classify, what type of error is worst will change.  
According to your opinion of which type of error is better, you will choose different metrics.