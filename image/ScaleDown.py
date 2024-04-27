from PIL import Image
from tkinter import filedialog, Tk
import os

def pickAFile():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()  
    root.destroy()  
    return file_path

def scaleDown(image):
    width, height = image.size  
    new_width = width // 2
    new_height = height // 2

    
    new_image = Image.new('RGB', (new_width, new_height))
    original_pixels = image.load()  
    new_pixels = new_image.load()  
    targetX = 0
    
    for x in range(0, width, 2):
        targetY = 0
        for y in range(0, height, 2):
            
            new_pixels[targetX, targetY] = original_pixels[x, y]
            targetY += 1
        targetX += 1

    return new_image

if __name__ == "__main__":
    filepath = pickAFile()  

    if filepath:
        with Image.open(filepath) as img:
            scaled_image = scaleDown(img)
            scaled_image.show()  
