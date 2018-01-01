#coding:UTF-8
import matplotlib.pyplot as plt
import numpy as np
import math

# x値のリストを引数に取り、シグモイド関数のy値のリストを返却する
def sigmoid(x):
    s = 1 / (1 + e**-x)
    return s

# x値のリストを引数に取り、微分したシグモイド関数のy値のリストを返却する
def d_sigmoid(x):
    d = sigmoid(x)*(1 - sigmoid(x))
    return d

e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

# シグモイド関数
y_sig = sigmoid(x)
# xがdx分だけ増加した場合の増加量 / dx。傾き。シグモイド関数の微分
y_dsig = (sigmoid(x+dx) - sigmoid(x)) / dx
# シグモイド関数の微分。記載が簡単な書き方
# dy_sig = sigmoid(x)*(1 - sigmoid(x))
dy_sig = d_sigmoid(x)

plt.plot(x, y_sig, label = "sigmoid")
plt.plot(x, y_dsig, label = "d_sigmoid")
plt.plot(x, dy_sig, label = "dy_sigmoid")
plt.legend()
plt.show()