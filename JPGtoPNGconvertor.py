import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}')
    base_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{base_name}.png','png')
    print(f'{base_name} DONE!')
