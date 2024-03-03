import cv2
from pdf2image import convert_from_path
import os

# 将PDF文件转换为图片
pdf_dir = 'E:/TeXworkspace/diagramPdf'
output_dir = 'E:/TeXworkspace/diagram/'

# 遍历指定目录下的所有 .pdf 文件
num = 0
for root, dirs, files in os.walk(pdf_dir):
    for file in files:
        if file.endswith('.pdf'):
            print(num)
            if num < 470:
                num += 1
                continue
            num += 1

            pdf_file = os.path.join(root, file)
            # 使用文件名（去除扩展名）作为输出文件名
            output_name = os.path.splitext(file)[0]

            output_png = os.path.join(output_dir, output_name + ".png")
            images = convert_from_path(pdf_file)

            # 遍历图片并保存
            for i, image in enumerate(images):
                image.save(f'{output_png}', 'PNG')
                image = cv2.imread(output_png)
                # 将图像转换为灰度图
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # 使用Canny边缘检测算法检测图像边缘
                edges = cv2.Canny(gray, threshold1=50, threshold2=100)
                # 查找轮廓
                contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # 找到最大的轮廓
                max_contour = max(contours, key=cv2.contourArea)
                # 获取轮廓的边界框
                x, y, width, height = cv2.boundingRect(max_contour)
                # lenth = len(contours)
                # x1, y1, width, height = cv2.boundingRect(contours[1])
                # x2, y2, width, height = cv2.boundingRect(contours[-1])
                # 裁剪图像
                # cropped_image = image[y1-150:y2 + 275, x1-100:x2 + 300]
                cropped_image = image[y - 250:y + height + 225, x - 300:x + width + 350]
                cropped_image = cv2.resize(cropped_image, (270, 200))
                # 保存裁剪后的图像到输出目录
                cv2.imwrite(output_png, cropped_image)
        break
