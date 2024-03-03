共3884个样本数据

这个目录下的4个python文件是前期用来处理数据的，它们的功能分别如下：
1、latexExtract ： 从tex文件中提取包含\xymatric块的内容，并存为新的tex文件
2、tex2pdf ：为每个tex文件构建命令，使其编译为交换图pdf文件
3、pdf2png ：tex只能编译为pdf，这个py文件将pdf转为png并利用边缘检测对图像进行了裁剪
4、texProcess : 这个文件对tex代码进行了处理，对单词进行了划分并保存为target_all.txt文件
5、vocab类 ： 里面对划分的词元进行统计和计数，对词元进行了编码
6、vocab2index : 将词元变为索引，并保存为tensor_all.pkl

1、target_all.pkl : 使用以下代码进行读取，其中存储了一个二位列表，方便根据整理后的tex代码建立vocab类
with open('dataprocess/target_all.pkl', 'rb') as f:
    target_all = pickle.load(f)
2、tensor_all.pkl : 将词元序列全部替换为索引序列，添加终止符，进行了截断和填充