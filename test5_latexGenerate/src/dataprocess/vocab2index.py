import pickle

import torch

from src.dataprocess.vocab import Vocab


def truncate_pad(line, num_steps, padding_token):
    """
    填充与截断序列长度，返回词元序列
    :param line:
    :param num_steps:
    :param padding_token:
    :return:
    """
    if len(line) > num_steps:
        return line[:num_steps]
    return line + [padding_token] * (num_steps - len(line))


def build_array(lines, vocab, num_steps):
    """
    词元序列转为索引序列，添加<eoc>和<pad>
    :param lines:
    :param vocab:
    :param num_steps:
    :return:
    """
    # 将词元序列，转为词元对应的索引序列
    # print(lines)
    lines = [[vocab['<bos>']] + vocab[l] + [vocab['<eos>']]for l in lines]
    # array为经过截断与填充的序列
    array = torch.tensor([truncate_pad(l, num_steps, vocab['<pad>']) for l in lines])
    # 保存合并后的二维列表到文件
    with open('tensor_all.pkl', 'wb') as f:
        pickle.dump(array, f)
    # print(f"{len(array)} tensor data saved.")
    # print(array[0])


with open('target_all.pkl', 'rb') as f:
    target_all = pickle.load(f)

# 创建vocab类
src_vocab = Vocab(target_all, min_freq=5, reserved_tokens=['<pad>', '<bos>', '<eos>'])
build_array(target_all, src_vocab, 125)
