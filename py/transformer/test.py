import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import StandardScaler

# 读取Excel数据
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# 选择输入和输出
input_columns = ['input1', 'input2', 'input3', 'input4', 'input5']
output_column = 'output1'

# 提取输入和输出
inputs = df[input_columns].values
outputs = df[output_column].values

# 数据标准化
scaler = StandardScaler()
inputs_scaled = scaler.fit_transform(inputs)

# 训练集 (前 17 组数据)
X_train = torch.tensor(inputs_scaled[:17], dtype=torch.float32)
y_train = torch.tensor(outputs[:17], dtype=torch.float32).unsqueeze(1)  # 变成列向量

# 测试集 (第 18 组数据)
X_test = torch.tensor(inputs_scaled[17].reshape(1, -1), dtype=torch.float32)

# 定义 Transformer 模型
class TransformerRegressor(nn.Module):
    def __init__(self, input_dim, d_model=64, nhead=4, num_layers=2):
        super(TransformerRegressor, self).__init__()
        self.input_embedding = nn.Linear(input_dim, d_model)  # 输入映射到 d_model 维度
        self.transformer = nn.Transformer(
            d_model=d_model, nhead=nhead, num_encoder_layers=num_layers, num_decoder_layers=num_layers, batch_first=True
        )
        self.fc = nn.Linear(d_model, 1)  # 最终输出 1 维（output1）

    def forward(self, src):
        src = self.input_embedding(src).unsqueeze(1)  # (batch_size, seq_len=1, d_model)
        out = self.transformer(src, src)  # Transformer 编码
        out = self.fc(out.squeeze(1))  # 还原回 1 维输出
        return out

# 初始化模型
model = TransformerRegressor(input_dim=5)
criterion = nn.MSELoss()  # 损失函数：均方误差
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam 优化器

# 训练模型
epochs = 500
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    predictions = model(X_train)
    loss = criterion(predictions, y_train)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.6f}")

# 预测第 18 组数据
model.eval()
with torch.no_grad():
    prediction = model(X_test).item()

print("\nPredicted output1 for the 18th data point:", prediction)
