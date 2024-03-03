## 批量将提取后的tex文件编译为pdf文件
import os
import subprocess


def compile_tex_to_png(tex_file, pdf_output_dir, output_name):
    # 构造输出文件的路径
    output_pdf = os.path.join(pdf_output_dir)
    # 构造编译命令
    command1 = ['D:\\MiKTeX\\miktex\\bin\\x64\\pdflatex.exe', '-interaction', 'nonstopmode', '-output-directory', output_pdf, tex_file]
    # 调用命令行工具进行编译
    subprocess.run(command1)


def batch_compile_tex_files(tex_dir, pdf_output_dir):
    # 遍历指定目录下的所有 .tex 文件
    for root, dirs, files in os.walk(tex_dir):
        for file in files:
            if file.endswith('.tex'):
                tex_file = os.path.join(root, file)
                # 使用文件名（去除扩展名）作为输出文件名
                output_name = os.path.splitext(file)[0]
                compile_tex_to_png(tex_file, pdf_output_dir, output_name)
                # break


# 调用示例
tex_dir = 'E:/TeXworkspace/diagramCode'
pdf_output_dir = 'E:/TeXworkspace/diagramPdf'
# png_output_dir = "E:/TeXworkspace/diagram"
# output_size = 'a4paper'  # 设置 PDF 文件大小，可选
batch_compile_tex_files(tex_dir, pdf_output_dir)
