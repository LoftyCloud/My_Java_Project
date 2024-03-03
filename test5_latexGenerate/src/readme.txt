src目录说明：
1、文件夹：
dataprocess：数据处理相关
model：训练得到的模型

2、py文件：
cnnEncoder：自定义卷积神经网络编码器
dataload：dataset类，方便使用dataloader加载
decoder：编码器GRU（LSTM变体）
model：Encoder-Decoder
model_train：训练并保存模型
resnet——encoder：使用预训练模型resnet对图像进行编码（未使用：out of memory）
test：开发过程中的测试处，无实际作用
val：加载模型并进行验证