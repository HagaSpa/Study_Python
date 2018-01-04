# coding: UTF-8
import math

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

# ニューラルネットワーク
class NeuralNetwork:
    # ニューロンのインスタンス
    neuron = Neuron()
    # 受け取った入力値のリストを全てニューロンのinput_sumに加算
    def commit(self, input_data):
        for data in input_data:
            self.neuron.setInput(data)
        return self.neuron.getOutput()


# ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

# 実行
trial_data = [-1.0, -2.0, -3.0]
print neural_network.commit(trial_data)