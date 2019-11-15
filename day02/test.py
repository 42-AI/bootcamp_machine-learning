import numpy as np


def sigmoid_(x):
    return 1 / (1 + np.exp(-x))
    # non vectorized version working with lists
    # if isinstance(x, int) or isinstance(x, float):
    #     return 1 / (1 + np.exp(-x))
    # else:
    #     sigmoid = []
    #     for i in range(len(x)):
    #         sigmoid.append(1 / (1 + np.exp(-x[i])))
    #     return sigmoid


def vec_log_loss_(y_true, y_pred, m, eps=1e-15):
    loss = -1 / m * np.sum(y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps))
    return loss


def vec_log_grad_(x, y_true, y_pred):
    return np.dot((y_pred - y_true), x)
    # or
    # return np.dot(x.T, (y_pred - y_true))
    # #same result because of the way how np.dot works


# --- TESTS FOR GRADIENT (and sigmoid btw) ---

x = np.array([1, 4.2])  # here 1 represent the intercept (a constant value intilialize at 1)
y_true = 1
theta = np.array([0.5, -0.5])
y_pred = sigmoid_(x * theta)
print(vec_log_grad_(x, y_pred, y_true))

x = np.array([1, -0.5, 2.3, -1.5, 3.2])
y_true = 0
theta = np.array([0.5, -0.5, 1.2, -1.2, 2.3])
y_pred = sigmoid_(x * theta)
print(vec_log_grad_(x, y_true, y_pred))

x_new = np.arange(2, 14).reshape((3, 4))
x_new = np.insert(x_new, 0, 1, axis=1)
# first column of x_new is now intercept values initiliazed to 1
y_true = np.array([1, 0, 1])
theta = np.array([0.5, -0.5, 1.2, -1.2, 2.3])
y_pred = sigmoid_(np.dot(x_new, theta))
print(vec_log_grad_(x_new, y_true, y_pred))
