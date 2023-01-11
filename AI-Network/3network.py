import numpy as np

def softmax(a):#softmax函数的输出是0.0到1.0之间的实数。并且，softmax函数的输出值的总和是1。
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def sigmoid(x):#sigmoid函数的平滑性对神经网络的学习具有重要意义。
    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x

def init_network():  # 权重偏置初始化，并建立字典
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network
def forward(network, x):  # 前向传播
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y
network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y) # [ 0.31682708 0.69627909]
# 机器学习的问题大致可以分为分类问题和回归问题。
# 分类问题是数据属于哪一个类别的问题。
# 比如，区分图像中的人是男性还是女性的问题就是分类问题。
# 而回归问题是根据某个输入预测一个（连续的）数值的问题。
# 比如，根据一个人的图像预测这个人的体重的问题就是回归问题（类似“57.4kg”这样的预测）。
# 神经网络需要根据情况改变输出层的激活函数。一般而言，回归问题用恒等函数，分类问题用softmax函数。