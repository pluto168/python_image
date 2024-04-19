from tkinter import filedialog, Tk
from PIL import Image

def pickAFile():
    root = Tk()
    root.withdraw()  # 隐藏根窗口
    file_path = filedialog.askopenfilename()  # 打开文件对话框并获取选择的文件路径
    root.destroy()  # 关闭根窗口
    return file_path

def getPixel(image, x, y):
    return image.getpixel((x, y))

def setColor(image, x, y, color):
    image.putpixel((x, y), color)

def distance(color1, color2):
    # 计算两个颜色之间的欧几里得距离
    return sum((component1 - component2) ** 2 for component1, component2 in zip(color1, color2)) ** 0.5

def changeWhiteToBlue(image):
    white = (255, 255, 255)
    blue = (0, 0, 255)
    for x in range(140, 450):
        for y in range(35, 320):
            pixel = getPixel(image, x, y)
            if distance(pixel, white) < 150:
                setColor(image, x, y, blue)
    return image

if __name__ == "__main__":
    filepath = pickAFile()  # 用户选择文件
    if filepath:
        picture = Image.open(filepath)  # 打开图片
        modified_picture = changeWhiteToBlue(picture)  # 修改指定颜色
        
        # 保存修改后的图片
        modified_picture.show()  # 显示修改后的图片
