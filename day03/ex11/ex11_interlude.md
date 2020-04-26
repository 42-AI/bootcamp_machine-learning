# More Evaluation Metrics!

Once your classifier is trained, you want to evaluate its performance. You already know about *cross-entropy*, because you implemented it as your *cost function*. But when it comes to classification, there are more informative metrics that we can use on top of the loss function. Each of them will focus on different error types.
 
A classification prediction is either right or wrong, nothing in between. Either an object is assigned to the right class, or to a wrong class. When calculating performance scores, it's common practice to compute a separate one for each class that your classifier learned to discriminate (in a one-vs-all manner). For a given *Class A*, that score answers the question: "how good is the model at assigning *A* objects to *Class A*, and not assigning *non-A* objects to *Class A*?"  

You may not realize it yet, but this question involves measuring two very different error types, and the distinction is crucial.

## Error Types
With respect to a given *Class A*, classification errors fall in two categories:
- **false positive:** when a *non-A* object is assigned to *Class A*.  
  For example: 
  - Pulling the fire alarm when there is no fire.
  - Considering that someone is sick when she isn't.
  - Identifying a face in an image when in fact it was a Teddy Bear.

- **false negative:** when an *A* object is assigned to another class than *Class A*.  
  For example: 
  - Not pulling the fire alarm when there is a fire.
  - Considering that someone is not sick when she isn't.
  - Failing to recognize a face in an image that does contain one.

It turns out that it's really hard to minimize both error types at the same time. You must decide which one is the most critical, depending on your use case. For example, if you want to detect cancer, of course it's not great if your model erroneously diagnoses cancer on a few healthy patients (**false positives**), but you absolutely want to avoid failing at diagnosing cancer on affected patients (**false negatives**) and let their state deteriorate while they think they are healthy. 

## Metrics
The metric you choose will focus more or less on those two error types. If we come back to the **Class A** classifier: 
- **Accuracy**: measures what percentage of all predictions are accurate.
- **Precision**: tells you how much you can trust your model when it tells you that an object belongs to *Class A*. More precisely, it measures what percentage of the objects that your model labels as **Class A** really are. You use precision when you are worried about **False positives**.
- **Recall**: tells you how much you can trust that your model has been able to recognize ALL *Class A* objects. It measures what percentage of **A objects** have been labeled by your model as belonging to Class A. You use recall when you are worried about **False negatives**.
- **F2 score**: combines precision and recall in one single measure. You try to get a good F2 score when you are worried about both **False positives** and **False negatives**.