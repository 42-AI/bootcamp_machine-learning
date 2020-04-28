# Interlude - Classification: The Art of Labelling Things
Over the last three days you have implemented your first machine learning algorithm. You also discovered the three main steps we follow when we build **learning algorithms**: 
![The Learning Cycle](../assets/Default.png){width=300px}

The first algorithm you discovered, **Multivariate Linear Regression**, can now be used to predict a numerical value, based on several features. This algorithm uses gradient descent to optimize its cost function.  

Now let's introduce you to your first **classification algorithm**: it is named **Logistic Regression**. It peforms a *classification task*, which means that you are not predicting a numerical value (like price, age, grades...) but **categories**, or **labels** (like dog, cat, sick/healty...).   

#### **Be careful!**  
Don't be confused by the word *'regression'* in **Logistic Regression**. It really is a *classification task*! The name is a bit tricky but you will quickly get used to it.  

Once again: **Logistic Regression is a classification algorithm** which assigns a given example to a category.  

### **Terminolgy:**
In this bootcamp we will use the following terms interchangeably: **class, category,** and **label**. They all refer to the *groups* to which each training example can be assigned to, in a classification task.