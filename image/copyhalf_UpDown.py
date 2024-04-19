import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os  # 導入 os 模組用於路徑操作

# 选择文件
def pickAFile():
    root = tk.Tk()
    root.withdraw()  # 隐藏根窗口
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

# 將圖片的上半部分複製到下半部分
def copyUpperHalf(image):
    width, height = image.size
    pixels = getPixels(image)
    for y in range(height // 2):
        for x in range(width):
            color = getColor(pixels[y * width + x])
            setColor(image, x, height - 1 - y, color)
    return image

if __name__ == "__main__":
    filepath = pickAFile()  # 使用者選擇文件
    if filepath:
        picture = Image.open(filepath)  # 打開圖片
        modified_picture = copyUpperHalf(picture)  # 複製圖片的上半部分到下半部分
        
        # 動態取得使用者的桌面路徑並儲存文件
        home_folder = os.path.expanduser('~')  # 取得主目錄路徑
        save_path = os.path.join(home_folder, 'Desktop', 'UP.png')  # 建構保存路徑
        modified_picture.save(save_path)  # 儲存修改後的圖片
        
        modified_picture.show()  # 顯示修改後的圖片
