import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class MyLinearRegression():
	"""
	put some descriptions in it !
	"""
	def __init__(self, nb_theta = 2, *theta):
		"""
		Generator of the class, nb_theta is the number of parameters constituting
		the linear model, theta is the parameters of the linear model -list type expected-.
		"""
		self.theta = []
		if  nb_theta == 2:
			if len(theta) == 0:
				self.theta = np.zeros(2)
			else:
				self.theta = np.array(theta)
		else:
			if all(elem is 0 for elem in theta):
				self.theta = np.zeros(nb_theta)
			else:
				self.theta = np.array(theta).reshape(nb_theta,)

	def predict(self, X):
		"""
		Method which apply the linear model to calcultate and return -array type-
		the prediction using the X values -array type-.
		"""
		if not isinstance(X, np.ndarray):
			raise TypeError("Object of array type is expected.")
		Y = np.array([])
		for elem in X:
			y = self.theta[0] + np.dot(self.theta[1:], elem)
			print(y)
			Y = np.append(Y, y, axis=0)
		return Y

	def score(self, X, Y):
		"""
		Method which calculate the R -sum of the square of the diffence of y-, in over words
		the cost function.
		"""
		predic_Y = self.predict(X)
		N = len(Y)
		R = (1/(2.0*N))*sum((predic_Y - Y)**2)
		return R

	def get_params(self):
		"""
		Method which return theta.
		"""
		return self.theta

	def set_params(self, params):
		"""
		Method to set the values of theta -list type -.
		"""
		if len(params) != len(self.theta):
			raise ValueError("Length of list parameters does not match the expected lentgh.")
		self.theta = np.array(params)

	def __str__(self):
		return ("[theta_i] = {} type ={}.".format(self.theta, type(self.theta)))


# ~~~~~~~~~~ lecture des datas ~~~~~~~~~~~~~ #
data = pd.read_csv("blue_pill_and_maths.csv")
Xpatient = np.array(data['patient'])
Xpill = np.array(data['mcg'])
Ynote = np.array(data['score'])
#print(Xpatient)
#print(Xpill)
#print(Ynote)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# ~~~~~~~~~~ test du generateur ~~~~~~~~~~~~ #
obj1 = MyLinearRegression()
obj2 = MyLinearRegression(2)
obj3 = MyLinearRegression(3)
obj4 = MyLinearRegression(3, [1.0, 2.0, 3.0])
#print(obj1)
#print(obj2)
#print(obj3)
#print(obj4)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# ~~~~~~~ test methode get_params ~~~~~~~~~ #
theta_param1 = obj1.get_params()
theta_param4 = obj4.get_params()
#print(theta_param1)
#print(theta_param4)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# ~~~~~~~ test methode set_params ~~~~~~~~~ #
obj2.set_params([5.0, 1.0])
obj4.set_params([1.0, 5.0, 10.0])
#print(obj1)
#print(obj4)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# ~~~~~~~~~ test methode predict ~~~~~~~~~~ #
Y = obj2.predict(Xpatient)
print(Y)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# ~~~~~~~~~~ test methode score ~~~~~~~~~~~ #
#Y = obj2.score()
#print(Y)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
