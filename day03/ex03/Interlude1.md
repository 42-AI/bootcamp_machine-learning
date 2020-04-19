# Predict I: Introducing the Sigmoid Function
  <img src="../../day00/assets/Predict.png"/>  

### **Formulating a Hypothesis**  
Remember that a hypothesis is an equation (with parameters) that allows a model to calculate predictions based on a set of features. The linear hypothesis we used before worked fine to predict continuous values but how could it be useful to tell, for example, if a patient is sick or not?

To get started, let's set an output range within which we'll work: sick patients will be assigned the value of 1, and healthy patients will be assigned to 0. The goal will be to build a hypothesis that outputs a [0-1] probability  that a patient is sick.

The good news is that we can keep the linear equation we already worked with! All we need to do is sqash its output through another function that is bounded between 0 and 1. That's the **Sigmoid function** and your next exercise is to implement it!