import sys
import os
from PIL import Image

# grab first and second argument

input_path = sys.argv[1]
output_path = sys.argv[2]

# if the output folder does not exist - it creates it
try:
    os.mkdir(os.getcwd() + '\\' + output_path)
    print(f'The output folder - {output_path}, has been created!')
except FileExistsError:
    print(
        f'The folder {output_path} already exists! All the PNG files will be saved in it! \n')

# loops through the InputJPG
for filename in os.listdir(input_path):
    current_img = Image.open(input_path + '\\' + filename)
    print(current_img.format, current_img.size, current_img.mode)
    # coverts the images to PNG + saves to the output folder
    current_img.save('.\\' + output_path + '\\' + filename + '.png', 'PNG')
