from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=20):
    """
    压缩指定文件夹中的图片

    :param input_folder: 包含原始图片的文件夹路径
    :param output_folder: 压缩后图片保存的文件夹路径
    :param quality: 图片质量（0-100之间的整数，数值越低质量越差）
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                img = Image.open(input_path)
                img.save(output_path, optimize=True, quality=quality)
            except Exception as e:
                print(f"无法压缩文件 {filename}: {str(e)}")

if __name__ == "__main__":
    input_folder = "./blog-imgs"  # 替换为你的输入文件夹路径
    output_folder = "./blog-imgs-compress"  # 替换为你的输出文件夹路径
    quality = 50  # 压缩质量，可以根据需要进行调整

    compress_images(input_folder, output_folder, quality)
