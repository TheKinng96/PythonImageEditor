from PIL import Image, ImageFilter

img = Image.open('./images/astro.jpg')
# filtered_img = img.convert('L')
# resize = img.resize((400,400))
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# resize.save("thumbnail..jpg")

img.thumbnail((400,400))
img.save('thumbnail.jpg')
# resize wont consider the ratio, whilst thumbnail will