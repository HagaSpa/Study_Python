# coding: UTF-8
import math
import matplotlib.pyplot as plt

# シグモイド関数（aが0なら0.5になり、正の数になるほど1に近づき負の数になるほど0に近づく）
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

# ニューロン
class Neuron:
    # 入力値の合計
    input_sum = 0.0
    output = 0.0

    # 入力値をセットする
    def setInput(self, inp):
        self.input_sum += inp

    # 出力値を取得する
    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0
        self.output = 0

# ニューラルネットワーク
class NeuralNetwork:
    # 入力値の重み
    w = [-0.5, 0.5]
    # ニューロンのインスタンス
    neuron = Neuron()
    # 受け取った入力値のリストを全てニューロンのinput_sumに加算
    def commit(self, input_data):
        self.neuron.reset()
        # input_dataとself.wの二つのリストを回す。リストの長さが違う場合短い方に合わせる
        for input, weight in zip(input_data, self.w):
            # 入力値とそれぞれの重みを乗算する
            data = input * weight
            self.neuron.setInput(data)
        return self.neuron.getOutput()

# 基準点(データの範囲を0.0-1.0に収めるため)
refer_point_0 = 34.5
refer_point_1 = 137.5

# ファイルの読み込み
trial_data = []
trial_data_file = open("trial_data.txt", "r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([float(line[0]) - refer_point_0, float(line[1]) - refer_point_1])
trial_data_file.close()


# ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

# 実行
position_tokyo = [[], []]
position_kanagawa = [[], []]
for data in trial_data:
    if neural_network.commit(data) < 0.5:
        position_tokyo[0].append(data[1]+refer_point_1)
        position_tokyo[1].append(data[0]+refer_point_0)
    else:
        position_kanagawa[0].append(data[1]+refer_point_1)
        position_kanagawa[1].append(data[0]+refer_point_0)

# プロット
plt.scatter(position_tokyo[0], position_tokyo[1], c="red", label="Tokyo", marker="+")
plt.scatter(position_kanagawa[0], position_kanagawa[1], c="blue", label="Kanagawa", marker="+")

plt.legend()
plt.show()