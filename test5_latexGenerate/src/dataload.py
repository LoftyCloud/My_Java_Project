# 数据加载
import os
import pickle

import torchvision.transforms as transforms
from PIL import Image
from torch.utils.data import Dataset

preprocess = transforms.Compose([
    transforms.ToTensor(),  # 转换为张量
    transforms.Normalize(mean=[0.5], std=[0.5]),  # 标准化
])


# 生成dataset类
class ImageTextDataset(Dataset):
    def __init__(self, image_folder):
        self.image_folder = image_folder
        with open('dataprocess/tensor_all.pkl', 'rb') as f:
            self.text = pickle.load(f)

    def __len__(self):
        return len(self.text)

    def __getitem__(self, index):
        filenames = os.listdir(self.image_folder)

        image_path = os.path.join(self.image_folder, filenames[index])
        img = Image.open(image_path).convert('L')  # 转为单通道图片
        # 正则化
        input_tensor = preprocess(img)
        text_tensor = self.text[index]
        return input_tensor, text_tensor

    # def calculate_bleu(self, reference, hypothesis):
    #     # 计算BLEU分数，hypothesis为模型预测的序列
    #     reference = [reference.split()]
    #     hypothesis = hypothesis.split()
    #     return sentence_bleu(reference, hypothesis)

