import sys
import os
import rawpy
import imageio

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(image_folder):
    raw = rawpy.imread(f'{image_folder}/{file}')
    thumb = raw.extract_thumb()
    base_name = os.path.splitext(file)[0]
if thumb.format == rawpy.ThumbFormat.JPEG:
    f = open(f'{output_folder}/{base_name}.jpeg', 'wb')
    f.write(thumb.data)
elif thumb.format == rawpy.ThumbFormat.BITMAP:
    imageio.imsave(f'{output_folder}/{base_name}.jpeg', thumb.data)