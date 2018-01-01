#coding:UTF-8
import matplotlib.pyplot as plt
import numpy as np

# グラフのx軸を生成。-5~15まで0.1ずつ刻むリスト
x = np.arange(-5, 15, 0.1)

# グラフのy軸を生成
# y = x^2 -10x + 10
y_2 = x**2 - 10*x + 10
# y = x^3 - 10x^2 - 10x + 10
y_3 = x**3 - 10*x**2 -10*x + 10

# plot(x, y) 第一引数にx軸の値、第二引数にy軸の値
plt.plot(x, y_2)
plt.plot(x, y_3)
# グラフ描画
plt.show()