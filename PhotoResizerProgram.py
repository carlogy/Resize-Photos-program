import os
from PIL import Image 
# Paste the folder path that houses the photo(s) you wish to resize right after the = of the line below.
folder = 'usr/example/folder/path'
print(folder)
# enter the name of the image in place of 'image1.jpg'.
try:
    image_path = os.path.join(folder, 'image1.jpg')
    image = Image.open(image_path)
    original_size = image.size
except OSError:
    print("Image unable to open")
    quit()

# Makes a copy of the original
copy = image.copy()

print(original_size)

# Resizes if image is larger than 500 x 500

if original_size > (500, 500) :
    print("Original Dimensions:" , original_size)
    # sets the max size and make a copy of the image
    max_size = (400, 400)
    copy.thumbnail(max_size)    
    # creates a new file name from the base name, the new max size, and the original file extension
    new_filename = os.path.splitext(os.path.basename(image_path))[0] + '_400' + os.path.splitext(image_path)[1]
    # saves the new image
    copy.save(new_filename)
    # prints a confirmation
    print(copy, "has been resized")

    




   



