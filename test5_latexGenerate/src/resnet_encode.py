# 使用预训练模型对照片进行编码，并保存 (没有用上：out of memory)
from os import listdir
from tkinter import Image

import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from pickle import dump

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小为224x224像素
    transforms.ToTensor(),  # 转换为张量
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # 标准化
])
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # cuda:0


def extract_features(directory):
    # 加载预训练的ResNet模型
    resnet = models.resnet18(pretrained=True)
    # 最后一层为分类层，删除该层
    resnet = torch.nn.Sequential(*list(resnet.children())[:-2])
    if torch.cuda.is_available():
        resnet = resnet.to(device)
    # print(resnet)
    features = dict()
    for name in listdir(directory):
        filename = directory + '/' + name
        # 加载图像并进行预处理
        image = Image.open(filename)
        input_tensor = preprocess(image).unsqueeze(0)  # 增加一个维度作为批量维度
        if torch.cuda.is_available():
            # 将张量移动到GPU上
            input_tensor = input_tensor.to(device)
        # 运行输入图像通过模型
        output = resnet(input_tensor)
        image_id = name.split('.')[0]
        # 保存特征
        features[image_id] = output
        print('>%s' % name)
    return features


# 提取特征
directory = "../data/diagram"
features = extract_features(directory)
print('Extracted Features: %d' % len(features))
# 'wb'表示以二进制模式写入文件
dump(features, open('features_resnet.pkl', 'wb'))
