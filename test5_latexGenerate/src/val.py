import pickle

import torch

from model import EncoderDecoder
from torch import nn
# 定义数据集
from torch.utils.data import random_split

from src.cnnEncoder import Encoder
from src.dataprocess.vocab import Vocab
from src.decoder import Decoder
import torch.nn.functional as F
image_folder = "../data/diagram"

# 将模型移动到设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 创建 Encoder 和 Decoder 实例
encoder = Encoder().to(device)
decoder = Decoder().to(device)
model = EncoderDecoder(encoder, decoder)
with open('test_set.pkl', 'rb') as f:
    test_set = pickle.load(f)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=16, shuffle=True)

# 加载模型权重
model.load_state_dict(torch.load('model/model_weights_epoch_10.pt', map_location='cpu'))
with open('dataprocess/target_all.pkl', 'rb') as f:
    target_all = pickle.load(f)
# 创建vocab类
src_vocab = Vocab(target_all, min_freq=5, reserved_tokens=['<pad>', '<bos>', '<eos>'])

for image, tex in test_loader:
    pre = model(image.to(device), tex.to(device))
    # print(pre[0].shape)
    seq = []
    for i in range(125-1):
        next_token = torch.multinomial(F.softmax(pre[0][i], dim=0), 1).item()
        # 将下一个标记添加到序列中
        seq.append(next_token)
    print(seq)
    for i in src_vocab.to_tokens(seq):
        if i !="enter":
            print(i+" ",end='')
        else:
            print("")
    print(tex[0])
    print(src_vocab.to_tokens(list(tex[0])))
    break
