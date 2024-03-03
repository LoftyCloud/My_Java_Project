# 对tex代码进行处理，划分词元并保存为target_all.pkl，方便vocab类读取

import os
import pickle


def preprocess_nmt(text):  # 标点符号前后添加空格
    def no_space(char, near_char):
        return char in set(',[{^_\']}()|') and near_char != ' ' and near_char != "\n"

    # 在单词和标点符号之间插入空格
    text = text.replace('\u202f', ' ').replace('\xa0', ' ')
    out = [' ' + char if i > 0 and no_space(char, text[i - 1]) else char for i, char in enumerate(text)]
    text = ''.join(out)
    out = [char + ' ' if (i < len(text)-1) and no_space(char, text[i + 1]) else char for i, char in
           enumerate(text)]
    return ''.join(out)  # 连接成字符串


# num_examples 样本的数量
def tokenize_nmt(text, num_examples=None):
    target = []
    # 按行分割成一个一个列表
    for i, line in enumerate(text.split('\n')):
        # 大于样本数量，停止添加
        if num_examples and i > num_examples:
            break
        target.append(line.split(' '))
    return target


def tex_split(text):
    """
    将tex文件内的内容划分为词元列表
    :param text:
    :return:
    """
    # 去掉前后两行
    content = text[2:-2]
    # 将剩余行连接成一个字符串
    content = ''.join(content)  # 读取tex文件中的目标部分
    content = preprocess_nmt(content)  # 标点符号前后添加空格
    target = tokenize_nmt(content)  # 按空格划分content
    split = []
    for i, line in enumerate(target):  # 将二维列表编码为一维，并对换行进行编码
        split = split + line
        if i != len(target) - 1:  # 非最后一行，则用enter代表换行
            split.append("enter")
    split = list(filter(lambda x: x != '', split[:-2]))   # 最后会有一个"enter"和" "，将其舍去；去除空字符串
    return split


# 去除前后两行，划分单词和空格
def word_split(tex_dir):
    # 遍历指定目录下的所有 .tex 文件
    target_all = []
    i = 0
    files = os.listdir(tex_dir)
    files.sort()  # 顺序读取

    for file in files:
        # print(file)
        file_path = os.path.join(tex_dir, file)
        with open(file_path, 'r') as f:
            content = f.readlines()
            split = tex_split(content)
            target_all.append(split)
            # print(target_all)
            # break
            i += 1
    # 保存合并后的二维列表到文件
    with open('target_all.pkl', 'wb') as f:
        pickle.dump(target_all, f)
    print(f"{i} tex files processed.")

#
# tex_dir = '../../data/diagramCode/'
# word_split(tex_dir)
# # 从文件中读取合并后的二维列表
# with open('target_all.pkl', 'rb') as f:
#     loaded_list = pickle.load(f)
# # 打印读取到的二维列表
# print(loaded_list[0])
