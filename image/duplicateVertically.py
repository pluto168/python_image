import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os


def pickAFile():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()  
    root.destroy()  
    return file_path

# 將圖片複製為上下兩份
def duplicateVertically(image):
    width, height = image.size
    # 創建一個新圖像，高度是原始圖片的兩倍
    new_image = Image.new('RGB', (width, height * 2))
    # 將原圖複製到新圖的上半部分
    new_image.paste(image, (0, 0))
    # 將原圖複製到新圖的下半部分
    new_image.paste(image, (0, height))
    return new_image

if __name__ == "__main__":
    filepath = pickAFile()  
    if filepath:
        picture = Image.open(filepath)  
        duplicated_picture = duplicateVertically(picture)  
        
        # 動態取得使用者的桌面路徑並儲存文件
        home_folder = os.path.expanduser('~')  
        save_path = os.path.join(home_folder, 'Desktop', 'duplicated_image.png')  
        duplicated_picture.save(save_path)  
        
        duplicated_picture.show()  
