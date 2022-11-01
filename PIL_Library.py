from PIL import Image

# Locating the image
im = Image.open("C:\\Users\\ibrah\\OneDrive\\Pictures\\pexels-eva-elijas-5741827.jpg")

print(im.filename)
print(im.format)
print(im.width)
print(im.height)
print(im.info)
# Display the image
'''im.show()

# Rotate the image
im_rot = im.rotate(45)
im_rot.show()

# Filename
im.filename()

# Save the image
im_rot.save('C:\\Users\\ibrah\\OneDrive\\Pictures\\rotated_img.jpg')

# Print the size of the image
print(im.size)

# Prints the format of the image
print(im.format)

# Resize the image
width, height = im.size
im.resize((int(width/2), int(height/2)))
im.show()
print(im.size)

# Save the thumbnail of the image
im.thumbnail((250,250))
im.save('C:\\Users\\ibrah\\OneDrive\\Pictures\\thumbnail1.jpg')

# Convert image to greyscale
im.convert('L').show()

# Cropping an image
width, height = im.size
area = (0, 0, width/2, height/2)     # Values are in the form of "left, upper, right and lower"
im = im.crop(area)
im.show()

# Paste an Image on another image

img2 = Image.open("C:\\Users\\ibrah\\OneDrive\\Pictures\\portrait.jpg")
im.paste(img2, (50, 50))
im.show()'''



