# Interlude - More Evaluation Metrics!

Once your classifier is trained, you want to evaluate its performance. You already know about *cross-entropy*, as you implemented it as your *cost function*. But when it comes to classification, there are more informative metrics we can use besides the loss function. Each metric focuses on different error types.  
But what is an error type?
 
A single classification prediction is either right or wrong, nothing in between. Either an object is assigned to the right class, or to the wrong class. When calculating performance scores for a multiclass classifier, we like to compute a separate score for each class that your classifier learned to discriminate (in a one-vs-all manner). In other words, for a given *Class A*, we want a score that can answer the question: "how good is the model at assigning *A* objects to *Class A*, and at NOT assigning *non-A* objects to *Class A*?"  

You may not realize it yet, but this question involves measuring two very different error types, and the distinction is crucial.

## Error Types
With respect to a given *Class A*, classification errors fall in two categories:

### **False positive:** when a *non-A* object is assigned to *Class A*.  
  For example: 
  - Pulling the fire alarm when there is no fire.

  - Considering that someone is sick when she isn't.
  
  - Identifying a face in an image when in fact it was a Teddy Bear.

### **False negative:** when an *A* object is assigned to another class than *Class A*.  
  For example: 
  - Not pulling the fire alarm when there is a fire.
  - Considering that someone is not sick when she isn't.
  - Failing to recognize a face in an image that does contain one.

It turns out that it's really hard to minimize both error types at the same time. At some point you'll need to decide which one is the most critical, depending on your use case. For example, if you want to detect cancer, of course it's not good if your model erroneously diagnoses cancer on a few healthy patients (**false positives**), but you absolutely want to avoid failing at diagnosing cancer on affected patients (**false negatives**) and let them go on with their lives while developing a potentially dangerous cancer. 

## Metrics
A metric is computed on a set of predictions along with the corresponding set of actual categories. The metric you choose will focus more or less on those two error types. If we come back to the **Class A** classifier: 
- **Accuracy**: tells you the percentage of predictions that are accurate (i.e. the correct class was predicted). Accuracy doesn't give information about either error type.
  
- **Precision**: tells you how much you can trust your model when it says that an object belongs to *Class A*. More precisely, it is the percentage of the objects assigned to *Class A* that really were *A* objects. You use precision when you want to control for **False positives**.
  
- **Recall**: tells you how much you can trust that your model is able to recognize ALL *Class A* objects. It is the percentage of all **A** objects that were properly classified by the model as *Class A*. You use recall when you want to control for **False negatives**.
  
- **F1 score**: combines precision and recall in one single measure. You use the F1 score when want to control both **False positives** and **False negatives**.