from tkinter import filedialog, Tk
from PIL import Image

def pickAFile():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()
    root.destroy()  
    return file_path

def getPixel(image, x, y):
    return image.getpixel((x, y))

def setColor(image, x, y, color):
    image.putpixel((x, y), color)

def distance(color1, color2):
    # 计算兩個顏色之間的歐幾裡得距離
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
    filepath = pickAFile()  
    if filepath:
        picture = Image.open(filepath)  
        modified_picture = changeWhiteToBlue(picture)  # 修改指定顏色
        
        modified_picture.show()  
