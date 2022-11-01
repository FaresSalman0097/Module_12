# pip install pillow

from PIL import Image

input_image = Image.open("C:\\Users\\ibrah\\OneDrive\\Pictures\\pexels-eva-elijas-5741827.jpg")
width, height = input_image.size
for i in range(width // 2):
    for j in range(height):
        print(input_image.getpixel((i, j)))

