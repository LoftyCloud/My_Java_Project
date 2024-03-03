# 构建CNN作为编码器
from torch import nn
from torch.nn import Sequential, Conv2d, ReLU, MaxPool2d, Linear, BatchNorm2d


# 转换成一个定长的中间语义表示c，对输入图像进行编码
class Encoder(nn.Module):
    def __init__(self):  # 输入为270*200大小的图像
        super(Encoder, self).__init__()
        self.conv = Sequential(                             # (16,1,270,200)
            Conv2d(1, 6, 5, stride=1),                      # (16,6,131,96)
            ReLU(),
            MaxPool2d(2),                                   # (16,6,128,93)
            BatchNorm2d(6),

            Conv2d(6, 16, 5, 1),                            # (16,16,57,42)
            ReLU(),
            MaxPool2d(2),                                   # (16,16,54,39)
            BatchNorm2d(16),

            Conv2d(16, 20, 5, 1),                           # (16,16,57,42)
            ReLU(),
            MaxPool2d(2),                                   # (16,16,54,39)
            BatchNorm2d(20),
        )

        self.fc = Sequential(
            Linear(12600, 10000),
            ReLU(),
            Linear(10000, 1000),                               # [16,1000]
            ReLU()
        )

    # 前向过程
    def forward(self, x):
        # X的形状应该为(batch_size,num_steps,embed_size)
        x = self.conv(x)
        x = x.view(x.size(0), -1)  # 展平
        x = self.fc(x)
        return x
