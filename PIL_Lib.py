from PIL import Image

img_PIL = Image.open("C:\\Users\\ibrah\\OneDrive\\Pictures\\1.jpg")
'''
# Open the image in photo viewer
img_PIL.show()

# Prints the filename
name = img_PIL.filename
print(name)

# Prints the format of the file
frmt = img_PIL.format
print("Format : ", frmt)

# Mode of the image
mde = img_PIL.mode
print("Mode : ", mde)

# Size of the image
sze = img_PIL.size
print("Size of the imege :", sze)

# Image info
inf = img_PIL.info
print("Image information : ", inf)

# Rotate the image
img = img_PIL.rotate(180)
img.show()

# Save the image
# img_PIL.save("C:\\Users\\ibrah\\OneDrive\\Pictures\\2.jpg")

# RGB values of the image
r, g, b = img_PIL.split()
print(r, g, b)
'''
# Width of the image
w = img_PIL.width
print("width : ", w)

# Height of the image
h = img_PIL.height
print("Height : ", h)
# Loading the image and see the RGB values corresponding to that pixel
rawdata = img_PIL.load()
print(rawdata[1023, 767])

#
for i in range(w // 2, w):
    for j in range(h // 2):
        rawdata[i, j] = (213, 191, 174)

for i in range(w//2):
    for j in range(h//2, h):
        rawdata[i, j] = (107, 146, 144)

# Coverting to greyscale
for i in range(w//2, w):
    for j in range(h//2, h):
        r, g, b = img_PIL.getpixel((i, j))
        gs = (0.299 * r + 0.587 * g + 0.114 * b)   # This is the universal formula for coverting color image to greyscale
        rawdata[i, j] = (int(gs), int(gs), int(gs))

img_PIL.save("C:\\Users\\ibrah\\OneDrive\\Pictures\\3.jpg")