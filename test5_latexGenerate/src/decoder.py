import torch
import torch.nn as nn


class Decoder(nn.Module):
    def __init__(self, input_size=1000, hidden_size=1000, vocab_size=1491, device=torch.device("cpu")):
        super(Decoder, self).__init__()
        self.device = device
        self.hidden_size = hidden_size
        # 定义嵌入层
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        # 定义GRU单元
        self.gru = nn.GRU(input_size, hidden_size)
        # 定义全连接层
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, encoder_output, captions):  # encoder_output(16,1000) caption(16,125)
        # 将编码器输出进行形状变换
        batch_size = encoder_output.size(0)
        caption_length = captions.size(1)  # 125

        embedded = self.embedding(captions).permute(1, 0, 2)  # (16,125,1000)
        hidden = self.init_hidden(batch_size)  # 1，16，1000
        # hidden = encoder_output.unsqueeze(0)  # (1,16,1000)
        outputs = []

        for t in range(caption_length):  # t :时间步，从0到125
            # 将编码器输出通过GRU单元进行解码
            # embedded[:, t, :].unsqueeze(1)表示时间步t上所有样本的嵌入向量
            output, hidden = self.gru(embedded[t, :, :].unsqueeze(1), hidden)  # (16, 1, 1000)  (1,16,1000)
            # 将GRU的输出通过全连接层进行映射到词表空间
            output = self.fc(output.squeeze(1))
            outputs.append(output.unsqueeze(1))
        outputs = torch.cat(outputs, dim=1)
        return outputs  # 输出词元的分布概率

    def init_hidden(self, batch_size):
        # 初始化隐藏状态
        # hidden = torch.zeros(1, batch_size, self.hidden_size)
        hidden = torch.zeros(1, 1, self.hidden_size).to(self.device)
        return hidden

