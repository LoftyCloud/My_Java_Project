import torch
from torch.utils.data import random_split

from dataload import ImageTextDataset
from cnnEncoder import Encoder
from decoder import Decoder

image_folder = "../data/diagram"
dataset = ImageTextDataset(image_folder)
# print(dataset[0])

# 数据划分，得到train_set, val_set, test_set
# 训练集、验证集、测试集划分
# 大约3500个训练样本，150验证样本，150测试样本
lengths = [int(len(dataset) * 0.9), int(len(dataset) * 0.05),
           len(dataset) - int(len(dataset) * 0.9) - int(len(dataset) * 0.05)]
train_set, val_set, test_set = random_split(dataset, lengths)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=16, shuffle=True,drop_last=True)

encoder = Encoder()
# 切换为测试模式
encoder.eval()
decoder = Decoder()
# 切换为测试模式
decoder.eval()

for image, text in train_loader:
    print(image.shape)
    x = encoder(image)
    print(x.unsqueeze(0).shape)  # [1,16,1000]
    # print(text)
    # print(text.shape)           # [16,125]
    y = decoder(x, text)
    print(y.shape)  # [1,16,1491]
    break
