# More Evaluation Metrics!

Once your classifier is trained, you want to evaluate its performance. You already know about *cross-entropy*, because you implemented it as your *cost function*. But when it comes to classification, there are more informative metrics that we can use on top of the loss function. Each of them will focus on different types of errors.
 
When dealing with a classification problem, it is common practice to calculate a separate performance score for each class. For a given *Class A*, that score answers the question: "how good is the model at assigning *A* objects to *Class A*, and not assigning *non-A* objects to *Class A*?"  

You may not realize it yet, but this question involves measuring two very different types of errors and the distinction is crucial.

## Types of errors
With respect to a given class, classification errors fall in two categories:
- **false positive:** when you erroneously label a *non-A* object as belonging *Class A*.  
  For example: 
  - Pulling the fire alarm when there is no fire.
  - Considering that someone is sick when she isn't.
  - Recognizing an object in an image as a face when in fact it was a Teddy Bear.

- **false negative:** when you label an *A* object as belonging to another class than *Class A*.  
  For example: 
  - Not pulling the fire alarm when there is a fire.
  - Considering that someone is not sick when she isn't.
  - Failing to recognize a face in an image that does contain one.

It turns out that it is really hard to minimize both types of errors at the same time. You will usually need to which one is the most critical depending on your use case. For example, if you want to detect cancer, sure it's not great if you erroneously diagnose cancer on a few healthy patients (**false positive**), but you absolutely want to avoid failing at diagnosing it (**false negative**) and let it develop in a patient who thinks they are healthy. 

More concretely, the type of error will help you choose a metric:

## Metrics
Given a model that is able to classify objects of **Class A** and **Others**
- **Accuracy**: measures what percentage of all predictions are accurate.
- **Precision**: tells you how much you can trust your model when it tells you that an object belongs to *Class A*. More precisely, it measures what percentage of the objects that your model labels as **Class A** really are. You use precision when you are worried about **False positives**.
- **Recall**: tells you how much you can trust that your model has been able to recognize ALL *Class A* objects. It measures what percentage of **A objects** have been labeled by your model as belonging to Class A. You use recall when you are worried about **False negatives**.
- **F2 score**: combines precision and recall in one single measure. You try to get a good F2 score when you are worried about both **False positives** and **False negatives**.