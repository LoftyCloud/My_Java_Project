import os
import re
# 提取latex代码中的\xymatrix块并保存

# 定义目录路径和正则表达式模式
directory = 'E:/TeXworkspace/book'
new_directory = 'E:/TeXworkspace/diagramCode'
pattern = r'\$\$\n*\\xymatrix{.*?}\n*\$\$'

# 创建新文件的模板内容
template_start = r'\documentclass{article} \usepackage[all]{xy} \begin{document}'
template_end = r'\end{document}'

# 遍历目录中的文件
for filename in os.listdir(directory):
    # print(filename)
    if filename.endswith('.tex'):
        # 构建文件的完整路径
        filepath = os.path.join(directory, filename)

        # 打开文件进行读取
        with open(filepath, 'r') as file:
            # 读取文件内容
            contents = file.read()

            # 使用正则表达式搜索xymatrix块
            matches = re.findall(pattern, contents, re.DOTALL)

            if matches:
                for i, match in enumerate(matches):
                    # 创建新文件名
                    new_filename = f'{i}_{filename}'
                    new_filepath = os.path.join(new_directory, new_filename)

                    # 写入新文件
                    with open(new_filepath, 'w') as new_file:
                        # 写入模板开头
                        new_file.write(template_start)
                        new_file.write('\n')

                        # 写入xymatrix块
                        new_file.write(match)
                        new_file.write('\n')

                        # 写入模板结尾
                        new_file.write(template_end)
                        new_file.write('\n')

                print(f"Found {len(matches)} xymatrix block(s) in {filename}.")
