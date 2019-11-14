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
		if not isinstance(nb_theta):
			if not isinstance(theta):
				self.theta = [0.0, 0.0]
			else:
				self.theta = [theta[0], theta[1]]
		else:
			if not isinstance(theta):
				self.theta = [0] * nb_theta
			else:
				for i in range(nb_theta):
					self.theta.append(theta[i])

	def predit(self, X):
		"""
		put some descriptions in it!
		"""
		pass
	
	def score(self, X, Y):
		"""
		put some descriptions in it!
		"""
		pass

	def set_params(self, **params):
		"""
		Put some descriptions in it!
		"""
		pass

	def set_params(self, **params):
		"""
		Put some description in it
		"""
		pass


obj1 = MyLinearRegression()
obj2 = MyLinearRegression(2)
obj3 = MyLinearRegression(3)
data = pd.read_csv("blue_pill_and_maths.csv")
Xpatient = np.array(data['patient'])
Xpill = np.array(data['mcg'])
Xscore = np.array(data['score'])


