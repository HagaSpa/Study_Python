#coding:UTF-8
import matplotlib.pyplot as plt
import numpy as np
import math

# x値のリストを引数に取り、シグモイド関数のy値のリストを返却する
def sigmoid(x):
    s = 1 / (1 + e**-x)
    return s

e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

# y = 1 / (1 + e^(-x))
# y_sig = 1 / (1 + e**-x)
y_sig = sigmoid(x)
print y_sig
plt.plot(x, y_sig)
plt.show()