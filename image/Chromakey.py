from tkinter import filedialog, Tk
from PIL import Image

def pickAFile():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()  
    root.destroy()  
    return file_path

def chromakey(source, bg, green_threshold=80, min_brightness=60):
    width, height = source.size
    source_pixels = source.load()  
    bg_pixels = bg.load()  

    for y in range(height):
        for x in range(width):
            px = source_pixels[x, y]
            if px[1] > green_threshold and px[1] > px[0] + 30 and px[1] > px[2] + 30 and sum(px) > min_brightness:
                source_pixels[x, y] = bg_pixels[x, y]  

if __name__ == "__main__":
    print("Select the source image:")
    source_filepath = pickAFile()
    print("Select the background image:")
    bg_filepath = pickAFile()

    if source_filepath and bg_filepath:
        source_image = Image.open(source_filepath)
        bg_image = Image.open(bg_filepath)

        
        bg_image = bg_image.resize(source_image.size)

        chromakey(source_image, bg_image)
        source_image.show()  
