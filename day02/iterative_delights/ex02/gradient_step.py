import numpy as np


def sigmoid_(x):
    return 1 / (1 + np.exp(-x))
    # non vectorized version
    # if isinstance(x, int) or isinstance(x, float):
    #     return 1 / (1 + np.exp(-x))
    # else:
    #     sigmoid = []
    #     for i in range(len(x)):
    #         sigmoid.append(1 / (1 + np.exp(-x[i])))
    #     return sigmoid


def gradient_(x, y_pred, y_true):
    return x * (y_pred - y_true)
    # non vectorized version
    # if isinstance(x, int) or isinstance(x, float):
    #     return x * (y_pred - y_true)
    # else:
    #     grad = []
    #     for i in range(len(x)):
    #         grad.append(x[i] * (y_pred[i] - y_true))
    #     return grad

x = 4
theta = 0.5
y_pred = sigmoid_(theta * x)
y_true = 1
print(gradient_(x, y_pred, y_true))

# array version, so we can do vectorized operations
x = np.array([-5, 0.109, 0.652, 4.897])
theta = np.array([-1.589, 0.2579, 0.023, -5.064])
y_pred = sigmoid_(theta * x)
y_true = 1
print(gradient_(x, y_pred, y_true))

# non array version, non vectorized
# x = [-5, 0.109, 0.652, 4.897]
# theta = [-1.589, 0.2579, 0.023, -5.064]
# test = []
# for i in range(len(x)):
#     test.append(x[i] * theta[i])
# y_pred = sigmoid_(test)
# y_true = 1
# print(gradient_(x, y_pred, y_true))
