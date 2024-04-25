from PIL import Image
from tkinter import filedialog, Tk
import os

def pickAFile():
    # 建立和隱藏根視窗
    root = Tk()
    root.withdraw()
    # 開啟檔案選擇對話方塊並取得選定的檔案路徑
    file_path = filedialog.askopenfilename()
    # 關閉根窗口
    root.destroy()
    return file_path

def mirrorVertical(image):
    width, height = image.size
    mirrorPoint = width // 2  # 使用整數除法取得中點
    
    # 處理影像的左半部分
    for y in range(height):
        for x in range(mirrorPoint):
            # 取得左側像素的顏色
            leftPixel = image.getpixel((x, y))
            # 在右側對應位置設定相同的顏色,width是總寬度
            image.putpixel((width - x - 1, y), leftPixel)

if __name__ == "__main__":
    # 讓使用者選擇一張圖片
    image_path = pickAFile()
    
    # 確保用戶選擇了一張圖片
    if image_path:
        # 打開並處理圖像
        with Image.open(image_path) as img:
            mirrorVertical(img)
            # 展示鏡像後的圖片
            img.show()
    else:
        print("未選擇檔案。")
