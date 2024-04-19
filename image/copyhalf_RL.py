import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

# 選擇文件
def pickAFile():
    root = tk.Tk()
    root.withdraw()  # 隱藏根視窗
    file_path = filedialog.askopenfilename()  # 打開檔案對話框並取得選擇的檔案路徑
    root.destroy()  # 關閉根視窗
    return file_path

# 取得所有像素
def getPixels(image):
    width, height = image.size
    return [image.getpixel((x, y)) for y in range(height) for x in range(width)]

# 取得像素的顏色
def getColor(pixel):
    return pixel  # 在Pillow中，像素本身就是顏色值的元組

# 设置像素的颜色
def setColor(image, x, y, color):
    image.putpixel((x, y), color)

# 將圖片的一半複製到另一半
def copyHalf(image):
    width, height = image.size
    pixels = getPixels(image)
    for y in range(height):
        for x in range(width // 2):
            color = getColor(pixels[y * width + x])
            setColor(image, width - 1 - x, y, color)
    return image

if __name__ == "__main__":
    filepath = pickAFile()  # 使用者選擇文件
    if filepath:
        picture = Image.open(filepath)  # 打開圖片
        modified_picture = copyHalf(picture)  # 複製圖片的一半
        # 动态获取用户的桌面路径
        home_folder = os.path.expanduser('~')  # 取得主目錄路徑
        save_path = os.path.join(home_folder, 'Desktop', 'rl.png')  # 建構保存路徑
        modified_picture.save(save_path)  # 儲存修改後的圖片
        modified_picture.show()  # 顯示修改後的圖片

