import pickle

import torch
import torch.optim as optim
from matplotlib import pyplot as plt
from torch import nn
from torch.utils.data import random_split

from cnnEncoder import Encoder
from dataload import ImageTextDataset
from decoder import Decoder
from model import EncoderDecoder


# 创建 Encoder 和 Decoder 实例
encoder = Encoder()
decoder = Decoder()
model = EncoderDecoder(encoder,decoder)

# 将模型移动到设备
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")
encoder.to(device)
decoder.to(device)

# 定义损失函数
loss_fn = nn.CrossEntropyLoss()
# 定义优化器
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 10
# 定义数据集
image_folder = "../data/diagram"
dataset = ImageTextDataset(image_folder)
lengths = [int(len(dataset) * 0.9), int(len(dataset) * 0.05),
           len(dataset) - int(len(dataset) * 0.9) - int(len(dataset) * 0.05)]
train_set, val_set, test_set = random_split(dataset, lengths)

with open('val_set.pkl', 'wb') as f:
    pickle.dump(val_set, f)
with open('test_set.pkl', 'wb') as f:
    pickle.dump(test_set, f)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=16, shuffle=True)
train_loss = []

# 迭代训练数据
for epoch in range(num_epochs):
    for i,(images, captions) in enumerate(train_loader):
        # 将图像和字幕移动到设备
        images = images.to(device)
        captions = captions.to(device)
        # 前向传播
        output = model(images, captions)
        # 计算损失
        loss = loss_fn(output.view(-1, output.size(2)), captions.view(-1))
        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # 打印损失
        if i % 50 == 0 :  # 3884个样本，batch_size =16， i最大为242
            print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item()}")
            train_loss.append(loss.item)
        # 每隔一定步骤保存模型
    if (epoch + 1) % 5 == 0:
        torch.save(model.state_dict(), 'model_weights_epoch_{}.pt'.format(epoch + 1))
        print(f"model saved as model_weights_epoch_{epoch + 1}.pt")

# 生成x轴数据
x = [val/5 for val in range(len(train_loss))]

# 绘制变化曲线
plt.plot(x, train_loss)

# 添加标签和标题
plt.xlabel('epoch')
plt.ylabel('loss')
plt.title('loss curve')

# 显示图表
plt.show()