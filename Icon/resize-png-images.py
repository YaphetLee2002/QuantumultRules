import os
from PIL import Image


def resize_images(input_folder, output_folder, target_size):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            # 打开图片
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                # 调整图片大小
                resized_img = img.resize(target_size, Image.LANCZOS)

                # 保存调整后的图片
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)
                print(f"已处理: {filename}")


# 设置参数
input_folder = 'Flag-icon'  # 输入文件夹路径
output_folder = 'Flag-icon-resized'  # 输出文件夹路径
target_size = (144, 144)  # 目标尺寸

# 执行图片调整
resize_images(input_folder, output_folder, target_size)
print("所有图片处理完成!")
