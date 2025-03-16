import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # 网络架构参数
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # 初始化权重和偏置
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size) * 0.1
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size) * 0.1
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.bias_output = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        # 前向传播
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = self.sigmoid(self.final_input)
        return self.final_output

    def backward(self, X, y, learning_rate):
        # 反向传播
        output_error = y - self.final_output
        output_delta = output_error * self.sigmoid_derivative(self.final_output)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)

        # 更新权重和偏置
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        # 训练网络
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, learning_rate)
            loss = np.mean(np.square(y - output))  # 均方误差损失
            if epoch % 100 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')

    def predict(self, X):
        return self.forward(X)

# 使用样例数据训练网络
if __name__ == '__main__':
    # 模拟一些输入数据，假设有10个输入特征
    X = np.array([
        [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
    ])
    
    # 对应的目标输出
    y = np.array([
        [0.5],
        [0.7]
    ])
    
    # 创建神经网络，输入10个节点，隐藏层5个节点，输出1个节点
    nn = NeuralNetwork(input_size=10, hidden_size=5, output_size=1)
    
    # 训练网络，训练1000次，学习率0.01
    nn.train(X, y, epochs=1000, learning_rate=0.01)
    
    # 使用训练好的网络进行预测
    test_input = np.array([[0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05]])
    prediction = nn.predict(test_input)
    
    print(f'Prediction for test input: {prediction}')
