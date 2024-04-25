from PIL import Image
from tkinter import filedialog, Tk
import os

def pickAFile():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()  
    root.destroy()  
    return file_path

def mirrorDiagonal(image):
    width, height = image.size
    pixels = image.load()

    
    for y in range(height):
        for x in range(y):  # 保持x小於y，僅處理對角線左側的像素
            # 取得左側的像素並複製到右側對應位置
            original_pixel = pixels[x, y]
            pixels[y, x] = original_pixel  # 將左側像素複製到右側

if __name__ == "__main__":
    filepath = pickAFile()  

    if filepath:
        with Image.open(filepath) as img:
            mirrorDiagonal(img)
            img.show()  
