from tkinter import filedialog, Tk
from PIL import Image

def pickAFile():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()  
    root.destroy()  
    return file_path

def edge_detection(image):
    width, height = image.size
    new_image = Image.new("RGB", (width, height))
    
    for x in range(width - 1):
        for y in range(height - 1):
            current_pixel = image.getpixel((x, y))
            bottom_right_pixel = image.getpixel((x + 1, y + 1))
            
            sum_current = sum(current_pixel)
            sum_bottom_right = sum(bottom_right_pixel)
            
            diff = abs(sum_bottom_right - sum_current)
            # Scaling diff to fit into 0-255 range
            diff = min(255, diff * 3)
            
            new_color = (diff, diff, diff)
            new_image.putpixel((x, y), new_color)
    
    return new_image

if __name__ == "__main__":
    filepath = pickAFile()  
    if filepath:
        source_image = Image.open(filepath)  
        edged_image = edge_detection(source_image)  
        
        
        edged_image.show()
