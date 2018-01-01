#coding:UTF-8
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)

# y = 2^x　2を底とするxの指数関数
y_2 = 2**x

# y = 3^x　3を底とするxの指数関数
y_3 = 3**x

print x
print y_2

# 指数関数はxの値が大きくになるにつれて、yの値が急激に増加する。
# また底の値が大きいほど傾きが大きく、急激にy値が増加する。
plt.plot(x, y_2)
plt.plot(x, y_3)
plt.show()