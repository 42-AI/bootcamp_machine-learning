import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class MyLinearRegression():
	"""
	put some descriptions in it !
	"""
	def __init__(self, nb_theta = 2, *theta):
		"""
		put some description in it!
		"""
		self.theta = []
		if  nb_theta == 2:
			if len(theta) == 0:
				self.theta = [0.0, 0.0]
			else:
				self.theta = [theta[0], theta[1]]
		else:
			if all(elem is 0 for elem in theta):
				self.theta = [0.0] * nb_theta
			else:
				self.theta = list(theta)

	def predict(self, X):
		"""
		put some descriptions in it!
		"""
		if not isinstance(X, np.ndarray):
			raise TypeError("Object of array type is expected.")
		Y = []
		for elem in X:
			print("val de self.theta: ", self.theta, "val de elem: ", elem)
			y = self.theta[0] + sum(self.theta[1:] * elem)
			Y.append(y)
		return np.array(Y)
	
	def score(self, X, Y):
		"""
		put some descriptions in it!
		"""
		pass

	def get_params(self):
		"""
		Put some descriptions in it!
		"""
		return self.theta

	def set_params(self, **params):
		"""
		Put some description in it
		"""
		if len(params) != len(self.theta):
			raise ValueError("Length of list parameters does not match the expected lentgh.")
			#exit()
		i = 0
		for elem in params:
			self.theta[i] = elem
			i += 1

	def __str__(self):
		return ("[theta_i] = {} type ={}.".format(self.theta, type(self.theta)))


obj1 = MyLinearRegression()
obj2 = MyLinearRegression(2)
obj3 = MyLinearRegression(3)
obj4 = MyLinearRegression(3, [1.0, 2.0, 3.0])

print(obj1)
print(obj2)
print(obj3)
print(obj4)
theta_param1 = obj1.get_params()
theta_param4 = obj4.get_params()
print(theta_param1)
print(theta_param4)
print(obj4.predict(np.array([[10.0, 100.0], [20.0, 200.0], [30.0, 300.0]])))
data = pd.read_csv("blue_pill_and_maths.csv")
Xpatient = np.array(data['patient'])
Xpill = np.array(data['mcg'])
Xscore = np.array(data['score'])


