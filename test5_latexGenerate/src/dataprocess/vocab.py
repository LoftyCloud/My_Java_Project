# 文本词表类，支持查询词表长度、通过索引查询词元、词元查询索引
# 统计词元的频率，返回每个词元及其出现的次数，以一个字典形式返回。
import collections
import pickle


def count_corpus(tokens):
    # 这里的tokens是一个1D列表或者是2D列表
    if len(tokens) == 0 or isinstance(tokens[0], list):
        # 将词元列表展平为一个列表
        tokens = [token for line in tokens for token in line]
    # 该方法用于统计某序列中每个元素出现的次数，以键值对的方式存在字典中。
    return collections.Counter(tokens)


class Vocab:
    def __init__(self, tokens=None, min_freq=0, reserved_tokens=None):
        if tokens is None:
            tokens = []
        if reserved_tokens is None:
            reserved_tokens = []

        # 按照单词出现频率排序
        counter = count_corpus(tokens)

        # counter.items():为一个字典

        # lambda x:x[1]:对第二个字段进行排序
        # reverse = True:降序
        self._token_freqs = sorted(counter.items(), key=lambda x: x[1], reverse=True)  # 排序

        # 未知单词的索引为0
        # idx_to_token用于保存所有未重复的词元
        self.idx_to_token = ['<unk>'] + reserved_tokens
        # token_to_idx:是一个字典，保存词元和其对应的索引，token: idx
        self.token_to_idx = {token: idx for idx, token in enumerate(self.idx_to_token)}

        for token, freq in self._token_freqs:
            # min_freq为最小出现的次数，如果小于这个数，这个单词被抛弃
            if freq < min_freq:
                break
            # 如果这个词元未出现在词表中，将其添加进词表
            if token not in self.token_to_idx:
                self.idx_to_token.append(token)
                # 因为第一个位置被位置单词占据
                self.token_to_idx[token] = len(self.idx_to_token) - 1

    # 返回词表的长度
    def __len__(self):
        return len(self.idx_to_token)

    # 获取要查询词元的索引，支持list，tuple查询多个词元的索引
    def __getitem__(self, tokens):
        if not isinstance(tokens, (list, tuple)):
            # self.unk：如果查询不到返回0
            return self.token_to_idx.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]

    # 根据索引查询词元，支持list，tuple查询多个索引对应的词元
    def to_tokens(self, indices):
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]

    @property
    def unk(self):
        return 0

    @property
    def token_freqs(self):
        return self._token_freqs


# with open('target_all.pkl', 'rb') as f:
#     target = pickle.load(f)
# counter = count_corpus(target)
# print(f"词表里共{len(counter)}个词元")  # 1492,共1492个词被收入词典并编码
#
# src_vocab = Vocab(target, min_freq=5, reserved_tokens=['<pad>', '<bos>', '<eos>'])
# # 返回前十个词元及其对应的索引
# print("前十个词元及其对应的索引:")
# print(list(src_vocab.token_to_idx.items())[:10])