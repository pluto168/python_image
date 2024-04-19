import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk

# 選擇文件
def pickAFile():
    root = tk.Tk()
    root.withdraw()  # 隱藏root窗口
    file_path = filedialog.askopenfilename()  # 打開檔案對話框並取得選擇的檔案路徑
    return file_path

# 建立圖片對象
def makePicture(file_path):
    try:
        return Image.open(file_path)
    except Exception as e:
        print("Error opening image: ", e)
        return None

# 展示圖片並即時顯示滑鼠懸停處的RGB值
def explore(image):
    root = tk.Tk()
    root.title("Image Explorer")

    # 將PIL影像轉換為Tkinter相容的PhotoImage對象
    tk_image = ImageTk.PhotoImage(image)
    label_image = tk.Label(root, image=tk_image)
    label_image.pack()

    # RGB值和颜色展示的标签
    label_rgb = tk.Label(root, text="", bg="white", fg="black")
    label_rgb.pack(fill="x")

    label_color = tk.Label(root, bg="white", width=4, height=1)
    label_color.pack()

    # 更新滑鼠懸停處的像素訊息
    def update_pixel_info(event):
        x, y = event.x, event.y
        if x < image.width and y < image.height:
            pixel = image.getpixel((x, y))
            # 對於非 RGB 影像（如單通道或RGBA影像），我們只取前三個值
            pixel_values = pixel if isinstance(pixel, tuple) else (pixel,)
            rgb_text = " ".join(f"{channel}: {value}" for channel, value in zip("RGB", pixel_values[:3]))
            label_rgb.config(text=rgb_text)
            label_color.config(bg=f'#{pixel_values[0]:02x}{pixel_values[1]:02x}{pixel_values[2]:02x}')

    # 綁定滑鼠移動事件
    label_image.bind("<Motion>", update_pixel_info)

    # 開始Tkinter事件循環
    root.mainloop()

if __name__ == "__main__":
    filepath = pickAFile()  # 使用者選擇文件
    if filepath:
        pic = makePicture(filepath)  # 建立圖片對象
        if pic:
            explore(pic)  # 顯示並探索圖片
        else:
            print("Failed to make a picture from the file.")
    else:
        print("No file was selected.")
