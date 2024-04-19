import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

# 选择文件
def pickAFile():
    root = tk.Tk()
    root.withdraw()  # 隐藏根窗口
    file_path = filedialog.askopenfilename()  # 打开文件对话框并获取选择的文件路径
    root.destroy()  # 关闭根窗口
    return file_path

# 获取所有像素
def getPixels(image):
    width, height = image.size
    return [image.getpixel((x, y)) for y in range(height) for x in range(width)]

# 获取像素的颜色
def getColor(pixel):
    return pixel  # 在Pillow中，像素本身就是颜色值的元组

# 设置像素的颜色
def setColor(image, x, y, color):
    image.putpixel((x, y), color)

# 将图片的一半复制到另一半
def copyHalf(image):
    width, height = image.size
    pixels = getPixels(image)
    for y in range(height):
        for x in range(width // 2):
            color = getColor(pixels[y * width + x])
            setColor(image, width - 1 - x, y, color)
    return image

if __name__ == "__main__":
    filepath = pickAFile()  # 用户选择文件
    if filepath:
        picture = Image.open(filepath)  # 打开图片
        modified_picture = copyHalf(picture)  # 复制图片的一半
        # 动态获取用户的桌面路径
        home_folder = os.path.expanduser('~')  # 获取主目录路径
        save_path = os.path.join(home_folder, 'Desktop', 'rl.png')  # 构建保存路径
        modified_picture.save(save_path)  # 保存修改后的图片
        modified_picture.show()  # 显示修改后的图片

