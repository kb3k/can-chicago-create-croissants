#!/usr/bin/python3

from PIL import Image

image = Image.open('croissant_toolarge.jpg')
new_image = image.resize((400, 400))
new_image.save('croissant.jpg')

print('image resized successfully;', image.size)

